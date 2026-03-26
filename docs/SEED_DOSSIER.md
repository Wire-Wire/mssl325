# Provisional Seed Dossier

**Date:** 2026-03-26
**Status:** Planning artifact only. Not labels. Not thresholds. Not dev-set membership.

---

## What this dossier is

This dossier identifies 4 representative windows from the bank for later human review. The seeds were selected to span the observed metric range while using only independent orbital passes. They are **operational planning tags**, not scientific classifications.

Every window in this dossier remains a **measurement-model-valid near-MP comparator window**.

---

## What this dossier is NOT

- Not a development set
- Not a labeled set — no window is PDL-positive, non-PDL, or assigned to any physical class
- Not a threshold definition — the seed boundaries are descriptive, not diagnostic
- Not evidence for or against any particular physical interpretation
- Not detector-ready input — human review is required before any threshold exploration

---

## Seed slate

| Seed | Window | Pass | Dn | EB | ρ(n,B) | Operational description |
|---|---|---|---|---|---|---|
| seed_A | usable_aug18_6h | P1 | 0.12 | 2.49 | -0.46 | Lowest observed Dn, highest EB among seeds |
| seed_B | usable_sep20_09_6h | P4 | 0.97 | 1.48 | -0.63 | Dn near unity, moderate EB |
| seed_C | usable_sep03_6h | P2 | 2.31 | 0.82 | -0.52 | Highest observed Dn, EB below unity |
| seed_D | usable_sep13_09_6h | P3 | 0.39 | 1.96 | -0.90 | Most negative ρ observed in the bank |

All 4 seeds are from independent orbital passes. No two seeds share a pass.

---

## Per-seed notes

### seed_A (usable_aug18_6h)

- **Observed behavior:** Dn = 0.12 (lowest in bank), EB = 2.49 (high), persistence = 0.94 (high)
- **Upstream:** Dp = 4.2 nPa, Bz = +0.3 nT
- **Why useful for planning:** Occupies one extreme of the observed Dn–EB space. Would be a natural starting point if a human reviewer wants to inspect the lowest-Dn end of the bank.
- **Caveats:** Membership = 86% (lowest in bank). ρ = -0.46 (weakest anti-correlation among seeds). The low Dn value could reflect measurement-model artifacts at this Dp, not necessarily a physical depletion signal. This window must NOT be treated as a PDL identification.

### seed_B (usable_sep20_09_6h)

- **Observed behavior:** Dn = 0.97 (near unity), EB = 1.48, persistence = 0.66
- **Upstream:** Dp = 3.0 nPa, Bz = +1.4 nT
- **Why useful for planning:** Represents intermediate metric behavior. Useful as a comparator against the extremes (seeds A and C).
- **Caveats:** Near-bin occupancy is the lowest in the bank (9%). The near-unity Dn may reflect near-background similarity rather than any meaningful depletion or enhancement.

### seed_C (usable_sep03_6h)

- **Observed behavior:** Dn = 2.31 (highest in bank), EB = 0.82 (below 1), persistence = 0.00
- **Upstream:** Dp = 3.5 nPa, Bz = +0.9 nT
- **Why useful for planning:** Occupies the opposite extreme from seed_A in Dn–EB space. The Dn > 1 / EB < 1 pattern is operationally distinct from seed_A's Dn < 1 / EB > 1 pattern.
- **Caveats:** EB < 1 and Dn > 1 could reflect a variety of sheath conditions under the encounter-averaged measurement model. This window must NOT be interpreted as a "non-PDL" or "compressed-sheath" identifier.

### seed_D (usable_sep13_09_6h)

- **Observed behavior:** Dn = 0.39, EB = 1.96, ρ = -0.90 (most negative in bank), persistence = 1.00
- **Upstream:** Dp = 3.1 nPa, Bz = -1.4 nT (southward)
- **Why useful for planning:** Shows the strongest observed trend anti-correlation. The only seed with southward Bz.
- **Caveats:** Universally negative ρ across the bank means ρ alone does not discriminate between windows. The strong ρ here may reflect this pass's particular s-range coverage rather than a distinctive physical process.

---

## Remaining bank windows not selected as seeds

| Window | Pass | Dn | EB | Why not a seed |
|---|---|---|---|---|
| usable_aug18_8h | P1 | 0.88 | 2.08 | Duration variant of seed_A's pass |
| usable_sep03_8h | P2 | 2.07 | 0.80 | Duration variant of seed_C's pass |
| usable_sep26_09_10h | P5 | 0.94 | 1.96 | Operationally similar to seed_B in Dn; strong ρ covered by seed_D |
| usable_sep27_09_10h | P6 | 1.31 | 1.23 | Intermediate — no extreme metric channel distinguishes it from seeds |
| usable_oct24_09_6h | P7 | 2.19 | 4.22 | Highest EB in bank (4.22), but Dn similar to seed_C; could serve as an alternate |

These windows are available for later review. They are not excluded — they are simply not selected as planning seeds in this slate.

---

## Explicit prohibitions on this dossier

1. No seed may be described as "PDL-positive," "non-PDL," "baseline," "control," or "confirmed event."
2. No seed may be used to define a detector threshold.
3. No seed may be treated as a member of a development or validation set.
4. The Dn/EB values in this dossier are outputs of the frozen measurement model under encounter-averaged conditions. They are NOT direct physical measurements of depletion or pileup.
5. This dossier does not constitute scientific evidence for or against the presence of a plasma depletion layer in any window.
