# Metric-Behavior Review — Phase 2a Bank

**Date:** 2026-03-26
**Bank:** 9 windows / 7 distinct passes / THD only / 2008 + 2009 seasons
**Canonical outputs:** `runs/20260326T040343Z_d0425fd4/metric_behavior_review.md`

---

## Purpose

This is a bounded descriptive review of how the frozen metric backbone behaves across the current real-window bank. It is NOT classification, NOT threshold setting, and NOT development-set labeling.

---

## Key findings

### 1. The metric backbone resolves distinguishable behavior

| Metric | Min | Max | Range | Interpretation |
|---|---|---|---|---|
| Dn | 0.12 | 2.31 | 2.19 | Factor ~20. Both depletion (Dn < 1) and enhancement (Dn > 1) observed. |
| EB | 0.80 | 4.22 | 3.42 | Most windows show EB > 1 (B enhancement near MP). Two Sep 3 windows show EB < 1. |
| ρ(n,B) | -0.91 | -0.46 | 0.45 | All windows show negative correlation. Universally anti-correlated. |
| Persistence | 0.00 | 1.00 | 1.00 | Full range. Reflects different depletion extents across passes. |
| ptot_smooth | 0.80 | 0.94 | 0.14 | Relatively stable. Total pressure is smooth across most windows. |

### 2. Duration variants behave consistently within a pass

For Dn: mean within-pass spread = 0.50, between-pass range = 1.80 → ratio 0.28
For EB: mean within-pass spread = 0.21, between-pass range = 3.41 → ratio 0.06

**Conclusion:** between-pass diversity dominates. Same-pass duration variants are not independent evidence. The 7 distinct passes, not the 9 windows, are the effective sample.

### 3. Dn and EB are approximately inversely related

Windows with low Dn (strong near-MP depletion) tend to have high EB (strong B enhancement). This is physically expected for a depletion layer under magnetic pileup — and is exactly the detector backbone's target pattern. The Sep 3 windows (high Dn, low EB) show the opposite pattern, consistent with compressed-sheath conditions.

### 4. Anti-correlation is universal

Every window with available ρ shows ρ < 0. The anti-correlation between density trends and |B| trends is consistently negative across all upstream regimes and both seasons. This is the most stable metric in the bank.

---

## What this review does and does not support

**Supports:**
- The frozen metric backbone resolves genuinely different physical states
- Duration variants are consistent within a pass
- The bank spans diverse metric behavior
- ρ(n,B) < 0 is universal in this sample

**Does NOT support:**
- Any threshold definition
- Any classification of windows as PDL or non-PDL
- Development-set membership decisions
- Detector readiness claims

---

## Artifacts

| File | Location |
|---|---|
| Metric matrix (JSON) | `runs/20260326T040343Z_d0425fd4/metric_matrix.json` |
| Metric matrix (CSV) | `runs/20260326T040343Z_d0425fd4/metric_matrix.csv` |
| Scatter plots | `runs/20260326T040343Z_d0425fd4/metric_scatter.png` |
| Seed stratification | `runs/20260326T040343Z_d0425fd4/seed_stratification.json` |
| Full review | `runs/20260326T040343Z_d0425fd4/metric_behavior_review.md` |
