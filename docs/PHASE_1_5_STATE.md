# Phase 2a State Document — Controlled Real-Window Expansion

**Date:** 2026-03-26
**Repo:** `mssl325` (branch: `main`)

---

## 1. Current state

Phase 2a: controlled real-window expansion with three-layer constraint discipline. The pipeline now produces non-null core metrics from 4 measurement-model-valid real THEMIS windows across 2 distinct upstream regimes (THD Sep 3 and Aug 18, 2008). No window is classified as PDL or non-PDL.

---

## 2. Constraint model (per Phase 2a upstream decision memo)

### Layer A — strong execution constraints (enforced)
- All windows have near/background s-bin leverage
- Dayside near-subsolar geometry required
- QC/eligibility grammar preserved intact
- Not starting with radial IMF
- Conservative naming: "measurement-model-valid near-MP comparator windows"

### Layer B — ranking/exploratory guidance (informing, not enforcing)
- SZA < 30°, X > 8 Re preferences used in curation scoring
- Moderate Dp useful for interpretability
- Window durations empirically determined, not literature standards

### Layer C — deferred (not decided)
- PDL-positive / non-PDL baseline labels
- Detector thresholds
- Development-set membership
- Final encounter-family definitions
- MMS thickness, SMILE/SXI priors

---

## 3. What changed in this phase

### Systematic scan
- Scanned THD dayside season (Aug-Oct 2008) for all dates where s > 0.5 at apogee
- Found 2 dates with background-bin reachability: Sep 3 (known) and Aug 18 (new)
- Confirmed that only Dp > ~3 nPa produces dual-bin coverage at 11.6 Re apogee

### New seed family
- Added aug18_thd to `configs/pilot_window_families.yaml`
- THD Aug 18 2008: Dp 3-5 nPa, mixed/weakly-negative Bz, different regime from Sep 3

### Expanded usable config
- `configs/pilot_live_usable.yaml` now contains 4 windows across 2 regimes
- All 4 produce PASS status with non-null core metrics

### Metric comparison across regimes

| Window | Dp | Bz | Dn | EB | Δβ | ρ |
|---|---|---|---|---|---|---|
| Sep 3 6h | 3.5 | +0.9 | 2.31 | 0.82 | +1.66 | -0.52 |
| Sep 3 8h | 3.5 | +2.6 | 2.07 | 0.80 | +1.70 | -0.51 |
| Aug 18 6h | 4.2 | +0.3 | 0.12 | 2.49 | -10.1 | -0.46 |
| Aug 18 8h | 3.6 | +0.1 | 0.88 | 2.08 | -10.1 | 0.00 |

Sep 3: Dn > 1 (density enhancement near MP), EB < 1 → compressed-sheath
Aug 18: Dn < 1 (density depletion), EB > 1 (B enhancement) → layer-like pattern

**Neither is classified.** The measurement model produces different metric patterns under different upstream conditions, as expected.

---

## 4. Decision status

### Frozen (unchanged)
Encounter unit, s = d_MP/(d_MP+d_BS), Shue/Merka baseline, dual near bins [0.2,0.4]+[0.6,1.0], IMF-agnostic detection, detector backbone (Dn, EB, Δβ, ρ, persistence), QC structural, provenance-first.

### Provisional (updated)
- Window duration: 6-8h for usable traversal with 11.6 Re apogee
- Dp constraint: usable windows need encounter-averaged Dp > ~3 nPa (empirical, not frozen)
- Resampling: 10 s cadence, 60 s max gap for multi-hour windows
- Encounter-averaged boundaries (time-varying computation deferred)

### Deferred (unchanged)
Detector thresholds, dev-set construction, encounter merge, radial-IMF cut, selection-function audit, shuffled-s falsification, time-varying s, MMS thickness, SMILE/SXI priors, PDL/non-PDL labeling.

---

## 5. Remaining blocker

Only 2 orbital passes (Sep 3, Aug 18 2008) produce usable windows from the Aug-Oct 2008 THD scan. Need 5-10 diverse passes for threshold exploration. Expansion requires scanning additional dayside seasons or probes.

---

## 6. Commands

```bash
# Usable pilot (4 windows, 2 regimes)
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live_usable.yaml

# Family validation
PYTHONPATH=src python -m pdl_pilot.cli.validate_families --config configs/pilot_window_families.yaml

# Tests (111 pass, 1 skip)
PYTHONPATH=src python -m pytest tests/ -v
```
