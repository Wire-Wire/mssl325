# Phase 6 EXTRA — Result

**Date:** 2026-03-31
**Scope:** 2007-2025, all 5 THEMIS probes, full local cache.
**Outcome:** SUCCESS (hard stop). Both target cone bins populated with substantially larger samples than the 2007-2010 FULL EXP.

---

## 1. Summary

| Metric | FULL EXP (2007-2010) | **EXTRA (2007-2025)** |
|---|---|---|
| Retained | 148 | **757** |
| quasi-radial (< 30 deg) | 4 | **28** |
| low-cone (30-45 deg) | 16 | **89** |
| intermediate (45-60 deg) | 44 | **199** |
| perpendicular (> 60 deg) | 84 | **441** |

---

## 2. Dn/EB per cone bin

| Cone bin | N | Dn median | Dn IQR | EB median | EB IQR | Dp median |
|---|---|---|---|---|---|---|
| quasi-radial | 28 | 0.891 | [0.061, 1.348] | 2.423 | [2.005, 3.155] | 1.65 |
| low-cone | 89 | 0.795 | [0.068, 1.173] | 2.545 | [1.564, 3.840] | 1.53 |
| intermediate | 199 | 0.785 | [0.121, 1.135] | 2.377 | [1.496, 4.093] | 2.25 |
| perpendicular | 441 | 0.735 | [0.143, 1.235] | 2.391 | [1.552, 4.149] | 2.44 |

Dn medians are broadly similar across all cone bins (0.74-0.89). EB medians are also similar (2.38-2.55). The wider IQRs in the low-cone/QR bins reflect both genuine physical spread and the probe/Dp regime differences.

---

## 3. Cross-cycle verification

The 2007-2025 archive spans three independent orbital cycles:

| Cycle | Years | N retained | QR | LC |
|---|---|---|---|---|
| Cycle 1 | 2007-2010 | 152 | 5 | 17 |
| Cycle 2 | 2016-2019 | 241 | 11 | 34 |
| ARTEMIS/other | 2011-2015, 2020-2025 | 364 | 12 | 38 |

Both Cycle 1 and Cycle 2 populate all four cone bins independently, confirming that the result is not an artifact of one specific orbital epoch.

---

## 4. Retained by probe

| Probe | N | Note |
|---|---|---|
| THA | 233 | Near-Earth, all cycles |
| THB | 37 | ARTEMIS perigee passes (2010+) |
| THC | 51 | ARTEMIS perigee passes (2010+) |
| THD | 217 | Near-Earth, all cycles |
| THE | 219 | Near-Earth, all cycles |

THD now contributes 217 encounters (29% of total), including 6 quasi-radial and 17 low-cone — far more than the 2007-2010 subset where THD had 0 QR and 2 LC. This substantially improves the THD representation in target bins.

---

## 5. Probe-conditioned comparison

| Family | N | Dn median | EB median | Dp median |
|---|---|---|---|---|
| THD | 217 | 0.715 | 2.243 | 2.45 |
| non-THD | 540 | 0.774 | 2.460 | 2.10 |

THD and non-THD Dn medians differ by only 0.06 — much closer than in the 2007-2010 subset (where it was 0.75 vs 0.66). The probe-family effect is smaller in the full dataset.

---

## 6. Files produced

- `reports/themis_conditioning/routeC_extra/scope_manifest_extra.json`
- `reports/themis_conditioning/routeC_extra/encounter_catalogue_extra.json`
- `reports/themis_conditioning/routeC_extra/encounter_catalogue_extra.csv`
- `reports/themis_conditioning/routeC_extra/routeC_extra_summary.json`
- `reports/themis_conditioning/routeC_extra/selection_flow_extra.md`
- `reports/themis_conditioning/routeC_extra/crossprobe_qc_gate_summary_extra.json`
- `reports/themis_conditioning/routeC_extra/crossprobe_overlap_groups_extra.csv`

---

## 7. Frozen anchors unchanged

Phase 4B, 5A/5B, MMS, Route B — all intact.
