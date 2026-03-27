# Phase 2D — Descriptive-Comparison Readiness Review

**Date:** 2026-03-26
**Basis:** Post-Phase-2C evidence base (9 windows / 7 passes / 4 clean + 2 cautious + 1 excluded)

---

## 1. Question

Does the current post-Phase-2C bank contain a sufficiently clean and sufficiently defensible evidence subset to justify a later bounded descriptive Dn/EB comparison stage?

---

## 2. Evidence structure summary

| Category | Passes | Effective N | Metric range (Dn) | Metric range (EB) |
|---|---|---|---|---|
| Clean core | P2, P4, P5, P6 | 4 | 0.94–2.31 | 0.82–1.96 |
| Cautious | P1, P3 | 2 | 0.12–0.39 | 1.96–2.49 |
| Excluded | P7 | 0 | — | — |
| **Total interpretable** | | **4 to 6** | **0.12–2.31** (with caveats) | **0.82–2.49** (with caveats) |

---

## 3. Metric diversity vs confounder-tested diversity

This is the central question for comparison readiness. The distinction matters because metric range alone — without confounder testing — can be misleading.

### Metric diversity (what the numbers span)

The full interpretable bank (6 passes) spans:
- Dn: 0.12 to 2.31 (factor ~20)
- EB: 0.82 to 2.49 (factor ~3)
- This is broad enough to resolve operationally different metric patterns

### Confounder-tested diversity (what survives interval scrutiny)

The clean core alone (4 passes) spans:
- Dn: 0.94 to 2.31 (factor ~2.5)
- EB: 0.82 to 1.96 (factor ~2.4)
- **No clean-core pass has Dn < 0.5**

The low-Dn range (Dn < 0.5) — which is where the detector backbone's primary depletion signal would appear — exists only in cautious passes:
- P1: Dn = 0.12 (high density noise, wave/mirror risk)
- P3: Dn = 0.39 (EB spike-dependent, but Dn itself is robust)

**Assessment:** The clean core spans enough metric diversity to show that the measurement model produces operationally distinguishable outputs. But it does NOT span the low-Dn range with confounder-tested confidence. The most physically interesting region (Dn ≪ 1) relies on cautious passes.

---

## 4. Unresolved confounder sufficiency

### Universal negative ρ — non-discriminative

**Status: acceptable as a caveat.** ρ(n,B) < 0 in every window makes it useless for within-bank discrimination. Any later descriptive comparison must acknowledge that ρ is a bank-wide property, not a signal/noise separator. This does not block descriptive Dn/EB comparison.

### Universal jet-like triggering — reinterpreted but not resolved

**Status: acceptable as a serious warning.** Phase 2C showed this is largely a long-window artifact (the 2× median Pdyn threshold is too broad for 6-10h windows). For the clean core, leave-spike-out analysis shows metrics survive. But the jet_flag remains TRUE for all windows, which means:
- No window has clean-of-jets certification
- Any later comparison must acknowledge that Pdyn fluctuations are present in all passes
- The jet criterion itself needs recalibration before any later confounder-resolution stage (deferred)

### Transient / mixing / boundary-motion — UNKNOWN

**Status: serious warning, but not a blocker.** All three remain UNKNOWN for all passes. This is because:
- Transient resolution would require IMF geometry analysis (deferred: conflicts with IMF-agnostic principle at detection time)
- Mixing resolution would require plasma-regime classification beyond current membership check (deferred)
- Boundary-motion resolution would require time-varying s (deferred: baseline-changing)

These unresolved channels mean any later descriptive comparison must proceed with the understanding that all windows carry unquantified transient/mixing/boundary-motion risk. This is tolerable for a bounded, descriptive comparison stage — it would be intolerable for any later detector-oriented validation.

### THD-only / Dp > 3 nPa selection bias

**Status: serious warning, but not a blocker for bounded exploration.** The bank systematically represents only compressed-sheath conditions on one probe. Any descriptive patterns observed in this bank cannot be claimed as universal. They are THD-specific, compressed-sheath-specific observations only.

### Encounter-averaged boundary uncertainty

**Status: acceptable as a caveat.** ±1 nPa Dp shifts boundaries ~1 Re. This is a known limitation of the frozen measurement model. It does not prevent bounded descriptive comparison but must be carried forward.

---

## 5. Seed sufficiency after Phase 2C

| Seed | Post-2C status | Still useful? |
|---|---|---|
| seed_A (P1) | Cautious: high density noise | Yes, but with wave/noise caveat. Only clean-enough low-Dn anchor. |
| seed_B (P4) | **Cleanest** | Yes. Best-supported pass in the bank. |
| seed_C (P2) | Clean | Yes. Clean high-Dn anchor. |
| seed_D (P3) | Weakened: EB spike-dependent | **Marginally.** Dn is robust (0.39), but the EB/rho claims are weakened. |

**Assessment:** The seeds still span the observed metric range and are useful as planning entry points. But they now carry explicit interval-level caveats that must be respected. Seed_D's EB weakness means the strongest anti-correlation claim in the bank is partially confounder-contaminated.

**No seed relabeling.** All remain planning artifacts only.

---

## 6. GO / NO-GO decision

### Decision: **CONDITIONAL GO**

The current evidence base is sufficient to justify a later **very bounded, descriptive Dn/EB comparison** — provided the following conditions are respected:

### What a later stage CAN do

1. Describe how Dn and EB vary across the 6 interpretable passes (4 clean + 2 cautious)
2. Note which passes show operationally similar or different metric patterns
3. Check whether duration variants produce consistent behavior within a pass
4. Report whether Δβ or persistence co-vary with Dn/EB patterns

### What a later stage CANNOT do

1. Define or propose threshold values
2. Classify any window as PDL-positive or non-PDL
3. Use ρ as a discriminative metric (it is universal in this bank)
4. Ignore the fact that the low-Dn range relies on cautious passes
5. Treat observations as generalizable beyond THD / compressed-sheath conditions
6. Skip human review before drawing any scientific conclusion

### Named evidence subset for the later stage

- **Primary evidence:** P2, P4, P5, P6 (clean core, 4 passes)
- **Secondary evidence:** P1, P3 (cautious, 2 passes — adds range but carries caveats)
- **Excluded:** P7 (spike-dominated, cannot participate in metric comparison)

---

## 7. Recommended next stage

### Name: **Phase 3A — Very Bounded Dn/EB Descriptive Comparison**

### Goal
Describe how Dn and EB vary across the 6-pass interpretable bank. This is descriptive only — no thresholds, no labels, no detector semantics.

### Hard boundaries
1. No thresholds are defined, proposed, or implied
2. No window may be labeled PDL-positive or non-PDL
3. The comparison must be reported as "under compressed-sheath / THD-only conditions"
4. P7 must remain excluded
5. Cautious passes (P1, P3) may be included for range context but their caveats must be stated
6. ρ must not be treated as discriminative (non-discriminative in this bank)
7. Human review is required before any further stage

### What remains deferred beyond Phase 3A
- Final detector thresholds
- Labels of any kind
- Development/validation set membership
- Encounter merge
- Radial-IMF cut
- Selection-function audit at catalogue scale
- Time-varying s
- Cross-probe verification
- MMS thickness
- SMILE/SXI priors

---

## 8. Summary

The bank's confounder-tested clean core (N=4) is narrow but defensible. Combined with 2 cautious passes (N=6 total interpretable), it spans enough metric and upstream diversity for a very bounded, descriptive Dn/EB comparison. The comparison is probe-specific, regime-specific, and explicitly descriptive only. The 3 permanently unresolved confounder channels (transient, mixing, boundary motion) are tolerable for descriptive work but would need resolution before any detector-oriented stage.
