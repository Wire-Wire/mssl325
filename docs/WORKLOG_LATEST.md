# Worklog — Latest Round

**Date:** 2026-03-28
**Round:** Thesis block wording revision (writing-safe repair only)

## What changed

Revised `docs/THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` to address five targeted wording issues identified by external scientific review. No scientific evidence values, bank membership, or stage status changed.

## Wording repairs made

1. **Limitations §1:** Removed "lower-Dp conditions may be more relevant for classical magnetic pileup under reduced reconnection rates" — replaced with "lower-Dp conditions are structurally excluded … not assessed here." This prevents the results block from implying a physics inference not directly established by the frozen comparator results.

2. **External recurrence section:** Restructured to lead with "one external recurrence record exists outside the main bank" before stating what it adds and does not add. Added explicit sentence: "does not independently validate the cautious-only Dn < 0.5 branch."

3. **Traceability note:** Compressed from 3 paragraphs to 3 sentences. Removed internal repo phase labels and file paths from the main narrative. Kept P7 exclusion rationale and audit-trail reference.

4. **Running prose:** Changed "confirmed-cautious passes" / "confirmed-cautious comparators" to "retained with documented caveats" / "retained under caveat" in running text. Ledger table status column unchanged for consistency.

5. **Exact supportable statements §3–4:** Tightened to match revised external recurrence wording.

## Files modified

- `docs/THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` — 5 targeted edits
- `docs/WORKLOG_LATEST.md` — this file

## Files intentionally not changed

- `docs/LLM_HANDOFF.md` — current stage status unchanged
- `docs/NEXT_QUESTION.md` — no change needed
- All frozen evidence values, configs, pipeline code — unchanged

## Impact

Writing-layer only. The thesis block is now less likely to overclaim on: lower-Dp physical relevance, external recurrence strength, and repo-internal process language. No scientific substance changed.
