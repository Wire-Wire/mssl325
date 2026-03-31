# MMS-P1 First Thickness Attempt

**Date:** 2026-03-28
**Event:** MMS-P1, 2015-11-12
**Stage:** Single-event first thickness attempt. P1 only. Methods-first, honest about failure.
**Authority:** User-authorized narrowed scope (P1 only, not P1+P3 bundle).

---

## A. Why this round exists

This is a one-event, methods-first first thickness attempt on MMS-P1 only. P3 is explicitly out of scope for this round because the user authorization was narrowed from the earlier bundled P1+P3 question to a sequential single-event approach. P1 was chosen as the first pilot because the readiness audit identified it as the event with the smallest nominal distance to the modeled magnetopause (0.4 Re) and the clearest boundary-crossing signature at screening level.

---

## B. Event context

| Field | Value |
|---|---|
| Date | 2015-11-12, focus window 07:30–09:30 UT |
| Mean position | X ≈ 11.4 Re, SZA ≈ 18° |
| Upstream (OMNI) | Dp ≈ 1.1 nPa, Bz ≈ −1.7 nT (steady, CV = 0.11) |
| FGM | 4/4 spacecraft, survey L2, ~115,000 pts each over 2h window |
| FPI | MMS1: ~1,600 points (fast L2 DIS), density 5.3–18.3 cm⁻³ |
| Shue-model MP | 11.0 Re (at Dp = 1.1, Bz = −1.7) |
| Nominal dist to MP | 0.4 Re |

**Note on density range:** The readiness screening reported 0.1–21.8 cm⁻³ over a broader ±2h window. The focused 07:30–09:30 UT window shows 5.3–18.3 cm⁻³ — the sub-1 cm⁻³ density from screening was outside this window and may represent a brief magnetospheric encounter at a different time. Within this focused window, the spacecraft remained in sheath-like density throughout.

---

## C. Final pairing decision

### Primary pairing

The main B-field transition occurs at approximately 08:57 UT (26 min into the window). |B| drops from ~34 nT to ~6 nT over approximately 4 minutes, with Bz rotating from −19 to +1 nT. This is paired with a simultaneous density gradient: density drops from ~15 cm⁻³ to ~5 cm⁻³ over the same interval.

**Selected start:** Onset of |B| decrease + density decrease at approximately 08:53 UT.
**Selected end:** B-field rotation completion + density minimum at approximately 08:58 UT.
**Gradient interval duration:** ~5 minutes (~300 s).

### Alternate pairing

An alternate, wider pairing uses the full beta transition as the defining feature: from β > 1 (sheath) to β < 1 (transition region). This gives approximately 08:50–09:02 UT (~12 min). The alternate pairing captures a broader transition but includes more of the ambient sheath.

### Why the primary is operationally preferred

The primary pairing corresponds to the steepest gradient and the most coherent cross-spacecraft signature. The alternate is wider and more ambiguous. **Neither pairing is presented as physically unique.**

---

## D. Normal hierarchy and interval dependence

### MVA normal (MMS1, gradient interval)

Minimum variance analysis on B-field vectors within the 4-minute gradient interval yields:

- Eigenvalues: λ₁ = 5.2, λ₂ = 15.6, λ₃ = 48.1
- **λ₂/λ₁ = 3.0** — well below the commonly used threshold of ~10 for a reliable MVA normal
- MVA normal (GSM): [0.32, 0.37, −0.87]

**Assessment:** The MVA normal points predominantly in the −Z direction, which is ~70° from the expected sunward magnetopause normal at this near-subsolar position (X = 11.4 Re, SZA = 18°). The low eigenvalue ratio indicates the minimum-variance direction is poorly constrained. **This is a serious failure of the MVA path.**

### Expected geophysical normal

For a near-subsolar position at X ≈ 11.4 Re, the magnetopause normal should point approximately along +X (sunward), perhaps with modest Y/Z components from the local curvature. The MVA result is grossly inconsistent with this expectation.

### Timing normal (4-SC)

The 4-spacecraft timing analysis found that MMS2, MMS3, and MMS4 all see the main transition at nearly identical time delays (~1118 s after MMS1). This means the three trailing spacecraft cannot distinguish a propagation direction — the ~10 km inter-spacecraft separation is far smaller than the time delay × any plausible boundary speed, producing an effectively degenerate timing geometry.

**Assessment:** The ~10 km MMS Phase 1 tetrahedron is too small relative to the structure scale to resolve a meaningful timing normal for this event. **The timing normal path fails.**

### Cross-check summary

| Method | Result | Status |
|---|---|---|
| MVA | Normal ~70° from expected direction, λ₂/λ₁ = 3.0 | **FAIL** — poorly constrained, geophysically inconsistent |
| Timing (4-SC) | Degenerate — separation too small for this crossing timescale | **FAIL** — cannot resolve propagation direction |
| Expected geophysical | ~[1, 0, 0] GSM at near-subsolar | Context only, not an independent estimate |

**No two independent normal estimates agree.** The scaffold requirement (§F) states that if no two methods agree within 30°, the event receives a geometry penalty and may be downgraded to "do not report thickness." Both independent paths fail here.

---

## E. Timing-based thickness attempt

### Method

The timing-based thickness requires a normal direction and a boundary speed. Neither is defensibly available:
- The MVA normal is geophysically inconsistent and poorly constrained.
- The timing normal is degenerate (4-SC separation too small).
- Without a defensible normal, no boundary speed can be computed.

### Result

**Lt is NOT defensible.** The timing-based thickness path fails because no reliable normal direction can be established from the available methods for this event. The ~10 km MMS Phase 1 tetrahedron is not matched to the scale of this crossing.

---

## F. Gradient-scale thickness attempt

### Method

The gradient-scale thickness requires computing the spatial density gradient ∇n from four-spacecraft measurements and deriving a scale length λ = n / |∇n|.

### Assessment

For the four-spacecraft gradient method (De Keyser et al. 2007) to produce a meaningful gradient, the inter-spacecraft separation must be comparable to the gradient scale length. The temporal gradient analysis shows a density gradient timescale of ~75 s. At a typical boundary speed of ~10–50 km/s, this corresponds to a spatial scale of ~750–3750 km. The MMS Phase 1 separation is ~10 km — **two orders of magnitude smaller** than the gradient scale.

At ~10 km separation, all four spacecraft see essentially the same density at any given time. The four-spacecraft gradient would measure only the tiny inter-spacecraft density difference, which is dominated by measurement noise at this scale, not by the large-scale boundary gradient.

### Result

**Lg is NOT defensible.** The gradient-scale thickness path fails because the MMS Phase 1 inter-spacecraft separation (~10 km) is far too small compared to the spatial scale of the density gradient (~1000 km or more) for this event. The four-spacecraft gradient method is not matched to this structure scale.

---

## G. Ambiguity and uncertainty ledger

| Component | Status | Assessment |
|---|---|---|
| Feature-picking ambiguity | Low-moderate | Primary and alternate pairings identified; gradient is clear but ~5 min wide |
| Alternate pairing sensitivity | Not computed | Cannot propagate to thickness without a normal |
| Normal-direction uncertainty | **CRITICAL FAILURE** | MVA poorly constrained (λ₂/λ₁ = 3.0, 70° from expected); timing degenerate |
| Timing uncertainty | **CRITICAL FAILURE** | 4-SC separation (~10 km) too small to resolve crossing timing |
| Tetrahedron / geometry penalty | **DOMINANT BLOCKER** | Phase 1 ~10 km separation not matched to ~1000 km structure scale |
| Gradient conditioning | **CRITICAL FAILURE** | Separation/scale mismatch (~10 km vs ~1000 km) |
| Model-context uncertainty | Moderate | Shue-model MP distance provides only coarse context |
| Method disagreement | N/A | Both methods fail; disagreement cannot be assessed |

---

## H. Representative event thickness decision

Applying the scaffold decision rule:

**Both timing and gradient paths fail.** Neither produces a defensible thickness estimate. The failure is structural: the MMS Phase 1 tetrahedron (~10 km separation) is not matched to the spatial scale of the boundary-adjacent gradient structure observed at this event. This is not a data-quality failure — it is a scale-mismatch failure.

**Final outcome: do_not_report.**

No single representative event-level thickness estimate is justified.

---

## I. Final event outcome

**Outcome: do_not_report**

### Exact blocker

The MMS Phase 1 inter-spacecraft separation (~10 km) is approximately two orders of magnitude smaller than the spatial scale of the density/magnetic gradient observed at this near-MP crossing. This scale mismatch prevents both timing-based and gradient-scale thickness definitions from producing defensible results:
- Timing: the 4-SC can't resolve the crossing propagation direction at this scale.
- Gradient: all 4 SC see the same field/density at any instant; the gradient is noise-dominated.

### What was still learned

1. The event shows a clear near-MP gradient structure (|B| drops ~28 nT, density drops ~10 cm⁻³ over ~5 min).
2. The structure is spatially extended (estimated ~750–3750 km) — much larger than the tetrahedron.
3. This scale mismatch is a structural property of MMS Phase 1 dayside operations, not a special feature of this event. Any near-MP gradient layer of comparable scale would encounter the same problem.
4. MMS Phase 2 (larger separations) or a different event with much shorter-scale structure would be needed to make these methods viable.

---

## J. Exact supportable statement and exact non-claim

### Supportable

MMS-P1 (2015-11-12) shows a clear near-magnetopause gradient structure observable on all four spacecraft, with |B| decreasing by ~28 nT and density by ~10 cm⁻³ over ~5 minutes. However, the MMS Phase 1 inter-spacecraft separation (~10 km) is not matched to the spatial scale of this structure (~1000 km or more), preventing both timing-based and gradient-scale thickness methods from producing defensible results. This is a structural scale mismatch, not a data-quality failure.

### Not supportable

- Any event-level thickness estimate for MMS-P1
- Any quality grade for this event
- Any physical identification of the observed gradient as a specific structure
- Any connection between this result and the frozen THEMIS comparator branch
- Any claim that MMS Phase 1 dayside operations can resolve near-MP gradient thickness at this spatial scale

---

## K. Implications for the MMS branch

The scale mismatch identified here is not P1-specific. It is a general property of MMS Phase 1 (~10 km separation) dayside magnetopause encounters where the gradient structure is spatially extended (hundreds to thousands of km). This means:

1. **MMS-P3 (2016-12-26) will face the same tetrahedron-scale limitation** unless the observed gradient at that event happens to be much sharper (sub-100 km scale), which cannot be determined without attempting the analysis.
2. **MMS Phase 2 operations** (larger separations, starting ~2018) would be more appropriate for gradient-layer thickness measurement, but require a separate data search not authorized in this round.
3. The scaffold's thickness method design (§G–H) is sound in principle; the failure is in the match between available spacecraft configuration and observed structure scale.
