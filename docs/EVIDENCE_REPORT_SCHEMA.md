# Evidence Report Schema

**Version:** 1.0
**Date:** 2026-03-26
**Stage:** Post-Phase-2D bounded exploration

---

## Purpose

This schema defines the structure of the reusable evidence-report package for the current comparator bank. It is designed so that humans, scripts, and later AI conversations can consume the same underlying data without ambiguity about what is factual vs what is stage-local judgment.

---

## Two-layer design

### Factual layer (stable across stages)

Contains measurements, geometry, upstream context, occupancy, membership, metrics, and interval-audit results. These do not change when review judgments are updated.

**Field naming convention:** Use descriptive, conservative names.

Allowed: `window_id`, `pass_id`, `geometry_context`, `metric_values`, `occupancy`, `data_validity`, `confounder_audit`

Forbidden: `label`, `class`, `is_pdl`, `positive`, `negative`, `baseline`, `ground_truth`

### Review layer (stage-local, may change)

Contains current evidence-status assignments (clean_core / cautious / excluded), seed references, caveat severity notes, and planning remarks. Stored in a separate `review_disposition` field, never baked into factual field names.

---

## Per-window record schema

```
{
  "window_id": str,               # encounter_id
  "pass_id": str,                 # e.g. "P2"
  "pass_date": str,               # ISO date
  "variant_group_id": str,        # e.g. "P1" for duration variants sharing a pass
  "is_duration_variant": bool,
  "probe": str,
  "time_start": str,
  "time_end": str,
  "geometry_context": {
    "sza_deg": float,
    "mlt_hours": float,
    "position_gsm_re": [float, float, float],
    "abs_z_re": float
  },
  "upstream_summary": {
    "dp_nPa": float,
    "bz_gsm_nT": float,
    "mach_alfven": float,
    "stability_flag": str
  },
  "measurement_model": {
    "mp_model": str,
    "bs_model": str,
    "mp_standoff_re": float,
    "bs_standoff_re": float,
    "distance_direction": str,
    "boundary_averaging": "encounter_averaged"
  },
  "data_validity": {
    "membership_fraction": float,
    "n_artifact_suspect": int,
    "n_unknown": int,
    "masked_fractions": {}
  },
  "occupancy": {
    "very_near": float,
    "near": float,
    "background": float,
    "s_min": float,
    "s_max": float,
    "s_range": float
  },
  "metric_values": {
    "Dn": float | null,
    "EB": float | null,
    "delta_beta": float | null,
    "rho_nB": float | null,
    "persistence": float | null,
    "ptot_smoothness": float | null,
    "fluctuation_amp": float | null
  },
  "confounder_audit": {
    "jet_flag": true | false | null,
    "wave_flag": true | false | null,
    "transient_flag": null,
    "mixing_flag": null,
    "motion_flag": true | false | null,
    "spike_fraction": float,
    "near_spikes": int,
    "bg_spikes": int,
    "Dn_clean": float | null,
    "EB_clean": float | null,
    "dens_cv_near": float | null,
    "grade": str,
    "grade_note": str
  },
  "review_disposition": {
    "evidence_status": "clean_core" | "cautious" | "excluded",
    "seed_reference": str | null,
    "caveats": [str],
    "stage": "phase_2d"
  },
  "source_run_id": str,
  "config_hash": str
}
```

---

## Cross-pass summary artifacts

| Artifact | Format | Purpose |
|---|---|---|
| `window_matrix.csv` | CSV (wide) | One row per window, all metrics + context |
| `pass_matrix.csv` | CSV (wide) | One row per pass (representative window) |
| `bin_stats_long.csv` | CSV (long) | Per-window, per-bin summary statistics |
| `confounder_register.csv` | CSV | Per-window confounder flag status |
| `bank_manifest.json` | JSON | Full bank registry with all fields |
| `bank_summary.json` | JSON | Compact summary counts and ranges |
| `review_layers.json` | JSON | Stage-local review dispositions only |
| `artifact_index.json` | JSON | Links to all generated artifacts |

---

## Figure conventions

- Timeline figures: density, |B|, beta, Pdyn, s(t) with bin shading and spike markers
- Profile figures: quantity vs s with bin boundaries and occupancy annotations
- All figures use encounter_id in filename
- All figures have conservative captions (no label language)

---

## Phase 3A schema extensions

### Additional artifacts (Phase 3A)

| Artifact | Format | Purpose |
|---|---|---|
| `pass_matrix.csv` | CSV (wide) | One row per pass, representative metrics |
| `figure_manifest.json` | JSON | Registry of all figures with `question_answered` |
| `claim_map.json` | JSON | Registry of all descriptive claims with evidence basis and caveats |
| `pass_report_chunks.json` | JSON | AI-consumable per-pass evidence chunks |
| `RUN_REVIEW_PACKET.md` | Markdown | Self-contained run-level review document |
| `RUN_REVIEW_PACKET_chunks.json` | JSON | Machine-readable review packet |

### Review-packet field conventions

- `operational_role`: "comparator_window" (stable)
- `comparison_scope`: "phase_3a_dneb" (stage-local)
- `primary_vs_secondary_evidence`: determined by `review_disposition.evidence_status`
- `caveat_register`: stored per-window in `review_disposition.caveats`

### Deferred artifacts

- `bin_stats_long.csv`: deferred because current run products do not expose per-bin profile-level exports
- `profile_long.csv`: deferred for same reason

---

## Naming discipline

Every window is a "measurement-model-valid near-MP comparator window."
Evidence status (clean_core / cautious / excluded) is bookkeeping, not classification.
No figure title, caption, or field name may use: PDL-positive, non-PDL, baseline, control, truth, label, dev-set.
