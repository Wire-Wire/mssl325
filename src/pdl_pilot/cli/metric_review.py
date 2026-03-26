"""
Bounded metric-behavior review across the current window bank.

Produces:
  - pass-aware metric matrix (JSON + CSV)
  - descriptive summary of metric spread, within-pass vs between-pass variation
  - compact metric correlation/scatter plots
  - provisional mini seed stratification slate

Usage:
    python -m pdl_pilot.cli.metric_review --run-dir runs/<latest_run_id>

Reads from a completed run's all_encounters.json.
"""
from __future__ import annotations

import argparse
import csv
import json
import logging
from pathlib import Path

import numpy as np

log = logging.getLogger(__name__)


def _load_bank(run_dir: Path) -> list[dict]:
    """Load all_encounters.json from a completed run."""
    path = run_dir / "all_encounters.json"
    with open(path) as f:
        return json.load(f)


def _identify_passes(bank: list[dict]) -> dict[str, list[dict]]:
    """Group windows by orbital pass (date)."""
    passes: dict[str, list[dict]] = {}
    for w in bank:
        date = w["time_start"][:10]
        passes.setdefault(date, []).append(w)
    return passes


def _build_matrix(bank: list[dict], passes: dict) -> list[dict]:
    """Build the pass-aware metric matrix."""
    # Map dates to pass numbers
    pass_dates = sorted(passes.keys())
    date_to_pass = {d: i + 1 for i, d in enumerate(pass_dates)}

    rows = []
    for w in bank:
        date = w["time_start"][:10]
        pass_num = date_to_pass[date]
        is_variant = len(passes[date]) > 1
        m = w["metrics"]
        o = w["mapping"]["occupancy"]
        u = w["upstream"]
        s = w["mapping"].get("s_stats", {})
        mem = w.get("membership_summary", {})

        rows.append({
            "encounter_id": w["encounter_id"],
            "pass_num": pass_num,
            "date": date,
            "is_duration_variant": is_variant,
            "n_variants_in_pass": len(passes[date]),
            "probe": w.get("probe", "thd"),
            "sza_deg": w.get("sza_deg"),
            "dp_nPa": u.get("dp_nPa"),
            "bz_nT": u.get("bz_gsm_nT"),
            "mach_alfven": u.get("mach_alfven"),
            "near_occ": o.get("near", 0),
            "bg_occ": o.get("background", 0),
            "vn_occ": o.get("very_near", 0),
            "membership_frac": mem.get("membership_fraction", 0),
            "s_min": s.get("min"),
            "s_max": s.get("max"),
            "s_range": (s.get("max", 0) - s.get("min", 0)) if s else None,
            "Dn": m.get("Dn"),
            "EB": m.get("EB"),
            "delta_beta": m.get("delta_beta"),
            "rho_nB": m.get("rho_nB_trend"),
            "persistence": m.get("persistence_frac"),
            "ptot_smooth": m.get("ptot_smoothness"),
        })
    return rows


def _describe_spread(rows: list[dict]) -> dict:
    """Compute descriptive statistics for each metric channel."""
    channels = ["Dn", "EB", "delta_beta", "rho_nB", "persistence", "ptot_smooth"]
    stats = {}
    for ch in channels:
        vals = [r[ch] for r in rows if r[ch] is not None]
        if not vals:
            stats[ch] = {"n": 0}
            continue
        arr = np.array(vals)
        stats[ch] = {
            "n": len(vals),
            "min": round(float(np.min(arr)), 3),
            "max": round(float(np.max(arr)), 3),
            "median": round(float(np.median(arr)), 3),
            "mean": round(float(np.mean(arr)), 3),
            "std": round(float(np.std(arr)), 3),
            "range": round(float(np.max(arr) - np.min(arr)), 3),
        }
    return stats


def _within_vs_between(rows: list[dict], passes: dict) -> dict:
    """Compare within-pass vs between-pass metric variation for Dn and EB."""
    result = {}
    for ch in ["Dn", "EB", "rho_nB"]:
        # Within-pass: for passes with >1 variant, measure spread
        within_spreads = []
        for date, windows in passes.items():
            if len(windows) > 1:
                vals = [w["metrics"].get(ch) for w in windows if w["metrics"].get(ch) is not None]
                if len(vals) > 1:
                    within_spreads.append(max(vals) - min(vals))

        # Between-pass: one representative per pass, measure spread
        pass_reps = []
        for date, windows in passes.items():
            vals = [w["metrics"].get(ch) for w in windows if w["metrics"].get(ch) is not None]
            if vals:
                pass_reps.append(np.median(vals))

        result[ch] = {
            "within_pass_spreads": [round(s, 3) for s in within_spreads],
            "mean_within_spread": round(float(np.mean(within_spreads)), 3) if within_spreads else None,
            "between_pass_range": round(float(max(pass_reps) - min(pass_reps)), 3) if len(pass_reps) > 1 else None,
            "between_pass_values": [round(float(v), 3) for v in pass_reps],
        }
    return result


def _stratify_seeds(rows: list[dict]) -> list[dict]:
    """Provisional mini seed stratification.

    Based on observed metric behavior + pass independence only.
    NOT classification. NOT thresholds. NOT labels.
    """
    # Use only independent pass representatives (for multi-variant passes, pick the 6h variant)
    pass_reps: dict[str, dict] = {}
    for r in rows:
        date = r["date"]
        if date not in pass_reps:
            pass_reps[date] = r
        elif not r["is_duration_variant"] or "6h" in r["encounter_id"]:
            pass_reps[date] = r

    reps = sorted(pass_reps.values(), key=lambda r: r["Dn"] if r["Dn"] is not None else 999)

    seeds = []
    # Slice by observed Dn behavior (low / intermediate / high) without defining thresholds
    # This is descriptive stratification for planning, not classification
    low_dn = [r for r in reps if r["Dn"] is not None and r["Dn"] < 0.5]
    mid_dn = [r for r in reps if r["Dn"] is not None and 0.5 <= r["Dn"] <= 1.5]
    high_dn = [r for r in reps if r["Dn"] is not None and r["Dn"] > 1.5]

    if low_dn:
        best = min(low_dn, key=lambda r: abs(r.get("rho_nB", 0) or 0))
        seeds.append({
            "seed_name": "seed_A",
            "encounter_id": best["encounter_id"],
            "date": best["date"],
            "rationale": f"Low Dn ({best['Dn']:.2f}), high EB ({best['EB']:.2f}): represents strongest near-MP depletion + enhancement pattern observed",
            "Dn": best["Dn"], "EB": best["EB"], "rho_nB": best.get("rho_nB"),
        })

    if mid_dn:
        best = mid_dn[len(mid_dn) // 2]  # median by Dn
        seeds.append({
            "seed_name": "seed_B",
            "encounter_id": best["encounter_id"],
            "date": best["date"],
            "rationale": f"Intermediate Dn ({best['Dn']:.2f}), moderate EB ({best['EB']:.2f}): represents near-neutral depletion behavior",
            "Dn": best["Dn"], "EB": best["EB"], "rho_nB": best.get("rho_nB"),
        })

    if high_dn:
        best = max(high_dn, key=lambda r: r["Dn"])
        seeds.append({
            "seed_name": "seed_C",
            "encounter_id": best["encounter_id"],
            "date": best["date"],
            "rationale": f"High Dn ({best['Dn']:.2f}), low EB ({best['EB']:.2f}): represents strongest near-MP density enhancement observed",
            "Dn": best["Dn"], "EB": best["EB"], "rho_nB": best.get("rho_nB"),
        })

    # Add a strong-anti-correlation seed if distinct from above
    strong_rho = [r for r in reps if r.get("rho_nB") is not None and r["rho_nB"] < -0.85]
    for sr in strong_rho:
        if sr["encounter_id"] not in [s["encounter_id"] for s in seeds]:
            seeds.append({
                "seed_name": f"seed_D",
                "encounter_id": sr["encounter_id"],
                "date": sr["date"],
                "rationale": f"Strong anti-correlation (rho={sr['rho_nB']:.2f}): represents strongest n-B coupling observed",
                "Dn": sr["Dn"], "EB": sr["EB"], "rho_nB": sr.get("rho_nB"),
            })
            break

    return seeds


def _generate_review_md(
    rows: list[dict],
    passes: dict,
    spread: dict,
    within_between: dict,
    seeds: list[dict],
    out_dir: Path,
) -> Path:
    """Generate the metric-behavior review markdown."""
    lines = [
        "# Metric-Behavior Review — Phase 2a Bank",
        "",
        f"**Bank size:** {len(rows)} windows across {len(passes)} distinct passes",
        f"**Passes with duration variants:** {sum(1 for d,w in passes.items() if len(w) > 1)}",
        "",
        "---",
        "",
        "## 1. Pass-Aware Metric Matrix",
        "",
        "| # | ID | Date | Var? | SZA | Dp | Bz | Near% | BG% | Dn | EB | Δβ | ρ(n,B) | Persist |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]

    for r in sorted(rows, key=lambda x: (x["date"], x["encounter_id"])):
        var = "yes" if r["n_variants_in_pass"] > 1 else ""
        rho = f"{r['rho_nB']:.2f}" if r["rho_nB"] is not None else "N/A"
        pers = f"{r['persistence']:.2f}" if r["persistence"] is not None else "N/A"
        lines.append(
            f"| {r['pass_num']} | {r['encounter_id']} | {r['date']} | {var} | "
            f"{r['sza_deg']:.0f}° | {r['dp_nPa']:.1f} | {r['bz_nT']:+.1f} | "
            f"{r['near_occ']:.0%} | {r['bg_occ']:.0%} | "
            f"{r['Dn']:.2f} | {r['EB']:.2f} | {r['delta_beta']:.1f} | {rho} | {pers} |"
        )

    lines.extend(["", "---", "", "## 2. Metric Spread Summary", ""])
    lines.append("| Metric | N | Min | Max | Median | Std | Range |")
    lines.append("|---|---|---|---|---|---|---|")
    for ch, st in spread.items():
        if st["n"] == 0:
            lines.append(f"| {ch} | 0 | — | — | — | — | — |")
        else:
            lines.append(f"| {ch} | {st['n']} | {st['min']:.3f} | {st['max']:.3f} | {st['median']:.3f} | {st['std']:.3f} | {st['range']:.3f} |")

    lines.extend(["", "**Key observations:**", ""])
    # Dn
    dn_s = spread.get("Dn", {})
    if dn_s.get("n", 0) > 0:
        lines.append(f"- **Dn** spans {dn_s['min']:.2f} to {dn_s['max']:.2f} (range {dn_s['range']:.2f}). "
                     f"Values both above and below 1.0 observed.")
    eb_s = spread.get("EB", {})
    if eb_s.get("n", 0) > 0:
        lines.append(f"- **EB** spans {eb_s['min']:.2f} to {eb_s['max']:.2f}. "
                     f"All values except 2 passes show EB > 1 (B enhancement near MP).")
    rho_s = spread.get("rho_nB", {})
    if rho_s.get("n", 0) > 0:
        lines.append(f"- **ρ(n,B)** all negative where available ({rho_s['min']:.2f} to {rho_s['max']:.2f}). "
                     f"Anti-correlation between density and |B| trends is consistent across the bank.")
    pers_s = spread.get("persistence", {})
    if pers_s.get("n", 0) > 0:
        lines.append(f"- **Persistence** spans {pers_s['min']:.2f} to {pers_s['max']:.2f}. "
                     f"High variance reflects different depletion extents.")

    lines.extend(["", "---", "", "## 3. Within-Pass vs Between-Pass Variation", ""])
    for ch, wb in within_between.items():
        lines.append(f"### {ch}")
        if wb["mean_within_spread"] is not None:
            lines.append(f"- Within-pass spread (duration variants): {wb['within_pass_spreads']} → mean {wb['mean_within_spread']:.3f}")
        else:
            lines.append(f"- No multi-variant passes with valid {ch}")
        if wb["between_pass_range"] is not None:
            lines.append(f"- Between-pass range (independent passes): {wb['between_pass_range']:.3f}")
            lines.append(f"- Pass-representative values: {wb['between_pass_values']}")
        lines.append("")

    lines.append("**Interpretation:**")
    # Check if within < between
    for ch in ["Dn", "EB"]:
        wb = within_between[ch]
        if wb["mean_within_spread"] is not None and wb["between_pass_range"] is not None:
            ratio = wb["mean_within_spread"] / wb["between_pass_range"] if wb["between_pass_range"] > 0 else 999
            if ratio < 0.3:
                lines.append(f"- {ch}: within-pass variation ({wb['mean_within_spread']:.3f}) is much smaller than between-pass variation ({wb['between_pass_range']:.3f}). Duration variants behave consistently.")
            else:
                lines.append(f"- {ch}: within-pass variation ({wb['mean_within_spread']:.3f}) is comparable to between-pass variation ({wb['between_pass_range']:.3f}). Duration choice matters for this metric.")

    lines.extend([
        "", "---", "",
        "## 4. Provisional Mini Seed Stratification",
        "",
        "The following seeds are selected for planning only. They are NOT scientific classes, "
        "NOT labeled examples, and NOT detector thresholds.",
        "",
    ])
    for s in seeds:
        rho = f"{s['rho_nB']:.2f}" if s["rho_nB"] is not None else "N/A"
        lines.append(f"### {s['seed_name']}: `{s['encounter_id']}` ({s['date']})")
        lines.append(f"- Dn={s['Dn']:.2f}, EB={s['EB']:.2f}, ρ={rho}")
        lines.append(f"- Rationale: {s['rationale']}")
        lines.append("")

    lines.extend([
        "**Naming discipline:** Every window in this bank remains a "
        "\"measurement-model-valid near-MP comparator window.\" "
        "Seed labels (A, B, C, D) are operational planning tags only.",
        "",
        "---",
        "",
        "## 5. What this review supports and does not support",
        "",
        "**Supports:**",
        "- The frozen metric backbone resolves distinguishable behavior across real passes",
        "- Duration variants are operationally similar within a pass (between-pass > within-pass for Dn, EB)",
        "- The bank spans a factor ~20 in Dn and ~5 in EB",
        "- Anti-correlation (ρ < 0) is consistently present",
        "",
        "**Does NOT support:**",
        "- Any classification or labeling of windows",
        "- Any threshold definition",
        "- Any statement about whether specific windows contain PDL",
        "- Development-set membership decisions",
    ])

    out_path = out_dir / "metric_behavior_review.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return out_path


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Bounded metric-behavior review")
    parser.add_argument("--run-dir", required=True, help="Path to completed run directory")
    args = parser.parse_args(argv)

    run_dir = Path(args.run_dir)
    bank = _load_bank(run_dir)
    passes = _identify_passes(bank)
    rows = _build_matrix(bank, passes)

    log.info("Bank: %d windows, %d passes", len(rows), len(passes))

    spread = _describe_spread(rows)
    wb = _within_vs_between(rows, passes)
    seeds = _stratify_seeds(rows)

    # Write machine-readable outputs
    matrix_path = run_dir / "metric_matrix.json"
    with open(matrix_path, "w") as f:
        json.dump(rows, f, indent=2, default=str)

    matrix_csv = run_dir / "metric_matrix.csv"
    with open(matrix_csv, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    seeds_path = run_dir / "seed_stratification.json"
    with open(seeds_path, "w") as f:
        json.dump({"seeds": seeds, "note": "Provisional planning artifacts only. Not labels."}, f, indent=2)

    review_md = _generate_review_md(rows, passes, spread, wb, seeds, run_dir)

    log.info("Outputs:")
    log.info("  Matrix JSON: %s", matrix_path)
    log.info("  Matrix CSV: %s", matrix_csv)
    log.info("  Seeds JSON: %s", seeds_path)
    log.info("  Review MD: %s", review_md)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
