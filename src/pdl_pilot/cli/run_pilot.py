"""
CLI entry point — run 1–2 pilot encounters end-to-end.

Phase 1.5 hardened: supports both synthetic and live THEMIS/OMNI data sources
via the DataProvider abstraction, with fill-value masking, scientific
preflight, honest QC grading, and corrected upstream computation.

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
from pdl_pilot.data.masking import mask_fill_values, MaskingSummary
from pdl_pilot.encounter.model import Encounter, UpstreamSummary, MappingResult
from pdl_pilot.mapping import compute_s_with_uncertainty, compute_bin_occupancy
from pdl_pilot.metrics import compute_metrics
from pdl_pilot.qc import generate_qc_report, compute_qc_flags
from pdl_pilot.qc.preflight import run_preflight, PreflightConfig as PFConfig

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


def _apply_fill_masking(
    edata: EncounterData, data_source: str, policy: str = "auto"
) -> dict[str, MaskingSummary]:
    """Apply fill-value masking to encounter data arrays.

    For live data: masks OMNI sentinels and CDF fills.
    For synthetic: no-op (synthetic has no fills).

    Returns dict of variable_name → MaskingSummary.
    """
    summaries: dict[str, MaskingSummary] = {}

    if policy == "off" or data_source in ("synthetic", "fixture"):
        return summaries

    # OMNI upstream arrays
    omni_pairs = [
        ("omni_bz_gsm_nT", "BZ_GSM", "omni"),
        ("omni_bt_nT", "F", "omni"),
        ("omni_dp_nPa", "Pressure", "omni"),
        ("omni_mach_alfven", "Mach_num", "omni"),
        ("omni_flow_speed_kms", "flow_speed", "omni"),
    ]
    for attr, var_name, ds_type in omni_pairs:
        arr = getattr(edata, attr, None)
        if arr is not None:
            masked, summary = mask_fill_values(arr, var_name, dataset_type=ds_type)
            setattr(edata, attr, masked)
            summaries[var_name] = summary
            if summary.n_masked_fill > 0:
                log.info("Masked %d fill values in OMNI %s (%.1f%%)",
                         summary.n_masked_fill, var_name,
                         summary.masked_fraction * 100)

    # THEMIS encounter arrays
    themis_pairs = [
        ("density_cm3", "density", "themis_mom"),
        ("bmag_nT", "bmag", "themis_fgm"),
        ("vflow_kms", "vflow", "themis_mom"),
        ("beta", "beta", "themis_mom"),
        ("ptot_nPa", "ptot", "themis_mom"),
    ]
    for attr, var_name, ds_type in themis_pairs:
        arr = getattr(edata, attr, None)
        if arr is not None:
            masked, summary = mask_fill_values(arr, var_name, dataset_type=ds_type)
            setattr(edata, attr, masked)
            summaries[var_name] = summary

    return summaries


def compute_cone_angle(bx: float | None, bt: float | None) -> float | None:
    """Compute IMF cone angle: angle between B and Sun-Earth line.

    Correct definition: cone_angle = arccos(|Bx| / |B|)
    where Bx is the radial (Sun-Earth) component.

    This requires the radial component, NOT Bz.
    Returns degrees, or None if inputs unavailable.
    """
    if bx is None or bt is None or bt <= 0:
        return None
    ratio = min(abs(bx) / bt, 1.0)
    return float(np.degrees(np.arccos(ratio)))


def compute_clock_angle(by: float | None, bz: float | None) -> float | None:
    """Compute IMF clock angle: arctan2(By, Bz) in GSM.

    Returns degrees [0, 360), or None if inputs unavailable.
    """
    if by is None or bz is None:
        return None
    return float(np.degrees(np.arctan2(by, bz))) % 360.0


def _build_upstream(edata: EncounterData, data_source: str) -> UpstreamSummary:
    """Build UpstreamSummary from EncounterData.

    For synthetic: use hardcoded defaults (as in Phase 1).
    For live: use OMNI time-series medians with corrected cone/clock angles.

    IMPORTANT: Cone angle is arccos(|Bx|/|B|), not arccos(|Bz|/|B|).
    This requires BX_GSE from OMNI.  If unavailable, cone_angle = None.
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
        valid = arr[np.isfinite(arr)]
        if len(valid) == 0:
            return None
        return float(np.nanmedian(valid))

    bz = _nanmed(edata.omni_bz_gsm_nT)
    bt = _nanmed(edata.omni_bt_nT)
    dp = _nanmed(edata.omni_dp_nPa)
    ma = _nanmed(edata.omni_mach_alfven)

    # Cone angle: requires Bx (radial component).
    # OMNI provides BX_GSE — we store it in extra omni arrays if available.
    # For now, if we have omni_bx_gse, use it; otherwise None (honest).
    bx_gse = _nanmed(getattr(edata, "omni_bx_gse_nT", None))
    cone_angle = compute_cone_angle(bx_gse, bt)

    # Clock angle: arctan2(By, Bz) in GSM
    by_gsm = _nanmed(getattr(edata, "omni_by_gsm_nT", None))
    clock_angle = compute_clock_angle(by_gsm, bz)

    # Stability: coefficient of variation of Dp
    stability = "unknown"
    if edata.omni_dp_nPa is not None:
        valid = edata.omni_dp_nPa[np.isfinite(edata.omni_dp_nPa)]
        if len(valid) > 5:
            mean_val = float(np.mean(valid))
            cv = float(np.std(valid) / mean_val) if mean_val > 0 else 999
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

    # --- 1b. Fill-value masking (Phase 1.5 hardening) ---
    mask_policy = config.preflight.fill_masking_policy
    masking_summaries = _apply_fill_masking(edata, config.data_source, mask_policy)
    masked_fractions = {
        k: v.masked_fraction for k, v in masking_summaries.items()
    }

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
    enc.masked_fraction_summary = masked_fractions

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

    # --- 4b. Scientific preflight (Phase 1.5 hardening) ---
    pf_cfg = PFConfig(
        max_sza_deg=config.preflight.max_sza_deg,
        min_x_gsm_re=config.preflight.min_x_gsm_re,
        max_abs_y_gsm_re=config.preflight.max_abs_y_gsm_re,
        min_valid_fraction=config.preflight.min_valid_fraction,
        min_density_cm3=config.preflight.min_density_cm3,
        max_density_cm3=config.preflight.max_density_cm3,
        min_bmag_nT=config.preflight.min_bmag_nT,
        max_bmag_nT=config.preflight.max_bmag_nT,
        min_beta_sheath=config.preflight.min_beta_sheath,
        max_beta_sheath=config.preflight.max_beta_sheath,
        min_membership_fraction=config.preflight.min_membership_fraction,
        min_near_occupancy=config.preflight.min_near_occupancy,
        min_bg_occupancy=config.preflight.min_bg_occupancy,
        min_s_std=config.preflight.min_s_std,
    )

    preflight = run_preflight(
        position_gsm_re=enc.position_gsm_re,
        sza_deg=enc.sza_deg,
        occupancy=occupancy,
        s_array=s_nom,
        density=enc.density_cm3,
        bmag=enc.bmag_nT,
        beta=enc.beta,
        masked_fractions=masked_fractions,
        cfg=pf_cfg,
        bins=config.bins,
    )

    enc.scientific_status = preflight.scientific_status
    enc.evaluable = preflight.evaluable
    enc.preflight_checks = preflight.checks
    enc.preflight_reasons = preflight.reasons
    enc.evaluable_metrics = preflight.evaluable_metrics
    enc.membership_summary = preflight.membership.to_dict()

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

    # --- 6. QC flags (with honest tri-state + grading policy) ---
    grade_policy = config.preflight.grade_with_incomplete_flags
    enc.qc = compute_qc_flags(enc, n_resid, enc.vflow_kms, grade_policy)

    # --- 7. QC report ---
    qc_path = generate_qc_report(enc, run_dir, config.bins)
    enc.artifact_paths["qc_report"] = str(qc_path)

    # --- 8. Save encounter JSON ---
    enc_path = run_dir / f"encounter_{enc.encounter_id}.json"
    enc.save_json(enc_path)
    enc.artifact_paths["encounter_json"] = str(enc_path)
    log.info("Encounter saved -> %s  [status=%s, evaluable=%s]",
             enc_path, enc.scientific_status, enc.evaluable)

    return enc


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="PDL Pilot — Phase-1.5 hardened encounter pipeline"
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

    # Summary
    n_evaluable = sum(1 for r in results if r.get("evaluable", False))
    tracker.write_manifest(extra={
        "n_encounters_processed": len(results),
        "n_evaluable": n_evaluable,
    })
    log.info("Run complete. Output -> %s  (%d/%d evaluable)",
             tracker.run_dir, n_evaluable, len(results))


if __name__ == "__main__":
    main()
