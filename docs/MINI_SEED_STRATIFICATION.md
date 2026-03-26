# Provisional Mini Seed Stratification

**Date:** 2026-03-26
**Status:** Planning artifact only. NOT labels. NOT thresholds. NOT dev-set membership.

---

## Purpose

This slate identifies 4 representative windows from the bank for later planning. The seeds span the observed metric range and represent independent orbital passes. They are operational planning tags, not scientific classifications.

Every window in the bank remains a **"measurement-model-valid near-MP comparator window."**

---

## Seed slate

| Seed | Window | Date | Dn | EB | ρ(n,B) | Rationale |
|---|---|---|---|---|---|---|
| seed_A | usable_aug18_6h | 2008-08-18 | 0.12 | 2.49 | -0.46 | Strongest near-MP depletion + B enhancement pattern observed |
| seed_B | usable_sep20_09_6h | 2009-09-20 | 0.97 | 1.48 | -0.63 | Near-neutral Dn behavior (Dn ≈ 1) |
| seed_C | usable_sep03_6h | 2008-09-03 | 2.31 | 0.82 | -0.52 | Strongest near-MP density enhancement (compressed-sheath) |
| seed_D | usable_sep13_09_6h | 2009-09-13 | 0.39 | 1.96 | -0.90 | Strongest n–|B| anti-correlation |

All 4 seeds are from independent orbital passes (4 distinct dates). No two seeds share the same pass.

---

## What the seeds cover

- **Dn range:** 0.12 to 2.31 (3 of the 4 quadrants: low-Dn/high-EB, mid-Dn/mid-EB, high-Dn/low-EB)
- **EB range:** 0.82 to 2.49
- **ρ range:** -0.90 to -0.46
- **Seasons:** 2008 (A, C) and 2009 (B, D)
- **Upstream Bz:** +0.3 (A), +1.4 (B), +0.9 (C), -1.4 (D)

---

## What this stratification is and is not

**Is:**
- A planning artifact for deciding what to review first in a bounded detector preparation
- A way to ensure coverage of different observed behaviors

**Is NOT:**
- A development set
- A labeled set (no window is PDL-positive, non-PDL, or baseline)
- A threshold definition
- A detector output

---

## Remaining deferred decisions

Before any detector-v0 work, these must still be decided (not in this document):
1. Whether these 4 seeds are sufficient for initial threshold exploration
2. Whether additional passes are needed first
3. How to handle the 3 remaining bank windows not selected as seeds
4. What role duration variants should play (additional evidence or redundant)
5. Whether any window's confounder flags (currently tri-state) need resolution first
