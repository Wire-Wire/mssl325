# Local Paper Library — Canonical Naming Status

**Generated:** 2026-03-25T20:34:06.666844

## Summary
- Total papers: **37**
- Successfully renamed: **37**
- Papers with naming uncertainty: **0**

## Naming Scheme
```
YYYY_firstauthor_short-title-keywords
```
- All lowercase
- Underscores separate year, author, title blocks
- Hyphens connect words within the title-keyword block
- Title keywords ≤ 6 words, stop-words removed
- Example: `1998_shue_magnetopause-location-extreme-solar-wind`

## Recommended Reference Format for Prompts

When referencing a paper in a prompt (Claude Code / ChatGPT Pro):
```
Use the canonical basename directly, e.g.:
  1998_shue_magnetopause-location-extreme-solar-wind
  1976_zwan_solar-wind-plasma-depletion-planetary-boundary
  2024_aghabozorgi_magnetopause-location-ml-solar-wind-propagation
```

Short inline reference: `[shue1998]` or `[zwan1976]` for brevity,
with canonical basename as the authoritative key.

## Directory Structure
```
output/
  pdfs/          — canonical-named PDF copies
  json/          — structured JSON (canonical source)
  markdown/      — readable Markdown layer
  chunks/        — chunked JSON for retrieval
  index/         — mappings, manifest, this file
  scripts/       — processing scripts
  logs/          — processing logs
```

## Root PDF Policy
Original PDFs in the project root directory are **NOT renamed**.
Only `output/` copies use canonical names.
The mapping files provide full traceability from old → new names.

## Complete Paper List

| # | Canonical Basename | Year | Author | Confidence |
|---|-------------------|------|--------|------------|
| 1 | `1989_kunsch_jackknife-bootstrap-stationary-observations` | 1989 | kunsch | high |
| 2 | `2004_wang_pdl-magnetosheath-flow-structure-forces` | 2004 | wang | high |
| 3 | `2004_haaland_four-spacecraft-magnetopause-crossing-time` | 2004 | haaland | high |
| 4 | `2007_dekeyser_least-squares-gradient-multipoint-cluster` | 2007 | dekeyser | high |
| 5 | `2009_zhou_error-estimation-multi-spacecraft-timing` | 2009 | zhou | high |
| 6 | `2011_vogt_accuracy-multipoint-boundary-crossing-time` | 2011 | vogt | high |
| 7 | `2013_archer_magnetosheath-dynamic-pressure-enhancements` | 2013 | archer | high |
| 8 | `2024_lin_magnetopause-model-performance-themis` | 2024 | lin | high |
| 9 | `2023_jung_mshpy23-magnetosheath-parameterized-model` | 2023 | jung | high |
| 10 | `2013_sandve_ten-rules-reproducible-computational-research` | 2013 | sandve | high |
| 11 | `2024_aghabozorgi_magnetopause-location-ml-solar-wind-propagation` | 2024 | aghabozorgi | high |
| 12 | `2024_pi_magnetosheath-spatial-profiles-imf-themis` | 2024 | pi | high |
| 13 | `2024_michottedewelle_magnetosheath-density-field-imf-orientation` | 2024 | michottedewelle | high |
| 14 | `2003_robertson_xray-emission-terrestrial-magnetosheath` | 2003 | robertson | high |
| 15 | `2024_grimmich_magnetopause-deviation-solar-wind-foreshock` | 2024 | grimmich | high |
| 16 | `2015_soucek_magnetosheath-plasma-stability-ulf-waves` | 2015 | soucek | high |
| 17 | `2017_rezeau_magnetopause-internal-structure-mms` | 2017 | rezeau | high |
| 18 | `2018_denton_lmn-current-sheet-coordinates-magnetopause` | 2018 | denton | high |
| 19 | `2019_sun_soft-xray-imaging-magnetosheath-cusps-mhd` | 2019 | sun | high |
| 20 | `2019_walsh_solar-wind-measurement-uncertainty-geospace` | 2019 | walsh | high |
| 21 | `2020_raptis_classifying-magnetosheath-jets-mms` | 2020 | raptis | high |
| 22 | `2020_staples_statistical-models-magnetopause-compressions` | 2020 | staples | high |
| 23 | `2025_jiang_ion-kinetic-instabilities-magnetosheath-mms` | 2025 | jiang | high |
| 24 | `2023_blancocano_jets-mirror-mode-waves-magnetosheath` | 2023 | blancocano | high |
| 25 | `1976_zwan_solar-wind-plasma-depletion-planetary-boundary` | 1976 | zwan | high |
| 26 | `1994_anderson_magnetic-spectral-signatures-magnetosheath-pdl` | 1994 | anderson | high |
| 27 | `1979_crooker_plasma-depletion-observations-dayside-magnetopause` | 1979 | crooker | high |
| 28 | `1997_anderson_plasma-depletion-subsolar-reconnection` | 1997 | anderson | high |
| 29 | `1998_shue_magnetopause-location-extreme-solar-wind` | 1998 | shue | high |
| 30 | `2005_king_solar-wind-spatial-scales-wind-ace-omni` | 2005 | king | high |
| 31 | `2005_merka_bow-shock-3d-position-shape-mach-number` | 2005 | merka | high |
| 32 | `2008_soucek_magnetosheath-mirror-modes-cluster` | 2008 | soucek | high |
| 33 | `2009_li_cold-dense-magnetopause-boundary-northward-imf` | 2009 | li | high |
| 34 | `2009_plaschke_magnetopause-motion-statistical-study-themis` | 2009 | plaschke | high |
| 35 | `2022_zhang_dayside-transient-phenomena-magnetosphere-ionosphere` | 2022 | zhang | high |
| 36 | `2019_vokhmyanin_omni-imf-data-quality-evaluation` | 2019 | vokhmyanin | high |
| 37 | `2016_steegen_multiverse-analysis-transparency` | 2016 | steegen | high |

## Uncertainties
None — all 37 papers have high-confidence naming.
