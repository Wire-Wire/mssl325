# THEMIS Archive Data Guide

> **Purpose:** Tell any LLM or human how to find and use the pre-built local THEMIS encounter cache. No CDAWeb fetch needed for anything in this cache.

---

## Where the data lives

```
data_cache/themis_archive/
├── raw_state/                 ← 1135 monthly STATE files (geometry)
│   └── {probe}_{year}_{month}.npz
├── encounters/                ← 6118 per-encounter JSONs (Dn/EB/QC)
│   └── {date}_{probe}.json
├── summary.json               ← Start here: global stats
├── retained_index.json        ← Only evaluable encounters, grouped by cone bin
├── encounter_index.json       ← All 6903 encounters (big file)
├── screened_index.json        ← All 6903 qualifying days with geometry
├── encounter_catalogue.csv    ← All 6903 as flat CSV
└── raw_state_index.json       ← STATE download manifest
```

## How to use it

**Start with `summary.json`** for global counts, then:

- **Need all retained encounters?** → `retained_index.json` (757 entries, grouped by cone bin)
- **Need a specific encounter?** → `encounters/{date}_{probe}.json` (e.g. `2017-08-15_tha.json`)
- **Need a flat table?** → `encounter_catalogue.csv` (6903 rows, all fields)
- **Need qualifying days only?** → `screened_index.json`
- **Need raw position data?** → `raw_state/{probe}_{year}_{month}.npz` (numpy arrays: times, x_re, y_re, z_re in Earth radii)

## Geometry screening criteria

```
X_GSM > 5 Re       (dayside)
SZA < 30°           (near-subsolar)
8 Re < r < 25 Re    (in magnetosheath, not inner magnetosphere or solar wind)
```

## What "retained" means

An encounter is retained if Dn and EB are both computable:
- Near-bin occupancy >= 5% (s in [0.2, 0.4])
- Background-bin occupancy >= 1% (s in [0.6, 1.0])
- Dn = median(density_near) / median(density_bg) is finite
- EB = median(|B|_near) / median(|B|_bg) is finite

## Coverage summary

| Metric | Value |
|---|---|
| Archive scope | THEMIS 2007-2025, all 5 probes, all 12 months |
| STATE files | 1135 |
| Qualifying days | 6903 |
| Retained (Dn/EB evaluable) | **757** |
| Disk size | ~1.6 GB |

## Retained by cone-angle bin

| Bin | Range | Count |
|---|---|---|
| quasi-radial | cone < 30° | **28** |
| low-cone | 30-45° | **89** |
| intermediate | 45-60° | **199** |
| perpendicular | > 60° | **441** |

## Retained by year × probe

| Year | THA | THB | THC | THD | THE | Total | QR | LC |
|---|---|---|---|---|---|---|---|---|
| 2007 | 15 | 12 | 10 | 10 | 9 | 56 | 2 | 8 |
| 2008 | 0 | 17 | 26 | 2 | 3 | 48 | 0 | 7 |
| 2009 | 9 | 8 | 15 | 4 | 3 | 39 | 3 | 2 |
| 2010 | 3 | — | — | 3 | 3 | 9 | 0 | 0 |
| 2013 | 2 | — | — | 3 | 2 | 7 | 0 | 0 |
| 2014 | 5 | — | — | 4 | 9 | 18 | 0 | 1 |
| 2015 | 16 | — | — | 11 | 10 | 37 | 0 | 2 |
| 2016 | 19 | — | — | 4 | 4 | 27 | 1 | 2 |
| 2017 | 23 | — | — | 10 | 30 | 63 | 5 | 15 |
| 2018 | 20 | — | — | 33 | 32 | 85 | 2 | 13 |
| 2019 | 17 | — | — | 24 | 25 | 66 | 3 | 4 |
| 2020 | 8 | — | — | 9 | 11 | 28 | 2 | 8 |
| 2021 | 15 | — | — | 16 | 15 | 46 | 6 | 6 |
| 2022 | 22 | — | — | 21 | 20 | 63 | 1 | 8 |
| 2023 | 25 | — | — | 24 | 23 | 72 | 0 | 6 |
| 2024 | 17 | — | — | 16 | 20 | 53 | 3 | 6 |
| 2025 | 17 | — | — | 23 | 0 | 40 | 0 | 1 |

QR = quasi-radial, LC = low-cone. THB/THC "—" = ARTEMIS (lunar orbit), not near-Earth after 2009.

Note: 2011-2012 have 0 retained (apogee too low for THA/THD/THE, THB/THC on ARTEMIS with no qualifying days under current geometry criteria).

## Dayside season by orbital cycle

THEMIS orbit precesses with ~8-9 year period:

| Cycle | Years | Peak months | THA/THD/THE apogee | Notes |
|---|---|---|---|---|
| 1 | 2007-2010 | Jul-Oct | 10-14 Re | All 5 probes near-Earth |
| gap | 2011-2015 | — | 1-6 Re | Apogee nightside |
| 2 | 2016-2019 | Aug-Nov | 7-13 Re | Only THA/THD/THE |
| gap | 2020-2024 | — | 1-5 Re | Apogee nightside |
| 3 | 2025+ | May-Aug | 10-11 Re | Ongoing |

THB/THC (ARTEMIS) contribute encounters in 2013-2015 and 2019-2024 from perigee passes, but these are fast flybys, not extended magnetosheath sojourns like the inner probes.

## Per-encounter JSON fields

Each file in `encounters/` contains:

```json
{
  "encounter_id": "2017-08-15_tha",
  "date": "2017-08-15",
  "year": 2017, "month": 8,
  "probe": "tha",
  "sza_deg": 12.3,
  "mlt": 11.8,
  "x_gsm_re": 10.5, "r_re": 11.2,
  "dp_nPa": 2.15, "bz_nT": -1.3, "ma": 9.4,
  "cone_deg": 25.1, "clock_deg": 145.2,
  "mp_standoff_re": 9.8, "bs_standoff_re": 12.6,
  "near_occ": 0.182, "bg_occ": 0.354,
  "Dn": 0.45, "EB": 2.13,
  "evaluable": true, "retained": true,
  "cone_bin": "quasi-radial",
  "qc_transition_cleanliness": "clean",
  "qc_disturbance": "undisturbed",
  "qc_boundary_motion": "stable",
  "omni_context_quality_note": "good",
  "boundary_uncertainty_note": "plausible",
  "n_points": 2160
}
```

## Quick-start recipes

**Get all quasi-radial encounters:**
```python
import json
with open('data_cache/themis_archive/retained_index.json') as f:
    ri = json.load(f)
qr = ri['by_cone_bin']['quasi-radial']  # list of 28 encounter dicts
```

**Get all retained as a DataFrame:**
```python
import pandas as pd
df = pd.read_csv('data_cache/themis_archive/encounter_catalogue.csv')
retained = df[df['retained'] == True]
```

**Load one encounter:**
```python
import json
with open('data_cache/themis_archive/encounters/2017-08-15_tha.json') as f:
    enc = json.load(f)
```

**Load STATE for a specific month:**
```python
import numpy as np
d = np.load('data_cache/themis_archive/raw_state/tha_2017_08.npz')
# d['times'] (unix seconds), d['x_re'], d['y_re'], d['z_re'] (Earth radii)
```
