# Interim Materials Pack — History, Decisions, and Changes

> **How to use this file:** This is the chronological and decision-history companion to 00_INTERIM_MASTER.md and 01_INTERIM_EVIDENCE_AND_TEMP_CONCLUSIONS.md. It explains how the project evolved, what was tried, what failed, what changed, and how the current frozen state was reached. A reader opening only this file should understand the full arc of project development, including the MMS failure path and the Phase 6 route evolution. For evidence and current conclusions, see the companion files.

---

## Project orientation (repeated for standalone reading)

This project studies the dayside Plasma Depletion Layer (PDL) using THEMIS encounter-level descriptors (Dn, EB) and MMS multi-spacecraft thickness methods. The project has two main branches (THEMIS comparator bank and MMS thickness) plus an upstream-conditioning exploration (Phase 6). As of the current stage, THEMIS and MMS are both frozen; Phase 6 is packaged as a bounded sidecar. Writing-safe thesis integration is active.

---

## 1. Timeline overview

| Date | Phase | Key event | Outcome |
|---|---|---|---|
| 2026-03-25 | Phase 1 | Pipeline scaffold with synthetic data | Working pipeline; synthetic Dn/EB validated |
| 2026-03-25 | Phase 1.5 | Live THEMIS/OMNI data bridge | CDAWeb integration; fill masking; preflight gates |
| 2026-03-26 | Phase 2A | Window bank construction | 9 windows, 7 passes, THD 2008–2009 |
| 2026-03-26 | Phase 2B | Bank audit (falsification, sensitivity) | Conditional GO with caveats |
| 2026-03-26 | Phase 2C | Confounder closure (leave-spike-out) | 4 clean + 2 cautious + 1 excluded |
| 2026-03-26 | Phase 2D | Detector readiness review | Conditional GO to descriptive comparison |
| 2026-03-26 | Phase 3A | Bounded Dn/EB comparison | Low-Dn range depends entirely on cautious passes |
| 2026-03-27 | Phase 3B | P1/P3 retention audit | Both confirmed-cautious |
| 2026-03-27 | Phase 4A | Independent low-Dn recurrence | THE Sep 19 (Dn = 0.76) — cross-probe recurrence |
| 2026-03-28 | Phase 4B | Results freeze | **THEMIS bank frozen for thesis** |
| 2026-03-28 | MMS | Scaffold → shortlist → readiness → P1 attempt | **do_not_report (scale mismatch)** |
| 2026-03-29 | MMS | Basis reset → branch freeze | **MMS branch frozen** |
| 2026-03-29 | Phase 5A | Case-atlas screening | 8 cases; 5 atlas-usable |
| 2026-03-29 | Phase 5B | Grouped descriptive pass | Clock-angle bin inventory |
| 2026-03-30 | Phase 6A | Upstream conditioning pilot | 11 encounters (2 synthetic); QR bin empty |
| 2026-03-30 | Phase 6A T2 | Low-cone targeted search | 3 candidates; all failed BG occupancy |
| 2026-03-30 | Audit | Synthetic contamination + scope mismatch discovered | N = 9 real (2 synthetics removed) |
| 2026-03-30 | Route A | Mandatory provenance repair | Clean N = 9 catalogue |
| 2026-03-30 | Route B | Inner-sheath descriptor (Dn_near, D\|B\|_near) | 5 computable; 3/5 gradient; modest yield |
| 2026-03-31 | Route C | Local-only archive scan | HARD NULL (sparse local data) |
| 2026-03-31 | FULL EXP | CDAWeb full archive 2007–2010 | 148 retained; 4 QR, 16 LC — **SUCCESS** |
| 2026-03-31 | Archive build | Expanded to 2007–2025 | 1135 STATE files; 757 retained |
| 2026-03-31 | Phase 6 freeze | Packaged as bounded sidecar | Writing-safe |
| 2026-03-31 | QC gate (2007–2010) | Cross-probe comparability test | **PASS** (77% consistent) |
| 2026-03-31 | EXTRA (2007–2025) | Full-archive QC gate | **FAIL** (same 78% rate, higher absolute count) |
| 2026-03-31 | Thesis packaging | Final harmonisation | All docs aligned, insertion pack created |

---

## 2. Early THEMIS development and audit phases

### Phase 1 / 1.5: Pipeline scaffold and live data

The pipeline was initially built on synthetic data to validate the measurement model architecture (s-coordinate, dual-bin design, metric computation). Phase 1.5 replaced synthetic data with live THEMIS/OMNI data from CDAWeb via cdasws, adding fill-value masking, scientific preflight gates, sheath-membership validation, and corrected cone-angle computation.

**Key design decisions:** The encounter (not the crossing) was chosen as the statistical unit. The detector was designed to be upstream-IMF-agnostic — IMF conditions are used for conditioning after detection, not during it. The s-coordinate normalises position between the model magnetopause and bow shock.

### Phase 2A–2D: Bank construction, audit, and readiness

Phase 2A produced nine measurement-model-valid windows from seven THD passes. Phase 2B tested the bank with shuffled-s falsification (confirming spatial structure depends on ordered s-position), duration-variant consistency (within-pass spread << between-pass range), and membership/confounder checks. Phase 2C performed leave-spike-out analysis on all seven passes, splitting the bank into clean core (4 passes), cautious (2 passes), and excluded (1 pass, P7). Phase 2D confirmed readiness for a bounded descriptive comparison, subject to hard boundaries: no thresholds, no labels, no detector semantics.

**Key issue discovered:** Universal jet triggering (jet_flag = TRUE for all windows). The 2x median Pdyn threshold is too broad for 6–10 hour windows. This flag has no discriminative power. Transient and mixing flags remain UNKNOWN throughout the project.

**Key design decision:** All windows remain "measurement-model-valid near-MP comparator windows." No window is ever called PDL-positive, non-PDL, or a labelled example.

**Files:** `docs/PHASE_2A_STATE.md` through `docs/PHASE_2D_DETECTOR_READINESS_REVIEW.md`

---

## 3. Comparator-bank consolidation and freeze

### Phase 3A: Bounded Dn/EB comparison

The first descriptive comparison showed clean-core Dn spanning 0.94–2.31 and EB spanning 0.80–1.96. The low-Dn region (Dn < 0.5) depends entirely on the two cautious passes (P1: 0.12, P3: 0.39). The Dn–EB inverse relationship was observed but is qualitative and not statistically significant at N = 9.

### Phase 3B: P1/P3 retention audit

Both cautious passes were examined in detail. P1 has extreme near-bin density noise (CV = 0.93) — the Dn = 0.12 could partly reflect magnetosheath turbulence. P3 has EB spike-dependent behaviour (delta 0.50 under spike removal) and the largest mapping sensitivity in the bank (±0.23 in s per ±1 nPa Dp). Both were retained as "confirmed-cautious" with explicit, unresolvable caveats.

### Phase 4A: Independent recurrence

A search for independent low-Dn candidates found THE Sep 19 2008 (Dn = 0.76, EB = 2.12) on a different probe. This is the first cross-probe evidence that sub-unity Dn recurs independently. However, THE Sep 19 is not less caveated than P1/P3 (membership 84%, Dp 2.8, extreme Mach number 21.1), and no independent candidate reaches Dn < 0.5.

### Phase 4B: Results freeze

The bank was frozen on 2026-03-28 with user authorisation. The freeze established the strongest supportable claim (operationally distinguishable Dn/EB; sub-unity Dn recurs cross-probe; Dn < 0.5 cautious-only), the strongest non-claim (no physical identification, no thresholds, no generalisation beyond compressed-sheath THD), and a stop condition (no renewed window search, no detector work, no class language).

**Files:** `docs/THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md`, `docs/PHASE_4B_RESULTS_FREEZE.md`

---

## 4. Phase 5 editorial packaging evolution

Phase 5A screened eight cases from the frozen seed with operational filters (SZA, clock angle, upstream stability). Cases were reviewed for three near-MP indicators (density down, |B| up, beta down). Four were reviewed as clear (P3, P4, P5, EXT), one as ambiguous (P6), two as not convincing (P2, P7), and one failed screening (P1 — quasi-radial geometry). Phase 5B grouped these by clock-angle bin: atlas-usable cases appeared only in the 60–120 deg and > 120 deg bins.

**Key design decision:** Review statuses (clear/ambiguous/not convincing) are explicitly editorial packaging, not scientific confidence classes. They do not strengthen or weaken the Phase 4B frozen claims. The caseset is too small (N = 8) for conditioned inference.

**What changed in project understanding:** Phase 5 demonstrated that the frozen bank can be illustrated with per-case crossing evidence, but the caseset does not add statistical weight to the encounter-level Dn/EB comparator results.

**Files:** `docs/THEMIS_CASESET.md`, `docs/PHASE_5B_CASESET_DESCRIPTIVE_PASS.md`

---

## 5. Phase 6 evolution and route changes

Phase 6 has the most complex history of any branch, involving multiple route attempts, resets, failures, and recoveries. The full story is:

### 5a. Phase 6A: Pilot and failure (2026-03-30)

Phase 6A opened a new THEMIS science branch asking how Dn/EB shift across IMF cone-angle regimes. Tranche 1 produced 11 encounters from locally cached runs. **Post-audit discovery:** 2 of 11 were synthetic fixtures (pilot_001, pilot_002) with hardcoded upstream parameters (Dp = 2.0, Bz = 2.0, Ma = 8.0, SZA = 0.0), inflating the intermediate-cone group. Tranche 2 targeted low-cone encounters by searching THD+THE in Aug–Oct 2008–2009 (every 3rd day). Three candidates found (cone 43–44 deg), but all failed background-bin occupancy because associated Dp was too low (1.9–2.7 nPa) for the sheath to be narrow enough. **Discovery of declared-vs-searched mismatch:** Tranche 2 declared "2007–2010" but actually searched only a narrow subspace.

### 5b. Audit and reset decision (2026-03-30)

The Phase 6A audit identified four interlocking failures: (1) synthetic contamination, (2) scope mismatch, (3) dual-bin occupancy bottleneck at low Dp, and (4) branch question broader than apparatus can answer. Four reset routes were proposed: Route A (mandatory repair), Route B (measurement-model change), Route C (regime-access expansion), Route D (question narrowing).

### 5c. Route A: Provenance repair (2026-03-30)

Mandatory repair removed the two synthetic fixtures, producing a clean N = 9 real encounter catalogue with scope-match discipline. Route A was a prerequisite for all other routes.

### 5d. Route B: Inner-sheath descriptor (2026-03-30)

Route B designed an alternative descriptor (Dn_near = very-near/near density ratio; D|B|_near same for |B|) that does not require the background bin. A regression test showed 5 of 12 encounters were Route-B-computable, including 1 recovered low-cone encounter (t2_20080904_thd, cone 43 deg). A bounded execution found that 3 of 5 encounters showed inner-sheath depletion-consistent gradients. However, the recovered low-cone encounter showed a flat inner-sheath profile (no depletion). Route B was frozen as a sidecar with modest yield. Its descriptors are not interchangeable with Dn/EB.

**What changed in understanding:** Route B confirmed that the very-near bin is sensitive to different physics than the near/background ratio. The descriptors capture different gradient scales, not the same phenomenon at different resolution.

### 5e. Decision-space repair (2026-03-31)

The post-Route-B menu was expanded from 3 options to 4 (Route B continuation, Route C, Route D, writing-safe return). The user chose Route C.

### 5f. Route C: Local-only attempt and HARD NULL (2026-03-31)

Route C searched locally cached data in the unsearched parts of 2007–2010 (2007, 2010, and 2008–2009 non-Aug-Oct). Only 3 unique date+probe combinations found; 2 had incomplete data. **HARD NULL** (0 quasi-radial, 1 low-cone retained). This null was caused by local data sparsity, not a definitive archive search.

### 5g. Route C FULL EXP: CDAWeb full-archive scan (2026-03-31)

The user authorised a one-off full-archive experiment overriding the prior writing-safe closure. Multi-threaded CDAWeb acquisition covered all five THEMIS probes, July–November 2007–2010. **Result: SUCCESS.** 2083 qualifying days processed; 148 retained encounters; 4 quasi-radial, 16 low-cone. The previously empty bins were populated by encounters from THA/THB/THC at low Dp (0.8–1.7 nPa), which were never searched before.

### 5h. Archive expansion to 2007–2025 (2026-03-31)

The user authorised expanding the local cache to cover 2007–2025, all probes, all months. This revealed that THEMIS inner probes have a second dayside season in 2016–2019 (same orbital geometry as 2007–2010) and that THB/THC (ARTEMIS) contribute encounters from lunar-orbit perigee passes across 2010–2025. Final archive: 1135 STATE files, 6903 qualifying days, 757 retained encounters (28 QR, 89 LC, 199 IM, 441 PP).

### 5i. Cross-probe QC gate and verdict discrepancy (2026-03-31)

Two cross-probe QC gates were run:

| Gate | Dataset | Overlap groups | Consistency rate | LC/QR OOM rate | Verdict |
|---|---|---|---|---|---|
| FULL EXP | 148 (2007–2010) | 26 | 77% | 25% (1/4) | **PASS** |
| EXTRA | 757 (2007–2025) | 208 | 78% | 22% (9/41) | **FAIL** |

The verdict discrepancy is a threshold-design artifact: the predeclared FAIL criterion (>= 3 OOM groups in absolute count) triggers at 9/41 even though the OOM rate (22%) is actually lower than the PASS dataset (25%). The underlying cross-probe consistency is the same or slightly better in the larger dataset. This is documented as a judgment-call issue, not a data contradiction.

### 5j. Phase 6 packaging and freeze (2026-03-31)

Phase 6 was packaged as a "bounded descriptive-methodological sidecar." It does not strengthen, extend, or validate Phase 4B. Cross-probe comparability remains an unresolved caveat. The broader upstream-conditioning question (whether Dn/EB shifts systematically with cone-angle regime) is explicitly deferred to future work.

**Files:** `docs/PHASE_6_MASTER_SUMMARY.md` (full Phase 6 history), `docs/PHASE_6_FULL_EXP_FREEZE.md` (freeze note)

---

## 6. MMS branch evolution and failure path

The MMS branch progressed through five stages before being frozen:

### 6a. Methods scaffold

A comprehensive framework was designed for multi-spacecraft thickness measurement: dual thickness definitions (timing-based Lt and gradient-scale Lg), normal-estimation hierarchy (MVA + timing cross-check), uncertainty ledger (six components), and quality grading (Gold/Silver/Bronze/do_not_report). The scaffold was methodologically sound and independent of the THEMIS branch.

### 6b. Event shortlist

Eleven MMS Phase 1 dayside passes (Oct 2015–Feb 2017) were screened. Seven failed due to absence of sustained near-MP density gradient within the ±2 hour apogee window. Three primaries (P1, P2, P3) and one reserve (R1) were identified. P3 had the best geometry (SZA 6 deg, Dp 2.6 nPa); P1 had the smallest distance to the model magnetopause (0.4 Re).

### 6c. Readiness audit

Full event-package analysis on all three primaries. P1 and P3 advanced (clear boundary-crossing signatures, plausible boundary adjacency). P2 was held (1.8 Re from magnetopause, no clear density transition).

### 6d. P1 thickness attempt — the critical failure

The first and only thickness attempt (2015-11-12) found a clear, real, four-spacecraft-observable near-magnetopause gradient: |B| drops ~28 nT, density drops ~10 cm^-3 over ~5 minutes. This is genuine magnetosheath structure. But all thickness methods failed:

- **MVA normal:** eigenvalue ratio 3.0 (far below reliable threshold ~10); direction 70 deg from expected sunward normal
- **Timing normal:** degenerate — 10 km four-spacecraft separation cannot resolve a ~1118-second delay timescale
- **Timing thickness (Lt):** not defensible without a reliable normal
- **Gradient thickness (Lg):** 10 km separation is noise-dominated at ~750–3750 km gradient scale

**Outcome: do_not_report.** The gradient is real but the spatial structure (~1000 km) is approximately 100x larger than the MMS Phase 1 tetrahedron (~10 km).

### 6e. Basis reset and branch freeze

Root-cause analysis confirmed the scale mismatch as the dominant structural blocker. The original methods scaffold lacked a separation-scale-match eligibility gate. Phase 2 separations (~25 km) offer only 2–3x improvement — still 40–100x mismatch. All continuation routes were evaluated and found insufficient:

- P3 attempt: same barrier expected
- Phase 2 events: insufficient improvement
- Method salvage: cannot overcome physical configuration
- Downgrade to "effective width": depends on boundary-definition choices

**Branch frozen with documented negative result.** The scale mismatch is a legitimate methodological finding for thesis integration: MMS excels at thin structures (~10–100 km), but typical extended near-MP gradient layers are ~100–3000 km.

**Files:** `docs/MMS_BRANCH_FREEZE.md`, `docs/MMS_P1_FIRST_THICKNESS_ATTEMPT.md`, `docs/MMS_BASIS_RESET.md`

---

## 7. Current frozen / bounded hierarchy and how it was reached

The project arrived at its current state through a series of explicit freeze decisions:

| Layer | What it is | When frozen | Why |
|---|---|---|---|
| **Phase 4B** | THEMIS 6-pass comparator bank | 2026-03-28 | Clean core + cautious spans support thesis-safe claims |
| **Phase 5A/5B** | Editorial caseset sidecars | 2026-03-29 | Illustration only; does not strengthen claims |
| **MMS branch** | Methods + P1 failure + basis reset | 2026-03-29 | Scale mismatch structural; documented negative result |
| **Phase 6** | Full-archive 757-encounter bounded sidecar | 2026-03-31 | Bins fillable but cross-probe comparability unresolved |
| **Route B** | Inner-sheath descriptor sidecar | 2026-03-30 | Modest yield; different semantics; not incorporated |

The hierarchy is:
1. **Phase 4B = sole claim-bearing anchor** — cite for THEMIS results
2. **Phase 5A/5B = editorial sidecars** — cite for illustration only
3. **Phase 6 = bounded descriptive-methodological sidecar** — cite for archive accessibility but not as validated comparison
4. **MMS = methods/limitation** — cite for methodological finding
5. **Route B = internal sidecar** — available but not on thesis path

---

## 8. Practical lessons for final-report writing

### What to present

1. The measurement model and its design choices (s-coordinate, dual-bin, encounter unit)
2. The THEMIS frozen bank (6 passes, clean core vs cautious, Dn/EB ranges, external recurrence)
3. The MMS thickness attempt and why it failed (real gradient, structural scale mismatch)
4. The Phase 6 full-archive result as a bounded sidecar (bins fillable, comparison deferred)
5. Explicit limitations throughout (single-probe bias, compressed-sheath bias, unresolved confounders, cross-probe caveat, MMS scale mismatch)

### What NOT to present

- Phase 6 as validating or extending Phase 4B
- Phase 5 review statuses as physical classes
- Any threshold, label, or detector semantics
- Occurrence rates or population-level statistics
- MMS thickness values (none exist)
- SMILE/SXI priors (none constructed)

### Historical material to use for methods provenance only

- The multi-stage audit trail (Phases 2A–2D) demonstrates methodological rigour
- The MMS failure path demonstrates honest reporting of negative results
- The Phase 6 route evolution demonstrates systematic exploration of alternatives

### Key wording patterns

- "measurement-model-valid near-MP comparator window" (not "PDL event")
- "operationally distinguishable Dn/EB outputs" (not "detected PDL")
- "cautious-only evidence with documented caveats" (not "confirmed depletion")
- "bounded descriptive-methodological sidecar" (not "validated cone-angle comparison")
- "structural scale mismatch" (not "MMS failure")
- "the broader upstream-conditioning question remains open" (not "cone angle does/does not control depletion")

### Source hierarchy for writing

| Priority | Source | Use |
|---|---|---|
| 1st | `THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` | THEMIS results claims |
| 2nd | `PHASE_4B_RESULTS_FREEZE.md` | Non-claims / ceiling |
| 3rd | `MMS_BRANCH_FREEZE.md` | MMS methods / limitation |
| 4th | `PHASE_6_THESIS_INSERTION_PACK.md` | Phase 6 pasteable prose |
| 5th | `THEMIS_CASESET.md` / `PHASE_5B_CASESET_DESCRIPTIVE_PASS.md` | Illustration |
| — | `PHASE_6_MASTER_SUMMARY.md` | Phase 6 navigation |
| — | `THEMIS_THESIS_WRITING_PACK.md` | Thesis-entry hub |
