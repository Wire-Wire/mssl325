# Window Bank Summary — Phase 2a Frozen State

**Date:** 2026-03-26
**Canonical run:** `runs/20260326T033744Z_9f985ab9/`
**Config:** `configs/pilot_live_usable.yaml`

---

## Bank overview

**7 measurement-model-valid comparator windows** across 4 orbital passes, 2 THEMIS seasons.

All windows:
- Produce PASS preflight status with non-null core metrics
- Have both near-bin (s = 0.2–0.4) and background-bin (s > 0.6) occupancy
- Are dayside near-subsolar (SZA 4°–22°)
- Use THD with encounter-averaged Dp > 3 nPa (compressed-sheath conditions)

No window is classified as PDL-positive, non-PDL, or any labeled category.

---

## Window table

| ID | Probe | Time range | SZA | Dp | Bz | Near% | BG% | Dn | EB | Δβ | ρ(n,B) | Memb% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| usable_aug18_6h | thd | 2008-08-18 18:00–00:00 | 22° | 4.2 | +0.3 | 16% | 48% | 0.12 | 2.49 | -10.1 | -0.46 | 86% |
| usable_sep03_6h | thd | 2008-09-03 19:00–01:00 | 14° | 3.5 | +0.9 | 17% | 27% | 2.31 | 0.82 | +1.7 | -0.52 | 100% |
| usable_sep03_8h | thd | 2008-09-03 17:00–01:00 | 12° | 3.5 | +2.6 | 13% | 40% | 2.07 | 0.80 | +1.7 | -0.51 | 100% |
| usable_sep13_09_6h | thd | 2009-09-13 17:00–23:00 | 17° | 3.1 | -1.4 | 17% | 47% | 0.39 | 1.96 | -6.8 | -0.90 | 100% |
| usable_sep26_09_10h | thd | 2009-09-26 14:00–00:00 | 4° | 3.0 | +0.9 | 18% | 40% | 0.94 | 1.96 | -12.8 | -0.91 | 98% |
| usable_oct24_09_6h | thd | 2009-10-24 14:30–20:30 | 20° | 4.2 | -0.5 | 14% | 65% | 2.19 | 4.22 | -3.4 | -0.66 | 98% |
| usable_aug18_8h | thd | 2008-08-18 17:00–01:00 | 22° | 3.6 | +0.1 | 17% | 12% | 0.88 | 2.08 | -10.1 | N/A | 85% |

---

## Per-window details

### usable_aug18_6h (2008-08-18)
- **Operational role:** measurement-model-valid near-MP comparator window
- **Position:** X=10.5 Re, Y=3.2, Z=-2.8, SZA=22°
- **Upstream:** Dp=4.2 nPa, Bz=+0.3 nT, Ma=11.2
- **s range:** [0.000, 0.715], 2161 points
- **Occupancy:** very_near=13%, near=16%, background=48%
- **Metrics:** Dn=0.12, EB=2.49, Δβ=-10.1, ρ=-0.46, persistence=0.94
- **Membership:** 86% sheath-plausible
- **Grade:** Silver (2 flags UNKNOWN: transient, mixing)
- **Notes:** Layer-like metric pattern. Different upstream from Sep 3.

### usable_sep03_6h (2008-09-03)
- **Operational role:** measurement-model-valid near-MP comparator window
- **Position:** X=10.4 Re, Y=1.7, Z=-1.9, SZA=14°
- **Upstream:** Dp=3.5 nPa, Bz=+0.9 nT, Ma=5.7
- **s range:** [0.000, 0.674], 2161 points
- **Occupancy:** very_near=31%, near=17%, background=27%
- **Metrics:** Dn=2.31, EB=0.82, Δβ=+1.7, ρ=-0.52, persistence=0.00
- **Membership:** 100% sheath-plausible
- **Grade:** Silver
- **Notes:** Compressed-sheath pattern (Dn>1, EB<1). First usable window found.

### usable_sep13_09_6h (2009-09-13)
- **Operational role:** measurement-model-valid near-MP comparator window
- **Position:** X=10.9 Re, Y=-0.9, Z=-1.8, SZA=17°
- **Upstream:** Dp=3.1 nPa, Bz=-1.4 nT (southward), Ma=9.1
- **s range:** [0.198, 0.654], 2161 points
- **Occupancy:** very_near=0.2%, near=17%, background=47%
- **Metrics:** Dn=0.39, EB=1.96, Δβ=-6.8, ρ=-0.90, persistence=0.96
- **Membership:** 100% sheath-plausible
- **Grade:** Silver
- **Notes:** Southward Bz regime. Strong anti-correlation.

### usable_sep26_09_10h (2009-09-26)
- **Operational role:** measurement-model-valid near-MP comparator window
- **Position:** X=11.3 Re, Y=-0.4, Z=-0.7, SZA=4°
- **Upstream:** Dp=3.0 nPa, Bz=+0.9 nT, Ma=8.9
- **s range:** [0.000, 0.713], 3601 points
- **Occupancy:** very_near=15%, near=18%, background=40%
- **Metrics:** Dn=0.94, EB=1.96, Δβ=-12.8, ρ=-0.91, persistence=0.81
- **Membership:** 98% sheath-plausible
- **Grade:** Silver
- **Notes:** Closest to subsolar of any window (SZA=4��). Very strong ρ.

### usable_oct24_09_6h (2009-10-24)
- **Operational role:** measurement-model-valid near-MP comparator window
- **Position:** X=10.7 Re, Y=-2.3, Z=-2.3, SZA=20°
- **Upstream:** Dp=4.2 nPa, Bz=-0.5 nT, Ma=7.0
- **s range:** [0.221, 0.741], 2161 points
- **Occupancy:** very_near=0%, near=14%, background=65%
- **Metrics:** Dn=2.19, EB=4.22, Δβ=-3.4, ρ=-0.66, persistence=0.02
- **Membership:** 98% sheath-plausible
- **Grade:** Silver
- **Notes:** Highest EB (4.22) and highest BG occupancy (65%).

---

## Caveats

- All windows use encounter-averaged Dp/Bz for boundary computation; time-varying boundaries deferred
- All windows are 6–10 hours long; these are exploratory durations, not standards
- Membership check is conservative (plasma/field basic sanity, not a region classifier)
- Grade capped at Silver because transient_flag and mixing_flag are not yet implemented
- The pattern Dn>1/EB<1 vs Dn<1/EB>1 is descriptive, NOT a PDL classification
