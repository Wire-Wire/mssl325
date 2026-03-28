# MMS Thickness Method Scaffold

**Date:** 2026-03-28
**Stage:** Methods-scaffold only. No event shortlist, no pilot results, no thickness values.
**Authority:** User-authorized red-level decision to open this branch.

---

## A. Branch scope and separation

### What this branch is for

Converting a small number of high-quality MMS near-magnetopause gradient intervals into defensible thickness estimates `L ± σ`, each with explicit start/end rationale, cross-checked normal estimates, both timing-based and gradient-scale thickness definitions reported, and an event quality grade.

The success criterion is not "many events." It is "a few events that can survive criticism" (blueprint §8).

### What this branch is not for

- Validating, upgrading, or back-filling the frozen THEMIS comparator bank
- Strengthening the cautious-only P1/P3 low-Dn evidence
- Reinterpreting THE Sep 19 external recurrence
- Defining PDL-positive or non-PDL classes
- Threshold calibration or detector construction
- SMILE/SXI prior generation (separate future scope)

### Explicit separation from the THEMIS branch

The THEMIS comparator + recurrence branch (Phase 4B frozen) and this MMS thickness branch are independent. MMS thickness results do not change THEMIS Dn/EB values, do not resolve THEMIS confounder caveats, and do not reclassify any THEMIS window. If a future integration layer connects them, that requires a separate red-level decision.

---

## B. Single scientific question and explicit non-goals

### Question

Under what operational conditions can an MMS near-magnetopause gradient interval support a defensible thickness estimate `L ± σ`?

### Non-goals for this scaffold round

- No event shortlist
- No pilot thickness values
- No `L` statistics
- No thickness-conditioned priors
- No physical class definitions
- No detector input from or output to the THEMIS branch

---

## C. Borrowed from literature vs must be defined here

| Method domain | Borrowed from literature | Must be defined in this project |
|---|---|---|
| **Timing analysis** | Cross-spacecraft timing logic, error estimation (Haaland et al. 2004; Zhou et al. 2009; Vogt et al. 2011) | Which start/end features count as the timed boundaries of a thickness-eligible interval |
| **Normals / LMN** | LMN coordinate estimation, MVA/MFR/cross-product methods, planarity diagnostics (Denton et al. 2018; Rezeau et al. 2018) | A preferred hierarchy of normal estimates for gradient layers (not sharp current sheets), with cross-check requirements |
| **Gradient methods** | Least-squares gradient calculation (De Keyser et al. 2007), volumetric tensor logic | How gradient-scale thickness is summarized into one event-level effective thickness |
| **Uncertainty** | Formal timing error, geometry sensitivity, method-comparison frameworks | How timing ambiguity, feature-picking variance, and normal-speed uncertainty combine into a final `L ± σ` |
| **Event grading** | General quality/geometry gates from boundary-crossing literature | The exact Gold/Silver/Bronze grading scheme for this project's thickness cases |

---

## D. Thickness-eligibility gate

An MMS interval is eligible for a thickness attempt only if ALL of the following are met:

### Required

1. **Near-subsolar dayside geometry.** Spacecraft must be sunward (X_GSM > 5 Re) with SZA preference < 30°. Flank/tail events are excluded.
2. **Upstream steadiness.** OMNI-propagated Dp and Bz must be relatively steady over the interval (no sustained reversal or >50% Dp change during the gradient crossing).
3. **Four-spacecraft data completeness.** All four MMS spacecraft must have usable FGM (magnetic field) and FPI (plasma moments) data spanning the gradient interval. Partial-coverage events are flagged, not automatically used.
4. **Tetrahedron quality.** The MMS tetrahedron must have adequate elongation/planarity for multi-point analysis. Severely degenerate configurations (Q_E or Q_P near limits) are excluded.
5. **Identifiable gradient interval.** At least one spacecraft must show a sustained density gradient and/or |B| gradient that spans a spatially resolvable near-MP region, not merely a single-point fluctuation.

### Fail conditions

- Any spacecraft has a major data gap during the gradient interval
- The tetrahedron is too elongated or too coplanar for volumetric gradient estimation
- No sustained gradient feature is identifiable on any spacecraft
- Upstream conditions are too disturbed for encounter-averaged boundary-model inputs to be meaningful
- The interval is on the nightside, deep flank, or high latitude

Four-spacecraft availability is necessary but not sufficient. Geometry, data quality, and identifiable gradient structure must all pass.

---

## E. Start/end feature menu and feature-pairing rules

### Operational start/end candidates

The following are recognized as operational candidates for start and end of a thickness-eligible interval. They are not physical class definitions.

| Feature | How identified | Typical location |
|---|---|---|
| Density gradient onset | Sustained decrease in ion density toward the magnetopause | Outer edge of near-MP gradient region |
| Density gradient end | Density reaches a local minimum or plateau near the boundary | Inner edge, near or at the magnetopause |
| |B| enhancement onset | Sustained increase in |B| toward the boundary | May precede or coincide with density gradient |
| |B| enhancement end | |B| reaches local maximum or plateau | Near or at the magnetopause |
| Beta transition | Sustained decrease in ion beta toward the boundary | Correlated with density/|B| changes |
| Magnetopause crossing | Sharp rotation or jump in B-field direction/magnitude | Defines the inner boundary of the sheath-side gradient |

### Feature-pairing rules

1. Start and end features must be identified on each spacecraft independently before cross-spacecraft timing is applied.
2. When multiple feature candidates exist on a single spacecraft, all plausible pairings must be noted. The preferred pairing is the one with the most consistent cross-spacecraft timing residuals.
3. When ambiguity exists, an explicit analyst note must record which pairing was chosen and why.
4. Feature-picking variance must be estimated by computing thickness under at least two plausible pairings if available.

---

## F. Normal-estimation hierarchy

### Preferred hierarchy

| Priority | Method | When preferred | Cross-check requirement |
|---|---|---|---|
| 1 | Multi-spacecraft timing normal | When timing residuals are small and consistent across all 4 spacecraft | Cross-check against MVA or MFR |
| 2 | Minimum variance analysis (MVA) on B-field | When single-spacecraft data is clean and eigenvalue ratios are adequate | Cross-check against timing or cross-product |
| 3 | Minimum Faraday residue (MFR) | When deHoffmann-Teller frame exists | Cross-check against MVA |
| 4 | Cross-product (constrained) | When B-field rotation is well-defined | Cross-check against timing |

### Cross-checking rules

- At least two independent normal estimates must agree within ~20° for the event to proceed to thickness computation.
- If the two best normals disagree by > 30°, the event is flagged and the normal-direction uncertainty is explicitly enlarged.
- If no two methods agree within 30°, the event receives a geometry penalty and may be downgraded to "do not report thickness."
- The normal used for thickness must be stated explicitly in the event record.

### Context checks

- The estimated normal should be broadly consistent with the expected magnetopause orientation at the spacecraft's GSM position.
- A normal pointing strongly away from the expected Sun-Earth line direction at near-subsolar geometry is a warning flag.

---

## G. Two fixed thickness definitions

### Definition A: Timing-based thickness

1. Identify the gradient start and end on each spacecraft.
2. Compute the time delay `Δt` for the start (or end) feature across the four spacecraft.
3. Estimate the normal direction `n̂` from the multi-spacecraft timing.
4. Estimate the normal speed `V_n` from `V_n = d / Δt` where `d` is the inter-spacecraft separation projected onto `n̂`.
5. Compute `L_timing = V_n × Δt_gradient` where `Δt_gradient` is the duration of the gradient interval on a reference spacecraft.

### Definition B: Gradient-scale thickness

1. Compute the spatial gradient `∇n` and/or `∇β` inside the gradient interval using the four-spacecraft least-squares gradient method (De Keyser et al. 2007).
2. Derive the local gradient scale length: `λ = n / |∇n|` (or equivalently for β).
3. Summarize the gradient scale length into an effective thickness `L_gradient` by integrating or averaging over the interval.

### Dual-definition requirement

Both definitions must be computed and reported for every thickness-eligible event. Disagreement between them is information, not something to suppress. The ratio `L_timing / L_gradient` is a consistency diagnostic.

---

## H. Uncertainty ledger and final `L ± σ`

### Required uncertainty components

| Component | Source | How estimated |
|---|---|---|
| Timing ambiguity (`σ_timing`) | Cross-correlation or feature-alignment uncertainty | Standard error of cross-spacecraft time delays |
| Feature-picking variance (`σ_feature`) | Ambiguity in start/end identification | Range of L over plausible feature pairings |
| Normal-direction uncertainty (`σ_normal`) | Spread among normal-estimation methods | Angular deviation between best two normals, propagated to L |
| Normal-speed uncertainty (`σ_Vn`) | Uncertainty in V_n from timing or deHoffmann-Teller | Formal error from timing fit or frame determination |
| Geometry/conditioning penalty | Tetrahedron quality, eigenvalue ratios | Multiplicative quality factor or additive penalty |
| Method disagreement | Timing vs gradient-scale thickness | `|L_timing - L_gradient|` reported as a diagnostic |

### Combination rule

The final reported uncertainty `σ_L` must combine at least the first four components. The combination may be root-sum-square if components are approximately independent, or a conservative envelope if correlations are suspected. The combination rule must be stated explicitly for each event.

### Output

Each event produces: `L_timing ± σ_timing`, `L_gradient ± σ_gradient`, and a combined best estimate `L ± σ_L` with the combination rule stated.

---

## I. Event quality grading

| Grade | Meaning | Conditions |
|---|---|---|
| **Gold** | High-confidence thickness estimate | All eligibility gates pass; normals agree within 20°; feature-picking variance small; both definitions consistent; tetrahedron quality good; upstream steady |
| **Silver** | Defensible thickness estimate with caveats | All eligibility gates pass; minor issues in one dimension (e.g. moderate normal disagreement 20–30°, or moderate feature ambiguity); both definitions reported |
| **Bronze** | Reported with major caveats | One or more serious concerns (large normal disagreement, poor tetrahedron, large feature-picking variance); thickness reported but flagged as unreliable |
| **Do not report** | Failed eligibility or failed quality gates | Missing data, degenerate tetrahedron, no identifiable gradient, normals disagree > 30° with no resolution, or upstream too disturbed |

---

## J. Minimum evidence package for each future event

Each MMS thickness event, if/when a pilot round is authorized, must produce:

1. **Multi-panel time-series figure:** B-field, density, beta, |B|, V for all 4 spacecraft, with start/end markers
2. **Normal-estimation comparison table:** all methods attempted, angular agreement, preferred normal stated
3. **Thickness computation summary:** L_timing, L_gradient, σ components, combined L ± σ
4. **Tetrahedron quality metrics:** Q_E, Q_P, inter-spacecraft separation
5. **Upstream context summary:** OMNI Dp, Bz, stability over the interval
6. **Quality grade** with explicit justification
7. **Analyst note:** feature-pairing rationale, ambiguity, and any concerns
8. **Caveat summary:** what this event-level estimate can and cannot support

---

## K. Compact event-registry schema

For future candidate tracking (no events registered yet):

```
mms_event:
  event_id: str                # unique identifier
  date: str                    # ISO date
  time_start: str              # gradient interval start
  time_end: str                # gradient interval end
  position_gsm_re: [x, y, z]  # mean position
  sza_deg: float
  upstream:
    dp_nPa: float
    bz_nT: float
    stability: str             # steady / variable / disturbed
  tetrahedron:
    separation_km: float       # mean inter-spacecraft distance
    quality_elongation: float
    quality_planarity: float
  thickness:
    L_timing_re: float | null
    sigma_timing_re: float | null
    L_gradient_re: float | null
    sigma_gradient_re: float | null
    L_combined_re: float | null
    sigma_combined_re: float | null
    combination_rule: str
  normals:
    method_used: str
    n_hat: [nx, ny, nz]
    angular_agreement_deg: float
    methods_compared: [str]
  grade: str                   # Gold / Silver / Bronze / do_not_report
  analyst_note: str
  caveats: [str]
```

No events are registered in this scaffold. This schema is a template for future use.

---

## L. Stop condition

### What a future MMS pilot could support at most

A small number (target: 3–5) of individually quality-graded thickness estimates with dual definitions, uncertainty budgets, and explicit analyst notes. These would anchor the spatial interpretation of the near-MP gradient for the mission-facing translation layer.

### What a future MMS pilot still could not support

- A universal thickness law or population-level thickness distribution
- Validation or upgrading of the frozen THEMIS cautious-only low-Dn branch
- Physical identification of any THEMIS comparator window as containing a specific structure
- Threshold or detector calibration
- Class-level definitions (PDL-positive, non-PDL, etc.)

### Explicit separation rule

MMS thickness results and THEMIS Dn/EB comparator results remain independent branches. Connecting them (e.g., thickness-conditioned priors, profile perturbation families) requires a separate future integration stage authorized by explicit user decision. This scaffold does not authorize that integration.
