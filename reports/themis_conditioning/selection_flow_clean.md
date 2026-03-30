# Phase 6 Route A ¡ª Clean Selection Flow

**Generated:** 2026-03-30T21:51:27.569294

## Source universe

Declared: All locally cached evaluable THEMIS encounters from live-mode CDAWeb-fetched runs
Searched: All runs/*/encounter_*.json, deduplicated by date+probe, filtered to evaluable with Dn>0
**Match: YES**

## Synthetic-fixture filter

Filter: Exclude encounters where dp=2.0 AND bz=2.0 AND ma=8.0 AND sza=0.0 (synthetic fixture signature)
Synthetic detected: 2 (pilot_001, pilot_002)
Clean real encounters retained: 9

## Clean catalogue

| Encounter | Probe | Date | SZA | Cone | Dp | Dn | EB | BG occ |
|---|---|---|---|---|---|---|---|---|
| usable_aug18_6h | thd | 2008-08-18 | 22 | 30.7 | 4.2 | 0.120 | 2.491 | 0.484 |
| usable_sep03_5h | thd | 2008-09-03 | 15 | 56.2 | 3.7 | 2.872 | 0.799 | 0.210 |
| cand4a_sep19_08_the | the | 2008-09-19 | 15 | 64.2 | 2.8 | 0.763 | 2.124 | 0.288 |
| usable_sep13_09_6h | thd | 2009-09-13 | 17 | 61.2 | 3.1 | 0.391 | 1.958 | 0.470 |
| usable_sep20_09_6h | thd | 2009-09-20 | 10 | 70.0 | 3.0 | 0.969 | 1.477 | 0.463 |
| usable_sep26_09_10h | thd | 2009-09-26 | 4 | 84.6 | 3.0 | 0.940 | 1.958 | 0.404 |
| usable_sep27_09_10h | thd | 2009-09-27 | 4 | 56.6 | 3.1 | 1.313 | 1.227 | 0.573 |
| usable_oct24_09_6h | thd | 2009-10-24 | 20 | 86.4 | 4.2 | 2.186 | 4.223 | 0.649 |
| cand4a_oct23_10_thd | thd | 2010-10-23 | 14 | 35.0 | 3.1 | 1.299 | 1.022 | 0.019 |

## Tranche-2 low-cone candidates (all BG-occupancy excluded)

- t2_20080904_thd: cone_search=43.3, status=excluded, reason=FAIL_OCCUPANCY
- t2_20090928_thd: cone_search=42.9, status=excluded, reason=FAIL_OCCUPANCY
- t2_20090928_the: cone_search=43.6, status=excluded, reason=FAIL_OCCUPANCY
