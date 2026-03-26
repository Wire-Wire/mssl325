# Selection Function Audit — How the Current Bank Was Shaped

**Date:** 2026-03-26
**Status:** Audit document. Does not change the bank.

---

## Purpose

This document reconstructs the practical constraints that shaped the current 9-window / 7-pass comparator bank. The purpose is to make the bank's selection biases explicit, not to correct them.

---

## The 6 constraints that shaped inclusion

### 1. Orbital apogee constraint (THD ~11.6 Re)

THEMIS-D has a ~24-hour orbit with apogee ~11.6 Re. This fixes the maximum geocentric distance available on any pass. Since the bow shock is typically at ~13 Re (Merka 2005), THD can never reach the outer sheath unless the boundaries are compressed inward by elevated Dp.

**Effect:** Structurally excludes low-Dp conditions from the bank.

### 2. Dp > ~3 nPa compressed-sheath requirement

For THD at 11.6 Re to produce s > 0.6 (background bin), the boundaries must be compressed so that the sheath width is narrower than the orbital range. This requires encounter-averaged Dp > ~3 nPa. Below this, s stays in the [0.0, 0.5] range regardless of window duration.

**Effect:** The entire bank is systematically biased toward compressed-sheath conditions. Lower-Dp sheath states (which may be more favorable for classical PDL formation under weaker reconnection) are structurally excluded.

### 3. Dayside geometry requirement

The frozen measurement model requires dayside near-subsolar geometry (SZA < 60° operational gate, with a preference for SZA < 30°). THD's dayside season occurs roughly Aug–Oct when the orbital apogee sweeps through the noon sector.

**Effect:** Bank is restricted to THD Aug–Oct 2008 and Sep–Oct 2009.

### 4. MOM L2 data availability

THEMIS MOM L2 (on-board ion moments, peim) is required for density and velocity. MOM starts ~Oct 2007 for THD. The alternative (GMOM, ground-computed) was not tested because the repo architecture uses MOM.

**Effect:** Excludes pre-Oct-2007 periods. Also excludes THC before Jan 2008 (MOM not available). THB has MOM but sparse plasma data in the sheath at its ~30 Re apogee.

### 5. OMNI data quality

OMNI 1-min upstream data is used for boundary model inputs and fill-value masking. OMNI gaps or fill values reduce the usable fraction of candidate windows. Windows with heavy OMNI intermittency may fail data-validity preflight.

**Effect:** Moderate — most 2008–2009 periods have adequate OMNI coverage.

### 6. Encounter-averaged boundary computation

The current measurement model uses a single set of MP/BS standoff distances per encounter, computed from median upstream conditions over the window. If Dp varies substantially within a window, the encounter-averaged s may not accurately represent the time-varying spatial position.

**Effect:** Longer windows (needed for dual-bin leverage) are more vulnerable to this averaging artifact. Windows where Dp changes by >50% during the encounter may have distorted s-mapping.

---

## What is NOT in the current selection

| Absent factor | Why absent |
|---|---|
| Low-Dp sheath (Dp < 2 nPa) | Structurally excluded by constraint #2 |
| Flank / high-latitude geometry | Excluded by constraint #3 |
| Cross-probe diversity | Only THD used; THC/THE have same apogee; THB has sparse MOM |
| Seasons beyond Aug–Oct | THD dayside apogee rotates out of noon sector |
| Pre-2007 data | MOM not available |
| IMF-conditioned selection | Detection is IMF-agnostic; Bz enters only post-detection |

---

## Naming discipline

This audit describes the current bank's practical construction. It does not propose corrections, new searches, or bank expansion. All windows remain **measurement-model-valid near-MP comparator windows**.
