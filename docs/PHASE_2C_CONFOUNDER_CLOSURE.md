# Phase 2C — Confounder Closure / Interval Audit

**Date:** 2026-03-26
**Bank:** 9 windows / 7 distinct passes / THD only

---

## 1. Purpose

Determine whether the current 7-pass comparator bank contains a sufficiently clean subset to justify a later detector-readiness review. This is done by auditing interval-level confounder structure, not by changing windows, metrics, or naming.

---

## 2. Method

For each of the 7 independent passes (one representative window each):
1. Loaded raw cached FGM, MOM, STATE, OMNI data
2. Resampled to 10 s on the encounter analysis timeline
3. Computed Pdyn proxy (n × v²) and identified spike intervals (> 2× median)
4. Computed leave-spike-out Dn and EB
5. Measured near-bin density coefficient of variation (wave/fluctuation proxy)
6. Assessed spike spatial distribution (near-bin vs background-bin)

Full per-pass results: `docs/PASS_INTERVAL_AUDIT.md`

---

## 3. Key findings

### 3.1 Universal jet-flag reinterpreted

Phase 2B reported jet_flag = TRUE for all 9 windows. The interval audit reveals **why** this is universal and what it means structurally:

- **Spike fractions range from 10% to 35%** across the 7 passes
- Spikes are NOT uniformly distributed across bins — they tend to concentrate in whichever bin has more occupancy (usually BG)
- The 2× median Pdyn threshold is too broad for 6-10h windows; it catches normal magnetosheath variability, not just jet-like structures

**Critical finding:** For P7 (Oct 24), spikes dominate 35% of data and are concentrated in the BG bin. After spike removal, Dn collapses from 2.19 to 0.67 and EB from 4.22 to 0.97 — the window's entire metric signature is spike-driven.

### 3.2 One pass is spike-dominated and unreliable

**P7 (Oct 24, 2009)** must be demoted from the usable bank for metric comparison purposes:
- 35% spike fraction (highest)
- All 495 spikes in BG bin
- After spike removal: Dn → 0.67, EB → 0.97 (near null)
- Window-level metrics are artifacts of spike contamination

### 3.3 One seed (seed_D / P3) has partially spike-dependent EB

P3 (Sep 13, 2009): Dn is robust (0.39 → 0.41 after spike removal), but EB drops from 1.96 to 1.46. The background bin's B-field signal is partially inflated by BG-concentrated spikes. Seed_D's "strongest anti-correlation" claim is weakened.

### 3.4 One seed (seed_A / P1) has very high density noise

P1 (Aug 18, 2008): Near-bin density CV = 0.93. Qualitative pattern survives spike removal (Dn 0.12 → 0.17, still well below 1), but the extreme noise raises wave/mirror-mode risk for the near-bin density.

### 3.5 Clean subset identified

**4 passes survive interval-level scrutiny with minimal caveats:**

| Pass | ΔDn | ΔEB | Spike% | Dens CV | Assessment |
|---|---|---|---|---|---|
| **P4** (Sep 20) | 0.01 | 0.02 | 21% | 0.08 | **Cleanest** |
| **P5** (Sep 26) | 0.04 | 0.01 | 13% | 0.33 | Clean |
| **P2** (Sep 3) | 0.22 | 0.02 | 16% | 0.23 | Clean (EB robust, Dn moderate shift) |
| **P6** (Sep 27) | 0.22 | 0.02 | 10% | 0.24 | Clean (low spikes) |

**2 passes survive with caveats:**

| Pass | Main caveat |
|---|---|
| **P1** (Aug 18) | High density noise (CV=0.93); possible wave contamination in near bin |
| **P3** (Sep 13) | EB partially spike-dependent (Δ=0.50); Dn robust |

**1 pass does not survive:**

| Pass | Reason |
|---|---|
| **P7** (Oct 24) | ❌ Spike-dominated; metrics collapse after spike removal |

---

## 4. Seed status after interval audit

| Seed | Pass | Status | Caveat change |
|---|---|---|---|
| seed_A | P1 | **usable with caveat** | Add: high density noise (CV=0.93); wave/mirror risk in near bin |
| seed_B | P4 | **cleanest — unchanged** | No new caveat. Strongest interval-level support. |
| seed_C | P2 | **clean — unchanged** | Dn shows moderate spike sensitivity (Δ=0.22) but EB is robust |
| seed_D | P3 | **weakened** | EB partially spike-dependent (1.96 → 1.46). Anti-correlation claim weakened. |

**Alternate seed consideration:** P5 (Sep 26) or P6 (Sep 27) could serve as alternate seed_D replacements, though neither has ρ as extreme as P3's -0.90. P5 has ρ=-0.91 at window level but this was not interval-audited for spike sensitivity on ρ directly (deferred: would require sidecar trend recomputation).

---

## 5. Transient / mixing / boundary-motion status

All three remain **UNKNOWN** for all 7 passes. Current data products and the frozen measurement model do not support their resolution:

- **Transient:** Would require foreshock geometry analysis and IMF Bx/cone-angle conditioning, which conflicts with IMF-agnostic detection principle at this stage.
- **Mixing:** Would require plasma-regime classification beyond current conservative membership check.
- **Boundary motion:** Encounter-averaged boundaries cannot resolve sub-window boundary crossings. Would require time-varying s (deferred).

These remain as carried-forward caveats, not as blockers.

---

## 6. Final gate judgment

### Question

Does the current 7-pass bank contain a sufficiently clean subset to justify a later detector-readiness review?

### Answer: **YES, with conditions**

**Clean core subset: P2, P4, P5, P6** (4 independent passes). These show:
- Metrics that qualitatively survive leave-spike-out sensitivity
- Low to moderate density noise
- No spike-dominated collapse

**Usable with caveats: P1, P3** (2 additional passes, including seeds A and D). These add range but carry identified interval-level concerns.

**Excluded from metric comparison: P7** (1 pass). Spike-dominated; window-level metrics are not representative.

### Conditions for any later detector-readiness step

1. P7 must be excluded or flagged in any metric-based analysis
2. Seed_D's EB must be interpreted with spike-sensitivity caveat
3. Seed_A's near-bin density noise must be acknowledged
4. Effective clean N = 4 (P2, P4, P5, P6), with 2 additional cautious passes (P1, P3)
5. Transient, mixing, and boundary-motion flags remain unresolved — any later work inherits these gaps
6. All windows remain measurement-model-valid comparator windows — no labels introduced
