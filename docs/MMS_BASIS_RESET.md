# MMS Thickness-Reportability Basis Reset

**Date:** 2026-03-29
**Stage:** Post-P1 diagnosis and next-step decision hardening. Not a thickness attempt.
**Authority:** User-authorized basis-reset round.

---

## A. Current MMS branch state

| Item | Status |
|---|---|
| Methods scaffold | Complete |
| Event shortlist | Complete (3 primary + 1 reserve from 11 screened) |
| Readiness audit | Complete (P1/P3 advance, P2 hold) |
| P1 thickness attempt | Complete: **do_not_report** |
| P3 thickness attempt | Not attempted |
| Reserve activation | Not attempted |
| Thickness values reported | **Zero** |

### What P1 showed

A clear near-MP gradient exists (|B| drops ~28 nT, density drops ~10 cm⁻³ over ~5 min). The gradient structure is real and observable on all four MMS spacecraft. But the ~10 km Phase 1 tetrahedron separation is ~100× smaller than the gradient spatial scale (~750–3750 km), causing both thickness methods to fail structurally.

### What P1 did not show

P1 did not show that the gradient is unreal, that the scaffold methods are wrong in principle, or that MMS data are unusable. It showed that the tetrahedron is not matched to the structure scale at this event.

---

## B. P1 root-cause tree

### 1. Event-level causes

| Factor | Strength of evidence | Assessment |
|---|---|---|
| Gradient is real | Strong (observed on 4 SC, |B|/density/beta transitions clear) | Not the failure point |
| Gradient is spatially extended (~1000 km) | Strong inference (temporal scale ~75 s × estimated V_n ~10–50 km/s) | Primary failure contributor |
| MVA normal poorly constrained (λ₂/λ₁ = 3.0) | Strong (direct eigenvalue measurement) | Consequence of extended, possibly non-planar structure |
| MVA normal geophysically inconsistent (70° off expected) | Strong | Corroborates that the structure is not a clean planar boundary crossing |

**Event-level verdict:** The event contains a real gradient but one that is spatially extended and possibly non-planar. This is plausible for a broad near-MP gradient layer under low Dp (1.1 nPa), where the sheath is wide.

### 2. Method-level causes

| Factor | Strength | Assessment |
|---|---|---|
| Timing method requires resolvable inter-SC time delays | Well-established (Haaland et al. 2004; Zhou et al. 2009) | Not the failure point; the method is sound |
| Gradient method requires separation ~ gradient scale | Well-established (De Keyser et al. 2007) | Not the failure point; the method is sound |
| Both methods fail when separation << gradient scale | Strong inference from P1 | The methods are correct but the configuration is wrong for this structure |

**Method-level verdict:** The methods are sound. They fail because the input configuration (10 km tetrahedron) is not matched to the output target (1000 km gradient).

### 3. Geometry / scale-match causes (THE DOMINANT ROOT CAUSE)

| Factor | Strength | Assessment |
|---|---|---|
| Phase 1 separation ~10 km | Measured | Fixed property of the MMS Phase 1 orbit configuration |
| Gradient scale ~750–3750 km | Estimated from temporal gradient + boundary speed range | The spatial scale of an extended near-MP gradient under typical conditions |
| Scale mismatch ~100× | Direct ratio | **Dominant blocker** |
| Phase 2 separation ~20–34 km | Measured in feasibility probe | Still ~40–100× smaller than gradient scale; **insufficient improvement** |

**Geometry-level verdict:** The scale mismatch is the dominant root cause. It is not specific to P1. Any extended near-MP gradient layer (~hundreds to thousands of km) will produce the same failure with MMS tetrahedra of 10–34 km.

### 4. Context-level causes

| Factor | Strength | Assessment |
|---|---|---|
| Boundary-adjacency was assessed mainly from Shue-model distance (0.4 Re) | Moderate | The model distance was close, but the focused analysis showed density never dropped below 5 cm⁻³ in the 2h window |
| Low Dp (1.1 nPa) produces wide sheath → extended gradient | Reasonable inference | Wide sheath under low Dp is consistent with the extended gradient observed |
| Readiness screening did not include a scale-match criterion | Correct | The scaffold and readiness audit did not require separation/scale compatibility |

**Context-level verdict:** The readiness basis was boundary-adjacency-focused without a scale-match gate. This allowed an event with real boundary adjacency but an unfavorable separation/scale ratio to pass all gates.

### 5. Branch-basis-level causes

| Factor | Strength | Assessment |
|---|---|---|
| Shortlist screened for gradient existence, not gradient sharpness | Correct | The screening criteria did not distinguish extended from sharp gradients |
| Readiness audit checked boundary adjacency, not scale-match feasibility | Correct | The readiness gates are necessary but not sufficient for thickness-reportability |
| The scaffold's eligibility gate (§D) requires "identifiable gradient interval" but not "separation-matched gradient" | Correct | A design gap in the scaffold |

**Basis-level verdict:** The current shortlist/readiness basis is incomplete. It admits events with real, boundary-adjacent gradients that are structurally not thickness-reportable under MMS tetrahedra.

---

## C. Five-direction comparison

### A. Direct MMS-P3 thickness attempt

| Dimension | Assessment |
|---|---|
| Strongest support | P3 passed readiness with boundary adjacency (with motion caveat); different upstream regime (Dp = 2.7 vs 1.1) |
| Hardest blocker | P3 has higher Dp, which means narrower sheath and potentially sharper gradients. But the P1 gradient was already ~1000 km at Dp = 1.1; at Dp = 2.7 the sheath is narrower but the gradient is still likely hundreds of km. The 10 km tetrahedron is still grossly undersized. |
| Risk of going in circles | **High.** Same Phase 1 separation. P3's boundary adjacency depended on boundary motion, adding uncertainty. The most likely outcome is another do_not_report for the same structural reason. |
| Information gain | Low. Would confirm the scale-mismatch pattern but add no new method capability. |
| Thesis value | Near zero if it also produces do_not_report. |
| **Verdict** | **Not recommended as primary.** |

### B. MMS shortlist / readiness basis reset

| Dimension | Assessment |
|---|---|
| Strongest support | The current basis is demonstrably incomplete (no scale-match gate). A revised basis could prevent future scale-mismatch failures. |
| Hardest blocker | Even with a revised basis, MMS Phase 1 (~10 km) and Phase 2 (~25 km) separations remain 40–100× smaller than typical extended near-MP gradients. The revised basis may screen out ALL broad-gradient events, leaving nothing. |
| Risk of going in circles | **Moderate.** A reset without a viable route is just a better-documented dead end. |
| Information gain | High for understanding the structural constraint. No thickness information. |
| Thesis value | The basis reset itself documents an important negative methodological result. |
| **Verdict** | **Useful as a documentation step, but only if paired with a viable next route.** |

### C. Method-only salvage without changing candidate basis

| Dimension | Assessment |
|---|---|
| Strongest support | None identified. Both methods (timing and gradient) require separation/scale compatibility that cannot be achieved by method tweaks. |
| Hardest blocker | The 100× scale mismatch is not a method-tuning problem. It is a physical configuration constraint. No software or analysis refinement can make a 10 km tetrahedron resolve a 1000 km gradient. |
| Risk of going in circles | **Very high.** |
| Information gain | None. |
| **Verdict** | **Not viable.** |

### D. Pause MMS branch

| Dimension | Assessment |
|---|---|
| Strongest support | Both Phase 1 and Phase 2 MMS separations (~10–34 km) appear structurally inadequate for extended near-MP gradient layers. No currently identified route resolves the scale mismatch without either (a) finding events with much sharper gradients (~10–100 km scale), or (b) using a fundamentally different measurement approach. |
| Hardest blocker | Pausing means no MMS thickness anchor in the thesis. |
| Risk of going in circles | Zero (no further action). |
| Information gain | The documented negative result is itself informative. |
| Thesis value | An honest negative result (scale mismatch documented) is citable. |
| **Verdict** | **Recommended as primary.** |

### E. P1 internal rescue / inner-sheet-like local sublayer follow-up

| Dimension | Assessment |
|---|---|
| Strongest support | None. The P1 data showed density never dropped below 5 cm⁻³ in the focused window, and the gradient is temporally broad (~5 min). There is no evidence of a thin, sharp sublayer that the 10 km tetrahedron could resolve. |
| Hardest blocker | No identifiable thin structure to rescue. |
| Risk of going in circles | High. |
| **Verdict** | **Not viable.** |

---

## D. Revised thickness-reportability basis

The current scaffold's eligibility gate (§D) requires: near-subsolar geometry, upstream steadiness, 4-SC completeness, tetrahedron quality, and identifiable gradient. **It does not require separation/scale compatibility.**

### Proposed addition (for any future MMS thickness work)

A sixth eligibility requirement:

**6. Separation–scale match.** The MMS tetrahedron separation must be within approximately one order of magnitude of the gradient's estimated spatial scale. If the temporal gradient timescale (Δt_feature) multiplied by a conservative boundary speed estimate (V_n ~ 10–100 km/s) gives a spatial scale >10× the tetrahedron separation, the event is thickness-ineligible under the current multi-spacecraft methods.

### What this revised basis means in practice

| Tetrahedron separation | Gradient scale required for thickness-eligibility |
|---|---|
| ~10 km (Phase 1) | ~10–100 km (very sharp, discontinuity-like) |
| ~25 km (Phase 2) | ~25–250 km (still quite sharp) |

Typical extended near-MP gradient layers are ~100–3000 km. This means:
- Phase 1 can only resolve discontinuity-like features (current sheets, sharp MP transitions), not broad gradient layers
- Phase 2 can potentially resolve moderately sharp features (~100 km), but not the extended gradients seen at P1

### Explicit distinction: boundary-adjacent vs thickness-reportable

| Category | Definition | P1 status |
|---|---|---|
| **Boundary-adjacent plausible** | Event shows density/|B|/beta transition consistent with near-MP location | P1: YES |
| **Thickness-reportable** | Boundary-adjacent AND gradient spatial scale is within ~10× of tetrahedron separation | P1: NO |

This distinction was missing from the original scaffold and is the central lesson of the P1 attempt.

---

## E. What P1 does and does not invalidate

| Claim | P1 invalidates? |
|---|---|
| The P1 event itself is unreal | **No.** The gradient is real and observed on all 4 SC. |
| The scaffold methods are wrong | **No.** The methods are standard and well-established. They fail here because the configuration doesn't match the structure. |
| All MMS Phase 1 events fail at thickness | **Overgeneralization, but close.** Any event with an extended gradient (~100+ km) will fail. Only discontinuity-like features (~10 km scale) could succeed. |
| All MMS Phase 2 events fail | **Not proven but likely for broad gradients.** The 25 km separation improves the match by only 2–3×. |
| The MMS thickness branch is permanently dead | **No, but it requires a fundamentally different target.** The branch would need either much larger separations (Cluster ~100–10,000 km) or events with much sharper features. |
| The current shortlist/readiness basis | **YES — invalidated.** The basis lacks a scale-match criterion and admits events that are boundary-adjacent but not thickness-reportable. |

**Summary:** P1 mainly invalidates the current basis (missing scale-match gate), not the methods or the existence of the gradient. The event-level failure is a consequence of the basis gap.

---

## F. Bounded feasibility probes

### Probe 1: MMS Phase 2 separation check

**Route:** Search for larger-separation MMS events in Phase 2 era (2019+).
**Access:** CDAWeb MMS1/MMS2 MEC position data.
**Finding:** Phase 2 separations are 20–34 km. This is only 2–3× larger than Phase 1 (~10 km). The gradient scale was ~750–3750 km. Even at 34 km, the scale mismatch remains ~40–100×.
**Conclusion:** Phase 2 **does not solve the scale-mismatch problem** for extended near-MP gradients. A Phase 2 shortlist would face the same structural barrier.

### Probe 2: Sharp/thin-layer search basis (not executed)

This probe was not executed because the scale-match analysis already shows that the required gradient scale (~10–100 km for Phase 1, ~25–250 km for Phase 2) corresponds to discontinuity-like or very sharp transition features, not broad gradient layers. Whether such sharp near-MP features exist and are thickness-eligible is a question that would require a fundamentally different candidate selection approach focused on thin current-sheet-like crossings rather than extended gradient layers. This is outside the current scaffold's intended target.

---

## G. Single recommended next move

### Primary recommendation: **Pause the MMS thickness branch**

**Reasons:**

1. The dominant failure mode (separation–scale mismatch) is not event-specific. It is a structural property of MMS inter-spacecraft separation (~10–34 km) versus typical near-MP gradient scales (~100–3000 km).

2. Phase 2 does not resolve the problem (2–3× improvement is insufficient against a 40–100× gap).

3. No method-level fix can bridge a ~100× scale mismatch.

4. The MMS thickness scaffold and methods are sound in principle. The failure is in the match between available constellation configuration and target structure scale.

5. The documented negative result (scale mismatch) is itself a legitimate thesis contribution: it demonstrates that MMS Phase 1/2 multi-spacecraft thickness methods are not applicable to extended near-MP gradient layers, and explicitly identifies the separation/scale criterion that any future attempt must satisfy.

### No fallback recommended

P3 would face the same barrier. Reserve MMS-R1 has the same Phase 1 separation. A Phase 2 shortlist would face a similar mismatch (25 km vs ~1000 km). None of these routes has a credible path to a defensible thickness estimate under the current knowledge.

### What "pause" means operationally

- No new shortlist, no new event packages, no new thickness attempts under the current basis.
- The MMS scaffold, shortlist, readiness audit, and P1 attempt remain as historical records.
- The P1 scale-mismatch result and the revised thickness-reportability basis are documented as methodological findings.
- Resumption would require either: (a) a Cluster-scale separation mission, (b) identified ultra-sharp near-MP features matching the ~10 km scale, or (c) a fundamentally different single-spacecraft or empirical thickness approach.

---

## H. Exact supportable statement and exact non-claim

### Supportable

The MMS-P1 first thickness attempt demonstrates that the scaffold's multi-spacecraft timing and gradient methods, while sound in principle, cannot produce defensible thickness estimates when the gradient spatial scale (~750–3750 km) exceeds the tetrahedron separation (~10 km) by approximately two orders of magnitude. This scale mismatch is a structural property of MMS Phase 1 dayside near-MP gradient encounters, extends to Phase 2 (where separation increases to only ~25 km), and invalidates the current shortlist/readiness basis, which lacked a separation–scale match criterion. The gradient structure observed at P1 is real, but the MMS configuration is not matched to measure its spatial extent.

### Not supportable

- Any MMS event-level thickness estimate
- That the gradient at P1 is unreal or scientifically uninteresting
- That MMS is useless for all magnetopause studies (it excels at thin-structure analysis where separation matches structure scale)
- Any connection between this result and the frozen THEMIS comparator branch
- Any physical identification of the P1 gradient as a specific structure
