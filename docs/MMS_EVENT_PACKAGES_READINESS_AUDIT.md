# MMS Event Package Readiness Audit

**Date:** 2026-03-28
**Stage:** Event-package / reportability analysis only. No thickness values produced.
**Scope:** 3 primary candidates (MMS-P1, P2, P3). Reserve untouched.

---

## 1. Why this round exists

The MMS shortlist identified 3 primary candidates from coarse screening. This round performs detailed event-level reportability analysis — boundary-adjacency checks, multi-spacecraft data verification, provisional interval logic, and normal/timing/gradient preflight — to determine which events, if any, earn a later first thickness attempt. No thickness is computed.

## 2. Why it is narrower than a thickness attempt

This round checks whether the event data are well-posed enough that thickness analysis could plausibly succeed. It does not execute that analysis. No boundary speeds, no L values, no σ_L values, and no quality grades are produced.

---

## 3. Three-event comparison matrix

| Dimension | MMS-P1 (2015-11-12) | MMS-P2 (2015-12-12) | MMS-P3 (2016-12-26) |
|---|---|---|---|
| **SZA** | 18° | 11° | 6° |
| **Dp** | 1.1 nPa | 2.1 nPa | 2.7 nPa |
| **MP standoff** | 11.0 Re | 10.0 Re | 9.8 Re |
| **Dist to MP** | **0.4 Re** | 1.8 Re | 2.1 Re |
| **FGM 4-SC** | 4/4 | 4/4 | 4/4 |
| **FPI 4-SC** | 4/4 | 4/4 | 4/4 |
| **Beta transition** | Yes | Yes | Yes |
| **Density transition** | Yes (0.1–21.8) | **No** (1.6–29.4) | Yes (0.5–39.1) |
| **Bz range** | 75 nT | 111 nT | 119 nT |
| **Boundary-adjacent** | **Plausible** | Not plausible | Plausible (with boundary-motion caveat) |
| **Pairing clarity** | Promising | Ambiguous | Promising |
| **Normal preflight** | Feasible | Uncertain | Feasible |
| **Timing preflight** | Feasible | Uncertain | Feasible |
| **Gradient preflight** | Feasible | Uncertain | Feasible |
| **Main blocker** | None identified | 1.8 Re from MP, no density transition | Nominal 2.1 Re from MP; requires boundary motion for adjacency |
| **Verdict** | **ADVANCE** | **HOLD** | **ADVANCE** |

---

## 4. Per-event summaries

### MMS-P1: 2015-11-12 — ADVANCE

**Boundary adjacency:** The spacecraft at X = 11.4 Re is only 0.4 Re from the Shue-model MP standoff (11.0 Re at Dp = 1.1 nPa). The data show a clear density transition from magnetosheath levels (~20 cm⁻³) to near-zero (0.1 cm⁻³), a large B-field rotation (Bz range 75 nT), and a beta transition from >2 to <0.3. This is the strongest boundary-adjacency signal among the three primaries.

**Provisional interval:** A magnetopause-crossing interval is identifiable in the MMS1 data with density drop + B-field rotation + beta transition. Start/end candidates exist at the density gradient onset and the B-field rotation completion.

**Preflight:** Normal estimation appears feasible (large coherent B-field rotation should support MVA). Timing should be feasible across 4 spacecraft given the clear crossing signature. Gradient computation is data-adequate (4-SC FPI coverage spans the gradient).

**Analyst note:** This is the event with the smallest distance to the modeled MP and the clearest boundary-crossing signature. The low Dp (1.1 nPa) means a wider sheath, which could make the gradient more extended — this is a potential advantage for thickness estimation. Recommended for a first thickness attempt.

### MMS-P2: 2015-12-12 — HOLD

**Boundary adjacency:** The spacecraft at X = 11.8 Re is 1.8 Re from the MP standoff (10.0 Re at Dp = 2.1 nPa). The density minimum is 1.6 cm⁻³ — still in the sheath regime, not reaching magnetospheric levels. While there is a large Bz range (111 nT) suggesting B-field structure, and beta transitions exist, the absence of a clear density transition to sub-1 cm⁻³ values means the spacecraft may not have actually crossed the magnetopause during this window.

**Main concern:** Without a clear MP crossing, the density gradient observed may be mid-sheath fluctuation structure rather than a boundary-adjacent gradient. Feature-pairing for thickness would be ambiguous because there is no clear inner (magnetopause-side) boundary.

**Analyst note:** Data quality is excellent (4/4 on both FGM and FPI). If future analysis shows that the MP was reached during a brief boundary-motion excursion not visible at this screening level, the event could be reconsidered. For now, it does not meet the boundary-adjacency plausibility requirement.

### MMS-P3: 2016-12-26 — ADVANCE

**Boundary adjacency:** The spacecraft at X = 11.9 Re is nominally 2.1 Re from the MP standoff (9.8 Re at Dp = 2.7 nPa). However, the data show density dropping to 0.5 cm⁻³ (near-magnetospheric), a very large B-field rotation (Bz range 119 nT), and clear beta transition. These signatures indicate that the magnetopause moved outward past the spacecraft at least once during the window, likely during a dynamic-pressure pulse or boundary oscillation. The boundary adjacency is plausible but depends on boundary motion rather than steady proximity.

**Provisional interval:** The strongest B-field rotation + density transition interval provides start/end candidates. The boundary-motion dependence adds feature-picking uncertainty.

**Preflight:** Normal estimation feasible (strong B rotation). Timing feasible (clear crossing signature). Gradient computation data-adequate. The main additional uncertainty is that the gradient may be sampled during a transient boundary excursion rather than a quasi-static configuration.

**Analyst note:** Best geometry (SZA = 6°) and highest Dp among primaries. The boundary-motion dependence adds caveat but does not prevent a thickness attempt — it adds to the uncertainty budget. Recommended for a first thickness attempt with the boundary-motion caveat explicitly carried.

---

## 5. Exact strongest supportable statement

Two of three primary MMS candidates (MMS-P1 and MMS-P3) show full four-spacecraft data completeness, boundary-adjacency plausibility, and sufficient gradient/crossing structure to warrant a first thickness attempt under the methods scaffold. One candidate (MMS-P2) is held because boundary adjacency is not plausible at this screening level. No thickness values, no quality grades, and no physical identifications are produced in this round.

## 6. Exact strongest non-claim

These event-package assessments do not constitute thickness results, do not identify physical layer structure, and do not connect to the frozen THEMIS comparator branch. Boundary-adjacency plausibility at screening level does not guarantee that a thickness estimate will succeed or be defensible.

## 7. Next red-level decision

At least one event received ADVANCE (two did). The user is asked:

**Authorize a first thickness attempt on MMS-P1 and MMS-P3 only?**

This would involve detailed multi-spacecraft interval analysis, start/end feature pairing, normal estimation with cross-checks, timing-based and gradient-scale thickness computations, uncertainty budgets, and quality grading — all per the existing MMS scaffold.

Reserve candidate MMS-R1 remains untouched. MMS-P2 remains on hold.
