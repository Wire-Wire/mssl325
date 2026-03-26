"""
Candidate-window validation and promotion workflow.

Runs each candidate through the live pipeline's preflight checks and
produces a compact comparison summary.  Promoted candidates are those
that pass all evaluability checks AND meet stricter curation criteria.

Usage:
    python -m pdl_pilot.cli.validate_candidates --config configs/pilot_candidates.yaml

Outputs:
    runs/<run_id>/candidate_summary.json   — machine-readable
    runs/<run_id>/candidate_summary.md     — human-readable comparison
    runs/<run_id>/encounter_<id>.json      — per-candidate artifacts
    runs/<run_id>/qc_<id>.png              — QC quicklook per candidate
"""
from __future__ import annotations

import argparse
import csv
import json
import logging
import sys
from pathlib import Path

import numpy as np

from pdl_pilot.config import load_config
from pdl_pilot.provenance import ProvenanceTracker
from pdl_pilot.cli.run_pilot import (
    _build_provider,
    process_encounter,
)

log = logging.getLogger(__name__)


# ---- Curation ranking criteria (stricter than preflight pass/fail) ----
# These are PREFERENCES for the first science-valid pilots, not hard gates.

def _compute_curation_score(enc_summary: dict) -> dict:
    """Score a validated candidate for science-pilot promotion.

    Returns dict with individual criteria + composite rank score.
    Higher score = better candidate.
    """
    score = 0.0
    notes: list[str] = []

    # Must be evaluable to even be considered
    if not enc_summary.get("evaluable", False):
        return {
            "promotable": False,
            "rank_score": -1.0,
            "criteria": {},
            "notes": [f"Not evaluable: {enc_summary.get('scientific_status', '?')}"],
        }

    criteria: dict[str, float] = {}

    # 1. Geometry — prefer near-subsolar
    sza = enc_summary.get("sza_deg")
    if sza is not None:
        if sza < 30:
            criteria["sza"] = 1.0
            score += 3.0
        elif sza < 45:
            criteria["sza"] = 0.6
            score += 1.5
        elif sza < 60:
            criteria["sza"] = 0.3
            score += 0.5
        else:
            criteria["sza"] = 0.0
    else:
        criteria["sza"] = 0.0

    pos = enc_summary.get("position_gsm_re")
    if pos:
        x, y, z = pos
        # X > 8 Re preferred
        if x > 10:
            criteria["x_gsm"] = 1.0
            score += 2.0
        elif x > 8:
            criteria["x_gsm"] = 0.7
            score += 1.0
        elif x > 5:
            criteria["x_gsm"] = 0.3
            score += 0.3
        else:
            criteria["x_gsm"] = 0.0

        # Low |Y| preferred
        if abs(y) < 3:
            criteria["y_gsm"] = 1.0
            score += 1.5
        elif abs(y) < 5:
            criteria["y_gsm"] = 0.7
            score += 1.0
        elif abs(y) < 10:
            criteria["y_gsm"] = 0.3
            score += 0.3
        else:
            criteria["y_gsm"] = 0.0

        # Low |Z|
        if abs(z) < 2:
            criteria["z_gsm"] = 1.0
            score += 0.5
        elif abs(z) < 5:
            criteria["z_gsm"] = 0.5
            score += 0.2
        else:
            criteria["z_gsm"] = 0.0
    else:
        criteria["x_gsm"] = criteria["y_gsm"] = criteria["z_gsm"] = 0.0

    # 2. Bin occupancy — need both near and background populated
    occ = enc_summary.get("mapping", {}).get("occupancy", {})
    near_occ = occ.get("near", 0)
    bg_occ = occ.get("background", 0)

    if near_occ > 0.1 and bg_occ > 0.1:
        criteria["occupancy"] = 1.0
        score += 3.0
    elif near_occ > 0.05 and bg_occ > 0.05:
        criteria["occupancy"] = 0.6
        score += 1.5
    elif near_occ > 0.02 and bg_occ > 0.02:
        criteria["occupancy"] = 0.3
        score += 0.5
    else:
        criteria["occupancy"] = 0.0
        notes.append("Low bin occupancy")

    # 3. Membership quality
    mem = enc_summary.get("membership_summary", {})
    mem_frac = mem.get("membership_fraction", 0)
    if mem_frac > 0.9:
        criteria["membership"] = 1.0
        score += 1.5
    elif mem_frac > 0.7:
        criteria["membership"] = 0.6
        score += 0.8
    elif mem_frac > 0.5:
        criteria["membership"] = 0.3
        score += 0.3
    else:
        criteria["membership"] = 0.0

    # 4. Data validity — low masked fractions
    masked = enc_summary.get("masked_fraction_summary", {})
    max_masked = max(masked.values()) if masked else 0.0
    if max_masked < 0.05:
        criteria["data_quality"] = 1.0
        score += 1.0
    elif max_masked < 0.2:
        criteria["data_quality"] = 0.6
        score += 0.5
    else:
        criteria["data_quality"] = 0.2
        notes.append(f"High masked fraction: {max_masked:.1%}")

    # 5. s-mapping quality — prefer good spread
    s_stats = enc_summary.get("mapping", {}).get("s_stats", {})
    s_range = (s_stats.get("max", 0) - s_stats.get("min", 0)) if s_stats else 0
    if s_range > 0.3:
        criteria["s_spread"] = 1.0
        score += 2.0
    elif s_range > 0.1:
        criteria["s_spread"] = 0.5
        score += 1.0
    else:
        criteria["s_spread"] = 0.1
        notes.append(f"Narrow s-range: {s_range:.3f}")

    # 6. Metrics available — all core metrics should be non-None
    metrics = enc_summary.get("metrics", {})
    n_available = sum(1 for k in ("Dn", "EB", "delta_beta", "rho_nB_trend")
                      if metrics.get(k) is not None)
    criteria["metrics_available"] = n_available / 4.0
    score += n_available * 0.5

    promotable = score >= 5.0  # Reasonable threshold for promotion
    if not promotable:
        notes.append(f"Score {score:.1f} below promotion threshold 5.0")

    return {
        "promotable": promotable,
        "rank_score": round(score, 2),
        "criteria": {k: round(v, 2) for k, v in criteria.items()},
        "notes": notes,
    }


def _generate_summary_md(results: list[dict], run_dir: Path) -> Path:
    """Generate human-readable markdown summary."""
    lines = [
        "# Candidate Validation Summary",
        "",
        f"**Run directory:** `{run_dir}`",
        f"**Candidates evaluated:** {len(results)}",
        "",
        "## Quick Overview",
        "",
        "| ID | Probe | SZA | X_GSM | Status | Evaluable | Near% | BG% | Dn | EB | Score | Promote? |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]

    for r in results:
        eid = r["encounter_id"]
        probe = r.get("probe", "?")
        sza = r.get("sza_deg")
        sza_s = f"{sza:.1f}" if sza is not None else "?"
        pos = r.get("position_gsm_re")
        x_s = f"{pos[0]:.1f}" if pos else "?"
        status = r.get("scientific_status", "?")
        ev = "YES" if r.get("evaluable") else "NO"
        occ = r.get("mapping", {}).get("occupancy", {})
        near_s = f"{occ.get('near', 0):.1%}"
        bg_s = f"{occ.get('background', 0):.1%}"
        m = r.get("metrics", {})
        dn_s = f"{m['Dn']:.3f}" if m.get("Dn") is not None else "N/A"
        eb_s = f"{m['EB']:.3f}" if m.get("EB") is not None else "N/A"
        cur = r.get("curation", {})
        score_s = f"{cur.get('rank_score', -1):.1f}"
        prom = "**YES**" if cur.get("promotable") else "no"
        lines.append(f"| {eid} | {probe} | {sza_s} | {x_s} | {status} | {ev} | {near_s} | {bg_s} | {dn_s} | {eb_s} | {score_s} | {prom} |")

    # Details per candidate
    lines.extend(["", "## Per-Candidate Details", ""])
    for r in results:
        eid = r["encounter_id"]
        lines.append(f"### {eid}")
        lines.append("")
        pos = r.get("position_gsm_re")
        if pos:
            lines.append(f"- **Position GSM:** ({pos[0]:.2f}, {pos[1]:.2f}, {pos[2]:.2f}) Re")
        lines.append(f"- **SZA:** {r.get('sza_deg', '?'):.1f}°" if r.get('sza_deg') is not None else "- **SZA:** ?")
        lines.append(f"- **MLT:** {r.get('mlt_hours', '?'):.1f}h" if r.get('mlt_hours') is not None else "- **MLT:** ?")
        lines.append(f"- **Scientific status:** {r.get('scientific_status', '?')}")
        lines.append(f"- **Evaluable:** {r.get('evaluable', False)}")

        occ = r.get("mapping", {}).get("occupancy", {})
        lines.append(f"- **Occupancy:** very_near={occ.get('very_near', 0):.1%}, near={occ.get('near', 0):.1%}, bg={occ.get('background', 0):.1%}")

        s_stats = r.get("mapping", {}).get("s_stats", {})
        if s_stats:
            lines.append(f"- **s range:** [{s_stats.get('min', 0):.3f}, {s_stats.get('max', 0):.3f}]")

        mem = r.get("membership_summary", {})
        lines.append(f"- **Membership:** {mem.get('membership_fraction', 0):.1%} sheath-plausible")

        m = r.get("metrics", {})
        lines.append(f"- **Metrics:** Dn={m.get('Dn')}, EB={m.get('EB')}, rho={m.get('rho_nB_trend')}")

        cur = r.get("curation", {})
        lines.append(f"- **Curation score:** {cur.get('rank_score', -1):.1f}")
        lines.append(f"- **Promotable:** {cur.get('promotable', False)}")
        if cur.get("notes"):
            for n in cur["notes"]:
                lines.append(f"  - {n}")

        reasons = r.get("preflight_reasons", [])
        if reasons:
            lines.append("- **Preflight issues:**")
            for rr in reasons:
                lines.append(f"  - {rr}")
        lines.append("")

    # Promotion summary
    promoted = [r for r in results if r.get("curation", {}).get("promotable")]
    lines.extend([
        "## Promotion Summary",
        "",
        f"**Promoted candidates:** {len(promoted)} / {len(results)}",
        "",
    ])
    if promoted:
        promoted_sorted = sorted(promoted, key=lambda r: r.get("curation", {}).get("rank_score", 0), reverse=True)
        for i, r in enumerate(promoted_sorted, 1):
            lines.append(f"{i}. **{r['encounter_id']}** (score={r['curation']['rank_score']:.1f})")
    else:
        lines.extend([
            "No candidates met the promotion threshold.",
            "**Next step:** Curate additional dayside windows in `configs/pilot_candidates.yaml`",
        ])

    out_path = run_dir / "candidate_summary.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="PDL Pilot — Candidate window validation and promotion"
    )
    parser.add_argument(
        "--config", required=True, help="Path to candidate manifest YAML."
    )
    parser.add_argument(
        "--promote-threshold", type=float, default=5.0,
        help="Minimum curation score for promotion (default: 5.0)."
    )
    args = parser.parse_args(argv)

    config = load_config(args.config)
    tracker = ProvenanceTracker(config)
    tracker.freeze_config()

    log.info("=== Candidate validation started — run_id=%s ===", tracker.run_id)
    log.info("Candidates to validate: %d", len(config.encounters))

    provider = _build_provider(config)

    # Record cache summary if live
    if config.data_source == "live":
        from pdl_pilot.data.cache import DataCache
        cache = DataCache(config.live.cache_dir, config.live.cache_policy)
        tracker.record_cache_summary(cache.summary())

    results: list[dict] = []
    for i, spec in enumerate(config.encounters, 1):
        log.info("--- Validating candidate %d/%d: %s ---",
                 i, len(config.encounters), spec.encounter_id)
        try:
            enc = process_encounter(spec, config, tracker.run_dir, provider, tracker)
            summary = enc.to_summary_dict()
        except Exception as e:
            log.error("Candidate %s FAILED with error: %s", spec.encounter_id, e)
            summary = {
                "encounter_id": spec.encounter_id,
                "probe": spec.probe,
                "scientific_status": "ERROR",
                "evaluable": False,
                "preflight_reasons": [f"Pipeline error: {e}"],
                "metrics": {},
                "mapping": {"occupancy": {}},
                "curation": {"promotable": False, "rank_score": -1, "notes": [str(e)]},
            }
            results.append(summary)
            continue

        # Compute curation score
        curation = _compute_curation_score(summary)
        # Override threshold if specified
        if curation["rank_score"] >= 0 and curation["rank_score"] < args.promote_threshold:
            curation["promotable"] = False
            if f"Score {curation['rank_score']:.1f}" not in str(curation.get("notes", "")):
                curation["notes"].append(
                    f"Score {curation['rank_score']:.1f} below threshold {args.promote_threshold}"
                )
        summary["curation"] = curation
        results.append(summary)

    # Update cache summary
    if config.data_source == "live":
        from pdl_pilot.data.cache import DataCache
        cache = DataCache(config.live.cache_dir, config.live.cache_policy)
        tracker.record_cache_summary(cache.summary())

    # Write machine-readable summary
    summary_json = tracker.run_dir / "candidate_summary.json"
    with open(summary_json, "w") as f:
        json.dump(results, f, indent=2, default=str)
    log.info("Machine-readable summary -> %s", summary_json)

    # Write human-readable summary
    summary_md = _generate_summary_md(results, tracker.run_dir)
    log.info("Human-readable summary -> %s", summary_md)

    # Write CSV for quick comparison
    csv_path = tracker.run_dir / "candidate_summary.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "encounter_id", "probe", "x_gsm", "y_gsm", "z_gsm", "sza_deg",
            "mlt_hours", "status", "evaluable", "near_occ", "bg_occ",
            "membership_frac", "Dn", "EB", "rho_nB", "rank_score", "promotable",
        ])
        for r in results:
            pos = r.get("position_gsm_re") or (None, None, None)
            occ = r.get("mapping", {}).get("occupancy", {})
            mem = r.get("membership_summary", {})
            m = r.get("metrics", {})
            cur = r.get("curation", {})
            writer.writerow([
                r.get("encounter_id", ""),
                r.get("probe", ""),
                f"{pos[0]:.2f}" if pos[0] is not None else "",
                f"{pos[1]:.2f}" if pos[1] is not None else "",
                f"{pos[2]:.2f}" if pos[2] is not None else "",
                f"{r.get('sza_deg', ''):.1f}" if r.get("sza_deg") is not None else "",
                f"{r.get('mlt_hours', ''):.1f}" if r.get("mlt_hours") is not None else "",
                r.get("scientific_status", ""),
                r.get("evaluable", False),
                f"{occ.get('near', 0):.4f}",
                f"{occ.get('background', 0):.4f}",
                f"{mem.get('membership_fraction', 0):.4f}",
                f"{m.get('Dn', '')}" if m.get("Dn") is not None else "",
                f"{m.get('EB', '')}" if m.get("EB") is not None else "",
                f"{m.get('rho_nB_trend', '')}" if m.get("rho_nB_trend") is not None else "",
                cur.get("rank_score", -1),
                cur.get("promotable", False),
            ])
    log.info("CSV summary -> %s", csv_path)

    # Promotion list
    promoted = sorted(
        [r for r in results if r.get("curation", {}).get("promotable")],
        key=lambda r: r.get("curation", {}).get("rank_score", 0),
        reverse=True,
    )

    n_total = len(results)
    n_eval = sum(1 for r in results if r.get("evaluable"))
    n_prom = len(promoted)

    tracker.write_manifest(extra={
        "n_candidates": n_total,
        "n_evaluable": n_eval,
        "n_promoted": n_prom,
        "promoted_ids": [r["encounter_id"] for r in promoted],
    })

    log.info("=== Validation complete ===")
    log.info("  Candidates: %d | Evaluable: %d | Promoted: %d", n_total, n_eval, n_prom)
    if promoted:
        log.info("  Promoted windows:")
        for r in promoted:
            log.info("    %s (score=%.1f)", r["encounter_id"],
                     r["curation"]["rank_score"])
    else:
        log.info("  No candidates promoted. Curate more dayside windows in pilot_candidates.yaml")


if __name__ == "__main__":
    main()
