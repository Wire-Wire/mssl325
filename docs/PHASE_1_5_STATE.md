# Phase 1.5 State Document — PDL Pilot Pipeline (Hardened)

**Date:** 2026-03-26
**Repo:** `mssl325` (branch: `main`)
**Package:** pdl-pilot v0.1.0, Python >= 3.10

---

## 1. Project mainline

This project builds a controlled THEMIS dayside PDL detection pipeline. The central question is whether a boundary-adjacent, layer-like density depletion can be isolated in THEMIS magnetosheath data after explicit coordinate control, confounder handling, and selection-function audit — and then translated into compact mission-facing priors for SMILE/SXI.

The blueprint (RP/internal_master_research_blueprint_PDL_SMILE.md) defines four problem layers: physics, measurement, engineering/audit, and mission translation. Phase 1 built the engineering skeleton. Phase 1.5 bridged it to real data. Phase 1.5 hardening makes the science interface honest.

---

## 2. Phase 1.5 hardening — what changed

This is a diagnostic hardening pass, NOT Phase 2. The goal is to ensure the pipeline is honest about data validity and encounter evaluability before any scientific conclusions.

### Changes made

| Area | What changed |
|---|---|
| **Fill-value masking** | New `data/masking.py` module. OMNI sentinel values (9999.99, 99.99, etc.) and CDF fill values (±1e31) are now replaced with NaN before any computation. Priority: attrs-based > known table > generic fallback. Per-variable masking summaries logged and recorded in provenance. |
| **Scientific preflight** | New `qc/preflight.py` module. Every encounter is evaluated for geometry (SZA, X_GSM, Y_GSM), data validity, sheath membership, bin occupancy, and s-sanity BEFORE metrics are interpreted. Status categories: PASS, FAIL_GEOMETRY, FAIL_DATA_VALIDITY, FAIL_MEMBERSHIP, FAIL_OCCUPANCY, FAIL_S_SANITY, REVIEW_NEEDED. |
| **Sheath membership** | Conservative validator in preflight: flags upstream-suspect (low n/B), magnetosphere-suspect (very low beta + high B), artifact-suspect (extreme values), and unknown (NaN) points. Not a full region classifier. |
| **Cone angle** | Corrected to arccos(\|Bx\|/\|B\|) using radial component (BX_GSE from OMNI), not arccos(\|Bz\|/\|B\|). Clock angle corrected to arctan2(By_GSM, Bz_GSM). If Bx or By unavailable, angles are honestly None. OMNI fetch now includes BX_GSE and BY_GSM. |
| **Tri-state QC flags** | Flags are now True/False/None (UNKNOWN). transient_flag and mixing_flag are honestly None (not implemented), not False. Grade logic respects unknowns: with default "cap_silver" policy, max grade is Silver when any flag is UNKNOWN. |
| **Config hardening knobs** | New `PreflightConfig` section with all preflight thresholds, fill masking policy, and grading policy. All PROVISIONAL. |
| **Encounter output** | JSON now includes: scientific_status, evaluable, evaluable_metrics, preflight_checks, preflight_reasons, membership_summary, masked_fraction_summary. |
| **QC report** | 6-panel PNG now shows STATUS/evaluable header, tri-state flag display, grade notes, and preflight reasons. |
| **Live config** | Windows explicitly marked DIAGNOSTIC ONLY / SCIENTIFICALLY INELIGIBLE with known geometry issues documented. |
| **Tests** | 37 new tests (96 total + 1 skipped). Covers masking, cone/clock angle, preflight, membership, tri-state flags, schema, e2e. |

---

## 3. Acceptance status

| Criterion | Status |
|---|---|
| Synthetic pilot path still works | **PASS** — Dn=0.949, EB=1.054, status=PASS, evaluable=True |
| Tests pass offline | **PASS** — 96 passed, 1 skipped |
| Fill values no longer silently enter boundary models/metrics | **PASS** — OMNI sentinels masked with per-variable summaries |
| Cone angle computed correctly | **PASS** — uses Bx (radial), not Bz; tested at 0°/45°/90° |
| Encounters have explicit scientific status | **PASS** — PASS/FAIL_GEOMETRY/etc. |
| Metrics not reported as meaningful when not evaluable | **PASS** — evaluable_metrics list controls interpretation |
| Confounder flags honest about unknowns | **PASS** — transient/mixing are None, grade capped |
| Grading honest about incomplete coverage | **PASS** — "cap_silver" policy + grade_note |
| Outputs expose validity/evaluability info | **PASS** — JSON has full preflight + membership + masking data |
| Docs updated | **PASS** |
| At least one real pilot evaluable | **NOT POSSIBLE** — current windows not dayside (see §11) |

---

## 4. Repo architecture

```
src/pdl_pilot/
  config/
    schema.py          — Pydantic config: +PreflightConfig (new)
  data/
    provider.py        — DataProvider ABC, EncounterData (+omni_bx_gse, +omni_by_gsm)
    synthetic.py       — Phase-1 synthetic generator
    synthetic_provider.py — SyntheticProvider
    live_provider.py   — LiveProvider: +BX_GSE, +BY_GSM fetch
    cache.py           — DataCache
    masking.py         — Fill-value masking (NEW)
  encounter/
    model.py           — Encounter (+scientific_status, +evaluable, +preflight fields)
                         QCFlags (tri-state: True/False/None, +grade_note)
  boundaries/          — shue1998.py, merka2005.py (unchanged)
  mapping/             — s_mapper.py (unchanged)
  metrics/             — calculator.py (unchanged)
  qc/
    reporter.py        — compute_qc_flags (tri-state + grade policy), generate_qc_report (updated)
    preflight.py       — Scientific preflight + sheath membership (NEW)
  provenance/          — tracker.py (unchanged)
  cli/
    run_pilot.py       — Pipeline with fill masking, preflight, corrected upstream, grade policy

configs/
  pilot_themis.yaml    — Synthetic pilot (+run_label v1_hardened)
  pilot_live.yaml      — Live pilot (windows marked INELIGIBLE, +preflight config)

tests/
  test_hardening.py    — 37 new tests (masking, angles, preflight, membership, tri-state, e2e)
  (all existing tests updated and passing)
```

---

## 5. Measurement model implementation

Unchanged from Phase 1.5 except:
- **Cone angle**: now correctly `arccos(|Bx_GSE|/|B|)` — angle between IMF and Sun-Earth line
- **Clock angle**: now correctly `arctan2(By_GSM, Bz_GSM)` — orientation in the Y-Z plane
- Both return None (not fake values) when upstream components unavailable

---

## 6. Scientific preflight checks

| Check | Criterion | Default threshold | Failure status |
|---|---|---|---|
| geometry_x | X_GSM >= min | 5.0 Re | FAIL_GEOMETRY |
| geometry_y | \|Y_GSM\| <= max | 15.0 Re | FAIL_GEOMETRY |
| geometry_sza | SZA <= max | 60.0° | FAIL_GEOMETRY |
| data_* | valid fraction >= min | 0.5 | FAIL_DATA_VALIDITY |
| membership | sheath fraction >= min | 0.5 | FAIL_MEMBERSHIP |
| occupancy_near | near-bin fraction >= min | 0.02 | FAIL_OCCUPANCY |
| occupancy_bg | bg-bin fraction >= min | 0.02 | FAIL_OCCUPANCY |
| s_sanity | std(s) >= min | 0.01 | FAIL_S_SANITY |

**Key design principle**: A FAIL_GEOMETRY or FAIL_OCCUPANCY encounter is NOT a scientific negative. It is *not evaluable*. This distinction is structural.

---

## 7. QC tri-state flags

| Flag | Implementation status | Values |
|---|---|---|
| jet_flag | Implemented | True / False / None (no velocity data) |
| wave_flag | Implemented | True / False / None (no trend data) |
| motion_flag | Implemented | True / False |
| transient_flag | NOT IMPLEMENTED | Always None |
| mixing_flag | NOT IMPLEMENTED | Always None |

### Grading policy

| Policy | Behavior |
|---|---|
| cap_silver | Max grade = Silver if any flags UNKNOWN. Default. |
| preliminary | Grade prefixed with "Preliminary-" |
| ungraded | Grade = "ungraded" if any UNKNOWN |

---

## 8. Config decision status

### Frozen

- Encounter is the statistical unit
- s = d_MP/(d_MP+d_BS) as spatial backbone, Sun-Earth line
- Shue 1998 MP + Merka 2005 BS baseline
- Dual near bins: [0.0,0.2] + [0.2,0.4], primary = [0.2,0.4]
- IMF-agnostic detection
- Detector backbone: Dn, EB, delta_beta, rho(n,B), persistence
- QC flags + grading are structural
- Synthetic fixtures retained
- Real pilot windows manually specified
- Provenance-first

### Provisional (new in hardening)

- Preflight geometry thresholds (SZA=60°, X>5 Re, |Y|<15 Re)
- Sheath membership thresholds (density 0.5-200, B 1-200, beta 0.01-100)
- Min valid fraction (0.5)
- Min bin occupancy (2%)
- Fill masking policy (auto)
- Grading policy (cap_silver)
- Cone angle correctness (depends on BX_GSE availability in OMNI)
- OMNI window (30 min pre, 10 min post)
- Resampling cadence (3 s)

### Deferred

- Detector thresholds, encounter merge, radial-IMF cut, shuffled-s falsification
- Selection-function audit, full confounder taxonomy
- Local-normal s, alternative MP/BS pair, Monte Carlo uncertainty
- MMS thickness, SMILE/SXI priors, ML classification

---

## 9. Test coverage

| Test file | Tests | New |
|---|---|---|
| test_boundaries | 8 | — |
| test_config | 5 | — |
| test_mapping | 6 | — |
| test_metrics | 3 | — |
| test_qc | 4 | 1 updated |
| test_provider | 10 | — |
| test_cache | 12 | — |
| test_normalization | 11+1 skip | — |
| **test_hardening** | **37** | **ALL NEW** |
| **Total** | **96 pass, 1 skip** | |

---

## 10. Live pilot status

Both current windows are SCIENTIFICALLY INELIGIBLE:

| Encounter | Position | SZA | Status |
|---|---|---|---|
| live_pilot_001 (THD) | Y=10.5 Re (deep flank) | 72° | FAIL_GEOMETRY |
| live_pilot_002 (THE) | X=−2.2 Re (nightside) | 116° | FAIL_GEOMETRY |

The live data bridge is functionally complete. The ONLY remaining blocker for science-relevant live pilots is manual curation of dayside encounter windows.

---

## 11. Implementation deviations from blueprint

| Blueprint | Implementation | Status |
|---|---|---|
| Cone angle from 3D B | Uses BX_GSE (radial), correct in spirit | **FIXED** |
| Sheath membership checks (§5.1) | Conservative validator implemented | **FIXED** |
| transient_flag | Still None (not implemented) | **HONEST** |
| mixing_flag | Still None (not implemented) | **HONEST** |
| Monotonicity score (§6.3) | Not implemented | Low priority |
| Force-balance sanity (§6.3) | ptot_smoothness is partial proxy | Low priority |
| OMNI fill values | Masked with per-variable table | **FIXED** |

---

## 12. Next step candidates (do not implement)

**Most logical next step**: Curate 3-5 real dayside THEMIS encounter windows (X>8 Re, |Y|<5 Re, SZA<30°, steady Dp) and run them through the hardened pipeline. This is the single action that converts "pipeline is honest" into "pipeline produces science-relevant results."

---

## 13. Key commands

```bash
# Synthetic pilot
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_themis.yaml

# Live pilot (diagnostic, windows are ineligible)
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live.yaml

# Tests
PYTHONPATH=src python -m pytest tests/ -v
```
