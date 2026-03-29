# Phase 5B — Caseset-Grouped Descriptive Inventory

**Date:** 2026-03-29
**Stage:** Grouped descriptive sidecar from completed Phase 5A caseset. Not conditioned statistics.
**Authority:** User-authorized Phase 5B. Uses caseset_summary.json only. No new search.
**Source:** `reports/themis_caseset/caseset_summary.json` (8 records from Phase 5A seed pass)

---

## Scope and non-claims

This document reorganizes the Phase 5A caseset into clock-angle groups and reports what review statuses and sheath-side indicators appear in each group. It is descriptive caseset bookkeeping only.

**This is NOT:** conditioned statistics, rates analysis, IMF dependence result, mechanism inference, detector prior, class inventory, or any strengthening of frozen Phase 4B claims.

**Review statuses** (clear / ambiguous / not convincing) are Phase 5A editorial packaging only, not scientific confidence classes or physical identifications.

---

## Operational screens inherited from Phase 5A

All cases passed or were excluded by these screens before grouping:
- SZA ≤ 30° (hard screen)
- Non-quasi-radial: |cone angle| > 30° (**fallback** — no inherited project cutoff)
- Upstream stable: Dp CV < 0.3 over 30-min centered window (**coarse rule-based gate**)

These are operational inclusion screens, not analysis axes.

---

## Grouped inventory by coarse clock-angle bin

### Clock angle < 60°

**Screened cases:** 1
**Atlas-usable:** 0

| Case | Clock | n↓ | \|B\|↑ | β↓ | Review status |
|---|---|---|---|---|---|
| P2 | 49° | no | no | no | not convincing |

P2 (2008-09-03, THD) is the only case in this bin. All three sheath-side indicators are reversed (Dn = 2.31, EB = 0.82, delta_beta = +1.7). It is reviewed as not convincing. This bin has no atlas-usable cases.

### Clock angle 60–120°

**Screened cases:** 2
**Atlas-usable:** 2 (1 clear + 1 ambiguous)

| Case | Clock | n↓ | \|B\|↑ | β↓ | Review status |
|---|---|---|---|---|---|
| P5 | 80° | yes | yes | yes | clear |
| P6 | 120° | no | yes | yes | ambiguous |

P5 (2009-09-26, THD, clean core) has all three indicators jointly present and is reviewed as clear. P6 (2009-09-27, THD, clean core) has |B|↑ and β↓ but not n↓ (Dn = 1.31 > 1), and is reviewed as ambiguous. Both are atlas-usable.

### Clock angle > 120°

**Screened cases:** 5 (including 1 screen fail, 1 not convincing)
**Atlas-usable:** 3 (all reviewed as clear)

| Case | Clock | n↓ | \|B\|↑ | β↓ | Review status | Note |
|---|---|---|---|---|---|---|
| P3 | 156° | yes | yes | yes | clear | cautious in frozen bank |
| P4 | 165° | yes | yes | yes | clear | clean core |
| EXT | 169° | yes | yes | yes | clear | external recurrence only |
| P7 | 146° | no | yes | yes | not convincing | excluded from frozen bank (spike-dominated) |
| P1 | 142° | — | — | — | screen fail | quasi-radial (cone = 24°), excluded from Phase 5A |

P3, P4, and EXT all have the three sheath-side indicators jointly present and are reviewed as clear. P7 is not convincing because it was excluded from the frozen bank as spike-dominated. P1 failed the non-quasi-radial screen.

EXT (THE 2008-09-19) remains external recurrence only; its Phase 5A review status does not change its frozen branch status as an external record not admitted to the main bank.

---

## Summary table

| Clock group | Screened | Atlas-usable | Clear | Ambiguous | Not convincing | Screen fail |
|---|---|---|---|---|---|---|
| < 60° | 1 | 0 | 0 | 0 | 1 | 0 |
| 60–120° | 2 | 2 | 1 | 1 | 0 | 0 |
| > 120° | 5 | 3 | 3 | 0 | 1 | 1 |
| **Total** | **8** | **5** | **4** | **1** | **2** | **1** |

---

## Indicator presence among atlas-usable cases

| Case | Clock group | n↓ | \|B\|↑ | β↓ | All three joint |
|---|---|---|---|---|---|
| P5 | 60–120° | ✓ | ✓ | ✓ | yes |
| P6 | 60–120° | ✗ | ✓ | ✓ | no (n not down) |
| P3 | > 120° | ✓ | ✓ | ✓ | yes |
| P4 | > 120° | ✓ | ✓ | ✓ | yes |
| EXT | > 120° | ✓ | ✓ | ✓ | yes (external recurrence) |

Of the 5 atlas-usable cases, 4 have all three indicators jointly present and 1 (P6) has two of three.

---

## One conservative takeaway

Within this small seed-derived caseset (8 screened from the frozen bank + external recurrence), atlas-usable review outcomes occur only in the 60–120° and >120° clock-angle bins, while the sole <60° screened case is reviewed as not convincing.

**This is descriptive caseset bookkeeping only.** It is not a rate, not a trend, not a mechanism claim, and not a threshold or class boundary. The caseset is too small (N = 8 screened, 5 atlas-usable) and too selection-function-constrained (compressed-sheath THD only, two seasons) to support any conditioned inference.

---

## What this inventory provides for thesis use

- A compact grouped summary of the Phase 5A atlas by coarse upstream context
- Explicit indicator presence/absence for each atlas-usable case
- Traceability from caseset_summary.json to grouped prose

## What this inventory does NOT provide

- Conditioned occurrence rates or fractions
- Subgroup medians, means, or trends
- Mechanism or IMF-dependence claims
- Detector-facing priors or class balance
- Any strengthening of frozen Phase 4B claims
