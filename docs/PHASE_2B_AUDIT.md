# Phase 2B Audit — Comparator Bank Falsification and Confounder Resolution

**Date:** 2026-03-26
**Bank:** 9 windows / 7 distinct passes / THD only / 2008 + 2009

---

## 1. Pass-aware audit summary

### Evidence structure

| Item | Count | Note |
|---|---|---|
| Total windows | 9 | |
| Distinct orbital passes | 7 | Effective independent N |
| Same-pass duration variants | 2 passes × 2 variants | P1 (Aug 18) and P2 (Sep 3) each have 6h + 8h |
| Probe | THD only | No cross-probe verification |
| Seasons | 2 (2008, 2009) | |
| Upstream Dp range | 3.0–4.2 nPa | All above ~3 nPa; lower-Dp sheath excluded |
| Upstream Bz range | -1.7 to +2.6 nT | Both northward and southward represented |

### Why same-pass variants are not independent evidence

Within-pass metric spread is much smaller than between-pass spread:
- Dn: within/between ratio = 0.28
- EB: within/between ratio = 0.06
- Δβ: within/between ratio = 0.004

Duration variants on the same pass produce operationally similar metrics. The 7 distinct passes, not the 9 windows, define the effective sample.

---

## 2. Selection-function audit

See `docs/SELECTION_FUNCTION_AUDIT.md` for the full standalone document.

**Summary:** The current bank's composition is shaped by 6 interlocking constraints that are all practical/engineering, not scientific selections. The bank is systematically biased toward compressed-sheath conditions and cannot represent the full dayside magnetosheath population.

---

## 3. Bounded falsification and sensitivity checks

### 3.1 Shuffled-s test

**Method:** Under spatial randomization (permuting s while preserving physical time series), the near-bin and background-bin would sample the same marginal distributions, producing Dn → 1, EB → 1.

**Result:** All 9 windows show at least one metric substantially deviating from 1.0. The s-ordered bin structure produces non-trivial metric differentiation that would be destroyed by spatial randomization.

**Dn–EB anti-correlation:** Spearman r = -0.45, p = 0.22. The direction is consistent with an inverse relationship but not statistically significant at N = 9. This is expected given the small sample.

**Conclusion:** The metric backbone captures structure that depends on ordered s-position, not merely marginal statistics. This is a necessary (not sufficient) condition for the metrics to reflect spatially organized magnetosheath structure.

### 3.2 Within-pass duration sensitivity

Already reported above: within-pass spreads are 6–28% of between-pass ranges for the three primary metrics. Duration choice affects occupancy balance but does not dramatically change the metric character of a pass.

### 3.3 Very-near bin sensitivity

**Architecture:** Dn, EB, Δβ, and persistence are computed from the near bin [0.2, 0.4] and background bin [0.6, 1.0] only. The very-near bin [0.0, 0.2] enters only the ρ(n,B) computation via the combined [0.0, 0.4] mask for trend anti-correlation.

**Impact of excluding very-near:**
- Dn, EB, Δβ, persistence: **unaffected** (these metrics never touch the vn bin)
- ρ(n,B): would narrow the computation region. For windows with high vn fraction (sep03_6h: 31%, aug18_8h: 25%), this could measurably change ρ. For windows with zero vn (sep20, oct24), ρ is already computed without vn data.

**Conclusion:** The primary metrics (Dn, EB) are insensitive to very-near bin inclusion/exclusion. Only ρ is affected, and its universal negativity makes it non-discriminative regardless.

### 3.4 Upstream-summary sensitivity

**Method:** Perturbed encounter-averaged Dp by ±1 nPa and recomputed boundary positions.

**Result:** MP shifts by ~0.7–1.0 Re, BS shifts by ~0.9–1.3 Re. This is a substantial fraction of the 3 Re sheath width. Since s depends on the ratio of distances to both boundaries, a 1 nPa Dp error could shift s by ~0.1–0.2 for individual points.

**Conclusion:** The encounter-averaged s-mapping is moderately sensitive to upstream pressure uncertainty. This is a known provisional limitation (the frozen baseline uses encounter-averaged boundaries). Resolving this would require time-varying s-mapping, which is deferred.

---

## 4. Confounder-resolution audit

### 4.1 Flag status

| Flag | Status | Resolution |
|---|---|---|
| jet_flag | Resolved | **TRUE for all 9 windows** — Pdyn spike > 2× median detected in every window |
| wave_flag | Resolved | FALSE for all 9 windows |
| motion_flag | Resolved | FALSE for all 9 windows (crossing_count = 1 for all) |
| transient_flag | **UNKNOWN** | Not implemented. Cannot assess foreshock/transient contamination. |
| mixing_flag | **UNKNOWN** | Not implemented. Cannot assess magnetospheric mixing contamination. |

### 4.2 Assessment

**Universal jet triggering:** Every window triggers the jet flag (Pdyn spike > 2× median). This means:
- The jet flag has no discriminative power within this bank
- All windows have at least one unresolved confounder risk
- No window can achieve Gold grade

**The universal jet triggering likely reflects the multi-hour window durations** used to achieve dual-bin coverage. Over 6–10 hours, the probability of at least one Pdyn fluctuation exceeding 2× median is high regardless of underlying physical state. The current jet threshold (2× median) may be too sensitive for long-duration windows.

**Transient and mixing flags remain UNKNOWN.** Without implementation, contamination from foreshock transients or magnetospheric mixing cannot be assessed. This is a known gap that limits grade ceiling to Silver.

### 4.3 Membership quality

Membership fractions range from 85% to 100%. Non-sheath points are predominantly classified as "unknown" (NaN/missing data) in the Aug 18 windows, not as magnetospheric or upstream contamination. No window shows systematic magnetosphere or solar-wind contamination.

---

## 5. Wording-drift audit

See `docs/WORDING_DRIFT_AUDIT.md` for the full standalone document.

**Summary:** Current docs are largely disciplined. Minor tightenings applied to seed_stratification.json rationales and the PHASE_1_5_STATE description of metric patterns.

---

## 6. Gate judgment

### Question

Is the current 9-window / 7-pass comparator bank scientifically clean enough to justify a later bounded detector-readiness stage?

### Answer: CONDITIONAL GO

The bank passes the following audit checks:
1. ✅ Dual-bin leverage confirmed in all 9 windows
2. ✅ Spatial structure confirmed: metrics deviate from shuffled-s null
3. ✅ Duration variants are consistent (not inflating apparent diversity)
4. ✅ Membership quality is adequate (≥85% for all windows)
5. ✅ Primary metrics (Dn, EB) are insensitive to very-near bin
6. ✅ Conservative naming is maintained throughout

The bank has the following known limitations that must be carried forward:
1. ⚠️ **Universal jet triggering** — every window triggers jet_flag; the flag has no discriminative power. The 2× median Pdyn threshold may need recalibration for long-duration windows (deferred).
2. ⚠️ **Two unresolved confounder channels** — transient_flag and mixing_flag remain UNKNOWN. No window achieves Gold grade.
3. ⚠️ **Single probe, Dp > 3 nPa bias** — the bank is systematically biased toward compressed-sheath conditions on THD.
4. ⚠️ **Effective N = 7** — any later analysis must treat this as the sample size, not 9.
5. ⚠️ **ρ is non-discriminative** — universally negative, it cannot distinguish between windows.
6. ⚠️ **Upstream sensitivity** — ±1 nPa Dp shifts boundaries by ~1 Re (deferred: requires time-varying s).

### Conditions for moving to a later bounded stage

Any later detector-readiness or threshold-exploration step must:
1. Treat N = 7 independent passes as the effective sample
2. Not use ρ as a discriminative metric in this bank
3. Acknowledge that all windows carry unresolved jet and confounder risk
4. Not convert observed metric patterns into physical class labels
5. Not claim that the bank represents the full dayside magnetosheath population
