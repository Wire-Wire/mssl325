# Next Question

**Stage:** Phase 4A complete. Awaiting user review.

## Active question

Phase 4A independent low-Dn recurrence test is complete. One cross-probe recurrence found (THE Sep 19, Dn = 0.76) below the clean-core floor but above the cautious range. No independent recurrence of Dn < 0.5. What is the next bounded stage?

## Outcome of Phase 4A

- 4 independent candidates tested (2 cross-probe THE, 1 different-year THD 2010, 1 same-probe different-date)
- 2 PASS, 2 FAIL_OCCUPANCY
- THE Sep 19 2008: Dn = 0.76, below clean-core floor (0.94), cross-probe independence
- THD Oct 23 2010: Dn = 1.30, not low-Dn
- No independent candidate reaches Dn < 0.5
- Dn < 0.5 remains cautious-only under the current apparatus

## Allowed this round

- User review of Phase 4A results
- Decision on next bounded stage
- Decision on whether THE Sep 19 should be admitted to the main bank (red decision)

## Forbidden this round

- Thresholds, labels, detector semantics, dev-set membership
- Auto-admission of any candidate to the main bank
- Changes to the frozen measurement model

## Decision mode

- `decision_mode`: red (next-stage decision requires user authorization)
- `auto_decision_scope`: green actions only
- `escalate_if`: any proposed next step
- `final_owner_if_escalated`: User
