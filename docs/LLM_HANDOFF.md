# LLM Handoff — PDL Pilot Pipeline (Hardened + Science Curation)

**Load this first when resuming in a new session.**

---

## One-line summary

Phase 1.5 hardened + curation workflow: first real dayside THEMIS encounters (THD Oct 2008, X~10 Re, SZA~23°, 100% sheath membership) run end-to-end, but all real pilots have 0% background-bin occupancy because the spacecraft stays deep in the inner sheath (s~0.1–0.24) — need wider radial traversal or full-orbit windows.

## Current milestone

- Phase 1 (synthetic MVP): **done**
- Phase 1.5 (dual-source bridge): **done**
- Phase 1.5 hardening (honest science interface): **done**
- Science pilot curation + first real runs: **done, with caveats**
- Phase 2 (threshold tuning, dev set): **not started**

## What this phase added

1. **Candidate manifest** (`configs/pilot_candidates.yaml`): verified dayside windows from THEMIS-D Oct 2008 and Jul 2008, positions confirmed from STATE L1 ephemeris.
2. **Validation CLI** (`src/pdl_pilot/cli/validate_candidates.py`): validates candidates through full pipeline, scores each for promotion, produces JSON/CSV/markdown summaries.
3. **Science pilot config** (`configs/pilot_live_science.yaml`): promoted windows with relaxed membership thresholds for low-Dp outer sheath.
4. **First real pilot results**: sci_oct13 (SZA=23°, 99.4% membership), sci_oct15 (SZA=23°, 100% membership). Both pass geometry+membership but fail occupancy (no background bin data).
5. **6 new curation tests** (102 total, all pass offline).

## What the real pilots show (honest)

| Window | SZA | Membership | s range | Near% | BG% | Metrics |
|---|---|---|---|---|---|---|
| sci_oct13 | 22.7° | 99.4% | 0.094–0.144 | 0% (all very_near) | 0% | None |
| sci_oct15 | 23.1° | 100% | 0.199–0.242 | 95.6% | 0% | None |

**Root cause**: spacecraft at ~10 Re stays in s < 0.25 for the entire 90-120 min window. Background bin (s > 0.6) requires being near the bow shock (~13 Re), which these passes don't reach. This is a real measurement-model insight, not a code bug.

## Single remaining blocker

**Background bin occupancy requires wider radial traversal.** Either:
1. Full-orbit windows (~6-12 hours) capturing both inbound and outbound legs
2. Passes where spacecraft traverses from outer sheath (near BS, ~13 Re) through inner sheath (near MP, ~10 Re) — requires apogee ~14 Re aimed at local noon

## Frozen decisions (unchanged)

Encounter unit, s-mapping formula, Shue/Merka boundaries, dual near bins, IMF-agnostic detection, detector backbone, QC structural, provenance-first.

## Provisional choices (updated)

- Membership min_density: 0.3 cm⁻³ (relaxed for low-Dp outer sheath)
- Membership min_fraction: 0.3 (relaxed)
- min_s_std: 0.005 (relaxed for narrow traversals)
- Curation promotion threshold: 5.0
- Window duration: 90-150 min (may need full orbit)

## Key files

| What | Where |
|---|---|
| Candidate manifest | `configs/pilot_candidates.yaml` |
| Validation CLI | `src/pdl_pilot/cli/validate_candidates.py` |
| Science pilot config | `configs/pilot_live_science.yaml` |
| Diagnostic live config | `configs/pilot_live.yaml` |
| Curation tests | `tests/test_curation.py` |
| Latest science run | `runs/20260326T010935Z_8be10664/` |

## Commands

```bash
# Candidate validation
PYTHONPATH=src python -m pdl_pilot.cli.validate_candidates --config configs/pilot_candidates.yaml

# Science pilot run
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live_science.yaml

# All tests (102 pass, 1 skip)
PYTHONPATH=src python -m pytest tests/ -v
```

## Next step (do not implement)

Find encounter windows where THD/THE radial position sweeps from ~13 Re (outer sheath, s~0.8) through ~10 Re (inner sheath, s~0.2) in a single pass. The existing Oct 2008 passes have the spacecraft sitting at ~10 Re the entire time. Seasons where orbit apogee reaches 13-14 Re near local noon would give the needed traversal. Alternatively, use the full ~24-hour orbit as one encounter to capture both legs.
