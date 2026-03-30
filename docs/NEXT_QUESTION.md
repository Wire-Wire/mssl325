> **THIS FILE IS THE LIVE CONTROL STATE.**
> Read this file first. If any other file in the repo conflicts with this file's stage, question, or blocking status, this file wins. Do not infer the current project stage from any other document.

# Next Question

**Stage:** Phase 6 post-Route-B. Route A complete. Route B bounded execution complete. Routes C and D not executed. Writing-safe return is a live option. Phase 6B blocked.

## What was done this round

Decision-space repair only. No new science execution.

The previous three-option menu (close B / open C / close Phase 6) did not represent the actual decision space. It omitted Route D (branch-question narrowing) and misframed writing-safe return as "close Phase 6 entirely." This round repaired the menu to reflect all four live post-Route-B options.

See `docs/PHASE_6_POST_ROUTEB_DECISION_MEMO.md` for full decision blocks.

## Route B bounded execution (completed previous round)

- Dn_near and D|B|_near computed on 5 Route-B-computable encounters (4 tranche-1 + 1 tranche-2 recovered)
- 3/5 show inner-sheath depletion gradient (Dn_near < 1 AND D|B|_near > 1)
- Recovered low-cone encounter (t2_20080904_thd, cone=43deg): no depletion (flat profile)
- Route B descriptors are NOT Dn/EB. Not interchangeable with frozen Phase 4B.
- Modest but nonzero descriptive yield. Does not extend regime coverage.

## Active question

**Which of the four post-Route-B options should be authorized next?**

| Option | Label | What it does | Main risk |
|---|---|---|---|
| **A** | Route B continuation | Refine or expand inner-sheath descriptor; search for more vn-occupied encounters | Diminishing returns; yield already known to be modest |
| **B** | Route C execution | Search unsearched 2007-2010 archive for low-cone encounters evaluable under original Dn/EB | Low-cone + high-Dp co-occurrence may be physically rare; may reproduce tranche-2 null |
| **C** | Route D-style narrowing | Narrow to within-regime stratification on accessible N=9 sample | N=9 may be too sparse; may just repackage Phase 4B |
| **D** | Writing-safe return | Accept Phase 6 as methodological finding; return to thesis writing | Lowest yield; no new science results beyond documented limitation |

Full decision blocks with scientific ceilings, preservation/sacrifice trade-offs, and first executable actions are in `docs/PHASE_6_POST_ROUTEB_DECISION_MEMO.md`.

## Blocked

- Phase 6B (occurrence / detector-preparatory / thresholds / labels / classes)
- No further science execution without explicit user authorization
- No modification of frozen Phase 4B, 5A/5B, or MMS branch

## Decision mode

- `decision_mode`: red
- `auto_decision_scope`: green only
- `escalate_if`: any science execution, route choice, or phase closure
- `final_owner_if_escalated`: User
