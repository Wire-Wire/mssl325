# Control-State Precedence

> This document defines read-order and conflict rules. It does not itself define the current stage. For live state, read `docs/NEXT_QUESTION.md` first.

---

## Precedence order

| Priority | File | Role |
|---|---|---|
| **1** | `docs/NEXT_QUESTION.md` | **Live control state.** Current mode, active question, allowed/forbidden actions. |
| **2** | `docs/WORKLOG_LATEST.md` | Latest applied round. What changed most recently. |
| **3** | `docs/LLM_HANDOFF.md` | Consolidated project context. Read after NEXT_QUESTION and WORKLOG. |
| **4** | Historical artifacts | Provenance and audit traceability only. |

## What counts as a historical artifact

Any document produced during a completed stage that is no longer the active control surface:

- `reports/current_bank/RUN_REVIEW_PACKET.md` — Phase 3A review packet
- `docs/PHASE_2B_AUDIT.md`, `PHASE_2C_*`, `PHASE_2D_*` — stage audits
- `docs/PHASE_3A_*`, `PHASE_3B_*` — stage records
- `docs/PHASE_4A_*` — recurrence test record
- `docs/MMS_EVENT_SHORTLIST.md`, `MMS_EVENT_PACKAGES_READINESS_AUDIT.md`, `MMS_P1_FIRST_THICKNESS_ATTEMPT.md`, `MMS_BASIS_RESET.md` — MMS branch stage records
- `docs/DECISION_LOG.md`, `docs/CHANGESET_LATEST.md` — operational logs

These are preserved for traceability. They must NOT override the live control state.

## Frozen result documents (citable, but not control)

These are the thesis-writing entry points. They contain the final frozen claims and non-claims:

- `docs/THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` — THEMIS results block
- `docs/PHASE_4B_RESULTS_FREEZE.md` — THEMIS branch freeze
- `docs/MMS_BRANCH_FREEZE.md` — MMS branch freeze

## Rule

If a historical artifact and a live control file disagree, the live control file wins. If a frozen result document and a historical stage record disagree on wording, the frozen result document reflects the final audited state.
