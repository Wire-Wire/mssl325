# MMS-P1 First Thickness Attempt — Report

**Outcome: do_not_report**

---

## Event: MMS-P1, 2015-11-12

| Field | Value |
|---|---|
| Position | X = 11.4 Re, SZA = 18° |
| Upstream | Dp = 1.1 nPa, Bz = −1.7 nT |
| FGM/FPI | 4/4 spacecraft FGM, MMS1 FPI |
| Tetrahedron | ~10 km (Phase 1) |

---

## Method results

| Method | Status | Blocker |
|---|---|---|
| MVA normal | **FAIL** | λ₂/λ₁ = 3.0; normal 70° from expected; poorly constrained |
| Timing normal | **FAIL** | 4-SC separation degenerate at this crossing timescale |
| Timing thickness (Lt) | **Not defensible** | No reliable normal direction |
| Gradient thickness (Lg) | **Not defensible** | Separation (~10 km) << gradient scale (~1000 km) |

---

## Dominant blocker

MMS Phase 1 inter-spacecraft separation (~10 km) is approximately two orders of magnitude smaller than the observed near-MP gradient spatial scale (~750–3750 km). This structural scale mismatch prevents both thickness definitions from producing defensible results.

---

## What was learned

A clear near-MP gradient exists (|B| drops ~28 nT, density drops ~10 cm⁻³ over ~5 min), but it is too spatially extended for the Phase 1 tetrahedron to resolve. This is a general Phase 1 limitation, not P1-specific.

---

Full analysis: `docs/MMS_P1_FIRST_THICKNESS_ATTEMPT.md`
Evidence panel: `figures/p1_evidence_panel.png`
