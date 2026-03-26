# LLM Handoff — PDL Pilot Pipeline

**Load this first when resuming in a new session.**

---

## One-line summary

9 measurement-model-valid real THEMIS windows across 7 distinct orbital passes (2008 + 2009 THD), all producing non-null core metrics with dual-bin leverage. Dn ranges 0.12–2.31, EB 0.80–4.22. No window classified. Bank is ready for bounded metric-behavior review.

## Current milestone

Phase 2a final: 9 windows / 7 passes / 111 tests passing.

## Window bank

| ID | Date | SZA | Dp | Bz | Near% | BG% | Dn | EB | ρ |
|---|---|---|---|---|---|---|---|---|---|
| usable_aug18_6h | 2008-08-18 | 22° | 4.2 | +0.3 | 16% | 48% | 0.12 | 2.49 | -0.46 |
| usable_sep03_6h | 2008-09-03 | 14° | 3.5 | +0.9 | 17% | 27% | 2.31 | 0.82 | -0.52 |
| usable_sep03_8h | 2008-09-03 | 12° | 3.5 | +2.6 | 13% | 40% | 2.07 | 0.80 | -0.51 |
| usable_sep13_09_6h | 2009-09-13 | 17° | 3.1 | -1.4 | 17% | 47% | 0.39 | 1.96 | -0.90 |
| usable_sep20_09_6h | 2009-09-20 | 10° | 3.0 | +1.4 | 9% | 46% | 0.97 | 1.48 | -0.63 |
| usable_sep26_09_10h | 2009-09-26 | 4° | 3.0 | +0.9 | 18% | 40% | 0.94 | 1.96 | -0.91 |
| usable_sep27_09_10h | 2009-09-27 | 4° | 3.1 | -1.7 | 16% | 57% | 1.31 | 1.23 | -0.72 |
| usable_oct24_09_6h | 2009-10-24 | 20° | 4.2 | -0.5 | 14% | 65% | 2.19 | 4.22 | -0.66 |
| usable_aug18_8h | 2008-08-18 | 22° | 3.6 | +0.1 | 17% | 12% | 0.88 | 2.08 | N/A |

All are "measurement-model-valid near-MP comparator windows." None is labeled.

## Key files

| What | Where |
|---|---|
| Window bank config | `configs/pilot_live_usable.yaml` |
| Window bank summary | `docs/WINDOW_BANK_SUMMARY.md` |
| Phase state | `docs/PHASE_2A_STATE.md` |
| Canonical run | `runs/20260326T040343Z_d0425fd4/` |

## Commands

```bash
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live_usable.yaml
PYTHONPATH=src python -m pytest tests/ -v
```

## Next step (do not implement)

Bounded metric-behavior review: systematically compare how Dn, EB, Δβ, ρ vary across the 7 passes and correlate with upstream conditions, without defining thresholds or assigning labels. This would be the first controlled scientific step beyond window-bank construction.
