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

1. **Dn and EB inversely related** — low-Dn windows have high EB, consistent with pileup physics
2. **ρ(n,B) universally negative** — the most stable metric in the bank
3. **Duration variants consistent** — within-pass Dn spread (0.50) ≪ between-pass range (1.80)
4. **7 effective independent observations**, not 9 (2 passes have duration variants)

## Seed slate (planning only)

| Seed | Window | Dn | EB | Why |
|---|---|---|---|---|
| A | aug18_6h | 0.12 | 2.49 | Strongest depletion + enhancement |
| B | sep20_09_6h | 0.97 | 1.48 | Near-neutral behavior |
| C | sep03_6h | 2.31 | 0.82 | Strongest enhancement (compressed-sheath) |
| D | sep13_09_6h | 0.39 | 1.96 | Strongest anti-correlation (ρ=-0.90) |

## Key files

| What | Where |
|---|---|
| Window bank config | `configs/pilot_live_usable.yaml` |
| Metric review doc | `docs/METRIC_BEHAVIOR_REVIEW.md` |
| Seed stratification | `docs/MINI_SEED_STRATIFICATION.md` |
| Review script | `src/pdl_pilot/cli/metric_review.py` |
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

Bounded detector-v0 preparation: use the 4 seeds as a starting point for supervised threshold exploration on Dn and EB. This requires human judgment to decide initial threshold candidates — it is NOT automatable from the current bank alone.
