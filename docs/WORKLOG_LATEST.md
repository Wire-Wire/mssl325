# Worklog — Latest Round

**Date:** 2026-03-28
**Round:** Thesis-body block creation + bounded verification

## What changed

Created `docs/THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` — a thesis-body results block for the frozen comparator + external-recurrence branch. Written in results logic (not repo phase chronology). Includes: frozen evidence ledger, clean-core Dn/EB span, cautious low-Dn extension, independent external recurrence, exact supportable statements, limitations, and traceability note. References two frozen figures.

## Verification performed

- All Dn/EB values verified against `runs/20260326T040343Z_d0425fd4/all_encounters.json`
- THE Sep 19 values verified against `runs/20260327T221306Z_227f7e3f/encounter_cand4a_sep19_08_the.json`
- Clean-core ranges confirmed: Dn [0.94, 2.31], EB [0.80, 1.96]
- SZA range confirmed: 4°–22° across 6 interpretable passes
- Dp range confirmed: 3.0–4.2 nPa
- P1 near-bin density CV = 0.93, membership = 86% confirmed
- P3 EB spike sensitivity Δ = 0.50, mapping sensitivity ±0.23 confirmed
- THE Sep 19: Dn = 0.76, Dp = 2.8, Ma = 21.1, membership = 84% confirmed
- P7 spike-removal collapse (2.19→0.67, 4.22→0.97) confirmed
- No mismatch found between thesis block numbers and frozen artifacts

## Files created

- `docs/THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md`

## Files modified

- `docs/WORKLOG_LATEST.md` — this file

## Files intentionally not changed

- `docs/LLM_HANDOFF.md` — per instructions
- `docs/NEXT_QUESTION.md` — per instructions
- `reports/current_bank/RUN_REVIEW_PACKET.md` — per instructions
- `docs/PHASE_4B_RESULTS_FREEZE.md` — per instructions
- All Phase 3A/3B/4A evidence values — unchanged
- All frozen figures, configs, pipeline code — unchanged

## Impact

Writing-layer only. No scientific content, evidence values, or control state changed. The thesis block is ready for integration into a thesis or paper draft.

## Decisions this round

- **Green taken:** thesis block structure, paragraph composition, ledger layout, figure references
- **Yellow taken:** none
- **Red detected:** none
