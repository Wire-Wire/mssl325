# Comparator Bank Report

**Windows:** 9 | **Passes:** 7 | **Probe:** THD

## Evidence matrix

| Pass | Date | Window | Status | SZA | Dp | Bz | Near% | BG% | Dn | EB | Spike% | Dn_clean | EB_clean |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 2008-08-18 | usable_aug18_6h | cautious | 22 | 4.2 | +0.3 | 16% | 48% | 0.12 | 2.49 | 24% | 0.17 | 2.29 |
| P1 | 2008-08-18 | usable_aug18_8h | cautious | 22 | 3.6 | +0.1 | 17% | 12% | 0.88 | 2.08 | 24% | 0.17 | 2.29 |
| P2 | 2008-09-03 | usable_sep03_6h | clean_core | 14 | 3.5 | +0.9 | 17% | 27% | 2.31 | 0.82 | 16% | 2.10 | 0.84 |
| P2 | 2008-09-03 | usable_sep03_8h | clean_core | 12 | 3.5 | +2.6 | 13% | 40% | 2.07 | 0.80 | 16% | 2.10 | 0.84 |
| P3 | 2009-09-13 | usable_sep13_09_6h | cautious | 17 | 3.1 | -1.4 | 17% | 47% | 0.39 | 1.96 | 25% | 0.41 | 1.46 |
| P4 | 2009-09-20 | usable_sep20_09_6h | clean_core | 10 | 3.0 | +1.4 | 9% | 46% | 0.97 | 1.48 | 21% | 0.96 | 1.49 |
| P5 | 2009-09-26 | usable_sep26_09_10h | clean_core | 4 | 3.0 | +0.9 | 18% | 40% | 0.94 | 1.96 | 13% | 0.90 | 1.94 |
| P6 | 2009-09-27 | usable_sep27_09_10h | clean_core | 4 | 3.1 | -1.7 | 16% | 57% | 1.31 | 1.23 | 10% | 1.10 | 1.20 |
| P7 | 2009-10-24 | usable_oct24_09_6h | excluded | 20 | 4.2 | -0.5 | 14% | 65% | 2.19 | 4.22 | 35% | 0.67 | 0.97 |

## Confounder summary

| Window | Jet | Wave | Transient | Mixing | Motion | Grade |
|---|---|---|---|---|---|---|
| usable_aug18_6h | TRUE | false | UNKNOWN | UNKNOWN | false | Silver |
| usable_sep03_6h | TRUE | false | UNKNOWN | UNKNOWN | false | Silver |
| usable_sep03_8h | TRUE | false | UNKNOWN | UNKNOWN | false | Silver |
| usable_sep13_09_6h | TRUE | false | UNKNOWN | UNKNOWN | false | Silver |
| usable_sep26_09_10h | TRUE | false | UNKNOWN | UNKNOWN | false | Silver |
| usable_sep20_09_6h | TRUE | false | UNKNOWN | UNKNOWN | false | Silver |
| usable_sep27_09_10h | TRUE | false | UNKNOWN | UNKNOWN | false | Silver |
| usable_oct24_09_6h | TRUE | false | UNKNOWN | UNKNOWN | false | Silver |
| usable_aug18_8h | TRUE | false | UNKNOWN | UNKNOWN | false | Silver |

## Naming discipline

Every window is a **measurement-model-valid near-MP comparator window**.
Evidence status (clean_core / cautious / excluded) is stage-local bookkeeping only.