# MMS Thickness Branch — Freeze Document

**Date:** 2026-03-29
**Status:** Frozen under current basis. No reportable thickness. Writing-safe for thesis integration.

---

## 1. Scope and status

The MMS thickness branch was opened as an independent methodological branch, decoupled from the frozen THEMIS comparator bank. Its purpose was to determine whether a small number of MMS near-magnetopause gradient intervals could support defensible event-level thickness estimates using multi-spacecraft timing and gradient methods.

The branch completed five stages before freezing:
1. Methods scaffold — defined eligibility gates, dual thickness definitions, normal hierarchy, uncertainty framework, and quality grading
2. Event shortlist — screened 11 MMS1 near-subsolar dayside passes (Phase 1, 2015–2017); found 3 primary + 1 reserve candidates
3. Readiness audit — full event-package analysis on 3 primaries; 2 advanced (MMS-P1, MMS-P3), 1 held (MMS-P2)
4. First thickness attempt — MMS-P1 (2015-11-12) attempted under the full scaffold; outcome: **do_not_report**
5. Basis reset — root-cause diagnosis; revised thickness-reportability criterion proposed; pause recommended

**Current status: frozen.** No reportable MMS thickness exists. No further analysis is authorized under the current basis.

---

## 2. Branch history

The methods scaffold defined two complementary thickness definitions (timing-based and gradient-scale), a normal-estimation hierarchy requiring cross-checking, an uncertainty ledger combining multiple error sources, and a Gold/Silver/Bronze quality grading scheme. The scaffold's eligibility gate required near-subsolar geometry, upstream steadiness, four-spacecraft data completeness, tetrahedron quality, and an identifiable gradient interval.

From 11 screened MMS1 dayside passes, 3 primary candidates survived coarse screening (density gradient structure, FGM/FPI completeness, upstream steadiness). MMS-P1 (2015-11-12) was selected for the first attempt because it had the smallest nominal distance to the modeled magnetopause (0.4 Re) and the clearest boundary-crossing signature.

The MMS-P1 attempt found a clear near-MP gradient (|B| drops ~28 nT, density drops ~10 cm⁻³ over ~5 min) observable on all four spacecraft. However, both thickness paths failed:
- **Timing:** MVA normal poorly constrained (λ₂/λ₁ = 3.0, 70° from expected direction); 4-SC timing degenerate at ~10 km separation
- **Gradient:** Tetrahedron separation (~10 km) approximately two orders of magnitude smaller than the gradient spatial scale (~750–3750 km)

The basis reset confirmed that this scale mismatch is structural: MMS Phase 2 separations (~25 km) provide only a 2–3× improvement, which is insufficient against a 40–100× gap. The original scaffold's eligibility gate lacked a separation–scale match criterion, which allowed a boundary-adjacent event that was structurally not thickness-reportable.

---

## 3. What was learned

### Positively established

1. The scaffold's methods (timing, gradient, normal hierarchy, uncertainty framework) are sound in principle and implementable from CDAWeb data.
2. The MMS-P1 event contains a real, four-spacecraft-observable near-MP gradient structure.
3. The dominant thickness-reportability constraint is separation–scale match, not data quality, upstream conditions, or method design.
4. MMS Phase 1 (~10 km) and Phase 2 (~25 km) tetrahedra are structurally too small for typical extended near-MP gradient layers (~100–3000 km).

### What failed

5. No defensible thickness estimate could be produced for MMS-P1.
6. Neither timing-based nor gradient-scale definitions yielded a reportable result.
7. The current shortlist/readiness basis did not include a separation–scale match gate, which is necessary to avoid future scale-mismatch failures.

### Root-cause decomposition

The failure is driven by three interacting causes, not only the geometric mismatch:

**Primary cause — geometric scale mismatch.** The structure to be measured (~750–3750 km) exceeds the tetrahedron separation (~10–34 km) by 40–100×. In the multi-spacecraft timing literature, timing/triangulation error is controlled by whether crossing times can be stably and unambiguously marked and whether the formation geometry provides adequate baseline. When the crossing-time uncertainty is comparable to the inter-spacecraft time delay, the normal and speed become indefensible, and thickness follows.

**Contributing cause — method applicability domain.** The timing method's classical assumptions (approximately 1-D, planar boundary moving at constant speed, with unambiguous per-spacecraft passage-time identification) are not met for a broad, possibly non-planar gradient region. The four-point gradient/reciprocal-vector methods amplify relative error when the measured inter-spacecraft differences are small compared to measurement noise — exactly the regime encountered when separation is much smaller than the gradient scale.

**Contributing cause — object-definition ambiguity.** The target structure is a broad near-MP gradient/transition/pileup-depletion region, not a thin current sheet or sharp discontinuity. Published PDL studies note that the outer boundary of the depletion layer is typically not sharp and that defining it carries inherent arbitrariness (whether by depletion factor, beta criterion, or N/B ratio). MMS was designed for thin-structure resolution at electron-kinetic scales, not for spatially extended gradient layers.

### Literature-grounded scale expectation

The observed gradient scale (~750–3750 km, or ~0.12–0.59 Re) is consistent with published PDL/pileup thickness estimates across multiple missions and epochs: classical theory predicted depletion layers of ~700–1300 km under certain parameters (Zwan & Wolf 1976); observational estimates range from ~0.1 Re (ISEE straight crossings) to ~0.6–1 Re in individual case studies. The observed scale at MMS-P1 is not anomalous — it is typical for this class of structure.

### What the failure most likely means

8. The failure is not event-specific. Any near-MP gradient layer with a spatial scale much larger than the tetrahedron separation (~100+ km) would produce the same outcome under MMS Phase 1/2.
9. Viable thickness measurement under the current scaffold methods would require either much larger inter-spacecraft separations (Cluster-scale, ~100–10,000 km) or events with much sharper structure (sub-100 km gradient scale).

### Closed continuation routes

An independent literature review confirmed that no viable continuation route exists under the current basis:

| Route | Assessment |
|---|---|
| Continue current shortlist (more Phase 1/2 events) | Same separation, same scale mismatch. High probability of repeating do_not_report. |
| Refine MVA/normal methods | Cannot overcome a physical configuration mismatch. Published MMS boundary studies confirm that non-planar, non-stationary boundaries cause normal-method disagreement systematically. |
| Use OMNI/model distance as geometric truth | OMNI is a propagated/time-shifted L1 product with documented representativeness limitations. Magnetopause model accuracy has a theoretical ceiling imposed by upstream propagation uncertainty. Neither constitutes event-level geometric truth. |
| Switch to MMS current-sheet thickness (thin-layer target) | Methodologically viable and well-matched to MMS separation. But this answers a different scientific question (current-sheet structure, not broad gradient-layer thickness). |
| Downgrade deliverable to operational effective width | Reduces the claim but still depends on boundary-definition choices and model/propagation geometry. Medium risk of circularity. |
| Switch mission (e.g. Cluster) | Scale-matched but constitutes a new project outside current scope. |

### What remains unknown

10. Whether sharp sub-100 km near-MP features exist and are thickness-eligible under the current scaffold is untested.
11. Whether a fundamentally different measurement approach (single-spacecraft empirical, or Cluster-based) would succeed is outside the scope of this branch.

---

## 4. Exact strongest supportable statement

The MMS thickness branch demonstrates that multi-spacecraft timing and gradient methods, as defined in the project scaffold and applied to MMS-P1 (2015-11-12), cannot produce a defensible near-MP gradient thickness estimate when the tetrahedron separation (~10 km in Phase 1) is approximately two orders of magnitude smaller than the observed gradient spatial scale (~750–3750 km). This is a structural configuration constraint of the MMS Phase 1 dayside constellation, not a data-quality or method-design failure. The gradient structure at MMS-P1 is real and observed on all four spacecraft, but is too spatially extended for the available inter-spacecraft baseline. MMS Phase 2 separations (~25 km) provide insufficient improvement.

---

## 5. Exact strongest non-claim

This branch does not provide any event-level thickness estimate, any quality-graded thickness set, any MMS-based validation of THEMIS comparator results, any physical identification of the observed gradient as a specific magnetosheath structure, or any detector/threshold/label semantics. The do_not_report outcome for MMS-P1 does not mean the gradient is unreal — it means the measurement configuration is not matched to the structure scale. The failure to produce a thickness does not invalidate MMS for all boundary studies; MMS excels at resolving thin structures where its separation matches the target scale.

---

## 6. What this branch does NOT provide

- No reportable event-level thickness (L ± σ)
- No quality-graded (Gold/Silver/Bronze) thickness set
- No MMS-based validation or upgrading of THEMIS Dn/EB results
- No connection between MMS P1 outcome and frozen THEMIS cautious passes (P1/P3)
- No physical class identification for any MMS or THEMIS window
- No detector, threshold, or label semantics

---

## 7. How this branch should be used in thesis writing

### Where it belongs

The MMS branch belongs in the **methods / measurement-model limitations** section of the thesis, not in the main results. It documents:
- A rigorous methods scaffold for multi-spacecraft near-MP thickness measurement
- A concrete application attempt that identified a structural scale-mismatch limitation
- A revised thickness-reportability criterion (separation–scale match) that was missing from the original design

### How to cite

- The scaffold design is citable as a defensible methods framework
- The P1 attempt is citable as a documented negative methodological result
- The scale-mismatch finding is citable as a thesis-level methodological contribution
- The revised reportability criterion (gradient scale within ~10× of tetrahedron separation) is citable as a practical recommendation

### How NOT to cite

- Do not cite the MMS branch as having produced a thickness result
- Do not cite the P1 gradient as a confirmed physical structure type
- Do not use the MMS outcome to validate or invalidate THEMIS results
- Do not frame the failure as MMS being generally unsuitable for magnetopause studies

---

## 8. Safe wording block

### Thesis paragraph

The MMS thickness branch applied a multi-spacecraft methods scaffold — comprising timing-based and gradient-scale thickness definitions, a normal-estimation hierarchy, and an explicit uncertainty framework — to a near-subsolar dayside MMS event (2015-11-12, SZA = 18°) showing a clear boundary-adjacent density and magnetic-field gradient on all four spacecraft. Both thickness paths produced non-reportable results because the MMS Phase 1 inter-spacecraft separation (~10 km) was approximately two orders of magnitude smaller than the observed gradient spatial scale (~750–3750 km), rendering the multi-spacecraft timing degenerate and the gradient computation noise-dominated. A subsequent feasibility probe confirmed that MMS Phase 2 separations (~25 km) provide only a 2–3× improvement, which is insufficient. The branch was frozen with no reportable event-level thickness, and the separation–scale match requirement was identified as a necessary addition to the thickness-eligibility gate.

### Paper paragraph

We attempted multi-spacecraft timing and gradient-scale thickness estimation on an MMS1 near-subsolar dayside event (2015-11-12) with four-spacecraft FGM/FPI coverage and a clear near-MP gradient. Both methods failed because the ~10 km Phase 1 tetrahedron separation was ~100× smaller than the gradient's estimated spatial scale. Phase 2 separations (~25 km) were found to be similarly inadequate. No reportable thickness was produced. The failure identifies a structural separation–scale match criterion for multi-spacecraft near-MP gradient thickness measurement.

### Safe sentences

1. "The MMS Phase 1 tetrahedron separation (~10 km) is structurally mismatched to the spatial scale of extended near-magnetopause gradient layers (~750–3750 km)."

2. "Both timing-based and gradient-scale thickness methods produced non-reportable results for the pilot event, owing to this separation–scale mismatch."

3. "The observed gradient structure is real and four-spacecraft-observable, but too spatially extended for the available inter-spacecraft baseline."

4. "A revised thickness-eligibility criterion requiring gradient spatial scale within approximately one order of magnitude of the tetrahedron separation was identified as a necessary scaffold addition."

5. "MMS Phase 2 separations (~25 km) provide only a 2–3× improvement over Phase 1, which is insufficient for extended gradient layers."

6. "No MMS event-level thickness exists in the current project; the branch is frozen as a documented methodological finding."

### Do not say

1. ~~"The MMS thickness attempt failed because the event was not a real boundary structure."~~ (The gradient is real; the configuration is mismatched.)

2. ~~"MMS cannot be used for magnetopause thickness measurement."~~ (MMS resolves thin structures well; it is extended gradients that are mismatched.)

3. ~~"The MMS result confirms the THEMIS low-Dn finding."~~ (The branches are independent and decoupled.)

4. ~~"The thickness-scaffold methods are flawed."~~ (The methods are standard; the configuration input is wrong for this structure scale.)

5. ~~"No near-MP gradient layer exists at the pilot event location."~~ (One clearly does; it is simply too wide for the tetrahedron.)

6. ~~"This negative result means MMS thickness work should be abandoned in the thesis."~~ (The documented negative result is a legitimate methodological contribution.)
