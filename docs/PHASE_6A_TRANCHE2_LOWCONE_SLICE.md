# Phase 6A Tranche 2 — Low-Cone-Targeted Second Slice

**Date:** 2026-03-30
**Authority:** User-authorized continuation of Phase 6A.
**Phase 4B/5A/5B remain frozen anchors.**

---

## 1. Authority and tranche-2 opening note

The user authorized a second bounded Phase 6A slice targeting the empty quasi-radial / low-cone regime from tranche 1. Tranche 1 found 11 evaluable encounters but zero with cone angle ≤ 30° (quasi-radial). This tranche tests whether the 2007–2010 THEMIS dayside archive contains evaluable low-cone encounters under the same measurement-context screens.

---

## 2. Scope and non-goals

**This tranche is:** one low-cone-targeted slice + integrated tranche1+2 synthesis. Descriptor-only.

**This tranche is NOT:** Phase 6B, occurrence analysis, bundle construction, detector preparation, mission-prior work, MMS work, or a causal conditioning study.

---

## 3. Declared tranche-2 slice

All THEMIS encounter outputs from the 2007–2010 dayside interval that satisfy the Phase 6 measurement-context screens AND have 30-minute mean IMF cone angle ≤ 45°, processed in chronological order. This is the only tranche-2 slice.

---

## 4. Sample definition and screens

**Candidate search:** ~80 dates scanned (every 3rd day, THD + THE, Aug–Oct 2008–2009). ~20 had near-subsolar geometry (SZA ≤ 30°). Only 3 had OMNI-derived cone angle ≤ 45° and s-range potential.

**Measurement-context screens applied (same as tranche 1):**
1. SZA ≤ 30°
2. Upstream data available
3. Near-bin occupancy ≥ 5%
4. Background-bin occupancy ≥ 1%
5. Membership ≥ 50%

---

## 5. Selection / exclusion ledger

| Encounter | Probe | Date | Cone | Dp | Status | Reason |
|---|---|---|---|---|---|---|
| t2_20080904_thd | THD | 2008-09-04 | 43° | 2.7 | EXCLUDED | BG bin = 0% |
| t2_20090928_thd | THD | 2009-09-28 | 43° | 1.9 | EXCLUDED | BG bin = 0% |
| t2_20090928_the | THE | 2009-09-28 | 44° | 1.9 | EXCLUDED | BG bin = 0% |

**All 3 candidates fail the background-bin occupancy screen.**

**Root cause:** Low-cone IMF conditions in the 2008–2009 THEMIS dayside archive correspond to lower encounter-averaged Dp (~1.9–2.7 nPa). At these pressures, the magnetopause and bow shock are farther out, the sheath is wider, and the ~11.6 Re inner-probe apogee cannot reach s > 0.6 (background bin). This is the same structural constraint that shaped the original Phase 4B bank.

**Retained from tranche 2: zero.**

---

## 6. Tranche-2 descriptor summaries

Not applicable — zero encounters retained.

---

## 7. Integrated tranche1+2 synthesis

Since tranche 2 retained zero new encounters, the combined sample is unchanged from tranche 1 (N = 11). However, the tranche-1 encounters can be reclassified into a coarser three-regime scheme:

| Regime | Cone range | N (tranche 1) | N (tranche 2) | Total | Dn median | EB median |
|---|---|---|---|---|---|---|
| low-cone | ≤ 45° | 4 | 0 | 4 | 0.95 | 1.05 |
| intermediate | 45–60° | 2 | 0 | 2 | 2.09 | 1.01 |
| perpendicular | > 60° | 5 | 0 | 5 | 0.94 | 1.96 |

**Key observation:** Under the coarser three-regime scheme, the low-cone group (N = 4, all from tranche 1 with cone 31–41°) shows Dn near unity (median 0.95) and EB near unity (median 1.05) — similar to the intermediate group and distinct from the perpendicular group (Dn median 0.94, EB median 1.96). The cone-angle descriptor pattern from tranche 1 is preserved under reclassification, but the low-cone bin contains only encounters from the upper end of the low-cone range (31–41°), not truly quasi-radial encounters (cone < 30°).

**The quasi-radial bin (cone ≤ 30°) remains empty.** The targeted expansion failed to populate it because the structural selection function (dual-bin requirement at 11.6 Re apogee) excludes the low-Dp conditions that co-occur with quasi-radial IMF.

---

## 8. QC / transition-contamination note

No new encounters were retained, so no QC extension was applied. The tranche-1 QC status (all upstream-stable, all >50% membership) is unchanged.

---

## 9. Boundary and upstream uncertainty note

Same as tranche 1: OMNI is propagated L1 context, not local truth. Magnetopause and bow-shock positions are encounter-averaged empirical model outputs. Cone and clock angles are 30-min OMNI averages. The selection function structurally couples cone angle and Dp through the dual-bin occupancy requirement.

---

## 10. Exact supportable statement

The low-cone-targeted Phase 6A tranche 2 found 3 candidate encounters with 30-min mean cone angle ≤ 45° in the 2007–2010 THEMIS dayside archive. All 3 failed the background-bin occupancy screen because the associated lower Dp (~1.9–2.7 nPa) makes the sheath too wide for the inner-probe apogee to reach s > 0.6. The quasi-radial regime (cone ≤ 30°) remains empty. The tranche-1 cone-angle descriptor pattern (perpendicular: lower Dn, higher EB; low-cone/intermediate: Dn and EB near unity) is preserved under reclassification but cannot be extended to truly quasi-radial conditions under the current measurement model.

---

## 11. Exact non-claim

- The absence of evaluable quasi-radial encounters does NOT mean quasi-radial near-MP sheath structure is physically absent or uninteresting. It means the current selection function (dual-bin requirement + 11.6 Re apogee + encounter-averaged boundaries) structurally excludes the low-Dp conditions that co-occur with quasi-radial IMF.
- No thresholds, labels, classes, detector semantics, or occurrence rates are defined or implied.
- No causal language ("perpendicular IMF favors depletion") is supported.
- The tranche-1 descriptor separation remains a controlled-sample observation, not a population-level or mechanism-level claim.

---

## 12. 6B-readiness verdict

**Phase 6B is NOT justified from this two-tranche result.** The targeted expansion failed: zero new encounters retained, quasi-radial bin still empty. The combined sample (N = 11) is unchanged from tranche 1 and remains structurally biased toward compressed-sheath (Dp > 3 nPa) and non-radial IMF conditions.

A later Phase 6B would require either:
- a fundamentally different measurement model that relaxes the dual-bin occupancy requirement
- a different spacecraft/mission with orbital reach matching wider sheath conditions
- or acceptance that the quasi-radial regime is not accessible under the current apparatus

None of these are authorized in this round. **The recommended next step is to stop Phase 6A and freeze this two-tranche result as a documented structural-limitation finding.**
