# Worklog — Latest Round

**Date:** 2026-03-30
**Round:** Phase 6A — THEMIS upstream conditioning, first tranche

## What changed

Opened Phase 6A as a user-authorized THEMIS science branch. Built a controlled near-subsolar encounter catalogue from all locally cached evaluable THEMIS encounters (N=11 after deduplication). Applied 5 inclusion screens (SZA, upstream availability, occupancy, membership) — all 11 pass. Stratified by IMF cone-angle regime (primary) and clock-angle group (secondary). Produced continuous descriptor summaries (Dn, EB) by stratum.

## Declared slice

All locally cached evaluable THEMIS encounters across all run directories in the repository. This is the single predeclared slice for Phase 6A tranche 1.

## Key findings

- **Perpendicular-IMF** (cone > 60°, N=5): Dn median 0.94 [0.76, 0.97], EB median 1.96 [1.96, 2.12]
- **Intermediate-IMF** (30° < cone ≤ 60°, N=6): Dn median 1.12 [0.95, 1.31], EB median 1.05 [1.03, 1.18]
- **Quasi-radial** (cone ≤ 30°): N=0 (empty bin)
- Occurrence/recovery layer: **deferred** (no inherited operational bundle field exists)

## Files created

- `docs/PHASE_6A_THEMIS_UPSTREAM_CONDITIONING.md` — branch charter + analysis narrative
- `reports/themis_conditioning/encounter_catalogue.json` — machine-readable catalogue
- `reports/themis_conditioning/encounter_catalogue.csv` — CSV mirror
- `reports/themis_conditioning/selection_flow.md` — inclusion/exclusion ledger
- `reports/themis_conditioning/conditioning_summary.json` — stratum summaries
- `reports/themis_conditioning/figures/phase6a_dn_eb_by_cone.png` — Dn vs EB scatter by regime
- `scripts/phase6a_pipeline.py` — sidecar analysis script

## Files modified

- `docs/NEXT_QUESTION.md` — Phase 6A active, three-option next decision
- `docs/LLM_HANDOFF.md` — mode updated to Phase 6A active; Phase 6A block added
- `docs/REPO_NAVIGATION_FOR_THESIS.md` — Phase 6A listed as active analysis (not thesis-safe)
- `docs/WORKLOG_LATEST.md` — this file

## Files intentionally not changed

- `docs/THESIS_BLOCK_FROZEN_COMPARATOR_RECURRENCE.md` — frozen
- `docs/PHASE_4B_RESULTS_FREEZE.md` — frozen
- `docs/THEMIS_CASESET.md` — frozen Phase 5A sidecar
- `docs/PHASE_5B_CASESET_DESCRIPTIVE_PASS.md` — frozen Phase 5B sidecar
- `docs/THEMIS_THESIS_WRITING_PACK.md` — frozen thesis hub
- `docs/MMS_BRANCH_FREEZE.md` — frozen
- All frozen evidence values, bank membership, configs, pipeline code

## No frozen values changed

Phase 4B remains the unchanged checkpoint. Phase 6A is additive and descriptor-only.
