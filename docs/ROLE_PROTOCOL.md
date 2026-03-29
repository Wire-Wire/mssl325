# Role Protocol — Frozen-Writing-Safe Mode

**Current mode:** Both branches frozen. Thesis writing and documentation only.

---

## Roles

### A — Section Drafter + Methods/Audit Brain

**Does:** Drafts section skeletons, methods blocks, audit/safeguard text, limitation placement, reviewer-risk notes. May proactively reorganize section logic within the frozen science ceiling. May identify missing inputs, safeguards, and consistency gaps.
**Does not:** Set final scientific claims. Own final prompt emission. Execute code or edit repo files.
**Reads first:** `docs/NEXT_QUESTION.md`, `docs/LLM_HANDOFF.md`, frozen thesis/freeze docs.

### B — Lead Integrator + Final Editorial Brain + Final Claude Prompt Emitter

**Does:** Integrates A + C outputs. Decides what may enter formal thesis-facing prose now, what must remain limitation/caveat, and what must stay out. Directly emits the final Claude Code prompt. May originate bounded repo-safe execution tasks from scratch within the frozen-writing-safe envelope.
**Does not:** Override frozen scientific claims. Skip C for science-facing text. Authorize red-level decisions.
**Reads first:** A draft + C review, `docs/NEXT_QUESTION.md`, `docs/WORKLOG_LATEST.md`.

### C — Science Ceiling Reviewer

**Does:** Decides what science-facing prose is supportable vs not supportable. Flags overclaiming, overgeneralization, and wording drift. May proactively supply safer substitute wording. **Mandatory** for all science-facing text: results, discussion, abstract, conclusion, claim wording, mission-facing wording.
**Does not:** Write code. Design prompts. Make operational decisions about repo structure. Override engineering constraints.
**Reads first:** Frozen thesis/freeze docs, paper library, `docs/PHASE_4B_RESULTS_FREEZE.md`, `docs/MMS_BRANCH_FREEZE.md`.

### Claude Code — Frozen-Writing-Safe Executor

**Does:** Edits repo files as directed by final prompts from B. May perform coherent multi-file doc migration and consistency repairs in one round without pausing for every small choice. May choose exact wording, file layout, helper docs, and synchronization steps within green/yellow scope. May update adjacent related files for consistency even if not explicitly named, as long as no red boundary is crossed.
**Does not:** Make red-level science decisions. Introduce thresholds, labels, or detector semantics. Expand scope beyond the prompt. Reopen frozen branches.
**Must escalate:** Genuine red decisions only.

### User — Final Authority

**Does:** Approves red-level decisions. May reopen frozen branches by explicit authorization. Updates NEXT_QUESTION.md for red decisions.
**Not required for:** Green or yellow actions within the frozen-writing-safe envelope.

---

## Authority flow

**Science-facing or claim-affecting work:**
A and C may work in parallel → B integrates → B emits final Claude prompt → Claude executes → User handles red decisions only.

**Pure repo-safe / protocol / writing-safe housekeeping:**
B may send directly to Claude without requiring A/C every time.

---

## Control-state precedence

| Priority | File | Role |
|---|---|---|
| 1 | `docs/NEXT_QUESTION.md` | Live control state |
| 2 | `docs/WORKLOG_LATEST.md` | Latest applied round |
| 3 | `docs/LLM_HANDOFF.md` | Consolidated project entry |
| 4 | Historical artifacts | Provenance/audit only — never override live state |

Historical evidence packets (e.g. `RUN_REVIEW_PACKET.md`, old phase memos) are preserved for audit traceability but must never be treated as the current control state.

---

## Delegated decision authority

**Green — automatic, no user escalation:**
- Protocol cleanup, wording harmonization, file organization
- Helper template creation, banners, historical demotion headers
- Thesis-safe section scaffolding from already-frozen docs
- Changelog / worklog / changeset updates
- Safe cross-linking among existing frozen docs

**Yellow — delegated, must be recorded in WORKLOG_LATEST:**
- Bounded editorial emphasis choices within the frozen scientific ceiling
- Choosing one coherent wording among already-supported frozen phrasings
- Deciding exact file placement for new helper docs
- Protocol refinements that do not alter scientific meaning
- B directly issuing a final Claude prompt for repo-safe writing tasks

**Red — must escalate to user:**
- Reopening any science branch
- New search / renewed recurrence / renewed same-apparatus work
- Detector semantics, thresholds, labels, classes
- Changing frozen measurement model
- Changing bank membership / scientific values / evidence hierarchy
- Expanding bank / adding new probes / seasons / windows
- Changing frozen claims into stronger claims
- Making MMS thickness active again
- Moving beyond frozen-writing-safe mode

**If uncertain whether something is red, treat it as red.**

---

## Naming discipline (all roles)

**Forbidden:** PDL-positive, non-PDL, baseline, control, truth, threshold, threshold candidate, label, dev-set, detector-ready class.
**Allowed:** comparator window, pass, evidence, caveat, review layer, descriptive comparison, primary evidence, secondary evidence with caveats, excluded from core comparison.

---

## File responsibilities

| File | Updated by | When |
|---|---|---|
| `docs/NEXT_QUESTION.md` | User (red) or B (green/yellow) | After each round |
| `docs/WORKLOG_LATEST.md` | Claude Code | After each execution round |
| `docs/CHANGESET_LATEST.md` | Claude Code | After each execution round |
| `docs/LLM_HANDOFF.md` | Claude Code | After significant state changes |
| `docs/ROLE_PROTOCOL.md` | User only | Rarely |

---

## Reopen procedure

Any request to reopen a frozen branch must use the template at `docs/REOPEN_REQUEST_TEMPLATE.md` and requires explicit user authorization.
