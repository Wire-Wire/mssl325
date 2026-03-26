# Phase 3A — Bounded Dn/EB Exploratory Comparison

**Date:** 2026-03-26
**Stage:** Descriptive comparison only. Not detector work.

---

## 1. Purpose

This stage answers one narrow question under the current frozen measurement model:

**How do Dn and EB compare across the current interpretable passes, and how much of the observed metric range depends on caveated evidence?**

This is descriptive, pass-aware, and caveat-explicit. It does not define thresholds, labels, or detector semantics.

---

## 2. Why Dn and EB are the primary comparison axes

The frozen detector backbone (blueprint §6.3) defines Dn and EB as the two primary near/background ratio metrics:
- **Dn** = median(density_near) / median(density_bg) — captures near-MP density behavior
- **EB** = median(|B|_near) / median(|B|_bg) — captures near-MP magnetic field behavior

These are the first-order spatial-comparison outputs of the measurement model. delta_beta, persistence, and ptot_smoothness are supporting context. rho(n,B) is universally negative in this bank and non-discriminative.

---

## 3. Evidence structure

| Role | Passes | Dn range | EB range | Use in comparison |
|---|---|---|---|---|
| Clean core | P2, P4, P5, P6 | 0.94–2.31 | 0.80–1.96 | Primary interpretable evidence |
| Cautious | P1, P3 | 0.12–0.39 | 1.96–2.49 | Extends range but carries interval-level caveats |
| Excluded | P7 | — | — | Not used (spike-dominated) |

**Key observation:** The clean core alone has no pass with Dn < 0.5. The entire low-Dn range — where near-MP density is substantially lower than background — depends on cautious passes P1 and P3.

---

## 4. Pass-aware Dn/EB comparison

| Pass | Status | Dn | EB | Dn_clean | EB_clean | Caveat |
|---|---|---|---|---|---|---|
| P4 | clean | 0.97 | 1.48 | 0.96 | 1.49 | Cleanest; minimal spike sensitivity |
| P5 | clean | 0.94 | 1.96 | 0.90 | 1.94 | Low spike fraction (13%) |
| P6 | clean | 1.31 | 1.23 | 1.10 | 1.20 | Lowest spike fraction (10%) |
| P2 | clean | 2.31 | 0.82 | 2.10 | 0.84 | EB robustly < 1 |
| P3 | cautious | 0.39 | 1.96 | 0.41 | 1.46 | EB drops by 0.50 after spike removal |
| P1 | cautious | 0.12 | 2.49 | 0.17 | 2.29 | Near-bin density CV = 0.93 (very noisy) |

---

## 5. What this comparison shows

Within the current frozen measurement model and compressed-sheath bank:

1. **Dn straddles unity in the clean core.** P4 and P5 show Dn near 1.0; P2 shows Dn > 2; P6 shows Dn near 1.3. These are operationally distinguishable outputs.

2. **The Dn < 0.5 region is entirely cautious.** P1 (Dn=0.12) and P3 (Dn=0.39) extend the range far below unity but carry density-noise and EB-spike caveats respectively.

3. **EB broadly mirrors Dn inversely** but the relationship is not tight. P2 (high Dn, low EB) and P1 (low Dn, high EB) sit at opposite corners; the other passes are intermediate.

4. **Spike removal does not qualitatively change the clean core.** For P4/P5/P6, Dn and EB shift by < 0.25 after spike removal. For P2, Dn shifts by 0.22 but remains > 2.

5. **P7 is excluded because its entire metric signature is a spike artifact** (Dn 2.19 → 0.67, EB 4.22 → 0.97 after removal).

---

## 6. What this comparison does NOT show

- No threshold is defined or implied by the Dn/EB spread.
- No pass is classified as PDL-positive, non-PDL, or any labeled category.
- No detector readiness is claimed.
- The observed Dn/EB range is regime-specific (THD, Dp > 3 nPa, 2 seasons).
- rho(n,B) is not used as a comparison axis because it is non-discriminative in this bank.

---

## 7. Deferred artifacts

- **bin_stats_long.csv** and **profile_long.csv**: deferred because current run products do not expose per-bin profile-level exports. Would require reloading raw cached arrays per pass.
- **Per-pass timeline audit figures**: deferred for same reason.

---

## 8. Conclusion

Phase 3A descriptive comparison completed under current caveats. No thresholds or labels implied. The clean core provides a confounder-tested Dn range of 0.94–2.31 and EB range of 0.80–1.96. The low-Dn range (Dn < 0.5) is supported only by cautious evidence.
