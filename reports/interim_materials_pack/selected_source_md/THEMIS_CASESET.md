# Phase 5A — THEMIS Case-Study Confirmation Set

**Date:** 2026-03-29
**Stage:** Additive caseset sidecar on frozen THEMIS science base.
**Authority:** User-authorized red-level THEMIS reopen (Phase 5A only).

---

## Scope and non-claims

This document describes a small confirmation/illustration atlas built from the frozen THEMIS evidence path plus the external recurrence record. It provides standardized case cards with Phase 5A review statuses (clear / ambiguous / not convincing) for thesis packaging.

**This atlas does NOT:**
- strengthen, weaken, or replace any frozen Phase 4B claim
- introduce detector semantics, thresholds, or labels
- define physical classes or positive/negative examples
- constitute conditioned occurrence statistics
- authorize mission-facing priors or translation work
- change frozen bank membership, numerical values, or evidence hierarchy

Phase 5A review statuses are editorial packaging concepts, not scientific confidence classes.

---

## Operational filters used

| Screen | Rule | Basis |
|---|---|---|
| Near-subsolar | SZA ≤ 30° | Hard screen from task specification |
| Clock-angle grouping | \|clock\| < 60°, 60–120°, > 120° | Organizational grouping from atan2(By_GSM, Bz_GSM) |
| Non-quasi-radial | 30-min mean \|cone angle\| > 30° | **Fallback operationalization** — no inherited project cutoff found in existing artifacts |
| Upstream stable | Dp CV < 0.3 over 30-min centered window | Conservative coarse yes/no gate — simple rule-based |

### Fallback/coarsening decisions logged

1. **Non-quasi-radial cutoff:** No stable inherited project cutoff existed in current artifacts. Used conservative fallback: 30-min mean absolute IMF cone angle > 30° = non-quasi-radial. This is an operational screen only, not a new physical threshold.
2. **Upstream stability:** Used Dp CV < 0.3 as a simple coarse gate. No new stability scalar was invented.
3. **Near-MP indicators:** Used frozen Dn < 1 as "n down," EB > 1 as "|B| up," and delta_beta < 0 as "beta down." These are the coarsest operationalizations consistent with the frozen measurement model.

---

## Selection flow

### Step 1 — Seed pass from frozen THEMIS layer

Screened all 7 frozen-bank passes (P1–P7) plus the external recurrence (THE 2008-09-19).

| Pass | SZA | Cone | Stable | Non-QR | Clock group | All screens pass? |
|---|---|---|---|---|---|---|
| P1 | 22° | 24° | ✓ | **FAIL** | >120 | No |
| P2 | 14° | 51° | ✓ | ✓ | <60 | Yes |
| P3 | 17° | 61° | ✓ | ✓ | >120 | Yes |
| P4 | 10° | 81° | ✓ | ✓ | >120 | Yes |
| P5 | 4° | 58° | ✓ | ✓ | 60–120 | Yes |
| P6 | 4° | 59° | ✓ | ✓ | 60–120 | Yes |
| P7 | 20° | 69° | ✓ | ✓ | >120 | Yes |
| EXT | 15° | 65° | ✓ | ✓ | >120 | Yes |

P1 fails the non-quasi-radial screen (cone = 24° < 30° fallback cutoff).

### Step 2 — Review-status assignment (7 screen-passing cases)

| Pass | n↓ | \|B\|↑ | β↓ | Review status | Atlas-usable |
|---|---|---|---|---|---|
| P3 | ✓ | ✓ | ✓ | **clear** | yes |
| P4 | ✓ | ✓ | ✓ | **clear** | yes |
| P5 | ✓ | ✓ | ✓ | **clear** | yes |
| EXT | ✓ | ✓ | ✓ | **clear** | yes |
| P6 | ✗ | ✓ | ✓ | ambiguous | yes |
| P2 | ✗ | ✗ | ✗ | not convincing | no |
| P7 | ✗ | ✓ | ✓ | not convincing | no |

### Stop condition

**Preferred target met:** 4 clear + 1 ambiguous = 5 atlas-usable cards from seed pass alone. No bounded extension needed.

---

## Final card inventory

| Count | Status |
|---|---|
| 4 | clear |
| 1 | ambiguous |
| 2 | not convincing |
| 1 | screen fail (quasi-radial) |
| **8** | **total screened** |

---

## Summary table

| Case | Date | SC | Clock group | n↓ | \|B\|↑ | β↓ | Review status |
|---|---|---|---|---|---|---|---|
| P3 | 2009-09-13 | THD | >120 | ✓ | ✓ | ✓ | clear |
| P4 | 2009-09-20 | THD | >120 | ✓ | ✓ | ✓ | clear |
| P5 | 2009-09-26 | THD | 60–120 | ✓ | ✓ | ✓ | clear |
| EXT | 2008-09-19 | THE | >120 | ✓ | ✓ | ✓ | clear |
| P6 | 2009-09-27 | THD | 60–120 | ✗ | ✓ | ✓ | ambiguous |
| P2 | 2008-09-03 | THD | <60 | ✗ | ✗ | ✗ | not convincing |
| P7 | 2009-10-24 | THD | >120 | ✗ | ✓ | ✓ | not convincing |

Raw counts by status: 4 clear, 1 ambiguous, 2 not convincing.
Raw counts by clock group: <60° = 1 (not convincing), 60–120° = 2 (1 clear, 1 ambiguous), >120° = 4 (3 clear, 1 not convincing).

---

## Clock-angle coverage note

The <60° group contains only P2, which is reviewed as not convincing (all three indicators reversed). This group remains sparse. This is not filled by extending the search — it reflects the frozen bank's composition under the Phase 5A screens.

---

## Case atlas

See `reports/themis_caseset/INDEX.md` for the case card and figure index.
See `reports/themis_caseset/caseset_summary.json` for structured machine-readable summary.

---

## What is minimally ready for a later Phase 5B

- 5 atlas-usable case cards (4 clear + 1 ambiguous) with standardized upstream context and sheath-side indicators
- Structured `caseset_summary.json` reusable for a bounded conditioned descriptive pass
- Clock-angle grouping already applied
- All cases already carry frozen Dn/EB values and Phase 5A review statuses

## What remains out of scope

- Conditioned occurrence statistics
- Clock-angle-dependent trends or rates
- Physical mechanism language
- Detector semantics, thresholds, labels
- Mission-facing priors
- Any strengthening of frozen Phase 4B claims
