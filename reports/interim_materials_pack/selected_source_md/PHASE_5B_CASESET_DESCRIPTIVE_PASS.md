# Phase 5B — Caseset-Grouped Descriptive Pass

**Date:** 2026-03-29
**Stage:** Grouped descriptive sidecar from completed Phase 5A caseset. Not conditioned statistics.
**Authority:** User-authorized Phase 5B. Uses caseset_summary.json only. No new search.
**Source:** `reports/themis_caseset/caseset_summary.json` (8 records from Phase 5A seed pass)

---

## 1. Scope and non-claims

This document reorganizes the Phase 5A caseset into clock-angle groups and reports what review statuses and sheath-side indicators appear in each group. It is a caseset-grouped descriptive sidecar only.

**This is NOT:** conditioned statistics, rates analysis, IMF dependence result, mechanism inference, detector prior, class inventory, or any strengthening of frozen Phase 4B claims.

**Review statuses** (reviewed as clear / reviewed as ambiguous / reviewed as not convincing) are Phase 5A editorial packaging only, not scientific confidence classes or physical identifications.

---

## 2. Input universe and conditioned subset

**Input:** 8 cases from Phase 5A seed pass (P1–P7 from frozen bank + EXT external recurrence).

**Inherited inclusion screens (operational, not analysis axes):**
- SZA ≤ 30° (hard screen)
- Non-quasi-radial: |cone angle| > 30° (**fallback** — no inherited project cutoff found)
- Upstream stable: Dp CV < 0.3 over 30-min centered window (**coarse rule-based gate**)

**After screening:** 7 cases pass all screens. P1 fails the non-quasi-radial screen (cone = 24°).

**Atlas-usable subset:** 5 of 7 screen-passing cases (4 reviewed as clear + 1 reviewed as ambiguous). P2 and P7 are reviewed as not convincing.

---

## 3. Grouped descriptive inventory by clock-angle bin

### Compact grouped table

| Clock group | Screened IDs | Atlas-usable IDs (review status) | n↓ | \|B\|↑ | β↓ | Note |
|---|---|---|---|---|---|---|
| < 60° | P2 | — | — | — | — | Sole case reviewed as not convincing (all indicators reversed) |
| 60–120° | P5, P6 | P5 (clear), P6 (ambiguous) | P5: ✓, P6: ✗ | both ✓ | both ✓ | P6 has Dn > 1 |
| > 120° | P3, P4, EXT, P7, P1 | P3 (clear), P4 (clear), EXT (clear) | all ✓ | all ✓ | all ✓ | EXT = external recurrence only; P7 not convincing (spike-dominated); P1 screen fail (quasi-radial) |

### Per-bin detail

**< 60° (1 screened, 0 atlas-usable).** P2 (2008-09-03, THD, clock = 49°) is the only case. All three sheath-side indicators are reversed (Dn = 2.31, EB = 0.82, delta_beta = +1.7). Reviewed as not convincing. This bin has no atlas-usable cases. The bin is sparse — it contains only one screened case from the frozen seed pass, which reflects the bank's composition under Phase 5A screens, not a subgroup-level negative result.

**60–120° (2 screened, 2 atlas-usable).** P5 (2009-09-26, THD, clock = 80°, clean core) has all three indicators jointly present and is reviewed as clear. P6 (2009-09-27, THD, clock = 120°, clean core) has |B|↑ and β↓ but not n↓ (Dn = 1.31 > 1), and is reviewed as ambiguous. Both are atlas-usable.

**> 120° (5 screened, 3 atlas-usable).** P3 (2009-09-13, THD, clock = 156°, cautious in frozen bank), P4 (2009-09-20, THD, clock = 165°, clean core), and EXT (2008-09-19, THE, clock = 169°, external recurrence only) all have the three indicators jointly present and are reviewed as clear. P7 (2009-10-24, THD, clock = 146°) is reviewed as not convincing because it was excluded from the frozen bank as spike-dominated. P1 (2008-08-18, THD, clock = 142°) failed the non-quasi-radial screen (cone = 24°).

EXT remains external recurrence only; its Phase 5A review status does not change its frozen branch status.

---

## 4. Coverage / empty-bin note

The < 60° clock-angle bin contains only one screened case (P2), which is reviewed as not convincing. This bin is sparse. The sparsity reflects the frozen bank's composition and the Phase 5A seed-pass design, not a concluded absence of near-MP sheath-side patterns at low clock angles. The caseset (N = 8 screened, 5 atlas-usable) is too small and too selection-function-constrained (compressed-sheath THD only, two seasons) to draw any clock-angle-conditioned inference.

---

## 5. Minimal takeaways

Within this small seed-derived caseset (8 screened from the frozen bank + external recurrence), atlas-usable review outcomes occur only in the 60–120° and >120° clock-angle bins, while the sole <60° screened case is reviewed as not convincing.

**This is descriptive caseset bookkeeping only.** It is not a rate, not a trend, not a mechanism claim, and not a threshold or class boundary.

Among the 5 atlas-usable cases, 4 have all three sheath-side indicators (n↓, |B|↑, β↓) jointly present. The one exception (P6, reviewed as ambiguous) has |B|↑ and β↓ but not n↓.

---

## 6. What remains later / not this round

**This inventory provides:**
- A compact grouped summary of the Phase 5A atlas by coarse upstream context
- Explicit indicator presence/absence per atlas-usable case per bin
- Traceability from caseset_summary.json to grouped prose

**This inventory does NOT provide:**
- Conditioned occurrence rates or fractions
- Subgroup medians, means, or trends
- Mechanism or IMF-dependence claims
- Detector-facing priors or class balance
- Any strengthening of frozen Phase 4B claims

Any further THEMIS analysis beyond this grouped descriptive sidecar requires a separate broader reopen decision by the user.
