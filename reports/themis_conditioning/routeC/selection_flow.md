# Route C — Selection Flow

**Date:** 2026-03-31
**Scope:** One full scan of the Route C declared slice under original Dn/EB semantics.

---

## Declared slice

| Sub-slice | Coverage |
|---|---|
| 2007 full year | All THEMIS near-subsolar dayside |
| 2010 full year | All THEMIS near-subsolar dayside |
| 2008 Jan-Jul, Nov-Dec | All THEMIS near-subsolar dayside (non-Aug-Oct) |
| 2009 Jan-Jul, Nov-Dec | All THEMIS near-subsolar dayside (non-Aug-Oct) |

## Searched slice

All locally cached THEMIS encounter data (data_cache/normalized/) with timestamps falling in the declared slice. No internet fetch. Exhaustive scan of 60 cache directories; 7 entries matched the Route C slice, deduplicating to 3 unique date+probe combinations.

**Declared slice = Searched slice = YES** (within the constraint of locally available data).

## Local data availability

The local cache is sparse. Most of the 2007-2010 THEMIS archive was never fetched from CDAWeb. The Route C scan is complete over all available local data but does not cover the full 2007-2010 archive.

## Candidate flow

| # | Date | Probe | In slice? | Data complete? | SZA OK? | Evaluable? | Retained? | Reason |
|---|---|---|---|---|---|---|---|---|
| 1 | 2007-07-15 | THC | YES | NO (missing MOM, STATE, OMNI) | ? | NO | NO | Incomplete data |
| 2 | 2008-07-14 | THD | YES | NO (missing STATE) | ? | NO | NO | Incomplete data |
| 3 | 2010-10-23 | THD | YES | YES | YES (14 deg) | YES | YES | Dn=1.33, EB=1.20, cone=55 deg |

## Route A encounters also in Route C slice

| Encounter | Date | Probe | Cone | Dn | EB | Note |
|---|---|---|---|---|---|---|
| cand4a_oct23_10_thd | 2010-10-23 | THD | 35 deg | 1.30 | 1.02 | Already in clean N=9 catalogue |

Note: The cone angle differs between the Route A catalogue (35 deg) and the Route C recomputation (55 deg). This is because the original Route A pipeline used a different time window and OMNI averaging period. Both values place this encounter outside the quasi-radial bin (cone < 30 deg). Under the Route A value (35 deg) it falls in the low-cone bin; under the Route C recomputation (55 deg) it falls in the intermediate bin.

## Retained counts by cone bin

| Cone bin | Route C new | Route A in slice | Combined |
|---|---|---|---|
| quasi-radial (< 30 deg) | 0 | 0 | **0** |
| low-cone (30-45 deg) | 0 | 1 | **1** |
| intermediate (45-60 deg) | 1 | 0 | 1 |
| perpendicular (> 60 deg) | 0 | 0 | 0 |

## Hard stop evaluation

- quasi-radial retained: **0** (threshold: >= 1) — NOT MET
- low-cone retained: **1** (threshold: >= 5) — NOT MET
- **OUTCOME: HARD NULL**
