# Comparator Bank and Independent Recurrence: Descriptive Results

---

## Scope of this results block

This block reports the descriptive outputs of a frozen encounter-level measurement model applied to real THEMIS dayside magnetosheath data. The measurement model uses Sun–Earth-line normalized magnetosheath coordinates (s = d_MP / (d_MP + d_BS)), with empirical boundary placements from the Shue et al. (1998) magnetopause model and the Merka et al. (2005) bow-shock model, driven by OMNI-propagated upstream conditions averaged over each encounter window. Two encounter-level ratios serve as the primary descriptive axes: a near-to-background density ratio (Dn) and a near-to-background magnetic-field-magnitude ratio (EB), computed from medians in fixed s-bins ([0.2, 0.4] for the near bin and [0.6, 1.0] for the background bin).

No thresholds, labels, physical identifications, or detector semantics are assigned to any encounter. All windows are measurement-model-valid near-MP comparator windows and nothing more.

---

## Frozen comparator bank

Six independent near-subsolar dayside THEMIS-D orbital passes from two seasons (2008 and 2009) constitute the interpretable comparator bank. All six passes were observed under compressed-sheath conditions (encounter-averaged dynamic pressure Dp = 3.0–4.2 nPa) at solar zenith angles of 4°–22°. Each pass required a 6–10 hour analysis window to populate both the near and background s-bins at the ~11.6 Re THD apogee under these Dp levels.

Of the seven passes originally considered, one (P7, 2009-10-24) was excluded after interval-level sensitivity analysis showed that its window-level metrics collapsed to near-unity values upon removal of Pdyn spike intervals (Dn shifted from 2.19 to 0.67; EB from 4.22 to 0.97). The remaining six passes were classified into two operational categories for evidence-bookkeeping purposes: four passes (P2, P4, P5, P6) form a confounder-tested clean core whose metrics are robust to leave-spike-out analysis (ΔDn ≤ 0.22, ΔEB ≤ 0.02), while two passes (P1, P3) were retained as confirmed-cautious comparators carrying documented interval-level caveats.

These categories are stage-local review bookkeeping. They are not physical classes.

### Frozen evidence ledger

| Pass | Date | Probe | SZA | Dp (nPa) | Bz (nT) | Near% | BG% | Memb% | Dn | EB | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P4 | 2009-09-20 | THD | 10° | 3.0 | +1.4 | 9% | 46% | 100% | 0.97 | 1.48 | clean core |
| P5 | 2009-09-26 | THD | 4° | 3.0 | +0.9 | 18% | 40% | 98% | 0.94 | 1.96 | clean core |
| P6 | 2009-09-27 | THD | 4° | 3.1 | −1.7 | 16% | 57% | 96% | 1.31 | 1.23 | clean core |
| P2 | 2008-09-03 | THD | 14° | 3.5 | +0.9 | 17% | 27% | 100% | 2.31 | 0.82 | clean core |
| P1 | 2008-08-18 | THD | 22° | 4.2 | +0.3 | 16% | 48% | 86% | 0.12 | 2.49 | cautious |
| P3 | 2009-09-13 | THD | 17° | 3.1 | −1.4 | 17% | 47% | 100% | 0.39 | 1.96 | cautious |
| — | 2008-09-19 | THE | 15° | 2.8 | −1.8 | 12% | 29% | 84% | 0.76 | 2.12 | external recurrence |

P7 (2009-10-24, THD) is excluded from this ledger; its metrics are spike-dominated and collapse upon interval sensitivity analysis (see traceability note).

Two additional windows (P1 8h variant, P2 8h variant) are duration variants of passes already represented. They produce operationally similar metrics (within-pass Dn spread of 0.50, between-pass range of 1.80) and are not counted as independent evidence.

---

## Clean-core Dn/EB span

The four clean-core passes span Dn from 0.94 (P5) to 2.31 (P2), and EB from 0.80 (P2) to 1.96 (P5). These ranges reflect operationally distinguishable measurement-model outputs across passes with different encounter-averaged upstream conditions: Dp ranges from 3.0 to 3.5 nPa, Bz from −1.7 to +1.4 nT, and Alfvén Mach number from 5.7 to 20.6. No clean-core pass produces Dn below 0.94.

Within the clean core, Dn and EB show an approximate inverse relationship: passes with higher Dn tend to have lower EB, and vice versa. This observed pattern is descriptive only and is not diagnostic of any specific physical state.

*[See Figure 1: reports/current_bank/figures/phase3a_dneb_comparison.png, left panel.]*

---

## Cautious low-Dn extension

Two confirmed-cautious passes extend the bank's Dn range below 0.5:

**P1 (2008-08-18, Dn = 0.12).** This pass has the lowest Dn in the bank and the highest EB (2.49). However, the near-bin density has a coefficient of variation of 0.93, indicating that the median density — from which Dn is computed — is drawn from a highly variable sample. The pattern qualitatively survives spike removal (Dn shifts from 0.12 to 0.17), but whether the low near-bin density reflects an ordered spatial structure or high magnetosheath variability (including possible mirror-mode or compressive-wave contributions; cf. Soucek et al. 2015) cannot be determined under the encounter-averaged measurement model. Membership is 86%, the lowest in the bank, with 14% of data points classified as unknown/NaN.

**P3 (2009-09-13, Dn = 0.39).** This pass shows Dn robust to spike removal (0.39 → 0.41) but carries a partially spike-dependent EB (1.96 → 1.46 after background-bin spike removal, Δ = 0.50). Mapping sensitivity is the largest in the bank: a ±1 nPa perturbation to encounter-averaged Dp shifts the mean-position s by ±0.23, enough to substantially redistribute near- and background-bin populations. The low Dp (3.1 nPa) places this pass near the lower edge of the compressed-sheath window that permits dual-bin coverage at THD's apogee.

All Dn < 0.5 evidence in this bank is cautious-only.

---

## Independent external recurrence outside the main bank

A systematic search across THEMIS-D (2008–2010) and THEMIS-E (2008) identified one independent candidate producing Dn below the clean-core floor: THE on 2008-09-19 (Dn = 0.76, EB = 2.12). This is the sole cross-probe evidence under the frozen measurement model that sub-unity Dn behavior recurs on an instrument chain independent of THD.

However, this candidate does not enter the cautious-only low-Dn region (Dn < 0.5), is not less caveated than the existing cautious passes (membership = 84%, encounter-averaged Dp = 2.8 nPa below the bank's practical preference, Alfvén Mach number = 21.1), and is preserved as an external recurrence record only — it is not admitted to the main six-pass bank.

No independent candidate reproduces Dn < 0.5 under the frozen model. This does not imply that such behavior is physically absent; it may reflect the selection-function constraints of the current apparatus, including the practical requirement for compressed-sheath conditions at the ~11.6 Re inner-probe apogee.

*[See Figure 2: reports/current_bank/figures/phase4a_lowdn_recurrence.png.]*

---

## Exact supportable statements

1. The frozen measurement model produces operationally distinguishable Dn and EB outputs across six independent dayside near-subsolar THD passes under compressed-sheath conditions.

2. The clean core (four passes) spans Dn 0.94–2.31 and EB 0.80–1.96, with metrics robust to leave-spike-out sensitivity analysis.

3. Two confirmed-cautious passes extend Dn below 0.5 (Dn = 0.12 and 0.39), but both carry interval-level caveats that cannot be resolved under the encounter-averaged measurement model.

4. One cross-probe candidate (THEMIS-E, 2008-09-19, Dn = 0.76) demonstrates that sub-unity Dn behavior recurs independently of THEMIS-D, though under comparable caveats and without entering the cautious-only low-Dn region.

5. No thresholds, labels, physical identifications, or detector semantics are defined or implied by these results.

---

## Limitations carried forward

1. **Single primary probe and compressed-sheath bias.** The bank comprises THD passes under encounter-averaged Dp > 3 nPa. Lower-Dp conditions — which may be more relevant for classical magnetic pileup under reduced reconnection rates (Zwan & Wolf 1976; Wang et al. 2004) — are structurally excluded because the ~11.6 Re inner-probe apogee cannot reach the background s-bin without boundary compression.

2. **Encounter-averaged boundary placement.** The s-mapping uses one set of boundary standoff distances per encounter, derived from median OMNI-propagated Dp and Bz. Condition-dependent magnetopause model errors (Lin et al. 2024; Aghabozorgi et al. 2024) and OMNI propagation uncertainty (Vokhmyanin et al. 2019; Walsh et al. 2019) are not resolved per-event. A ±1 nPa Dp perturbation shifts boundaries by approximately 1 Re, which is a substantial fraction of the ~3 Re compressed-sheath width.

3. **Unresolved confounder channels.** Transient contamination, magnetospheric mixing, and sub-window boundary motion remain structurally unresolved under the current data products and measurement model. The jet-like Pdyn spike flag triggers universally under 6–10 hour windows and provides no discriminative information.

4. **Effective sample size.** The effective independent N is six passes for the interpretable bank, reduced to four for the clean core. Duration variants within a pass are not independent evidence.

5. **Regime-specific, not population-representative.** The dayside magnetosheath spatial profile is sensitive to IMF orientation and upstream pressure (Pi et al. 2024; Michotte de Welle et al. 2024). The current bank samples only compressed-sheath conditions under both northward and southward Bz, which restricts any physical interpretation to this specific regime.

---

## Traceability / provenance note

The results reported here were produced through a sequence of bounded stages: bank construction and validation (Phase 2a–2D), descriptive Dn/EB comparison (Phase 3A), cautious-pass retention audit (Phase 3B), independent recurrence test (Phase 4A), and results freeze (Phase 4B). Each stage was user-authorized with explicit scope boundaries. The full audit trail is preserved in the repository under `docs/PHASE_*.md` and `reports/current_bank/`. Machine-readable evidence artifacts are available under `runs/20260326T040343Z_d0425fd4/evidence/`.

P7 (2009-10-24, THD) was excluded after Phase 2C interval analysis showed that 35% of its data consisted of Pdyn spike intervals concentrated in the background bin, and removal of these intervals shifted Dn from 2.19 to 0.67 and EB from 4.22 to 0.97, indicating that the window-level metrics were predominantly spike-driven.

The THEMIS-E external recurrence (2008-09-19) was identified by a bounded search across THD 2008–2010 and THE 2008 dayside seasons (Phase 4A) and is preserved as an external record, not admitted to the main bank.
