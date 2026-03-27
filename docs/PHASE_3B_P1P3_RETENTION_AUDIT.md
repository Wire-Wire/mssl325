# Phase 3B — P1/P3 Retention Audit

**Date:** 2026-03-27
**Authority:** User-authorized. Phase 3A signed off. Phase 3B authorized as P1/P3 retention audit only.
**Decision vocabulary:** confirmed-cautious or downgraded. No other dispositions permitted.
**Default rule:** If retention cannot be affirmatively defended, downgrade conservatively.

---

## Scope and guardrails

**Single question:** Can P1 and P3 remain in the six-pass interpretable bank as cautious low-Dn comparators, or should either be downgraded?

**Prohibited:** thresholds, labels, detector semantics, dev-set membership, bank expansion, measurement-model changes, promotion to clean, use of "upgrade" or "unchanged."

---

## P1 review (usable_aug18_6h — 2008-08-18)

### Current status
Cautious. Dn = 0.12, EB = 2.49. Near-bin density CV = 0.93. Membership = 86% (291 unknown/NaN points). Spike removal: Dn 0.12 → 0.17 (qualitatively stable), EB 2.49 → 2.29.

### 1. Mapping sensitivity
±1 nPa Dp perturbation shifts the mean-position s by −0.16 to +0.13. At Dp−1 nPa (= 3.2 nPa), the near bin gains at the expense of background. At Dp+1 nPa (= 5.2 nPa), the background bin gains. The bin-assignment balance is moderately sensitive to encounter-averaged Dp. Under the frozen measurement model, this is a known and accepted uncertainty (Walsh et al. 2019; Lin et al. 2024). P1's Dn is computed from whichever points fall in the near and background bins under the encounter-averaged boundary positions. A 1 nPa Dp error could shift which physical intervals contribute to each bin, but cannot be resolved without time-varying s (deferred).

**Assessment:** Mapping sensitivity is moderate and within the range documented for all passes. Not a specific basis for downgrading P1 beyond its existing cautious status.

### 2. Propagated-upstream limitations
P1's encounter-averaged Dp = 4.2 nPa, Bz = +0.3 nT. OMNI propagation introduces uncertainty in both timing and magnitude (Vokhmyanin et al. 2019). The Bz is nearly zero, meaning the boundary model is not strongly Bz-dependent for this pass. The Dp = 4.2 nPa is the highest in the bank, placing P1 in the most compressed-sheath regime. Under compressed conditions, the sheath is thinner and small Dp errors produce proportionally larger s shifts. This adds to the mapping-sensitivity concern but does not introduce a qualitatively new risk.

**Assessment:** No specific upstream-propagation basis for downgrading beyond cautious.

### 3. Foreshock / jet alternatives
P1 has the highest near-bin density CV (0.93) in the bank. This extreme noise level means the median near-bin density — which determines Dn — is computed from a highly variable sample. Archer & Horbury (2013) and Raptis et al. (2020) document that Pdyn spikes in the dayside sheath are heterogeneous and can create localized density enhancements and depressions. P1's 24% spike fraction is concentrated entirely in the background bin (344 spikes in BG, 0 in near), which means the near-bin density itself is not directly spike-contaminated. However, the high overall density variability (CV = 0.70 on raw data) suggests that the near-bin sample may be dominated by large-amplitude fluctuations rather than a broad, ordered spatial structure.

**This is the critical concern for P1.** The Dn = 0.12 (after spike removal: 0.17) is by far the lowest in the bank. A near-bin density CV of 0.93 means the standard deviation is nearly equal to the mean. Under these conditions, the median near-bin density is a noisy estimator, and the Dn ratio is driven by a few low-density intervals rather than a sustained spatial pattern. Whether those low-density intervals reflect genuine spatial structure, mirror-mode/wave packets (Soucek et al. 2015), or simply high magnetosheath variability cannot be determined from current data products.

**Assessment:** The foreshock/jet concern does not directly contaminate P1's near bin (spikes are in BG), but the extreme density variability in the near bin means the low-Dn value is carried by a noisy median. This is the most serious unresolved risk for P1.

### 4. Mixing risk
P1 has 291 unknown/NaN points (14% of data), the most in the bank. Only 5% of valid density points are below 1.0 cm⁻³; none are below 0.5 cm⁻³. Magnetospheric mixing under northward Bz (Li et al. 2009) typically produces cold, dense plasma in the boundary layer, not extremely low density. The P1 Bz is +0.3 (weakly northward), so cold-dense mixing is plausible in principle, but the density distribution does not show a clear magnetospheric-like population. The conservative membership check classifies 86% as sheath-plausible.

**Assessment:** Mixing risk is not the dominant concern for P1. The high unknown/NaN fraction is a data-quality issue, not a mixing signature. No basis for downgrading on mixing alone.

### 5. Boundary-motion risk
P1 spans 6 hours (18:00–00:00 UT). Over this duration, the magnetopause position can vary substantially (Plaschke et al. 2009 document multi-Re MP motion on timescales of minutes to hours). The encounter-averaged s uses a single set of boundaries for the entire window. If the MP moved inward during part of the window, some "near-bin" points may actually have been in the magnetosphere, and some "background" points may have been closer to the MP than the averaged s indicates. This is a shared limitation of all 6-10h windows in the bank, not P1-specific.

**Assessment:** Boundary-motion risk is a bank-wide caveat. Not a P1-specific basis for downgrading.

### P1 disposition

The mapping sensitivity, upstream propagation, mixing, and boundary-motion risks are within the range already documented for the bank and do not require downgrading beyond cautious.

However, the foreshock/jet dimension reveals that P1's extreme near-bin density variability (CV = 0.93) means the Dn = 0.12 value is driven by a noisy median, not a sustained spatial structure. This concern was already identified in Phase 2C and is the reason P1 was classified as cautious. The audit does not find new evidence that resolves this concern, nor does it find evidence that makes it worse.

**Disposition: confirmed-cautious.**

P1 may remain in the interpretable bank as a cautious low-Dn comparator. Its Dn = 0.12 must always be reported with the caveat that the near-bin density CV = 0.93 means the ratio is driven by a noisy sample, and whether this reflects genuine spatial structure or high magnetosheath variability cannot be determined under the frozen measurement model.

---

## P3 review (usable_sep13_09_6h — 2009-09-13)

### Current status
Cautious. Dn = 0.39, EB = 1.96 (EB drops to 1.46 after spike removal, Δ = 0.50). Membership = 100%. Spike removal: Dn 0.39 → 0.41 (robust), EB 1.96 → 1.46. Near-bin density CV = 0.47.

### 1. Mapping sensitivity
±1 nPa Dp perturbation shifts the mean-position s by −0.23 to +0.17. This is the LARGEST mapping sensitivity of any pass examined, because P3 has the lowest Dp in the cautious group (3.1 nPa) and the sheath is wider. At Dp−1 (= 2.1 nPa), the mean-position s drops from 0.54 to 0.31 — a large shift that would move many background points into the gap or near bin. This means P3's bin assignments are particularly sensitive to upstream-pressure uncertainty.

**Assessment:** Mapping sensitivity for P3 is larger than for most other passes. The Dn value is moderately robust (0.39 → 0.41 after spike removal), but the bin populations that produce this Dn depend on a Dp value (3.1 nPa) that is near the lower edge of the bank's usability range. A 1 nPa Dp error could substantially redistribute points across bins.

### 2. Propagated-upstream limitations
P3's Dp = 3.1 nPa is the second-lowest encounter-averaged pressure in the interpretable bank. At this Dp, the sheath is wider and the dual-bin coverage depends more critically on the boundary compression being accurate. OMNI propagation uncertainty (Vokhmyanin et al. 2019) at Dp ~ 3 nPa could represent a proportionally larger fractional error than at Dp ~ 4 nPa. The Bz = −1.4 nT (southward) affects the MP standoff via the Shue model's Bz-dependent coefficient.

**Assessment:** P3 is more vulnerable to upstream propagation uncertainty than higher-Dp passes. This does not invalidate the pass but adds weight to the mapping-sensitivity caveat.

### 3. Foreshock / jet alternatives
P3 has 25% spike fraction, with 531 of 542 spikes concentrated in the background bin. The near-bin density CV = 0.47 is moderate (not extreme like P1's 0.93). The near bin itself appears relatively clean of spike contamination. The EB shift from 1.96 to 1.46 after spike removal is driven by the BG-bin |B| being inflated by spike intervals, not by near-bin contamination.

**Assessment:** The near-bin density for P3 is reasonably clean (CV = 0.47, no spike contamination in the near bin). The Dn = 0.39 (robust to spike removal at 0.41) is a more defensible measurement than P1's Dn = 0.12. The EB value is spike-dependent (already documented), but Dn is not.

### 4. Mixing risk
P3 has 100% membership, 0 NaN points, and Bz = −1.4 nT (southward). Southward Bz disfavors cold-dense mixing (Li et al. 2009), which is primarily a northward-Bz phenomenon. The density distribution does not show evidence of magnetospheric-like contamination.

**Assessment:** Mixing risk is low for P3. No basis for concern.

### 5. Boundary-motion risk
P3 spans 6 hours (17:00–23:00 UT). The bank-wide boundary-motion caveat applies. The Dp = 3.1 nPa is relatively low, meaning the MP is further out and boundary motion could be proportionally more impactful on near-bin assignments. This adds to the mapping-sensitivity concern.

**Assessment:** Boundary-motion risk is a bank-wide caveat with moderate additional concern for P3 due to low Dp.

### P3 disposition

P3's Dn = 0.39 is robust to spike removal (Δ = 0.02), the near bin is not spike-contaminated (CV = 0.47), and mixing risk is low (100% membership, southward Bz). The EB spike-dependency (already documented) is carried forward as an existing caveat.

The mapping-sensitivity concern is more serious for P3 than for most other passes because Dp = 3.1 nPa is near the bank's lower usability edge and produces the largest s-perturbation of any examined pass. However, the Dn value itself is robust to the spike-removal test, which is the strongest available interval-level sensitivity check under the frozen measurement model.

**Disposition: confirmed-cautious.**

P3 may remain in the interpretable bank as a cautious low-Dn comparator. Its Dn = 0.39 must always be reported with the caveats that (a) EB is partially spike-dependent, (b) mapping sensitivity is high due to low Dp, and (c) the bin-assignment balance depends on a Dp value near the bank's lower usability edge.

---

## Measurement-model ceiling summary

The frozen measurement model (encounter-averaged Shue98/Merka05, Sun–Earth-line s, propagated OMNI inputs) imposes the following ceilings on what the P1 and P3 Dn values can be claimed to represent:

1. Dn is a ratio of encounter-level median densities in two s-bins. It is not a point measurement of depletion at a known spatial location.
2. The s-bin assignments depend on encounter-averaged Dp and Bz, not time-varying boundary positions. A ±1 nPa Dp error shifts s by 0.13–0.23 for these passes.
3. The upstream Dp and Bz are OMNI-propagated values, not locally measured. Their accuracy is condition-dependent (Vokhmyanin et al. 2019; Walsh et al. 2019).
4. Shue 1998 and Merka 2005 are empirical fits with documented condition-dependent accuracy (Lin et al. 2024; Aghabozorgi et al. 2024). Neither is per-event truth.

---

## Confounder-plausibility summary

| Confounder | P1 | P3 |
|---|---|---|
| Jet/spike (near bin) | Not directly contaminated (0 near spikes), but extreme density noise (CV=0.93) | Not contaminated (10 near spikes out of ~380 near points); CV=0.47 |
| Wave/mirror | Unresolved. High density CV is consistent with mirror-mode or wave activity. | Moderate density CV. No specific wave evidence. |
| Transient | UNKNOWN for both | UNKNOWN for both |
| Mixing | Low risk (density > 0.5 everywhere; weakly northward Bz) | Low risk (100% membership; southward Bz disfavors mixing) |
| Boundary motion | Bank-wide caveat | Bank-wide caveat; higher mapping sensitivity at Dp=3.1 |

---

## Final dispositions

| Pass | Disposition | Key caveat carried forward |
|---|---|---|
| **P1** | **confirmed-cautious** | Near-bin density CV = 0.93; Dn = 0.12 driven by noisy median; 14% NaN; whether pattern is spatial structure or high variability is unresolvable under frozen model |
| **P3** | **confirmed-cautious** | EB partially spike-dependent (Δ=0.50); mapping sensitivity is the largest in the bank (±0.23 for ±1 nPa Dp); Dp=3.1 near lower usability edge |

---

## Exact strongest low-Dn statement that remains supportable

Under the frozen measurement model, two cautious passes (P1 and P3) produce encounter-level Dn values below 0.5 (P1: 0.12, P3: 0.39). Both are robust to spike removal (P1: 0.12→0.17, P3: 0.39→0.41). However, P1's Dn is driven by a near-bin density median from a highly variable sample (CV = 0.93), and both passes carry encounter-averaged mapping sensitivity that could redistribute bin populations under ±1 nPa upstream perturbation. The clean core (P2, P4, P5, P6) has no pass with Dn below 0.94. All low-Dn evidence in this bank is cautious-only.

## Exact low-Dn statement that remains unsupported

It is not supportable to claim that the current bank contains confounder-tested evidence for Dn < 0.5 behavior. Both low-Dn passes carry documented caveats that cannot be resolved under the frozen measurement model. The low-Dn pattern may reflect genuine boundary-adjacent spatial structure, but it may equally reflect high magnetosheath variability (P1) or mapping-sensitivity artifacts at low Dp (P3).

## Whether the six-pass bank remains defensible

**Yes.** The six-pass interpretable bank (P2, P4, P5, P6 clean core + P1, P3 confirmed-cautious) remains defensible as a descriptive comparator bank under the frozen measurement model. Both P1 and P3 survive retention audit as confirmed-cautious. The bank spans Dn 0.12–2.31 and EB 0.80–2.49 across 6 independent passes, with all Dn < 0.5 evidence explicitly marked as cautious.
