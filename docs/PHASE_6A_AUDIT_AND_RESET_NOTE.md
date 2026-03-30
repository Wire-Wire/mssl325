# Phase 6A — Post-Tranche-2 Audit and Control Reset

**Date:** 2026-03-30
**Type:** Audit and control-state repair. No new science.
**Phase 4B remains the claim-bearing baseline.**

---

## 1. Authority and scope

This is a post-tranche-2 audit of the current Phase 6A implementation. It does not rerun science, add encounters, or extend the branch. It checks whether the current "structural-limitation finding" claim is actually supported, and repairs the control state to match the audited evidence level.

---

## 2. Strongest supportable reading of tranche 1

### What tranche 1 established

Tranche 1 retained 11 encounters from the local archive, deduplicated by date + probe. For the 9 real THEMIS encounters, it showed that Dn and EB produce different median values in perpendicular-IMF vs intermediate-IMF strata. This is a descriptive within-sample observation.

### What tranche 1 did NOT establish

- A controlled encounter catalogue free of provenance contamination (see §5)
- Coverage of the quasi-radial regime
- Any causal or population-level conditioning statement

### Verified provenance issue: synthetic encounters in the catalogue

**pilot_001 (2012-07-15) and pilot_002 (2013-02-20) are synthetic fixture encounters, not real THEMIS data.** This is verified from the catalogue JSON:
- Both have `sza: 0.0` (impossible for real near-subsolar data — means SZA was never computed from real ephemeris)
- Both have `dp: 2.0, bz: 2.0, ma: 8.0` (these are the hardcoded synthetic defaults in `_build_upstream()`)
- Both have identical Dn (0.949) and EB (1.054) with delta_beta ≈ 0
- Their dates (2012, 2013) fall outside the 2008–2009 THEMIS real-data seasons

These entered the tranche-1 catalogue because the pipeline script scanned all `runs/*/encounter_*.json` without filtering out synthetic-mode runs.

**Impact:** The tranche-1 "N = 11" is actually N = 9 real + 2 synthetic. The "intermediate" cone regime (reported N = 6) contains 2 synthetic encounters. This inflates the intermediate-cone group and partially contaminates the cross-regime comparison.

**Corrected real-data counts:**
- Total real encounters: 9
- Perpendicular (cone > 60°): 5 (unchanged, all real)
- Intermediate (30–60°): 4 (was 6, minus 2 synthetic)
- Quasi-radial (≤ 30°): 0 (unchanged)

---

## 3. Strongest supportable reading of tranche 2

### What tranche 2 actually tested

Tranche 2 found 3 low-cone candidates (cone 43–44°) and all 3 failed the background-bin occupancy screen. Zero new encounters were retained.

### Declared-slice vs searched-slice mismatch

**Confirmed.** The declared slice was: "All THEMIS encounter outputs from the 2007–2010 dayside interval." The actual search scanned: "THD + THE, Aug–Oct 2008–2009, every 3rd day" — omitting 2007, 2010, and months outside Aug–Oct. The declared slice was broader than what was actually searched. This means the zero-retained result applies only to the searched subspace, not to the full declared 2007–2010 interval.

### What zero retained encounters supports

That within the Aug–Oct 2008–2009 THD/THE subspace, low-cone (43–44°) encounters under the current dual-bin occupancy requirement at 11.6 Re apogee fail to retain. This is a branch-local negative pilot result for this specific subspace, not a proven structural inaccessibility of the entire quasi-radial regime.

---

## 4. Combined two-tranche interpretation

### What the combined result supports

A branch-local pilot finding: within the locally available real THEMIS encounters (9 real, compressed-sheath-biased, 2008–2009 THD/THE, cone > 30°), Dn and EB descriptors shift with cone-angle regime in a direction qualitatively consistent with published expectations (Pi et al. 2024; Michotte de Welle et al. 2024). But this is a small-N, apparatus-limited, provenance-contaminated pilot observation, not a controlled catalogue result.

### What the combined result does NOT support

- A "structural-limitation finding" broader than the actually-searched subspace
- Any claim about the quasi-radial regime (never populated)
- Any claim about the 2007 or 2010 subspace (never searched in tranche 2)
- A clean N = 11 encounter sample (2 are synthetic)

---

## 5. Verified design/provenance vulnerabilities

### Verified from current artifacts

1. **Synthetic contamination:** pilot_001 and pilot_002 are synthetic fixtures in the tranche-1 catalogue (SZA = 0, hardcoded Dp/Bz/Ma, identical metrics, dates outside real-data seasons).
2. **Declared vs searched slice mismatch:** Tranche 2 declared 2007–2010 but searched only Aug–Oct 2008–2009.
3. **No true quasi-radial encounter:** The integrated "low-cone" group (N = 4 in the two-slice summary) contains cone = 31°, 33°, 35°, 41° — all above the 30° quasi-radial threshold. The label "low-cone" obscures this.

### Unresolved / not fully confirmable

4. Whether additional low-cone encounters exist in the unsearched parts of the 2007–2010 interval (2007, 2010, and months outside Aug–Oct) is unknown.
5. Whether the dual-bin occupancy failure at Dp < 2.7 nPa is truly universal for all cone < 45° encounters, or only for the 3 tested, is not fully established.

---

## 6. Exact verdict

**Apparatus-limited pilot stop with broader question still open.**

The current Phase 6A formulation is exhausted as a pilot: it produced a small-N descriptive observation that is contaminated by 2 synthetic encounters, covers only the non-radial / compressed-sheath regime, failed to populate the quasi-radial bin, and searched a narrower subspace than declared. The descriptor pattern within the accessible regime is qualitatively interesting but cannot be claimed as a controlled catalogue result.

The broader upstream-conditioning question (how do near-MP descriptors shift across the full cone-angle range) is not answered and not proven unanswerable. A differently formulated Phase 6 — with synthetic fixtures excluded, a properly declared and searched archive scope, and potentially a relaxed dual-bin requirement — could revisit this question. But that would be a reset, not a continuation.

---

## 7. Exact non-claim

The audit forbids the project from saying:
- "The quasi-radial regime is structurally inaccessible" (only 3 candidates were tested in a narrow subspace)
- "Phase 6A established a controlled cone-angle conditioning result" (the catalogue contains synthetic contamination and the sample is apparatus-limited)
- "The perpendicular-IMF descriptor pattern is a multi-regime finding" (the quasi-radial comparison arm is empty)
- Any causal, threshold, label, class, detector, or prior language

---

## 8. Exact next red-level question

The single next red-level user decision is:

**Authorize a Phase 6 reset branch?**

This means:
- Current Phase 6A formulation is closed as an apparatus-limited pilot
- Phase 6B is not justified from the current basis
- No further science proceeds without an explicit reset authorization
- A reset would need to address: synthetic exclusion, proper archive scope declaration, and the dual-bin occupancy constraint
