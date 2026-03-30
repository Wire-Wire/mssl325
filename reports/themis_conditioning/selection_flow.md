# Phase 6A Selection Flow

**Declared slice:** All locally cached evaluable THEMIS encounters across all run directories.

## Universe

| Step | Count | Note |
|---|---|---|
| Total encounter JSONs in runs/ | 78 | Multiple runs, many duplicates |
| Unique encounters (deduplicated by date+probe) | 11 | Preferred usable_ prefix versions |
| Evaluable with valid Dn | 11 | All passed preflight in their original runs |

## Inclusion screens applied

| Screen | Rule | Excluded |
|---|---|---|
| Near-subsolar | SZA ≤ 30° | 0 |
| Upstream data quality | OMNI cone/clock available | 0 |
| Near-bin occupancy | ≥ 5% | 0 |
| Background-bin occupancy | ≥ 1% | 0 |
| Membership | ≥ 50% | 0 |

**Total retained: 11. Total excluded: 0.**

All 11 locally cached evaluable encounters pass the Phase 6A inclusion screens.

## Screens NOT applied (by design)

- Cone angle / radiality: variable of interest, not inclusion filter
- Clock angle / Bz sign: variable of interest, not inclusion filter
- Dp > 3 nPa: inherited Phase 4B bank preference, NOT a Phase 6A filter
- Non-quasi-radial: Phase 5A sidecar filter, NOT inherited into Phase 6A

## Inherited structural biases (carried forward, not corrected)

- THD-dominated (9 of 11 are THD; 2 are THE/THD-2010)
- Compressed-sheath-biased (all encounters have Dp ≥ 2.8 nPa)
- Two seasons only (2008 + 2009 dominate; one 2010, one 2012, one 2013)
- Single inner-probe apogee (~11.6 Re)
