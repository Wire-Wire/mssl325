# Phase 6 EXTRA — Execution Plan

**Date:** 2026-03-31
**Status:** Pre-registered plan. Created before analysis.

---

## 1. Exact question

Same as FULL EXP: can the THEMIS near-subsolar dayside archive yield enough low-cone / quasi-radial encounters evaluable under original Dn/EB semantics to support a bounded descriptive comparison? And does the cross-probe QC gate pass?

## 2. Scope

2007-2025 full local cache (757 retained encounters). Supersedes the 2007-2010 FULL EXP (148 retained) as the definitive dataset.

## 3. Analysis steps

1. Summary stats by cone bin, year, probe, Dn/EB distributions
2. Hard stop evaluation (QR >= 1 or LC >= 5)
3. Cross-probe QC gate:
   - 3A. Overlap-valid same-date multi-probe groups
   - 3B. Pairwise spread (log10 Dn/EB)
   - 3C. Probe-conditioned distributions (THD vs non-THD)
   - 3D. Regime-shift check (Dp/probe entanglement)
   - 3E. QC concentration check
4. Cross-cycle independent verification (Cycle 1 vs Cycle 2)
5. Verdict + comparison with original FULL EXP verdict

## 4. Verdict logic

Same as original gate:
- **PASS:** nontrivial overlap AND LC/QR OOM groups < 3 AND inconsistent < 50%
- **FAIL:** LC/QR OOM groups >= 3 OR inconsistent >= 50%
- **INDETERMINATE:** sparse or ambiguous

## 5. Deliverables

- `docs/PHASE_6_EXTRA_ACTIVATION.md`
- `docs/PHASE_6_EXTRA_PLAN.md` (this file)
- `docs/PHASE_6_EXTRA_RESULT.md`
- `docs/PHASE_6_EXTRA_QC_GATE_REPORT.md`
- `reports/themis_conditioning/routeC_extra/` (all machine-readable outputs)

## 6. Non-claims

Same as all Phase 6 work. No thresholds, labels, classes, detector, occurrence, or mission language.
