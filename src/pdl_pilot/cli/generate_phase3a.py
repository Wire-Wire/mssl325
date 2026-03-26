"""
Generate Phase 3A Dn/EB exploratory comparison artifacts.

Fills schema gaps (pass_matrix.csv, figure_manifest, claim_map, pass_report_chunks),
produces Phase 3A comparison figure, and generates the run-level review packet.

Usage:
    python -m pdl_pilot.cli.generate_phase3a --run-dir runs/<run_id>
"""
from __future__ import annotations

import argparse
import csv
import json
import logging
from pathlib import Path
from datetime import datetime, timezone

import numpy as np

log = logging.getLogger(__name__)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate Phase 3A artifacts")
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args(argv)

    run_dir = Path(args.run_dir)
    ev = run_dir / "evidence"

    with open(ev / "json/bank_manifest.json") as f:
        records = json.load(f)
    with open(run_dir / "run_manifest.json") as f:
        manifest = json.load(f)

    # Pass representatives
    pass_reps = {}
    for r in records:
        d = r["pass_date"]
        if d not in pass_reps or "6h" in r["window_id"]:
            pass_reps[d] = r

    # ---- 1. pass_matrix.csv ----
    (ev / "csv").mkdir(parents=True, exist_ok=True)
    fields = [
        "pass_id", "date", "n_windows", "evidence_status", "sza_deg", "dp_nPa", "bz_nT",
        "near_occ", "bg_occ", "membership_frac", "Dn", "EB", "delta_beta", "rho_nB",
        "persistence", "spike_frac", "Dn_clean", "EB_clean", "dens_cv_near", "seed_ref",
    ]
    with open(ev / "csv/pass_matrix.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for d in sorted(pass_reps.keys()):
            r = pass_reps[d]
            n_w = sum(1 for x in records if x["pass_date"] == d)
            w.writerow({
                "pass_id": r["pass_id"], "date": d, "n_windows": n_w,
                "evidence_status": r["review_disposition"]["evidence_status"],
                "sza_deg": r["geometry_context"]["sza_deg"],
                "dp_nPa": r["upstream_summary"]["dp_nPa"],
                "bz_nT": r["upstream_summary"]["bz_gsm_nT"],
                "near_occ": r["occupancy"]["near"],
                "bg_occ": r["occupancy"]["background"],
                "membership_frac": r["data_validity"]["membership_fraction"],
                "Dn": r["metric_values"]["Dn"],
                "EB": r["metric_values"]["EB"],
                "delta_beta": r["metric_values"]["delta_beta"],
                "rho_nB": r["metric_values"]["rho_nB"],
                "persistence": r["metric_values"]["persistence"],
                "spike_frac": r["confounder_audit"]["spike_fraction"],
                "Dn_clean": r["confounder_audit"]["Dn_clean"],
                "EB_clean": r["confounder_audit"]["EB_clean"],
                "dens_cv_near": r["confounder_audit"]["dens_cv_near"],
                "seed_ref": r["review_disposition"]["seed_reference"] or "",
            })
    log.info("Wrote pass_matrix.csv")

    # ---- 2. Phase 3A figure ----
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    reps = list(pass_reps.values())
    status_c = {"clean_core": "#2166ac", "cautious": "#d6604d", "excluded": "#999999"}
    status_m = {"clean_core": "o", "cautious": "s", "excluded": "X"}

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Phase 3A: Bounded Dn/EB Exploratory Comparison (Descriptive Only)", fontsize=11)

    ax = axes[0]
    for r in reps:
        st = r["review_disposition"]["evidence_status"]
        ax.scatter(r["metric_values"]["Dn"], r["metric_values"]["EB"],
                   c=status_c[st], marker=status_m[st], s=120,
                   edgecolors="k", linewidths=0.7, zorder=3)
        ax.annotate(r["pass_id"],
                    (r["metric_values"]["Dn"], r["metric_values"]["EB"]),
                    fontsize=8, ha="left", va="bottom",
                    xytext=(4, 4), textcoords="offset points")
    ax.axhline(1, color="gray", ls="--", lw=0.5, alpha=0.5)
    ax.axvline(1, color="gray", ls="--", lw=0.5, alpha=0.5)
    ax.set_xlabel("Dn (near / background density ratio)")
    ax.set_ylabel("EB (near / background |B| ratio)")
    ax.set_title("Pass-representative Dn vs EB\n(blue=clean core, red=cautious, gray=excluded)")

    ax = axes[1]
    for r in reps:
        ca = r["confounder_audit"]
        st = r["review_disposition"]["evidence_status"]
        if ca.get("Dn_clean") is None:
            continue
        ax.scatter(r["metric_values"]["Dn"], ca["Dn_clean"],
                   c=status_c[st], marker=status_m[st], s=120,
                   edgecolors="k", linewidths=0.7, zorder=3)
        ax.annotate(r["pass_id"],
                    (r["metric_values"]["Dn"], ca["Dn_clean"]),
                    fontsize=8, ha="left", va="bottom",
                    xytext=(4, 4), textcoords="offset points")
    ax.plot([0, 2.5], [0, 2.5], "k--", lw=0.5, alpha=0.5)
    ax.set_xlabel("Dn (original)")
    ax.set_ylabel("Dn (after spike removal)")
    ax.set_title("Spike-removal sensitivity\n(on diagonal = robust)")
    ax.set_xlim([0, 2.5])
    ax.set_ylim([0, 2.5])

    plt.tight_layout()
    fig_path = Path("reports/current_bank/figures/phase3a_dneb_comparison.png")
    fig_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(str(fig_path), dpi=150)
    plt.close()
    log.info("Saved %s", fig_path)

    # ---- 3. figure_manifest.json ----
    (ev / "index").mkdir(parents=True, exist_ok=True)
    figs = {
        "cross_pass_summary": {
            "path": "reports/current_bank/figures/cross_pass_summary.png",
            "question_answered": "How do Dn, EB, spike fraction, and occupancy co-vary across the bank?",
            "stage": "phase_2d",
        },
        "phase3a_dneb_comparison": {
            "path": str(fig_path),
            "question_answered": "How do Dn and EB compare across passes, and how robust is Dn to spike removal?",
            "stage": "phase_3a",
        },
    }
    with open(ev / "index/figure_manifest.json", "w") as f:
        json.dump(figs, f, indent=2)

    # ---- 4. claim_map.json ----
    claims = {
        "phase3a_claim_1": {
            "statement": "Clean core (P2, P4, P5, P6) spans Dn 0.94-2.31 and EB 0.80-1.96.",
            "evidence_basis": ["P2", "P4", "P5", "P6"],
            "evidence_type": "clean_core",
            "caveats": [],
        },
        "phase3a_claim_2": {
            "statement": "Low-Dn range (Dn < 0.5) is carried only by cautious passes (P1: 0.12, P3: 0.39).",
            "evidence_basis": ["P1", "P3"],
            "evidence_type": "cautious",
            "caveats": ["P1: density noise CV=0.93", "P3: EB partially spike-dependent"],
        },
        "phase3a_claim_3": {
            "statement": "P7 excluded: metrics collapse after spike removal.",
            "evidence_basis": ["P7"],
            "evidence_type": "excluded",
            "caveats": ["spike-dominated"],
        },
        "phase3a_claim_4": {
            "statement": "rho(n,B) is universally negative and non-discriminative within this bank.",
            "evidence_basis": ["all_interpretable"],
            "evidence_type": "descriptive",
            "caveats": ["THD only", "Dp > 3 nPa bias"],
        },
    }
    with open(ev / "index/claim_map.json", "w") as f:
        json.dump(claims, f, indent=2)

    # ---- 5. pass_report_chunks.json ----
    (ev / "chunks").mkdir(parents=True, exist_ok=True)
    chunks = []
    for d in sorted(pass_reps.keys()):
        r = pass_reps[d]
        rd = r["review_disposition"]
        ca = r["confounder_audit"]
        mv = r["metric_values"]
        chunks.append({
            "chunk_type": "pass_evidence",
            "pass_id": r["pass_id"],
            "date": d,
            "evidence_status": rd["evidence_status"],
            "seed_ref": rd.get("seed_reference"),
            "Dn": mv["Dn"], "EB": mv["EB"],
            "Dn_clean": ca.get("Dn_clean"),
            "EB_clean": ca.get("EB_clean"),
            "rho_nB": mv.get("rho_nB"),
            "delta_beta": mv.get("delta_beta"),
            "persistence": mv.get("persistence"),
            "spike_frac": ca.get("spike_fraction"),
            "dens_cv_near": ca.get("dens_cv_near"),
            "caveats": rd.get("caveats", []),
            "dp_nPa": r["upstream_summary"]["dp_nPa"],
            "bz_nT": r["upstream_summary"]["bz_gsm_nT"],
            "near_occ": r["occupancy"]["near"],
            "bg_occ": r["occupancy"]["background"],
        })
    with open(ev / "chunks/pass_report_chunks.json", "w") as f:
        json.dump(chunks, f, indent=2, default=str)

    # ---- 6. Update artifact index ----
    idx = {
        "schema": "docs/EVIDENCE_REPORT_SCHEMA.md",
        "json": ["evidence/json/bank_manifest.json", "evidence/json/bank_summary.json",
                  "evidence/json/review_layers.json", "evidence/json/pass_summary.jsonl"],
        "csv": ["evidence/csv/window_matrix.csv", "evidence/csv/confounder_register.csv",
                "evidence/csv/interval_audit_matrix.csv", "evidence/csv/pass_matrix.csv"],
        "index": ["evidence/index/artifact_index.json", "evidence/index/figure_manifest.json",
                   "evidence/index/claim_map.json"],
        "chunks": ["evidence/chunks/bank_report_chunks.json", "evidence/chunks/pass_report_chunks.json"],
        "review": ["evidence/review/RUN_REVIEW_PACKET.md", "evidence/review/RUN_REVIEW_PACKET_chunks.json"],
        "reports": "reports/current_bank/",
        "stage": "phase_3a",
    }
    with open(ev / "index/artifact_index.json", "w") as f:
        json.dump(idx, f, indent=2)

    # ---- 7. RUN_REVIEW_PACKET_chunks.json ----
    (ev / "review").mkdir(parents=True, exist_ok=True)
    packet_chunks = {
        "run_id": manifest.get("run_id", ""),
        "config_hash": manifest.get("config_hash", ""),
        "stage": "phase_3a",
        "bank_scope": {"total_windows": 9, "total_passes": 7,
                        "clean_core": 4, "cautious": 2, "excluded": 1},
        "primary_comparison_subset": ["P2", "P4", "P5", "P6"],
        "secondary_with_caveats": ["P1", "P3"],
        "excluded_from_comparison": ["P7"],
        "passes": chunks,
        "claims": claims,
        "figures": figs,
        "non_claims": [
            "No thresholds are defined or implied.",
            "No window is classified as PDL-positive or non-PDL.",
            "No development-set membership is assigned.",
            "rho(n,B) is non-discriminative within this bank.",
        ],
    }
    with open(ev / "review/RUN_REVIEW_PACKET_chunks.json", "w") as f:
        json.dump(packet_chunks, f, indent=2, default=str)

    print(f"Phase 3A artifacts generated in {ev}")
    print("  pass_matrix.csv, figure_manifest.json, claim_map.json, pass_report_chunks.json")
    print(f"  Figure: {fig_path}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
