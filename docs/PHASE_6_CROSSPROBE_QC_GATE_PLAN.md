# Phase 6 Cross-Probe QC Gate — Plan

**Date:** 2026-03-31
**Type:** One-off comparability gate. Not a science reopen.

---

## Exact question

Are the low-cone / quasi-radial FULL EXP Dn/EB values sufficiently cross-probe comparable to the frozen THD-dominated Phase 4B bank to justify packaging Phase 6 as a bounded descriptive comparison under original semantics?

## Exact scope

FULL EXP 2007-2010 retained catalogue only (148 encounters). No new data, no archive expansion.

## Exact primary inputs

1. `reports/themis_conditioning/routeC_exp/encounter_catalogue_routeC_exp.json`
2. `reports/themis_conditioning/routeC_exp/routeC_exp_summary.json`
3. `data_cache/themis_archive/encounters/*.json` (for supplementary per-encounter detail)

## Exact verdict logic

- **PASS:** nontrivial overlap-valid subset exists AND cross-probe spreads do not show repeated order-of-magnitude divergence dominating the low-cone signal AND the signal is not obviously reducible to probe-family / regime shift alone.
- **FAIL:** >= 3 overlap-valid groups show order-of-magnitude pairwise Dn or EB disagreement aligned with probe/context uncertainty, OR low-cone signal is clearly probe-family-specific.
- **INDETERMINATE:** overlap evidence too sparse or ambiguous.

## Exact non-claims

- PASS does not mean "cone-angle physics proven." It means "bounded descriptive comparison is packaging-safe."
- FAIL does not mean "physics absent." It means "Phase 6 stays at methodological/descriptive level."
- No thresholds, labels, classes, detector semantics, or occurrence language.
