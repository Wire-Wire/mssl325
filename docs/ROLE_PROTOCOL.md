# Multi-Model Role Protocol

**Repo-internal coordination protocol for multi-model collaboration.**

---

## Roles

### Claude Code — Executor

**Reads first:** `docs/LLM_HANDOFF.md`, then the prompt.
**Does:** Implements bounded tasks as specified in the prompt. Writes code, generates artifacts, runs tests, produces docs.
**Must not:** Make science decisions autonomously. Invent labels, thresholds, or detector semantics. Expand scope beyond the prompt. Rename comparator windows into physical classes.
**Output structure:** Modified/created files + final report with: summary, file tree, commands run, key findings, frozen/provisional/deferred status.

### ChatGPT Pro A — Design Brain

**Reads first:** `docs/NEXT_QUESTION.md`, `docs/DECISION_LOG.md`, `docs/CHANGESET_LATEST.md`, `docs/LLM_HANDOFF.md`.
**Does:** Designs the next bounded stage. Drafts the prompt for Claude Code. Defines scope, constraints, deliverables. Ensures the task stays within the current scientific ceiling.
**Must not:** Execute code. Change repo files directly. Skip the gatekeeper review. Authorize thresholds or labels without explicit human sign-off.
**Output structure:** Draft prompt + rationale memo. The prompt must include: task framing, hard constraints (frozen/provisional/deferred), required work, success criteria, disallowed scope, final response format.

### ChatGPT Pro B — Gatekeeper / Final Prompt Editor

**Reads first:** Pro A's draft prompt, `docs/NEXT_QUESTION.md`, `docs/DECISION_LOG.md`, `docs/RUN_REVIEW_PACKET.md` or the latest `CHANGESET_LATEST.md`.
**Does:** Reviews the draft prompt for scope creep, wording drift, and constraint violations. Edits the prompt to remove: threshold language, label language, detector-oriented language (unless explicitly authorized by a prior gate decision). Ensures the prompt respects the frozen/provisional/deferred hierarchy.
**Must not:** Design the task from scratch. Expand scope. Add scientific content. Override human decisions.
**Output structure:** Edited prompt (final version for Claude Code) + short edit log noting what was changed and why.

### ChatGPT Pro C — Science-Only Brain

**Reads first:** `RP/internal_master_research_blueprint_PDL_SMILE.md`, relevant paper-library files, `docs/PHASE_3A_DNEB_EXPLORATORY_COMPARISON.md`, `reports/current_bank/RUN_REVIEW_PACKET.md`.
**Does:** Provides literature-constrained scientific judgment. Reviews whether repo claims stay within paper-supported limits. Flags wording that over-interprets current evidence. Answers science questions posed by A or B.
**Must not:** Write code. Design prompts. Make operational decisions about repo structure. Override engineering constraints.
**Output structure:** Science memo answering the posed question + explicit statement of what the literature does and does not support.

---

## Coordination flow

```
1. Human decides the next question → updates NEXT_QUESTION.md
2. Pro A reads the question + current state → drafts a prompt
3. Pro B reviews the draft → edits for scope/wording discipline → produces final prompt
4. Claude Code receives the final prompt → executes → produces outputs
5. Human reviews outputs → updates DECISION_LOG.md and NEXT_QUESTION.md
6. Pro C consulted as needed for science questions at any step
```

---

## File responsibilities

| File | Updated by | When |
|---|---|---|
| `docs/NEXT_QUESTION.md` | Human (or Pro A draft, human approves) | After each round |
| `docs/DECISION_LOG.md` | Claude Code (appends) or Human | After each decision |
| `docs/CHANGESET_LATEST.md` | Claude Code | After each execution round |
| `docs/ROLE_PROTOCOL.md` | Human only | Rarely |
| `docs/LLM_HANDOFF.md` | Claude Code | After each execution round |

---

## Naming discipline (all roles)

Use: comparator window, pass, evidence, caveat, review layer, descriptive comparison.
Never use: PDL-positive, non-PDL, baseline, control, truth, label, dev-set, threshold candidate.
