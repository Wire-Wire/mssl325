# Next Question

**Stage:** Phase 6A audited. Current formulation closed as apparatus-limited pilot.

## Audit outcome

Post-tranche-2 audit found:
1. **Synthetic contamination:** pilot_001 and pilot_002 are synthetic fixtures in the tranche-1 catalogue (SZA=0, hardcoded Dp/Bz/Ma). Effective real N = 9, not 11.
2. **Declared vs searched slice mismatch:** Tranche 2 declared "2007–2010" but searched only Aug–Oct 2008–2009.
3. **No true quasi-radial encounter:** All "low-cone" group encounters have cone > 30°.

**Verdict:** Apparatus-limited pilot stop with broader question still open.

## Active question

**Authorize a Phase 6 reset branch?**

A reset would need to address:
- synthetic fixture exclusion from the encounter universe
- proper archive scope declaration matching actual search
- the dual-bin occupancy constraint that co-excludes low-Dp / low-cone conditions

Current Phase 6A formulation is closed. Phase 6B is not justified. No further science proceeds without explicit reset authorization.

## Decision mode

- `decision_mode`: red (reset authorization requires user)
- `auto_decision_scope`: green only (documentation, formatting)
- `escalate_if`: any new science, search, or analysis
- `final_owner_if_escalated`: User
