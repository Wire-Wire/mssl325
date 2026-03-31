# Interim Materials Pack — Master Overview

> **How to use this file:** This is the single-file entry point for preparing an interim report. It provides a high-level but concrete overview of the entire project: what was done, what was found, what the limitations are, and where to find everything. The two companion files (01_INTERIM_EVIDENCE_AND_TEMP_CONCLUSIONS.md and 02_INTERIM_HISTORY_DECISIONS_AND_CHANGES.md) provide deeper evidence-focused and history-focused detail. All three files are intentionally self-contained and partially overlapping; each can be read independently.

---

## 1. Project overview

**Title:** Revisiting the Dayside Plasma Depletion Layer with THEMIS and MMS: Occurrence, Thickness, and SMILE/SXI-Relevant Density Priors

**One-sentence summary:** This project investigates whether a boundary-adjacent density-depletion / magnetic-pileup structure (the Plasma Depletion Layer, or PDL) can be isolated in controlled THEMIS dayside magnetosheath encounter data, whether MMS multi-spacecraft measurements can convert the statistical signature into a physical thickness, and whether the results can be translated into compact priors for the forthcoming SMILE/SXI soft X-ray telescope.

**Project identity:** A four-part research programme covering (1) controlled THEMIS detection, (2) confounder handling and robustness, (3) MMS thickness measurement, and (4) SMILE/SXI mission translation. The work is measurement-conscious, encounter-level, upstream-IMF-agnostic for detection, and explicitly conservative — preferring defensibility over complexity.

**Source:** `RP/internal_master_research_blueprint_PDL_SMILE.md`

---

## 2. Motivation and scientific problem

The plasma depletion layer (PDL) is a boundary-adjacent structure in the dayside magnetosheath where magnetic pressure rises and plasma density drops as the solar wind flow stagnates near the magnetopause. Classical theory (Zwan and Wolf 1976; Crooker et al. 1979) and later observational and MHD work (Anderson et al. 1997; Wang et al. 2004) support the basic physical picture. However, in modern large databases, the same state-space signature can be mimicked by spatial mixing, mapping uncertainty, magnetosheath jets, wave trains, foreshock variability, and boundary motion. The central scientific problem is therefore not whether the PDL concept is interesting, but whether a PDL-like structure can be isolated under controlled, auditable conditions.

The practical motivation includes the upcoming SMILE mission, whose Soft X-ray Imager (SXI) will observe the magnetopause and cusps in soft X-rays. SXI signal interpretation depends on knowing the density distribution in the near-magnetopause region. If the PDL is real and recurrent, it changes the expected density profile and thus the soft X-ray emission — making controlled PDL statistics directly mission-relevant.

---

## 3. Research questions and objectives

The project has four primary research questions:

1. **Detection:** Can a boundary-adjacent, layer-like PDL be detected in a controlled THEMIS dayside near-subsolar encounter sample without circular IMF assumptions?
2. **Robustness:** Does the signal survive measurement-model criticism, confounder audit, and selection-function analysis?
3. **Thickness:** Can a small number of MMS cases convert the statistical THEMIS signature into a physical thickness with uncertainty?
4. **Translation:** Can the resulting occurrence and depletion statistics be translated into compact, conditional priors for SMILE/SXI forward modelling?

As of the current stage, Questions 1 and 2 have been addressed through a frozen THEMIS comparator bank (Phase 4B). Question 3 was attempted but blocked by a structural scale mismatch (MMS branch frozen). Question 4 remains entirely deferred.

---

## 4. Work completed so far

### 4a. THEMIS comparator bank (Phases 1–4B) — CLAIM-BEARING

A measurement model was designed using a normalised magnetosheath coordinate (s = d_MP / (d_MP + d_BS), Shue 1998 magnetopause, Merka 2005 bow shock) with dual-bin near/background architecture. The encounter is the statistical unit, not the crossing. Nine measurement-model-valid comparator windows were produced from seven independent THD orbital passes (2008–2009) under near-subsolar dayside geometry (SZA 4–22 deg) and compressed-sheath conditions (Dp > 3 nPa).

After a multi-stage audit (window bank validation, shuffled-s falsification, interval-level confounder closure, P1/P3 retention audit, independent recurrence test), the bank was frozen at Phase 4B:
- **Clean core:** 4 passes (P2, P4, P5, P6) with Dn 0.94–2.31, EB 0.80–1.96, metrics robust under spike removal.
- **Cautious:** 2 passes (P1: Dn = 0.12, P3: Dn = 0.39) with documented caveats (density noise, EB spike sensitivity).
- **Excluded:** 1 pass (P7: spike-dominated, metrics collapse under sensitivity analysis).
- **External recurrence:** THE Sep 19 2008 (Dn = 0.76, cross-probe, not admitted to main bank).

**Strongest supportable claim:** The frozen measurement model produces operationally distinguishable Dn/EB outputs across six independent THD passes. Sub-unity Dn recurs on an independent cross-probe. The cautious-only low-Dn region (Dn < 0.5) is not independently recurred.

**Source:** `docs/THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md`, `docs/PHASE_4B_RESULTS_FREEZE.md`

### 4b. Phase 5A/5B editorial sidecars — ILLUSTRATIVE ONLY

Eight cases were screened from the frozen seed. Four were reviewed as clear (P3, P4, P5, EXT), one as ambiguous (P6), two as not convincing (P2, P7), and one failed screening (P1, quasi-radial). These were grouped by clock-angle bin. Atlas-usable cases appear only in the 60–120 deg and >120 deg bins; the sole < 60 deg case was not convincing. These are editorial packaging, not scientific confidence classes.

**Source:** `docs/THEMIS_CASESET.md`, `docs/PHASE_5B_CASESET_DESCRIPTIVE_PASS.md`

### 4c. Phase 6 full-archive upstream-conditioning exploration — BOUNDED SIDECAR

Phase 6 asked whether the previously empty quasi-radial (cone < 30 deg) and low-cone (30–45 deg) IMF regimes could be populated under original Dn/EB semantics. After multiple route attempts (6A pilot, Route A repair, Route B inner-sheath descriptor sidecar, Route C local-only null, Route C FULL EXP with CDAWeb acquisition), a full-archive scan across all five THEMIS probes (2007–2025) found 757 evaluable encounters: 28 quasi-radial, 89 low-cone, 199 intermediate, and 441 perpendicular.

A cross-probe QC gate found that same-day multi-probe groups agree within one order of magnitude in Dn in approximately 78% of cases, but the low-cone and quasi-radial bins are dominated by non-THD probes at lower Dp (median 1.5–1.7 nPa vs Phase 4B's > 3 nPa). Cross-probe comparability with the frozen THD bank is not validated.

**Strongest supportable claim:** The previously empty cone-angle bins are fillable under the original measurement-model family. Phase 6 does NOT validate, extend, or strengthen Phase 4B.

**Source:** `docs/PHASE_6_FULL_EXP_FREEZE.md`, `docs/PHASE_6_MASTER_SUMMARY.md`

### 4d. MMS thickness branch — FROZEN, NO REPORTABLE THICKNESS

A methods scaffold was designed for MMS multi-spacecraft thickness measurement using timing-based and gradient-scale approaches. Eleven MMS Phase 1 dayside events were screened; three primaries were shortlisted (MMS-P1, P2, P3); two advanced to readiness (P1, P3). The first thickness attempt on MMS-P1 (2015-11-12) resulted in a **do_not_report** outcome: the MMS Phase 1 tetrahedron separation (~10 km) is approximately 100 times smaller than the observed near-magnetopause gradient spatial scale (~750–3750 km). Both timing-based and gradient-scale thickness methods failed structurally. This is not a data-quality failure but a fundamental scale mismatch.

A basis reset confirmed the root cause as a missing separation-scale-match eligibility gate. MMS Phase 2 separations (~25 km) offer only a 2–3x improvement, which is insufficient. The branch was frozen as a documented negative methodological result.

**Strongest supportable claim:** The scale mismatch between MMS Phase 1 tetrahedron separation and typical near-MP gradient scales prevents defensible thickness estimation. This is a structural limitation of the current MMS configuration for extended gradient layers, not a failure of the methods or data.

**Source:** `docs/MMS_BRANCH_FREEZE.md`, `docs/MMS_P1_FIRST_THICKNESS_ATTEMPT.md`, `docs/MMS_BASIS_RESET.md`

### 4e. Local data infrastructure

A full THEMIS encounter archive cache was built covering 2007–2025, all five probes, all months, with 1135 monthly STATE ephemeris files, 6903 qualifying near-subsolar days, and 6118 per-encounter JSON products. This infrastructure supports reproducibility and any future analysis without re-fetching from CDAWeb.

**Source:** `docs/THEMIS_ARCHIVE_DATA_GUIDE.md`, `data_cache/themis_archive/summary.json`

---

## 5. Current supported results / temporary conclusions

| ID | Statement | Status | Source |
|---|---|---|---|
| R1 | The frozen measurement model produces operationally distinguishable Dn/EB across 6 independent THD passes | **CURRENT SUPPORTED** | Phase 4B |
| R2 | Clean-core Dn spans 0.94–2.31; EB spans 0.80–1.96 | **CURRENT SUPPORTED** | Phase 4B |
| R3 | Sub-unity Dn recurs on independent cross-probe (THE Sep 19, Dn = 0.76) | **CURRENT SUPPORTED** | Phase 4A/4B |
| R4 | The Dn < 0.5 region is cautious-only, not independently recurred | **CURRENT SUPPORTED** | Phase 3B/4B |
| R5 | The quasi-radial and low-cone bins are fillable under original Dn/EB (757 encounters, 28 QR, 89 LC) | **BOUNDED SIDECAR** | Phase 6 |
| R6 | Cross-probe comparability with frozen THD bank is not validated (78% same-day agreement, 22% OOM) | **BOUNDED SIDECAR** | Phase 6 QC gate |
| R7 | MMS Phase 1 tetrahedron is structurally too small for typical near-MP gradient thickness | **CURRENT SUPPORTED (methods/limitation)** | MMS branch |
| R8 | No physical identification, no thresholds, no labels, no detector semantics defined | **CURRENT SUPPORTED (ceiling)** | All phases |

---

## 6. Major limitations / unresolved issues

1. **Single-probe dominance in Phase 4B:** The frozen bank is THD-only (2008–2009). Generalization to other probes, seasons, or solar-wind conditions is not supported.
2. **Compressed-sheath bias:** All Phase 4B encounters have Dp > 3 nPa. Lower-Dp sheath conditions are structurally excluded.
3. **Unresolved confounders:** Transient, mixing, and boundary-motion flags remain UNKNOWN for all passes. Maximum QC grade is Silver.
4. **Cross-probe comparability:** Phase 6 low-cone/QR encounters come from different probes (THA/THB/THC) at different Dp. The ~22% order-of-magnitude disagreement rate in cross-probe overlap groups is unresolved.
5. **MMS scale mismatch:** No defensible thickness. Phase 2 separations insufficient. Resumption requires scale-matched targets.
6. **No occurrence layer:** No detection bundle, no occurrence rates, no population-level statistics exist.
7. **No mission translation:** SMILE/SXI priors not constructed.

---

## 7. MMS branch summary, failure path, and lessons

The MMS thickness branch progressed through five stages before being frozen:

1. **Methods scaffold** — Defined timing-based and gradient-scale thickness definitions, normal-estimation hierarchy, uncertainty ledger, and quality grading (Gold/Silver/Bronze/do_not_report).
2. **Event shortlist** — Screened 11 MMS Phase 1 dayside passes (2015–2017). Three primaries (P1, P2, P3) and one reserve (R1) identified. Seven failed due to absence of sustained near-MP gradient.
3. **Readiness audit** — P1 and P3 advanced; P2 held (too far from magnetopause, no clear density transition).
4. **P1 thickness attempt** — Event 2015-11-12, Dp 1.1 nPa, SZA 18 deg. Clear four-spacecraft gradient observed (|B| drops 28 nT, density drops 10 cm^-3 over ~5 min). However: MVA normal poorly constrained (eigenvalue ratio 3.0, direction 70 deg from expected); timing normal degenerate (10 km separation vs 1118 s delay); gradient computation dominated by noise at 10 km separation. **Result: do_not_report.**
5. **Basis reset** — Root cause: ~100x scale mismatch between tetrahedron (~10 km) and gradient (~750–3750 km). Phase 2 separations (~25 km) improve by only 2–3x. Revised reportability criterion: gradient scale must be within ~10x of tetrahedron separation. **Recommendation: pause branch.**

**Lesson:** The gradient is real and methods are sound. The blocker is configuration: MMS Phase 1/2 is structurally too small for extended near-MP gradients. This is a legitimate negative methodological result for thesis integration.

**Sources:** `docs/MMS_BRANCH_FREEZE.md`, `docs/MMS_P1_FIRST_THICKNESS_ATTEMPT.md`, `docs/MMS_BASIS_RESET.md`, `reports/mms_p1_first_thickness/p1_evidence_panel.png`

---

## 8. What remains to be done

| Item | Status | Notes |
|---|---|---|
| Thesis THEMIS results chapter | Ready to write | Use Phase 4B frozen block + Phase 6 sidecar |
| Thesis MMS methods/limitation section | Ready to write | Use MMS freeze doc |
| Thesis discussion / limitations | Ready to write | Combine Phase 4B caveats + Phase 6 caveats + MMS |
| Thesis future-work section | Ready to write | Cross-probe validation, Dp-controlled comparison, MMS scale-matched targets, SMILE translation |
| Cross-probe calibration validation | NOT DONE | Required before Phase 6 can be promoted beyond sidecar |
| Dp-controlled sub-stratification | NOT DONE | Required to disentangle probe-access from cone-angle effects |
| Occurrence / detection bundle | NOT DONE | Phase 6B never opened |
| SMILE/SXI translation | NOT DONE | Awaits occurrence layer |

---

## 9. Key source map

### Claim-bearing (cite for results)

| Document | What it provides |
|---|---|
| `docs/THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` | THEMIS frozen evidence ledger, supportable statements |
| `docs/PHASE_4B_RESULTS_FREEZE.md` | Strongest claims, non-claims, safe sentences |
| `docs/MMS_BRANCH_FREEZE.md` | MMS freeze with thesis-safe wording |

### Bounded sidecars (cite with ceiling)

| Document | What it provides |
|---|---|
| `docs/PHASE_6_FULL_EXP_FREEZE.md` | Phase 6 package note, caveats, thesis placement |
| `docs/PHASE_6_THESIS_INSERTION_PACK.md` | Pasteable thesis prose for Phase 6 |
| `docs/THEMIS_CASESET.md` | Phase 5A case atlas (illustration only) |
| `docs/PHASE_5B_CASESET_DESCRIPTIVE_PASS.md` | Phase 5B grouped inventory (illustration only) |

### Key figures

| Figure | Content | Location |
|---|---|---|
| Dn vs EB comparison | 6-pass comparator scatter | `selected_figures/phase3a_dneb_comparison.png` |
| Independent recurrence | THE Sep 19 in Dn/EB space | `selected_figures/phase4a_lowdn_recurrence.png` |
| Cross-pass summary | Occupancy, sensitivity, bank overview | `selected_figures/cross_pass_summary.png` |
| MMS-P1 evidence panel | Four-spacecraft gradient observation | `selected_figures/p1_evidence_panel.png` |
| THEMIS caseset examples | P3, P4, EXT crossing quicklooks | `selected_figures/P3_*.png`, `P4_*.png`, `EXT_*.png` |

### Data products

| File | What it provides |
|---|---|
| `selected_reports_and_data/encounter_catalogue_clean.json` | Phase 6 clean N=9 catalogue |
| `selected_reports_and_data/routeC_exp_summary.json` | FULL EXP 148-encounter summary |
| `selected_reports_and_data/routeC_extra_summary.json` | EXTRA 757-encounter summary |
| `selected_reports_and_data/themis_archive_summary.json` | Full 2007–2025 archive cache stats |
| `selected_reports_and_data/p1_thickness_attempt_summary.json` | MMS-P1 attempt outcome |
| `selected_reports_and_data/caseset_summary.json` | Phase 5A caseset metadata |
