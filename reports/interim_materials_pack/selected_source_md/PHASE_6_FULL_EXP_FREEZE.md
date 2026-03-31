# Phase 6 FULL EXP — Freeze / Package Note

**Date:** 2026-03-31
**Type:** Bounded descriptive-methodological result. Packaged and frozen.
**Status:** Phase 6 science closed. Writing-safe.

---

## 1. Exact strongest supportable statement

A full-archive scan of the THEMIS near-subsolar dayside data (2007-2025, all five probes, SZA <= 30 deg, 8 < r < 25 Re) processed 6903 qualifying days and found 757 encounters evaluable under original Dn/EB semantics. Of these, 28 are quasi-radial (cone < 30 deg) and 89 are low-cone (30-45 deg). These bins were previously empty in Phase 4B and in all earlier Phase 6 attempts. The result demonstrates that the low-cone and quasi-radial regimes are fillable under the original measurement-model family when the full multi-probe, multi-year archive is searched without convenience subsampling. Cross-probe comparability with the frozen THD-dominated Phase 4B bank is not yet established.

---

## 2. Exact non-claims

- Phase 6 does NOT validate, extend, or strengthen frozen Phase 4B claims.
- Phase 6 does NOT establish that low-cone Dn/EB values are physically comparable to Phase 4B compressed-sheath THD values.
- Phase 6 does NOT constitute a positive upstream-conditioning result ("cone angle controls depletion behavior").
- Phase 6 does NOT classify any encounter as containing a specific physical structure.
- Phase 6 does NOT define thresholds, labels, classes, or detector semantics.
- Phase 6 does NOT support occurrence rates, mission priors, or SMILE/SXI translation.
- Phase 6B was never opened and remains blocked.

---

## 3. Relationship to Phase 4B

| Aspect | Phase 4B (frozen claim-bearing) | Phase 6 FULL EXP (bounded sidecar) |
|---|---|---|
| Scientific status | Claim-bearing anchor | Descriptive-methodological result |
| Probe coverage | THD only (2008-2009) | THA, THB, THC, THD, THE (2007-2025) |
| Dp regime | > 3 nPa (compressed sheath) | 0.8-6+ nPa (mixed, many low-Dp) |
| Cone-angle coverage | Intermediate + perpendicular only | All bins including quasi-radial |
| Dn/EB range | Dn 0.12-2.31, EB 0.80-4.22 | Much wider (Dn 0.01-8+, EB 0.7-15+) |
| Cross-probe validation | N/A (single probe) | **Not established** |
| Thesis citability | Primary results | Bounded sidecar only |

Phase 6 shows that the bins are fillable. It does not show that the filled values are comparable to Phase 4B or interpretable in the same measurement context.

---

## 4. Relationship to Route B sidecar

Route B (Dn_near, D|B|_near inner-sheath descriptors) is a separate frozen sidecar with modest yield. It is not incorporated into the Phase 6 FULL EXP package. The FULL EXP uses only original Dn/EB semantics. Route B results are documented in `docs/PHASE_6_ROUTEB_BOUNDED_EXECUTION.md` and remain available for future work but are not part of the thesis-safe Phase 6 package.

---

## 5. Mandatory caveats

**5a. Cross-probe comparability.** The quasi-radial and low-cone encounters come primarily from THA, THB (ARTEMIS perigee passes), and THC — probes with different orbital characteristics, calibration histories, and spatial sampling than THD. Direct Dn/EB comparison across probes has not been validated.

**5b. Dp regime difference.** Phase 4B encounters have Dp > 3 nPa (compressed sheath). Phase 6 low-cone encounters have Dp 0.8-1.7 nPa. The measurement model (s-mapping, bin boundaries) behaves differently at different Dp: boundary standoff distances, sheath width, and the meaning of "near" vs "background" all shift.

**5c. Extremely wide Dn/EB range.** Phase 6 low-cone encounters show Dn as low as 0.01 and EB as high as 15. This range is far wider than Phase 4B and may reflect different probe calibration, different background-bin populations, boundary-layer contamination, or genuinely different physics. The cause is unresolved.

**5d. THB/THC ARTEMIS passes.** THB and THC contributed encounters from 2010-2025 via lunar-orbit perigee passes. These are fast magnetosheath fly-throughs, not extended sojourns like the inner-probe encounters.

---

## 6. Thesis placement guidance

Phase 6 belongs **after** the frozen Phase 4B results block, placed as a bounded descriptive-methodological sidecar. Recommended placement:

| Thesis section | Source | Role |
|---|---|---|
| Results: THEMIS comparator bank | Phase 4B frozen docs | **Primary claim-bearing** |
| Results: upstream-conditioning exploration | `PHASE_6_FULL_EXP_FREEZE.md` | Bounded sidecar |
| Discussion: selection-function and regime access | `PHASE_6_FULL_EXP_FREEZE.md` §5 | Caveats and limitations |
| Future work | `PHASE_6_FULL_EXP_FREEZE.md` §7 | Explicit deferral |

**Recommended thesis wording pattern:**

"A full-archive search across all five THEMIS probes (2007-2025) demonstrated that the quasi-radial and low-cone IMF regimes are evaluable under the same Dn/EB measurement family used for the primary comparator bank. However, the newly populated bins draw primarily from probes and Dp regimes not represented in the frozen THD bank, and cross-probe comparability remains unvalidated. A direct physical comparison across cone-angle regimes is therefore deferred to future work."

---

## 7. Future-work boundary sentence

The broader upstream-conditioning question — whether near-magnetopause descriptor behavior shifts systematically across cone-angle regimes — remains open. Phase 6 establishes that the required encounter population exists in the archive. Answering the conditioning question requires cross-probe validation, Dp-controlled sub-stratification, and potentially a dedicated calibration comparison, none of which are attempted here.

---

## 8. Retained encounter summary

| Cone bin | Count | Primary probes | Dp range (nPa) |
|---|---|---|---|
| quasi-radial (< 30 deg) | 28 | THA, THB, THC | 0.8-2.5 |
| low-cone (30-45 deg) | 89 | THA, THB, THC, THD, THE | 0.8-4.0 |
| intermediate (45-60 deg) | 199 | all five | 0.8-6+ |
| perpendicular (> 60 deg) | 441 | all five | 0.8-6+ |
| **Total retained** | **757** | | |

By year: 2007 (56), 2008 (48), 2009 (39), 2010 (9), 2013-2015 (62), 2016-2019 (241), 2020-2025 (302).

---

## 9. Key files

| File | Role |
|---|---|
| `docs/PHASE_6_FULL_EXP_FREEZE.md` | This document |
| `docs/PHASE_6_ROUTEC_FULL_EXP_RESULT.md` | Execution result with encounter tables |
| `docs/PHASE_6_ROUTEC_FULL_EXP_PLAN.md` | Pre-registered execution plan |
| `docs/PHASE_6_FULL_EXP_ACTIVATION.md` | EXP activation record |
| `docs/THEMIS_ARCHIVE_DATA_GUIDE.md` | Data cache layout and usage (engineering only) |
| `data_cache/themis_archive/` | Full local cache (1135 STATE, 6118 encounters, indexes) |
| `reports/themis_conditioning/routeC_exp/` | Route C EXP outputs (2007-2010 subset) |

---

## 10. Frozen anchors unchanged

Phase 4B six-pass bank, THE Sep 19 external recurrence, Phase 5A/5B caseset sidecars, MMS branch freeze — all intact and unmodified.
