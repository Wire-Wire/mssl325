# Phase 6 — Thesis Insertion Pack

> **Purpose:** Ready-to-paste thesis prose for Phase 6, with placement guidance, limitations, and wording guardrails. All text below is writing-safe under the current frozen ceiling.

---

## A. Role statement

Phase 6 is a **bounded descriptive-methodological sidecar** placed after the frozen Phase 4B comparator bank in the thesis. Phase 4B remains the sole claim-bearing anchor for all THEMIS near-magnetopause descriptor results. Phase 6 does not strengthen, extend, or validate Phase 4B claims. No occurrence, threshold, class, detector, or mission-prior interpretation is supported by Phase 6.

---

## B. Main-text insertion block

> **Placement:** Results chapter, after the Phase 4B comparator-bank subsection and the Phase 5A/5B editorial sidecars. Suggested subsection title: *"Full-archive cone-angle regime accessibility"* or equivalent.

The Phase 4B comparator bank draws exclusively from THD during the 2008--2009 dayside season under compressed-sheath conditions (Dp > 3~nPa), leaving the quasi-radial (cone < 30\textdegree) and low-cone (30--45\textdegree) IMF regimes empty. To assess whether these regimes are accessible under the same measurement family, a full-archive scan was conducted across all five THEMIS probes (THA, THB, THC, THD, THE) spanning 2007--2025, covering every month and every day without convenience subsampling, with a near-subsolar geometry requirement (SZA $\leq$ 30\textdegree, 8 < r < 25~R\textsubscript{E}).

Under the original Dn/EB semantics (near-bin [0.2, 0.4] and background-bin [0.6, 1.0] occupancy thresholds unchanged), 757 encounters were retained as evaluable. Of these, 28 fall in the quasi-radial bin and 89 in the low-cone bin, with 199 intermediate and 441 perpendicular. The previously empty bins are therefore fillable under the original measurement-model family when the full multi-probe archive is searched.

However, the newly populated low-cone and quasi-radial encounters come primarily from THA, THB, and THC at lower dynamic pressures (median Dp $\approx$ 1.5--1.7~nPa) than the Phase 4B bank. Cross-probe comparability with the frozen THD-dominated bank has not been validated, and a direct physical comparison of Dn/EB across cone-angle regimes is deferred to future work.

---

## C. Limitations paragraph

> **Placement:** Discussion chapter, limitations subsection; or as a closing paragraph of the Phase 6 results subsection.

Several caveats constrain the interpretability of the expanded encounter set. The quasi-radial and low-cone encounters are drawn primarily from THA, THB (ARTEMIS perigee passes post-2010), and THC, probes whose orbital characteristics, calibration histories, and spatial sampling differ from THD. These encounters occupy a systematically lower dynamic-pressure regime (Dp $\approx$ 0.8--2.5~nPa) than the Phase 4B bank (Dp > 3~nPa), meaning that boundary-model standoff distances, sheath width, and the physical content of the near and background s-bins all shift. A cross-probe QC assessment found that same-day multi-probe overlap groups agree within one order of magnitude in Dn in approximately 78\% of cases, but approximately 22\% of low-cone and quasi-radial overlap groups exhibit order-of-magnitude Dn disagreements of unresolved origin. Furthermore, low-cone IMF conditions are associated with a transient-rich quasi-parallel foreshock environment, and OMNI-propagated upstream context carries additional representativeness uncertainty under such conditions. These factors collectively prevent direct cross-regime physical comparison at the present stage.

---

## D. Discussion / future-work bridge

> **Placement:** Discussion chapter, future-work subsection.

The broader upstream-conditioning question---whether near-magnetopause descriptor behaviour shifts systematically across IMF cone-angle regimes---remains open. Phase 6 establishes that the required encounter population exists within the THEMIS archive: 28 quasi-radial and 89 low-cone encounters are evaluable under the original Dn/EB measurement family. Answering the conditioning question itself would require dedicated cross-probe calibration validation, dynamic-pressure-controlled sub-stratification to disentangle the probe-access and Dp effects from any cone-angle-dependent signal, and careful treatment of the transient-rich quasi-parallel foreshock environment that characterises low-cone conditions. These steps are beyond the scope of the present work and are left as explicit targets for future investigation.

---

## E. Figure / table placement note

Phase 6 does not require a main-text figure or table. If a summary is desired, a compact table of cone-bin counts and median Dn/EB (4 rows) may be placed:

- **After** Table T1 (Phase 4B frozen evidence ledger) and Table T2 (Phase 5B grouped inventory)
- **Before** any discussion/limitations section
- Labelled as a sidecar table (e.g., "Table T3: Full-archive cone-bin encounter counts under original Dn/EB semantics")

| Cone bin | N | Dn median | EB median | Dp median (nPa) |
|---|---|---|---|---|
| quasi-radial (< 30 deg) | 28 | 0.89 | 2.42 | 1.65 |
| low-cone (30--45 deg) | 89 | 0.80 | 2.55 | 1.53 |
| intermediate (45--60 deg) | 199 | 0.79 | 2.38 | 2.25 |
| perpendicular (> 60 deg) | 441 | 0.74 | 2.39 | 2.44 |

Do NOT place this table adjacent to or interleaved with the Phase 4B frozen ledger. Keep visual separation to prevent inadvertent cross-bank comparison.

---

## F. Do-not-say block

| # | Blocked pattern | Why |
|---|---|---|
| 1 | "Phase 6 validates / extends / strengthens Phase 4B" | Phase 6 is a sidecar, not a validation layer |
| 2 | "Cone angle controls / modulates depletion behaviour" | No conditioned comparison is supported |
| 3 | "Low-cone encounters show (or lack) a PDL signature" | No physical identification is supported |
| 4 | "The full archive confirms cone-angle dependence" | Archive fillability is not mechanism inference |
| 5 | "Phase 6 encounters are directly comparable to Phase 4B" | Cross-probe comparability is unvalidated |
| 6 | Any threshold, detection-rule, or class/label language | No detector semantics exist |
| 7 | "Occurrence rate," "occurrence fraction," or "event rate" | No occurrence layer is defined |
| 8 | "Route B inner-sheath descriptors confirm the Dn/EB pattern" | Route B uses different semantics; not confirming evidence |
| 9 | "The quasi-radial regime is structurally inaccessible" | It is accessible; only previously unsearched |
| 10 | "SMILE/SXI priors," "mission-facing output," or "forward model input" | No mission-translation layer exists |

---

## G. Source map

| Document | Layer | Role in this insertion pack |
|---|---|---|
| `PHASE_6_FULL_EXP_FREEZE.md` | **Bounded sidecar (ceiling)** | Primary source for strongest statement, non-claims, caveats, thesis placement |
| `PHASE_6_MASTER_SUMMARY.md` | **Bounded sidecar (navigation)** | Numbers, timeline, file index |
| `PHASE_6_EXTRA_QC_GATE_REPORT.md` | **Bounded sidecar (QC evidence)** | Cross-probe consistency rate (78%), OOM rate (22%) |
| `THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` | **Claim-bearing** | Phase 4B bank values cited for contrast only |
| `PHASE_4B_RESULTS_FREEZE.md` | **Claim-bearing (ceiling)** | Non-claims and ceiling that Phase 6 must not exceed |
| `THEMIS_THESIS_WRITING_PACK.md` | **Navigation** | Source hierarchy and placement map |
| `THEMIS_ARCHIVE_DATA_GUIDE.md` | **Engineering only** | Data cache layout; not a scientific-claim source |
