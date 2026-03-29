# Repo Navigation for Thesis Writing

**Purpose:** Help a thesis writer quickly find the right materials and know what to ignore.

---

## A. Directory map

### Frozen science layers (cite from these)

| Directory | What it contains | Status |
|---|---|---|
| `docs/THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` | **Start here.** Thesis-body results block for THEMIS comparator + recurrence branch. | Frozen, writing-safe |
| `docs/MMS_BRANCH_FREEZE.md` | MMS branch freeze document with thesis-safe wording block. | Frozen, writing-safe |
| `docs/PHASE_4B_RESULTS_FREEZE.md` | THEMIS branch freeze with strongest claims/non-claims and safe sentences. | Frozen |
| `reports/current_bank/` | THEMIS bank evidence: per-pass sheets, figures, comparison reports. | Frozen |
| `reports/mms_p1_first_thickness/` | MMS-P1 thickness attempt: evidence panel, summary JSON, report. | Frozen |
| `reports/mms_basis_reset/` | MMS basis-reset diagnosis report. | Frozen |

### Historical process records (cite for methods provenance only)

| Directory | What it contains | Status |
|---|---|---|
| `docs/PHASE_2A_STATE.md` through `docs/PHASE_3B_*` | Stage-by-stage audit trail for THEMIS branch. | Historical |
| `docs/PHASE_4A_INDEPENDENT_LOWDN_RECURRENCE.md` | THE Sep 19 cross-probe recurrence test. | Historical |
| `docs/MMS_THICKNESS_METHOD_SCAFFOLD.md` | MMS methods scaffold (eligible for methods-chapter citation). | Historical/methods |
| `docs/MMS_EVENT_SHORTLIST.md` | MMS shortlist screening process. | Historical |
| `docs/MMS_EVENT_PACKAGES_READINESS_AUDIT.md` | MMS event-package readiness analysis. | Historical |
| `docs/MMS_P1_FIRST_THICKNESS_ATTEMPT.md` | Full MMS-P1 thickness attempt analysis. | Historical |
| `docs/MMS_BASIS_RESET.md` | Root-cause diagnosis after P1 failure. | Historical |
| `reports/mms_shortlist/` | MMS screening registry, quicklooks, candidate cards. | Historical |
| `reports/mms_event_packages/` | MMS event cards, readiness matrix, evidence panels. | Historical |

### Control/coordination files (do not cite as results)

| File | Purpose |
|---|---|
| `docs/LLM_HANDOFF.md` | Session entry point for AI conversations. |
| `docs/NEXT_QUESTION.md` | Current control state (frozen). |
| `docs/WORKLOG_LATEST.md` | Latest round summary. |
| `docs/EVIDENCE_REPORT_SCHEMA.md` | Schema for machine-readable evidence outputs. |

### Code / config / runtime (for reproducibility)

| Directory | Purpose |
|---|---|
| `src/pdl_pilot/` | Pipeline code (31 Python files). Frozen. |
| `configs/` | YAML configs for synthetic pilots, live pilots, candidates, families, usable bank. |
| `runs/` | Runtime outputs (27 run directories). Contains encounter JSONs, QC PNGs, manifests. |
| `data_cache/` | Cached CDAWeb downloads. For reproducibility. |
| `tests/` | 124 passing tests. |
| `RP/` | Internal research blueprint. |

---

## B. What to read first when writing

1. **`docs/THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md`** — the THEMIS results block. Contains the evidence ledger, exact supportable statements, limitations, and traceability note.

2. **`docs/MMS_BRANCH_FREEZE.md`** — the MMS methods/limitation block. Contains what was learned, what failed, and the safe wording block.

3. **`docs/PHASE_4B_RESULTS_FREEZE.md`** — the THEMIS freeze document with strongest claims and do-not-say examples.

4. **`reports/current_bank/figures/`** — the two main THEMIS figures:
   - `phase3a_dneb_comparison.png` (Dn vs EB comparison)
   - `phase4a_lowdn_recurrence.png` (independent recurrence)

5. **`reports/mms_p1_first_thickness/figures/p1_evidence_panel.png`** — the MMS-P1 evidence panel.

---

## C. What is frozen vs historical vs live

| Category | What it means | Examples |
|---|---|---|
| **Frozen** | Writing-safe. Citable as thesis results or methods. Will not change. | Thesis block, freeze docs, bank reports, MMS freeze |
| **Historical** | Documents the process that led to frozen results. Cite only for provenance/methods. | Phase docs, audit docs, shortlist records |
| **Live (code/config)** | Still executable. For reproducibility, not direct citation. | `src/`, `configs/`, `tests/` |
| **Control** | AI/human coordination. Do not cite. | `LLM_HANDOFF.md`, `NEXT_QUESTION.md`, `WORKLOG_LATEST.md` |

---

## D. Quick reference: what goes where in the thesis

| Thesis section | Primary sources |
|---|---|
| **Results: THEMIS comparator bank** | `THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md`, `PHASE_4B_RESULTS_FREEZE.md` |
| **Results: figures** | `reports/current_bank/figures/` |
| **Methods: THEMIS measurement model** | `RP/internal_master_research_blueprint_PDL_SMILE.md` §5–6, `src/pdl_pilot/` |
| **Methods: MMS thickness approach** | `MMS_THICKNESS_METHOD_SCAFFOLD.md`, `MMS_BRANCH_FREEZE.md` |
| **Discussion: MMS limitation** | `MMS_BRANCH_FREEZE.md` §3–5, `MMS_BASIS_RESET.md` |
| **Discussion: selection function** | `SELECTION_FUNCTION_AUDIT.md` |
| **Discussion: confounders** | `PHASE_2C_CONFOUNDER_CLOSURE.md`, `PASS_INTERVAL_AUDIT.md` |
