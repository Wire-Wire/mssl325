"""
CLI entry point — run 1–2 pilot encounters end-to-end.

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
from pdl_pilot.data.synthetic import generate_synthetic_encounter
from pdl_pilot.encounter.model import Encounter, UpstreamSummary, MappingResult
from pdl_pilot.mapping import compute_s_with_uncertainty, compute_bin_occupancy
from pdl_pilot.metrics import compute_metrics
from pdl_pilot.qc import generate_qc_report, compute_qc_flags

log = logging.getLogger(__name__)


def process_encounter(enc_spec, config, run_dir: Path) -> Encounter:
    """Process one encounter through the full Phase-1 pipeline."""
    log.info("=== Processing encounter: %s ===", enc_spec.encounter_id)

    # --- 1. Load data ---
    if config.data_source in ("synthetic", "fixture"):
        data = generate_synthetic_encounter(enc_spec, seed=config.random_seed)
    else:
        raise NotImplementedError(
            "Live data loading requires pyspedas. Set data_source='synthetic'."
        )

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

    # Position metadata (synthetic: subsolar)
    enc.position_gsm_re = (
        float(np.mean(data["x_gsm_re"])),
        float(np.mean(data.get("y_gsm_re", np.zeros(1)))),
        float(np.mean(data.get("z_gsm_re", np.zeros(1)))),
    )
    enc.mlt_hours = 12.0
    enc.sza_deg = 0.0
    enc.abs_z_re = abs(enc.position_gsm_re[2])

    # --- 3. Upstream summary (synthetic defaults) ---
    enc.upstream = UpstreamSummary(
        bz_gsm_nT=2.0, bt_nT=5.0, cone_angle_deg=45.0,
        clock_angle_deg=30.0, dp_nPa=2.0, mach_alfven=8.0,
        stability_flag="stable",
    )

    # --- 4. s-mapping ---
    s_nom, s_lo, s_hi, mp0, bs0 = compute_s_with_uncertainty(
        data["x_gsm_re"],
        dp_nPa=enc.upstream.dp_nPa,
        bz_nT=enc.upstream.bz_gsm_nT,
        mach_alfven=enc.upstream.mach_alfven,
        unc=config.uncertainty,
    )
    occupancy = compute_bin_occupancy(s_nom, config.bins)

    # Sanity: all s in [0,1], not all identical
    s_ok = bool(np.all((s_nom >= 0) & (s_nom <= 1)) and np.std(s_nom) > 0.01)

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
            "dp_nPa": enc.upstream.dp_nPa,
            "bz_nT": enc.upstream.bz_gsm_nT,
            "mach_alfven": enc.upstream.mach_alfven,
        },
    )
    log.info("s-mapping: MP=%.2f Re  BS=%.2f Re  occupancy=%s",
             mp0, bs0, occupancy)

    # --- 5. Metrics ---
    cadence = float(np.median(np.diff(enc.time_unix)))
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
        description="PDL Pilot — Phase-1 encounter pipeline"
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
    log.info("Encounters to process: %d", len(config.encounters))

    results: list[dict] = []
    for spec in config.encounters:
        enc = process_encounter(spec, config, tracker.run_dir)
        results.append(enc.to_summary_dict())

    # Write combined results
    combined = tracker.run_dir / "all_encounters.json"
    with open(combined, "w") as f:
        json.dump(results, f, indent=2, default=str)

    tracker.write_manifest(extra={"n_encounters_processed": len(results)})
    log.info("Run complete. Output → %s", tracker.run_dir)


if __name__ == "__main__":
    main()
