# Phase 6 Route C — Result: Bounded Null

**Date:** 2026-03-31
**Authority:** User-authorized Route C execution with predeclared hard stop.
**Outcome:** HARD NULL. Phase 6 science closed. Writing-safe return activated.

---

## 1. What was done

One full scan of the Route C declared slice under original Dn/EB semantics. The declared slice covered the complement of the Phase 6A tranche-1 and tranche-2 searched space within 2007-2010: specifically 2007 (full year), 2010 (full year), and 2008-2009 months outside Aug-Oct.

The scan was constrained to locally cached data only (no internet fetch). All 60 data_cache/normalized/ directories were inventoried. Seven cache entries matched the Route C slice, deduplicating to 3 unique date+probe combinations.

---

## 2. What the scan found

| Date | Probe | Data status | Evaluable? | Cone | Retained? |
|---|---|---|---|---|---|
| 2007-07-15 | THC | Incomplete (no MOM, STATE, OMNI) | No | ? | No |
| 2008-07-14 | THD | Incomplete (no STATE) | No | ? | No |
| 2010-10-23 | THD | Complete | Yes | 55 deg (intermediate) | Yes |

The single complete encounter (2010-10-23 THD) is the same physical encounter as cand4a_oct23_10_thd in the clean Route A catalogue (where it appears with cone=35 deg from the original pipeline run). Under both cone values, it is not quasi-radial.

One additional Route A catalogue encounter falls in the Route C slice: cand4a_oct23_10_thd (2010-10-23, cone=35 deg under Route A, low-cone bin).

---

## 3. Hard stop evaluation

| Criterion | Value | Threshold | Met? |
|---|---|---|---|
| quasi-radial (cone < 30 deg) retained | 0 | >= 1 | NO |
| low-cone (30-45 deg) retained | 1 | >= 5 | NO |

**OUTCOME: HARD NULL.**

The predeclared success condition is not met. The Route C declared slice yields zero new evaluable low-cone or quasi-radial encounters beyond what was already catalogued.

---

## 4. Why the null occurred

The null has three interlocking causes:

**4a. Local data sparsity.** The Route C declared slice covers a large temporal range (2007 + 2010 + non-Aug-Oct 2008-2009) but the local data cache contains almost no data from this range. Only 3 unique date+probe combinations were found, and 2 of those had incomplete data (missing STATE and/or MOM files). The local cache was built during earlier pipeline development and concentrated on Aug-Oct 2008-2009 THD orbits.

**4b. The same structural Dp barrier.** Even if the local cache were complete, the dual-bin occupancy requirement (near >= 5%, background >= 1%) structurally excludes low-cone encounters under low Dp. The tranche-2 experience (3 low-cone candidates, all BG=0 at Dp 1.9-2.7 nPa) demonstrated this barrier. Route C could not overcome it because the barrier is physical (sheath width vs probe apogee), not a search-design artifact.

**4c. No data-acquisition campaign was executed.** Route C was constrained to locally cached data. A comprehensive Route C with full CDAWeb acquisition over the 2007-2010 archive might find additional encounters, but would face the same Dp barrier for low-cone evaluability.

---

## 5. Scope-match attestation

- **Declared slice:** 2007 full year + 2010 full year + 2008 non-Aug-Oct + 2009 non-Aug-Oct
- **Searched slice:** All locally cached THEMIS encounter data with timestamps in the declared slice
- **Declared = Searched:** YES
- **No convenience subsampling.** Every locally cached data point in the slice was evaluated.
- **Machine-readable manifest:** `reports/themis_conditioning/routeC/scope_manifest.json`

The scope match holds within the constraint of locally available data. The local cache does not contain the full 2007-2010 THEMIS archive. This is explicitly documented, not hidden.

---

## 6. What this null means

**It means:** Within the locally available data for the Route C declared slice, there are no new evaluable low-cone or quasi-radial encounters under the original Dn/EB measurement model.

**It does not mean:** That the full 2007-2010 THEMIS archive contains zero such encounters. A full CDAWeb acquisition campaign over the entire 2007-2010 archive was not executed. However, the structural Dp barrier documented in Phase 6A tranche-2 suggests that even a complete search would face the same evaluability constraint at low cone angles.

**It is:** A bounded archive-/apparatus-level null within the locally available data. Not a physics theorem about quasi-radial sheath structure.

---

## 7. Deterministic closure

Per the predeclared Route C execution plan:

**HARD NULL CONDITION MET. Phase 6 science is closed.**

| Component | Final status |
|---|---|
| Route A | Complete. Clean catalogue N=9. |
| Route B | Frozen sidecar. Modest yield. Not continued. |
| Route C | Complete. Bounded null. |
| Route D | Not executed. |
| Phase 6B | Blocked. Not opened. |
| Phase 6 science | **Closed.** |
| Project mode | **Writing-safe thesis return.** |

The broader upstream-conditioning question remains explicitly open. It is not answered negatively. A future study with full CDAWeb coverage or a wider-apogee mission could revisit it.

---

## 8. Exact strongest supportable Phase 6 statement

Phase 6 attempted upstream conditioning of the frozen THEMIS measurement model. Route A repaired the encounter catalogue (N=9 real after synthetic removal). Route B introduced an auxiliary inner-sheath descriptor with modest yield (3/5 inner-sheath gradients, recovered low-cone shows no depletion; frozen as sidecar, not interchangeable with Dn/EB). Route C scanned the locally available data in the unsearched 2007-2010 THEMIS archive for low-cone encounters evaluable under original Dn/EB; the scan found no new evaluable low-cone or quasi-radial encounters. The dual-bin occupancy requirement creates a Dp-dependent structural barrier that excludes the quasi-radial regime at the inner-probe apogee. The quasi-radial conditioning question remains open for future work with broader archive coverage or wider-apogee missions.

---

## 9. Exact strongest blocked overclaim

- "The quasi-radial regime is physically inaccessible" (it is inaccessible under the current apparatus and local data; not a general statement)
- "Phase 6 proves cone-angle dependence" (Phase 6 did not populate the quasi-radial bin)
- "Route C searched the full 2007-2010 archive" (it searched locally cached data only)
- Any threshold, label, class, detector, or occurrence language
- Any strengthening of frozen Phase 4B claims

---

## 10. Files produced

| File | Type |
|---|---|
| `docs/PHASE_6_ROUTEC_EXECUTION_PLAN.md` | Pre-registered plan |
| `docs/PHASE_6_ROUTEC_RESULT.md` | This document (bounded null) |
| `reports/themis_conditioning/routeC/scope_manifest.json` | Machine-readable scope manifest |
| `reports/themis_conditioning/routeC/selection_flow.md` | Human-readable selection flow |
| `reports/themis_conditioning/routeC/encounter_catalogue_routeC.json` | Full catalogue |
| `reports/themis_conditioning/routeC/encounter_catalogue_routeC.csv` | Tabular catalogue |
| `reports/themis_conditioning/routeC/routeC_summary.json` | Summary with hard stop |
| `scripts/phase6_routeC_scan.py` | Scan script |

## 11. Frozen anchors unchanged

Phase 4B six-pass bank, THE Sep 19 external recurrence, MMS branch freeze, Phase 5A/5B caseset sidecars — all intact and unmodified.
