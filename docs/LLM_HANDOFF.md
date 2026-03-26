# LLM Handoff — PDL Pilot Pipeline (First Usable Real Science Runs)

**Load this first when resuming in a new session.**

---

## One-line summary

First usable real THEMIS science windows achieved: THD Sep 3 2008, compressed sheath (Dp~3.5 nPa), s spans 0.0–0.69, both near (17%) and background (27%) bins populated, producing non-null core metrics (Dn=2.3, EB=0.82, rho=-0.52) — the measurement model works end-to-end on real data.

## Current milestone

- Phase 1 (synthetic MVP): **done**
- Phase 1.5 (dual-source bridge): **done**
- Phase 1.5 hardening (honest science interface): **done**
- Science pilot curation + first real runs: **done, with caveats**
- Window-family expansion + first usable runs: **done — metrics produced**
- Phase 2 (threshold tuning, dev set): **not started**

## What this phase added

1. **Window-family workflow** (`configs/pilot_window_families.yaml` + `src/pdl_pilot/cli/validate_families.py`): duration-ladder testing of seed windows with per-family scoring.
2. **Key discovery**: Oct 2008 THD windows (apogee 11.6 Re) NEVER reach background bin regardless of duration — the sheath is too wide at low Dp. Confirmed as controlled negative.
3. **Solution**: Found that THD Sep 3 2008 had elevated Dp (3-7 nPa) compressing the sheath boundaries inward. Same orbital range now spans s=0.0–0.69.
4. **Usable science config** (`configs/pilot_live_usable.yaml`): three window variants of Sep 3 2008, all producing PASS with real metrics.
5. **9 new tests** for family workflow (111 total, all pass).

## First usable real pilot results

| Window | Duration | SZA | s range | Near% | BG% | Dn | EB | Δβ | ρ | Grade |
|---|---|---|---|---|---|---|---|---|---|---|
| usable_sep03_6h | 6h | 13.8° | 0.000–0.674 | 16.9% | 26.7% | 2.31 | 0.82 | +1.66 | -0.52 | Silver |
| usable_sep03_8h | 8h | 12.0° | 0.000–0.664 | 13.1% | 39.7% | 2.07 | 0.80 | +1.70 | -0.51 | Silver |
| usable_sep03_5h | 5h | 14.9° | 0.000–0.689 | 18.5% | 21.0% | 2.87 | 0.80 | +2.06 | -0.63 | Silver |

**Science interpretation**: Dn > 1 and EB < 1 indicate density ENHANCEMENT and B REDUCTION near MP — the opposite of a PDL. This is expected for compressed-sheath conditions (high Dp, northward Bz). These are NOT PDL candidates — they are measurement-model validation windows demonstrating the pipeline works.

## Key insight for next phase

The dual-bin measurement model requires that encounter-averaged Dp is high enough to compress the sheath so that the spacecraft's orbital range spans both s-bins. This means:
- **Low-Dp passes** (Dp < 2 nPa): sheath too wide → spacecraft stays in very-near/near only
- **High-Dp passes** (Dp > 3 nPa): compressed sheath → both bins accessible
- **Actual PDL candidates** need moderate Dp + southward Bz (weaker reconnection → more pileup)

## Frozen decisions (unchanged)

Encounter unit, s-mapping formula, Shue/Merka boundaries, dual near bins, IMF-agnostic detection, detector backbone, QC structural, provenance-first.

## Provisional choices (updated)

- Encounter windows: 5-8 hours needed for full sheath traversal
- Resampling cadence: 10 s for multi-hour windows (was 3 s)
- Max gap: 60 s for long windows (was 30 s)
- Dp threshold for usable windows: ~3+ nPa (empirical observation, not frozen)

## Key files

| What | Where |
|---|---|
| Family manifest | `configs/pilot_window_families.yaml` |
| Family validation CLI | `src/pdl_pilot/cli/validate_families.py` |
| Usable science config | `configs/pilot_live_usable.yaml` |
| Latest usable run | `runs/20260326T021017Z_c05767ec/` |
| Family tests | `tests/test_families.py` |

## Commands

```bash
# Family duration-ladder validation
PYTHONPATH=src python -m pdl_pilot.cli.validate_families --config configs/pilot_window_families.yaml

# Usable science pilot run
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live_usable.yaml

# All tests (111 pass, 1 skip)
PYTHONPATH=src python -m pytest tests/ -v
```

## Next step (do not implement)

Find encounter windows under moderate Dp (2-4 nPa) with southward Bz where actual PDL-like signatures (Dn < 1, EB > 1, Δβ < 0, rho < 0) might appear. The Sep 3 windows demonstrate the measurement model works but show compressed-sheath signatures, not PDL. A handful of southward-Bz + moderate-Dp windows from THD's Aug-Oct 2008 dayside season would be the first real test of whether the detector backbone separates layer-like encounters from non-PDL sheath states.
