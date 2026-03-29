# LLM Handoff — PDL Pilot Pipeline

**Load this first when resuming in a new session.**
**Mode: frozen-writing-safe.** Both branches frozen. Phase 5A/5B sidecars complete. No active science question.

---

## Control-state precedence

| Priority | File | Role |
|---|---|---|
| 1 | `docs/NEXT_QUESTION.md` | Live control state |
| 2 | `docs/WORKLOG_LATEST.md` | Latest applied round |
| 3 | `docs/LLM_HANDOFF.md` | Consolidated project entry (this file) |
| 4 | Historical artifacts (RUN_REVIEW_PACKET, old phase memos, sign-off packets) | Provenance/audit only — never override live state |

See also `docs/CONTROL_STATE_PRECEDENCE.md` for full precedence rules.

---

## Current writing-safe frozen summary

**THEMIS branch frozen (Phase 4B).** Six-pass interpretable bank (4 clean core + 2 cautious) + one external cross-probe recurrence (THE Sep 19). Writing-safe for thesis integration.

**MMS branch frozen.** Scaffold → shortlist → readiness → P1 do_not_report → basis reset → freeze. No reportable thickness. Scale mismatch structural (~100×). Branch closed as methodological finding.

No thresholds, no labels, no detector semantics on either branch.

**Strongest claim:** The frozen measurement model produces operationally distinguishable Dn/EB outputs across 6 independent THD passes. Sub-unity Dn recurs on an independent cross-probe (THE Sep 19, Dn = 0.76). The cautious-only low-Dn region (Dn < 0.5) is not independently recurred.

**Strongest non-claim:** No physical identification, no threshold, no generalization beyond compressed-sheath THD conditions. THE Sep 19 is external recurrence only, not admitted to the main bank.

**Phase 5A/5B caseset sidecars (2026-03-29).** 8 cases screened from frozen seed pass. 4 reviewed as clear (P3, P4, P5, EXT) + 1 reviewed as ambiguous (P6). Phase 5B grouped these by clock-angle bin: atlas-usable cases appear in 60–120° and >120° bins only; the sole <60° screened case is reviewed as not convincing. Review statuses are editorial packaging only, not scientific confidence classes. Frozen Phase 4B claims unchanged. See `docs/PHASE_5B_CASESET_DESCRIPTIVE_PASS.md`.

**For thesis writing, start from:**
1. `docs/THEMIS_THESIS_WRITING_PACK.md` (THEMIS thesis-entry hub)
2. `docs/THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` (claim-bearing results)
3. `docs/MMS_BRANCH_FREEZE.md` (MMS methods/limitation)
4. `docs/REPO_NAVIGATION_FOR_THESIS.md` (full repo map)

---

## Historical bank ledger (provenance — do not lift into thesis prose without context)

9 measurement-model-valid THEMIS windows across 7 passes. Dn spans 0.12–2.31, EB 0.80–4.22, rho universally negative. Duration variants consistent within passes. No labels or thresholds assigned.

## Window bank (9 windows / 7 passes)

| ID | Date | SZA | Dp | Bz | Near% | BG% | Dn | EB | ρ | Seed? |
|---|---|---|---|---|---|---|---|---|---|---|
| usable_aug18_6h | 2008-08-18 | 22° | 4.2 | +0.3 | 16% | 48% | 0.12 | 2.49 | -0.46 | **A** |
| usable_aug18_8h | 2008-08-18 | 22° | 3.6 | +0.1 | 17% | 12% | 0.88 | 2.08 | N/A | (variant) |
| usable_sep03_6h | 2008-09-03 | 14° | 3.5 | +0.9 | 17% | 27% | 2.31 | 0.82 | -0.52 | **C** |
| usable_sep03_8h | 2008-09-03 | 12° | 3.5 | +2.6 | 13% | 40% | 2.07 | 0.80 | -0.51 | (variant) |
| usable_sep13_09_6h | 2009-09-13 | 17° | 3.1 | -1.4 | 17% | 47% | 0.39 | 1.96 | -0.90 | **D** |
| usable_sep20_09_6h | 2009-09-20 | 10° | 3.0 | +1.4 | 9% | 46% | 0.97 | 1.48 | -0.63 | **B** |
| usable_sep26_09_10h | 2009-09-26 | 4° | 3.0 | +0.9 | 18% | 40% | 0.94 | 1.96 | -0.91 | |
| usable_sep27_09_10h | 2009-09-27 | 4° | 3.1 | -1.7 | 16% | 57% | 1.31 | 1.23 | -0.72 | |
| usable_oct24_09_6h | 2009-10-24 | 20° | 4.2 | -0.5 | 14% | 65% | 2.19 | 4.22 | -0.66 | |

All remain "measurement-model-valid near-MP comparator windows." None labeled.

## Key review findings

1. **Dn and EB approximately inversely related** — observed pattern, not a diagnostic rule
2. **ρ(n,B) negative across all bank windows** — but universality within this bank means ρ has no discriminative power here; it may reflect a property common to all compressed-sheath comparator conditions
3. **Duration variants consistent** — within-pass Dn spread (0.50) ≪ between-pass range (1.80)
4. **Effective N = 7** independent passes, not 9 windows

## Scientific risks (see METRIC_BEHAVIOR_REVIEW.md for details)

- Single probe (THD only), Dp > 3 nPa selection bias, encounter-averaged boundaries, universal ρ < 0 is non-discriminative, confounder flags incomplete (transient/mixing = UNKNOWN)

## Seed slate (planning only — not labels)

| Seed | Window | Dn | EB | Operational description |
|---|---|---|---|---|
| A | aug18_6h | 0.12 | 2.49 | Lowest Dn, highest EB among seeds |
| B | sep20_09_6h | 0.97 | 1.48 | Dn near unity, moderate EB |
| C | sep03_6h | 2.31 | 0.82 | Highest Dn, EB below unity |
| D | sep13_09_6h | 0.39 | 1.96 | Most negative ρ in bank |

## Key files

| What | Where |
|---|---|
| Comparator atlas | `docs/COMPARATOR_ATLAS.md` |
| Seed dossier | `docs/SEED_DOSSIER.md` |
| Metric review (tightened) | `docs/METRIC_BEHAVIOR_REVIEW.md` |
| Window bank config | `configs/pilot_live_usable.yaml` |
| Window bank summary | `docs/WINDOW_BANK_SUMMARY.md` |
| Phase 2a state | `docs/PHASE_2A_STATE.md` |
| Review artifacts | `runs/20260326T040343Z_d0425fd4/` |

## Commands

```bash
# Run the bank
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live_usable.yaml

# Run the metric review
PYTHONPATH=src python -m pdl_pilot.cli.metric_review --run-dir runs/20260326T040343Z_d0425fd4

# Tests (117 pass, 1 skip)
PYTHONPATH=src python -m pytest tests/ -v
```

## Phase 2B audit gate (2026-03-26)

**Question:** Is the bank clean enough for a later bounded detector-readiness stage?

**Answer: CONDITIONAL GO**

Passes: dual-bin leverage confirmed, spatial structure survives shuffled-s null, duration variants consistent, membership ≥85%, primary metrics insensitive to very-near bin, naming conservative.

Conditions carried forward:
1. Universal jet triggering (all 9 windows) — jet_flag has zero discriminative power; threshold may need recalibration for long windows
2. transient_flag and mixing_flag remain UNKNOWN — max grade = Silver
3. THD-only, Dp > 3 nPa selection bias — bank does not represent full sheath population
4. Effective N = 7, not 9
5. ρ universally negative — non-discriminative in this bank
6. ±1 nPa Dp shifts boundaries ~1 Re — moderate upstream sensitivity (deferred)

**Full audit:** `docs/PHASE_2B_AUDIT.md`
**Selection logic:** `docs/SELECTION_FUNCTION_AUDIT.md`
**Wording audit:** `docs/WORDING_DRIFT_AUDIT.md`
**Machine-readable:** `runs/20260326T040343Z_d0425fd4/phase2b_audit_summary.json`

## Phase 2C interval audit (2026-03-26)

**Question:** Does the 7-pass bank contain a sufficiently clean subset after interval-level confounder scrutiny?

**Answer: YES, with conditions**

**Clean core (4 passes):** P2 (Sep 3), P4 (Sep 20), P5 (Sep 26), P6 (Sep 27). Metrics survive leave-spike-out. Low-to-moderate density noise.

**Usable with caveats (2 passes):** P1 (Aug 18, seed_A: high density noise CV=0.93), P3 (Sep 13, seed_D: EB partially spike-dependent, Δ=0.50).

**Excluded (1 pass):** P7 (Oct 24) — spike-dominated. Dn collapses 2.19→0.67, EB 4.22→0.97 after spike removal.

**Seed status update:**
- seed_A (P1): usable with noise caveat
- seed_B (P4): **cleanest** — unchanged
- seed_C (P2): clean — unchanged
- seed_D (P3): weakened — EB partially spike-dependent

**Full audit:** `docs/PHASE_2C_CONFOUNDER_CLOSURE.md`
**Pass cards:** `docs/PASS_INTERVAL_AUDIT.md`
**Machine-readable:** `runs/20260326T040343Z_d0425fd4/phase2c_interval_audit.json`

## Key files (updated)

| What | Where |
|---|---|
| **Phase 2C confounder closure** | `docs/PHASE_2C_CONFOUNDER_CLOSURE.md` |
| **Pass interval audit** | `docs/PASS_INTERVAL_AUDIT.md` |
| Phase 2B audit | `docs/PHASE_2B_AUDIT.md` |
| Seed dossier (updated) | `docs/SEED_DOSSIER.md` |
| Comparator atlas | `docs/COMPARATOR_ATLAS.md` |
| Window bank config | `configs/pilot_live_usable.yaml` |
| Interval audit data | `runs/20260326T040343Z_d0425fd4/phase2c_interval_audit.json` |

## Phase 2D comparison-readiness review (2026-03-26)

**Question:** Is the post-Phase-2C bank sufficient to support a very bounded descriptive Dn/EB comparison?

**Answer: CONDITIONAL GO — for descriptive comparison only**

**Clean core (4 passes):** P2, P4, P5, P6. Dn 0.94–2.31, EB 0.82–1.96. Confounder-tested.
**Cautious (2 passes):** P1, P3. Extend Dn range to 0.12–0.39 but carry density-noise and EB-spike caveats.
**Excluded (1 pass):** P7. Spike-dominated.

**Key insufficiency:** Clean core alone has no pass with Dn < 0.5. The low-Dn range relies entirely on cautious passes.

**Carried-forward caveats:**
- Universal negative ρ: non-discriminative within this bank
- Universal jet triggering: long-window artifact; metrics survive in clean core
- Transient/mixing/boundary-motion UNKNOWN: tolerable for descriptive work only
- THD-only / Dp > 3 nPa bias: results are regime-specific
- Encounter-averaged boundaries: provisional limitation

**This review does NOT authorize:** thresholds, labels, detector semantics, or dev-set membership.

**Full review:** `docs/PHASE_2D_DETECTOR_READINESS_REVIEW.md`
**Evidence matrix:** `docs/READINESS_EVIDENCE_MATRIX.md`

## Evidence-report package (2026-03-26)

A reusable evidence package now exists with two-layer design (factual + review).

**Machine-readable:** `runs/20260326T040343Z_d0425fd4/evidence/`
- `json/bank_manifest.json` — full per-window structured records (9 windows)
- `json/bank_summary.json` — compact bank statistics
- `json/review_layers.json` — stage-local dispositions only
- `json/pass_summary.jsonl` — one line per pass
- `csv/window_matrix.csv` — wide-format metrics + context
- `csv/confounder_register.csv` — per-window confounder flags
- `csv/interval_audit_matrix.csv` — spike sensitivity data
- `chunks/bank_report_chunks.json` — AI-consumable chunks
- `index/artifact_index.json` — links all artifacts

**Human-facing:** `reports/current_bank/`
- `INDEX.md` — navigation
- `bank_report.md` — cross-pass evidence matrix + confounder table
- `passes/<window_id>.md` — per-pass evidence sheets (7 pages)
- `figures/cross_pass_summary.png` — Dn-EB scatter, spike sensitivity, occupancy

**Schema:** `docs/EVIDENCE_REPORT_SCHEMA.md`
**Generator:** `src/pdl_pilot/cli/generate_evidence.py`
**Tests:** 124 pass, 1 skip

## Key files (updated)

| What | Where |
|---|---|
| **Evidence schema** | `docs/EVIDENCE_REPORT_SCHEMA.md` |
| **Evidence generator** | `src/pdl_pilot/cli/generate_evidence.py` |
| **Bank manifest (JSON)** | `runs/.../evidence/json/bank_manifest.json` |
| **Bank report** | `reports/current_bank/bank_report.md` |
| **Per-pass pages** | `reports/current_bank/passes/` |
| Phase 2D readiness review | `docs/PHASE_2D_DETECTOR_READINESS_REVIEW.md` |
| Window bank config | `configs/pilot_live_usable.yaml` |

## Phase 3A: Bounded Dn/EB exploratory comparison (2026-03-26)

Completed. Descriptive only. No thresholds or labels.

**Key finding:** Clean core (P2, P4, P5, P6) spans Dn 0.94-2.31, EB 0.80-1.96. Low-Dn range (< 0.5) depends entirely on cautious passes (P1: 0.12, P3: 0.39).

**Artifacts:**
- Science memo: `docs/PHASE_3A_DNEB_EXPLORATORY_COMPARISON.md`
- Comparison report: `reports/current_bank/phase3a_dneb_comparison.md`
- Run review packet: `runs/.../evidence/review/RUN_REVIEW_PACKET.md`
- Figure: `reports/current_bank/figures/phase3a_dneb_comparison.png`
- Schema gaps filled: `pass_matrix.csv`, `figure_manifest.json`, `claim_map.json`, `pass_report_chunks.json`

**Schema deferred:** `bin_stats_long.csv` and `profile_long.csv` — current run products do not expose per-bin profile-level exports.

## Phase 3B: P1/P3 retention audit (2026-03-27)

**User decisions applied:** Phase 3A signed off as descriptive checkpoint. Phase 3B authorized as P1/P3 retention audit only. Decision vocabulary restricted to confirmed-cautious or downgraded.

**Outcome:**
- P1 (aug18_6h): **confirmed-cautious.** Near-bin density CV=0.93; Dn=0.12 driven by noisy median; 14% NaN. Pattern qualitatively survives spike removal but is not confounder-tested at the interval level.
- P3 (sep13_09_6h): **confirmed-cautious.** EB partially spike-dependent (Δ=0.50); mapping sensitivity ±0.23 at Dp=3.1 (largest in bank). Dn=0.39 is robust to spike removal.

**Bank status:** Six-pass interpretable bank remains defensible. All low-Dn evidence (Dn < 0.5) is cautious-only and must always be reported as such.

**Strongest supportable low-Dn statement:** Two cautious passes produce Dn < 0.5, both robust to spike removal, but P1's Dn is driven by a noisy near-bin sample and both carry mapping-sensitivity caveats that cannot be resolved under the frozen model.

**Not supportable:** Confounder-tested evidence for Dn < 0.5.

**Full audit:** `docs/PHASE_3B_P1P3_RETENTION_AUDIT.md`
**Report:** `reports/current_bank/phase3b_p1p3_retention_audit.md`
**Decision record:** `docs/PHASE_3A_SIGNOFF_AND_PHASE_3B_SCOPE.md`

## Phase 4A: Independent low-Dn recurrence test (2026-03-27)

**User-authorized.** Searched for independent candidates outside the current six-pass bank.

**Search space:** THD 2008-09, THE 2008, THD 2010. 4 candidates tested. 2 PASS, 2 FAIL_OCCUPANCY.

**Key finding:** THE Sep 19 2008 produces Dn = 0.76 on a different probe. This is below the clean-core floor (0.94) but above the cautious range (Dn < 0.5). It is the first cross-probe evidence that Dn < 1 behavior recurs independently.

**However:** The candidate is not less caveated than P1/P3 (84% membership, borderline Dp = 2.8, extreme Ma = 21.1). No independent candidate reaches Dn < 0.5. The cautious-only character of all Dn < 0.5 evidence is unchanged.

**Strongest claim:** Dn < 1 recurs on an independent probe. Dn < 0.5 does not.

**Full analysis:** `docs/PHASE_4A_INDEPENDENT_LOWDN_RECURRENCE.md`
**Report:** `reports/current_bank/phase4a_lowdn_recurrence_report.md`
**Shortlist:** `runs/20260327T221306Z_227f7e3f/evidence/csv/phase4a_candidate_shortlist.csv`
**Figure:** `reports/current_bank/figures/phase4a_lowdn_recurrence.png`

## Phase 4B: Results freeze (2026-03-28)

**Comparator + recurrence branch frozen for thesis integration.**

- Six-pass interpretable bank: frozen (P2/P4/P5/P6 clean core + P1/P3 confirmed-cautious; P7 excluded)
- THE Sep 19 (Dn = 0.76): external recurrence record only; not admitted to bank
- Writing-safe results block: thesis paragraph, paper paragraph, 5 safe sentences, 5 do-not-say examples
- Stop condition: no renewed same-apparatus search, no detector work, no class language under current apparatus

**Full freeze:** `docs/PHASE_4B_RESULTS_FREEZE.md`
**Report:** `reports/current_bank/phase4b_results_freeze_report.md`

**Any future scientific move on the THEMIS branch requires a new red-level user decision.**

## MMS thickness branch (2026-03-28)

**Independent branch. Frozen under current basis.** No reportable thickness. The P1 scale-mismatch result and revised reportability criterion are documented as methodological findings for thesis use.

**Branch history:** scaffold → shortlist (3 primary + 1 reserve) → readiness audit (P1/P3 advance, P2 hold) → P1-only thickness attempt (do_not_report due to Phase 1 scale mismatch).

**What the scaffold defines:**
- Thickness-eligibility gate (geometry, data, tetrahedron, upstream, gradient)
- Start/end feature menu and feature-pairing rules
- Normal-estimation hierarchy with cross-check requirements
- Two fixed thickness definitions (timing-based + gradient-scale)
- Uncertainty ledger and `L ± σ` combination design
- Event quality grading (Gold / Silver / Bronze / do not report)
- Minimum per-event evidence package
- Event-registry schema (template, no events registered)
- Explicit stop condition and THEMIS branch separation

**What the scaffold does NOT do:** shortlist events, compute thickness values, validate THEMIS results, or define physical classes.

### MMS event shortlist (2026-03-28)

**User-authorized.** Screened 11 MMS1 near-subsolar dayside passes from Phase 1 (2015–2017).

**Result:** 3 primary + 1 reserve candidates.

| ID | Date | SZA | Dp | Density CV | Disposition |
|---|---|---|---|---|---|
| MMS-P1 | 2015-11-12 | 18° | 1.1 | 0.45 | primary |
| MMS-P2 | 2015-12-12 | 11° | 2.0 | 0.35 | primary |
| MMS-P3 | 2016-12-26 | 6° | 2.6 | 0.47 | primary |
| MMS-R1 | 2017-01-05 | 7° | 2.6 | 0.44 | reserve |

**No thickness values, no physical identification, no quality grades assigned.**

**Full shortlist:** `docs/MMS_EVENT_SHORTLIST.md`
**Screening registry:** `reports/mms_shortlist/screening_registry.csv`
**Quicklooks:** `reports/mms_shortlist/figures/`

### MMS event-package readiness audit (2026-03-28)

**User-authorized.** Full event-package analysis on 3 primaries. No thickness values produced.

| ID | Dist to MP | Beta trans | Dens trans | Boundary adj | Verdict |
|---|---|---|---|---|---|
| MMS-P1 | 0.4 Re | ✓ | ✓ | plausible | **ADVANCE** |
| MMS-P2 | 1.8 Re | ✓ | ✗ | not plausible | HOLD |
| MMS-P3 | 2.1 Re | ✓ | ✓ | plausible (motion) | **ADVANCE** |

**No thickness values, no quality grades, no physical identification.**
Reserve MMS-R1 untouched. MMS-P2 on hold.

**Full audit:** `docs/MMS_EVENT_PACKAGES_READINESS_AUDIT.md`
**Event cards:** `reports/mms_event_packages/events/`

### MMS-P1 first thickness attempt (2026-03-28)

**User-authorized (P1 only, not P1+P3 bundle).** Full single-event thickness attempt on MMS-P1.

**Outcome: do_not_report.**

The MMS Phase 1 tetrahedron separation (~10 km) is ~100× smaller than the observed near-MP gradient spatial scale (~750–3750 km). Both timing-based and gradient-scale thickness paths fail:
- MVA normal: poorly constrained (λ₂/λ₁ = 3.0), 70° from expected direction
- Timing normal: degenerate (4-SC separation too small for this crossing timescale)
- Lt: not defensible (no reliable normal)
- Lg: not defensible (separation << gradient scale)

**A clear gradient exists** (|B| drops ~28 nT, density drops ~10 cm⁻³ over ~5 min) but the structure is too spatially extended for Phase 1 methods.

**This is a structural Phase 1 scale-mismatch limitation**, not a data-quality failure. It likely applies to any MMS Phase 1 dayside event with similarly extended gradient layers.

**No reportable thickness. No quality grade. P3 untouched. Reserve untouched.**

**Full analysis:** `docs/MMS_P1_FIRST_THICKNESS_ATTEMPT.md`
**Report:** `reports/mms_p1_first_thickness/mms_p1_first_thickness_report.md`
**Summary:** `reports/mms_p1_first_thickness/p1_thickness_attempt_summary.json`

### MMS basis reset (2026-03-29)

**Root cause:** Scale mismatch between MMS tetrahedron (~10–34 km in Phase 1/2) and typical near-MP gradient scale (~750–3750 km). Ratio is ~40–100×. Both Phase 1 and Phase 2 are structurally inadequate for extended gradient layers.

**Feasibility probes:** Phase 2 separations checked (20–34 km). Only 2–3× improvement. Insufficient.

**Five-direction comparison:** P3 attempt (not recommended, same barrier), basis reset (useful for documentation), method salvage (not viable), **pause (recommended)**, P1 rescue (not viable).

**Revised reportability criterion:** Gradient spatial scale must be within ~10× of tetrahedron separation. Current MMS can only resolve ~10–100 km features (Phase 1) or ~25–250 km features (Phase 2).

**Primary recommendation: Pause the MMS thickness branch.** The documented scale-mismatch result is a legitimate methodological thesis contribution.

**Full analysis:** `docs/MMS_BASIS_RESET.md`
**Report:** `reports/mms_basis_reset/mms_basis_reset_report.md`

### MMS branch freeze (2026-03-29)

**MMS branch frozen.** No reportable thickness. The scale-mismatch result and revised reportability criterion are preserved as methodological findings.

**Freeze document:** `docs/MMS_BRANCH_FREEZE.md`
**Repo navigation:** `docs/REPO_NAVIGATION_FOR_THESIS.md`
**Reports index:** `reports/INDEX.md`

**Any future MMS reopening requires explicit user authorization.**

## Commands

```bash
# Generate Phase 3A artifacts
PYTHONPATH=src python -m pdl_pilot.cli.generate_phase3a --run-dir runs/20260326T040343Z_d0425fd4

# Generate base evidence package
PYTHONPATH=src python -m pdl_pilot.cli.generate_evidence --run-dir runs/20260326T040343Z_d0425fd4

# Run all tests (124 pass, 1 skip)
PYTHONPATH=src python -m pytest tests/ -v
```

## Collaboration protocol

See `docs/ROLE_PROTOCOL.md` for full role definitions. Summary below.

### Shared inputs (frozen-writing-safe mode)

| Priority | File | Purpose |
|---|---|---|
| 1 | `docs/NEXT_QUESTION.md` | Live control state |
| 2 | `docs/WORKLOG_LATEST.md` | Latest applied round |
| 3 | `docs/LLM_HANDOFF.md` | Consolidated project entry |
| — | Historical evidence artifacts | Provenance/audit only |

Note: `reports/current_bank/RUN_REVIEW_PACKET.md` is a historical Phase 3A artifact preserved for provenance. It is NOT the live control state.

### Roles

- **A** — Section Drafter + Methods/Audit Brain. Drafts section skeletons, methods blocks, safeguard text. Does not set final claims or emit Claude prompts.
- **B** — Lead Integrator + Final Editorial Brain + Final Claude Prompt Emitter. Integrates A + C, decides what enters thesis-facing prose, emits final Claude prompts. May originate bounded repo-safe tasks directly.
- **C** — Science Ceiling Reviewer. Decides what science-facing prose is supportable. Mandatory for results, discussion, abstract, conclusion, and any claim wording. May proactively supply safer substitute wording.
- **Claude Code** — Frozen-Writing-Safe Executor. Edits repo files within green/yellow scope. May perform coherent multi-file documentation work in one pass. Must escalate genuine red decisions.
- **User** — Final authority for red decisions only.

### Authority flow

For science-facing work: A + C (parallel) → B integrates → B emits final prompt → Claude executes.
For repo-safe housekeeping: B → Claude directly.

### Delegated decision authority

**Green — automatic:** protocol cleanup, wording harmonization, file organization, helper templates, thesis-safe section scaffolding from frozen docs, cross-linking, banners, changelog updates.

**Yellow — delegated, recorded in WORKLOG_LATEST:** bounded editorial emphasis within frozen ceiling, file placement for new helpers, protocol refinements that do not alter scientific meaning, B originating repo-safe Claude tasks.

**Red — escalate to user:** reopening any science branch, new search, detector semantics, thresholds, labels, bank changes, measurement-model changes, frozen-claim strengthening, MMS reactivation.

**If uncertain whether something is red, treat it as red.**

### Semantic guardrails

**Forbidden vocabulary:** PDL-positive, non-PDL, baseline, control, truth, threshold, threshold candidate, label, dev-set, detector-ready class.

**Allowed vocabulary:** comparator window, pass, evidence, caveat, review layer, descriptive comparison, primary evidence, secondary evidence with caveats, excluded from core comparison.

## Next step

See `docs/NEXT_QUESTION.md`.
