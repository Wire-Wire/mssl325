"""
Generate reusable evidence-report package from a completed bank run.

Produces machine-readable JSON/CSV artifacts, human-facing per-pass
evidence sheets, and cross-pass summary reports.

Usage:
    python -m pdl_pilot.cli.generate_evidence --run-dir runs/<run_id>
"""
from __future__ import annotations

import argparse
import csv
import json
import logging
from pathlib import Path

import numpy as np

log = logging.getLogger(__name__)

# ---- Review dispositions from Phase 2C/2D ----
CLEAN_CORE_DATES = {"2008-09-03", "2009-09-20", "2009-09-26", "2009-09-27"}
CAUTIOUS_DATES = {"2008-08-18", "2009-09-13"}
EXCLUDED_DATES = {"2009-10-24"}
SEED_MAP = {
    "usable_aug18_6h": "seed_A",
    "usable_sep20_09_6h": "seed_B",
    "usable_sep03_6h": "seed_C",
    "usable_sep13_09_6h": "seed_D",
}
CAVEATS_BY_DATE = {
    "2009-10-24": ["Spike-dominated: metrics collapse after spike removal"],
    "2008-08-18": ["High near-bin density noise (CV=0.93); wave/mirror risk"],
    "2009-09-13": ["EB partially spike-dependent (delta=0.50)"],
}


def _get_status(date: str) -> str:
    if date in CLEAN_CORE_DATES:
        return "clean_core"
    if date in CAUTIOUS_DATES:
        return "cautious"
    if date in EXCLUDED_DATES:
        return "excluded"
    return "unknown"


def _build_records(bank, audit, manifest, pass_map, variants_map):
    records = []
    for w in bank:
        d = w["time_start"][:10]
        pid = pass_map[d]
        a = audit.get(d, {})
        m = w["metrics"]
        u = w["upstream"]
        o = w["mapping"]["occupancy"]
        s = w["mapping"].get("s_stats", {})
        mem = w.get("membership_summary", {})
        qc = w.get("qc", {})

        rec = {
            "window_id": w["encounter_id"],
            "pass_id": pid,
            "pass_date": d,
            "variant_group_id": pid,
            "is_duration_variant": len(variants_map.get(d, [])) > 1,
            "probe": w.get("probe", "thd"),
            "time_start": w["time_start"],
            "time_end": w["time_end"],
            "geometry_context": {
                "sza_deg": w.get("sza_deg"),
                "mlt_hours": w.get("mlt_hours"),
                "position_gsm_re": w.get("position_gsm_re"),
                "abs_z_re": w.get("abs_z_re"),
            },
            "upstream_summary": {
                "dp_nPa": u.get("dp_nPa"),
                "bz_gsm_nT": u.get("bz_gsm_nT"),
                "mach_alfven": u.get("mach_alfven"),
                "stability_flag": u.get("stability_flag"),
            },
            "measurement_model": {
                "mp_model": w["mapping"].get("mp_model", "shue1998"),
                "bs_model": w["mapping"].get("bs_model", "merka2005"),
                "mp_standoff_re": w["mapping"].get("mp_standoff_re"),
                "bs_standoff_re": w["mapping"].get("bs_standoff_re"),
                "distance_direction": "sun_earth_line",
                "boundary_averaging": "encounter_averaged",
            },
            "data_validity": {
                "membership_fraction": mem.get("membership_fraction", 0),
                "n_artifact_suspect": mem.get("n_artifact_suspect", 0),
                "n_unknown": mem.get("n_unknown", 0),
                "masked_fractions": w.get("masked_fraction_summary", {}),
            },
            "occupancy": {
                "very_near": o.get("very_near", 0),
                "near": o.get("near", 0),
                "background": o.get("background", 0),
                "s_min": s.get("min"),
                "s_max": s.get("max"),
                "s_range": (s.get("max", 0) - s.get("min", 0)) if s else None,
            },
            "metric_values": {
                "Dn": m.get("Dn"),
                "EB": m.get("EB"),
                "delta_beta": m.get("delta_beta"),
                "rho_nB": m.get("rho_nB_trend"),
                "persistence": m.get("persistence_frac"),
                "ptot_smoothness": m.get("ptot_smoothness"),
                "fluctuation_amp": m.get("fluctuation_amp"),
            },
            "confounder_audit": {
                "jet_flag": qc.get("jet_flag"),
                "wave_flag": qc.get("wave_flag"),
                "transient_flag": qc.get("transient_flag"),
                "mixing_flag": qc.get("mixing_flag"),
                "motion_flag": qc.get("motion_flag"),
                "spike_fraction": a.get("spike_frac"),
                "near_spikes": a.get("near_spikes"),
                "bg_spikes": a.get("bg_spikes"),
                "Dn_clean": a.get("Dn_clean"),
                "EB_clean": a.get("EB_clean"),
                "dens_cv_near": a.get("dens_cv_near"),
                "grade": qc.get("grade"),
                "grade_note": qc.get("grade_note", ""),
            },
            "review_disposition": {
                "evidence_status": _get_status(d),
                "seed_reference": SEED_MAP.get(w["encounter_id"]),
                "caveats": CAVEATS_BY_DATE.get(d, []),
                "stage": "phase_2d",
            },
            "source_run_id": manifest.get("run_id", ""),
            "config_hash": manifest.get("config_hash", ""),
        }
        records.append(rec)
    return records


def _write_json(records, ev_dir, manifest, pass_dates, pass_map):
    (ev_dir / "json").mkdir(parents=True, exist_ok=True)

    with open(ev_dir / "json/bank_manifest.json", "w") as f:
        json.dump(records, f, indent=2, default=str)

    summary = {
        "n_windows": len(records),
        "n_passes": len(pass_dates),
        "n_clean_core": sum(1 for r in records
                            if r["review_disposition"]["evidence_status"] == "clean_core"),
        "n_cautious": sum(1 for r in records
                          if r["review_disposition"]["evidence_status"] == "cautious"),
        "n_excluded": sum(1 for r in records
                          if r["review_disposition"]["evidence_status"] == "excluded"),
        "stage": "phase_2d",
        "source_run_id": manifest.get("run_id", ""),
    }
    with open(ev_dir / "json/bank_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    review = {r["window_id"]: r["review_disposition"] for r in records}
    with open(ev_dir / "json/review_layers.json", "w") as f:
        json.dump(review, f, indent=2)

    (ev_dir / "json").mkdir(exist_ok=True)
    with open(ev_dir / "json/pass_summary.jsonl", "w") as f:
        for d in sorted(pass_dates):
            wins = [r for r in records if r["pass_date"] == d]
            rep = wins[0]
            line = {
                "pass_id": pass_map[d],
                "date": d,
                "n_windows": len(wins),
                "window_ids": [w["window_id"] for w in wins],
                "evidence_status": rep["review_disposition"]["evidence_status"],
                "Dn": rep["metric_values"]["Dn"],
                "EB": rep["metric_values"]["EB"],
            }
            f.write(json.dumps(line, default=str) + "\n")


def _write_csv(records, audit, ev_dir, pass_map):
    (ev_dir / "csv").mkdir(parents=True, exist_ok=True)

    # window_matrix.csv
    fields = [
        "window_id", "pass_id", "pass_date", "is_duration_variant", "probe",
        "sza_deg", "dp_nPa", "bz_nT", "near_occ", "bg_occ", "membership_frac",
        "s_min", "s_max", "Dn", "EB", "delta_beta", "rho_nB", "persistence",
        "spike_frac", "Dn_clean", "EB_clean", "dens_cv_near",
        "evidence_status", "seed_ref", "n_caveats",
    ]
    with open(ev_dir / "csv/window_matrix.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in records:
            w.writerow({
                "window_id": r["window_id"],
                "pass_id": r["pass_id"],
                "pass_date": r["pass_date"],
                "is_duration_variant": r["is_duration_variant"],
                "probe": r["probe"],
                "sza_deg": r["geometry_context"]["sza_deg"],
                "dp_nPa": r["upstream_summary"]["dp_nPa"],
                "bz_nT": r["upstream_summary"]["bz_gsm_nT"],
                "near_occ": r["occupancy"]["near"],
                "bg_occ": r["occupancy"]["background"],
                "membership_frac": r["data_validity"]["membership_fraction"],
                "s_min": r["occupancy"]["s_min"],
                "s_max": r["occupancy"]["s_max"],
                "Dn": r["metric_values"]["Dn"],
                "EB": r["metric_values"]["EB"],
                "delta_beta": r["metric_values"]["delta_beta"],
                "rho_nB": r["metric_values"]["rho_nB"],
                "persistence": r["metric_values"]["persistence"],
                "spike_frac": r["confounder_audit"]["spike_fraction"],
                "Dn_clean": r["confounder_audit"]["Dn_clean"],
                "EB_clean": r["confounder_audit"]["EB_clean"],
                "dens_cv_near": r["confounder_audit"]["dens_cv_near"],
                "evidence_status": r["review_disposition"]["evidence_status"],
                "seed_ref": r["review_disposition"]["seed_reference"] or "",
                "n_caveats": len(r["review_disposition"]["caveats"]),
            })

    # confounder_register.csv
    cf_fields = [
        "window_id", "pass_id", "jet_flag", "wave_flag", "transient_flag",
        "mixing_flag", "motion_flag", "grade", "spike_frac",
        "near_spikes", "bg_spikes", "Dn_clean", "EB_clean", "dens_cv_near",
    ]
    with open(ev_dir / "csv/confounder_register.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cf_fields)
        w.writeheader()
        for r in records:
            ca = r["confounder_audit"]
            w.writerow({k: ca.get(k, "") for k in cf_fields[2:]}
                       | {"window_id": r["window_id"], "pass_id": r["pass_id"]})

    # interval_audit_matrix.csv
    ia_fields = [
        "pass_id", "date", "window", "Dn_original", "EB_original",
        "spike_frac", "Dn_clean", "EB_clean", "Dn_change", "EB_change",
        "dens_cv_near", "membership",
    ]
    with open(ev_dir / "csv/interval_audit_matrix.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ia_fields)
        w.writeheader()
        for d in sorted(audit.keys()):
            a = audit[d]
            w.writerow({
                "pass_id": pass_map.get(d, "?"),
                "date": d,
                "window": a.get("window", ""),
                "Dn_original": a.get("Dn_original"),
                "EB_original": a.get("EB_original"),
                "spike_frac": a.get("spike_frac"),
                "Dn_clean": a.get("Dn_clean"),
                "EB_clean": a.get("EB_clean"),
                "Dn_change": a.get("Dn_change"),
                "EB_change": a.get("EB_change"),
                "dens_cv_near": a.get("dens_cv_near"),
                "membership": a.get("membership"),
            })


def _write_index(ev_dir, run_dir):
    (ev_dir / "index").mkdir(parents=True, exist_ok=True)
    idx = {
        "schema": "docs/EVIDENCE_REPORT_SCHEMA.md",
        "json": [str(p.relative_to(run_dir)) for p in (ev_dir / "json").glob("*")],
        "csv": [str(p.relative_to(run_dir)) for p in (ev_dir / "csv").glob("*")],
        "reports": "reports/current_bank/",
        "stage": "phase_2d",
    }
    with open(ev_dir / "index/artifact_index.json", "w") as f:
        json.dump(idx, f, indent=2)


def _write_chunks(records, ev_dir):
    (ev_dir / "chunks").mkdir(parents=True, exist_ok=True)
    chunks = []
    for r in records:
        chunks.append({
            "chunk_type": "window_evidence",
            "window_id": r["window_id"],
            "pass_id": r["pass_id"],
            "evidence_status": r["review_disposition"]["evidence_status"],
            "Dn": r["metric_values"]["Dn"],
            "EB": r["metric_values"]["EB"],
            "rho_nB": r["metric_values"]["rho_nB"],
            "dp_nPa": r["upstream_summary"]["dp_nPa"],
            "bz_nT": r["upstream_summary"]["bz_gsm_nT"],
            "near_occ": r["occupancy"]["near"],
            "bg_occ": r["occupancy"]["background"],
            "spike_frac": r["confounder_audit"]["spike_fraction"],
            "Dn_clean": r["confounder_audit"]["Dn_clean"],
            "EB_clean": r["confounder_audit"]["EB_clean"],
            "caveats": r["review_disposition"]["caveats"],
        })
    with open(ev_dir / "chunks/bank_report_chunks.json", "w") as f:
        json.dump(chunks, f, indent=2, default=str)


def _generate_bank_report(records, pass_dates, pass_map, report_dir):
    """Generate human-facing bank report and per-pass pages."""
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "passes").mkdir(exist_ok=True)

    # INDEX.md
    lines = [
        "# Evidence Report — Current Comparator Bank",
        "",
        "| Document | Path |",
        "|---|---|",
        "| Bank report | [bank_report.md](bank_report.md) |",
    ]
    for d in sorted(pass_dates):
        pid = pass_map[d]
        wins = [r for r in records if r["pass_date"] == d]
        rep = wins[0]
        lines.append(
            f"| {pid} ({d}) | [passes/{rep['window_id']}.md](passes/{rep['window_id']}.md) |"
        )
    lines.extend([
        "",
        "All windows are measurement-model-valid near-MP comparator windows.",
        "No window is labeled or classified.",
    ])
    (report_dir / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")

    # bank_report.md
    blines = [
        "# Comparator Bank Report",
        "",
        f"**Windows:** {len(records)} | **Passes:** {len(pass_dates)} | **Probe:** THD",
        "",
        "## Evidence matrix",
        "",
        "| Pass | Date | Window | Status | SZA | Dp | Bz | Near% | BG% | Dn | EB | Spike% | Dn_clean | EB_clean |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for r in sorted(records, key=lambda x: (x["pass_date"], x["window_id"])):
        rho_s = f"{r['metric_values']['rho_nB']:.2f}" if r["metric_values"]["rho_nB"] is not None else "N/A"
        dn_c = f"{r['confounder_audit']['Dn_clean']:.2f}" if r["confounder_audit"]["Dn_clean"] is not None else ""
        eb_c = f"{r['confounder_audit']['EB_clean']:.2f}" if r["confounder_audit"]["EB_clean"] is not None else ""
        sp = f"{r['confounder_audit']['spike_fraction']:.0%}" if r["confounder_audit"]["spike_fraction"] is not None else ""
        blines.append(
            f"| {r['pass_id']} | {r['pass_date']} | {r['window_id']} | "
            f"{r['review_disposition']['evidence_status']} | "
            f"{r['geometry_context']['sza_deg']:.0f} | "
            f"{r['upstream_summary']['dp_nPa']:.1f} | "
            f"{r['upstream_summary']['bz_gsm_nT']:+.1f} | "
            f"{r['occupancy']['near']:.0%} | {r['occupancy']['background']:.0%} | "
            f"{r['metric_values']['Dn']:.2f} | {r['metric_values']['EB']:.2f} | "
            f"{sp} | {dn_c} | {eb_c} |"
        )

    blines.extend([
        "",
        "## Confounder summary",
        "",
        "| Window | Jet | Wave | Transient | Mixing | Motion | Grade |",
        "|---|---|---|---|---|---|---|",
    ])
    for r in records:
        ca = r["confounder_audit"]
        def _fs(v):
            if v is True: return "TRUE"
            if v is False: return "false"
            return "UNKNOWN"
        blines.append(
            f"| {r['window_id']} | {_fs(ca['jet_flag'])} | {_fs(ca['wave_flag'])} | "
            f"{_fs(ca['transient_flag'])} | {_fs(ca['mixing_flag'])} | "
            f"{_fs(ca['motion_flag'])} | {ca['grade']} |"
        )

    blines.extend([
        "",
        "## Naming discipline",
        "",
        "Every window is a **measurement-model-valid near-MP comparator window**.",
        "Evidence status (clean_core / cautious / excluded) is stage-local bookkeeping only.",
    ])
    (report_dir / "bank_report.md").write_text("\n".join(blines), encoding="utf-8")

    # Per-pass pages (one per representative window)
    seen_dates = set()
    for r in sorted(records, key=lambda x: x["pass_date"]):
        d = r["pass_date"]
        if d in seen_dates and r["is_duration_variant"]:
            continue
        seen_dates.add(d)

        plines = [
            f"# {r['pass_id']} — {d} ({r['window_id']})",
            "",
            f"**Status:** {r['review_disposition']['evidence_status']}",
            f"**Seed:** {r['review_disposition']['seed_reference'] or 'none'}",
            "",
            "## Identity",
            f"- Window: `{r['window_id']}`",
            f"- Pass: {r['pass_id']} ({d})",
            f"- Probe: {r['probe']}",
            f"- Time: {r['time_start']} to {r['time_end']}",
            f"- Duration variant: {'yes' if r['is_duration_variant'] else 'no'}",
            "",
            "## Geometry",
            f"- SZA: {r['geometry_context']['sza_deg']:.1f} deg",
            f"- Position GSM: {r['geometry_context']['position_gsm_re']}",
            "",
            "## Upstream",
            f"- Dp: {r['upstream_summary']['dp_nPa']:.1f} nPa",
            f"- Bz: {r['upstream_summary']['bz_gsm_nT']:+.1f} nT",
            f"- Ma: {r['upstream_summary']['mach_alfven']:.1f}",
            "",
            "## Measurement model",
            f"- MP: {r['measurement_model']['mp_model']} ({r['measurement_model']['mp_standoff_re']:.2f} Re)",
            f"- BS: {r['measurement_model']['bs_model']} ({r['measurement_model']['bs_standoff_re']:.2f} Re)",
            f"- Boundary averaging: {r['measurement_model']['boundary_averaging']}",
            "",
            "## Occupancy",
            f"- Very-near: {r['occupancy']['very_near']:.1%}",
            f"- Near: {r['occupancy']['near']:.1%}",
            f"- Background: {r['occupancy']['background']:.1%}",
            f"- s range: [{r['occupancy']['s_min']:.3f}, {r['occupancy']['s_max']:.3f}]",
            "",
            "## Data validity",
            f"- Membership: {r['data_validity']['membership_fraction']:.1%}",
            f"- Artifacts: {r['data_validity']['n_artifact_suspect']}",
            f"- Unknown: {r['data_validity']['n_unknown']}",
            "",
            "## Metrics",
            f"- Dn: {r['metric_values']['Dn']:.3f}" if r["metric_values"]["Dn"] else "- Dn: null",
            f"- EB: {r['metric_values']['EB']:.3f}" if r["metric_values"]["EB"] else "- EB: null",
            f"- delta_beta: {r['metric_values']['delta_beta']:.2f}" if r["metric_values"]["delta_beta"] else "- delta_beta: null",
            f"- rho_nB: {r['metric_values']['rho_nB']:.3f}" if r["metric_values"]["rho_nB"] is not None else "- rho_nB: null",
            f"- persistence: {r['metric_values']['persistence']:.2f}" if r["metric_values"]["persistence"] is not None else "- persistence: null",
            "",
            "## Confounder audit",
        ]
        ca = r["confounder_audit"]
        if ca["spike_fraction"] is not None:
            plines.append(f"- Spike fraction: {ca['spike_fraction']:.1%}")
            plines.append(f"- Dn after spike removal: {ca['Dn_clean']}" if ca["Dn_clean"] else "- Dn_clean: N/A")
            plines.append(f"- EB after spike removal: {ca['EB_clean']}" if ca["EB_clean"] else "- EB_clean: N/A")
        if ca["dens_cv_near"] is not None:
            plines.append(f"- Near-bin density CV: {ca['dens_cv_near']:.3f}")
        plines.append(f"- Grade: {ca['grade']} ({ca['grade_note']})")

        if r["review_disposition"]["caveats"]:
            plines.extend(["", "## Caveats"])
            for c in r["review_disposition"]["caveats"]:
                plines.append(f"- {c}")

        plines.extend(["", "## QC report", f"See `qc_{r['window_id']}.png` in run directory."])

        (report_dir / "passes" / f"{r['window_id']}.md").write_text(
            "\n".join(plines), encoding="utf-8"
        )


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate evidence-report package")
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args(argv)

    run_dir = Path(args.run_dir)
    ev_dir = run_dir / "evidence"

    with open(run_dir / "all_encounters.json") as f:
        bank = json.load(f)
    audit = {}
    audit_path = run_dir / "phase2c_interval_audit.json"
    if audit_path.exists():
        with open(audit_path) as f:
            audit = json.load(f)
    with open(run_dir / "run_manifest.json") as f:
        manifest = json.load(f)

    pass_dates = sorted(set(w["time_start"][:10] for w in bank))
    pass_map = {d: f"P{i+1}" for i, d in enumerate(pass_dates)}
    variants_map = {}
    for w in bank:
        d = w["time_start"][:10]
        variants_map.setdefault(d, []).append(w["encounter_id"])

    records = _build_records(bank, audit, manifest, pass_map, variants_map)

    _write_json(records, ev_dir, manifest, pass_dates, pass_map)
    _write_csv(records, audit, ev_dir, pass_map)
    _write_index(ev_dir, run_dir)
    _write_chunks(records, ev_dir)
    _generate_bank_report(records, pass_dates, pass_map, Path("reports/current_bank"))

    log.info("Evidence package generated: %d records", len(records))
    log.info("  JSON: %s", ev_dir / "json")
    log.info("  CSV: %s", ev_dir / "csv")
    log.info("  Reports: reports/current_bank/")
    print(f"Evidence package: {len(records)} records, {len(pass_dates)} passes")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
