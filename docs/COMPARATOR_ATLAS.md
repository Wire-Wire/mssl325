# Pass-Aware Comparator Atlas

**Date:** 2026-03-26
**Bank:** 9 windows / 7 distinct passes / THD only / 2008 + 2009 seasons
**Config:** `configs/pilot_live_usable.yaml`
**Canonical run:** `runs/20260326T040343Z_d0425fd4/`

---

## Purpose

This atlas is a descriptive, pass-aware inventory of the current window bank. It does not classify, label, or interpret any window. Every window is a **measurement-model-valid near-MP comparator window** and nothing more.

---

## Pass structure

The bank contains 9 windows from 7 distinct orbital passes. Two passes (Aug 18 and Sep 3, 2008) have duration variants — these are operational variants of the same orbital traverse, not independent observations.

**Effective independent sample size: 7 passes.**

| Pass | Date | Season | Windows | Duration variant? |
|---|---|---|---|---|
| P1 | 2008-08-18 | 2008 | usable_aug18_6h, usable_aug18_8h | yes (2 variants) |
| P2 | 2008-09-03 | 2008 | usable_sep03_6h, usable_sep03_8h | yes (2 variants) |
| P3 | 2009-09-13 | 2009 | usable_sep13_09_6h | no |
| P4 | 2009-09-20 | 2009 | usable_sep20_09_6h | no |
| P5 | 2009-09-26 | 2009 | usable_sep26_09_10h | no |
| P6 | 2009-09-27 | 2009 | usable_sep27_09_10h | no |
| P7 | 2009-10-24 | 2009 | usable_oct24_09_6h | no |

---

## Full window table

| ID | Pass | Variant? | SZA | Dp | Bz | Near% | BG% | Memb% | Dn | EB | Δβ | ρ(n,B) | Persist | ptot_sm |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| usable_aug18_6h | P1 | yes | 22° | 4.2 | +0.3 | 16% | 48% | 86% | 0.12 | 2.49 | -10.1 | -0.46 | 0.94 | 0.86 |
| usable_aug18_8h | P1 | yes | 22° | 3.6 | +0.1 | 17% | 12% | 85% | 0.88 | 2.08 | -10.1 | N/A | 0.72 | 0.83 |
| usable_sep03_6h | P2 | yes | 14° | 3.5 | +0.9 | 17% | 27% | 100% | 2.31 | 0.82 | +1.7 | -0.52 | 0.00 | 0.80 |
| usable_sep03_8h | P2 | yes | 12° | 3.5 | +2.6 | 13% | 40% | 100% | 2.07 | 0.80 | +1.7 | -0.51 | 0.00 |  0.80 |
| usable_sep13_09_6h | P3 | no | 17° | 3.1 | -1.4 | 17% | 47% | 100% | 0.39 | 1.96 | -6.8 | -0.90 | 1.00 | 0.94 |
| usable_sep20_09_6h | P4 | no | 10° | 3.0 | +1.4 | 9% | 46% | 100% | 0.97 | 1.48 | -3.1 | -0.63 | 0.66 | 0.94 |
| usable_sep26_09_10h | P5 | no | 4° | 3.0 | +0.9 | 18% | 40% | 98% | 0.94 | 1.96 | -12.8 | -0.91 | 0.61 | 0.81 |
| usable_sep27_09_10h | P6 | no | 4° | 3.1 | -1.7 | 16% | 57% | 96% | 1.31 | 1.23 | -4.2 | -0.72 | 0.32 | 0.86 |
| usable_oct24_09_6h | P7 | no | 20° | 4.2 | -0.5 | 14% | 65% | 98% | 2.19 | 4.22 | -3.4 | -0.66 | 0.00 | 0.93 |

---

## Per-channel notes

| Metric | Available | Missing | Note |
|---|---|---|---|
| Dn | 9/9 | — | |
| EB | 9/9 | — | |
| Δβ | 9/9 | — | |
| ρ(n,B) | 8/9 | usable_aug18_8h | Trend anti-correlation not computed for 8h variant (insufficient near-bin trend data) |
| Persistence | 9/9 | — | |
| ptot_smooth | 9/9 | — | |

---

## Observed metric ranges (descriptive only — not thresholds)

| Metric | Min | Max | Range |
|---|---|---|---|
| Dn | 0.12 | 2.31 | 2.19 |
| EB | 0.80 | 4.22 | 3.42 |
| Δβ | -12.8 | +1.7 | 14.5 |
| ρ(n,B) | -0.91 | -0.46 | 0.45 |
| Persistence | 0.00 | 1.00 | 1.00 |

These ranges describe what the measurement model produces under the observed upstream conditions. They do not define boundaries between physical states.

---

## Naming discipline

Every window in this atlas is a **measurement-model-valid near-MP comparator window**. No window is classified, labeled, or assigned to a physical category. Metric values are operational outputs of the frozen measurement model, not diagnostic indicators of specific magnetosheath states.
