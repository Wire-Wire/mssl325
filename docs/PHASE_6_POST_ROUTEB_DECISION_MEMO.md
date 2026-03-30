# Phase 6 — Post-Route-B Decision Memo

**Date:** 2026-03-31
**Type:** Decision-space repair. No new science execution.
**Authority:** This memo reconstructs the actual post-Route-B decision space so the user can authorize the next bounded move. No route is chosen here. Phase 6B remains blocked.

---

## 1. Scope and authority

This memo does not execute science. It does not close Phase 6 or any route. It does not reopen frozen branches. It replaces the previous narrow three-option menu (close B / open C / close Phase 6) with the full four-option post-Route-B decision space that actually exists.

Phase 4B, Phase 5A/5B, and MMS branch remain frozen. No frozen claims are altered.

---

## 2. Actual current Phase 6 state

| Component | Status |
|---|---|
| Route A (mandatory provenance repair) | **Complete.** Synthetic fixtures removed. Clean catalogue N=9 real. Scope-match manifest produced. |
| Route B regression test | **Complete.** 5/12 encounters Route-B-computable. 1 low-cone recovered (t2_20080904_thd, cone=43deg). |
| Route B bounded execution | **Complete.** Dn_near and D\|B\|_near computed on all 5 computable encounters. Coherence assessment done. Ledger produced. |
| Route C (regime-access search) | **Not executed.** Remains a live option. |
| Route D (branch-question narrowing) | **Not executed.** Remains a live option. Was defined in `PHASE_6_RESET_OPTIONS.md` but never revisited after Route B execution. |
| Phase 6B (occurrence / detector-preparatory) | **Blocked.** Minimum preconditions (see `PHASE_6_RESET_OPTIONS.md` section 9) not met. |
| Frozen anchors | **Unchanged.** Phase 4B six-pass bank, THE Sep 19 external recurrence, MMS branch freeze all intact. |

---

## 3. What Route B now means

Route B is no longer hypothetical. It has been designed, regression-tested, and executed. Its actual yield is known:

**What it established:**
- The auxiliary descriptor (Dn_near = very_near/near density ratio, D|B|_near = very_near/near |B| ratio) is computable on 5 of 12 Phase 6 encounters.
- 3 of 5 computable encounters show Dn_near < 1 AND D|B|_near > 1 (density drops, |B| rises toward MP), consistent with an inner-sheath depletion gradient.
- The strongest signal is usable_sep26_09_10h (Dn_near=0.028, D|B|_near=2.055, perpendicular geometry, Dp=3.05 nPa).
- 1 low-cone encounter (t2_20080904_thd, cone=43deg) was recovered from the BG-occupancy-excluded tranche-2 set.

**What it did not establish:**
- The recovered low-cone encounter does not show a depletion signature (Dn_near=1.053, D|B|_near=1.071 — flat inner-sheath profile).
- The 3 encounters with clear inner-sheath gradients are all also evaluable under the original Dn/EB basis. Route B did not reveal new behavior in those encounters — it described the same encounters through a different lens.
- Route B descriptors (Dn_near, D|B|_near) are semantically distinct from frozen Phase 4B Dn/EB. They measure a different gradient (very-near vs near, not near vs background). The 2/4 cross-check divergence confirms this: an encounter can show Dn > 1 under the original basis while showing Dn_near < 1 under Route B. These are not interchangeable.

**Modest but nonzero descriptive yield:**
- Route B confirms that inner-sheath density/field gradients exist in some compressed-sheath encounters.
- Route B recovered one low-cone data point, but that data point is flat.
- Route B does not extend meaningful regime coverage. It does not answer the cone-angle conditioning question.

---

## 4. The repaired post-Route-B decision space

Four options are live. Each is independent; they are not a sequence.

| Option | Short label |
|---|---|
| **A** | Route B continuation |
| **B** | Route C execution |
| **C** | Route D-style narrowing |
| **D** | Writing-safe return |

---

## 5. Option A: Route B continuation

**What it solves:** Could refine the inner-sheath descriptor with additional QC layers (boundary-layer contamination assessment, very-near bin uncertainty quantification) or expand the Route B universe by searching for encounters with very-near occupancy in unsearched parts of the 2007-2010 archive.

**What it preserves:** Route B descriptor semantics already established. Phase 4B frozen. No measurement-model change to the frozen Dn/EB basis.

**What it sacrifices:** Time. Route B has already shown modest yield. Further work on the same descriptor may not improve regime coverage. The very-near bin's low occupancy (4.5% for the recovered low-cone encounter) and potential boundary-layer contamination (sep26_09_10h vn density is 1.7 cm-3 vs near density of 63 cm-3 — a 36x ratio suggesting possible MP boundary-layer sampling) are structural concerns that more encounters cannot resolve.

**Scientific ceiling:** Inner-sheath gradient descriptors computed on a modestly larger sample, still not directly comparable to Phase 4B Dn/EB, still unlikely to populate the quasi-radial regime (cone <=30deg).

**Main risk:** Diminishing returns. The mechanism is understood. The yield is known to be modest. Additional encounters will likely reproduce the same occupancy pattern.

**First executable action if chosen:** Design a targeted very-near-occupancy search of unsearched parts of the 2007-2010 THEMIS archive, focusing on intervals where THD/THE were deep inside the inner magnetosheath (small s).

---

## 6. Option B: Route C execution

**What it solves:** Searches for encounters that satisfy the original dual-bin occupancy requirement (Dn/EB computable) at lower cone angles. Preserves direct comparability with the frozen Phase 4B bank.

**What it preserves:** Dn/EB descriptor definitions. Phase 4B frozen bank as the comparison baseline. Encounter-averaged boundaries. Cone-angle-first conditioning logic.

**What it sacrifices:** May sacrifice time and effort if the low-cone + high-Dp co-occurrence is physically rare. The tranche-2 pilot found only 3 low-cone candidates (cone 43-44deg) and all had Dp < 2.7 nPa. A broader search covers 2007, 2010, and non-Aug-Oct months, which are unsearched, but the co-occurrence rarity is a physical constraint, not a search-design failure.

**Scientific ceiling:** If successful: a small low-cone + high-Dp sample with Dn/EB directly comparable to the Phase 4B compressed-sheath bank. This would enable a bounded two-regime descriptive comparison. If unsuccessful: a documented null result confirming the co-occurrence rarity.

**Main risk:** The searched subspace yields zero additional evaluable low-cone encounters, reproducing the tranche-2 outcome on a larger scale. This would be informative (confirming the structural limitation) but would not advance the science.

**First executable action if chosen:** Define the unsearched parts of the 2007-2010 THEMIS dayside archive (2007, 2010, non-Aug-Oct 2008-2009). Design a systematic low-cone search with explicit scope-match discipline. Set a firm stop criterion (e.g., if zero retained after full search, close Route C).

---

## 7. Option C: Route D-style narrowing

**What it solves:** Accepts that the quasi-radial regime is structurally inaccessible under the current apparatus and narrows the Phase 6 branch question to: within the accessible non-radial / compressed-sheath regime, is there finer-grained conditioning structure (cone-angle bins, clock-angle bins, Dp sub-stratification)?

**What it preserves:** Frozen measurement model. Dn/EB definitions. Phase 4B frozen bank. The clean N=9 tranche-1 catalogue as the working universe. No new search needed.

**What it sacrifices:** Gives up explicitly on answering the quasi-radial conditioning question. The low-cone / quasi-radial regime becomes a documented "not assessed" boundary. Also: N=9 may be too small for meaningful within-regime stratification. The existing sample already showed only 2 cone-angle bins with unequal N (perpendicular=5, intermediate=4, quasi-radial=0).

**Scientific ceiling:** A documented within-regime exploratory stratification showing whether Dn/EB varies systematically within the accessible compressed-sheath / non-radial regime. At best this would be a methodological contribution: "the measurement model can detect within-regime descriptor variation at the encountered sample size." At worst: N=9 is too sparse for any subdivision to be informative.

**Main risk:** N=9 is structurally too small for the subdivision to yield anything beyond what Phase 4B already showed. Route D may just repackage the existing bank without new insight.

**First executable action if chosen:** Produce a formal within-regime stratification design on the clean N=9 sample, specifying: which upstream dimensions to stratify by, minimum bin size, what "informative" means at this N, and an explicit stop criterion.

---

## 8. Option D: Writing-safe return

**What it solves:** Accepts Phase 6 as a completed exploratory branch that documented: (a) the Dp-dependent dual-bin occupancy barrier, (b) the Route B inner-sheath descriptor as a modest but real alternative lens, (c) the structural inaccessibility of the quasi-radial regime under the current apparatus. Returns the project to frozen-writing-safe mode for thesis integration.

**What it preserves:** Everything frozen. Phase 4B claims. MMS branch freeze. Route B execution as a documented methodological sidecar. No measurement-model changes. No scope expansion.

**What it sacrifices:** Gives up on answering the cone-angle conditioning question within the thesis. The quasi-radial question becomes an explicitly deferred future-work item. Phase 6 would be documented as a methodological exercise: "we attempted upstream conditioning, discovered an apparatus limitation, explored an alternative inner-sheath descriptor with modest yield, and closed the branch."

**Scientific ceiling:** Phase 6 contributes to the thesis as a methods/limitations chapter section. The frozen Phase 4B bank remains the primary science result. Route B's inner-sheath gradients may appear as a brief supplementary observation. The strongest Phase 6 thesis statement would be: "upstream-conditioning analysis was attempted; the dual-bin occupancy requirement creates a Dp-dependent access barrier that excludes the low-cone regime at the inner-probe apogee; this limitation is documented for future work with wider-apogee missions."

**Main risk:** Phase 6 yields no new science results for the thesis beyond the methodological finding. This is the safest option but also the lowest-yield.

**First executable action if chosen:** Write Phase 6 into a thesis-safe "Methods: Upstream Conditioning Attempt" section, documenting the Dp barrier, Route B sidecar, and explicit future-work pointers. Update the thesis writing pack.

---

## 9. Exact strongest supportable current Phase 6 statement

Phase 6 attempted upstream conditioning of the frozen THEMIS measurement model. Route A repaired the encounter catalogue (N=9 real after synthetic removal). Route B introduced an auxiliary inner-sheath descriptor (Dn_near, D|B|_near) that does not require background-bin occupancy. The bounded execution showed that 3 of 5 computable encounters exhibit an inner-sheath density-depletion / field-enhancement gradient. One low-cone encounter (cone=43deg) was recovered but shows no depletion signature. The dual-bin occupancy requirement creates a Dp-dependent structural barrier that excludes the quasi-radial regime at the inner-probe apogee. The quasi-radial conditioning question remains unanswered.

---

## 10. Exact strongest blocked overclaim

Any of the following would be overclaiming:
- "Route B shows that the PDL extends into the inner sheath" (Route B shows inner-sheath gradients in some encounters; it does not identify a physical layer)
- "The quasi-radial regime is inaccessible" (it is inaccessible under the current apparatus and measurement model; a wider-apogee mission or different formulation could revisit it)
- "Phase 6 confirms the cone-angle dependence of PDL signatures" (Phase 6 did not populate the quasi-radial bin; it cannot confirm or deny cone-angle dependence)
- "Route B descriptors are consistent with Phase 4B Dn/EB" (they measure different gradients; the 2/4 cross-check divergence explicitly demonstrates non-interchangeability)
- Any threshold, label, class, or detector-level language applied to Route B results

---

## 11. Exact next red-level user question

**Which of the four post-Route-B options should be authorized next?**

| Option | Label | One-line purpose |
|---|---|---|
| **A** | Route B continuation | Refine or expand the inner-sheath descriptor (modest expected yield, new encounters unlikely to change the picture) |
| **B** | Route C execution | Search for low-cone encounters evaluable under original Dn/EB (may hit co-occurrence rarity wall) |
| **C** | Route D-style narrowing | Narrow to within-regime stratification on the accessible N=9 sample (may be too sparse) |
| **D** | Writing-safe return | Accept Phase 6 as a methodological finding and return to thesis writing (safest, lowest yield) |

Phase 6B remains blocked regardless of choice.
No option requires or enables thresholds, labels, detector semantics, or class language.

---

## 12. Files and references

| Document | Role |
|---|---|
| `docs/PHASE_6_ROUTEB_BOUNDED_EXECUTION.md` | Route B execution results and coherence assessment |
| `docs/PHASE_6_ROUTE3_B_COMPATIBLE_MEASUREMENT_MODEL.md` | Route B design and regression test (superseded by bounded execution) |
| `docs/PHASE_6_ROUTE3_ACTIVATION.md` | Route 3 activation (Route A repair + Route B regression) |
| `docs/PHASE_6_RESET_OPTIONS.md` | Original B/C/D reset options (pre-execution) |
| `docs/PHASE_6A_AUDIT_AND_RESET_NOTE.md` | Phase 6A audit and control reset |
| `reports/themis_conditioning/route3b_ledger.json` | Route B full ledger |
| `reports/themis_conditioning/route3b_ledger.csv` | Route B tabular ledger |
| `reports/themis_conditioning/encounter_catalogue_clean.json` | Clean N=9 catalogue |
