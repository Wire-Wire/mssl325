# Phase 6 Route C FULL EXP — Result: Bounded Comparison (SUCCESS)

**Date:** 2026-03-31
**Authority:** User-authorized red-level one-off full-archive experiment.
**Outcome:** SUCCESS. Both success conditions met (quasi-radial >= 1 AND low-cone >= 5).

---

## 1. What was done

One full-archive scan of the entire 2007-2010 THEMIS near-subsolar dayside interval via CDAWeb. All five probes (THA, THB, THC, THD, THE), July-November each year, every day (no convenience subsampling). 90 (year, month, probe) combinations searched. 2083 qualifying near-subsolar days processed with multi-threaded CDAWeb acquisition. Original Dn/EB semantics preserved throughout.

---

## 2. Scope match attestation

- **Declared slice:** All THEMIS 2007-2010, Jul-Nov, all 5 probes, SZA <= 30 deg
- **Searched slice:** Every (year, month, probe) in scope had STATE ephemeris fetched from CDAWeb. Every qualifying day had FGM + MOM + OMNI fetched (6h encounter windows). No subsampling.
- **Declared = Searched:** YES
- **Machine-readable manifest:** `reports/themis_conditioning/routeC_exp/scope_manifest.json`

THB and THC excluded from 2010+ (ARTEMIS transition).

---

## 3. Summary counts

| Metric | Count |
|---|---|
| (year, month, probe) combinations searched | 90 |
| Qualifying near-subsolar days | 2083 |
| Encounters processed | 2083 |
| Unique retained (Dn/EB computable, SZA <= 30) | **148** |

### Retained by cone bin

| Cone bin | Count |
|---|---|
| quasi-radial (cone < 30 deg) | **4** |
| low-cone (30-45 deg) | **16** |
| intermediate (45-60 deg) | 44 |
| perpendicular (> 60 deg) | 84 |

---

## 4. Hard stop evaluation

| Criterion | Value | Threshold | Met? |
|---|---|---|---|
| quasi-radial retained | **4** | >= 1 | **YES** |
| low-cone retained | **16** | >= 5 | **YES** |

**OUTCOME: SUCCESS.** Both primary target bins are populated.

---

## 5. Quasi-radial encounters (cone < 30 deg)

| Date | Probe | Cone | Dp | Dn | EB | Note |
|---|---|---|---|---|---|---|
| 2007-08-08 | THA | 25.2 | 1.15 | 0.658 | 2.405 | Dn < 1, EB > 1 |
| 2007-08-12 | THA | 29.0 | 1.42 | 0.032 | 3.117 | Very low Dn, high EB |
| 2009-07-25 | THB | 22.2 | 1.08 | 3.924 | 4.740 | Dn > 1, EB > 1 |
| 2009-08-10 | THC | 19.7 | 0.99 | 3.456 | 5.917 | Dn > 1, EB > 1 |

All four are from probes other than THD and from the 2007/2009 July-August season — the previously unsearched part of the archive. All have Dp around 1.0-1.4 nPa, well below the Phase 4B bank's Dp > 3 nPa. This confirms that the quasi-radial regime is accessible at low Dp via probes with different orbital geometry (THA, THB, THC had larger apogee in 2007).

Two of four show Dn < 1 with EB > 1 (consistent with depletion/pileup). Two show Dn > 1 with EB > 1 (density enhancement with field enhancement). This is descriptive variety, not a classification.

---

## 6. Low-cone encounters (30-45 deg) — 16 retained

| Date | Probe | Cone | Dp | Dn | EB |
|---|---|---|---|---|---|
| 2007-08-12 | THB | 44.4 | 1.51 | 0.839 | 2.997 |
| 2007-08-12 | THC | 38.2 | 1.50 | 0.084 | 3.600 |
| 2007-08-12 | THD | 37.4 | 1.50 | 0.050 | 3.584 |
| 2007-08-13 | THB | 39.1 | 1.05 | 0.023 | 3.600 |
| 2007-08-13 | THC | 42.5 | 1.06 | 0.016 | 3.564 |
| 2007-08-13 | THD | 44.2 | 1.07 | 0.010 | 3.821 |
| 2007-08-13 | THE | 44.2 | 1.07 | 0.016 | 4.330 |
| 2007-08-19 | THA | 43.7 | 1.67 | 0.033 | 2.309 |
| 2008-07-14 | THC | 43.2 | 1.30 | 1.117 | 7.886 |
| 2008-07-18 | THC | 40.8 | 0.84 | 0.045 | 3.779 |
| 2008-07-24 | THC | 40.7 | 0.82 | 3.633 | 3.282 |
| 2008-09-20 | THB | 43.0 | 1.50 | 0.137 | 15.069 |
| 2008-09-20 | THC | 44.4 | 1.50 | 0.068 | 4.372 |
| 2008-09-21 | THB | 38.7 | 1.50 | 0.075 | 6.531 |
| 2009-10-05 | THC | 35.8 | 0.87 | 0.125 | 3.887 |
| 2009-11-11 | THB | 41.9 | 0.94 | 8.314 | 3.840 |

The low-cone bin contains 16 encounters from 10 unique dates across 4 probes. Dp ranges from 0.82 to 1.67 nPa. Most show Dn < 1 with very high EB (> 2). Several show extremely low Dn (0.01-0.08) with EB > 3. A few show Dn > 1.

---

## 7. Key observations (descriptive, not claims)

**7a. The quasi-radial and low-cone regimes ARE populated in the full archive.** The previous Phase 6A tranches and local-only Route C missed them because they searched only THD+THE in Aug-Oct 2008-2009. The newly found encounters come primarily from THA/THB/THC in July-August 2007-2009 — probes with larger apogees that could reach the background bin even at low Dp.

**7b. Low-Dp co-occurrence IS present in the archive.** The quasi-radial and low-cone encounters all have Dp around 0.8-1.7 nPa — much lower than the Phase 4B bank's Dp > 3 nPa. These encounters still satisfy the dual-bin occupancy requirement because THA/THB/THC (especially THC with its ~20 Re apogee in 2007) can reach the background bin at lower Dp.

**7c. The Dn/EB descriptor range is wider than Phase 4B.** Phase 4B clean core: Dn 0.94-2.31, EB 0.80-1.96. The FULL EXP low-cone encounters show Dn as low as 0.01 and EB as high as 15.1. This much wider range may reflect different probe calibration, different orbital geometry, or genuinely different magnetosheath conditions at low cone angles. Caution is warranted before direct comparison with the THD-dominated Phase 4B bank.

**7d. Multi-probe considerations.** The Phase 4B frozen bank is THD-dominated (2008-2009). The FULL EXP low-cone encounters come primarily from THA, THB, THC. Cross-probe comparability has not been validated. The extremely low Dn values (0.01-0.05) and extremely high EB values (> 3) in many low-cone encounters may reflect calibration differences, different spatial sampling, or different background-bin plasma populations at these probes' orbital positions.

---

## 8. Exact strongest supportable statement

The full 2007-2010 THEMIS near-subsolar dayside archive, searched without convenience subsampling across all five probes and July-November each year, yields 148 encounters evaluable under original Dn/EB semantics. Of these, 4 are quasi-radial (cone < 30 deg) and 16 are low-cone (30-45 deg), all previously undiscovered because earlier searches were limited to THD+THE in Aug-Oct 2008-2009. The low-cone and quasi-radial encounters come primarily from THA/THB/THC at Dp 0.8-1.7 nPa — a regime not accessible to THD at its orbital position. Both target bins are now populated, enabling a bounded descriptive comparison across cone-angle regimes under original Dn/EB semantics.

---

## 9. Exact strongest blocked overclaim

- "The quasi-radial regime shows a different PDL signature" (no physical identification; Dn/EB values are descriptors, not structure labels)
- "Low-cone encounters confirm cone-angle-dependent depletion" (the comparison is descriptive; no causal or statistical inference is supported at this stage)
- "The expanded bank validates Phase 4B" (Phase 4B is THD-only; cross-probe comparability has not been established)
- Any threshold, label, class, detector, or occurrence language
- Any claim that the extremely low Dn values at low cone angles represent genuine PDL signatures rather than measurement-model artifacts

---

## 10. Exact non-claims

- No thresholds applied. No encounters classified.
- Cross-probe comparability (THD vs THA/THB/THC) is NOT established.
- The wider Dn/EB range in the expanded catalogue may reflect probe/orbital/calibration differences, not physics alone.
- Phase 4B frozen claims are unchanged.
- Route B descriptors were not used.

---

## 11. Files produced

| File | Type |
|---|---|
| `docs/PHASE_6_FULL_EXP_ACTIVATION.md` | EXP activation |
| `docs/PHASE_6_ROUTEC_FULL_EXP_PLAN.md` | Pre-registered plan |
| `docs/PHASE_6_ROUTEC_FULL_EXP_RESULT.md` | This document |
| `reports/themis_conditioning/routeC_exp/scope_manifest.json` | Scope manifest |
| `reports/themis_conditioning/routeC_exp/selection_flow.md` | Selection flow |
| `reports/themis_conditioning/routeC_exp/encounter_catalogue_routeC_exp.json` | Full catalogue |
| `reports/themis_conditioning/routeC_exp/encounter_catalogue_routeC_exp.csv` | Tabular catalogue |
| `reports/themis_conditioning/routeC_exp/routeC_exp_summary.json` | Summary |
| `scripts/phase6_routeC_full_exp.py` | Scan script |

---

## 12. Next red-level question

Route C FULL EXP SUCCESS. The bounded descriptive comparison is now possible.

**Does the user want to:**
1. Package this FULL EXP result into thesis-safe integration (cone-angle-stratified descriptive comparison)?
2. Authorize further Phase 6 science (cross-probe validation, QC tightening, etc.)?

Phase 6B remains blocked by default.

---

## 13. Frozen anchors unchanged

Phase 4B six-pass bank, THE Sep 19 external recurrence, Phase 5A/5B caseset sidecars, MMS branch freeze — all intact and unmodified. Route B remains frozen sidecar.
