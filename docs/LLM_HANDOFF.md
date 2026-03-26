# LLM Handoff — PDL Pilot Pipeline

**Load this first when resuming in a new session.**

---

## One-line summary

9 measurement-model-valid THEMIS windows across 7 passes, now reviewed: Dn spans 0.12–2.31, EB 0.80–4.22, ρ universally negative. 4 provisional planning seeds selected. Duration variants are consistent within passes. No labels or thresholds assigned.

## Current milestone

Phase 2D detector-readiness review complete. **CONDITIONAL GO** for Phase 3A bounded threshold exploration. N=6 interpretable passes (4 clean + 2 cautious). P7 excluded.

## Window bank (9 windows / 7 passes)

| ID | Date | SZA | Dp | Bz | Near% | BG% | Dn | EB | ρ | Seed? |
|---|---|---|---|---|---|---|---|---|---|---|
| usable_aug18_6h | 2008-08-18 | 22° | 4.2 | +0.3 | 16% | 48% | 0.12 | 2.49 | -0.46 | **A** |
| usable_aug18_8h | 2008-08-18 | 22° | 3.6 | +0.1 | 17% | 12% | 0.88 | 2.08 | N/A | (variant) |
| usable_sep03_6h | 2008-09-03 | 14° | 3.5 | +0.9 | 17% | 27% | 2.31 | 0.82 | -0.52 | **C** |
| usable_sep03_8h | 2008-09-03 | 12° | 3.5 | +2.6 | 13% | 40% | 2.07 | 0.80 | -0.51 | (variant) |
| usable_sep13_09_6h | 2009-09-13 | 17° | 3.1 | -1.4 | 17% | 47% | 0.39 | 1.96 | -0.90 | **D** |
| usable_sep20_09_6h | 2009-09-20 | 10° | 3.0 | +1.4 | 9% | 46% | 0.97 | 1.48 | -0.63 | **B** |
| usable_sep26_09_10h | 2009-09-26 | 4° | 3.0 | +0.9 | 18% | 40% | 0.94 | 1.96 | -0.91 | |
| usable_sep27_09_10h | 2009-09-27 | 4° | 3.1 | -1.7 | 16% | 57% | 1.31 | 1.23 | -0.72 | |
| usable_oct24_09_6h | 2009-10-24 | 20° | 4.2 | -0.5 | 14% | 65% | 2.19 | 4.22 | -0.66 | |

All remain "measurement-model-valid near-MP comparator windows." None labeled.

## Key review findings

1. **Dn and EB approximately inversely related** — observed pattern, not a diagnostic rule
2. **ρ(n,B) negative across all bank windows** — but universality within this bank means ρ has no discriminative power here; it may reflect a property common to all compressed-sheath comparator conditions
3. **Duration variants consistent** — within-pass Dn spread (0.50) ≪ between-pass range (1.80)
4. **Effective N = 7** independent passes, not 9 windows

## Scientific risks (see METRIC_BEHAVIOR_REVIEW.md for details)

- Single probe (THD only), Dp > 3 nPa selection bias, encounter-averaged boundaries, universal ρ < 0 is non-discriminative, confounder flags incomplete (transient/mixing = UNKNOWN)

## Seed slate (planning only — not labels)

| Seed | Window | Dn | EB | Operational description |
|---|---|---|---|---|
| A | aug18_6h | 0.12 | 2.49 | Lowest Dn, highest EB among seeds |
| B | sep20_09_6h | 0.97 | 1.48 | Dn near unity, moderate EB |
| C | sep03_6h | 2.31 | 0.82 | Highest Dn, EB below unity |
| D | sep13_09_6h | 0.39 | 1.96 | Most negative ρ in bank |

## Key files

| What | Where |
|---|---|
| Comparator atlas | `docs/COMPARATOR_ATLAS.md` |
| Seed dossier | `docs/SEED_DOSSIER.md` |
| Metric review (tightened) | `docs/METRIC_BEHAVIOR_REVIEW.md` |
| Window bank config | `configs/pilot_live_usable.yaml` |
| Window bank summary | `docs/WINDOW_BANK_SUMMARY.md` |
| Phase 2a state | `docs/PHASE_2A_STATE.md` |
| Review artifacts | `runs/20260326T040343Z_d0425fd4/` |

## Commands

```bash
# Run the bank
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live_usable.yaml

# Run the metric review
PYTHONPATH=src python -m pdl_pilot.cli.metric_review --run-dir runs/20260326T040343Z_d0425fd4

# Tests (117 pass, 1 skip)
PYTHONPATH=src python -m pytest tests/ -v
```

## Phase 2B audit gate (2026-03-26)

**Question:** Is the bank clean enough for a later bounded detector-readiness stage?

**Answer: CONDITIONAL GO**

Passes: dual-bin leverage confirmed, spatial structure survives shuffled-s null, duration variants consistent, membership ≥85%, primary metrics insensitive to very-near bin, naming conservative.

Conditions carried forward:
1. Universal jet triggering (all 9 windows) — jet_flag has zero discriminative power; threshold may need recalibration for long windows
2. transient_flag and mixing_flag remain UNKNOWN — max grade = Silver
3. THD-only, Dp > 3 nPa selection bias — bank does not represent full sheath population
4. Effective N = 7, not 9
5. ρ universally negative — non-discriminative in this bank
6. ±1 nPa Dp shifts boundaries ~1 Re — moderate upstream sensitivity (deferred)

**Full audit:** `docs/PHASE_2B_AUDIT.md`
**Selection logic:** `docs/SELECTION_FUNCTION_AUDIT.md`
**Wording audit:** `docs/WORDING_DRIFT_AUDIT.md`
**Machine-readable:** `runs/20260326T040343Z_d0425fd4/phase2b_audit_summary.json`

## Phase 2C interval audit (2026-03-26)

**Question:** Does the 7-pass bank contain a sufficiently clean subset after interval-level confounder scrutiny?

**Answer: YES, with conditions**

**Clean core (4 passes):** P2 (Sep 3), P4 (Sep 20), P5 (Sep 26), P6 (Sep 27). Metrics survive leave-spike-out. Low-to-moderate density noise.

**Usable with caveats (2 passes):** P1 (Aug 18, seed_A: high density noise CV=0.93), P3 (Sep 13, seed_D: EB partially spike-dependent, Δ=0.50).

**Excluded (1 pass):** P7 (Oct 24) — spike-dominated. Dn collapses 2.19→0.67, EB 4.22→0.97 after spike removal.

**Seed status update:**
- seed_A (P1): usable with noise caveat
- seed_B (P4): **cleanest** — unchanged
- seed_C (P2): clean — unchanged
- seed_D (P3): weakened — EB partially spike-dependent

**Full audit:** `docs/PHASE_2C_CONFOUNDER_CLOSURE.md`
**Pass cards:** `docs/PASS_INTERVAL_AUDIT.md`
**Machine-readable:** `runs/20260326T040343Z_d0425fd4/phase2c_interval_audit.json`

## Key files (updated)

| What | Where |
|---|---|
| **Phase 2C confounder closure** | `docs/PHASE_2C_CONFOUNDER_CLOSURE.md` |
| **Pass interval audit** | `docs/PASS_INTERVAL_AUDIT.md` |
| Phase 2B audit | `docs/PHASE_2B_AUDIT.md` |
| Seed dossier (updated) | `docs/SEED_DOSSIER.md` |
| Comparator atlas | `docs/COMPARATOR_ATLAS.md` |
| Window bank config | `configs/pilot_live_usable.yaml` |
| Interval audit data | `runs/20260326T040343Z_d0425fd4/phase2c_interval_audit.json` |

## Phase 2D detector-readiness review (2026-03-26)

**Question:** Is the post-Phase-2C bank sufficient to justify a later bounded threshold-exploration stage?

**Answer: CONDITIONAL GO**

**Clean core (4 passes):** P2, P4, P5, P6. Dn 0.94–2.31, EB 0.82–1.96. Confounder-tested.
**Cautious (2 passes):** P1, P3. Extend Dn range to 0.12–0.39 but carry density-noise and EB-spike caveats.
**Excluded (1 pass):** P7. Spike-dominated.
**Interpretable N = 6** (4 clean + 2 cautious). P7 excluded.

**Key insufficiency:** Clean core alone has no pass with Dn < 0.5. The low-Dn range relies entirely on cautious passes.

**Tolerability of unresolved issues:**
- Universal negative ρ: acceptable caveat (non-discriminative, cannot be used as threshold)
- Universal jet triggering: serious warning (long-window artifact; metrics survive in clean core)
- Transient/mixing/boundary-motion UNKNOWN: serious warning, tolerable for bounded exploration
- THD-only / Dp > 3 nPa bias: serious warning; results are regime-specific, not universal
- Encounter-averaged boundaries: acceptable caveat

**Recommended next stage:** Phase 3A — Bounded Metric-Threshold Exploration
- Identify provisional Dn/EB threshold candidates (descriptive, not classification)
- Thresholds are exploratory starting points, not frozen decisions
- ρ excluded as discriminative metric
- P7 excluded; P1/P3 usable with stated caveats only

**Full review:** `docs/PHASE_2D_DETECTOR_READINESS_REVIEW.md`
**Evidence matrix:** `docs/READINESS_EVIDENCE_MATRIX.md`

## Evidence-report package (2026-03-26)

A reusable evidence package now exists with two-layer design (factual + review).

**Machine-readable:** `runs/20260326T040343Z_d0425fd4/evidence/`
- `json/bank_manifest.json` — full per-window structured records (9 windows)
- `json/bank_summary.json` — compact bank statistics
- `json/review_layers.json` — stage-local dispositions only
- `json/pass_summary.jsonl` — one line per pass
- `csv/window_matrix.csv` — wide-format metrics + context
- `csv/confounder_register.csv` — per-window confounder flags
- `csv/interval_audit_matrix.csv` — spike sensitivity data
- `chunks/bank_report_chunks.json` — AI-consumable chunks
- `index/artifact_index.json` — links all artifacts

**Human-facing:** `reports/current_bank/`
- `INDEX.md` — navigation
- `bank_report.md` — cross-pass evidence matrix + confounder table
- `passes/<window_id>.md` — per-pass evidence sheets (7 pages)
- `figures/cross_pass_summary.png` — Dn-EB scatter, spike sensitivity, occupancy

**Schema:** `docs/EVIDENCE_REPORT_SCHEMA.md`
**Generator:** `src/pdl_pilot/cli/generate_evidence.py`
**Tests:** 124 pass, 1 skip

## Key files (updated)

| What | Where |
|---|---|
| **Evidence schema** | `docs/EVIDENCE_REPORT_SCHEMA.md` |
| **Evidence generator** | `src/pdl_pilot/cli/generate_evidence.py` |
| **Bank manifest (JSON)** | `runs/.../evidence/json/bank_manifest.json` |
| **Bank report** | `reports/current_bank/bank_report.md` |
| **Per-pass pages** | `reports/current_bank/passes/` |
| Phase 2D readiness review | `docs/PHASE_2D_DETECTOR_READINESS_REVIEW.md` |
| Window bank config | `configs/pilot_live_usable.yaml` |

## Commands

```bash
# Generate evidence package from current run
PYTHONPATH=src python -m pdl_pilot.cli.generate_evidence --run-dir runs/20260326T040343Z_d0425fd4

# Run all tests (124 pass, 1 skip)
PYTHONPATH=src python -m pytest tests/ -v
```

## Next step (do not implement)

Phase 3A — Bounded Metric-Threshold Exploration: examine how provisional Dn and EB thresholds descriptively separate the 6 interpretable passes, without assigning labels or freezing decisions. Requires human review of seed time series first.
