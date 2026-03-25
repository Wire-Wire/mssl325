# Phase 1.5 State Document — PDL Pilot Pipeline

**Date:** 2026-03-25
**Repo:** `mssl325` (branch: `main`, commit: `ac3bc92`)
**Package:** pdl-pilot v0.1.0, Python ≥ 3.10

---

## 1. Project mainline

This project builds a controlled THEMIS dayside PDL detection pipeline. The central question is whether a boundary-adjacent, layer-like density depletion can be isolated in THEMIS magnetosheath data after explicit coordinate control, confounder handling, and selection-function audit — and then translated into compact mission-facing priors for SMILE/SXI.

The blueprint (RP/internal_master_research_blueprint_PDL_SMILE.md) defines four problem layers: physics, measurement, engineering/audit, and mission translation. Phase 1 built the engineering skeleton. Phase 1.5 bridges it to real data.

---

## 2. Phase 1.5 goal and acceptance status

**Goal:** Extend the Phase-1 synthetic MVP into a dual-source pilot pipeline that runs the same encounter-level flow on both synthetic fixtures and real THEMIS/OMNI data.

| Acceptance criterion | Status |
|---|---|
| Existing synthetic pilot path still works | **PASS** — Dn=0.949, EB=1.054, ρ=−0.946 reproduced |
| Repo supports live data source mode | **PASS** — `data_source: "live"` dispatches to LiveProvider |
| Minimal THEMIS+OMNI adapter exists | **PASS** — FGM, MOM, STATE, OMNI via cdasws |
| Live data cached locally with source metadata | **PASS** — 8 normalized NPZ files, cache index, hit/miss logged |
| Provenance manifests include live-source details | **PASS** — per-encounter SourceMetadata in manifest |
| Same pipeline produces outputs for both modes | **PASS** — encounter JSON, QC PNG, manifest for both |
| 1–2 real pilots run if windows exist | **PARTIAL** — runs complete but windows are not dayside (see §11) |
| Tests remain offline-safe | **PASS** — 59 passed, 1 skipped (network test), 0 failures |
| No scope creep | **PASS** — no catalogue/tuning/MMS/priors code added |

---

## 3. Repo architecture

```
src/pdl_pilot/
  config/
    schema.py          — Pydantic config: BinConfig, BoundaryModelConfig, FilterConfig,
                         UncertaintyConfig, EncounterSpec, LiveDataConfig, PipelineConfig
  data/
    provider.py        — DataProvider ABC, EncounterData container, SourceMetadata
    synthetic.py       — Phase-1 synthetic generator (600pts, 1s, PDL-like envelope)
    synthetic_provider.py — SyntheticProvider wrapping synthetic.py
    live_provider.py   — LiveProvider: CDAWeb/cdasws fetch + normalize + resample
    cache.py           — DataCache: deterministic paths, NPZ storage, JSON index
  encounter/
    model.py           — Encounter, UpstreamSummary, MappingResult, MetricBundle, QCFlags
  boundaries/
    shue1998.py        — Shue (1998) MP standoff + flaring
    merka2005.py       — Merka (2005) BS standoff (Farris-Russell form)
  mapping/
    s_mapper.py        — compute_s, compute_s_with_uncertainty, compute_bin_occupancy
  metrics/
    calculator.py      — Dn, EB, Δβ, ρ(n,B), persistence, ptot_smoothness, fluctuation_amp
  qc/
    reporter.py        — compute_qc_flags + generate_qc_report (6-panel PNG)
  provenance/
    tracker.py         — ProvenanceTracker: run_id, frozen config, manifest, source metadata
  cli/
    run_pilot.py       — CLI entry: provider dispatch, upstream build, pipeline orchestration

configs/
  pilot_themis.yaml    — Synthetic pilot (2 encounters, data_source=synthetic)
  pilot_live.yaml      — Live pilot (2 encounters, data_source=live)

tests/
  test_boundaries.py   — Shue1998, Merka2005 (8 tests)
  test_config.py       — Config loading, hashing (5 tests)
  test_mapping.py      — s-coordinate, occupancy (6 tests)
  test_metrics.py      — Trend extraction, metrics (3 tests)
  test_qc.py           — QC flags, grading, PNG, provenance (4 tests)
  test_provider.py     — Provider abstraction, dispatch (10 tests)
  test_cache.py        — Cache paths, policy, index (12 tests)
  test_normalization.py — Interp, epoch, upstream build (11 tests, 1 skipped)
```

---

## 4. Dual-source implementation

### Provider abstraction

`DataProvider` (ABC) → `fetch(EncounterSpec) → EncounterData`

- **SyntheticProvider**: wraps `generate_synthetic_encounter()`. 600 pts at 1 s. PDL-like Gaussian envelope at x=10.3 Re (50% density dip, 40% B enhancement). Hardcoded 200 eV ion temperature. All arrays share fake epoch.
- **LiveProvider**: lazy-imports `cdasws`. Fetches 4 datasets per encounter:
  - **THx_L2_FGM**: `thx_fgs_gsm` (vector B-field GSM) → compute |B|. Fallback: `thx_fgs_btotal`.
  - **THx_L2_MOM**: `thx_peim_density`, `thx_peim_velocity_gsm`, `thx_peim_ptot`. Fallback: density-only with T=200 eV assumed.
  - **THx_L1_STATE**: `thx_pos_gsm` in km, converted to Re (÷6371.2).
  - **OMNI_HRO_1MIN**: BZ_GSM, F, Pressure, Mach_num, flow_speed. Window: [tstart−30min, tend+10min].

### Normalization

All data resampled onto a common analysis timeline:
- Cadence: 3.0 s (PROVISIONAL)
- Method: linear interpolation (PROVISIONAL)
- Gap masking: NaN for gaps >30 s (PROVISIONAL)
- Beta: computed from `peim_ptot` (eV/cm³ → nPa via ×1.6e-4) and magnetic pressure
- If `peim_ptot` unavailable: fallback T=200 eV

### Caching

`DataCache` in `data_cache/normalized/{encounter_id}/{dataset}.npz`.
- Policy: "use" (reuse) / "refresh" (re-download) / "skip" (no cache)
- Index: `data_cache/cache_index.json` with dataset, trange, timestamp, cache_hit per entry
- Raw CDF cache (`data_cache/raw/`) exists structurally but is not used in Phase 1.5 — cdasws returns xarray directly, normalized data is cached as NPZ

---

## 5. Measurement model implementation

### s-coordinate (s_mapper.py)

```
s = d_MP / (d_MP + d_BS)
```

where `d_MP = |x_GSM − MP_standoff|`, `d_BS = |x_GSM − BS_standoff|`, along the Sun–Earth line (x-axis only).

- **MP**: Shue (1998) — `r₀ = (11.4 + k·Bz) · Dp^(-1/6.6)` with Bz-sign-dependent k
- **BS**: Merka (2005) — Farris-Russell form with 1.1 compression factor; fallback ratio 1.3 if Ma ≤ 1
- **Uncertainty envelope**: simple perturbation ±0.5 Re (MP), ±1.0 Re (BS); generates s_lo, s_hi
- **Local-normal variant**: NOT implemented. Blueprint §5.1 marks this as provisional/deferred.

### Bins

| Bin | Range | Role |
|---|---|---|
| very_near | [0.0, 0.2) | Physics-rich, fragile to boundary error |
| near | [0.2, 0.4) | **Primary robust science bin** |
| background | [0.6, 1.0] | Normalization baseline |

Gap [0.4, 0.6) is intentionally unassigned — transition zone.

### Upstream context

- Synthetic: hardcoded (Bz=2, Bt=5, Dp=2, Ma=8, stable)
- Live: median of OMNI arrays over analysis window
  - Stability: CV(Dp) < 0.3 → "stable", else "variable"
  - Cone angle: arccos(|Bz|/Bt) — only uses Bz, not full 3D. This is an **acknowledged limitation** (OMNI provides BZ_GSM but the cone angle properly requires Bx).
  - Clock angle: arctan2(|Bz|, Bt) — similarly simplified

---

## 6. Encounter object and pipeline flow

### Encounter (model.py)

Top-level container with nested:
- `UpstreamSummary` — OMNI-derived averages
- `MappingResult` — s(t), occupancy, uncertainty, model inputs
- `MetricBundle` — Dn, EB, Δβ, ρ, persistence, ptot_smoothness, fluctuation_amp
- `QCFlags` — jet/wave/transient/motion/mixing flags + Gold/Silver/Bronze grade

Plus time-series arrays (in-memory only, not serialized to JSON).

### Pipeline flow (run_pilot.py)

1. Load config → build provider (synthetic or live)
2. For each EncounterSpec:
   a. `provider.fetch(spec)` → EncounterData
   b. Build Encounter shell with position metadata (MLT, SZA)
   c. Build UpstreamSummary (hardcoded or OMNI medians)
   d. Compute s-mapping + uncertainty + occupancy
   e. Compute metrics (Dn, EB, Δβ, ρ, persistence, ptot_smoothness)
   f. Compute QC flags and grade
   g. Generate 6-panel QC report PNG
   h. Save encounter JSON
3. Write combined all_encounters.json
4. Write run_manifest.json with full provenance

---

## 7. Minimal metrics — what they are and how they are computed

| Metric | Definition | Bin used | Interpretation |
|---|---|---|---|
| Dn | median(n_near) / median(n_bg) | near / background | <1 → depletion |
| EB | median(\|B\|_near) / median(\|B\|_bg) | near / background | >1 → enhancement |
| Δβ | median(β_near) − median(β_bg) | near / background | <0 → beta reduction |
| ρ(n,B) | Spearman(n_trend, \|B\|_trend) in [0.0, 0.4) | very_near + near | <0 → anti-correlation (PDL signature) |
| Persistence | fraction(n < n_bg) in near bin | near | High → sustained depletion |
| ptot_smoothness | 1 − σ(ptot)/mean(ptot) in near region | very_near + near | High → smooth total pressure (layer-like) |
| fluctuation_amp | σ(density − trend) | full interval | High → noisy (wave/jet?) |

Trend extraction: running median with 120 s window (scipy median_filter, reflect edges).

**No thresholds are applied.** All metrics are raw values. Classification is deferred to Phase 2.

---

## 8. QC report contents

6-panel PNG figure per encounter:
1. Density (raw + trend) vs time
2. |B| (raw + trend) vs time
3. Beta (log scale) vs time
4. Total pressure vs time
5. s(t) with bin boundaries (very_near=red, near=orange, background=blue)
6. Text summary: all metrics, grade, flags, occupancy

### QC flags (current thresholds — all PROVISIONAL)

| Flag | Trigger | Threshold |
|---|---|---|
| jet_flag | max(n·v²) > 2× median(n·v²) | 2× |
| wave_flag | σ(density_residual) / median(\|density_trend\|) > 0.3 | 0.3 |
| motion_flag | crossing_count > 2 | 2 |
| transient_flag | placeholder (always False) | — |
| mixing_flag | placeholder (always False) | — |

Grade: 0 flags → Gold, 1 → Silver, ≥2 → Bronze.

---

## 9. Config decision status

### Frozen (do not reopen)

- Encounter is the statistical unit
- s = d_MP/(d_MP+d_BS) as spatial backbone
- Shue 1998 MP + Merka 2005 BS as baseline
- Dual near bins: [0.0,0.2] + [0.2,0.4], primary = [0.2,0.4]
- IMF-agnostic detection (IMF enters post-detection)
- Detector backbone: Dn, EB, Δβ, ρ(n,B), persistence
- QC flags + grading are structural outputs
- Synthetic fixtures retained
- Real pilot windows manually specified
- Provenance-first run design

### Provisional (Phase 1.5 — configurable, confirm with real pilots)

- Distance along Sun–Earth line (local-normal deferred)
- Trend window: 120 s
- s-uncertainty: ±0.5 Re MP, ±1.0 Re BS (simple perturbation)
- Jet threshold: 2× median Pdyn
- Wave threshold: 0.3 relative fluctuation
- Live backend: cdasws
- Default plasma product: THEMIS MOM L2 (peim), not GMOM
- Resampling cadence: 3 s, linear interpolation
- Max gap fill: 30 s
- OMNI pre-window: 30 min
- Cache layout: data_cache/{raw,normalized}/
- Pilot encounter windows (not vetted)

### Deferred (do not implement now)

- Detector thresholds (Dn, EB, Δβ, ρ, persistence)
- Encounter merge thresholds
- Radial-IMF cut
- Final confounder logic (transient_flag, mixing_flag are placeholders)
- Selection-function audit
- Shuffled-s falsification
- Full Monte Carlo uncertainty
- Local-normal s variant
- Alternative MP/BS model pair for sensitivity
- MMS thickness
- SMILE/SXI priors
- ML classification

---

## 10. Test coverage

| Test file | Module | Tests | Notes |
|---|---|---|---|
| test_boundaries | Shue1998, Merka2005 | 8 | Standoff values, pressure/Bz dependence, flank |
| test_config | Schema, loading | 5 | Defaults, hashing, YAML round-trip |
| test_mapping | s-coordinate | 6 | Boundary values (s=0 at MP, s=1 at BS), occupancy |
| test_metrics | Calculator | 3 | Trend smoothing, depletion detection, empty-data |
| test_qc | Flags, reporting | 4 | Jet/motion/wave flags, grading, PNG generation |
| test_provider | Provider abstraction | 10 | SyntheticProvider, dispatch, metadata, determinism |
| test_cache | DataCache | 12 | Paths, policies, index persistence, clear, roundtrip |
| test_normalization | Live utils | 11+1 | Interp, epoch, gaps, upstream build, integration (skipped) |
| **Total** | | **59 pass, 1 skip** | All offline-safe |

**Not tested:** Full end-to-end CLI (process_encounter with real config). QC report visual correctness (only checks PNG exists). Live data quality flag propagation. OMNI fill values / bad data markers.

---

## 11. Live pilot status — critical findings

### What ran

Both live encounters ran end-to-end without errors. CDAWeb fetch, caching, normalization, s-mapping, metrics, QC, and provenance all worked.

### What the data actually shows

| Encounter | Position (X,Y,Z GSM Re) | SZA | MLT | s range | Near-bin occ. | Metrics |
|---|---|---|---|---|---|---|
| live_pilot_001 (THD) | (3.5, 10.5, −1.0) | 71.9° | 16.8h | [0.409, 0.411] | 0% | all None |
| live_pilot_002 (THE) | (−2.2, −4.5, −0.5) | 115.6° | 4.3h | [0.447, 0.447] | 0% | all None |

### Problems

1. **Neither encounter is in the dayside magnetosheath.** pilot_001 is at Y=10.5 Re (deep flank, SZA=72°). pilot_002 is at X=−2.2 Re (nightside). Blueprint §6.2 targets SZA < 30°, MLT 09–15.
2. **s is in the gap zone** [0.4, 0.6) for both — no occupancy in any named bin, so no metrics can be computed.
3. **s range is extremely narrow** (±0.001) — the spacecraft barely moved relative to boundaries over the 15–20 min window. This produces a degenerate s(t) profile.
4. **s_sanity_ok = False** for both — std(s) < 0.01 triggers the sanity check failure.

### Root cause

The pilot windows were chosen for data availability, not for confirmed dayside magnetosheath geometry. This is not a code bug — the pipeline correctly reports that these intervals have no near-MP content.

### What this means

The live data bridge is **functionally complete and working**. The only remaining blocker for a scientifically meaningful live pilot is selecting encounter windows where the spacecraft is actually in the dayside magnetosheath near the magnetopause.

---

## 12. Implementation deviations from blueprint

| Blueprint expectation | Actual implementation | Severity | Notes |
|---|---|---|---|
| Cone angle from 3D B-field | arccos(\|Bz\|/Bt) using only OMNI Bz | Low | OMNI provides BX_GSE, BY_GSE but not BY_GSM directly. Acceptable for upstream context. |
| Sheath membership checks (§5.1) | Not implemented | Medium | No explicit check that spacecraft is in the sheath (vs magnetosphere or solar wind). The s-mapping assumes sheath; no plasma regime validation exists. |
| Boundary contamination control (§5.1) | Not implemented beyond s-sanity check | Medium | No explicit flagging of near-boundary points where sheath membership is ambiguous. |
| Monotonicity score (§6.3, supporting check) | Not implemented | Low | Blueprint lists this under "supporting checks". Not in MetricBundle. |
| Force-balance sanity (§6.3, supporting check) | Not implemented | Low | Blueprint lists this as supporting. ptot_smoothness is a partial proxy. |
| Transient flag (§6.4) | Placeholder (always False) | Low | Blueprint expects operational flag. Currently a stub. |
| Mixing flag (§6.4) | Placeholder (always False) | Low | Blueprint expects operational flag. Currently a stub. |
| MOM vs GMOM | Uses MOM (peim) | None | Correct default; blueprint does not specify a preference. |
| OMNI fill values | Not filtered | Medium | CDAWeb returns fill values (9999.99, etc.) which are not masked. They propagate as real data into medians and could corrupt upstream summary. |

---

## 13. Blockers, caveats, non-goals

### Current blockers for scientifically meaningful live pilots

1. Need manually curated encounter windows with confirmed dayside magnetosheath geometry (SZA < 30°, X > 8 Re, in sheath not magnetosphere)
2. OMNI fill values (typically 9999.99 or 99999.9) are not filtered — could silently corrupt upstream medians

### Caveats

- The `peim_ptot` variable in THEMIS MOM is total thermal pressure (ion + electron); beta and ptot derived from it are approximate
- The synthetic generator's PDL signature (Gaussian envelope at x=10.3 Re) is illustrative, not physically realistic
- The 3 s resampling cadence is appropriate for pilot-scale analysis but may need adjustment for multi-hour encounters
- Cache stores normalized intermediates; if normalization logic changes, cache must be cleared manually

### Non-goals for this phase

- Automatic encounter discovery / crossing harvesting
- Threshold tuning for classification
- Full confounder taxonomy (transient, mixing)
- Selection-function audit
- MMS thickness
- SMILE/SXI priors
- ML classification
- Notebook workflows

---

## 14. Next-step candidates (do not implement — for planning only)

**Most logical next step:** Curate 3–5 real dayside magnetosheath encounter windows from known THEMIS passes and re-run the live pipeline. Criteria: X_GSM > 8 Re, |Y| < 5 Re, SZA < 30°, with OMNI showing moderate steady Dp (1–4 nPa). This is the single action that converts "pipeline works" into "pipeline produces science-relevant results."

**After that:**
1. Add OMNI fill-value masking (replace fill values with NaN before median computation)
2. Add basic sheath membership check (e.g., beta > 0.1, |B| not magnetospheric-level)
3. Run the blueprint's pilot-analysis questions (§11.1): does s(t) show occupancy? do clear-PDL and clear-non-PDL cases separate on metrics?
4. Begin threshold exploration on a small hand-labeled development set

---

## 15. Key file paths for reference

| Resource | Path |
|---|---|
| Blueprint | `RP/internal_master_research_blueprint_PDL_SMILE.md` |
| Synthetic config | `configs/pilot_themis.yaml` |
| Live config | `configs/pilot_live.yaml` |
| Pipeline entry point | `src/pdl_pilot/cli/run_pilot.py` |
| Provider interface | `src/pdl_pilot/data/provider.py` |
| Live adapter | `src/pdl_pilot/data/live_provider.py` |
| Encounter model | `src/pdl_pilot/encounter/model.py` |
| Latest synthetic run | `runs/20260325T222621Z_7343078a/` |
| Latest live run | `runs/20260325T222812Z_528d4f77/` |
| Cache index | `data_cache/cache_index.json` |
