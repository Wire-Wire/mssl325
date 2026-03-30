> **STATUS:** Superseded by `docs/PHASE_6_ROUTEB_BOUNDED_EXECUTION.md` (2026-03-30). The bounded execution has been completed; the regression test described here was the precursor. For Route B results, read the bounded execution doc. For the current decision space, read `docs/NEXT_QUESTION.md`.

# Phase 6 Route 3B — Compatible Measurement-Model Extension

**Date:** 2026-03-30
**Stage:** Design + tiny regression test only. Not a full execution.

---

## 1. Scope and authority

This document defines a compatible measurement-model extension (Route B) for the Phase 6 reset. It was tested on the clean Route A universe and the existing tranche-2 low-cone candidates only. No new archive search was performed. Route C remains contingent.

---

## 2. Why Route B is being tested now

The Phase 6A pilot failed because the dual-bin (near + background) occupancy requirement structurally excludes low-cone / low-Dp encounters: the ~11.6 Re inner-probe apogee cannot reach the background bin (s > 0.6) when the sheath is wide. Route B tests whether an alternative descriptor that does NOT require the background bin can recover low-cone evaluability.

---

## 3. What semantic bottleneck it addresses

The bottleneck is that Dn = median(density_near) / median(density_bg) and EB = median(|B|_near) / median(|B|_bg) both require populated background bins. Under low Dp, the spacecraft never reaches s > 0.6, making Dn and EB undefined. Route B defines an auxiliary descriptor that compares density and |B| within the inner sheath only.

---

## 4. What frozen semantics remain unchanged

- Dn and EB remain defined exactly as before whenever both bins are populated
- The encounter remains the unit
- Sun–Earth-line s-mapping, Shue 1998, Merka 2005 remain the boundary models
- Upstream context remains OMNI-propagated encounter-averaged
- Phase 4B frozen claims are not altered or strengthened

---

## 5. Primary auxiliary descriptor family

**Δn_near** = median(density in s = [0.0, 0.2]) / median(density in s = [0.2, 0.4])

**Δ|B|_near** = median(|B| in s = [0.0, 0.2]) / median(|B| in s = [0.2, 0.4])

These compare the very-near bin to the near bin within the inner sheath only. They require very-near occupancy > 1% AND near occupancy ≥ 1%.

**Semantic cost:** These are NOT the same as Dn / EB. They measure a gradient within the near-MP region, not a ratio against the outer sheath. They are explicitly marked as Phase-6-reset-only semantics, not directly interchangeable with frozen Phase 4B Dn / EB.

---

## 6. Backup descriptor family

None proposed in this round. If the primary fails, Route C (regime-access reset preserving Dn/EB) is the fallback.

---

## 7. Transition / boundary-layer / disturbance QC layer

Any future Route B execution must include these audit fields per encounter:

| QC field | What it checks | Values |
|---|---|---|
| transition_cleanliness_qc | Whether the near-MP gradient is clean or muddled by boundary-layer mixing | clean / mixed / unclear |
| disturbance_qc | Whether the encounter is dominated by transient/jet-like activity | undisturbed / disturbed / uncertain |
| omni_context_quality_note | OMNI data quality / fill-fraction during the upstream window | good / partial / poor |
| boundary_uncertainty_note | Whether encounter-averaged boundaries are plausible for this Dp/Bz | plausible / uncertain / suspect |

These are audit fields only, not labels or exclusion rules.

---

## 8. Tiny regression test design

**Test scope:** 9 clean real tranche-1 encounters + 3 tranche-2 low-cone candidates (all from existing artifacts; no new search).

**Test question:** Is the auxiliary descriptor computable on encounters that previously failed the dual-bin screen? Does it recover any low-cone evaluability?

**Computability criterion:** very-near occupancy > 1% AND near occupancy ≥ 1%.

---

## 9. Results of the tiny regression test

### Clean tranche-1 encounters (N = 9)

| Encounter | Cone | VN occ | Near occ | BG occ | Original Dn/EB? | Route B? |
|---|---|---|---|---|---|---|
| usable_aug18_6h | 31° | ~13% | 16% | 48% | ✓ | ✓ |
| usable_sep03_5h | 56° | ~18% | 18% | 21% | ✓ | ✓ |
| usable_sep26_09_10h | 85° | ~15% | 18% | 40% | ✓ | ✓ |
| usable_sep27_09_10h | 57° | ~7% | 16% | 57% | ✓ | ✓ |
| cand4a_sep19_08_the | 64° | 0% | 12% | 29% | ✓ | ✗ |
| usable_sep13_09_6h | 61° | <1% | 17% | 47% | ✓ | ✗ |
| usable_sep20_09_6h | 70° | 0% | 9% | 46% | ✓ | ✗ |
| usable_oct24_09_6h | 86° | 0% | 14% | 65% | ✓ | ✗ |
| cand4a_oct23_10_thd | 35° | 0% | 9% | 2% | ✓ | ✗ |

Route B computable: 4 of 9 (the ones with populated very-near bins).

### Tranche-2 low-cone candidates (N = 3, all BG = 0)

| Encounter | Cone | VN occ | Near occ | Route B? |
|---|---|---|---|---|
| t2_20080904_thd | 43° | 4.5% | 21% | **✓ RECOVERED** |
| t2_20090928_thd | 43° | 0% | 27% | ✗ |
| t2_20090928_the | 44° | 0% | 29% | ✗ |

**One low-cone encounter recovered:** t2_20080904_thd (cone = 43°) was previously excluded because BG = 0, but it has very-near occupancy (4.5%) + near occupancy (21.1%), making it evaluable under Route B.

The other two tranche-2 candidates have zero very-near occupancy, so Route B does not help them.

---

## 10. Exact strongest supportable statement

Route B's auxiliary descriptor (very-near / near ratio) is computable on 5 of 12 tested encounters, including 1 low-cone encounter (t2_20080904_thd, cone = 43°) that was previously excluded under the dual-bin requirement. This is a marginal but genuine recovery of one low-cone data point. The descriptor does not require hidden rescue logic or manual event carving — it is defined by the same s-bin structure already in the measurement model, just applied to a different bin pair.

---

## 11. Exact non-claim

- Route B does not recover the quasi-radial regime (cone ≤ 30°)
- Route B recovers only 1 of 3 tested low-cone encounters
- The auxiliary descriptor is NOT Dn / EB and is NOT directly comparable to Phase 4B frozen values
- The recovery is small enough that a single additional encounter does not constitute a regime comparison
- No thresholds, labels, classes, detector semantics, or prior language are introduced
- This test does not authorize a full Route B execution

---

## 12. Decision trigger

**Route B is marginally viable.** It recovers exactly 1 low-cone encounter from 3 tested. This is not zero — the mechanism works — but the yield is low. Whether this is sufficient for a bounded Route B execution depends on whether the user values a single additional low-cone data point enough to accept the semantic cost (different descriptor basis, not comparable to Phase 4B).

**If the user judges 1 recovered encounter as worth proceeding:** authorize a bounded Route B execution on the clean universe.

**If the user judges 1 recovered encounter as insufficient:** authorize Route C (regime-access reset with broader search preserving Dn/EB).
