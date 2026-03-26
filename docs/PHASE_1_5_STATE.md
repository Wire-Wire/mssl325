# Phase 1.5 State Document — First Usable Real Science Runs

**Date:** 2026-03-26
**Repo:** `mssl325` (branch: `main`)
**Package:** pdl-pilot v0.1.0, Python >= 3.10

---

## 1. Current state in one sentence

First usable real THEMIS encounter windows achieved: THD Sep 3 2008 under elevated Dp (3.5 nPa) compresses the sheath so that the dual-bin measurement model produces non-null core metrics (Dn, EB, Δβ, ρ) from real CDAWeb data, validating the full pipeline end-to-end.

---

## 2. What changed in this phase

### Window-family workflow
- New `configs/pilot_window_families.yaml`: duration-ladder manifests for seed families
- New `src/pdl_pilot/cli/validate_families.py`: tests each seed at [30, 90, 180, 360, 720] min
- Produces JSON/CSV/markdown summaries per family, ranks windows for usability

### Key findings from duration sweeps

| Family | Apogee | Dp | Result |
|---|---|---|---|
| oct08_thd | 11.6 Re | ~1.0 nPa | **Never reaches BG bin** — sheath too wide at low Dp |
| jul07_thc | 14.7 Re | N/A | **No MOM data** — THC MOM L2 not available in 2007 |
| sep03_thd | 11.6 Re | ~3.5 nPa | **BOTH bins populated!** — compressed sheath spans s=0.0–0.69 |

**Physical insight**: The dual-bin design requires that encounter-averaged upstream pressure compresses the sheath enough for the orbital range to span both bins. At ~11.6 Re apogee:
- Dp < 2 nPa: sheath too wide → s stays < 0.5
- Dp > 3 nPa: sheath compressed → s reaches 0.6+ (background bin)

### First usable results

| Encounter | SZA | Near% | BG% | Dn | EB | Δβ | ρ |
|---|---|---|---|---|---|---|---|
| usable_sep03_6h | 13.8° | 16.9% | 26.7% | 2.31 | 0.82 | +1.66 | -0.52 |
| usable_sep03_8h | 12.0° | 13.1% | 39.7% | 2.07 | 0.80 | +1.70 | -0.51 |
| usable_sep03_5h | 14.9° | 18.5% | 21.0% | 2.87 | 0.80 | +2.06 | -0.63 |

**Note**: Dn > 1 + EB < 1 = density enhancement + B reduction near MP. This is a compressed-sheath signature under high Dp + northward Bz, NOT a PDL. These windows validate the measurement model, not the detector.

---

## 3. Repo architecture additions

```
NEW:
  configs/pilot_window_families.yaml    — duration-ladder seed families
  configs/pilot_live_usable.yaml        — promoted usable science config
  src/pdl_pilot/cli/validate_families.py — family validation CLI
  tests/test_families.py                — 9 tests for family workflow

EXISTING (unchanged):
  configs/pilot_themis.yaml             — synthetic pilot
  configs/pilot_live.yaml               — diagnostic live (known-ineligible)
  configs/pilot_candidates.yaml         — candidate bank
  configs/pilot_live_science.yaml       — first science (occupancy-limited)
```

---

## 4. Decision status

### Frozen (unchanged)
Encounter unit, s=d_MP/(d_MP+d_BS), Shue/Merka baseline, dual near bins [0.2,0.4]+[0.6,1.0], IMF-agnostic detection, detector backbone (Dn, EB, Δβ, ρ, persistence), QC structural, provenance-first.

### Provisional (updated)
- Window duration: 5-8h for usable traversal (was 1-2h)
- Resampling cadence: 10 s for multi-hour windows
- Max gap: 60 s for long windows
- Dp constraint: usable windows need Dp > ~3 nPa with current orbits
- s-mapping uses encounter-averaged boundaries (time-varying deferred)

### Deferred (unchanged)
Detector thresholds, dev-set construction, encounter merge, radial-IMF cut, selection-function audit, shuffled-s falsification, time-varying boundary computation, MMS thickness, SMILE/SXI priors, ML classification.

---

## 5. Remaining blockers for Phase 2

1. **Current usable windows are compressed-sheath, not PDL-like.** Need southward Bz + moderate Dp encounters.
2. **Encounter-averaged boundaries**: The current s-mapping uses one set of boundaries for the whole encounter. Time-varying Dp causes s to shift during the encounter but the pipeline doesn't capture this.
3. **Only one orbital pass (Sep 3 2008)**: Need 5-10 diverse passes for a minimal development set.

---

## 6. Commands

```bash
# Synthetic pilot (unchanged)
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_themis.yaml

# Family validation (duration ladder)
PYTHONPATH=src python -m pdl_pilot.cli.validate_families --config configs/pilot_window_families.yaml

# Usable science pilot run (first real metrics)
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live_usable.yaml

# Tests (111 passed, 1 skipped)
PYTHONPATH=src python -m pytest tests/ -v
```

---

## 7. Next step (do not implement)

Find 5-10 encounter windows under moderate Dp (2-4 nPa) with southward Bz (Bz < -2 nT) during THD/THE dayside seasons (Aug-Oct 2008, Sep-Oct 2009). These would be the first windows where actual PDL-like signatures (Dn < 1, EB > 1, Δβ < 0) might appear — the beginning of a real development set for threshold exploration.
