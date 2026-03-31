# Phase 6 Route C — Execution Plan

**Date:** 2026-03-31
**Authority:** User-authorized red-level Route C execution.
**Status:** Pre-registered plan. Must be written before the scan.

---

## 1. Branch purpose

Route C is the decisive original-semantics test: can the unsearched 2007-2010 THEMIS near-subsolar dayside archive yield low-cone encounters evaluable under the original dual-bin Dn/EB measurement model?

If yes: bounded low-cone comparison package.
If no: bounded null, Phase 6 science closed, writing-safe return.

---

## 2. Exact preserved semantics

- **Original Dn/EB only.** Dn = median(density_near) / median(density_bg). EB = median(|B|_near) / median(|B|_bg). Near bin = s [0.2, 0.4]. Background bin = s [0.6, 1.0].
- **No Route B proxy.** Route B descriptors (Dn_near, D|B|_near) are frozen sidecar values only. They are NOT computed, referenced, or substituted within Route C core reporting.
- **Encounter-averaged boundaries.** Shue 1998 magnetopause, Merka 2005 bow shock, OMNI-propagated upstream.
- **Same occupancy screens.** Near-bin occupancy >= 5%, background-bin occupancy >= 1%.
- **Same SZA screen.** SZA <= 30 deg (near-subsolar).
- **No new measurement-model elements.**

---

## 3. Exact archive scope (declared slice)

The Route C declared slice is the complement of the Phase 6A tranche-1 and tranche-2 searched slice within the 2007-2010 THEMIS dayside archive:

| Sub-slice | Description |
|---|---|
| **2007** | All THEMIS (THA/THB/THC/THD/THE) near-subsolar dayside encounters, full year |
| **2010** | All THEMIS (THA/THB/THC/THD/THE) near-subsolar dayside encounters, full year |
| **2008 non-Aug-Oct** | All THEMIS near-subsolar dayside encounters in Jan-Jul, Nov-Dec 2008 |
| **2009 non-Aug-Oct** | All THEMIS near-subsolar dayside encounters in Jan-Jul, Nov-Dec 2009 |

The tranche-1 searched space was: all locally cached runs (Aug-Oct 2008-2009 primarily).
The tranche-2 searched space was: THD+THE, Aug-Oct 2008-2009, every 3rd day.
Route C covers everything in 2007-2010 that those tranches did NOT search.

**Data source constraint:** Route C uses only locally cached data (data_cache/normalized/ and runs/). No internet fetch. This means the Route C scan can only evaluate encounters for which local FGM, MOM, STATE, and OMNI data already exist. The scope manifest will record both the declared slice and the actually-available local data within that slice.

---

## 4. Exact cone bins

| Bin | Range | Route C target? |
|---|---|---|
| quasi-radial | cone < 30 deg | **YES — primary target** |
| low-cone | 30-45 deg | **YES — primary target** |
| intermediate | 45-60 deg | context only |
| perpendicular | > 60 deg | context only |

Route C core reporting focuses on quasi-radial and low-cone bins only.

---

## 5. Exact QC tracks

For every candidate/retained encounter, the following QC audit fields are assessed:

| QC field | What it checks | Values |
|---|---|---|
| transition_cleanliness_qc | Whether the near-MP gradient is clean or muddled | clean / mixed / unclear / not_assessed |
| disturbance_qc | Whether the encounter is dominated by transient/jet-like activity | undisturbed / uncertain / disturbed |
| boundary_motion_qc | Whether significant MP boundary motion contaminates the bin structure | stable / uncertain / dynamic |
| omni_context_quality_note | OMNI data quality and fill fraction | good / partial / poor |
| boundary_uncertainty_note | Whether Shue/Merka boundaries are plausible for this Dp/Bz | plausible / uncertain / suspect |

These are conservative audit fields only. They are NOT labels, scores, or exclusion rules.

An encounter is **routeC_core_usable** if:
1. Dn/EB computable under the original measurement model (near_occ >= 5%, bg_occ >= 1%)
2. NOT obviously dominated by severe transition/disturbance/boundary-motion contamination

---

## 6. Exact stop criteria

After one full scan, evaluate the hard stop exactly once:

**SUCCESS CONDITION:**
- quasi-radial (cone < 30 deg) retained >= 1
- OR low-cone (30-45 deg) retained >= 5

**HARD NULL CONDITION:**
- quasi-radial retained = 0 AND low-cone retained < 5

---

## 7. Exact deliverables

| # | File | Type |
|---|---|---|
| 1 | `docs/PHASE_6_ROUTEC_EXECUTION_PLAN.md` | This document |
| 2 | `docs/PHASE_6_ROUTEC_RESULT.md` | Bounded comparison or bounded null memo |
| 3 | `reports/themis_conditioning/routeC/scope_manifest.json` | Machine-readable scope/search manifest |
| 4 | `reports/themis_conditioning/routeC/selection_flow.md` | Human-readable selection flow |
| 5 | `reports/themis_conditioning/routeC/encounter_catalogue_routeC.json` | Full encounter catalogue |
| 6 | `reports/themis_conditioning/routeC/encounter_catalogue_routeC.csv` | Tabular encounter catalogue |
| 7 | `reports/themis_conditioning/routeC/routeC_summary.json` | Summary with hard stop evaluation |

---

## 8. Exact non-claims

- Route C results are descriptive only.
- No thresholds, labels, classes, detector language.
- No occurrence-rate claims or causal language.
- A Route C null is a bounded archive-/apparatus-level null within the declared slice, not a physics theorem about quasi-radial sheath structure.
- Route B descriptors are NOT used as substitutes for Dn/EB.
- Phase 4B frozen claims are not altered.

---

## 9. Deterministic closure logic

| Outcome | Action |
|---|---|
| SUCCESS | Write bounded comparison memo. Update control files. Phase 6B still blocked. Next red-level question: further Phase 6 science or writing-safe integration? |
| HARD NULL | Write bounded null memo. Phase 6 science closed. Project returns to writing-safe thesis mode. Broader upstream-conditioning question remains explicitly open, not answered negatively. Route B remains frozen sidecar. Route D not executed. Phase 6B not opened. |
