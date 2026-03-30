# Phase 6A Tranche-2 Selection Flow

**Declared slice:** Low-cone-targeted (cone ≤ 45°) THEMIS dayside encounters from 2007–2010, not already in tranche 1.

## Candidate search

| Step | Count |
|---|---|
| Dates scanned (every 3rd day, THD+THE, Aug–Oct 2008–2009) | ~80 |
| Near-subsolar with SZA ≤ 30° | ~20 |
| OMNI available with cone ≤ 45° | **3** |
| With s-range potential (s_apo > 0.3) | 3 |

## Pipeline processing

| Encounter | Probe | Date | Cone (search) | Dp | Status | Reason |
|---|---|---|---|---|---|---|
| t2_20080904_thd | THD | 2008-09-04 | 43° | 2.7 | FAIL_OCCUPANCY | BG bin = 0% |
| t2_20090928_thd | THD | 2009-09-28 | 43° | 1.9 | FAIL_OCCUPANCY | BG bin = 0% |
| t2_20090928_the | THE | 2009-09-28 | 44° | 1.9 | FAIL_OCCUPANCY | BG bin = 0% |

## Result

**Zero retained.** All 3 low-cone candidates fail the background-bin occupancy screen because low-cone IMF conditions tend to have lower Dp, and at Dp < ~2.7 nPa the sheath is too wide for the ~11.6 Re inner-probe apogee to reach s > 0.6.

This is a structural selection-function limitation: the frozen measurement model's dual-bin requirement under the inner-probe orbital constraint systematically excludes low-Dp / low-cone conditions.
