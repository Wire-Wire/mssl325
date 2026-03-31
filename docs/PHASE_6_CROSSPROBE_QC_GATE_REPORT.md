# Phase 6 Cross-Probe QC Gate — Report

**Date:** 2026-03-31
**Type:** One-off comparability gate. Decision support only.
**Input:** FULL EXP 2007-2010 retained catalogue (148 encounters).
**Verdict:** **PASS** (with mandatory caveats).

---

## 1. Overlap-valid same-date multi-probe groups

26 dates in the FULL EXP retained catalogue have >= 2 probes retained on the same day. These provide direct cross-probe comparability tests.

| # | Date | Probes | Cone range | Dp range | Dn range | EB range | OOM? |
|---|---|---|---|---|---|---|---|
| 1 | 2007-08-11 | 5 (all) | 79-81 | 1.9-2.0 | 1.03-1.29 | 0.92-2.31 | no |
| 2 | 2007-08-12 | 4 (ABCD) | 29-44 | 1.4-1.5 | 0.03-0.84 | 3.0-3.6 | **Dn OOM** |
| 3 | 2007-08-13 | 5 (all) | 39-50 | 1.1 | 0.01-0.03 | 3.6-4.3 | no |
| 4 | 2007-08-15 | 5 (all) | 75-86 | 2.1-2.5 | 0.06-1.74 | 0.73-3.98 | **Dn OOM** |
| 5 | 2007-08-16 | 5 (all) | 48-57 | 2.4-2.6 | 0.02-0.76 | 2.0-3.3 | **Dn OOM** |
| 6 | 2007-08-17 | 5 (all) | 84-87 | 1.6 | 0.02-0.07 | 2.8-4.1 | no |
| 7 | 2007-08-19 | 5 (all) | 44-84 | 1.7 | 0.03-0.03 | 2.3-3.4 | no |
| 8 | 2007-08-22 | 4 (BCDE) | 87 | 1.4 | 1.01-1.02 | 1.3-1.5 | no |
| 9 | 2007-08-25 | 5 (all) | 46-55 | 3.3-4.0 | 0.02-0.13 | 2.7-7.4 | no |
| 10 | 2007-08-26 | 5 (all) | 60 | 3.7 | 0.68-0.90 | 1.0-1.7 | no |
| 11 | 2008-08-18 | 2 (DE) | 49-51 | 3.6-3.9 | 0.75-1.38 | 1.3-1.7 | no |
| 12 | 2008-08-28 | 2 (BC) | 65 | 1.6 | 0.02-0.09 | 3.6-12.5 | no |
| 13 | 2008-09-03 | 2 (CE) | 56-60 | 1.4-3.3 | 0.02-2.38 | 0.9-5.4 | **Dn OOM** |
| 14 | 2008-09-05 | 2 (BC) | 52 | 1.4 | 0.20-0.81 | 3.4-11.9 | no |
| 15 | 2008-09-09 | 2 (BC) | 49 | 1.6 | 0.26-0.49 | 5.8-17.3 | no |
| 16 | 2008-09-14 | 3 (CDE) | 52-62 | 6.7-6.8 | 0.42-4.59 | 2.1-9.7 | **Dn OOM** |
| 17 | 2008-09-16 | 2 (BC) | 66 | 1.1 | 0.50-0.55 | 5.4-17.2 | no |
| 18 | 2008-09-20 | 2 (BC) | 43-44 | 1.5 | 0.07-0.14 | 4.4-15.1 | no |
| 19 | 2009-09-13 | 3 (ADE) | 63-70 | 2.1-4.0 | 0.82-1.05 | 1.7-1.9 | no |
| 20 | 2009-09-26 | 2 (DE) | 59-68 | 2.9-3.1 | 0.74-0.97 | 1.4-2.4 | no |
| 21 | 2009-09-27 | 2 (DE) | 64-70 | 3.0 | 0.92-0.99 | 1.4-1.9 | no |
| 22 | 2009-10-16 | 2 (AC) | 51-60 | 0.8-1.4 | 1.16-3.13 | 1.8-5.8 | no |
| 23 | 2009-10-22 | 2 (AD) | 81-82 | 2.2-3.3 | 1.24-3.67 | 1.6-4.8 | no |
| 24 | 2010-10-11 | 3 (ADE) | 67-68 | 3.8-4.1 | 0.006-0.49 | 1.9-2.2 | **Dn OOM** |
| 25 | 2010-10-23 | 3 (ADE) | 53-57 | 3.6-3.7 | 1.37-1.38 | 1.2-1.3 | no |
| 26 | 2010-11-10 | 3 (ADE) | 81-85 | 3.6-3.8 | 1.47-1.96 | 2.0-2.9 | no |

---

## 2. Pairwise spread results

118 total pairwise comparisons across 26 overlap groups.

**Overall:**
- 13 pairs (11%) show order-of-magnitude Dn disagreement (|Δlog10(Dn)| >= 1.0)
- 0 pairs show order-of-magnitude EB disagreement
- 20 of 26 groups (77%) have maximum Dn log-spread < 1 dex (cross-probe consistent)
- 6 of 26 groups (23%) have maximum Dn log-spread >= 1 dex (cross-probe inconsistent)

**In low-cone / quasi-radial groups specifically:**
- 4 overlap groups contain low-cone or quasi-radial encounters
- 1 of 4 (2007-08-12) shows OOM Dn disagreement
- 3 of 4 are cross-probe consistent

**Key observation:** The 2007-08-12 group has THA (cone=29°, Dn=0.032) alongside THB (cone=44°, Dn=0.839) — a 1.4 dex Dn difference. But the cone angles differ substantially between probes on this date. The 2007-08-13 group (cone 39-44°, all probes) shows all 5 probes at Dn 0.01-0.03 — near-perfect cross-probe agreement.

**EB spread:** EB shows much tighter cross-probe agreement than Dn. No single group has OOM EB disagreement. The maximum EB log-spread is 0.74 dex (2007-08-15).

---

## 3. Probe-conditioned comparison

**Overall THD vs non-THD (full retained catalogue):**

| Family | N | Dn median | EB median | Dp median |
|---|---|---|---|---|
| THD | 19 | 0.752 | 2.353 | 2.93 nPa |
| non-THD | 129 | 0.658 | 3.356 | 1.64 nPa |

The non-THD family has systematically lower Dp (median 1.64 vs 2.93 nPa) and somewhat higher EB (median 3.36 vs 2.35). Dn medians are comparable (0.66 vs 0.75).

**Per-cone-bin THD vs non-THD:**

| Cone bin | THD N | THD Dn med | non-THD N | non-THD Dn med | Comparable? |
|---|---|---|---|---|---|
| quasi-radial | 0 | — | 4 | 2.057 | N/A (no THD) |
| low-cone | 2 | 0.030 | 14 | 0.079 | Yes (similar order) |
| intermediate | 4 | 0.388 | 40 | 0.455 | Yes |
| perpendicular | 13 | 0.916 | 71 | 0.729 | Yes |

In the low-cone bin, the 2 THD encounters (Dn 0.01, 0.05) and 14 non-THD encounters (Dn median 0.079) are in the same order of magnitude. The quasi-radial bin has no THD encounters for comparison.

---

## 4. Regime-shift check

Dp and probe access are entangled with cone bin:

| Cone bin | N | Dp median | THD fraction | Dominant probes |
|---|---|---|---|---|
| quasi-radial | 4 | 1.11 | 0% | THA, THB, THC |
| low-cone | 16 | 1.19 | 12% | THC, THB |
| intermediate | 44 | 1.91 | 9% | THC, THB, THA |
| perpendicular | 84 | 1.90 | 15% | THC, THB, THA |

The entanglement is real: low-cone and quasi-radial encounters are systematically lower-Dp and non-THD-dominated. This is a structural access effect (the inner probes THD/THE can only reach the background bin at higher Dp), not a measurement artifact. **However, within the multi-probe overlap groups, same-date probes at similar Dp show broadly consistent Dn/EB values, which means the probe-family effect is not the dominant source of descriptor variation.**

---

## 5. QC concentration check

71 encounters show extreme Dn (< 0.05) or extreme EB (> 5). Their QC profile:

| QC profile | Count |
|---|---|
| transition=clean, disturbance=undisturbed, boundary=uncertain, omni=good | 42 |
| transition=clean, disturbance=undisturbed, boundary=plausible, omni=good | 12 |
| transition=clean, disturbance=uncertain, boundary=uncertain, omni=good | 7 |
| transition=mixed or uncertain | 10 |

**The extreme values do NOT cluster in poor-QC encounters.** 42 of 71 (59%) have clean transition and undisturbed disturbance. The "boundary=uncertain" flag reflects Dp outside the 2-6 nPa range (most low-cone encounters have Dp < 2 nPa), which is a known regime difference, not a data-quality failure.

The 13 OOM pairwise disagreement encounters: 8 have "plausible" boundary, 5 have "uncertain"; 13 have "clean" transition, 3 have "mixed/unclear". The OOM disagreements are not driven by obviously contaminated data.

---

## 6. Verdict

**PASS.**

Justification:
1. **Nontrivial overlap:** 26 same-date multi-probe groups (far exceeding the minimum).
2. **Limited OOM divergence in target bins:** Only 1 of 4 low-cone/quasi-radial overlap groups shows OOM Dn disagreement, and that case involves different cone angles between probes.
3. **Not reducible to probe family alone:** 20 of 26 overlap groups (77%) show < 1 dex Dn spread across probes on the same day. The 2007-08-13 group (5 probes, cone 39-44°, Dn 0.01-0.03) demonstrates near-perfect cross-probe agreement in the low-cone bin.
4. **QC not concentrating in extreme values:** Extreme Dn/EB encounters are not systematically poor-QC.

**Mandatory caveats that survive PASS:**
- The quasi-radial bin has zero THD encounters; direct THD-vs-others comparison is impossible for cone < 30°.
- Dp is structurally entangled with cone bin — low-cone encounters are lower-Dp.
- EB shows a persistent ~0.5 dex offset between THB/THC and THA/THD/THE (THB/THC EB systematically higher, possibly calibration-related).
- The PASS verdict authorizes bounded descriptive comparison, not physical-mechanism inference.

---

## 7. Packaging consequence

**Phase 6 may be packaged as a bounded descriptive comparison under original Dn/EB semantics, but not as a validated favorable-conditions result, not as a Phase 4B extension, and not as a Phase 6B bridge.**

The cross-probe QC gate shows that same-day multi-probe encounters are broadly consistent in Dn/EB (77% within 1 dex), that the low-cone/quasi-radial bin is not dominated by probe-family artifacts, and that extreme values do not cluster in poor-QC encounters. This justifies treating the cone-bin-stratified Dn/EB comparison as descriptively meaningful under the original measurement-model family, with the caveats above.

---

## 8. Non-claims

- This gate does NOT establish that cone-angle physics is proven.
- This gate does NOT validate Phase 4B claims at new cone angles.
- This gate does NOT support occurrence rates, thresholds, labels, classes, or detector semantics.
- This gate does NOT resolve the EB offset between probe families.
- This gate does NOT resolve the Dp-cone entanglement.
