# Phase 2a State Document — Frozen Window Bank

**Date:** 2026-03-26
**Repo:** `mssl325`
**Canonical run:** `runs/20260326T033744Z_9f985ab9/`

---

## 1. What Phase 2a is

Phase 2a is a controlled real-window expansion stage. It is NOT Phase 2 (threshold tuning, development-set construction, or scientific classification). Its purpose is to demonstrate that the frozen measurement model can produce usable near/background metric comparisons from real THEMIS data across multiple upstream regimes.

---

## 2. What has been achieved

1. **7 measurement-model-valid comparator windows** across 4 orbital passes, 2 THEMIS seasons (2008 + 2009)
2. **All 7 produce PASS status** with non-null core metrics (Dn, EB, Δβ, ρ)
3. **Both near and background bins populated** in every window
4. **Multiple upstream regimes** represented: northward Bz / southward Bz / mixed Bz, Dp range 3–4 nPa
5. **SZA range 4°–22°** — near-subsolar geometry confirmed for all
6. **Different metric patterns observed**: Dn>1 (compressed sheath) and Dn<1 (layer-like), demonstrating the measurement model resolves real regime differences

---

## 3. What each window can and cannot be called

### What it IS
Every window in the bank is a **measurement-model-valid near-MP comparator window**. This means:
- It passes all preflight checks (geometry, data validity, membership, occupancy, s-sanity)
- It produces non-null core metrics under the frozen measurement model
- Its near/background comparison is interpretable within the current s-bin framework

### What it is NOT
No window is:
- A confirmed PDL event
- A confirmed non-PDL baseline or negative control
- A labeled development-set example
- A validated event in any classifier sense
- Evidence for or against any upstream-dependence hypothesis

---

## 4. Constraint model (three layers)

### Layer A — strong execution constraints (enforced in code)
- All windows have near + background s-bin leverage
- All are dayside / near-subsolar / low-latitude
- QC / eligibility grammar preserved (preflight is a hard gate)
- Radial IMF avoided in this stage
- Fill-value masking active; sheath membership checked

### Layer B — ranking / exploratory guidance (not hard rules)
- SZA < 30° and X > 8 Re were used as ranking preferences during candidate selection
- "Moderate steady Dp" (2–5 nPa) was useful for interpretability
- 6–10h window durations are empirically determined, not literature-defined standards
- Non-radial IMF was preferred but not formally required

### Layer C — deferred (not decided here)
- PDL-positive / non-PDL classification
- Detector thresholds for Dn, EB, Δβ, ρ, persistence
- Development-set labels
- Encounter-family boundaries from exploratory long windows
- Selection-function audit, shuffled-s falsification
- Time-varying boundary computation
- MMS thickness, SMILE/SXI priors

---

## 5. Physical insight from current bank

The current bank shows two distinct metric patterns under the encounter-averaged measurement model:

| Pattern | Dn | EB | Δβ | Example windows |
|---|---|---|---|---|
| Compressed-sheath | >1 | <1 | >0 | sep03 (both), oct24 |
| Layer-like | <1 | >1 | <0 | aug18, sep13 |

The sep26 window (Dn≈1, EB≈2) is intermediate.

**This is a descriptive observation, not a classification.** The patterns may reflect different upstream conditions, different boundary-motion histories, or different sheath structures. The frozen measurement model correctly resolves these differences, which is the Phase 2a validation target.

---

## 6. Decision status

### Frozen
- Encounter as statistical unit
- s = d_MP/(d_MP+d_BS) along Sun-Earth line
- Shue 1998 MP + Merka 2005 BS baseline
- Dual near bins [0.2,0.4] + background [0.6,1.0]
- IMF-agnostic detection (upstream enters post-detection)
- Detector backbone: Dn, EB, Δβ, ρ(n,B), persistence
- QC flags + grading structural (tri-state, cap_silver)
- Fill-value masking (OMNI sentinels, CDF fills)
- Preflight eligibility checks
- Conservative window naming

### Provisional
- Window durations: 6–10h (empirical, not standard)
- Dp > 3 nPa constraint (empirical for 11.6 Re apogee)
- Resampling: 10 s cadence, 60 s max gap
- Encounter-averaged boundaries (time-varying deferred)
- Sheath membership: conservative plasma/field sanity

### Deferred
- Detector thresholds, dev-set labels, encounter merge
- Radial-IMF cut, selection-function audit, shuffled-s
- Time-varying s-mapping, alternative MP/BS pair
- MMS thickness, SMILE/SXI priors
- PDL / non-PDL classification

---

## 7. Remaining blocker

The bank has 7 windows but only 4 distinct orbital passes (2 dates in 2008, 2 dates in 2009). For threshold exploration, ~10–15 diverse passes would be better. The THD Sep-Oct 2009 season has additional candidates (Sep 3, Sep 27, others) that could expand the bank further, but each requires individual validation.

---

## 8. Commands

```bash
# Run the frozen window bank (7/7 evaluable)
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live_usable.yaml

# Family validation
PYTHONPATH=src python -m pdl_pilot.cli.validate_families --config configs/pilot_window_families.yaml

# Tests (111 pass, 1 skip)
PYTHONPATH=src python -m pytest tests/ -v
```
