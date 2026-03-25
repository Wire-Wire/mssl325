# LLM Handoff — PDL Pilot Pipeline

**Load this first when resuming in a new session.**

---

## One-line summary

Phase 1.5 complete: a config-driven THEMIS PDL detection pipeline that runs end-to-end on both synthetic and real CDAWeb data, with full provenance, but the live pilot windows are not actually dayside encounters — the data bridge works, the science-grade pilots have not happened yet.

## Current milestone

- Phase 1 (synthetic MVP): **done**
- Phase 1.5 (dual-source bridge): **done, needs better pilot windows**
- Phase 2 (threshold tuning, development set, catalogue): **not started**

## Frozen decisions (do not reopen)

- Encounter (not crossing) is the statistical unit
- `s = d_MP / (d_MP + d_BS)` normalized coordinate, Sun–Earth line
- Shue 1998 (MP) + Merka 2005 (BS) as baseline boundary models
- Dual near bins: [0.0,0.2] fragile + [0.2,0.4] primary, background [0.6,1.0]
- IMF-agnostic detection (upstream enters post-detection only)
- Detector backbone: Dn, EB, Δβ, trend-scale ρ(n,|B|), persistence
- QC flags + Gold/Silver/Bronze grading are structural, not optional
- Provenance-first design (frozen config, manifest, logging)

## Provisional choices (Phase 1.5, configurable)

- Backend: cdasws (CDAWeb REST API)
- Plasma product: THEMIS MOM L2 (peim), not GMOM
- Resampling: 3 s cadence, linear interpolation, 30 s max gap → NaN
- OMNI window: 30 min pre, 10 min post
- Trend window: 120 s running median
- s-uncertainty: ±0.5 Re MP, ±1.0 Re BS (simple perturbation)
- QC thresholds: jet=2× median Pdyn, wave=0.3 relative fluctuation, motion=>2 crossings
- Pilot windows: not vetted as dayside events

## Deferred decisions (do not implement)

- Detector thresholds for Dn, EB, Δβ, ρ, persistence
- Local-normal s variant
- Full Monte Carlo uncertainty
- Alternative MP/BS model pair for sensitivity
- Encounter merge thresholds
- Radial-IMF cut
- Shuffled-s falsification
- Selection-function audit
- MMS thickness (timing + gradient-scale)
- SMILE/SXI priors
- ML classification

## Core capabilities implemented

1. **Synthetic data generation** — 600-point PDL-like sheath traversal with embedded depletion
2. **Live data fetch** — THEMIS FGM/MOM/STATE + OMNI 1-min via cdasws, with caching + fallbacks
3. **Normalization** — resampling, gap masking, unit conversion (km→Re, eV/cm³→nPa)
4. **s-mapping** — normalized coordinate with uncertainty envelope and bin occupancy
5. **Metrics** — Dn, EB, Δβ, ρ, persistence, ptot_smoothness, fluctuation_amp (no thresholds)
6. **QC** — jet/wave/motion flags + Gold/Silver/Bronze grading + 6-panel diagnostic PNG
7. **Provenance** — frozen config, run manifest with git/packages/source metadata/cache summary
8. **Config-driven** — YAML configs, Pydantic validation, data_source dispatch

## Top 5 risks / gaps

1. **Live pilot windows are not dayside.** pilot_001: SZA=72°, Y=10.5 Re (flank). pilot_002: X=−2.2 Re (nightside). No near-bin occupancy, all metrics NULL. Need windows with X>8 Re, SZA<30°.
2. **OMNI fill values not filtered.** CDAWeb returns 9999.99 etc. as fill. These propagate into upstream medians. Could produce garbage Dp/Bz/Ma for boundary models.
3. **No sheath membership check.** Pipeline assumes all data within the encounter window is magnetosheath. No validation against magnetospheric or solar-wind plasma regimes.
4. **transient_flag and mixing_flag are stubs** (always False). Blueprint §6.4 expects them operational for QC grading.
5. **Cone/clock angle computation is approximate.** Uses only OMNI BZ_GSM (not full 3D B-vector). Acceptable for Phase 1.5 context but not sufficient for fine IMF conditioning.

## Next incremental tasks (priority order)

1. **Curate 3–5 real dayside encounter windows** (X>8 Re, |Y|<5 Re, SZA<30°, steady Dp). This is the single blocker for science-relevant live results.
2. **Add OMNI fill-value masking** — replace fill values (9999.99, 99999.9) with NaN before computing medians.
3. **Add minimal sheath membership check** — beta>0.1, density>1 cm⁻³, |B| in sheath range.
4. **Run blueprint pilot-analysis questions** (§11.1): does s(t) show mixed-bin occupancy? do metrics separate clear positives from negatives?
5. **Begin development-set construction** for threshold exploration.

## Key files

| What | Where |
|---|---|
| Blueprint | `RP/internal_master_research_blueprint_PDL_SMILE.md` |
| Full state doc | `docs/PHASE_1_5_STATE.md` |
| Pipeline entry | `src/pdl_pilot/cli/run_pilot.py` |
| Provider interface | `src/pdl_pilot/data/provider.py` |
| Live adapter | `src/pdl_pilot/data/live_provider.py` |
| Encounter model | `src/pdl_pilot/encounter/model.py` |
| Config schema | `src/pdl_pilot/config/schema.py` |
| Synthetic config | `configs/pilot_themis.yaml` |
| Live config | `configs/pilot_live.yaml` |

## Repo stats

- 59 offline-safe tests, all passing
- 2 configs (synthetic + live)
- 4 completed runs (2 synthetic, 2 live)
- 8 cached CDAWeb datasets
- Dependencies: numpy, scipy, matplotlib, pydantic, pyyaml + optional cdasws, cdflib
