> **USAGE:** This file records what changed in the most recent applied round. It is secondary to `docs/NEXT_QUESTION.md`. Do not use this file alone to infer the current project stage. If conflict exists, `docs/NEXT_QUESTION.md` wins.

> **Current-state echo:** Phase 6 Route C FULL EXP complete. SUCCESS. 4 quasi-radial + 16 low-cone retained. Awaiting user decision. See `docs/NEXT_QUESTION.md`.

# Worklog — Latest Round

**Date:** 2026-03-31
**Round:** Phase 6 Route C FULL EXP (user-authorized full-archive experiment)

## What changed

### FULL EXP executed

Full-archive scan of all THEMIS 2007-2010, Jul-Nov, all 5 probes via CDAWeb. Multi-threaded (8 workers). 90 (year, month, probe) combinations searched. 2083 near-subsolar qualifying days processed. Original Dn/EB semantics.

### Result: SUCCESS

- 148 unique retained encounters (Dn/EB computable)
- 4 quasi-radial (cone < 30 deg): 2007-08-08 THA (25.2), 2007-08-12 THA (29.0), 2009-07-25 THB (22.2), 2009-08-10 THC (19.7)
- 16 low-cone (30-45 deg): from THA/THB/THC/THD/THE across 2007-2009
- 44 intermediate, 84 perpendicular
- Both success conditions met

### Key finding

Quasi-radial and low-cone encounters come from THA/THB/THC at Dp 0.8-1.7 nPa — probes with larger orbital reach not previously searched. Cross-probe comparability with Phase 4B THD bank not yet validated.

### All earlier Phase 6 layers frozen as historical context

Phase 6A tranches, Route A repair, Route B sidecar, prior local-only Route C — all preserved, not rewritten.

## Files created

- `docs/PHASE_6_FULL_EXP_ACTIVATION.md`
- `docs/PHASE_6_ROUTEC_FULL_EXP_PLAN.md`
- `docs/PHASE_6_ROUTEC_FULL_EXP_RESULT.md`
- `reports/themis_conditioning/routeC_exp/` (scope_manifest, selection_flow, catalogue JSON/CSV, summary)
- `scripts/phase6_routeC_full_exp.py`
- `data_cache/routeC_exp_state/` (90 monthly STATE files)
- `data_cache/routeC_exp_enc/` (1691+ encounter caches)

## Files modified

- `docs/NEXT_QUESTION.md` — FULL EXP SUCCESS, three-option menu
- `docs/WORKLOG_LATEST.md` — this file
- `docs/LLM_HANDOFF.md` — FULL EXP block added

## Frozen anchors unchanged

Phase 4B, 5A/5B, MMS — all intact. Route B frozen sidecar. No thresholds, labels, or detector semantics.
