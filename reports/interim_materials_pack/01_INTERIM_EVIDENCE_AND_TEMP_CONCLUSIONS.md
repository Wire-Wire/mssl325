# Interim Materials Pack — Evidence and Temporary Conclusions

> **How to use this file:** This is the evidence-focused companion to 00_INTERIM_MASTER.md. It walks through each major workstream with exact numbers, identifies what evidence exists, what temporary conclusions are supportable, and where the evidence lives. Each section is labelled with its scientific status. A reader opening only this file should understand what the project found, to what confidence level, and where to find the supporting materials.

---

## Project orientation

This project studies the dayside Plasma Depletion Layer (PDL) using THEMIS encounter-level descriptors (Dn = near-bin / background-bin density ratio; EB = same for |B|) under a normalised magnetosheath coordinate (s = d_MP / (d_MP + d_BS)). A parallel MMS branch attempted multi-spacecraft thickness measurement. The project aims toward SMILE/SXI mission priors, though that translation stage has not been reached.

**Current state:** THEMIS comparator bank frozen (Phase 4B). Phase 6 full-archive exploration packaged as a bounded sidecar. MMS branch frozen with no reportable thickness. Writing-safe thesis integration active.

---

## A. THEMIS comparator-bank evidence (CURRENT SUPPORTED)

### A1. What exists

A measurement model using the s-coordinate, Shue 1998 magnetopause, Merka 2005 bow shock, and encounter-averaged OMNI upstream was applied to nine THEMIS-D (THD) comparator windows from seven independent orbital passes (Aug–Oct 2008 and Sep–Oct 2009). All encounters are near-subsolar (SZA 4–22 deg) under compressed-sheath conditions (Dp > 3 nPa). The model computes encounter-level medians of density and |B| in near ([0.2, 0.4] in s) and background ([0.6, 1.0] in s) bins, producing Dn (density ratio) and EB (|B| ratio).

### A2. What it shows

After interval-level confounder audit (leave-spike-out sensitivity analysis):

| Category | Passes | Dn range | EB range | Notes |
|---|---|---|---|---|
| Clean core | P2, P4, P5, P6 | 0.94–2.31 | 0.80–1.96 | Metrics robust under spike removal (max delta Dn 0.22, max delta EB 0.02) |
| Cautious | P1, P3 | 0.12–0.39 | 1.96–2.49 | P1: density CV 0.93; P3: EB spike-dependent (delta 0.50) |
| Excluded | P7 | 2.19 (collapses to 0.67) | 4.22 (collapses to 0.97) | Spike-dominated; 35% spike fraction |
| External recurrence | THE Sep 19 | 0.76 | 2.12 | Cross-probe; not admitted to bank; membership 84% |

**Key derived observations:**
- Dn and EB are approximately inversely related across the bank (Spearman r = -0.45, p = 0.22, N = 9 — not statistically significant but qualitatively consistent).
- rho(n, B) trend anti-correlation is negative for all passes (range -0.91 to -0.46) — but this universality means rho has no discriminative power within this bank.
- Duration variants (6h vs 8h on same pass) are consistent: within-pass Dn spread 0.50 vs between-pass range 1.80.
- Effective independent N = 7 (not 9, because 2 passes have duration variants).

### A3. Temporary conclusions

| Conclusion | Status | Confidence caveat |
|---|---|---|
| The measurement model produces operationally distinguishable Dn/EB across 6 THD passes | **CURRENT SUPPORTED** | Limited to compressed-sheath THD conditions |
| Clean-core Dn spans 0.94–2.31, EB 0.80–1.96 | **CURRENT SUPPORTED** | Confounder-tested |
| Sub-unity Dn recurs on independent cross-probe (THE Sep 19, Dn = 0.76) | **CURRENT SUPPORTED** | THE Sep 19 is not less caveated than P1/P3 |
| Dn < 0.5 evidence is cautious-only (P1: 0.12, P3: 0.39) | **CURRENT SUPPORTED** | Not independently recurred; unresolvable under frozen model |
| No physical identification of any encounter as containing a PDL | **CURRENT SUPPORTED (ceiling)** | Intentional design choice |

### A4. What is explicitly NOT supported

- Any threshold, label, class, or detector semantics
- Physical identification of encounters as PDL-positive or PDL-negative
- Generalisation beyond compressed-sheath THD conditions (Dp > 3 nPa, SZA < 22 deg)
- Population-level occurrence rates
- The claim that Dn < 1 or EB > 1 "indicates" a PDL

### A5. Source files

- `selected_source_md/THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` — frozen evidence ledger
- `selected_source_md/PHASE_4B_RESULTS_FREEZE.md` — strongest claims and non-claims
- `selected_reports_and_data/bank_report.md` — full evidence matrix
- `selected_reports_and_data/phase3a_dneb_comparison.md` — descriptive comparison
- `selected_reports_and_data/phase4a_lowdn_recurrence_report.md` — cross-probe recurrence
- `selected_reports_and_data/phase4b_results_freeze_report.md` — formal freeze report
- `selected_figures/phase3a_dneb_comparison.png` — Dn vs EB scatter (Figure T1)
- `selected_figures/phase4a_lowdn_recurrence.png` — recurrence plot (Figure T2)
- `selected_figures/cross_pass_summary.png` — bank summary

---

## B. Phase 5A/5B caseset sidecars (EDITORIAL / ILLUSTRATIVE)

### B1. What exists

Eight cases from the frozen seed were screened with operational filters (SZA, clock angle, non-quasi-radial, upstream stability). Each was reviewed for three sheath-side indicators: density decrease (n down), magnetic field increase (|B| up), and beta decrease (beta down) near the magnetopause.

### B2. What it shows

| Clock-angle bin | Cases screened | Atlas-usable | Review statuses |
|---|---|---|---|
| < 60 deg | 1 | 0 | P2: not convincing |
| 60–120 deg | 2 | 2 | P5: clear, P6: ambiguous |
| > 120 deg | 5 | 3 | P3, P4, EXT: clear; P7: not convincing; P1: screen fail |
| **Total** | **8** | **5** | 4 clear, 1 ambiguous, 2 not convincing, 1 screen fail |

Four of five atlas-usable cases show all three indicators jointly present. P6 (ambiguous) shows |B| up and beta down but not density down.

### B3. Temporary conclusions

| Conclusion | Status |
|---|---|
| 5 atlas-usable cases available for appendix illustration | **EDITORIAL SIDECAR** |
| Atlas-usable cases appear only in 60–120 deg and > 120 deg clock bins | **EDITORIAL SIDECAR** |
| Review statuses are NOT physical classes or confidence measures | **CEILING** |

### B4. Source files

- `selected_source_md/THEMIS_CASESET.md` — full case atlas
- `selected_source_md/PHASE_5B_CASESET_DESCRIPTIVE_PASS.md` — grouped inventory
- `selected_reports_and_data/caseset_summary.json` — machine-readable metadata
- `selected_figures/P3_20090913_crossing.png`, `P4_20090920_crossing.png`, `EXT_20080919_crossing.png` — crossing quicklooks

---

## C. Phase 6 full-archive exploration (BOUNDED SIDECAR)

### C1. What exists

A full-archive scan of the entire THEMIS near-subsolar dayside dataset (2007–2025, all five probes THA/THB/THC/THD/THE, SZA < 30 deg, 8 < r < 25 Re) using CDAWeb acquisition processed 6903 qualifying days. Under original Dn/EB semantics (unchanged bin definitions and occupancy thresholds), 757 encounters were retained as evaluable.

### C2. What it shows

| Cone-angle bin | N | Dn median | Dn IQR | EB median | EB IQR | Dp median (nPa) |
|---|---|---|---|---|---|---|
| quasi-radial (< 30 deg) | 28 | 0.89 | [0.06, 1.35] | 2.42 | [2.01, 3.16] | 1.65 |
| low-cone (30–45 deg) | 89 | 0.80 | [0.07, 1.17] | 2.55 | [1.56, 3.84] | 1.53 |
| intermediate (45–60 deg) | 199 | 0.79 | [0.12, 1.14] | 2.38 | [1.50, 4.09] | 2.25 |
| perpendicular (> 60 deg) | 441 | 0.74 | [0.14, 1.24] | 2.39 | [1.55, 4.15] | 2.44 |

Dn medians are broadly similar across all cone bins (0.74–0.89). The Dn/EB range is much wider than Phase 4B (Dn 0.01–8+, EB 0.7–15+ vs Phase 4B Dn 0.12–2.31, EB 0.80–4.22).

**Cross-probe QC gate (2007–2025, 757 encounters):** 208 same-date multi-probe overlap groups tested. Group consistency (< 1 dex Dn spread): 78%. Low-cone/quasi-radial groups with order-of-magnitude Dn disagreement: 9 of 41 (22%). The QC gate formal verdict was FAIL under absolute-count threshold (>= 3 OOM groups), but the rate-based consistency (78%) was the same as or better than the 2007–2010 subset that formally PASSED.

**Cross-cycle verification:** Two independent orbital cycles (2007–2010 and 2016–2019) both populate all four cone bins, confirming the result is not epoch-specific.

### C3. Temporary conclusions

| Conclusion | Status |
|---|---|
| The quasi-radial and low-cone bins are fillable under original Dn/EB semantics | **BOUNDED SIDECAR** |
| Cross-probe comparability with frozen THD bank is not validated (78% agreement, 22% OOM) | **BOUNDED SIDECAR (caveat)** |
| Low-cone/QR encounters come from THA/THB/THC at lower Dp (1.5–1.7 nPa) — probe and Dp are entangled with cone bin | **BOUNDED SIDECAR (caveat)** |
| Phase 6 does NOT validate, extend, or strengthen Phase 4B | **CEILING** |
| Direct physical comparison across cone-angle regimes is deferred | **OPEN QUESTION** |

### C4. NOT SAFE TO PROMOTE

- "Phase 6 proves cone-angle-dependent depletion"
- "Low-cone encounters show / lack PDL signatures"
- "The full archive confirms cone-angle dependence"
- Any occurrence rate or threshold language

### C5. Source files

- `selected_source_md/PHASE_6_FULL_EXP_FREEZE.md` — freeze package note
- `selected_source_md/PHASE_6_MASTER_SUMMARY.md` — complete Phase 6 history
- `selected_source_md/PHASE_6_EXTRA_QC_GATE_REPORT.md` — cross-probe QC (2007–2025)
- `selected_reports_and_data/routeC_exp_summary.json` — FULL EXP summary (148 encounters)
- `selected_reports_and_data/routeC_extra_summary.json` — EXTRA summary (757 encounters)
- `selected_reports_and_data/crossprobe_qc_gate_summary_extra.json` — QC gate JSON
- `selected_reports_and_data/themis_archive_summary.json` — full archive stats

---

## D. MMS thickness branch evidence (CURRENT SUPPORTED — methods/limitation)

### D1. What exists

A methods scaffold for multi-spacecraft thickness measurement was implemented. Eleven MMS Phase 1 dayside events were screened; three primaries identified; two advanced to readiness (P1, P3). One thickness attempt was completed (P1).

### D2. What it shows

**Screening (11 events):**

| Candidate | Date | SZA | Dp (nPa) | Verdict |
|---|---|---|---|---|
| MMS-P1 | 2015-11-12 | 18 deg | 1.1 | Primary — ADVANCE |
| MMS-P2 | 2015-12-12 | 11 deg | 2.0 | Primary — HOLD |
| MMS-P3 | 2016-12-26 | 6 deg | 2.6 | Primary — ADVANCE |
| MMS-R1 | 2017-01-05 | 7 deg | 2.6 | Reserve |
| 7 others | — | — | — | Failed (no sustained gradient) |

**P1 attempt outcome:** A clear near-MP gradient was observed (|B| drops ~28 nT, density drops ~10 cm^-3 over ~5 minutes) on all four MMS spacecraft. However:
- MVA normal: poorly constrained (eigenvalue ratio 3.0; 70 deg from expected direction)
- Timing normal: degenerate (10 km separation, 1118 s delay timescale)
- Gradient thickness: dominated by noise at 10 km separation
- **Scale mismatch ratio: ~100x** (10 km tetrahedron vs ~750–3750 km gradient)
- **Verdict: do_not_report**

**Basis reset conclusion:** MMS Phase 1 (~10 km) and Phase 2 (~25 km) tetrahedra are both structurally too small. A revised reportability criterion was proposed: gradient spatial scale must be within ~10x of tetrahedron separation.

### D3. Temporary conclusions

| Conclusion | Status |
|---|---|
| Near-MP gradient exists and is observable on four MMS spacecraft | **CURRENT SUPPORTED** |
| Scale mismatch (~100x) prevents defensible thickness estimation | **CURRENT SUPPORTED** |
| MMS Phase 2 separations insufficient (2–3x improvement only) | **CURRENT SUPPORTED** |
| This is a structural configuration limitation, not a data or methods failure | **CURRENT SUPPORTED** |
| Documented negative result is a legitimate thesis contribution | **CURRENT SUPPORTED** |

### D4. Source files

- `selected_source_md/MMS_BRANCH_FREEZE.md` — branch freeze with thesis wording
- `selected_source_md/MMS_P1_FIRST_THICKNESS_ATTEMPT.md` — full P1 analysis
- `selected_source_md/MMS_BASIS_RESET.md` — root-cause diagnosis
- `selected_reports_and_data/mms_p1_first_thickness_report.md` — evidence report
- `selected_reports_and_data/mms_basis_reset_report.md` — basis-reset report
- `selected_reports_and_data/mms_event_shortlist_report.md` — shortlist
- `selected_reports_and_data/mms_event_package_readiness_report.md` — readiness
- `selected_reports_and_data/p1_thickness_attempt_summary.json` — machine-readable
- `selected_figures/p1_evidence_panel.png` — four-spacecraft evidence panel
- `selected_figures/mms_20151112_quicklook.png` — P1 quicklook

---

## E. Data infrastructure and archive assets

### E1. THEMIS archive cache (2007–2025)

| Asset | Count |
|---|---|
| Monthly STATE ephemeris files | 1135 |
| Qualifying near-subsolar days processed | 6903 |
| Per-encounter JSON products | 6118 |
| Unique retained (Dn/EB evaluable) | 757 |
| Disk size | ~1.6 GB |

Geometry screening: X_GSM > 5 Re, SZA < 30 deg, 8 < r < 25 Re. All five THEMIS probes across three orbital cycles (2007–2010, 2016–2019, 2025+) plus ARTEMIS perigee passes.

### E2. Pipeline code

31 Python source files in `src/pdl_pilot/` covering live data fetch (CDAWeb/cdasws), fill-value masking, s-mapping, boundary models, metric computation, preflight gates, QC, and report generation. 124 tests passing.

### E3. Source files

- `selected_source_md/THEMIS_ARCHIVE_DATA_GUIDE.md` — complete usage guide
- `selected_reports_and_data/themis_archive_summary.json` — global stats
