# Pass-Level Interval Audit — Phase 2C

**Date:** 2026-03-26
**Method:** Loaded raw cached FGM/MOM/STATE/OMNI data for one representative window per pass, resampled to 10 s, computed Pdyn spike analysis and leave-spike-out metric sensitivity.

---

## Summary table

| Pass | Date | Window | Spike% | Near spk | BG spk | Dn orig | Dn clean | ΔDn | EB orig | EB clean | ΔEB | dens CV | Clean? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | 2008-08-18 | aug18_6h | 23.8% | 0 | 344 | 0.12 | 0.17 | 0.05 | 2.49 | 2.29 | 0.20 | 0.93 | ⚠️ noisy |
| P2 | 2008-09-03 | sep03_6h | 15.8% | 99 | 27 | 2.31 | 2.10 | 0.22 | 0.82 | 0.85 | 0.02 | 0.23 | ✓ survives |
| P3 | 2009-09-13 | sep13_09_6h | 25.1% | 10 | 531 | 0.39 | 0.41 | 0.01 | 1.96 | 1.46 | 0.50 | 0.47 | ⚠️ EB shifts |
| P4 | 2009-09-20 | sep20_09_6h | 21.2% | 41 | 16 | 0.97 | 0.96 | 0.01 | 1.48 | 1.49 | 0.02 | 0.08 | ✓ **cleanest** |
| P5 | 2009-09-26 | sep26_09_10h | 12.6% | 92 | 142 | 0.94 | 0.90 | 0.04 | 1.96 | 1.94 | 0.01 | 0.33 | ✓ survives |
| P6 | 2009-09-27 | sep27_09_10h | 10.2% | 100 | 116 | 1.31 | 1.10 | 0.22 | 1.23 | 1.20 | 0.02 | 0.24 | ✓ survives |
| P7 | 2009-10-24 | oct24_09_6h | **35.2%** | 0 | 495 | 2.19 | **0.67** | **1.52** | 4.22 | **0.97** | **3.26** | 0.10 | ❌ **spike-dominated** |

**dens CV** = coefficient of variation of density in the near bin (higher = noisier).

---

## Pass cards

### P1 — 2008-08-18 (seed_A)

- **Spike fraction:** 23.8%. All 344 spikes in background bin; near bin has zero spikes.
- **Leave-spike-out:** Dn 0.12 → 0.17 (qualitatively stable, still strongly below 1). EB 2.49 → 2.29 (reduced but still high). Pattern survives.
- **Near-bin density CV = 0.93** — very high fluctuation level. Near-bin density is extremely noisy.
- **Wave/mirror risk:** High density CV suggests possible mirror-mode or wave-dominated intervals in the near bin. Unresolved with current information.
- **Membership:** 86% (lowest in bank). 291 unknown/NaN points.
- **Assessment:** Pattern qualitatively survives spike removal, but high density noise and low membership add caveat. Usable with caution.

### P2 — 2008-09-03 (seed_C)

- **Spike fraction:** 15.8%. Spikes mainly in near bin (99), few in BG (27).
- **Leave-spike-out:** Dn 2.31 → 2.10, EB 0.82 → 0.85. Minimal change. Pattern robust.
- **Near-bin density CV = 0.23** — moderate.
- **Membership:** 100%.
- **Assessment:** Relatively clean. Metrics robust to spike removal. No obvious wave or transient concern from interval structure.

### P3 — 2009-09-13 (seed_D)

- **Spike fraction:** 25.1%. Overwhelmingly in BG bin (531 of 542 spikes).
- **Leave-spike-out:** Dn 0.39 → 0.41 (stable). **EB 1.96 → 1.46 (Δ=0.50)** — significant reduction.
- **Interpretation:** The high EB value is partially supported by Pdyn-spike-contaminated BG-bin intervals. After spike removal, EB drops but remains above 1.0. Dn is robust. The strong ρ=-0.90 should be treated cautiously since EB is spike-sensitive.
- **Assessment:** Dn pattern survives. EB partially spike-dependent. seed_D's "strongest anti-correlation" claim rests partly on spike-inflated EB contrast.

### P4 — 2009-09-20 (seed_B)

- **Spike fraction:** 21.2%. Mainly in near bin (41), few in BG (16).
- **Leave-spike-out:** Dn 0.97 → 0.96, EB 1.48 → 1.49. **Both change by < 0.02.** Most robust pass in the bank.
- **Near-bin density CV = 0.08** — very low. Quiet near bin.
- **Membership:** 100%.
- **Assessment:** **Cleanest pass in the bank.** Metrics are essentially unaffected by spike removal. Low noise. Full membership.

### P5 — 2009-09-26

- **Spike fraction:** 12.6% (lowest). Distributed between near (92) and BG (142).
- **Leave-spike-out:** Dn 0.94 → 0.90, EB 1.96 → 1.94. Pattern robust.
- **Near-bin density CV = 0.33** — moderate.
- **Assessment:** Second-cleanest pass. Low spike fraction, robust metrics.

### P6 — 2009-09-27

- **Spike fraction:** 10.2% (absolute lowest). Distributed between near (100) and BG (116).
- **Leave-spike-out:** Dn 1.31 → 1.10 (moderate shift). EB 1.23 → 1.20 (stable).
- **Assessment:** Low spike contamination. Dn shows moderate sensitivity (~16% change) but qualitative pattern preserved.

### P7 — 2009-10-24

- **Spike fraction: 35.2% — highest in bank.** All 495 spikes in BG bin.
- **Leave-spike-out: Dn 2.19 → 0.67 (Δ=1.52). EB 4.22 → 0.97 (Δ=3.26).** Window-level metrics collapse after spike removal.
- **Assessment: ❌ Spike-dominated.** The extreme metric values (highest EB in bank at 4.22) are almost entirely driven by Pdyn-spike intervals in the background bin. After spike removal, both Dn and EB approach unity — the null expectation. This pass cannot support any metric-based comparison without spike resolution.

---

## Confounder status by pass

| Pass | Jet spikes | Wave/mirror risk | Transient risk | Mixing risk | Boundary motion |
|---|---|---|---|---|---|
| P1 | ⚠️ 24% but BG only | ⚠️ high dens CV (0.93) | unresolved | unresolved | no obvious evidence |
| P2 | ✓ 16%, pattern survives | low risk (CV 0.23) | unresolved | unresolved | no obvious evidence |
| P3 | ⚠️ 25% BG-concentrated, EB shifts | moderate (CV 0.47) | unresolved | unresolved | no obvious evidence |
| P4 | ✓ 21%, pattern survives | ✓ low (CV 0.08) | unresolved | unresolved | no obvious evidence |
| P5 | ✓ 13%, pattern survives | moderate (CV 0.33) | unresolved | unresolved | no obvious evidence |
| P6 | ✓ 10%, pattern survives | moderate (CV 0.24) | unresolved | unresolved | no obvious evidence |
| P7 | ❌ 35%, metrics collapse | low (CV 0.10) | unresolved | unresolved | no obvious evidence |

**Transient, mixing, and boundary-motion flags remain UNKNOWN for all passes.** Current data products do not support their resolution without additional implementation.
