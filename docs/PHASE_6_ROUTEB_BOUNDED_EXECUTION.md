# Phase 6 Route 3B — Bounded Execution Results

**Date:** 2026-03-30
**Authority:** User-authorized bounded Route B execution on the clean Route A universe.
**Scope:** Compute Δn_near and Δ|B|_near auxiliary descriptors on all Route-B-computable encounters. No thresholds, labels, classes, or detector semantics. No new archive search.

---

## 1. What was done

Loaded cached THEMIS FGM/MOM/STATE data for all 12 encounters in the Phase 6 universe (9 clean tranche-1 + 3 tranche-2 low-cone). Recomputed s-mapping from raw position data using Shue 1998 / Merka 2005 with encounter-averaged OMNI upstream. Computed per-bin medians for the very-near [0.0, 0.2] and near [0.2, 0.4] s-bins. Applied Route B auxiliary descriptors to all Route-B-computable encounters (5 of 12).

---

## 2. Descriptor definitions (unchanged from design)

| Descriptor | Definition | Semantic meaning |
|---|---|---|
| Δn_near | median(density in s=[0.0, 0.2]) / median(density in s=[0.2, 0.4]) | Inner-sheath density gradient: <1 means density drops toward MP |
| Δ\|B\|_near | median(\|B\| in s=[0.0, 0.2]) / median(\|B\| in s=[0.2, 0.4]) | Inner-sheath field gradient: >1 means \|B\| rises toward MP |

**These are NOT Dn / EB.** They compare adjacent inner-sheath bins, not near-vs-background. They are explicitly Phase-6-reset-only semantics.

---

## 3. Route B ledger — computable encounters (N=5)

| Encounter | Cone | Dp | Δn_near | Δ\|B\|_near | n_vn | n_near | b_vn | b_near | QC |
|---|---|---|---|---|---|---|---|---|---|
| usable_aug18_6h | 30.7° | 4.25 | **0.756** | **1.028** | 1.59 | 2.10 | 50.05 | 48.70 | clean |
| usable_sep03_5h | 56.2° | 3.69 | **0.977** | **1.283** | 43.75 | 44.76 | 53.97 | 42.08 | clean |
| usable_sep26_09_10h | 84.6° | 3.05 | **0.028** | **2.055** | 1.73 | 62.61 | 59.01 | 28.72 | clean |
| usable_sep27_09_10h | 56.6° | 3.12 | **0.982** | **0.939** | 85.23 | 86.79 | 14.51 | 15.46 | mixed |
| t2_20080904_thd | 43.3° | 2.56 | **1.053** | **1.071** | 16.85 | 16.01 | 21.41 | 19.99 | mixed |

Units: density in cm⁻³, |B| in nT. QC refers to transition_cleanliness_qc.

---

## 4. Route B ledger — non-computable encounters (N=7)

| Encounter | Cone | Reason | VN occ |
|---|---|---|---|
| cand4a_sep19_08_the | 64.2° | vn_occ = 0.0% | 0.0% |
| usable_sep13_09_6h | 61.2° | vn_occ = 0.2% (below 1% threshold) | 0.2% |
| usable_sep20_09_6h | 70.0° | vn_occ = 0.0% | 0.0% |
| usable_oct24_09_6h | 86.4° | vn_occ = 0.0% | 0.0% |
| cand4a_oct23_10_thd | 35.0° | vn_occ = 0.0% | 0.0% |
| t2_20090928_thd | 42.9° | vn_occ = 0.0% + no upstream params | 0.0% |
| t2_20090928_the | 43.6° | vn_occ = 0.0% + no upstream params | 0.0% |

---

## 5. QC audit fields

| Encounter | transition_cleanliness | disturbance | omni_context | boundary_uncertainty |
|---|---|---|---|---|
| usable_aug18_6h | clean | undisturbed | good | plausible |
| usable_sep03_5h | clean | undisturbed | good | plausible |
| usable_sep26_09_10h | clean | undisturbed | good | plausible |
| usable_sep27_09_10h | mixed | undisturbed | good | plausible |
| t2_20080904_thd | mixed | undisturbed | good | plausible |

---

## 6. Coherence assessment (4 bounded questions)

### Q1: Does Δn_near < 1 co-occur with Δ|B|_near > 1?

This is the classical PDL signature in the inner sheath: density depletes while magnetic field piles up.

**Result: 3 of 5 encounters show this pattern.**

- **aug18_6h**: Δn=0.756, Δ|B|=1.028 — YES, clean PDL-consistent gradient
- **sep03_5h**: Δn=0.977, Δ|B|=1.283 — YES, marginal density drop but clear |B| rise
- **sep26_09_10h**: Δn=0.028, Δ|B|=2.055 — YES, strongest signal (density drops 97%, |B| doubles)
- **sep27_09_10h**: Δn=0.982, Δ|B|=0.939 — NO, flat in both quantities
- **t2_20080904_thd**: Δn=1.053, Δ|B|=1.071 — NO, slight rises in both (no depletion)

### Q2: Is the recovered low-cone encounter within the tranche-1 range?

t2_20080904_thd (cone=43.3°, the only recovered low-cone encounter):
- Δn_near = 1.053 — OUTSIDE tranche-1 range [0.028, 0.982]
- Δ|B|_near = 1.071 — WITHIN tranche-1 range [0.939, 2.055]

The recovered encounter does NOT show a density depletion signature through this descriptor. Both density and |B| are essentially flat across the inner sheath. This is a descriptive observation, not a classification.

### Q3: Cross-check — are Dn and Δn_near directionally consistent?

For encounters where both the original Dn (near/bg) and Route B Δn_near (vn/near) are computable:

| Encounter | Dn | Δn_near | Consistent? |
|---|---|---|---|
| usable_aug18_6h | 0.113 | 0.756 | YES — both < 1 (depletion in both gradient scales) |
| usable_sep03_5h | 2.872 | 0.977 | NO — Dn > 1 (enhancement vs bg), Δn < 1 (depletion in inner sheath) |
| usable_sep26_09_10h | 0.932 | 0.028 | YES — both < 1 |
| usable_sep27_09_10h | 1.310 | 0.982 | NO — Dn > 1, Δn < 1 (marginal) |

**2/4 consistent, 2/4 divergent.** The divergence is expected: Dn and Δn_near measure different gradients. Dn compares near-MP to background; Δn_near compares very-near to near within the inner sheath only. An encounter can show density enhancement vs background (Dn > 1) while still showing a depletion gradient within the inner sheath (Δn < 1) — this is physically plausible for a sheath where density peaks in the near bin and drops very close to the MP.

### Q4: Very-near residence time

Of the 5 computable encounters, very-near occupancy ranges from 4.5% (t2_20080904_thd) to 33.5% (sep03_5h). The recovered low-cone encounter has the lowest occupancy, consistent with its borderline computability.

---

## 7. Exact strongest supportable statement

Route B's auxiliary descriptor (Δn_near, Δ|B|_near) was computed on 5 of 12 encounters in the Phase 6 universe, including 1 recovered low-cone encounter (t2_20080904_thd, cone=43°). Three of 5 encounters show a density-depletion / field-enhancement gradient within the inner sheath (Δn < 1 and Δ|B| > 1), consistent with a PDL-like signature at the very-near-to-near scale. The strongest signal is in usable_sep26_09_10h (perpendicular geometry, Dp=3.05 nPa). The recovered low-cone encounter does not show this pattern; both descriptors are near unity, indicating a flat inner-sheath profile.

---

## 8. Exact non-claims

- No threshold was applied. No encounter was classified.
- No detector semantics were introduced.
- The 3/5 consistency rate is a descriptive observation, not a statistical test.
- Δn_near / Δ|B|_near are NOT Dn / EB. Cross-comparison is informative but not substitutive.
- The recovered low-cone encounter contributes one data point. Its flat descriptor values do not support or refute the PDL hypothesis at this cone angle — the sample is too small.
- Phase 4B frozen claims are not altered, strengthened, or weakened.
- No labels (PDL / non-PDL) are assigned. No prior language is introduced.

---

## 9. Semantic cost of Route B (as designed)

The Route B descriptor is not comparable to the frozen Phase 4B Dn/EB basis:
- It measures a different gradient (very-near vs near, not near vs background)
- It is sensitive to the very-near bin, which has the lowest occupancy and highest position uncertainty
- The 2/4 cross-check divergence (Q3) confirms that the descriptors capture different physics
- The strongest PDL signature (sep26_09_10h, Δn=0.028) comes from an encounter where the near bin density is ~63 cm⁻³ but very-near is ~1.7 cm⁻³ — a factor of 36× difference that suggests the spacecraft may be sampling the magnetopause boundary layer in the very-near bin, not just the depleted magnetosheath

---

## 10. Decision trigger

Route B is now executed. The bounded analysis is complete. The next decision is:

**Does the user wish to (a) close Phase 6 Route B here and return to the main Phase 6 decision tree, or (b) proceed with any Route C exploration?**

Given that:
- Route B recovered 1 low-cone encounter, but it shows no inner-sheath depletion gradient
- 3/5 encounters show PDL-consistent inner-sheath gradients, but these are all also evaluable under the original Dn/EB basis
- The very-near bin is small and may contaminate with boundary-layer plasma

…the descriptive value of Route B is modest. It confirms that inner-sheath gradients exist in some encounters but does not provide new regime coverage.

---

## 11. Files produced

- `scripts/phase6_route3b_bounded_execution.py` — execution script
- `reports/themis_conditioning/route3b_ledger.json` — full ledger with coherence assessment
- `reports/themis_conditioning/route3b_ledger.csv` — tabular ledger
- `docs/PHASE_6_ROUTEB_BOUNDED_EXECUTION.md` — this document

## 12. Frozen anchors unchanged

Phase 4B, 5A/5B, and MMS branch remain frozen. No frozen claims altered.
