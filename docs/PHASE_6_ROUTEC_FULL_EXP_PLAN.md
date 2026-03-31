# Phase 6 Route C FULL EXP — Execution Plan

**Date:** 2026-03-31
**Authority:** User-authorized red-level full-archive experiment.
**Status:** Pre-registered plan. Created before the scan.

---

## 1. Branch purpose

Final direct test: can the full 2007-2010 THEMIS near-subsolar dayside archive yield enough low-cone / quasi-radial encounters evaluable under original Dn/EB semantics to support a bounded conditioning comparison?

---

## 2. Preserved semantics

- Original Dn/EB only: Dn = median(density_near) / median(density_bg), EB = median(|B|_near) / median(|B|_bg)
- Bins: near [0.2, 0.4], background [0.6, 1.0] in normalized s-coordinate
- Boundary models: Shue 1998 (MP), Merka 2005 (BS)
- Upstream: OMNI HRO 1-min, encounter-averaged
- Encounter = unit of analysis
- Route B descriptors NOT used as substitutes

---

## 3. Declared full archive scope

**All THEMIS near-subsolar dayside data in the 2007-2010 interval** that can be processed into encounter-level products under the current measurement family, without convenience subsampling, with full archive acquisition via CDAWeb.

Specifically:
- **Years:** 2007, 2008, 2009, 2010
- **Probes:** THA, THB, THC, THD, THE (all five THEMIS probes)
- **Months:** July through November each year (the THEMIS dayside apogee season)
- **Geometry filter:** Near-subsolar (SZA <= 30 deg), X_GSM > 5 Re
- **Cadence:** Every day in the dayside season is checked for near-subsolar geometry
- **No convenience subsampling:** Every day, every probe

Note: THEMIS probes have dayside apogee roughly Jul-Nov. Outside this season the probes are on the nightside and cannot observe the dayside magnetosheath. Months outside Jul-Nov are excluded by orbital geometry, not by convenience.

THB and THC transitioned to ARTEMIS (lunar orbit) during 2010. They are included for 2007-2009 only where they have near-Earth orbits.

---

## 4. Exact search universe

For each (year, month, day, probe) combination in the declared scope:
1. Fetch THEMIS STATE ephemeris from CDAWeb
2. Check if the probe is in the dayside magnetosheath (X_GSM > 5 Re, SZA <= 30 deg, distance from MP consistent with sheath residence)
3. If yes, define a 6-hour encounter window centered on the near-subsolar apogee
4. Fetch FGM, MOM, OMNI for the encounter window
5. Compute s-mapping, occupancy, Dn/EB
6. Record in the catalogue

---

## 5. Exact cone bins

| Bin | Range | EXP target? |
|---|---|---|
| quasi-radial | cone < 30 deg | **Primary target** |
| low-cone | 30-45 deg | **Primary target** |
| intermediate | 45-60 deg | Context only |
| perpendicular | > 60 deg | Context only |

---

## 6. Exact inclusion / exclusion logic

An encounter is **retained** if:
1. SZA <= 30 deg (near-subsolar geometry)
2. Near-bin occupancy >= 5%
3. Background-bin occupancy >= 1%
4. Dn and EB both computable (non-null)
5. Not a synthetic fixture (dp != 2.0 or bz != 2.0 or ma != 8.0 or sza != 0.0)
6. Not obviously dominated by severe contamination in quicklook QC

An encounter is **excluded** with documented reason if any criterion fails.

---

## 7. Exact QC tracks

| QC field | Values |
|---|---|
| transition_cleanliness_qc | clean / mixed / unclear / not_assessed |
| disturbance_qc | undisturbed / uncertain / disturbed |
| boundary_motion_qc | stable / uncertain / dynamic |
| omni_context_quality_note | good / partial / poor |
| boundary_uncertainty_note | plausible / uncertain / suspect |

Audit fields only. Not labels or scores.

---

## 8. Exact deliverables

- `docs/PHASE_6_FULL_EXP_ACTIVATION.md`
- `docs/PHASE_6_ROUTEC_FULL_EXP_PLAN.md` (this document)
- `docs/PHASE_6_ROUTEC_FULL_EXP_RESULT.md`
- `reports/themis_conditioning/routeC_exp/scope_manifest.json`
- `reports/themis_conditioning/routeC_exp/selection_flow.md`
- `reports/themis_conditioning/routeC_exp/encounter_catalogue_routeC_exp.json`
- `reports/themis_conditioning/routeC_exp/encounter_catalogue_routeC_exp.csv`
- `reports/themis_conditioning/routeC_exp/routeC_exp_summary.json`

---

## 9. Exact hard stop / success logic

Evaluated once after the full scan:

**SUCCESS:** quasi-radial retained >= 1 OR low-cone (30-45 deg) retained >= 5
**HARD NULL:** quasi-radial retained = 0 AND low-cone retained < 5

---

## 10. Exact closure logic

| Outcome | Action |
|---|---|
| SUCCESS | Bounded comparison memo. Next red-level question: package into thesis or further Phase 6 science? Phase 6B still blocked. |
| HARD NULL | Bounded null memo. Phase 6 science finally closed after FULL EXP. Writing-safe thesis return. Broader question deferred to future work. Route B remains sidecar. Route D not opened. Phase 6B not opened. |
