# Phase 4A — Independent Low-Dn Recurrence Test

**Date:** 2026-03-27
**Authority:** User-authorized as a bounded descriptive stage. Not detector work.
**Single question:** Can low-Dn-like comparator behavior recur in candidates independent of the current six-pass bank?

---

## Scope and guardrails

This stage is descriptive only. It does not define thresholds, labels, detector semantics, or dev-set membership. No candidate is auto-admitted to the main bank. All existing Phase 3A/3B evidence values are unchanged.

---

## Search-space audit

### What was searched

| Search axis | Range | Independence from current bank |
|---|---|---|
| THD 2008 Aug–Oct | every other day, excluding bank dates | Same probe, same season — weakest independence |
| THD 2009 Aug–Oct | every other day, excluding bank dates | Same probe, adjacent season |
| **THE 2008 Aug–Oct** | every other day | **Cross-probe** — THE has same orbit as THD but independent instrument chain |
| **THD 2010 Sep–Oct** | every other day | **Different year** — 2 years later than 2008 season |

### Independence rules applied

1. No date overlapping a current bank pass
2. No duration variant of a current bank pass
3. Cross-probe (THE) counted as independent because it provides an independent instrument chain on the same orbital geometry
4. Different-year (2010) counted as independent because it samples a different solar-cycle phase

### Selection function inherited

All candidates inherit the same frozen-model constraints:
- ~11.6 Re apogee (THD/THE inner probes)
- Dp > ~2.5 nPa required for any dual-bin potential
- Dayside SZA < 40°
- MOM L2 data availability
- Encounter-averaged s-mapping

---

## Candidate shortlist

| ID | Probe | Date | Status | SZA | Dp | Bz | Near% | BG% | Dn | EB | ρ | Memb% | Independence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **cand4a_sep19_08_the** | **THE** | **2008-09-19** | **PASS** | **15°** | **2.8** | **-1.8** | **12%** | **29%** | **0.76** | **2.12** | **-0.90** | **84%** | **Cross-probe** |
| cand4a_oct23_10_thd | THD | 2010-10-23 | PASS | 14° | 3.1 | +2.2 | 9% | 2% | 1.30 | 1.02 | +0.43 | 100% | Different year |
| cand4a_sep03_09_thd | THD | 2009-09-03 | FAIL | 26° | 3.6 | -0.2 | 25% | 0% | — | — | — | 99% | Same probe/season |
| cand4a_sep25_08_the | THE | 2008-09-25 | FAIL | 18° | 2.8 | -2.0 | 24% | 0% | — | — | — | 100% | Cross-probe |

---

## Key findings

### 1. One independent candidate below the clean-core Dn floor

**THE Sep 19 2008 (cand4a_sep19_08_the)** produces Dn = 0.76 under the frozen measurement model. This is:
- Below the clean-core Dn floor (0.94)
- Above the current cautious-only range (P1: 0.12, P3: 0.39)
- From a **different probe** (THE, not THD) — the strongest available independence axis
- Under southward Bz = -1.8 nT and relatively low Dp = 2.8 nPa

### 2. No independent candidate enters the cautious-only low-Dn region (Dn < 0.5)

The deepest independent Dn observed is 0.76. No independent candidate reaches Dn < 0.5. The P1/P3 cautious range (0.12–0.39) remains unrecurred by any independent pass found in this search.

### 3. The THE Sep 19 candidate carries its own caveats

| Dimension | Assessment |
|---|---|
| Near-bin occupancy | 12% — low but above 2% threshold |
| Background occupancy | 29% — adequate |
| Membership | 84% — moderate (same level as P1, lowest in main bank) |
| Dp | 2.8 nPa — below the bank's practical 3 nPa preference; near lower edge |
| Bz | -1.8 nT southward — consistent Bz regime with P3 |
| Mach | 21.1 — very high; boundary-model accuracy less tested at extreme Ma |
| ρ | -0.90 — strong, but non-discriminative (universal in current bank) |

**This candidate is not less caveated than P1/P3.** It has moderate membership (84%), low near-occupancy (12%), borderline Dp (2.8), and extreme Ma (21.1). It is comparable to P1 in caveat severity, not cleaner.

### 4. Why the search space is limited

The failure to find recurrence below Dn < 0.5 is driven by:

1. **Selection-function limits** — the frozen model requires Dp > ~2.5 nPa for dual-bin leverage at 11.6 Re apogee. This excludes lower-Dp conditions that may be more favorable for sustained near-MP depletion.
2. **Encounter-averaging** — the single-boundary-set per encounter smooths over Dp variations. A pass where Dp is high early (compressing boundaries) and low later (relaxing them) gets averaged to moderate Dp, which may obscure interval-level low-Dn structure.
3. **Orbital constraint** — THD/THE/THC all have ~11.6 Re apogee. No inner THEMIS probe reaches the outer sheath at low Dp. THB reaches further but has sparse MOM data.
4. **Physical rarity under compressed sheath** — if low-Dn behavior is primarily associated with magnetic pileup under conditions that also favor wider sheath (lower Dp, northward Bz), then the compressed-sheath selection filter structurally disfavors the regime most likely to produce it.

### 5. Is a more independent search space feasible?

Under the frozen measurement model: **marginally.** The main axes already tested (cross-probe, different year) are the strongest available. The remaining untested axes are:
- **THC** (same orbit as THD/THE, MOM starts Jan 2008) — would provide a third probe but no new orbital geometry
- **THB** (wider orbit, reaches outer sheath at low Dp) — but sparse MOM data in the sheath makes most passes unusable
- **Different THEMIS years** (2011–2012) — possible but orbit has been lowered, reducing apogee further

No fundamentally different search space is available without relaxing the frozen measurement model (e.g., accepting GMOM instead of MOM, or implementing time-varying s).

---

## Regime and context summary for shortlisted candidates

| Candidate | Cone angle context | Radial IMF? | Foreshock risk | Jet plausibility | Mixing plausibility | Boundary-motion caveat |
|---|---|---|---|---|---|---|
| THE Sep 19 | Not computed (BX_GSE not cached) | Unknown | Southward Bz disfavors strong foreshock | Long-window artifact expected | Moderate (84% membership) | Bank-wide caveat |
| THD Oct 23 | Not computed | Unknown | Northward Bz | Long-window artifact expected | Low (99.9% membership) | Bank-wide caveat |

---

## Recurrence verdict

Low-Dn-like behavior (Dn < 1) does recur independently: THE Sep 19 2008 produces Dn = 0.76 on a different probe. This is below the clean-core floor (0.94) and provides the first cross-probe evidence that the frozen measurement model can produce Dn < 1 from an instrument chain independent of THD.

However, this recurrence is:
1. Above the cautious-only range (Dn < 0.5) — the P1/P3 region is not recurred
2. Not less caveated than P1/P3 — THE Sep 19 carries moderate membership (84%), low near-occupancy (12%), borderline Dp (2.8), and extreme Ma (21.1)
3. A single additional independent pass — not a pattern

---

## Exact strongest claim now supportable

Under the frozen measurement model, one independent cross-probe candidate (THE Sep 19 2008, Dn = 0.76) produces Dn below the clean-core floor (0.94), demonstrating that Dn < 1 behavior is not unique to THD. However, no independent candidate reaches the cautious-only low-Dn region (Dn < 0.5), and the single independent recurrence is not less caveated than the existing cautious passes. The cautious-only character of all Dn < 0.5 evidence remains unchanged.

## Exact claim still not supportable

It remains not supportable to claim confounder-tested or independently recurrent evidence for Dn < 0.5 behavior under the current frozen measurement model and available THEMIS data.

## Whether a genuinely more independent search space was feasible

Marginally. Cross-probe (THE) and different-year (2010) axes were tested. THC remains untested but offers the same orbital geometry. THB offers different geometry but sparse plasma data. No fundamentally different search space is available without relaxing the frozen model.
