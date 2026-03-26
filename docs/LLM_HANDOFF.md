# LLM Handoff — PDL Pilot Pipeline

**Load this first when resuming in a new session.**

---

## One-line summary

7 measurement-model-valid real THEMIS windows across 4 orbital passes and 2 seasons, all producing non-null core metrics with dual-bin leverage. Two distinct metric patterns observed (compressed-sheath vs layer-like). No window classified as PDL or non-PDL.

## Current milestone

Phase 2a frozen: window bank stable, docs frozen, 111 tests passing.

## Window bank (7 windows)

| ID | Date | SZA | Dp | Bz | Near% | BG% | Dn | EB | ρ |
|---|---|---|---|---|---|---|---|---|---|
| usable_aug18_6h | 2008-08-18 | 22° | 4.2 | +0.3 | 16% | 48% | 0.12 | 2.49 | -0.46 |
| usable_sep03_6h | 2008-09-03 | 14° | 3.5 | +0.9 | 17% | 27% | 2.31 | 0.82 | -0.52 |
| usable_sep03_8h | 2008-09-03 | 12° | 3.5 | +2.6 | 13% | 40% | 2.07 | 0.80 | -0.51 |
| usable_sep13_09_6h | 2009-09-13 | 17° | 3.1 | -1.4 | 17% | 47% | 0.39 | 1.96 | -0.90 |
| usable_sep26_09_10h | 2009-09-26 | 4° | 3.0 | +0.9 | 18% | 40% | 0.94 | 1.96 | -0.91 |
| usable_oct24_09_6h | 2009-10-24 | 20° | 4.2 | -0.5 | 14% | 65% | 2.19 | 4.22 | -0.66 |
| usable_aug18_8h | 2008-08-18 | 22° | 3.6 | +0.1 | 17% | 12% | 0.88 | 2.08 | N/A |

All are "measurement-model-valid near-MP comparator windows." None is labeled.

## Constraint model (three layers)
- **Layer A** (strong): dual-bin leverage, dayside geometry, QC intact, conservative naming
- **Layer B** (ranking only): SZA/Dp preferences, window durations, non-radial IMF preference
- **Layer C** (deferred): PDL labels, thresholds, dev-set, MMS, priors

## Key files
| What | Where |
|---|---|
| Window bank config | `configs/pilot_live_usable.yaml` |
| Window bank summary | `docs/WINDOW_BANK_SUMMARY.md` |
| Phase state | `docs/PHASE_2A_STATE.md` |
| Family manifest | `configs/pilot_window_families.yaml` |
| Canonical run | `runs/20260326T033744Z_9f985ab9/` |

## Commands
```bash
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live_usable.yaml
PYTHONPATH=src python -m pytest tests/ -v
```

## Next step (do not implement)
Expand the bank to ~10-15 passes by scanning THD 2009 remaining candidates (Sep 3, Sep 27, and others identified in the systematic scan). Then begin threshold exploration on the expanded bank.
