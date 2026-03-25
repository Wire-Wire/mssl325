# Internal PDL Blueprint

## Internal Master Research Blueprint

### Revisiting the Dayside Plasma Depletion Layer with THEMIS and MMS

**Occurrence, Thickness, and SMILE/SXI-Relevant Density Priors**

---

## Document status

**Internal execution document, not an outward-facing proposal.**

**Purpose:** to fix the current research spine, method architecture, literature strategy, and near-term execution order.

**Basis:** synthesized from the two internal RP drafts, the acquisition workbook, and the current uploaded paper pool.

**Bibliographic control** remains in the acquisition workbook; this document functions as the project’s execution console.

**Prepared for internal use • 25 March 2026**

---

## Contents at a glance

| Section | What this part fixes |
|---|---|
| 1. Project identity at the freeze point | What the project is really doing, what it is not doing, and what burden of proof it carries. |
| 2. Core argument chain and likely objections | The logic that has to survive criticism, and the specific objections the design is built to answer. |
| 3. Main question, subquestions, deliverables | The research question stack and the outputs that will count as success. |
| 4. Physics, measurement, engineering, translation | Separates the project into its four real problem classes so they are not blurred together. |
| 5. Measurement model | Fixes the role of mapping, boundary placement, OMNI representativeness, sheath membership, and near-bin design. |
| 6. THEMIS catalogue and detector MVP | Defines the encounter as the statistical unit, the detector minimum, and the QC/confounder logic. |
| 7. Validation and audit | Distinguishes validation, falsification, robustness, provenance, and selection-function audit. |
| 8. MMS thickness branch | Protects the thickness work from scope creep and defines what can and cannot be borrowed. |
| 9. SMILE/SXI translation | Specifies what mission-facing outputs must look like so the project ends with usable priors. |
| 10. Literature architecture and execution strategy | Locks the role of the current literature pool and the first-pass conversion sequence. |
| 11. Work plan for the next 4–8 weeks | Turns the blueprint into a practical short-horizon execution plan. |
| 12. Thesis growth map and decision status | Shows how methods/results/discussion grow from this blueprint and what is frozen vs open. |
| Final three control lists | Tomorrow’s actions, the freeze list, and the decisions that must wait for first-pass extraction or pilot tests. |

---

# 1. Project identity at the current freeze point

This project is no longer in the stage of trying to decide whether the topic is interesting. The topic is already strong enough. The real task now is to turn a physically plausible but observationally slippery dayside magnetosheath structure into something that is operationally credible, statistically defensible, spatially interpretable, and mission-usable.

The project is not mainly trying to “say something about the PDL” in a loose phenomenological sense. Classical theory and later observational/MHD work already support the basic physical picture: magnetic flux piles up against the dayside magnetopause when reconnection is comparatively weak, magnetic pressure rises, density falls, plasma beta falls, and a boundary-adjacent layer can form (Zwan & Wolf, 1976; Crooker et al., 1979; Anderson et al., 1997; Wang et al., 2004). The real problem is that in modern large databases the same state-space signature can be faked by spatial mixing, mapping uncertainty, jets, wave trains, foreshock-related variability, and boundary motion.

The project is therefore best understood as a four-part research program. It asks whether a boundary-adjacent, layer-like PDL can be detected in a controlled THEMIS dayside sample without circular IMF assumptions; whether that signal survives measurement-model and confounder criticism; whether a small number of MMS cases can convert the statistical signature into a physical thickness with uncertainty; and whether the resulting occurrence and depletion statistics can be translated into compact, conditional priors for SMILE/SXI forward modeling.

The central internal judgment is this: the research spine is already frozen enough to execute. What remains open is not the project’s identity but its operationalization—especially threshold tuning, encounter bookkeeping, uncertainty propagation, and the exact form of the mission-facing priors.

## What the project is, and what it is not

### It is:

- A controlled study of whether a dayside boundary-adjacent depletion layer can be isolated as a real magnetosheath structure after explicit coordinate control, confounder handling, and selection-function audit.
- A measurement-conscious THEMIS catalogue project in which the primary statistical unit is the encounter, not the raw crossing.
- A conservative detector-building project that keeps upstream IMF/solar-wind variables outside the detector and uses them only after detection for conditioning and explanation.
- A low-N but high-value MMS calibration branch that turns a signature into a spatial scale, with uncertainty and quality grading.
- A mission-translation project whose end product is not a story about the PDL, but a small family of conditional priors and sensitivity outputs relevant to SMILE/SXI.

### It is not:

- It is not a general review of all magnetosheath depletion phenomena.
- It is not a full global magnetosheath reconstruction or a new global model.
- It is not a reconnection-rate study, even though reconnection context matters physically.
- It is not a machine-learning classification project unless ML later appears as an optional enhancement.
- It is not a full SXI inversion or retrieval framework; the imaging component should remain a forward-sensitivity and prior-delivery layer.

## Working verdict

The spine is sufficiently fixed to execute. Default behavior from this point onward should be to operationalize, not to reopen the topic question or keep expanding the literature pool by default.

---

# 2. Core argument chain and the burden of proof

The project should be defended as a chain, not as a menu of loosely connected tasks. The physical premise is that magnetic pileup near the dayside magnetopause can generate a density-depleted, |B|-enhanced, low-beta layer adjacent to the boundary under suitable IMF geometry. The observational problem is that the same pattern is easy to imitate when measurements from different relative positions are mixed together, when boundary models are treated as exact truth, or when jets, wave packets, or mixing episodes are allowed to masquerade as quasi-static layers.

The methodological response is to build a controlled THEMIS encounter catalogue, map each measurement into normalized magnetosheath space, apply an IMF-agnostic event-level detector based on local signatures only, and keep confounder flags and selection-function documentation inside the core design rather than as afterthoughts. The validation bridge is then the MMS thickness branch, which does not carry the whole thesis but prevents the result from collapsing into pure statistical signature hunting. The translation payoff is a compact set of near-magnetopause density and occurrence priors that can perturb a baseline sheath model for SMILE/SXI-relevant forward modeling.

If any one of those links fails, the overall project weakens sharply. A detector without a measurement model can be dismissed as a coordinate artifact. A detector without QC can be dismissed as a confounder classifier in disguise. A statistical signal without even a small thickness branch can look like signature chasing. A physically interesting result without a compact output format will not truly become mission-facing.

## Main claims and the proof each claim requires

| Claim | What must be shown | Most likely criticism | Primary design response |
|---|---|---|---|
| A real boundary-adjacent PDL-like layer exists in the controlled THEMIS sample. | Near-MP depletion, \|B\| enhancement, beta reduction, trend-scale n–\|B\| anti-correlation, and persistence survive event-level analysis. | This is just mixed sheath sampling or local fluctuation structure. | Normalized s-mapping, encounter-based sampling, trend-vs-fluctuation decomposition, persistence logic. |
| The inferred signal is not mainly a mapping or boundary-placement artifact. | The near-MP signal remains under alternative boundary models and conservative s-bin choices. | Your PDL is just model error near the magnetopause. | Explicit measurement model, dual near bins, multi-model sensitivity, uncertainty envelopes, conservative use of OMNI. |
| The positive class is not dominated by confounders. | Jet-, wave-, transient-, motion-, and mixing-dominated intervals are explicitly flagged and separated from clean layer-like cases. | You have re-labeled other magnetosheath phenomena as PDL. | QC taxonomy, ambiguous class during tuning, Gold/Silver/Bronze rating, visual QC for the development set. |
| The THEMIS result can be given a spatial anchor. | At least a few MMS cases yield defensible layer thicknesses with quality grades and uncertainty ranges. | Thickness is feature-picking dressed up as multi-spacecraft analysis. | Two operational thickness definitions, timing and gradient-scale cross-checks, explicit geometry/planarity grading. |
| The result is mission-usable rather than merely descriptive. | Occurrence and depletion outputs are expressed as compact conditional priors with applicability limits and a simple sensitivity demonstration. | The SMILE link is too loose and remains interpretive rhetoric. | Define the prior format in advance and treat imaging papers as translation targets, not as detector evidence. |

## The reviewer objections most worth anticipating

- “Near-boundary depletion is a mapping artifact.” This is answered only if the measurement model is explicit and sensitivity-tested.
- “Your positive cases are really jets, mirror-mode packets, foreshock transients, or mixing intervals.” This is answered only if QC is structural rather than decorative.
- “Occurrence trends are just a by-product of your geometry and stability filters.” This is answered only by a visible selection-function audit.
- “MMS thickness is too uncertain to trust.” This is answered by quality-graded, uncertainty-first operationalization rather than by chasing sample size.
- “The mission relevance is overstated.” This is answered only if the output is a compact prior or perturbation family, not a discussion paragraph.

---

# 3. Main question, subquestions, and final deliverables

## Main question

How large, how common, and under what upstream conditions is the near-subsolar dayside plasma depletion layer in Earth’s magnetosheath, once spatial mixing, mapping uncertainty, OMNI representativeness limits, and major magnetosheath confounders are treated as first-order design problems rather than background caveats?

## Subquestions

- Can a boundary-adjacent, layer-like depletion signature be recovered in THEMIS without encoding IMF geometry into the detector itself?
- Does the signal scale mainly with IMF cone angle and clock angle, with secondary dependence on dynamic pressure and Alfvén Mach number, rather than being reducible to a simple northward/southward split?
- How much of the apparent near-magnetopause signal survives boundary-model uncertainty, s-bin choice, encounter merging, and conservative OMNI handling?
- Can a small number of MMS events provide defensible PDL thickness estimates in Earth radii despite the fact that the PDL is a gradient layer rather than a single discontinuity?
- What is the minimal mission-facing output form that SMILE/SXI can actually use: occurrence priors, depletion-factor priors, profile perturbations, or thickness-conditioned priors?

## Final deliverables

- A controlled THEMIS encounter catalogue with encounter-level metadata, normalized s-mapping, upstream context summaries, and explicit selection-function documentation.
- A conservative PDL detector and QC taxonomy that outputs core metrics, confounder flags, and Gold/Silver/Bronze credibility grades for each encounter.
- Occurrence and depletion statistics as functions of IMF geometry and secondary drivers, with uncertainty and sensitivity results attached.
- A small, quality-graded MMS thickness set (target: at least three defensible cases) with two operational thickness definitions and uncertainty propagation.
- A compact SMILE/SXI-facing prior package plus a forward-model sensitivity demonstration using a smooth baseline sheath profile and a PDL-perturbed alternative.

## Minimum acceptable success criteria

| Output | Minimum acceptable result | Why this is enough |
|---|---|---|
| THEMIS catalogue | A clean, well-documented encounter catalogue with selection-function audit and reproducible metadata. | Without this, all later statistics are vulnerable to silent sample-definition drift. |
| Detector | A detector v1 that clearly separates high-confidence, ambiguous, and negative cases, even if it is conservative. | A conservative detector is preferable to an overfitted, high-recall detector at MSc scope. |
| Statistics | Stable occurrence and depletion outputs under a bounded robustness grid. | The project succeeds by being defensible, not by maximizing complexity. |
| MMS branch | At least three high-quality thickness estimates with uncertainty and quality grades. | A few strong cases anchor the spatial interpretation more credibly than many weak ones. |
| Mission translation | A compact prior package and a simple sensitivity note showing why near-MP depletion matters for model outputs. | This is sufficient to establish mission-facing value without drifting into full retrieval or inversion scope. |

---

# 4. The project’s four real problem classes: physics, measurement, engineering, translation

One of the most important internal clarifications is that the project is not one homogeneous scientific question. It contains four distinct problem classes, and confusion arises when they are treated as if they were interchangeable. A physically correct intuition does not solve the measurement problem; a measurement-conscious detector does not automatically produce a mission-facing output; and a reproducible pipeline does not by itself establish physical meaning.

Keeping the four layers separate is not bureaucratic. It is what prevents the thesis from smearing together explanation, evidence, implementation, and application.

| Layer | What belongs here | Main risk if mishandled | What the output should look like |
|---|---|---|---|
| Physics problem | Magnetic pileup, flow diversion, reduced beta, draping, reconnection context, and how PDL signatures are expected to behave under different IMF geometry. | The project collapses into generic phenomenology or vague physical storytelling. | Clear physical semantics for what should count as a PDL-like layer, plus condition-dependent expectations. |
| Measurement problem | Mapping into normalized magnetosheath space, boundary placement, OMNI representativeness, sheath membership, near-bin design, encounter construction, and contamination control. | The positive class can be dismissed as a coordinate artifact or sample-definition artifact. | An explicit measurement model with uncertainty, not a hidden assumption stack. |
| Engineering and audit problem | Detector implementation, QC report generation, configuration tracking, bounded robustness grid, encounter-level resampling, and provenance. | Results become irreproducible or depend on hidden researcher choices. | A configuration-driven pipeline whose outputs can be regenerated and audited. |
| SMILE/SXI translation problem | Compact prior formats, applicability limits, baseline-vs-perturbed sheath comparison, and sensitivity of imaging outputs to near-MP depletion. | Mission relevance stays rhetorical and never becomes a usable product. | Parameterised priors and a short sensitivity note, not a broad application narrative. |

## Practical implication

When you are stuck, ask which layer of the project you are actually working on. A physical question should not be answered by a reproducibility paper, a detector question should not be answered by a large-sample interpretation map, and a mission-facing claim should not be justified by detector literature alone.

---

# 5. The measurement model is not support material; it is one of the project’s cores

The most important methodological decision already present in the project is that the measurement model is treated as a first-class module. That is correct and should be preserved. The detector’s variables—depletion, magnetic enhancement, beta reduction, anti-correlation, persistence—only have physical meaning if the spatial interpretation of the measurements is defensible. If the effective distance from the magnetopause is unknown, then the detector is not evaluating a layer; it is evaluating where the spacecraft may or may not have been relative to a modeled boundary.

This is why mapping, boundary placement, OMNI representativeness, sheath membership, and bin design are not background caveats. They are part of what makes the signal real or not real. In this project, the measurement model is the bridge between in-situ time series and a physically interpretable near-boundary spatial statement.

## 5.1 Core measurement-model components

| Component | Current default stance | Why it matters | Status now |
|---|---|---|---|
| Magnetopause placement | Use Shue et al. (1998) as the baseline MP surface and treat model error as condition-dependent rather than negligible. | Near-MP depletion can otherwise be dismissed as boundary-placement error. | Frozen as baseline; uncertainty handling still to be finalized. |
| Bow-shock placement | Use one empirical BS model as baseline and keep at least one alternative for sensitivity. | The normalized sheath coordinate depends on both boundaries, not the MP alone. | Frozen at the design level; final sensitivity pair remains open. |
| Normalized coordinate s | Use `s = d_MP / (d_MP + d_BS)` as the backbone spatial variable. | This is what prevents fixed time windows from mixing very different sheath locations. | Frozen. |
| Distance definition | Default to along the Sun–Earth line, with a local-normal alternative tested on a subset. | Different distance definitions may matter most near the MP and under nontrivial geometry. | Provisional; pilot comparison required. |
| OMNI representativeness | Use OMNI as context and averaged driver windows, not as exact local forcing truth. | L1-to-dayside propagation and IMF inhomogeneity can blur associations. | Frozen conceptually; exact window metrics still open. |
| Sheath membership | Keep explicit checks for likely magnetospheric or upstream contamination before metric calculation. | A near-MP point outside the sheath is not a valid PDL datum. | Frozen conceptually; exact filters remain provisional. |
| Near-bin design | Retain two near bins: very-near `[0.0,0.2]` and near `[0.2,0.4]`, with the latter treated as the primary robust bin. | The most dramatic boundary-adjacent signal is also the most fragile to boundary error and motion. | Frozen. |
| Boundary contamination control | Drop or flag points whose sheath status is ambiguous and report removal rates. | Without this, the strongest apparent signal may be produced by contamination, not depletion. | Frozen conceptually; exact numerical gate remains open. |

## 5.2 Normalized magnetosheath mapping

The normalized coordinate should remain the project’s spatial backbone:

```text
s = d_MP / (d_MP + d_BS)
```

where `d_MP` and `d_BS` are distances from the spacecraft position to the modeled magnetopause and bow shock along a chosen direction. The point of this mapping is not elegance. It is that relative position is the correct variable for comparing near-boundary versus background sheath measurements across different events and trajectories. Recent large-database work has made that point clearly enough that the project should treat s-mapping as a structural requirement, not an optional refinement.

The most important operational stance here is not “choose the perfect model.” It is “do not pretend the chosen model is the truth.” The correct design is a baseline geometry plus condition-aware caveats plus sensitivity tests, not a false certainty surface.

## 5.3 Why the dual near-bin design should stay

The two near bins are not unnecessary complexity. They formalize a mature trade-off between physics sensitivity and measurement defensibility. The very-near bin `[0.0, 0.2]` is where a boundary-adjacent depletion layer should be strongest if it is real, but that same bin is also where boundary motion, placement error, and contamination are most dangerous. The near bin `[0.2, 0.4]` is less dramatic but more statistically trustworthy.

Treating `[0.2, 0.4]` as the primary science bin and `[0.0, 0.2]` as the physics-rich but fragile sensitivity bin is exactly the right design stance for a defensible MSc-scale project. It also gives the thesis an honest language for separating “largest apparent signal” from “most robust signal.”

## 5.4 OMNI and upstream context

OMNI should be treated as necessary but not exact. The project is correct to use OMNI for pre-encounter stability filters, upstream condition tags, and post-detection statistical conditioning. It should not use OMNI as if it perfectly specifies the actual solar wind and IMF structure seen by the subsolar interaction region at fine temporal resolution. Literature on OMNI quality and solar-wind propagation uncertainty shows that representativeness can be limited, especially when the relevant flow tube is small or the upstream structure is inhomogeneous.

The correct consequence is not to abandon OMNI. It is to use averaged windows, record variability metrics, keep causal timing claims conservative, and resist over-fine binning in the conditioning analysis.

## 5.5 What is frozen, what remains provisional, and what stays open in the measurement model

| Frozen now | Provisional / pilot-confirm | Open decisions |
|---|---|---|
| Normalized s as spatial backbone; Shue baseline MP model; one baseline BS model plus alternative sensitivity run; dual near bins with `[0.2,0.4]` as primary; explicit sheath-membership checks; OMNI used as context rather than exact truth. | Default distance direction for the full catalogue; exact stability-window summary statistics; exact contamination filters for extreme near-boundary points; whether to add optional Monte Carlo perturbations during the first statistics pass. | Final alternative MP/BS model pair; exact s-uncertainty propagation scheme; exact point-removal threshold for ambiguous sheath membership; whether the local-normal version of s should become a default or remain a subset check. |

---

# 6. THEMIS catalogue design and the detector minimum viable product

The THEMIS branch is where the project becomes a real statistical study rather than a set of interesting examples. The crucial design choice is that the statistical unit is the encounter, not the raw crossing. This should now be treated as fixed. A single boundary-motion episode can generate several nominal crossings; treating those as independent samples would silently inflate the effective sample size and distort occurrence estimates.

The catalogue should therefore be encounter-centric from the start. Crossings matter, but mainly as metadata attached to a broader physical episode: they help define sheath windows, motion proxies, contamination risk, and quality flags. The sample count is the encounter count.

## 6.1 Encounter versus crossing

A crossing is a boundary transition event. An encounter is the larger analysis unit containing one or several nearby crossings plus the surrounding sheath interval, upstream summary, geometry, mapping solution, and quality information. The catalogue needs the encounter because the detector evaluates a layer-like sheath structure, not a single crossing timestamp.

This is also the correct place to store metadata that later becomes important for audit and interpretation: encounter duration, number of rapid crossings, normal-flow proxies, stability context, data coverage, and the reasons an encounter was excluded or downgraded.

## 6.2 Primary sample design

| Design choice | Current working stance | Why this is in the design | Status |
|---|---|---|---|
| Geometry | Near-subsolar dayside sample with small solar-zenith angle; initial target `<30°` with sensitivity extension if needed. | Classical PDL expectations and the project’s scope both target the near-subsolar dayside region. | Provisional numeric cut; frozen design principle. |
| Local time / latitude | Restrict to roughly `09–15 MLT` and low `|Z_GSM|` in the main sample. | Avoids unnecessary flank/high-latitude complexity and keeps the sample close to the classical target regime. | Provisional numeric cut; frozen design principle. |
| Upstream stability | Require relatively steady IMF direction/magnitude and dynamic pressure before the encounter. | Reduces detector confusion from rapidly changing drivers and weakens the case for time-local coincidence artifacts. | Frozen conceptually; exact metrics remain provisional. |
| Radial IMF | Treat strongly radial IMF as a dedicated regime rather than mixing it into the primary robust sample. | Radial IMF expands the foreshock toward the subsolar region and changes the contamination environment. | Frozen strategy; exact cut remains open. |
| Encounter merging | Merge rapid multiple crossings into one encounter when they clearly belong to the same boundary-motion episode. | Prevents double-counting and keeps the sample closer to physical episodes. | Frozen strategy; exact merge thresholds still open. |
| Exclusions | Report all exclusions and their reasons rather than silently dropping cases. | This is what makes a selection-function audit possible later. | Frozen. |

## 6.3 Detector MVP: what counts as core, support, QC, and later optional extension

| Category | Components | Role in the classification | Status now |
|---|---|---|---|
| Core PDL criteria | `Dn = median(n_near)/median(n_bg)`; `EB = median(|B|_near)/median(|B|_bg)`; `Δβ = median(β_near) − median(β_bg)`; trend-scale n–\|B\| anti-correlation; persistence across the near bin. | These define whether the encounter is layer-like at all. | Frozen as the detector backbone; thresholds remain open. |
| Supporting checks | Trend-vs-fluctuation decomposition; monotonicity toward the MP; total-pressure smoothness/consistency; simple force-balance sanity checks. | Reduce false positives and strengthen physical interpretability without defining the class by themselves. | Frozen conceptually; exact scoring still provisional. |
| Confounder / QC layer | Jet flag; wave or mirror-mode dominance flag; foreshock/transient flag; boundary-motion flag; mixing flag; overall Gold/Silver/Bronze grade. | This is what separates positive evidence from plausible alternatives. | Frozen as a required structural layer. |
| Optional later enhancements | Probabilistic classifier, ML scoring, event clustering, full Monte Carlo uncertainty at every stage, or more elaborate force-balance modeling. | May improve performance later but are not needed for the core thesis argument. | Do not activate before the MVP is working. |

## 6.4 Why confounders and QC are half of the result

The detector does not become credible merely by finding low density and high |B| near the magnetopause. In the dayside magnetosheath, that is not a unique signature. Jets can create short, strong dynamic-pressure structures; mirror-mode and related compressive waves can generate anti-correlated n and |B| fluctuations; foreshock transients can disturb the near-subsolar sheath; boundary motion can turn temporal variability into apparent spatial structure; and magnetospheric mixing can contaminate the very region where the signal is expected to be strongest.

For this reason, QC and confounder handling are not auxiliary modules. They are part of what the positive class means. A “PDL-positive” encounter without QC logic is too close to a generic “near-MP unusual interval” label. The correct internal stance is that the detector output includes both positive evidence and alternative-explanation structure.

| Confounder class | Why it matters for PDL detection | Minimum required handling |
|---|---|---|
| Jets | Can create local depletion/compression structure, high flow anomalies, and strong dynamic-pressure excursions that look layer-like if treated instantaneously. | Flag dynamic-pressure spikes and flow-speed anomalies; allow ambiguous classification rather than forced exclusion-only logic. |
| Mirror-mode / wave trains | Can produce anti-correlated n and \|B\| fluctuations without a monotonic boundary-adjacent layer. | Separate trend from high-frequency components; use wave-dominance and total-pressure smoothness checks. |
| Foreshock transients | Especially dangerous under radial or quasi-radial conditions near the subsolar region. | Keep radial IMF separate, use dedicated transient flags where possible, and preserve an explicit disturbed-regime label. |
| Boundary motion | Can create repeated crossings and spatial/temporal ambiguity in exactly the region where the signal is sought. | Use encounter merging, crossing metadata, motion proxies, and per-encounter quality grading. |
| Mixing / CDMP-like intervals | Magnetospheric-like plasma can encroach into the nominal sheath and mimic boundary-adjacent structure. | Use plasma/field sanity checks and explicit mixing flags instead of assuming all near-MP data are sheath data. |

## 6.5 Threshold tuning and development-set philosophy

The correct tuning strategy is staged and conservative. Build a small development set of encounters manually labeled as clear-PDL, clear-non-PDL, and ambiguous. Use that set to tune thresholds for separation without forcing the ambiguous class to disappear. Then test stability on an independent time interval or spacecraft subset. The purpose is not to maximize apparent performance; it is to avoid a detector that only looks good because it absorbed hidden researcher decisions.

This is also where “IMF-agnostic detection” becomes operational rather than rhetorical. IMF geometry should not be a detector input during tuning. It becomes part of the post-detection conditioning and interpretation layer.

## 6.6 Encounter-level output schema

| Output domain | Mandatory fields | Why the field set matters |
|---|---|---|
| Encounter metadata | Time bounds, spacecraft, crossing count, GSM position, MLT, solar-zenith angle, duration, merge notes. | Turns the encounter into a real statistical unit rather than an anonymous event ID. |
| Upstream summary | OMNI averages and variability measures over pre-encounter windows; regime tags; stability flags. | Allows later conditioning and makes filter logic auditable. |
| Mapping layer | MP/BS model choices, model inputs, s(t), s-bin occupancy, and mapping uncertainty notes. | Without this, the spatial meaning of the detector cannot be inspected. |
| PDL metrics | Dn, EB, Δβ, anti-correlation score, persistence score, monotonicity score, total-pressure support score. | This is the core evidence bundle for each encounter. |
| QC layer | Jet/wave/transient/motion/mixing flags plus Gold/Silver/Bronze grade and analyst note if needed. | Stores alternative explanations in the same object as the positive evidence. |
| QC figures | Standardized plots versus time and versus s, including filtered components and bin overlays. | Makes rapid review, development-set labeling, and appendix figure production feasible. |

---

# 7. Validation, falsification, robustness, provenance, and selection-function audit

These five ideas are close enough to be confused but different enough that the thesis should keep them separate. They answer different kinds of criticism. A detector can be validated yet not robust; a pipeline can be reproducible yet selection-biased; a robustness grid can exist yet still fail to include a falsification test. Keeping the categories explicit will make the methods chapter much stronger.

| Concept | Question it answers | Minimum implementation here | What goes wrong if omitted |
|---|---|---|---|
| Validation | Does the detector identify the intended class at all? | Manually labeled development set plus consistency checks on selected cases. | The detector can look plausible without ever being shown to separate clear positives from clear negatives. |
| Falsification | Can the claimed spatial structure be intentionally broken? | At minimum, a shuffled-s test and wave-dominated negative controls. | A detector may be responding to generic fluctuations rather than a boundary-adjacent spatial layer. |
| Robustness | Do the main results survive reasonable analysis choices? | Bounded grid over thresholds, filter width, s-bin choice, and boundary-model choice. | Results may depend on one convenient parameter choice and collapse under mild perturbation. |
| Provenance | Can every output be regenerated with the same settings and code state? | Config-driven runs, stored parameters, reproducible environment, and figure regeneration scripts. | The catalogue and figures become irreproducible once the analysis evolves. |
| Selection-function audit | What population did the filters actually leave you with? | Compare pre/post-filter distributions of geometry and upstream variables and report key sensitivities. | Physical dependence can be confused with filter dependence or survivorship within the sample. |

## Important internal rule

Audit papers should harden the workflow, not authorize endless branching. The purpose of a multiverse-style mindset here is a bounded, reported robustness grid with explicit choices—not uncontrolled post hoc variation.

---

# 8. MMS thickness branch: what it is for, what it can borrow, and what it must define itself

The MMS branch should remain protected from two opposite mistakes: overloading it until it becomes a second thesis, and under-specifying it until the resulting thicknesses look like feature-picking. Its job is narrower and more strategic. It is there to convert a detector-class signal into a spatial quantity, to show that at least some high-quality candidates behave enough like real layers to justify a thickness estimate, and to provide the mission-facing outputs with one geometrical anchor beyond a depletion factor alone.

This means the correct success criterion is not “many events.” It is “a few events that can survive criticism.”

## 8.1 What can be borrowed directly, and what cannot

| Method domain | Can be borrowed from the literature | Must be operationalized in this project |
|---|---|---|
| Timing analysis | Cross-spacecraft timing logic, error estimation, and quality gates from multi-spacecraft boundary literature. | Which PDL start/end features count as the timed boundaries of the layer. |
| Normals and coordinates | LMN and related coordinate-estimation logic, cross-checks, planarity concepts, and dimensionality diagnostics. | A hierarchy of preferred normal estimates for PDL-like gradient layers rather than sharp current sheets. |
| Gradient methods | Least-squares gradient calculation and volumetric-tensor logic. | How gradient-scale thickness is summarized into one event-level effective thickness. |
| Uncertainty treatment | Formal timing error, geometry sensitivity, and method-comparison logic. | How timing ambiguity, feature-picking variance, and normal-speed uncertainty are combined into a final `L ± σ` estimate. |
| Event grading | General ideas about data quality, geometry, and consistency checks. | The exact Gold/Silver/Bronze grading scheme for PDL thickness cases. |

## 8.2 Thickness definitions

Keeping two complementary thickness definitions is the right choice and should now be treated as fixed. Definition A is timing-based: identify the layer start and end on each spacecraft, estimate a layer-normal direction and normal speed `V_n`, and convert duration into spatial thickness via `L = V_n Δt`. Definition B is gradient-scale based: estimate `∇n` and/or `∇β` inside the depletion region, derive a local scale length, and summarize that into an effective thickness.

This dual approach is important because the PDL is not naturally a single discontinuity. A one-definition workflow would leave the thickness branch too vulnerable to criticism about feature selection and layer semantics.

## 8.3 Quality and success criteria for the MMS branch

- Prefer 3–5 near-subsolar dayside events with steady upstream context and good tetrahedron geometry; do not force larger N at the expense of credibility.
- Require explicit start/end rationale for each event, plus a short analyst note when ambiguity exists.
- Cross-check timing normals against at least one alternative normal estimate where possible.
- Report thickness with uncertainty and quality grade, not as a bare number.
- Treat disagreement between timing and gradient-scale thickness as information, not as something to hide.

---

# 9. What the SMILE/SXI-facing output must look like

The translation layer is where the project stops being a PDL study alone and becomes a mission-facing product. To achieve that, the final outputs must be designed as outputs from the beginning. The project should not end with “PDLs matter for SXI.” It should end with a small set of conditional quantities that can perturb a baseline sheath model or feed a simple forward sensitivity exercise.

The key discipline here is to keep the output compact, conditional, and explicit about where it applies. That is what will distinguish a usable prior package from a broad relevance claim.

| Output product | Suggested form | Why it is useful | What not to overclaim |
|---|---|---|---|
| Occurrence prior | `P(PDL | cone angle, clock angle, secondary driver regime)`, with confidence intervals. | Lets forward models decide when a PDL-like perturbation is likely to be active. | Do not claim universality outside the controlled dayside regime. |
| Depletion prior | Conditional distribution of `Dn` (and optionally `EB` or `Δβ`) by regime, in binned or compact parametric form. | Encodes how strong the density deficit tends to be when the layer occurs. | Do not finalize the exact functional family before seeing first extracted distributions. |
| Thickness / profile context | A small representative `L` distribution from the MMS branch or a simple profile-perturbation family near the MP. | Gives the density prior spatial meaning rather than treating it as a pointwise deficit only. | Do not pretend the low-N MMS subset defines a universal global thickness law. |
| Applicability limits | Explicit statement of geometry, stability, and regime limits for which the priors are intended. | Prevents mission-facing over-translation. | Applicability is part of the product, not a caveat footnote. |
| Sensitivity note | Baseline vs PDL-perturbed sheath profile comparison in a simple forward-model or emissivity-like calculation. | Shows why the prior matters for brightness gradients or boundary interpretation. | This is not a full inversion framework and should not expand into one. |

## 9.1 What mission relevance should sound like in the thesis

The mission-facing section should be short, concrete, and operational. It should say what prior or perturbation family is recommended, under which conditions it applies, what uncertainty goes with it, and what the leading-order consequence is for a simple forward calculation. That is enough. The project does not need to claim that it solves imaging retrieval, only that it supplies one missing near-boundary density ingredient in a form that imaging work can actually use.

---

# 10. The literature architecture is already strong enough; the task now is controlled extraction and use

The acquisition pool is already in the right state for execution. It contains 59 papers across 9 functional modules, plus supporting resources such as the THEMIS magnetopause crossing database and OMNI documentation. The immediate conversion queue contains 35 papers and is already ordered in a way that reflects the project’s real logic: measurement model first, detector/QC second, audit hardening third, thickness methods fourth, interpretation and catalogue caveats next, and mission-facing translation after the core pipeline structure is clear.

That is exactly the right shape. It means the project has already moved beyond “collecting literature” into “using literature to control design decisions.” The correct default from here is not to keep expanding the pool. It is to extract the right information from the existing pool in the right order.

## 10.1 Module structure of the current literature pool

| Module | Papers currently in pool | Current maturity in the literature | What this module must still operationalize in the thesis |
|---|---:|---|---|
| Foundational PDL physics | 6 | mature background | Translate classical signatures into a concise physical-semantic rule set that detector and discussion can both use. |
| IMF geometry and dayside sheath structure | 6 | mature statistics / interpretation | Turn cone angle, clock angle, radial IMF, and s-position into explicit analysis bins and reporting strata. |
| Mapping, measurement model, normalized coordinate, and OMNI | 5 | mature components, integration still needed | Define how MP/BS model error, upstream propagation, and stability windows combine into s-bin uncertainty and filter design. |
| Catalogue engineering, crossing/encounter logic, and data caveats | 5 | literature sparse / application immature | Encounter-merge thresholds, stability windows, excluded-regime metadata, and selection bookkeeping schema. |
| Detector and layer-likeness semantics | 3 | physics mature, detector literature sparse | Signal decomposition, persistence logic, and non-circular explanation-vs-detection separation. |
| Confounders and QC taxonomy | 12 | subfields mature, PDL-specific integration still needed | Build a QC flag hierarchy that allows compound structures and mixed evidence, not single-threshold exclusions. |
| MMS thickness, boundary methods, and uncertainty | 11 | methods mature, PDL application immature | Feature pairing, start/end definitions, normal hierarchy, planarity grade, and total `L±σ` synthesis. |
| Mission-facing priors, parameterization, and forward-model relevance | 7 | forward-model background mature, PDL-specific translation immature | Translate occurrence and depletion statistics into compact conditional priors that can perturb a baseline sheath model. |
| Audit, robustness, and reproducibility | 4 | borrowed methods mature | Define which choices vary, which stay fixed, how encounter-level resampling works, and what gets logged automatically. |

## 10.2 What the module balance is telling you

The detector module is intentionally thin (3 papers). That is not a weakness of your pool; it reflects the fact that the field does not provide a ready-made IMF-agnostic, audit-ready PDL detector. You are expected to operationalize one.

The QC/confounder module is thicker than the detector module. That is a strength, because in this project negative discrimination is almost as important as positive identification.

The MMS thickness module is also thick, but those papers are borrowed methods, not direct evidence that a PDL exists. Their role is methodological hardening.

The mapping/measurement-model module is compact but complete. It should remain near the front of the conversion sequence because it sets the meaning of all spatial claims.

The mission-facing module is already sufficiently built. It should not be allowed to grow so large that it displaces the detector or measurement core.

## 10.3 First-pass conversion sequence and why the sequence matters

| Batch | Core papers or modules | What to extract first | Concrete output unlocked |
|---|---|---|---|
| Batch 1: mapping and measurement control | MAP-04, MAP-05, MAP-03, MAP-01, MAP-02 | Model assumptions, regime-dependent error behavior, OMNI caveats, and implementation notes for s-space. | A baseline measurement model and a first uncertainty/control plan. |
| Batch 2: detector semantics and QC anchors | DET-01, DET-02 plus the core QC set (mirror modes, jets, transient phenomena, mixed structures) | Joint layer-like signatures, trend-vs-fluctuation logic, and the operational exclusion logic for confounders. | Detector v0 and the first QC taxonomy. |
| Batch 3: audit hardening | AUD-01, AUD-03, AUD-02 | Encounter-aware uncertainty, bounded robustness design, and provenance rules. | A finite robustness grid and run-provenance specification. |
| Batch 4: MMS thickness workflow | THK-04, THK-07, THK-08, THK-05, THK-10, THK-09 | Timing error model, gradient workflow, LMN/normal logic, and quality gates. | Thickness workflow template and case-selection checklist. |
| Batch 5: interpretation and catalogue caveats | GEO-05, GEO-06, CAT-02, CAT-04, CAT-01, CAT-03, plus thin foundation anchors | How IMF geometry should be binned, how encounter engineering should be defended, and what large-sample external consistency should look like. | Interpretation strata and selection-function/audit vocabulary. |
| Batch 6: mission translation | PRI-01, PRI-03, PRI-06 | What a baseline sheath model looks like, how density structure enters imaging calculations, and what a compact parameterization can look like. | A concrete prior format and sensitivity-demonstration design. |

## 10.4 Misuse guardrails: how not to let the literature do the wrong job

| Paper group | Likely misuse | Safer use in this project |
|---|---|---|
| MAP-01 / MAP-02  \nShue 1998; Merka 2005 | Treating empirical MP/BS surfaces as true boundaries for each event. | Use them as baseline geometry for normalized s-mapping, then attach explicit error envelopes and regime caveats. |
| GEO-05 / GEO-06  \nMichotte de Welle 2024; Pi 2024 | Using large-sample spatial-profile papers as detector labels or event truth sets. | Use them to justify stratification, interpretation, and external consistency checks. |
| QC-03 / QC-05 / QC-07 / QC-10  \nArcher 2013; Plaschke 2018; Raptis 2020; Blanco-Cano 2023 | Assuming a single jet definition or threshold is enough to exclude all jet-like contamination. | Use several papers together to show jets are heterogeneous and can overlap with other structures. |
| AUD-01 / AUD-03 / AUD-04  \nKünsch 1989; Steegen 2016; Silberzahn 2018 | Using audit papers as permission for endless post hoc analysis branching. | Use them to define a bounded, reported robustness grid and encounter-aware uncertainty design. |
| THK-04 / THK-05 / THK-10 / THK-09  \nHaaland 2004; De Keyser 2007; Denton 2018; Rezeau 2018 | Treating neighboring boundary/current-sheet methods as a finished PDL thickness recipe. | Borrow equations and gates, but explicitly define PDL start/end, feature pairing, and total uncertainty yourself. |
| PRI-01 / PRI-03 / PRI-06  \nRobertson 2003; Sun 2019; Mshpy23 2024 | Treating smooth-sheath parameterizations or emissivity models as evidence that PDL can be ignored. | Use them as translation targets and baselines that your PDL-aware priors can perturb. |

## Literature-control rule from this point onward

Expansion is closed by default. Only execution-exposed gaps that materially weaken detector defensibility, measurement control, or mission translation should trigger targeted additions.

---

# 11. The next 4–8 weeks: execution sequence, pilot goals, and go/no-go logic

The short-horizon goal is not to generate thesis-grade statistics immediately. It is to move from conceptual closure to operational control. The order matters. A large catalogue run performed before the measurement model, detector semantics, and QC plotting are stable will create noise faster than it creates knowledge.

The correct near-term strategy is therefore to win first on interpretation control and only then on sample size.

| Time block | Primary objectives | Concrete outputs | Decision unlocked |
|---|---|---|---|
| Weeks 1–2 | Build the pipeline skeleton, implement baseline s-mapping, convert the first measurement-model and QC papers, and run 1–2 pilot encounters end-to-end. | Encounter object, s-mapper, metric calculator, standard QC figure, and first uncertainty/control notes. | Whether the measurement-model design is implementable as currently frozen. |
| Weeks 3–4 | Assemble the development set, implement detector metrics on trend-scale quantities, and produce a small case-study atlas. | Clear-PDL / clear-non-PDL / ambiguous mini-set, detector v0.1, first confounder flags. | Whether the detector backbone separates cases cleanly enough to justify threshold tuning. |
| Weeks 5–6 | Run bounded threshold and bin tests, implement the selection-function audit, and stress the detector with falsification checks. | Detector v1, robustness grid, shuffled-s test, filter-sensitivity results, audit scripts. | Whether the project can safely move from pilot cases to a larger controlled batch. |
| Weeks 7–8 | Run the first controlled THEMIS batch, compare qualitative patterns with large-sample maps, and shortlist MMS thickness candidates. | First occurrence/depletion figures, first regime-conditioned profiles, preliminary MMS candidate list. | Whether the main statistical branch is stable enough to scale and whether the MMS branch has at least a few viable events. |

## 11.1 Pilot-analysis questions that must be answered before scaling

- Does the normalized-coordinate mapping produce sensible `s(t)` and enough occupancy in the planned near/background bins for real encounters?
- Do clear-PDL and clear-non-PDL pilot cases separate on `Dn`, `EB`, `Δβ`, anti-correlation, and persistence in the way the detector assumes?
- Do wave-dominated and jet-dominated intervals fall naturally into ambiguous or flagged space rather than into the positive class?
- Does the shuffled-s falsification test destroy the apparent layer-like trend in cases that are supposed to be spatial?
- Is the `[0.0,0.2]` bin usable as a science-facing sensitivity bin, or is it too contaminated to do more than support thickness-focused interpretation?
- Can at least one high-quality MMS event produce a reasonably consistent timing-based and gradient-scale thickness estimate?

## 11.2 Go / no-go rule for moving to a larger THEMIS batch

Do not scale the catalogue just because data access is working. The project should move to a larger THEMIS batch only after five conditions are met: the encounter object is stable, s-mapping has been sanity-checked on real cases, detector metrics separate at least some clear positives from clear negatives, confounder flags catch obvious contaminated cases, and the selection-function audit scripts exist. Until then, more data will mainly amplify uncertainty and hidden inconsistency.

---

# 12. How the thesis should grow from this blueprint, and the current decision status

## 12.1 Thesis growth map

| Thesis section | What grows into it from this blueprint | What you should prepare now |
|---|---|---|
| Methods | Sample design, encounter logic, measurement model, detector metrics, QC taxonomy, audit framework, MMS thickness workflow, and mission-facing output format. | Pipeline objects, configuration schema, QC figure templates, and the measurement-model notes from first-pass extraction. |
| Results | Case-study atlas, superposed-coordinate profiles, occurrence and depletion statistics, robustness results, and MMS thickness cases. | Pilot plots, standard figure grammar, and a clean output schema for batch analyses. |
| Discussion | Physical interpretation versus measurement limitation, confounder residuals, regime-specific behavior, and the limits of the SMILE translation. | A running log of what is explanation, what is evidence, and what remains uncertainty. |
| Mission-facing outputs | Occurrence priors, depletion priors, thickness/profile context, applicability limits, and the sensitivity note. | A compact output specification now, so later results already fall into the right containers. |

## 12.2 Current decision status: frozen, provisional, and open

### Frozen now

- The project’s main identity: occurrence + thickness + mission-facing priors, not pure phenomenology.
- THEMIS encounter, not raw crossing, is the statistical unit.
- Detection is IMF-agnostic at detection time; IMF geometry enters after detection for conditioning and interpretation.
- Normalized magnetosheath mapping in s-space is the spatial backbone of the catalogue.
- Dual near bins stay, with `[0.2,0.4]` as the primary robust bin and `[0.0,0.2]` as the fragile but physics-rich sensitivity bin.
- The detector backbone is `Dn`, `EB`, `Δβ`, trend-scale n–\|B\| anti-correlation, and persistence, with total pressure as a supporting score rather than a sole criterion.
- Confounder flags and quality grading are structural outputs, not optional commentary.
- The MMS branch keeps two thickness definitions and quality grades.
- The mission-facing output remains priors plus a sensitivity demonstration, not full inversion.

### Provisional, but close to frozen

- Exact SZA, MLT, and `|Z|` numerical cuts for the primary THEMIS sample.
- Exact upstream stability metrics and pre-encounter window summary definitions.
- Exact filter width for trend-scale decomposition.
- Exact shape of the Gold/Silver/Bronze grading logic.
- Which alternative MP and BS models provide the most informative sensitivity pair.
- Whether the local-normal version of s is only a subset check or becomes a more general alternative.

### Open decisions that must wait for extraction or pilot tests

- Final numeric thresholds for `Dn`, `EB`, `Δβ`, anti-correlation, persistence, and wave-dominance.
- Exact radial-IMF boundary used to separate the dedicated regime.
- Exact contamination-removal threshold for ambiguous near-boundary sheath membership.
- Whether the timing-based or gradient-scale thickness estimate becomes primary in the write-up.
- The final mathematical form of the depletion prior package once the empirical distributions are visible.
- Whether total-pressure behavior is reliable enough to contribute a score or should remain a softer support check.

## Final internal judgment

The project’s logic is sufficiently compressed and defended to move into download, conversion, first-pass extraction, and pilot analysis. The main risk now is not conceptual weakness; it is losing discipline and repeatedly reopening design choices that are already settled enough to proceed.

---

# Appendix: selected reference backbone by module (the workbook remains the full bibliography)

This appendix is not meant to replace the acquisition workbook. Its purpose is to keep visible which papers are functioning as the main intellectual anchors for each module so that first-pass extraction stays aligned with the project architecture.

## Foundational PDL physics

- Zwan & Wolf (1976) — Depletion of solar wind plasma near a planetary boundary.
- Crooker, Eastman, & Stiles (1979) — Observations of plasma depletion in the magnetosheath at the dayside magnetopause.
- Anderson, Phan, & Fuselier (1997) — Relationships between plasma depletion and subsolar magnetopause reconnection.
- Wang, Raeder, & Russell (2004) — Plasma depletion layer: Magnetosheath flow structure and forces.

## IMF geometry and dayside sheath structure

- Michotte de Welle et al. (2024) — Spatial distribution of plasma density and magnetic field amplitude in the dayside magnetosheath as a function of IMF orientation.
- Pi et al. (2024) — Spatial profiles of magnetosheath parameters under different IMF orientations: THEMIS observations.
- Michotte de Welle et al. (2022) — Global three-dimensional draping of magnetic field lines in Earth’s magnetosheath from in-situ spacecraft measurements.

## Mapping, measurement model, and OMNI

- Shue et al. (1998) — Magnetopause location under extreme solar wind conditions.
- Merka et al. (2005) — Three-dimensional position and shape of the bow shock and their variation with upstream Mach numbers and IMF orientation.
- Walsh, Bhakyapaibul, & Zou (2019) — Quantifying the uncertainty of using solar wind measurements for geospace inputs.
- Lin et al. (2024) — Assessing the performance of magnetopause models based on THEMIS data.
- Aghabozorgi Nafchi et al. (2024) — Magnetopause location modeling using machine learning: inaccuracy due to solar wind parameter propagation.

## Catalogue engineering and caveats

- King & Papitashvili (2005) — Solar wind spatial scales in and comparisons of hourly Wind and ACE plasma and magnetic field data.
- Plaschke et al. (2009) — Statistical study of the magnetopause motion: first results from THEMIS.
- Vokhmyanin et al. (2019) — On the evaluation of data quality in the OMNI interplanetary magnetic field and solar wind data set.
- Staples et al. (2020) — Do statistical models capture the dynamics of the magnetopause during sudden magnetospheric compressions?

## Detector and QC anchors

- Anderson, Fuselier, Gary, & Denton (1994) — Magnetic spectral signatures in the Earth’s magnetosheath and plasma depletion layer.
- Soucek, Lucek, & Dandouras (2008) — Properties of magnetosheath mirror modes observed by Cluster and their response to changes in plasma parameters.
- Archer & Horbury (2013) — Magnetosheath dynamic pressure enhancements: occurrence and typical properties.
- Soucek, Escoubet, & Grison (2015) — Magnetosheath plasma stability and ULF wave occurrence as a function of location in the magnetosheath.
- Raptis et al. (2020) — Classifying Magnetosheath Jets Using MMS: Statistical Properties.
- Blanco-Cano et al. (2023) — Jets and Mirror Mode Waves in Earth’s Magnetosheath.
- Jiang et al. (2025) — Spatial dependence of ion-kinetic instabilities in the Earth’s magnetosheath: MMS observations.

## MMS thickness and uncertainty

- Haaland et al. (2004) — Four-spacecraft determination of magnetopause orientation, motion and thickness.
- De Keyser et al. (2007) — Least-squares gradient calculation from multi-point observations of scalar and vector fields.
- Zhou et al. (2009) — On the error estimation of multi-spacecraft timing method.
- Vogt, Haaland, & Paschmann (2011) — Accuracy of multi-point boundary crossing time analysis.
- Denton et al. (2018) — Determining L-M-N current sheet coordinates at the magnetopause from MMS data.
- Rezeau et al. (2018) — Analyzing the magnetopause internal structure: new possibilities offered by MMS tested in a case study.

## Mission-facing priors and forward-model relevance

- Robertson & Cravens (2003) — X-ray emission from the terrestrial magnetosheath.
- Sun et al. (2019) — Soft X-ray imaging of the magnetosheath and cusps under different solar wind conditions.
- Jung et al. (2024) — Mshpy23: a user-friendly, parameterized model of magnetosheath conditions.

## Audit and reproducibility

- Künsch (1989) — The jackknife and the bootstrap for general stationary observations.
- Sandve et al. (2013) — Ten simple rules for reproducible computational research.
- Steegen et al. (2016) — Increasing transparency through a multiverse analysis.

---

# 1) Short action plan: start tomorrow

- Freeze a one-page project charter containing only four boxes: core question, measurement model, detector MVP, and mission-facing output.
- Start first-pass literature conversion and extraction in the existing queue order, beginning with the measurement-model papers and the core QC anchors.
- Implement the minimum pipeline objects immediately: encounter table, s-mapping module, detector-metric calculator, QC figure generator, and run-provenance logger.
- Build a small development set of encounters labeled clear-PDL, clear-non-PDL, and ambiguous before touching full-catalogue statistics.
- Run one or two THEMIS pilot encounters end-to-end and force them to output `s(t)`, near/background occupancy, detector metrics, flags, and a standard QC report.
- Only after those pilots behave sensibly should threshold tuning and wider catalogue execution begin.

# 2) Freeze list: do not keep revising these now

- Encounter is the statistical unit; crossing count is metadata, not the sample size.
- Detection remains IMF-agnostic at detection time.
- Normalized magnetosheath mapping is the project’s spatial backbone.
- Dual near bins remain in place, with `[0.2,0.4]` as the primary robust bin.
- Confounders and QC remain structural outputs, not post hoc commentary.
- The detector backbone remains `Dn`, `EB`, `Δβ`, trend-scale anti-correlation, and persistence.
- Total pressure remains a supporting consistency check, not the sole physical criterion.
- Radial IMF stays a dedicated regime rather than being mixed into the primary robust sample.
- The MMS branch keeps two thickness definitions and quality grading.
- The mission-facing output stays as priors plus a sensitivity demonstration, not a full imaging inversion.

# 3) Decisions that must wait for first-pass extraction or small pilot tests

- Exact numerical thresholds for `Dn`, `EB`, `Δβ`, anti-correlation strength, persistence, and wave-dominance.
- Exact filter width for separating trend-scale structure from high-frequency fluctuations.
- Exact SZA / MLT / `|Z|` cut values for the primary THEMIS sample.
- Exact radial-IMF cut for the dedicated disturbed regime.
- Exact encounter-merge threshold during boundary-motion episodes.
- Exact contamination-removal rule for ambiguous sheath membership near the magnetopause.
- Which alternative MP and BS models become the main sensitivity pair.
- Whether Sun–Earth-line or local-normal s becomes the preferred default outside subset testing.
- Which thickness definition becomes primary in the write-up when the two do not perfectly agree.
- The final mathematical form of the SMILE/SXI-facing depletion prior package.

Page
