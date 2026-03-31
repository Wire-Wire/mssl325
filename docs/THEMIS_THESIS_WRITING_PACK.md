# THEMIS Thesis-Writing Pack

**Purpose:** Primary thesis-entry hub for THEMIS writing. Organizes the claim-bearing layer, editorial sidecars, figures, tables, and wording discipline into one navigable surface.

This document is editorial navigation only. It contains no new scientific claims.

---

## 1. Purpose and scope

This hub exists so a thesis writer can:
- find the claim-bearing THEMIS results quickly
- know which sidecars illustrate but do not strengthen those results
- place figures and tables without citation drift
- avoid wording that exceeds the frozen ceiling

It does NOT replace the frozen science documents. It routes to them.

---

## 2. Source hierarchy for thesis writing

| Layer | Role | Documents | Citability |
|---|---|---|---|
| **Claim-bearing** | Defines what is supported and not supported | `THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md`, `PHASE_4B_RESULTS_FREEZE.md` | **Primary thesis citation source** |
| **Editorial sidecar** | Illustrates / organizes, does not strengthen | `THEMIS_CASESET.md` (Phase 5A), `PHASE_5B_CASESET_DESCRIPTIVE_PASS.md` | Cite for illustration/appendix only |
| **Bounded descriptive sidecar** | Archive-level result, does not strengthen Phase 4B | `PHASE_6_FULL_EXP_FREEZE.md` | Thesis sidecar (bounded ceiling) |
| **Navigation / data** | Figures, tables, machine-readable summaries | `reports/current_bank/figures/`, `reports/themis_caseset/`, `caseset_summary.json` | Reference for figures and tables |
| **Historical provenance** | Process records, audit trail | Old phase docs (2B–4A), `RUN_REVIEW_PACKET.md`, `PHASE_5B_CASESET_DESCRIPTIVE_INVENTORY.md` | Methods provenance only |
| **Control** | Workflow state | `NEXT_QUESTION.md`, `WORKLOG_LATEST.md`, `LLM_HANDOFF.md` | Do not cite in thesis |

**Key distinctions:**
- Phase 4B answers *what is supported.* Phase 5A shows *what screened examples look like.* Phase 5B shows *how those examples sit in coarse clock-angle buckets.* None of the sidecars strengthen the frozen claims.
- `PHASE_5B_CASESET_DESCRIPTIVE_PASS.md` is the active Phase 5B thesis-sidecar source. `PHASE_5B_CASESET_DESCRIPTIVE_INVENTORY.md` is a historical/superseded variant not on the primary thesis path.

---

## 3. Recommended THEMIS thesis subsection structure

### Main results block (claim-bearing)

**Source:** `THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md`

Content:
- Frozen comparator bank (6 passes: 4 clean core + 2 cautious)
- Clean-core Dn/EB span (0.94–2.31 / 0.80–1.96)
- Cautious low-Dn extension (P1: 0.12, P3: 0.39, both with interval-level caveats)
- Independent external recurrence (THE Sep 19, Dn = 0.76, external only)
- Exact supportable statements
- Limitations carried forward

### Carried-forward ceiling / non-claims

**Source:** `PHASE_4B_RESULTS_FREEZE.md` §C

Content:
- No physical identification
- No threshold or detection semantics
- No generalization beyond compressed-sheath THD
- Cautious-only character of all Dn < 0.5 evidence

### Phase 5A case-atlas confirmation layer (editorial sidecar)

**Source:** `THEMIS_CASESET.md`

Content:
- 8 cases screened from frozen seed pass
- 4 reviewed as clear, 1 ambiguous, 2 not convincing, 1 screen fail
- Standardized cards with upstream context and sheath-side indicators
- Atlas-usable subset for appendix illustration

### Phase 5B grouped descriptive sidecar (editorial sidecar)

**Source:** `PHASE_5B_CASESET_DESCRIPTIVE_PASS.md`

Content:
- Compact grouped table by clock-angle bin
- Coverage/empty-bin note (<60° sparse)
- Conservative takeaway: descriptive caseset bookkeeping only

### Phase 6: Full-archive upstream-conditioning exploration (bounded descriptive-methodological sidecar)

**Source:** `PHASE_6_FULL_EXP_FREEZE.md`

Content:
- Full-archive scan result: 757 encounters evaluable under original Dn/EB across all cone bins
- Quasi-radial (28) and low-cone (89) bins now populated — previously empty in Phase 4B
- Cross-probe comparability with frozen THD bank NOT validated
- Mandatory caveats: different probes, different Dp regime, wider Dn/EB range of unresolved origin
- Thesis-safe conclusion: the bins are fillable; direct cross-regime comparison deferred to future work

**Ceiling:** Phase 6 does NOT strengthen frozen Phase 4B claims. It does NOT validate cone-angle-dependent descriptor behavior. It is a bounded descriptive-methodological result showing archive-level fillability. It should NOT be cited as a validated cone-angle physics comparison.

**Wording patterns:**
- "bounded full-archive descriptive result"
- "the quasi-radial and low-cone bins are evaluable under the original measurement family"
- "cross-probe comparability remains unvalidated"
- "a direct physical comparison across cone-angle regimes is deferred to future work"

**Do NOT say:**
- "Phase 6 extends / validates / strengthens Phase 4B"
- "low-cone encounters show / lack PDL signatures"
- "cone angle controls / modulates depletion behavior"
- "the full archive confirms cone-angle dependence"

### Traceability / appendix bridge

**Source:** `THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` traceability note + `REPO_NAVIGATION_FOR_THESIS.md`

Content:
- Stage provenance (Phases 2a–4B)
- Machine-readable artifact locations
- Reproducibility pointers

---

## 4. Figure and table placement map

### Recommended main-text items

| Label | Source | Content |
|---|---|---|
| **Figure T1** | `reports/current_bank/figures/phase3a_dneb_comparison.png` | Dn vs EB comparison across 6 interpretable passes |
| **Figure T2** | `reports/current_bank/figures/phase4a_lowdn_recurrence.png` | Independent recurrence: THE Sep 19 in Dn/EB space |
| **Table T1** | Condensed from `THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` frozen evidence ledger | 7-row ledger: P1–P6 + EXT with Dn, EB, status |
| **Table T2** | Condensed from `PHASE_5B_CASESET_DESCRIPTIVE_PASS.md` grouped table | 3-row grouped inventory: <60° / 60–120° / >120° |

### Recommended appendix items

| Item | Source | Content |
|---|---|---|
| 5 atlas-usable Phase 5A cards | `reports/themis_caseset/cases/` (P3, P4, P5, EXT, P6) | Standardized crossing figures + upstream context |
| Non-usable case note | `reports/themis_caseset/cases/` (P2, P7, P1) | Brief: P2 not convincing (indicators reversed), P7 not convincing (spike-dominated), P1 screen fail (quasi-radial) |
| Crossing quicklook figures | `reports/themis_caseset/figures/` | One per atlas-usable card |

Do NOT promote the full eight-card atlas into the main thesis text by default. The main text should reference the grouped summary; individual cards belong in the appendix.

---

## 5. Role labels and wording discipline

### Role of each layer

| Document | Role in thesis | What it may support |
|---|---|---|
| `THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` | Results claims | "The clean core spans Dn 0.94–2.31" |
| `PHASE_4B_RESULTS_FREEZE.md` | Non-claims / ceiling | "No threshold is defined or implied" |
| `THEMIS_CASESET.md` | Illustration | "Eight cases were screened; four were reviewed as clear" |
| `PHASE_5B_CASESET_DESCRIPTIVE_PASS.md` | Grouped illustration | "Atlas-usable cases appear in the 60–120° and >120° bins" |

### Required wording patterns

When citing Phase 5A/5B:
- "reviewed as clear / ambiguous / not convincing" (always attach "review status")
- "within this small seed-derived caseset"
- "grouped descriptive inventory only"
- "editorial packaging, not scientific confidence class"

When citing EXT:
- "external recurrence only"
- "not admitted to the main bank"

When citing frozen results:
- "under the frozen measurement model"
- "cautious-only evidence with documented interval-level caveats"

---

## 6. Do-not-say block

The following are blocked for THEMIS thesis writing under the current frozen ceiling:

| Blocked | Why |
|---|---|
| "The low-Dn passes demonstrate the presence of a plasma depletion layer" | No physical identification is supported |
| "Clear cases are PDL cases / positive examples" | Review statuses are not physical classes |
| "High clock angle favors depletion / pileup signatures" | No conditioned rates or trends from N=8 caseset |
| "The <60° regime lacks real events" | Sparse coverage is not a concluded absence |
| "Dn < 1 with EB > 1 separates convincing from non-convincing" | No threshold or rule is defined |
| "The cross-probe recurrence validates the detection pipeline" | No detector semantics exist |
| "The six-pass bank constitutes a development set" | No dev-set membership is assigned |
| "Absence of independent Dn < 0.5 means such behavior is physically rare" | Absence may reflect selection-function limits |

---

## 7. Navigation notes

| Document | Thesis-route status |
|---|---|
| `THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` | **Primary claim-bearing source** |
| `PHASE_4B_RESULTS_FREEZE.md` | **Primary ceiling/non-claims source** |
| `THEMIS_CASESET.md` | Active Phase 5A sidecar |
| `PHASE_5B_CASESET_DESCRIPTIVE_PASS.md` | **Active Phase 5B sidecar** |
| `PHASE_5B_CASESET_DESCRIPTIVE_INVENTORY.md` | Historical/superseded — not on primary thesis path |
| `RUN_REVIEW_PACKET.md` | Historical Phase 3A artifact — off thesis-results route |
| Old phase docs (2B–4A) | Historical provenance only |
| `MMS_BRANCH_FREEZE.md` | Separate MMS methods/limitation block |
