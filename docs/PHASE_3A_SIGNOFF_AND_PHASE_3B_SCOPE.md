# Phase 3A Sign-Off and Phase 3B Scope

**Date:** 2026-03-27
**Status:** Decision-support memo for user review. Not final authorization.
**Authority:** The user remains the final approver.

---

## 1. What the current stage is

Phase 3A is a very bounded descriptive Dn/EB comparison package built on a 9-window / 7-pass THD-only comparator bank, under compressed-sheath conditions (encounter-averaged Dp > 3 nPa), using Shue 1998 + Merka 2005 empirical boundary models, with Sun–Earth-line encounter-averaged s-mapping.

The bank has been:
- constructed (Phase 2a)
- falsification-audited (Phase 2B)
- interval-audited for confounder structure (Phase 2C)
- reviewed for comparison readiness (Phase 2D)
- described across Dn/EB with pass-aware evidence weighting (Phase 3A)

The evidence hierarchy is:
- **Clean core** (P2, P4, P5, P6): 4 independent passes. Metrics survive leave-spike-out sensitivity. No pass has Dn < 0.5.
- **Cautious** (P1, P3): 2 independent passes. Extend Dn range to 0.12–0.39 but carry identified interval-level caveats (P1: near-bin density CV = 0.93; P3: EB partially spike-dependent, Δ = 0.50).
- **Excluded** (P7): 1 pass. Spike-dominated; metrics collapse after spike removal.

These categories are stage-local operational bookkeeping. They are not physical classes and do not imply scientific classification of any window.

---

## 2. What Phase 3A can be signed off as

Phase 3A can be signed off as:

**A descriptive, measurement-model-bounded, pass-aware Dn/EB comparison across 6 interpretable THD passes, under compressed-sheath conditions, with no thresholds, no labels, and no detector semantics.**

Specifically, Phase 3A establishes:

1. Dn and EB are the first-order descriptive comparison axes (median near-bin / median background-bin ratios for density and |B|).
2. Δβ, persistence, and ptot_smoothness are supporting context metrics only.
3. ρ(n,B) is non-discriminative within this bank (universally negative across all windows).
4. The clean core (P2, P4, P5, P6) spans Dn 0.94–2.31 and EB 0.80–1.96.
5. The low-Dn range (Dn < 0.5) depends entirely on cautious passes P1 and P3.
6. Duration variants within a pass are operationally consistent (within/between ratio < 0.28 for Dn, < 0.06 for EB).

---

## 3. What Phase 3A cannot be claimed to support

Phase 3A does not support:

1. **Thresholds or threshold candidates.** No Dn or EB boundary between categories is defined, proposed, or implied.
2. **Labels or physical classes.** No window is PDL-positive, non-PDL, a baseline, a control, or a development-set member.
3. **Detector semantics.** The metrics are outputs of the frozen measurement model, not diagnostic indicators of specific physical states.
4. **Generalization beyond THD / compressed sheath.** The bank is structurally biased toward Dp > 3 nPa on one probe in two seasons. It cannot represent the full dayside magnetosheath population. Lower-Dp sheath conditions—which may be more favorable for classical PDL-like pileup under weaker reconnection (Zwan & Wolf 1976; Anderson et al. 1997)—are structurally excluded.
5. **Resolved confounders.** transient_flag and mixing_flag remain UNKNOWN for all passes. Boundary motion is not resolvable under encounter-averaged s.
6. **Per-event upstream truth.** OMNI is a propagated L1-to-bow-shock-nose product, not a local upstream measurement (Vokhmyanin et al. 2019; Walsh et al. 2019). Shue 1998 and Merka 2005 are empirical fits with condition-dependent accuracy (Lin et al. 2024; Aghabozorgi et al. 2024). Encounter-averaged s does not resolve time-varying boundary positions within multi-hour windows.

---

## 4. What the evidence hierarchy is

| Category | Passes | Dn range | EB range | Basis |
|---|---|---|---|---|
| Clean core | P2, P4, P5, P6 | 0.94–2.31 | 0.80–1.96 | Metrics survive leave-spike-out; low-moderate density noise |
| Cautious | P1, P3 | 0.12–0.39 | 1.96–2.49 | P1: near-bin density CV=0.93; P3: EB Δ=0.50 after spike removal |
| Excluded | P7 | (not used) | (not used) | Spike-dominated; Dn 2.19→0.67, EB 4.22→0.97 after spike removal |

These are review-layer bookkeeping categories. They describe the current audit status of each pass under the interval-level confounder analysis performed in Phase 2C. They are not physical classifications.

---

## 5. What the single next bounded stage is

### Phase 3B — Measurement-model and confounder hardening on the existing six-pass bank

### Central question

Whether cautious low-Dn passes P1 and P3 can remain in the interpretable bank as cautious low-Dn comparators after explicit review of:

1. **Mapping sensitivity.** How much does ±1 nPa encounter-averaged Dp uncertainty shift s-bin assignments and Dn/EB for P1 and P3 specifically? Is P1's Dn = 0.12 defensible under boundary-model perturbation, or does it fall within the mapping-uncertainty envelope?

2. **Propagated-upstream limitations.** How much does OMNI propagation uncertainty (Vokhmyanin et al. 2019) affect the encounter-averaged Dp and Bz used for P1 and P3? Is the P1/P3 Dn < 0.5 pattern robust to plausible upstream-summary perturbation?

3. **Foreshock / jet alternatives.** Can the P1 near-bin density depression (CV = 0.93) be explained entirely by localized jet-like or foreshock-related Pdyn fluctuations (Archer & Horbury 2013; Raptis et al. 2020; Zhang et al. 2022), rather than reflecting a broad spatial structure? What does the P1 interval structure actually look like when Pdyn spikes are localized?

4. **Mixing risk.** Does P1 or P3 show any interval-level evidence consistent with magnetospheric mixing contamination in the near bin (Li et al. 2009)? Is the membership check (currently conservative) sufficient to exclude this?

5. **Boundary-motion risk.** Over the 6–8h P1 window, does the encounter-averaged s accurately represent the actual spatial position, or is boundary motion during the window large enough to scramble the near/background comparison?

### What Phase 3B is

A document-layer and review-layer hardening pass on the existing six-pass bank. It does not produce new data, new windows, new metrics, new code, or new evidence values. It produces:
- a per-pass (P1 and P3 focused) measurement-model sensitivity assessment
- a per-pass confounder-plausibility assessment using current data products and paper-library constraints
- a revised review-layer disposition for P1 and P3 (either confirmed-cautious, downgraded, or unchanged)
- an updated evidence hierarchy that reflects the outcome

### What Phase 3B is allowed to do

- Re-examine P1 and P3 interval structure using already-cached data products
- Compute bounded sensitivity tests (±Dp perturbation on s, leave-interval-out on Dn) as audit-only sidecar calculations
- Consult the paper library for confounder-plausibility constraints
- Update the review-layer disposition of P1 and P3 (upgrade, confirm, or downgrade their cautious status)
- Update the evidence hierarchy documentation
- Update WORKLOG_LATEST and RUN_REVIEW_PACKET

### What Phase 3B is forbidden to do

- Define, propose, or imply thresholds or threshold candidates
- Assign labels: PDL-positive, non-PDL, baseline, control, truth, dev-set member
- Introduce detector semantics
- Expand the bank (no new windows, probes, or seasons)
- Change the frozen measurement model (Shue98/Merka05, Sun–Earth-line s, encounter-averaged boundaries)
- Change stored metric values or evidence-layer facts
- Begin MMS thickness or SMILE/SXI prior work
- Introduce IMF-conditioned detection logic
- Recast comparator windows as physical classes
- Imply that human sign-off has already occurred

---

## 6. What remains after Phase 3B

Regardless of Phase 3B outcome, these remain deferred:
- Detector thresholds and labels
- Development/validation set membership
- Encounter-merge finalization
- Radial-IMF regime cut
- Selection-function audit at catalogue scale
- Time-varying s-mapping
- Cross-probe verification
- MMS thickness
- SMILE/SXI priors

---

## Decision requested

The user is asked to decide:

1. **Is Phase 3A signed off as a descriptive-only, measurement-model-bounded Dn/EB comparison package?**

2. **Is Phase 3B — measurement-model and confounder hardening on P1/P3 — approved as the next bounded stage?**

This memo supports that decision. It does not make it.
