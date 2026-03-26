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
| Persistence | 0.00 | 1.00 | 1.00 | Full range observed. High variance across passes. |
| ptot_smooth | 0.80 | 0.94 | 0.14 | Relatively stable. Total pressure is smooth across most windows. |

### 2. Duration variants behave consistently within a pass

For Dn: mean within-pass spread = 0.50, between-pass range = 1.80 → ratio 0.28
For EB: mean within-pass spread = 0.21, between-pass range = 3.41 → ratio 0.06

**Conclusion:** between-pass diversity dominates. Same-pass duration variants are not independent evidence. The 7 distinct passes, not the 9 windows, are the effective sample.

### 3. Dn and EB are approximately inversely related

Windows with low Dn tend to have high EB, and vice versa. This inverse relationship is observed in the data but is not itself diagnostic of any particular physical state. Both low-Dn/high-EB and high-Dn/low-EB patterns are operationally distinct under the measurement model without implying that either pattern corresponds to a specific physical class.

### 4. ρ(n,B) is negative across the current bank

Every window with available ρ shows ρ < 0. However, this is observed across only 7 THD passes in 2 seasons, all under encounter-averaged Dp > 3 nPa. The universality of negative ρ within this bank does not make ρ a discriminative metric — it may reflect a property common to all compressed-sheath comparator windows rather than a physically diagnostic signal.

---

## What this review does and does not support

**Supports:**
- The frozen metric backbone produces operationally distinguishable outputs across real passes
- Duration variants are consistent within a pass
- The bank spans diverse metric values
- ρ(n,B) < 0 is observed across all windows in this sample (but see risk note below)

**Does NOT support:**
- Any threshold definition
- Any classification of windows as PDL or non-PDL
- Development-set membership decisions
- Detector readiness claims

---

## Scientific risk note

The following limits apply to the current bank and review:

1. **Single probe:** All 9 windows are THD. No cross-probe verification exists.
2. **Effective N = 7:** Two passes have duration variants that are not independent. The effective independent sample is 7, not 9.
3. **Encounter-averaged boundaries:** The s-mapping uses one set of boundary distances per encounter, computed from median upstream conditions. Time-varying Dp within an encounter shifts the true s but is not resolved. This is a known provisional limitation.
4. **Dp > 3 nPa selection bias:** All usable windows required high enough Dp to compress the sheath for dual-bin coverage. This introduces a systematic bias toward compressed-sheath conditions. Lower-Dp sheath states are structurally excluded from the current bank.
5. **Universal negative ρ is not diagnostic:** Because ρ < 0 in every window, it currently has no discriminative power within this bank. It cannot distinguish between windows and should not be treated as a classification feature at this stage.
6. **OMNI / mapping uncertainty:** Upstream conditions are from OMNI (L1 propagation, not local measurement). Boundary models are empirical fits. Both introduce condition-dependent uncertainty that is not yet quantified per-encounter.
7. **No confounder resolution:** transient_flag and mixing_flag remain UNKNOWN (tri-state None). All grades are capped at Silver. Confounder contamination cannot be ruled out for any window.
8. **Descriptive only:** This review describes measurement-model outputs. It does not establish whether any window contains a plasma depletion layer, a compressed sheath, or any other specific physical structure.

---

## Artifacts

| File | Location |
|---|---|
| Metric matrix (JSON) | `runs/20260326T040343Z_d0425fd4/metric_matrix.json` |
| Metric matrix (CSV) | `runs/20260326T040343Z_d0425fd4/metric_matrix.csv` |
| Scatter plots | `runs/20260326T040343Z_d0425fd4/metric_scatter.png` |
| Seed stratification | `runs/20260326T040343Z_d0425fd4/seed_stratification.json` |
| Full review | `runs/20260326T040343Z_d0425fd4/metric_behavior_review.md` |
