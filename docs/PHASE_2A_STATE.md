# Phase 2a State Document — Final Window Bank

**Date:** 2026-03-26
**Repo:** `mssl325`
**Canonical run:** `runs/20260326T040343Z_d0425fd4/`

---

## 1. What Phase 2a achieved

A bank of **9 measurement-model-valid comparator windows** across **7 distinct orbital passes** and 2 THEMIS seasons (2008-09), all producing PASS status with non-null core metrics and dual-bin (near + background) leverage.

---

## 2. Pass inventory

7 distinct orbital passes, all THD:
- 2008-08-18 (2 windows), 2008-09-03 (2 windows)
- 2009-09-13, 2009-09-20, 2009-09-26, 2009-09-27, 2009-10-24 (1 each)

See `docs/WINDOW_BANK_SUMMARY.md` for the full per-window table.

---

## 3. What windows can and cannot be called

**Can be called:** measurement-model-valid near-MP comparator window.

**Cannot be called:** PDL-positive, non-PDL, baseline, development-set member, labeled example of any kind.

---

## 4. Decision status

### Frozen
- Encounter as statistical unit
- s = d_MP/(d_MP+d_BS) along Sun-Earth line
- Shue 1998 MP + Merka 2005 BS baseline
- Dual near bins [0.2,0.4] + background [0.6,1.0]
- IMF-agnostic detection
- Detector backbone: Dn, EB, Δβ, ρ(n,B), persistence
- QC flags + grading structural (tri-state, cap_silver)
- Preflight eligibility checks
- Fill-value masking
- Conservative window naming

### Provisional
- 6–10 h window durations (empirical, not standard)
- Dp > 3 nPa practical selection preference
- 10 s cadence / 60 s max gap for multi-hour windows
- Encounter-averaged boundaries
- Conservative sheath membership (plasma/field sanity)

### Deferred
- Detector thresholds
- PDL / non-PDL labels
- Development-set membership
- Encounter merge finalization
- Radial-IMF cut
- Selection-function audit, shuffled-s falsification
- Time-varying s-mapping, alternative MP/BS pair
- MMS thickness, SMILE/SXI priors

---

## 5. Readiness for the next bounded step

**The bank is broad enough for a bounded metric-behavior review.** 7 distinct passes with Dn ranging 0.12–2.31 and EB ranging 0.80–4.22 provide sufficient diversity to examine how the detector backbone metrics vary across windows without defining thresholds or assigning labels. This would be the first controlled scientific step beyond window-bank construction.

---

## 6. Commands

```bash
# Run the 9-window bank (9/9 evaluable)
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live_usable.yaml

# Tests (111 pass, 1 skip)
PYTHONPATH=src python -m pytest tests/ -v
```
