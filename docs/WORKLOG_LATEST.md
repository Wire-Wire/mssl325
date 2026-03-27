# Worklog — Latest Round

**Date:** 2026-03-27
**Round:** Phase 4A — Independent low-Dn recurrence test

## What changed

Executed Phase 4A: systematic search for independent THEMIS candidates outside the current six-pass bank. Searched THD 2008-09, THE 2008, THD 2010 (every other day, SZA < 40°, Dp > 2.5 nPa). Found 6 candidates with dual-bin potential; ran 4 through the full frozen pipeline. 2 PASS, 2 FAIL_OCCUPANCY.

Key result: THE Sep 19 2008 produces Dn = 0.76 on a cross-probe independent pass, below the clean-core floor (0.94). No independent candidate reaches Dn < 0.5.

## Files created

- `docs/PHASE_4A_INDEPENDENT_LOWDN_RECURRENCE.md` — full analysis
- `reports/current_bank/phase4a_lowdn_recurrence_report.md` — compact report
- `reports/current_bank/figures/phase4a_lowdn_recurrence.png` — Dn/EB figure with independent candidates
- `runs/20260327T221306Z_227f7e3f/evidence/csv/phase4a_candidate_shortlist.csv` — machine-readable shortlist
- `runs/20260327T221306Z_227f7e3f/` — run outputs (4 encounter JSONs, 4 QC PNGs)

## Files modified

- `docs/NEXT_QUESTION.md` — stage updated to Phase 4A complete
- `docs/LLM_HANDOFF.md` — milestone updated, Phase 4A block added
- `docs/WORKLOG_LATEST.md` — this file

## Files intentionally not changed

- `reports/current_bank/RUN_REVIEW_PACKET.md` — Phase 3A packet; Phase 4A results are separate
- All Phase 3A/3B documents — evidence values unchanged
- `configs/pilot_live_usable.yaml` — main bank config unchanged; no candidate auto-admitted
- All frozen core pipeline code — unchanged

## Impact

One cross-probe recurrence of Dn < 1 found. Dn < 0.5 remains cautious-only. The independent candidate is not less caveated than P1/P3.

## Decisions this round

- **Green taken:** search-space selection, candidate window placement, figure layout
- **Yellow taken:** none
- **Red applied:** Phase 4A authorization (user decision from prior round)
- **Red detected for next round:** whether to admit THE Sep 19 to the main bank (user decision required)
