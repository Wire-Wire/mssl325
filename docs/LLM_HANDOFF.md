# LLM Handoff — PDL Pilot Pipeline

**Load this first when resuming in a new session.**

---

## One-line summary

9 measurement-model-valid THEMIS windows across 7 passes, now reviewed: Dn spans 0.12–2.31, EB 0.80–4.22, ρ universally negative. 4 provisional planning seeds selected. Duration variants are consistent within passes. No labels or thresholds assigned.

## Current milestone

Metric-behavior review complete. 4-seed provisional stratification slate produced.

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

## Next step (do not implement)

Human-supervised review of the 4 seed windows to decide whether the current bank is sufficient for bounded threshold exploration, or whether additional passes under different upstream conditions (lower Dp, different Bz regimes) are needed first. This decision requires human judgment — it is not automatable from the current bank alone.
