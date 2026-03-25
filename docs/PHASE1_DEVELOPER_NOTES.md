# PDL Pilot — Developer Notes (Phase 1 + 1.5)

## What Phase 1 includes

A minimal, config-driven encounter pipeline (v0) that can process
1–2 THEMIS pilot encounters end-to-end and output:

- **Encounter-level data artifact** (JSON) with full metadata
- **Baseline s(t) mapping** with occupancy summary and sanity flags
- **Measurement-model metadata** (boundary model inputs/outputs, uncertainty envelope)
- **Minimal detector metrics** (Dn, EB, delta-beta, trend-scale anti-correlation,
  total-pressure smoothness, persistence, fluctuation amplitude)
- **Standardized QC report** (6-panel PNG with time series, s-mapping, metrics, flags)
- **Full run provenance** (frozen config, run manifest with git hash, packages, timestamps)

## What Phase 1.5 adds

Phase 1.5 extends the pipeline with a **dual-source data bridge** so the same
encounter-level pipeline runs in both synthetic and live THEMIS/OMNI mode:

- **DataProvider abstraction** (`data/provider.py`): base class + `EncounterData` container
  with source metadata for provenance
- **SyntheticProvider** (`data/synthetic_provider.py`): wraps the existing Phase-1
  generator behind the provider interface — synthetic fixtures remain first-class
- **LiveProvider** (`data/live_provider.py`): fetches real THEMIS FGM/MOM/STATE + OMNI
  1-min data from CDAWeb via `cdasws`, normalizes onto a common analysis timeline
- **DataCache** (`data/cache.py`): local file-based cache for raw CDF downloads and
  normalized intermediates, with deterministic paths, hit/miss reporting, and index
- **Extended config** (`config/schema.py`): `LiveDataConfig` for backend, dataset IDs,
  OMNI window, resampling tolerances, cache policy
- **Extended provenance** (`provenance/tracker.py`): manifests now include per-encounter
  source metadata (datasets, variables, probes, time ranges, cache hits, remote files)
- **Updated CLI** (`cli/run_pilot.py`): automatic provider dispatch based on
  `data_source` setting; computes upstream summary from OMNI for live runs
- **Live pilot config** (`configs/pilot_live.yaml`): 2 manually specified real encounter
  windows for pipeline validation

### What remains synthetic-only
- Pilot encounters in `configs/pilot_themis.yaml` always use synthetic data

### What is now live-capable
- Any encounter in a config with `data_source: "live"` will fetch real data

## What Phase 1.5 explicitly does NOT include

- Full catalogue pipeline or batch processing
- Automatic encounter discovery or crossing harvesting
- Threshold tuning campaign or classification decisions
- Full confounder taxonomy
- Selection-function audit
- MMS thickness calculations
- SMILE/SXI mission-facing priors
- Machine learning
- Notebook workflows

## How to run the synthetic pilot

```bash
# From the project root:
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_themis.yaml
```

## How to run the live pilot

```bash
# Install live dependencies first:
pip install cdasws cdflib

# Then:
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live.yaml
```

The live pilot will:
1. Fetch THEMIS FGM/MOM/STATE + OMNI from CDAWeb
2. Cache raw data in `data_cache/`
3. Normalize and resample onto a common timeline
4. Run the same encounter pipeline as synthetic
5. Record full source provenance in the run manifest

## How to run tests

```bash
PYTHONPATH=src python -m pytest tests/ -v
```

All tests run offline by default.  To enable live integration tests:
```bash
PDL_LIVE_TESTS=1 PYTHONPATH=src python -m pytest tests/ -v
```

## What files are produced (per run)

Each run creates `runs/<timestamp>_<run_id>/` containing:

| File | Content |
|------|---------|
| `config_used.yaml` | Frozen copy of the config that drove this run |
| `run_manifest.json` | Provenance: run_id, config hash, git commit, packages, timestamps, source metadata |
| `run.log` | Full structured log |
| `encounter_<id>.json` | Per-encounter summary (metadata, upstream, mapping, metrics, QC) |
| `qc_<id>.png` | 6-panel diagnostic figure |
| `all_encounters.json` | Combined encounter summaries |

For live runs, `run_manifest.json` additionally includes:
- `source_data`: per-encounter lists of `SourceMetadata` (datasets, variables, probes, time ranges, cache hit/miss, remote files)
- `cache_summary`: cache directory state (file counts, policy)

## Package structure

```
src/pdl_pilot/
  config/         — YAML config schema (Pydantic) + loader
                    Phase 1.5: LiveDataConfig for live source settings
  provenance/     — Run ID, config freeze, manifest, logging setup
                    Phase 1.5: source metadata + cache summary in manifest
  data/           — Data adapters
                    provider.py     — DataProvider ABC + EncounterData + SourceMetadata
                    synthetic.py    — Phase-1 synthetic generator (unchanged)
                    synthetic_provider.py — SyntheticProvider (wraps synthetic.py)
                    live_provider.py     — LiveProvider (CDAWeb/cdasws)
                    cache.py             — DataCache for local file caching
  encounter/      — Encounter data model (the statistical unit)
  boundaries/     — Shue 1998 MP model, Merka 2005 BS model
  mapping/        — Normalized s-coordinate computation + bin occupancy
  metrics/        — PDL detector metric calculator
  qc/             — QC flag computation + report generation
  cli/            — Command-line entry point (Phase 1.5: dual-source dispatch)
```

## Decision status

### Frozen choices (Phase 1, preserved in Phase 1.5)
- Encounter is the statistical unit, not the raw crossing
- Normalized s = d_MP / (d_MP + d_BS) as spatial backbone
- Shue 1998 as baseline magnetopause model
- Merka 2005 (Farris-Russell form) as baseline bow-shock model
- Dual near bins: very-near [0.0, 0.2] and near [0.2, 0.4]
- IMF-agnostic detection (no upstream input to detector)
- Robust statistics (medians/quantiles) for metrics
- Synthetic fixtures retained as first-class data source
- Real pilot windows are manually specified (not auto-discovered)
- Provenance-first run design

### Provisional choices (Phase 1.5 — confirm with pilot data)
- Distance along Sun-Earth line (local-normal variant deferred)
- Trend extraction via running median with 120 s window
- Simple perturbation envelope for s-uncertainty (±0.5 Re MP, ±1.0 Re BS)
- Jet flag threshold (Pdyn > 2× median)
- Wave flag threshold (relative fluctuation > 0.3)
- **Live backend: cdasws (CDAWeb REST API)**
- **Default plasma product: THEMIS MOM L2 (not GMOM)**
- **Resampling cadence: 3 s (linear interpolation)**
- **Max gap fill: 30 s (larger gaps → NaN)**
- **OMNI pre-window: 30 min before encounter start**
- **Cache layout: data_cache/{raw,normalized}/**
- **Pilot encounter windows (not vetted as confirmed PDL events)**

### Deferred / open decisions
- Classification thresholds for Dn, EB, delta-beta, etc.
- Local-normal s variant
- Full Monte Carlo uncertainty propagation
- OMNI data quality filtering details
- Development set curation and threshold tuning
- Gold/Silver/Bronze grading criteria refinement
- Full confounder taxonomy
- MMS thickness calculations
- SMILE/SXI mission-facing priors
- Selection-function audit
- Machine learning
- Final Sun–Earth-line vs local-normal default

## Literature anchors used in code

| Module | Key references |
|--------|---------------|
| Boundary models | shue1998, merka2005 |
| Measurement model | lin2024, aghabozorgi2024, walsh2019, vokhmyanin2019 |
| Detector semantics | zwan1976, crooker1979, anderson1997, wang2004 |
| QC / confounders | archer2013, soucek2008, soucek2015, raptis2020, blancocano2023 |
| Provenance | sandve2013, steegen2016 |
