# Run Review Packet — Phase 3A

**Self-contained review document for human/AI inspection.**

---

## A. Run identity and guardrails

| Field | Value |
|---|---|
| Run ID | 20260326T040343Z_d0425fd4 |
| Stage | Phase 3A — Bounded Dn/EB exploratory comparison |
| Bank scope | 9 windows / 7 passes / THD only / 2008+2009 |
| Primary comparison | P2, P4, P5, P6 (clean core, 4 passes) |
| Secondary with caveats | P1, P3 (cautious, 2 passes) |
| Excluded | P7 (spike-dominated, 1 pass) |

**Frozen baseline:** encounter-unit, Sun-Earth-line s-mapping, Shue98 MP + Merka05 BS, dual bins [0.2,0.4]+[0.6,1.0], IMF-agnostic detection, conservative naming.

**Provisional:** 6-10h windows, Dp > 3 nPa preference, encounter-averaged boundaries, conservative membership.

**Explicit non-claims:**
- No thresholds are defined or implied
- No window is classified as PDL-positive or non-PDL
- No development-set membership is assigned
- rho(n,B) is non-discriminative within this bank
- This packet does NOT authorize detector work

---

## B. Bank headline summary

| Item | Count |
|---|---|
| Total windows | 9 |
| Total passes | 7 (effective independent N) |
| Clean core passes | 4 (P2, P4, P5, P6) |
| Cautious passes | 2 (P1, P3) |
| Excluded passes | 1 (P7) |
| Probe | THD only |
| Seasons | 2008, 2009 |
| Dp range | 3.0-4.2 nPa |
| Bz range | -1.7 to +2.6 nT |

---

## C. Core figures

- **Dn/EB comparison:** `reports/current_bank/figures/phase3a_dneb_comparison.png`
  - Left: Dn vs EB by evidence status (blue=clean, red=cautious, gray=excluded)
  - Right: Dn original vs Dn after spike removal (on-diagonal = robust)
- **Cross-pass summary:** `reports/current_bank/figures/cross_pass_summary.png`
- **Per-window QC:** `runs/.../qc_<window_id>.png` (9 files)

---

## D. Core evidence table

| Pass | Status | SZA | Dp | Bz | Near% | BG% | Memb% | Dn | EB | Dn_clean | EB_clean | Spike% | Key caveat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | cautious | 22 | 4.2 | +0.3 | 16% | 48% | 86% | 0.12 | 2.49 | 0.17 | 2.29 | 24% | Density noise CV=0.93 |
| P2 | clean | 14 | 3.5 | +0.9 | 17% | 27% | 100% | 2.31 | 0.82 | 2.10 | 0.84 | 16% | |
| P3 | cautious | 17 | 3.1 | -1.4 | 17% | 47% | 100% | 0.39 | 1.96 | 0.41 | 1.46 | 25% | EB spike-dependent |
| P4 | **clean** | 10 | 3.0 | +1.4 | 9% | 46% | 100% | 0.97 | 1.48 | 0.96 | 1.49 | 21% | **Cleanest pass** |
| P5 | clean | 4 | 3.0 | +0.9 | 18% | 40% | 98% | 0.94 | 1.96 | 0.90 | 1.94 | 13% | |
| P6 | clean | 4 | 3.1 | -1.7 | 16% | 57% | 96% | 1.31 | 1.23 | 1.10 | 1.20 | 10% | |
| P7 | excluded | 20 | 4.2 | -0.5 | 14% | 65% | 98% | 2.19 | 4.22 | 0.67 | 0.97 | 35% | Spike-dominated |

**Supporting metrics (clean core + cautious only):**

| Pass | Δβ | ρ(n,B) | Persistence | ptot_smooth |
|---|---|---|---|---|
| P1 | -10.1 | -0.46 | 0.94 | 0.86 |
| P2 | +1.7 | -0.52 | 0.00 | 0.80 |
| P3 | -6.8 | -0.90 | 1.00 | 0.94 |
| P4 | -3.1 | -0.63 | 0.66 | 0.94 |
| P5 | -12.8 | -0.91 | 0.61 | 0.81 |
| P6 | -4.2 | -0.72 | 0.32 | 0.86 |

---

## E. Measurement-model caveat section

- **Boundary models:** Shue 1998 (MP) + Merka 2005 (BS). Empirical fits; condition-dependent accuracy not quantified per-encounter.
- **Upstream source:** OMNI 1-min (L1 propagation to bow shock nose). Representativeness limited by propagation delay and IMF structure.
- **Boundary averaging:** Encounter-averaged MP/BS standoff from median upstream Dp and Bz. Time-varying Dp within multi-hour windows shifts the true s but is not resolved.
- **Key uncertainty:** +/-1 nPa Dp shifts boundaries by ~1 Re. This is a substantial fraction of the ~3 Re sheath width.

---

## F. Confounder status section

| Confounder | Resolution | Bank-wide status |
|---|---|---|
| Jet/spike (Pdyn) | Partially resolved | jet_flag=TRUE for all 9 windows. Universal triggering is a long-window artifact. Leave-spike-out: 4 clean passes survive; P7 collapses. |
| Wave/mirror | Partial proxy | wave_flag=FALSE for all. Near-bin density CV ranges 0.08-0.93. P1 has very high noise. |
| Transient | **UNKNOWN** | Not implemented. Would require IMF geometry analysis. |
| Mixing | **UNKNOWN** | Not implemented. Would require plasma-regime classification. |
| Boundary motion | **UNKNOWN** | Not resolvable without time-varying s (deferred). |

---

## F2. Literature-constrained rationale: why descriptive comparison only

The current package supports a descriptive Dn/EB comparison but does NOT support thresholds, labels, or detector semantics. The reasons are grounded in the evidence limits and the paper-library constraints:

1. **Encounter-averaged boundaries are provisional.** The s-mapping uses median upstream conditions per encounter. Walsh et al. (2019) and Aghabozorgi et al. (2024) document condition-dependent MP model inaccuracy under propagation uncertainty. Until time-varying s is implemented, bin assignments carry encounter-averaging artifacts.

2. **The bank is structurally biased.** All 9 windows require Dp > 3 nPa for dual-bin coverage (a practical constraint from THD's 11.6 Re apogee). Pi et al. (2024) and Michotte de Welle et al. (2024) show that dayside sheath profiles are IMF- and pressure-dependent. The current bank cannot represent the full dayside sheath population.

3. **Three confounder channels remain unresolved.** Transient contamination (Zhang et al. 2022), magnetospheric mixing (Li et al. 2009), and boundary motion (Plaschke et al. 2009) cannot be assessed with current data products. Archer & Horbury (2013) and Raptis et al. (2020) show that Pdyn spikes are heterogeneous; the universal jet triggering in this bank reflects long-window sampling, not uniform jet contamination.

4. **Effective N = 7 passes (4 clean + 2 cautious + 1 excluded).** This is insufficient for threshold calibration or statistical detector construction. It is sufficient only for a descriptive comparison of how the measurement model behaves across a small, biased, confounder-audited sample.

5. **The low-Dn range depends on caveated evidence.** No clean-core pass has Dn < 0.5. The two cautious passes (P1, P3) that provide the low-Dn range carry density-noise and EB-spike caveats respectively. Any claim about low-Dn behavior must acknowledge this dependency.

---

## G. What this run supports / does not support

**Supports:**
- A very bounded descriptive Dn/EB exploratory comparison across 6 interpretable passes
- Observation that clean core spans Dn 0.94-2.31, EB 0.80-1.96
- Observation that low-Dn range (< 0.5) depends entirely on cautious passes
- Observation that all windows show rho(n,B) < 0 (but this is non-discriminative)

**Does NOT support:**
- Any threshold definition
- Any classification of windows
- Any detector-v0 semantics
- Any development-set claims
- Any generalization beyond THD / compressed-sheath conditions

---

## H. Artifact map

| Category | Path |
|---|---|
| Bank manifest (JSON) | `evidence/json/bank_manifest.json` |
| Pass matrix (CSV) | `evidence/csv/pass_matrix.csv` |
| Window matrix (CSV) | `evidence/csv/window_matrix.csv` |
| Confounder register (CSV) | `evidence/csv/confounder_register.csv` |
| Interval audit (CSV) | `evidence/csv/interval_audit_matrix.csv` |
| Claim map (JSON) | `evidence/index/claim_map.json` |
| Figure manifest (JSON) | `evidence/index/figure_manifest.json` |
| Review chunks (JSON) | `evidence/review/RUN_REVIEW_PACKET_chunks.json` |
| Pass chunks (JSON) | `evidence/chunks/pass_report_chunks.json` |
| Phase 3A figure | `reports/current_bank/figures/phase3a_dneb_comparison.png` |
| Per-window QC reports | `qc_<window_id>.png` (9 files) |

---

## I. Decision status

**Current stage:** Phase 3A descriptive comparison — sign-off pending.

**This packet supports:** green and yellow decisions only (report improvements, artifact completion, descriptive framing within current ceiling).

**This packet does NOT authorize:** thresholds, threshold candidates, labels, detector semantics, dev-set membership, bank expansion, or changes to the frozen measurement model. These are red decisions requiring user sign-off.

**Preferred review entry point:** This packet is the recommended starting document for all roles (Pro A, Pro B, Pro C, and human reviewers).
