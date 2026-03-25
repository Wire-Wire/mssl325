"""
CLI entry point — run 1–2 pilot encounters end-to-end.

Phase 1.5: supports both synthetic and live THEMIS/OMNI data sources
via the DataProvider abstraction.

Usage:
    python -m pdl_pilot.cli.run_pilot --config configs/pilot_themis.yaml
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

import numpy as np

from pdl_pilot.config import load_config
from pdl_pilot.provenance import ProvenanceTracker
from pdl_pilot.data.provider import DataProvider, EncounterData
from pdl_pilot.data.synthetic_provider import SyntheticProvider
from pdl_pilot.encounter.model import Encounter, UpstreamSummary, MappingResult
from pdl_pilot.mapping import compute_s_with_uncertainty, compute_bin_occupancy
from pdl_pilot.metrics import compute_metrics
from pdl_pilot.qc import generate_qc_report, compute_qc_flags

log = logging.getLogger(__name__)


def _build_provider(config) -> DataProvider:
    """Instantiate the appropriate DataProvider based on config.data_source."""
    if config.data_source in ("synthetic", "fixture"):
        return SyntheticProvider(seed=config.random_seed)
    elif config.data_source == "live":
        from pdl_pilot.data.live_provider import LiveProvider
        return LiveProvider(config.live)
    else:
        raise ValueError(f"Unknown data_source: {config.data_source!r}")


def _build_upstream(edata: EncounterData, data_source: str) -> UpstreamSummary:
    """Build UpstreamSummary from EncounterData.

    For synthetic: use hardcoded defaults (as in Phase 1).
    For live: use OMNI time-series medians.
    """
    if data_source in ("synthetic", "fixture"):
        return UpstreamSummary(
            bz_gsm_nT=2.0, bt_nT=5.0, cone_angle_deg=45.0,
            clock_angle_deg=30.0, dp_nPa=2.0, mach_alfven=8.0,
            stability_flag="stable",
        )

    # Live: compute from OMNI arrays
    def _nanmed(arr):
        if arr is None or len(arr) == 0:
            return None
        v = float(np.nanmedian(arr))
        return v if np.isfinite(v) else None

    bz = _nanmed(edata.omni_bz_gsm_nT)
    bt = _nanmed(edata.omni_bt_nT)
    dp = _nanmed(edata.omni_dp_nPa)
    ma = _nanmed(edata.omni_mach_alfven)

    # Cone/clock angle from Bz/Bt
    cone_angle = None
    clock_angle = None
    if bz is not None and bt is not None and bt > 0:
        cone_angle = float(np.degrees(np.arccos(np.clip(abs(bz) / bt, 0, 1))))
        clock_angle = float(np.degrees(np.arctan2(abs(bz), bt)))

    # Stability: coefficient of variation of Dp
    stability = "unknown"
    if edata.omni_dp_nPa is not None:
        valid = edata.omni_dp_nPa[np.isfinite(edata.omni_dp_nPa)]
        if len(valid) > 5:
            cv = float(np.std(valid) / np.mean(valid)) if np.mean(valid) > 0 else 999
            stability = "stable" if cv < 0.3 else "variable"

    return UpstreamSummary(
        bz_gsm_nT=bz,
        bt_nT=bt,
        cone_angle_deg=cone_angle,
        clock_angle_deg=clock_angle,
        dp_nPa=dp if dp is not None else 2.0,
        mach_alfven=ma if ma is not None else 8.0,
        stability_flag=stability,
    )


def process_encounter(
    enc_spec,
    config,
    run_dir: Path,
    provider: DataProvider,
    tracker: ProvenanceTracker | None = None,
) -> Encounter:
    """Process one encounter through the full pipeline."""
    log.info("=== Processing encounter: %s (source: %s) ===",
             enc_spec.encounter_id, provider.name)

    # --- 1. Load data via provider ---
    edata = provider.fetch(enc_spec)

    # Record source metadata for provenance
    if tracker and edata.source_metadata:
        tracker.record_source_metadata(enc_spec.encounter_id, edata.source_metadata)

    # Use legacy dict interface for backward-compat with downstream code
    data = edata.to_legacy_dict()

    # --- 2. Build encounter shell ---
    enc = Encounter(
        encounter_id=enc_spec.encounter_id,
        spacecraft=enc_spec.spacecraft,
        probe=enc_spec.probe,
        time_start=enc_spec.time_start,
        time_end=enc_spec.time_end,
        crossing_count=enc_spec.crossing_count,
    )
    enc.time_unix = data["time_unix"]
    enc.density_cm3 = data["density_cm3"]
    enc.bmag_nT = data["bmag_nT"]
    enc.beta = data["beta"]
    enc.ptot_nPa = data["ptot_nPa"]
    enc.vflow_kms = data["vflow_kms"]

    # Position metadata
    enc.position_gsm_re = (
        float(np.nanmean(data["x_gsm_re"])),
        float(np.nanmean(data.get("y_gsm_re", np.zeros(1)))),
        float(np.nanmean(data.get("z_gsm_re", np.zeros(1)))),
    )

    # MLT and SZA — simplified geometry for now
    x, y, z = enc.position_gsm_re
    enc.abs_z_re = abs(z)
    if np.isfinite(x) and np.isfinite(y):
        enc.mlt_hours = float((12.0 + np.degrees(np.arctan2(y, x)) / 15.0) % 24.0)
        enc.sza_deg = float(np.degrees(np.arctan2(
            np.sqrt(y**2 + z**2), x
        )))
    else:
        enc.mlt_hours = 12.0
        enc.sza_deg = 0.0

    # --- 3. Upstream summary ---
    enc.upstream = _build_upstream(edata, config.data_source)

    # Quality notes from live data
    if edata.quality_notes:
        log.info("Data quality notes: %s", edata.quality_notes)

    # --- 4. s-mapping ---
    dp_for_mapping = enc.upstream.dp_nPa if enc.upstream.dp_nPa is not None else 2.0
    bz_for_mapping = enc.upstream.bz_gsm_nT if enc.upstream.bz_gsm_nT is not None else 0.0
    ma_for_mapping = enc.upstream.mach_alfven if enc.upstream.mach_alfven is not None else 8.0

    s_nom, s_lo, s_hi, mp0, bs0 = compute_s_with_uncertainty(
        data["x_gsm_re"],
        dp_nPa=dp_for_mapping,
        bz_nT=bz_for_mapping,
        mach_alfven=ma_for_mapping,
        unc=config.uncertainty,
    )
    occupancy = compute_bin_occupancy(s_nom, config.bins)

    # Sanity: all s in [0,1], not all identical
    s_ok = bool(np.all((s_nom >= 0) & (s_nom <= 1)) and np.nanstd(s_nom) > 0.01)

    enc.mapping = MappingResult(
        mp_model=config.boundary_models.magnetopause,
        bs_model=config.boundary_models.bow_shock,
        mp_standoff_re=mp0,
        bs_standoff_re=bs0,
        s_array=s_nom,
        s_sanity_ok=s_ok,
        s_uncertainty_lo=s_lo,
        s_uncertainty_hi=s_hi,
        occupancy=occupancy,
        model_inputs={
            "dp_nPa": dp_for_mapping,
            "bz_nT": bz_for_mapping,
            "mach_alfven": ma_for_mapping,
        },
    )
    log.info("s-mapping: MP=%.2f Re  BS=%.2f Re  occupancy=%s",
             mp0, bs0, occupancy)

    # --- 5. Metrics ---
    cadence = float(np.nanmedian(np.diff(enc.time_unix)))
    bundle, n_trend, b_trend, n_resid, b_resid = compute_metrics(
        s_nom, enc.density_cm3, enc.bmag_nT, enc.beta, enc.ptot_nPa,
        config.bins, config.filters, cadence,
    )
    enc.metrics = bundle
    enc.density_trend = n_trend
    enc.bmag_trend = b_trend
    enc.density_residual = n_resid
    enc.bmag_residual = b_resid

    # --- 6. QC flags ---
    enc.qc = compute_qc_flags(enc, n_resid, enc.vflow_kms)

    # --- 7. QC report ---
    qc_path = generate_qc_report(enc, run_dir, config.bins)
    enc.artifact_paths["qc_report"] = str(qc_path)

    # --- 8. Save encounter JSON ---
    enc_path = run_dir / f"encounter_{enc.encounter_id}.json"
    enc.save_json(enc_path)
    enc.artifact_paths["encounter_json"] = str(enc_path)
    log.info("Encounter saved → %s", enc_path)

    return enc


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="PDL Pilot — Phase-1/1.5 encounter pipeline"
    )
    parser.add_argument(
        "--config", required=True, help="Path to YAML config file."
    )
    args = parser.parse_args(argv)

    config = load_config(args.config)
    tracker = ProvenanceTracker(config)
    tracker.freeze_config()

    log.info("PDL Pilot run started — run_id=%s", tracker.run_id)
    log.info("Config hash: %s", config.config_hash())
    log.info("Data source: %s", config.data_source)
    log.info("Encounters to process: %d", len(config.encounters))

    # Build the data provider
    provider = _build_provider(config)
    log.info("Data provider: %s", provider.name)

    # Record cache summary if live
    if config.data_source == "live":
        from pdl_pilot.data.cache import DataCache
        cache = DataCache(config.live.cache_dir, config.live.cache_policy)
        tracker.record_cache_summary(cache.summary())

    results: list[dict] = []
    for spec in config.encounters:
        enc = process_encounter(spec, config, tracker.run_dir, provider, tracker)
        results.append(enc.to_summary_dict())

    # Update cache summary after all fetches
    if config.data_source == "live":
        from pdl_pilot.data.cache import DataCache
        cache = DataCache(config.live.cache_dir, config.live.cache_policy)
        tracker.record_cache_summary(cache.summary())

    # Write combined results
    combined = tracker.run_dir / "all_encounters.json"
    with open(combined, "w") as f:
        json.dump(results, f, indent=2, default=str)

    tracker.write_manifest(extra={"n_encounters_processed": len(results)})
    log.info("Run complete. Output → %s", tracker.run_dir)


if __name__ == "__main__":
    main()
