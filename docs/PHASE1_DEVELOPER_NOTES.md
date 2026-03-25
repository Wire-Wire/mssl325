# PDL Pilot — Phase 1 Developer Notes

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

## What Phase 1 explicitly does NOT include

- Full catalogue pipeline or batch processing
- Threshold tuning campaign or classification decisions
- Full confounder taxonomy (only simple flag placeholders)
- Selection-function audit (beyond interface placeholders)
- Shuffled-s falsification
- MMS thickness calculations
- SMILE/SXI mission-facing priors
- Machine learning
- Large notebook workflows

## How to run the pilot

```bash
# From the project root:
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_themis.yaml
```

## How to run tests

```bash
PYTHONPATH=src python -m pytest tests/ -v
```

## What files are produced (per run)

Each run creates `runs/<timestamp>_<run_id>/` containing:

| File | Content |
|------|---------|
| `config_used.yaml` | Frozen copy of the config that drove this run |
| `run_manifest.json` | Provenance: run_id, config hash, git commit, packages, timestamps |
| `run.log` | Full structured log |
| `encounter_<id>.json` | Per-encounter summary (metadata, upstream, mapping, metrics, QC) |
| `qc_<id>.png` | 6-panel diagnostic figure |
| `all_encounters.json` | Combined encounter summaries |

## Package structure

```
src/pdl_pilot/
  config/         — YAML config schema (Pydantic) + loader
  provenance/     — Run ID, config freeze, manifest, logging setup
  data/           — Data adapters (synthetic generator; live adapter = TODO)
  encounter/      — Encounter data model (the statistical unit)
  boundaries/     — Shue 1998 MP model, Merka 2005 BS model
  mapping/        — Normalized s-coordinate computation + bin occupancy
  metrics/        — PDL detector metric calculator
  qc/             — QC flag computation + report generation
  cli/            — Command-line entry point
```

## Decision status

### Frozen choices (Phase 1)
- Encounter is the statistical unit, not the raw crossing
- Normalized s = d_MP / (d_MP + d_BS) as spatial backbone
- Shue 1998 as baseline magnetopause model
- Merka 2005 (Farris-Russell form) as baseline bow-shock model
- Dual near bins: very-near [0.0, 0.2] and near [0.2, 0.4]
- IMF-agnostic detection (no upstream input to detector)
- Robust statistics (medians/quantiles) for metrics

### Provisional choices (confirm with pilot data)
- Distance along Sun-Earth line (local-normal variant deferred)
- Trend extraction via running median with 120 s window
- Simple perturbation envelope for s-uncertainty (±0.5 Re MP, ±1.0 Re BS)
- Jet flag threshold (Pdyn > 2× median)
- Wave flag threshold (relative fluctuation > 0.3)

### Deferred / open decisions
- Classification thresholds for Dn, EB, delta-beta, etc.
- Local-normal s variant
- Full Monte Carlo uncertainty propagation
- OMNI data quality filtering details
- Development set curation and threshold tuning
- Gold/Silver/Bronze grading criteria refinement
- Live THEMIS data adapter (requires pyspedas)
- Full confounder taxonomy

## Literature anchors used in code

| Module | Key references |
|--------|---------------|
| Boundary models | shue1998, merka2005 |
| Measurement model | lin2024, aghabozorgi2024, walsh2019, vokhmyanin2019 |
| Detector semantics | zwan1976, crooker1979, anderson1997, wang2004 |
| QC / confounders | archer2013, soucek2008, soucek2015, raptis2020, blancocano2023 |
| Provenance | sandve2013, steegen2016 |
