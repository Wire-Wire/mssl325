# Phase 3A: Dn/EB Exploratory Comparison

**Stage:** Descriptive only. No thresholds. No labels.

---

## Pass-aware Dn/EB comparison

| Pass | Date | Status | Dn | EB | Dn_clean | EB_clean | Δβ | Persist | Spike% |
|---|---|---|---|---|---|---|---|---|---|
| P4 | 2009-09-20 | **clean** | 0.97 | 1.48 | 0.96 | 1.49 | -3.1 | 0.66 | 21% |
| P5 | 2009-09-26 | clean | 0.94 | 1.96 | 0.90 | 1.94 | -12.8 | 0.61 | 13% |
| P6 | 2009-09-27 | clean | 1.31 | 1.23 | 1.10 | 1.20 | -4.2 | 0.32 | 10% |
| P2 | 2008-09-03 | clean | 2.31 | 0.82 | 2.10 | 0.84 | +1.7 | 0.00 | 16% |
| P3 | 2009-09-13 | cautious | 0.39 | 1.96 | 0.41 | 1.46 | -6.8 | 1.00 | 25% |
| P1 | 2008-08-18 | cautious | 0.12 | 2.49 | 0.17 | 2.29 | -10.1 | 0.94 | 24% |

P7 (2009-10-24) excluded: spike-dominated, metrics collapse after spike removal.

---

## Primary vs secondary evidence

| Evidence tier | Passes | Dn range | EB range | Caveat summary |
|---|---|---|---|---|
| Clean core | P2, P4, P5, P6 | 0.94–2.31 | 0.80–1.96 | Metrics survive spike removal; low-to-moderate noise |
| Cautious | P1, P3 | 0.12–0.39 | 1.96–2.49 | P1: density noise CV=0.93; P3: EB spike-dependent |
| **Combined interpretable** | **6 passes** | **0.12–2.31** | **0.80–2.49** | Low-Dn range depends on cautious passes |

---

## Caveat register

| Caveat | Applies to | Severity |
|---|---|---|
| Low-Dn range carried by cautious evidence only | Bank-wide | Structural |
| P1 near-bin density noise (CV=0.93) | P1 | Serious warning |
| P3 EB partially spike-dependent (Δ=0.50) | P3 | Serious warning |
| P7 spike-dominated | P7 | Blocker (excluded) |
| Universal jet triggering | All windows | Accepted caveat (long-window artifact) |
| Transient/mixing/motion flags UNKNOWN | All windows | Carried forward |
| THD-only, Dp > 3 nPa bias | Bank-wide | Structural |
| Encounter-averaged boundaries | Bank-wide | Provisional |
| rho(n,B) non-discriminative | Bank-wide | Context only |

---

## Figure

See `figures/phase3a_dneb_comparison.png`:
- Left panel: Dn vs EB by evidence status
- Right panel: Dn original vs Dn after spike removal

---

All windows remain measurement-model-valid near-MP comparator windows. No labels implied.
