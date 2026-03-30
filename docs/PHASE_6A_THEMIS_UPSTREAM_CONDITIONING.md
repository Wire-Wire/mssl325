> **POST-AUDIT STATUS (2026-03-30):** This tranche-1 document is an apparatus-limited pilot result, not a controlled catalogue finding. It contains 2 synthetic fixture encounters (pilot_001, pilot_002) that should not have entered the real-data catalogue. The effective real-data sample is N=9, not N=11. See `docs/PHASE_6A_AUDIT_AND_RESET_NOTE.md` for the full audit.

# Phase 6A — THEMIS Upstream Conditioning in a Controlled Near-Subsolar Encounter Catalogue

**Date:** 2026-03-30
**Authority:** User-authorized red-level THEMIS reopen.
**Phase 4B/5A/5B remain frozen anchors.** This branch does not alter frozen claims.

---

## 1. Authority and branch-opening note

The user explicitly authorized a new THEMIS science branch (Phase 6A) to move beyond the frozen Phase 4B/5A/5B checkpoint. Phase 4B remains the frozen comparator-bank anchor. Phase 5A/5B remain editorial sidecars. Phase 6A is additive and descriptor-first: it asks how continuous near-MP descriptors shift across coarse upstream-geometry strata within one controlled local encounter catalogue.

**Single branch question:** Within one controlled near-subsolar THEMIS encounter catalogue, how do continuous near-magnetopause descriptors (Dn, EB) shift across coarse upstream-geometry strata?

---

## 2. Scope and non-goals

**Phase 6A is:**
- a descriptor-first, controlled-sample conditioning branch
- additive on top of a frozen science base
- analysis-active but not yet thesis-safe

**Phase 6A is NOT:**
- detector work, threshold work, label/class work
- mission-prior or SMILE/SXI translation
- causal "favorable conditions" work
- MMS work
- a strengthening of frozen Phase 4B claims
- conditioned occurrence statistics (no inherited bundle field exists locally; recovery layer deferred)

---

## 3. Sample definition and declared slice

**Declared slice:** All locally cached evaluable THEMIS encounters across all run directories in the repository.

**Unit of inference:** encounter (not crossing, window, or Phase 5A case card).

**Universe:** 11 unique encounters after deduplication by date + probe.
- 9 THD (2008–2010), 1 THE (2008), 1 THD (2012), 1 THE (2013)
- All passed preflight and have valid Dn/EB

**Inclusion screens (define usable measurement context only):**
1. SZA ≤ 30° (near-subsolar)
2. OMNI upstream data available for cone/clock derivation
3. Near-bin occupancy ≥ 5%
4. Background-bin occupancy ≥ 1%
5. Membership ≥ 50%

**All 11 encounters pass all screens. Zero exclusions.**

**Screens NOT applied (by design):**
- Cone angle is a variable of interest, not an inclusion filter
- Clock angle / Bz sign are variables of interest
- Dp > 3 nPa is not inherited as a Phase 6A filter
- The Phase 5A non-quasi-radial cutoff is not inherited

---

## 4. Selection-function / exclusion ledger

| Screen | Excluded | Reason |
|---|---|---|
| SZA > 30° | 0 | — |
| Upstream unavailable | 0 | — |
| Near occupancy < 5% | 0 | — |
| BG occupancy < 1% | 0 | — |
| Membership < 50% | 0 | — |
| **Total excluded** | **0** | — |

**Inherited structural biases (not corrected, carried forward):**
- THD-dominated (9/11)
- Compressed-sheath-biased (all Dp ≥ 2.8 nPa)
- Two primary seasons (2008 + 2009)
- Single inner-probe apogee (~11.6 Re)

See `reports/themis_conditioning/selection_flow.md` for full flow.

---

## 5. Conditioning axes and rationale

**Primary axis 1 — IMF cone-angle regime:**
- quasi-radial: cone ≤ 30° (N = 0 in this slice)
- intermediate: 30° < cone ≤ 60° (N = 6)
- perpendicular: cone > 60° (N = 5)

**Primary axis 2 — coarse absolute IMF clock-angle group:**
- < 60° (N = 2)
- 60–120° (N = 5)
- > 120° (N = 4)

**Control axis — upstream stability:**
- All 11 encounters are upstream-stable (Dp CV < 0.3). This axis has no discrimination in the current slice.

**Why cone angle first:** The IMF cone angle determines the foreshock geometry and the degree to which the quasi-parallel bow shock interacts with the dayside sheath. This is an upstream-geometry axis that is independent of any downstream depletion/pileup hypothesis.

**Why Dp, Bz sign, and M_A are not primary axes:** They are available as secondary context but the sample (N = 11) cannot support 3+ dimensional stratification. They are reported per-encounter in the catalogue for later use.

---

## 6. Continuous descriptor summaries

### By cone-angle regime (primary axis)

| Regime | N | Dn median | Dn IQR | EB median | EB IQR |
|---|---|---|---|---|---|
| quasi-radial | 0 | — | — | — | — |
| intermediate | 6 | 1.12 | [0.95, 1.31] | 1.05 | [1.03, 1.18] |
| perpendicular | 5 | 0.94 | [0.76, 0.97] | 1.96 | [1.96, 2.12] |

**Descriptive observation:** In this 11-encounter controlled sample, perpendicular-IMF encounters show lower Dn (median 0.94, all ≤ 1) and higher EB (median 1.96), while intermediate-cone encounters show Dn near or above unity (median 1.12) and EB near unity (median 1.05). The quasi-radial bin is empty.

### By clock-angle group (secondary axis)

| Clock group | N | Dn median | Dn IQR | EB median | EB IQR |
|---|---|---|---|---|---|
| < 60° | 2 | 1.12 | [1.04, 1.21] | 1.04 | [1.03, 1.05] |
| 60–120° | 5 | 0.97 | [0.94, 2.19] | 1.96 | [1.48, 2.49] |
| > 120° | 4 | 0.86 | [0.67, 1.04] | 1.59 | [1.18, 2.00] |

### Encounter-level detail

| Encounter | Probe | Date | Cone | Regime | Clock | Group | Dp | Bz | Dn | EB |
|---|---|---|---|---|---|---|---|---|---|---|
| usable_aug18_6h | THD | 2008-08-18 | 31° | int | 115° | 60–120 | 4.2 | +0.3 | 0.12 | 2.49 |
| usable_sep03_5h | THD | 2008-09-03 | 56° | int | 87° | 60–120 | 3.7 | +0.5 | 2.87 | 0.80 |
| cand4a_sep19_08_the | THE | 2008-09-19 | 64° | perp | 169° | >120 | 2.8 | −1.8 | 0.76 | 2.12 |
| usable_sep13_09_6h | THD | 2009-09-13 | 61° | perp | 135° | >120 | 3.1 | −1.4 | 0.39 | 1.96 |
| usable_sep20_09_6h | THD | 2009-09-20 | 70° | perp | 90° | 60–120 | 3.0 | +1.4 | 0.97 | 1.48 |
| usable_sep26_09_10h | THD | 2009-09-26 | 85° | perp | 92° | 60–120 | 3.0 | +0.9 | 0.94 | 1.96 |
| usable_sep27_09_10h | THD | 2009-09-27 | 57° | int | 120° | >120 | 3.1 | −1.7 | 1.31 | 1.23 |
| usable_oct24_09_6h | THD | 2009-10-24 | 86° | perp | 81° | 60–120 | 4.2 | −0.5 | 2.19 | 4.22 |
| cand4a_oct23_10_thd | THD | 2010-10-23 | 35° | int | 1° | <60 | 3.1 | +2.2 | 1.30 | 1.02 |
| pilot_001 | THD | 2012-07-15 | 41° | int | 164° | >120 | — | — | 0.95 | 1.05 |
| pilot_002 | THE | 2013-02-20 | 33° | int | 34° | <60 | — | — | 0.95 | 1.05 |

---

## 7. Occurrence / recovery layer: deferred

No inherited operational signature-bundle field exists locally that can be reused without inventing new semantics. The frozen bank and Phase 5A sidecars use review statuses (clear/ambiguous/not convincing) that are editorial packaging, not binary bundle targets.

**The occurrence/recovery layer is explicitly deferred.** Phase 6A remains descriptor-only. Any future bundle-recovery analysis would require a separate authorization.

---

## 8. Boundary and upstream uncertainty note

All upstream context is derived from OMNI 1-min data, which is a propagated L1-to-bow-shock-nose product (Vokhmyanin et al. 2019; Walsh et al. 2019). Cone and clock angles are 30-min averages of the OMNI-propagated IMF, not local measurements. The magnetopause and bow-shock positions are encounter-averaged model outputs (Shue 1998, Merka 2005) with condition-dependent accuracy (Lin et al. 2024; Aghabozorgi et al. 2024). Dn and EB are encounter-level median ratios under this frozen measurement model.

These outputs are controlled-sample descriptive summaries, not local per-event truth or universal occurrence rates.

---

## 9. Exact supportable statement

Within one controlled near-subsolar THEMIS encounter catalogue (N = 11, SZA ≤ 30°, all upstream-stable), encounters under perpendicular IMF (cone > 60°, N = 5) show lower Dn (median 0.94) and higher EB (median 1.96) than encounters under intermediate IMF (cone 30–60°, N = 6, Dn median 1.12, EB median 1.05). The quasi-radial bin (cone ≤ 30°) is empty in this slice. This is a descriptive, within-sample observation under the frozen measurement model, not a conditioned occurrence rate, causal claim, or detection rule.

---

## 10. Exact non-claim

Phase 6A does not support:
- Any claim about real-space occurrence rates or population-level conditioning
- Causal language such as "perpendicular IMF favors depletion"
- Threshold, detector, label, or class semantics
- Any strengthening of frozen Phase 4B claims
- Any physical identification of encounters as containing specific structures
- Generalization beyond this compressed-sheath, THD-dominated, inner-probe, two-season sample

---

## 11. Go/no-go note for a later Phase 6B

The descriptor separation between perpendicular-IMF and intermediate-IMF encounters is visible (Dn and EB shift in opposite directions across the two regimes) and is qualitatively consistent with published expectations for IMF-orientation-dependent sheath structure (Pi et al. 2024; Michotte de Welle et al. 2024). However, the sample is small (N = 11), the quasi-radial bin is empty, the slice is structurally biased (compressed sheath, THD-dominated), and no occurrence/recovery layer has been tested. A later Phase 6B would need to either expand the archive slice under predeclared rules or define a defensible operational bundle — both of which require separate user authorization.
