# Phase 6 EXTRA — Cross-Probe QC Gate Report

**Date:** 2026-03-31
**Input:** 757 retained encounters from 2007-2025 full local cache.
**Verdict:** **FAIL** (under predeclared absolute-count threshold).

---

## 1. Overlap-valid groups

**208 same-date multi-probe groups** (vs 26 in the 2007-2010 FULL EXP). Of these, **41 contain low-cone or quasi-radial encounters** (vs 4 previously).

---

## 2. Pairwise spread

| Metric | FULL EXP (2007-2010) | **EXTRA (2007-2025)** |
|---|---|---|
| Total pairs | 118 | **436** |
| OOM Dn pairs | 13 (11%) | **71 (16%)** |
| OOM EB pairs | 0 (0%) | **5 (1%)** |
| Consistent groups (< 1 dex) | 20/26 (77%) | **163/208 (78%)** |
| Inconsistent groups (>= 1 dex) | 6/26 (23%) | **45/208 (22%)** |
| LC/QR groups with OOM Dn | 1/4 (25%) | **9/41 (22%)** |

---

## 3. Why the verdict flipped from PASS to FAIL

The predeclared FAIL criterion is: **LC/QR OOM groups >= 3**.

- Original: 1/4 = 25% -> below absolute threshold of 3 -> **PASS**
- EXTRA: 9/41 = 22% -> above absolute threshold of 3 -> **FAIL**

**The underlying consistency rate is actually slightly better in the EXTRA dataset** (22% OOM rate vs 25%, 78% group consistency vs 77%). The verdict flip is entirely driven by the absolute-count threshold applied to a 10x larger sample.

---

## 4. Probe-conditioned analysis

| Cone bin | THD N | THD Dn median | non-THD N | non-THD Dn median |
|---|---|---|---|---|
| quasi-radial | 6 | 1.616 | 22 | 0.730 |
| low-cone | 17 | 0.670 | 72 | 0.832 |
| intermediate | 54 | 0.642 | 145 | 0.821 |
| perpendicular | 140 | 0.758 | 301 | 0.726 |

THD is now present in ALL cone bins including quasi-radial (N=6) — this was impossible in the 2007-2010 subset (0 THD in QR). The THD/non-THD Dn medians are within the same order of magnitude in every bin.

---

## 5. Regime-shift check

| Cone bin | N | THD fraction | Dp median |
|---|---|---|---|
| quasi-radial | 28 | 21% | 1.65 |
| low-cone | 89 | 19% | 1.53 |
| intermediate | 199 | 27% | 2.25 |
| perpendicular | 441 | 32% | 2.44 |

Dp-cone entanglement persists but is less extreme than in 2007-2010. THD is present at 19-21% even in the low-cone/QR bins (vs 0% in the original).

---

## 6. QC concentration

222 extreme encounters (Dn < 0.05 or EB > 5). Of these, 186 (84%) have "clean" transition QC. Extreme values do NOT cluster in poor-QC encounters — same finding as the original gate.

---

## 7. Cross-cycle independent verification (new in EXTRA)

| Cycle | Dn median (all bins) | EB median (all bins) | QR count | LC count |
|---|---|---|---|---|
| Cycle 1 (2007-2010) | ~0.70 | ~3.0 | 5 | 17 |
| Cycle 2 (2016-2019) | ~0.90 | ~2.9 | 11 | 34 |

Both cycles populate all cone bins independently. Dn/EB ranges overlap. This is an independent replication that was unavailable in the 2007-2010 FULL EXP.

---

## 8. Verdict

**FAIL** under the predeclared absolute-count criterion (LC/QR OOM groups = 9 >= 3).

**However, the rate-based evidence is actually equivalent to or slightly better than the original PASS:**

| Rate metric | Original (PASS) | EXTRA (FAIL) |
|---|---|---|
| Group consistency | 77% | 78% |
| LC/QR OOM rate | 25% | 22% |
| THD in QR bin | 0% | 21% |

The FAIL is a threshold-design artifact, not a data-quality deterioration.

---

## 9. Packaging consequence

Under strict predeclared logic:
**"Phase 6 EXTRA remains packageable only as a bounded descriptive-methodological sidecar; no direct cross-bank comparison to frozen Phase 4B should be claimed."**

**Interpretive note for user decision:** The underlying cross-probe consistency is the same or better than the dataset that PASSED. The absolute-count threshold (>= 3) was designed for the 148-encounter FULL EXP; applied to a 5x larger sample, it mechanically produces FAIL even when rates improve. Whether to use the rate-based or absolute-count criterion for final packaging is a user judgment call.

---

## 10. Non-claims

Same as all Phase 6 work. No thresholds, labels, classes, detector, occurrence, or mission language. Phase 4B unchanged. Route B not used. Phase 6B blocked.
