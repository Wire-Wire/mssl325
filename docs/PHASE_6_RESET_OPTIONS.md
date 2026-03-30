# Phase 6 Reset Options — Decision Memo

**Date:** 2026-03-30
**Type:** Decision-space packaging. No new science.
**Prerequisite:** Phase 6A audited and closed as apparatus-limited pilot (`docs/PHASE_6A_AUDIT_AND_RESET_NOTE.md`).

---

## 1. Authority and scope

This memo does not reopen science. It makes the post-audit Phase 6 choice space legible so the user can authorize one bounded next move. Phase 4B remains the frozen claim-bearing baseline. Phase 6A remains closed as an apparatus-limited pilot. Phase 6B remains blocked.

---

## 2. What failed in the current Phase 6A formulation

Four interlocking failures, in order of severity:

**2a. Provenance / cache-derived universe problem.** The tranche-1 encounter universe was built by scanning all `runs/*/encounter_*.json` without filtering out synthetic-mode outputs. This admitted pilot_001 and pilot_002 (synthetic fixtures with hardcoded SZA = 0, Dp = 2, Bz = 2, Ma = 8) into the real-data catalogue. The reported N = 11 is actually N = 9 real + 2 synthetic.

**2b. Declared-slice vs searched-slice mismatch.** Tranche 2 declared "2007–2010 THEMIS dayside interval" but actually searched only THD + THE, Aug–Oct 2008–2009, every 3rd day. The 2007, 2010, and non-Aug–Oct subspaces were never searched. The zero-retained result applies to the searched subspace only.

**2c. Dual-bin occupancy / evaluability bottleneck.** The frozen measurement model requires both near-bin (s 0.2–0.4) and background-bin (s > 0.6) occupancy in a single encounter. At the ~11.6 Re inner-probe apogee, this requires encounter-averaged Dp > ~3 nPa to compress the sheath enough for the spacecraft to reach the background bin. Low-cone IMF conditions tend to co-occur with lower Dp, which means the dual-bin requirement systematically excludes the low-Dp / low-cone regime — the regime most relevant to the branch question.

**2d. Branch-question entanglement with platform reach.** The Phase 6A question ("how do descriptors shift across the full cone-angle range") implicitly required access to the quasi-radial regime. But the frozen measurement model + inner-probe orbit structurally limits access to a compressed-sheath, non-radial subset. The branch question was broader than what the current apparatus can answer.

---

## 3. What remains scientifically alive

Despite the pilot failure, the following remain open:

1. **The cone-angle-first science question is meaningful.** Published work (Pi et al. 2024; Michotte de Welle et al. 2024) shows that dayside magnetosheath spatial profiles are IMF-orientation-dependent. Whether near-MP descriptor behavior shifts with cone-angle regime in a controlled THEMIS sample remains an unanswered, testable question.

2. **The descriptor-first logic is sound.** Dn and EB as continuous encounter-level descriptors are well-defined under the frozen measurement model. The issue is not the descriptor semantics but the sample access.

3. **The broader upstream-conditioning question is not proven unanswerable.** It is only proven unanswerable *under the current formulation* (dual-bin requirement + inner-probe apogee + 2008–2009 Aug–Oct search). A different formulation could revisit it.

---

## 4. Mandatory repair layer (Route A)

**Required before any strategic reset. Not itself the science answer.**

Route A fixes the provenance and scope problems that infected Phase 6A:

| Repair | What it does |
|---|---|
| Synthetic-fixture exclusion | Filter the encounter universe to exclude synthetic-mode outputs (identifiable by hardcoded upstream Dp = 2, Bz = 2, Ma = 8, SZA = 0) |
| Scope-declaration / search-match discipline | Require that any future declared slice exactly matches the actual search space; log the match explicitly |
| Data-source filter | Require that the encounter universe is built only from live-mode CDAWeb-fetched runs, not from cached synthetic pilot runs |

**Route A is necessary but not sufficient.** After Route A, the corrected tranche-1 sample would be N = 9 real encounters, all with cone > 30°, all in the non-radial compressed-sheath regime. The dual-bin bottleneck and the empty quasi-radial bin would remain. Route A alone does not recover regime access or change the measurement model.

---

## 5. Strategic reset family B — measurement-model reset

**Focus:** Change or relax the dual-bin occupancy / evaluability requirement that creates the Dp-dependent bottleneck.

| Dimension | Assessment |
|---|---|
| **What it changes** | Relaxes or replaces the requirement that both near bin (s 0.2–0.4) and background bin (s > 0.6) must be populated in a single encounter. Options include: single-bin analysis (near-MP descriptors only, without background normalization), sliding s-window, or profile-based descriptors that do not require dual-bin occupancy. |
| **What it preserves** | Encounter as the unit, Sun–Earth-line s-mapping, Shue/Merka boundaries, cone-angle-first conditioning logic, OMNI-propagated upstream context. |
| **Main gain** | Potentially recovers access to the low-Dp / low-cone regime by removing the constraint that co-excludes it. Could dramatically expand the usable encounter universe. |
| **Main risk** | Without a background bin, Dn and EB (defined as near/background ratios) lose their current normalization basis. The measurement model would need a new descriptor definition, which means the Phase 4B frozen descriptors would not be directly comparable. This is a significant science-design cost. |
| **Open question** | Whether a single-bin or profile-based descriptor can carry the same interpretive weight as the dual-bin Dn/EB ratio is not established from current evidence. |

---

## 6. Strategic reset family C — regime-access / geometry-access reset

**Focus:** Preserve the current descriptor semantics (Dn, EB) while finding a different data route to populate the low-cone regime.

| Dimension | Assessment |
|---|---|
| **What it changes** | Expands the encounter search to either: (a) the full 2007–2010 interval (filling the declared-vs-searched gap), (b) additional probes or orbital phases where Dp happens to be higher during low-cone IMF periods, or (c) a different mission/spacecraft with wider apogee that can reach the background bin at lower Dp. |
| **What it preserves** | The frozen measurement model, Dn/EB descriptor definitions, encounter-averaged boundaries, cone-angle-first conditioning logic. |
| **Main gain** | If even a few low-cone encounters can be found where Dp is coincidentally high enough (>3 nPa), the dual-bin requirement would be met without changing the measurement model. The descriptors would remain directly comparable to the Phase 4B frozen bank. |
| **Main risk** | The co-occurrence of low cone angle + high Dp may be physically rare in the near-Earth environment. The tranche-2 pilot found only 3 candidates with cone 43–44° and all had Dp < 2.7 nPa. A broader search might find a few more, but a systematic emptiness of the low-cone + high-Dp co-occurrence space would leave this route similarly apparatus-limited. |
| **Open question** | Whether the unsearched parts of the 2007–2010 interval (2007, 2010, non-Aug–Oct months) contain low-cone + high-Dp encounters is unknown but testable. |

---

## 7. Strategic reset family D — branch-question reset

**Focus:** Narrow the branch question to the regime that is actually accessible, rather than trying to answer the full cone-angle-range question now.

| Dimension | Assessment |
|---|---|
| **What it changes** | Redefines the Phase 6 question from "how do descriptors shift across the full cone-angle range" to "within the accessible non-radial / compressed-sheath regime, how do descriptors shift with more granular cone-angle, clock-angle, and upstream pressure stratification." |
| **What it preserves** | The frozen measurement model, Dn/EB definitions, encounter-averaged boundaries, encounter as the unit. Also preserves the dual-bin requirement (since the accessible regime already satisfies it). |
| **Main gain** | Can proceed immediately on the corrected N = 9 real encounters plus any additional non-radial encounters from expanded search. No measurement-model change needed. The quasi-radial gap is explicitly acknowledged as a regime boundary rather than treated as a failure to be overcome. |
| **Main risk** | The corrected sample (N = 9) may be too small for meaningful within-regime stratification. The accessible regime is structurally biased toward compressed-sheath conditions (Dp > 3 nPa), which limits the interpretive range. This route explicitly gives up on answering the quasi-radial conditioning question. |
| **Open question** | Whether N = 9 (or a modestly expanded sample from broader search within the same regime) supports any finer-grained conditioning than tranche 1 already attempted. |

---

## 8. Routes to reject

| Rejected route | Why |
|---|---|
| **Route A alone as final answer** | Provenance repair corrects the catalogue but does not address the dual-bin bottleneck, the empty quasi-radial bin, or the small sample. After Route A, the branch is cleaner but not scientifically advanced. |
| **Same question + same measurement model + just search more** | The Phase 6A tranche-2 experience showed that low-cone encounters systematically fail the dual-bin screen under the current model. Searching more within the same constraints will likely produce the same empty result. |
| **Axis reset away from cone-angle-first** | The cone-angle-first framing is literature-supported (Pi et al. 2024; Michotte de Welle et al. 2024) and was the original Phase 6 design choice. Switching to a different primary axis (e.g., Bz sign, Dp, or clock angle) without new evidence motivating the switch would be ad hoc. |
| **Direct Phase 6B / detector / occurrence-preparatory launch** | The current evidence base (N = 9 real, provenance-contaminated catalogue, no quasi-radial coverage, no occurrence layer) does not support any detector-preparatory, occurrence-analysis, or threshold-exploration stage. |

---

## 9. Minimum preconditions for any future Phase 6B planning

Phase 6B (conditioned occurrence / detector-preparatory) cannot be authorized until ALL of the following are met:

1. **Route A completed:** provenance repair, synthetic exclusion, scope-match discipline in place.
2. **One strategic reset (B, C, or D) executed successfully** with a clean, properly scoped encounter catalogue.
3. **Corrected sample N sufficient** for the branch question: at minimum ~15–20 independent encounters for a 2-regime comparison, or ~10 for a single-regime granular stratification.
4. **At least two cone-angle regimes populated** (if B or C was chosen) or explicit acknowledgment that only one regime is addressable (if D was chosen).
5. **No inherited synthetic contamination** in the Phase 6B candidate universe.
6. **Occurrence/recovery bundle definition** completed as a separate authorized step before any recovery analysis is run.

---

## 10. Exact next red-level decision

This memo does not choose between B, C, and D.

The user is asked:

**After mandatory provenance/scope repair (Route A), which Phase 6 reset family should be authorized?**

| Option | One-line purpose |
|---|---|
| **B** | Change the measurement model to remove the dual-bin bottleneck (loses Dn/EB comparability with Phase 4B) |
| **C** | Preserve Dn/EB, expand the search for low-cone encounters with coincidentally high Dp (may hit the same physical co-occurrence limit) |
| **D** | Narrow the question to the accessible non-radial regime only (gives up quasi-radial, may work with the existing small sample) |

**Route A is mandatory regardless of B/C/D choice.** Phase 6B remains blocked until a reset succeeds.
