"""
Window-family validation — duration-ladder sweep for seed windows.

For each seed family, generates a ladder of windows at different durations
and validates each through the existing live pipeline.  Produces a compact
comparison showing how occupancy, s-range, and metric evaluability change
with window length.

Usage:
    python -m pdl_pilot.cli.validate_families --config configs/pilot_window_families.yaml

Outputs:
    runs/<run_id>/family_summary.json   — machine-readable
    runs/<run_id>/family_summary.md     — human-readable comparison
    runs/<run_id>/family_summary.csv    — CSV for quick comparison
    runs/<run_id>/encounter_<id>.json   — per-window artifacts
    runs/<run_id>/qc_<id>.png           — QC quicklooks
"""
from __future__ import annotations

import argparse
import csv
import json
import logging
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import yaml

from pdl_pilot.config.schema import PipelineConfig, EncounterSpec, LiveDataConfig, PreflightConfig
from pdl_pilot.provenance import ProvenanceTracker
from pdl_pilot.cli.run_pilot import _build_provider, process_encounter

log = logging.getLogger(__name__)


def _load_family_config(path: str | Path) -> dict:
    """Load a window-family YAML manifest."""
    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    return raw


def _generate_window_specs(family: dict) -> list[EncounterSpec]:
    """Generate EncounterSpec list for one family's duration ladder."""
    seed_id = family["seed_id"]
    probe = family["probe"]
    center_str = family["center"]
    anchor = family.get("anchor", "centered")
    durations = family.get("durations_minutes", [30, 90, 180, 360])
    notes_base = family.get("notes", "")

    center_dt = datetime.fromisoformat(center_str)
    if center_dt.tzinfo is None:
        center_dt = center_dt.replace(tzinfo=timezone.utc)

    specs = []
    for dur in durations:
        half = timedelta(minutes=dur / 2)
        if anchor == "centered":
            t_start = center_dt - half
            t_end = center_dt + half
        elif anchor == "fixed_start":
            t_start = center_dt
            t_end = center_dt + timedelta(minutes=dur)
        elif anchor == "fixed_end":
            t_start = center_dt - timedelta(minutes=dur)
            t_end = center_dt
        else:
            t_start = center_dt - half
            t_end = center_dt + half

        eid = f"{seed_id}_{dur}m"
        spec = EncounterSpec(
            encounter_id=eid,
            spacecraft="themis",
            probe=f"th{probe[-1]}" if not probe.startswith("th") else probe,
            time_start=t_start.strftime("%Y-%m-%dT%H:%M:%S"),
            time_end=t_end.strftime("%Y-%m-%dT%H:%M:%S"),
            crossing_count=1,
            notes=f"Family {seed_id}, {dur}min window. {notes_base.strip()[:80]}",
        )
        specs.append(spec)

    return specs


def _compute_window_score(summary: dict) -> dict:
    """Score a family window for usability (same criteria as curation + occupancy emphasis)."""
    if summary.get("scientific_status") == "ERROR":
        return {"usable": False, "score": -1.0, "notes": ["Pipeline error"]}

    score = 0.0
    notes = []

    # Geometry
    sza = summary.get("sza_deg")
    if sza is not None and sza < 30:
        score += 2.0
    elif sza is not None and sza < 60:
        score += 1.0

    pos = summary.get("position_gsm_re")
    if pos and pos[0] > 8:
        score += 1.0

    # Membership
    mem = summary.get("membership_summary", {})
    mem_frac = mem.get("membership_fraction", 0)
    if mem_frac > 0.5:
        score += 1.5
    elif mem_frac > 0.3:
        score += 0.5

    # CRITICAL: near AND background occupancy (the whole point)
    occ = summary.get("mapping", {}).get("occupancy", {})
    near_occ = occ.get("near", 0)
    bg_occ = occ.get("background", 0)

    if near_occ > 0.05 and bg_occ > 0.05:
        score += 4.0  # high weight — this is what we're testing
        notes.append(f"BOTH bins populated: near={near_occ:.1%}, bg={bg_occ:.1%}")
    elif near_occ > 0.02 and bg_occ > 0.02:
        score += 2.0
        notes.append(f"Marginal occupancy: near={near_occ:.1%}, bg={bg_occ:.1%}")
    else:
        notes.append(f"Missing bin occupancy: near={near_occ:.1%}, bg={bg_occ:.1%}")

    # s-range spread
    s_stats = summary.get("mapping", {}).get("s_stats", {})
    s_range = s_stats.get("max", 0) - s_stats.get("min", 0) if s_stats else 0
    if s_range > 0.5:
        score += 2.0
    elif s_range > 0.3:
        score += 1.0
    elif s_range > 0.1:
        score += 0.3

    # Metrics evaluable
    metrics = summary.get("metrics", {})
    n_metrics = sum(1 for k in ("Dn", "EB", "delta_beta", "rho_nB_trend")
                    if metrics.get(k) is not None)
    score += n_metrics * 0.5

    usable = (near_occ > 0.02 and bg_occ > 0.02 and
              mem_frac > 0.3 and
              summary.get("scientific_status") not in ("ERROR", "FAIL_GEOMETRY"))

    return {"usable": usable, "score": round(score, 2), "notes": notes}


def _generate_summary_md(all_results: dict, run_dir: Path) -> Path:
    """Generate human-readable family comparison summary."""
    lines = [
        "# Window-Family Validation Summary",
        "",
        f"**Run directory:** `{run_dir}`",
        "",
    ]

    for fam_id, windows in all_results.items():
        lines.extend([
            f"## Family: {fam_id}",
            "",
            "| Duration | Status | s_min | s_max | s_range | Near% | BG% | Memb% | Dn | EB | Score | Usable? |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|",
        ])
        for w in windows:
            eid = w["encounter_id"]
            dur = eid.split("_")[-1]  # e.g. "30m"
            status = w.get("scientific_status", "?")
            s_stats = w.get("mapping", {}).get("s_stats", {})
            s_min = f"{s_stats.get('min', 0):.3f}" if s_stats else "?"
            s_max = f"{s_stats.get('max', 0):.3f}" if s_stats else "?"
            s_rng = f"{s_stats.get('max', 0) - s_stats.get('min', 0):.3f}" if s_stats else "?"
            occ = w.get("mapping", {}).get("occupancy", {})
            near_s = f"{occ.get('near', 0):.1%}"
            bg_s = f"{occ.get('background', 0):.1%}"
            mem = w.get("membership_summary", {})
            mem_s = f"{mem.get('membership_fraction', 0):.1%}"
            m = w.get("metrics", {})
            dn_s = f"{m['Dn']:.3f}" if m.get("Dn") is not None else "N/A"
            eb_s = f"{m['EB']:.3f}" if m.get("EB") is not None else "N/A"
            ws = w.get("window_score", {})
            sc = f"{ws.get('score', -1):.1f}"
            usable = "**YES**" if ws.get("usable") else "no"
            lines.append(f"| {dur} | {status} | {s_min} | {s_max} | {s_rng} | {near_s} | {bg_s} | {mem_s} | {dn_s} | {eb_s} | {sc} | {usable} |")
        lines.append("")

    # Overall promotion
    lines.extend(["## Promotion Candidates", ""])
    usable_all = []
    for fam_id, windows in all_results.items():
        for w in windows:
            if w.get("window_score", {}).get("usable"):
                usable_all.append(w)
    usable_all.sort(key=lambda w: w.get("window_score", {}).get("score", 0), reverse=True)

    if usable_all:
        lines.append(f"**{len(usable_all)} usable windows found:**")
        lines.append("")
        for i, w in enumerate(usable_all[:10], 1):
            sc = w.get("window_score", {}).get("score", 0)
            occ = w.get("mapping", {}).get("occupancy", {})
            lines.append(f"{i}. **{w['encounter_id']}** (score={sc:.1f}, near={occ.get('near',0):.1%}, bg={occ.get('background',0):.1%})")
    else:
        lines.append("**No usable windows found.** Need seeds with higher orbital apogee (R > 13 Re).")

    out_path = run_dir / "family_summary.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="PDL Pilot — Window-family duration-ladder validation"
    )
    parser.add_argument(
        "--config", required=True, help="Path to window-family YAML."
    )
    parser.add_argument(
        "--families", nargs="*", default=None,
        help="Only run specific family seed_ids (default: all)."
    )
    args = parser.parse_args(argv)

    raw = _load_family_config(args.config)
    families = raw.get("families", [])
    if args.families:
        families = [f for f in families if f["seed_id"] in args.families]

    log.info("=== Window-family validation ===")
    log.info("Families to test: %d", len(families))

    # Build a pipeline config for live data
    config = PipelineConfig(
        run_label="family_validation",
        data_source="live",
        output_dir="runs",
        preflight=PreflightConfig(
            max_sza_deg=60.0,
            min_x_gsm_re=5.0,
            min_valid_fraction=0.3,
            min_density_cm3=0.3,
            min_membership_fraction=0.3,
            min_near_occupancy=0.01,
            min_bg_occupancy=0.01,
            min_s_std=0.005,
            fill_masking_policy="auto",
            grade_with_incomplete_flags="cap_silver",
        ),
        live=LiveDataConfig(
            cache_dir="data_cache",
            cache_policy="use",
            resample_cadence_seconds=10.0,  # coarser for long windows
            max_gap_seconds=60.0,
        ),
    )

    tracker = ProvenanceTracker(config)
    tracker.freeze_config()
    provider = _build_provider(config)

    log.info("Run ID: %s", tracker.run_id)

    all_results: dict[str, list[dict]] = {}
    flat_results: list[dict] = []

    for fam in families:
        fam_id = fam["seed_id"]
        log.info("--- Family: %s ---", fam_id)
        specs = _generate_window_specs(fam)
        fam_results = []

        for spec in specs:
            log.info("Validating window: %s [%s → %s]",
                     spec.encounter_id, spec.time_start, spec.time_end)
            try:
                enc = process_encounter(spec, config, tracker.run_dir, provider, tracker)
                summary = enc.to_summary_dict()
            except Exception as e:
                log.error("Window %s FAILED: %s", spec.encounter_id, e)
                summary = {
                    "encounter_id": spec.encounter_id,
                    "probe": spec.probe,
                    "scientific_status": "ERROR",
                    "evaluable": False,
                    "preflight_reasons": [f"Error: {e}"],
                    "metrics": {},
                    "mapping": {"occupancy": {}, "s_stats": {}},
                    "membership_summary": {},
                }

            summary["window_score"] = _compute_window_score(summary)
            summary["family_id"] = fam_id
            fam_results.append(summary)
            flat_results.append(summary)

        all_results[fam_id] = fam_results

    # Write outputs
    summary_json = tracker.run_dir / "family_summary.json"
    with open(summary_json, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    log.info("JSON summary → %s", summary_json)

    summary_md = _generate_summary_md(all_results, tracker.run_dir)
    log.info("Markdown summary → %s", summary_md)

    # CSV
    csv_path = tracker.run_dir / "family_summary.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "family", "encounter_id", "duration_min", "probe",
            "x_gsm", "sza_deg", "status",
            "s_min", "s_max", "s_range",
            "near_occ", "bg_occ", "membership",
            "Dn", "EB", "rho_nB",
            "score", "usable",
        ])
        for r in flat_results:
            fam = r.get("family_id", "")
            eid = r.get("encounter_id", "")
            # Extract duration from encounter_id suffix
            dur = eid.split("_")[-1].replace("m", "") if "_" in eid else ""
            pos = r.get("position_gsm_re") or [None, None, None]
            s_stats = r.get("mapping", {}).get("s_stats", {})
            occ = r.get("mapping", {}).get("occupancy", {})
            mem = r.get("membership_summary", {})
            m = r.get("metrics", {})
            ws = r.get("window_score", {})
            writer.writerow([
                fam, eid, dur,
                r.get("probe", ""),
                f"{pos[0]:.2f}" if pos[0] is not None else "",
                f"{r.get('sza_deg', ''):.1f}" if r.get("sza_deg") is not None else "",
                r.get("scientific_status", ""),
                f"{s_stats.get('min', 0):.3f}" if s_stats else "",
                f"{s_stats.get('max', 0):.3f}" if s_stats else "",
                f"{s_stats.get('max', 0) - s_stats.get('min', 0):.3f}" if s_stats else "",
                f"{occ.get('near', 0):.4f}",
                f"{occ.get('background', 0):.4f}",
                f"{mem.get('membership_fraction', 0):.4f}",
                f"{m.get('Dn', '')}" if m.get("Dn") is not None else "",
                f"{m.get('EB', '')}" if m.get("EB") is not None else "",
                f"{m.get('rho_nB_trend', '')}" if m.get("rho_nB_trend") is not None else "",
                ws.get("score", -1),
                ws.get("usable", False),
            ])
    log.info("CSV summary → %s", csv_path)

    # Final tally
    n_usable = sum(1 for r in flat_results if r.get("window_score", {}).get("usable"))
    tracker.write_manifest(extra={
        "n_families": len(families),
        "n_windows_tested": len(flat_results),
        "n_usable": n_usable,
        "usable_ids": [r["encounter_id"] for r in flat_results
                       if r.get("window_score", {}).get("usable")],
    })

    log.info("=== Family validation complete ===")
    log.info("  Families: %d | Windows: %d | Usable: %d",
             len(families), len(flat_results), n_usable)

    if n_usable > 0:
        best = sorted(
            [r for r in flat_results if r.get("window_score", {}).get("usable")],
            key=lambda r: r.get("window_score", {}).get("score", 0),
            reverse=True,
        )
        log.info("  Best usable windows:")
        for r in best[:5]:
            occ = r.get("mapping", {}).get("occupancy", {})
            log.info("    %s (score=%.1f, near=%.1%%, bg=%.1%%)",
                     r["encounter_id"],
                     r.get("window_score", {}).get("score", 0),
                     occ.get("near", 0) * 100,
                     occ.get("background", 0) * 100)
    else:
        log.info("  No usable windows. All tested seed families lack sufficient s-range.")


if __name__ == "__main__":
    main()
