# Window Bank Summary — Phase 2a Final State

**Date:** 2026-03-26
**Canonical run:** `runs/20260326T040343Z_d0425fd4/`
**Config:** `configs/pilot_live_usable.yaml`

---

## Bank overview

**9 measurement-model-valid comparator windows** across **7 distinct orbital passes**, 2 THEMIS seasons (2008 + 2009), 1 probe (THD).

All windows:
- Produce PASS preflight status with non-null core metrics
- Have both near-bin (s = 0.2–0.4) and background-bin (s > 0.6) occupancy
- Are dayside near-subsolar (SZA 4°–22°)
- Use THD with encounter-averaged Dp > 3 nPa
- Are conservatively named: "measurement-model-valid near-MP comparator windows"

No window is classified as PDL-positive, non-PDL, or any labeled category.

---

## Pass inventory

| Pass | Date | Season | N windows | SZA range | Dp | Bz |
|---|---|---|---|---|---|---|
| 1 | 2008-08-18 | 2008 | 2 (6h, 8h) | 22° | 3.6–4.2 | +0.1 to +0.3 |
| 2 | 2008-09-03 | 2008 | 2 (6h, 8h) | 12–14° | 3.5 | +0.9 to +2.6 |
| 3 | 2009-09-13 | 2009 | 1 (6h) | 17° | 3.1 | -1.4 |
| 4 | 2009-09-20 | 2009 | 1 (6h) | 10° | 3.0 | +1.4 |
| 5 | 2009-09-26 | 2009 | 1 (10h) | 4° | 3.0 | +0.9 |
| 6 | 2009-09-27 | 2009 | 1 (10h) | 4° | 3.1 | -1.7 |
| 7 | 2009-10-24 | 2009 | 1 (6h) | 20° | 4.2 | -0.5 |

---

## Window table

| ID | Date | SZA | Dp | Bz | Near% | BG% | Dn | EB | ρ(n,B) |
|---|---|---|---|---|---|---|---|---|---|
| usable_aug18_6h | 2008-08-18 | 22° | 4.2 | +0.3 | 16% | 48% | 0.12 | 2.49 | -0.46 |
| usable_sep03_6h | 2008-09-03 | 14° | 3.5 | +0.9 | 17% | 27% | 2.31 | 0.82 | -0.52 |
| usable_sep03_8h | 2008-09-03 | 12° | 3.5 | +2.6 | 13% | 40% | 2.07 | 0.80 | -0.51 |
| usable_sep13_09_6h | 2009-09-13 | 17° | 3.1 | -1.4 | 17% | 47% | 0.39 | 1.96 | -0.90 |
| usable_sep20_09_6h | 2009-09-20 | 10° | 3.0 | +1.4 | 9% | 46% | 0.97 | 1.48 | -0.63 |
| usable_sep26_09_10h | 2009-09-26 | 4° | 3.0 | +0.9 | 18% | 40% | 0.94 | 1.96 | -0.91 |
| usable_sep27_09_10h | 2009-09-27 | 4° | 3.1 | -1.7 | 16% | 57% | 1.31 | 1.23 | -0.72 |
| usable_oct24_09_6h | 2009-10-24 | 20° | 4.2 | -0.5 | 14% | 65% | 2.19 | 4.22 | -0.66 |
| usable_aug18_8h | 2008-08-18 | 22° | 3.6 | +0.1 | 17% | 12% | 0.88 | 2.08 | N/A |

---

## Metric diversity

The bank spans a range of Dn values from 0.12 to 2.31, EB from 0.80 to 4.22, and ρ from -0.91 to -0.46. This range is descriptive and does not imply classification. The measurement model resolves different metric patterns under different upstream conditions.

---

## Candidates tried but not promoted

| Candidate | Date | Reason for non-promotion |
|---|---|---|
| sep03_09 (6h/10h) | 2009-09-03 | FAIL_OCCUPANCY: no background bin even at 10h (Dp not high enough at apogee) |
| sep26_09 (6h) | 2009-09-26 | FAIL_OCCUPANCY: no near bin at 6h (needed 10h to capture inbound leg) |
| sep27_09 (6h) | 2009-09-27 | FAIL_OCCUPANCY: no near bin at 6h (needed 10h) |
| oct08 family (all) | 2008-10-13/15 | FAIL_OCCUPANCY: Dp < 2 nPa, s never reaches BG bin at any duration |

---

## Readiness assessment

With 9 windows across 7 distinct passes, the bank now has enough pass diversity for a **bounded metric-behavior review** — a systematic comparison of how the core metrics (Dn, EB, Δβ, ρ) vary across windows, without defining thresholds or labels. This is the next bounded step beyond Phase 2a.
