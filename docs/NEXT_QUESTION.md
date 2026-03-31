> **THIS FILE IS THE LIVE CONTROL STATE.**
> Read this file first. If any other file in the repo conflicts with this file's stage, question, or blocking status, this file wins. Do not infer the current project stage from any other document.

# Next Question

**Stage:** Phase 6 Route C FULL EXP complete. SUCCESS. Both target cone bins populated. Awaiting user decision on next step.

## FULL EXP result

Full-archive scan of all THEMIS 2007-2010, Jul-Nov, all 5 probes, SZA <= 30 deg. No convenience subsampling. 2083 encounters processed. 148 retained (Dn/EB computable).

| Cone bin | Retained | Target met? |
|---|---|---|
| quasi-radial (< 30 deg) | **4** | YES (>= 1) |
| low-cone (30-45 deg) | **16** | YES (>= 5) |
| intermediate (45-60 deg) | 44 | context |
| perpendicular (> 60 deg) | 84 | context |

Key finding: quasi-radial and low-cone encounters come from THA/THB/THC at Dp 0.8-1.7 nPa — a regime not accessible to THD. Cross-probe comparability with the Phase 4B THD bank is not yet established.

## Active question

**Does the user want to:**

| Option | What it does | Key caveat |
|---|---|---|
| **A** | Package FULL EXP into thesis-safe cone-angle-stratified descriptive comparison | Cross-probe comparability not yet validated |
| **B** | Authorize further Phase 6 science (e.g., cross-probe QC, calibration check) | Scope expansion beyond current EXP |
| **C** | Return to writing-safe mode with FULL EXP as documented finding | Safest; comparison deferred to future work |

See `docs/PHASE_6_ROUTEC_FULL_EXP_RESULT.md` for full details.

## Blocked

- Phase 6B (occurrence / detector / thresholds / labels / classes)
- Route B continuation (frozen sidecar)
- Modification of frozen Phase 4B / 5A / 5B / MMS

## Decision mode

- `decision_mode`: red
- `escalate_if`: any scope expansion, cross-probe validation, or phase closure
- `final_owner_if_escalated`: User
