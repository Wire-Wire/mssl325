> **THIS FILE IS THE LIVE CONTROL STATE.**
> Read this file first. If any other file in the repo conflicts with this file's stage, question, or blocking status, this file wins. Do not infer the current project stage from any other document.

# Next Question

**Stage:** Phase 6 Route 3 activated. Route A complete. Route B regression tested. Awaiting user choice.

## What was done this round

1. **Route A (mandatory repair):** 2 synthetic fixtures removed. Clean catalogue: N = 9 real encounters. Scope-match manifest produced.
2. **Route B (regression test):** Auxiliary near-MP descriptor (very_near / near ratio) tested on 12 encounters. 1 low-cone encounter recovered (t2_20080904_thd, cone = 43°). Marginal viability.

## Active question

**Route B recovers 1 low-cone encounter. Is that sufficient to proceed, or should Route C (broader search) be authorized instead?**

| Option | What it does | Trade-off |
|---|---|---|
| **Authorize bounded Route B execution** | Use the auxiliary descriptor on the clean universe + 1 recovered low-cone encounter | Only 1 new data point; descriptor not comparable to Phase 4B Dn/EB |
| **Authorize Route C** | Broader archive search preserving original Dn/EB | Requires new CDAWeb search; may hit same Dp co-occurrence limit |

## Blocked

- Phase 6B, detector/threshold/label/class/prior work
- No further science without explicit user authorization

## Decision mode

- `decision_mode`: red
- `auto_decision_scope`: green only
- `escalate_if`: any science execution
- `final_owner_if_escalated`: User
