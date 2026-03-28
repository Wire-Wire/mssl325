# MMS Event Shortlist — Pilot-Readiness Screening

**Date:** 2026-03-28
**Stage:** Bounded shortlist screening only. No thickness values. No physical identification.
**Authority:** User-authorized red-level decision.

---

## A. Authority and boundaries

This round screens MMS near-subsolar dayside passes for pilot-readiness: whether they are well-posed enough that a future thickness attempt could plausibly produce a defensible `L ± σ`. It does not compute thickness, does not identify physical classes, and does not connect to the frozen THEMIS comparator branch.

---

## B. Candidate source and screening order

**Source:** MMS1 position (MMS1_MEC_SRVY_L2_EPHT89D), FGM (MMS1_FGM_SRVY_L2), FPI ions (MMS1_FPI_FAST_L2_DIS-MOMS), and OMNI (OMNI_HRO_1MIN), all from CDAWeb via cdasws.

**Screening population:** MMS Phase 1 dayside seasons (Oct 2015 – Feb 2017). Dates sampled at weekly intervals. 20 dates produced near-subsolar apogee (R > 9 Re, X > 7 Re, SZA < 35°). The 11 best geometry candidates (SZA < 20°) were screened first, in chronological order.

**Stop rule:** Stop when 3 primary + up to 2 reserve candidates are found, or 20 event-contexts are screened, whichever comes first. The 3-primary target was reached after 11 screenings.

---

## C. Screening-unit definition

The top-level screening unit is an **event-context**: one MMS dayside apogee pass, assessed for data completeness, upstream steadiness, and gradient structure within a ±2 hour window around apogee.

A surviving event-context nominates one **provisional primary gradient interval** — the best-looking sustained density/|B| gradient visible in the quicklook. This is not a final feature pairing and not a de facto physical layer definition. It is a screening-level interval nomination for future detailed analysis.

---

## D. Registry summary

| Item | Count |
|---|---|
| Total screened | 11 |
| Primary | 3 |
| Reserve | 1 |
| Fail | 7 |

### Fail reasons

| Reason | Count |
|---|---|
| no_sustained_gradient | 6 |
| data_coverage_fail (FPI) | 1 |

Most failures were due to the absence of a sustained density gradient in the ±2h apogee window. These passes likely sampled relatively undisturbed outer sheath with no clear boundary-adjacent gradient structure during the observation window.

---

## E. Primary candidates

### MMS-P1: 2015-11-12

- **Position:** X = 11.4 Re, SZA = 18°
- **Upstream:** Dp = 1.1 nPa, steady (CV = 0.11)
- **FGM:** 230,397 points (survey mode)
- **FPI:** 3,200 points (fast mode)
- **Gradient structure:** Density CV = 0.45 over the ±2h window. Sustained density variation visible in quicklook.
- **Disposition:** primary
- **Caveats:** Low Dp (1.1 nPa) — boundaries are further out. The low Dp may mean the spacecraft is deep in the sheath rather than near the MP gradient. This must be checked in a future full-event package.
- **Quicklook:** `reports/mms_shortlist/figures/mms_20151112_quicklook.png`
- **Recommendation:** Deserves a full event package with detailed interval assessment.

### MMS-P2: 2015-12-12

- **Position:** X = 11.8 Re, SZA = 11°
- **Upstream:** Dp = 2.0 nPa, steady (CV = 0.14)
- **FGM:** 230,397 points
- **FPI:** 3,200 points
- **Gradient structure:** Density CV = 0.35. Moderate density variation.
- **Disposition:** primary
- **Caveats:** Moderate gradient amplitude. Need to confirm that the gradient is boundary-adjacent rather than mid-sheath fluctuation.
- **Quicklook:** `reports/mms_shortlist/figures/mms_20151212_quicklook.png`
- **Recommendation:** Deserves a full event package.

### MMS-P3: 2016-12-26

- **Position:** X = 11.9 Re, SZA = 6°
- **Upstream:** Dp = 2.6 nPa, steady (CV = 0.15)
- **FGM:** 230,396 points
- **FPI:** 3,200 points
- **Gradient structure:** Density CV = 0.47 over the window. Strongest density variation among primaries.
- **Disposition:** primary
- **Caveats:** Best geometry (SZA = 6°) and strongest gradient signal. Higher Dp (2.6) places boundaries closer to spacecraft. Must verify MP crossing is present.
- **Quicklook:** `reports/mms_shortlist/figures/mms_20161226_quicklook.png`
- **Recommendation:** Strongest primary candidate. Deserves a full event package.

---

## F. Reserve candidate

### MMS-R1: 2017-01-05

- **Position:** X = 11.9 Re, SZA = 7°
- **Upstream:** Dp = 2.6 nPa, steady (CV = 0.23)
- **FGM:** 230,397 points
- **FPI:** 3,200 points
- **Gradient structure:** Density CV = 0.44. Similar to MMS-P3.
- **Disposition:** reserve
- **Caveats:** Very similar geometry and upstream to MMS-P3 (~10 days later). May sample the same large-scale sheath conditions. Upstream slightly less steady than primaries.
- **Quicklook:** `reports/mms_shortlist/figures/mms_20170105_quicklook.png`

---

## G. Why failed candidates failed

| Date | SZA | Fail reason | Detail |
|---|---|---|---|
| 2015-11-19 | 12° | FPI unavailable | No FPI fast-mode data in the window |
| 2015-11-26 | 7° | no_sustained_gradient | Density CV = 0.10; flat sheath |
| 2015-12-05 | 6° | no_sustained_gradient | Density CV = 0.13; flat sheath |
| 2015-12-19 | 17° | no_sustained_gradient | Density CV = 0.17; flat sheath |
| 2016-12-12 | 18° | no_sustained_gradient | Density CV = 0.22; weak fluctuation |
| 2016-12-19 | 12° | no_sustained_gradient | Density CV = 0.14; flat sheath |
| 2017-01-12 | 13° | no_sustained_gradient | Density CV = 0.18; flat sheath |

The dominant failure mode is the absence of a near-MP gradient structure during the observation window. This is expected: not every dayside apogee pass encounters the spacecraft in a region of active boundary-adjacent gradient.

---

## H. Strongest supportable statement

Three MMS1 near-subsolar dayside passes (Nov 12 and Dec 12 2015, Dec 26 2016) show sufficient data completeness, upstream steadiness, and coarse density gradient structure to warrant a future full-event assessment for thickness feasibility. One additional reserve candidate exists. No thickness values, no physical identifications, and no quality grades are assigned at this screening stage.

---

## I. Exact non-claim

This shortlist does not constitute a thickness-capable event set. Coarse screening cannot confirm that the observed density variations are boundary-adjacent MP gradient structures. Detailed interval analysis, multi-spacecraft timing, and normal estimation are required before any thickness attempt is justified. No event is identified as a PDL case or any other physical class.

---

## J. Exact next red-level decision

**At least 2 defensible primary candidates were found (3 primaries + 1 reserve).**

The user is asked to decide:

**Authorize full event packages + first thickness attempt on the 3 primary candidates only?**

This would involve:
- Detailed multi-spacecraft interval analysis per the MMS scaffold
- Start/end feature identification and pairing
- Normal estimation with cross-checks
- Timing-based and gradient-scale thickness computations
- Uncertainty budget and quality grading
- Per-event evidence packages

Alternatively:
- Revise the shortlist basis (different source, different gates)
- Or pause the MMS branch
