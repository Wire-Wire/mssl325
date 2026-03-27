# Next Question

**Stage:** Phase 3B complete. Awaiting user review of retention audit.

## Active question

Phase 3B has been executed. P1 and P3 are both confirmed-cautious. What is the next bounded stage?

## Outcome of Phase 3B

- P1: confirmed-cautious (near-bin density CV=0.93; Dn driven by noisy median)
- P3: confirmed-cautious (EB spike-dependent; mapping sensitivity ±0.23 at Dp=3.1)
- Six-pass bank remains defensible as a descriptive comparator bank
- All low-Dn evidence (Dn < 0.5) remains cautious-only

## Allowed this round

- Human review of the Phase 3B retention audit
- Decision on the next bounded stage
- No scope beyond the existing six-pass bank without explicit authorization

## Forbidden this round

- Thresholds, labels, detector semantics, dev-set membership
- Promotion of P1 or P3 to clean
- New window expansion, MMS thickness, SMILE/SXI priors
- Changes to the frozen measurement model
- Use of upgrade, unchanged, clean, detector-ready, or any strengthening vocabulary

## Sign-off condition

User confirms Phase 3B audit and names the next stage (or requests a specific follow-up).

## Decision mode

- `decision_mode`: red (next-stage decision requires user authorization)
- `auto_decision_scope`: green actions only
- `escalate_if`: any proposed next step
- `final_owner_if_escalated`: User
