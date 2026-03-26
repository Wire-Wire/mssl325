# LLM Handoff — PDL Pilot Pipeline (Hardened)

**Load this first when resuming in a new session.**

---

## One-line summary

Phase 1.5 hardened: THEMIS PDL detection pipeline now enforces fill-value masking, scientific eligibility preflight, sheath-membership checks, correct IMF cone angle, and honest tri-state QC grading — but the live pilot windows are still not dayside encounters, so the data bridge works but no science-grade live results exist yet.

## Current milestone

- Phase 1 (synthetic MVP): **done**
- Phase 1.5 (dual-source bridge): **done**
- Phase 1.5 hardening (honest science interface): **done**
- Phase 2 (threshold tuning, development set, catalogue): **not started**

## What the hardening pass added

1. **Fill-value masking** (`data/masking.py`): OMNI sentinels (9999.99 etc.) and CDF fills (±1e31) → NaN. Per-variable summaries in provenance.
2. **Scientific preflight** (`qc/preflight.py`): geometry + data validity + sheath membership + bin occupancy + s-sanity → explicit PASS/FAIL_GEOMETRY/FAIL_OCCUPANCY/etc. Failed = not evaluable, NOT a scientific negative.
3. **Sheath membership**: conservative validator (density/B/beta ranges). Flags upstream-suspect, magnetosphere-suspect, artifact, unknown.
4. **Correct cone angle**: arccos(|Bx|/|B|) using OMNI BX_GSE, not Bz. Clock angle: arctan2(By_GSM, Bz_GSM). None if unavailable.
5. **Tri-state QC flags**: True/False/None. transient and mixing are honestly None. Grade capped to Silver max when flags UNKNOWN.
6. **Config knobs**: PreflightConfig with all preflight thresholds, fill policy, grade policy.
7. **Encounter output**: scientific_status, evaluable, evaluable_metrics, preflight_checks, membership_summary, masked_fraction_summary.
8. **37 new tests** (96 total, all passing offline).

## Frozen decisions (do not reopen)

- Encounter (not crossing) is the statistical unit
- `s = d_MP / (d_MP + d_BS)` normalized coordinate, Sun-Earth line
- Shue 1998 (MP) + Merka 2005 (BS) as baseline boundary models
- Dual near bins: [0.0,0.2] fragile + [0.2,0.4] primary, background [0.6,1.0]
- IMF-agnostic detection (upstream enters post-detection only)
- Detector backbone: Dn, EB, delta_beta, trend-scale rho(n,|B|), persistence
- QC flags + grading are structural, not optional
- Provenance-first design
- Scientific preflight is mandatory (encounters must be explicitly evaluable)
- Not-evaluable != negative (structural distinction)

## Provisional choices (all configurable)

- Preflight thresholds: SZA < 60°, X > 5 Re, |Y| < 15 Re (relaxed from blueprint's <30°)
- Sheath membership: density 0.5-200 cm-3, B 1-200 nT, beta 0.01-100
- Min valid fraction: 0.5, min bin occupancy: 2%
- Fill masking policy: "auto" (attrs > table > generic)
- Grade policy: "cap_silver" (max Silver when flags UNKNOWN)
- Backend: cdasws, MOM L2 (peim), 3s cadence, 30s max gap, 30min OMNI pre-window

## Deferred decisions (do not implement)

- Detector thresholds, encounter merge, radial-IMF cut
- Local-normal s, alternative MP/BS pair, Monte Carlo uncertainty
- Shuffled-s falsification, selection-function audit
- Full confounder taxonomy (transient, mixing implementations)
- MMS thickness, SMILE/SXI priors, ML classification

## Top 5 risks / gaps

1. **Live pilot windows still not dayside.** pilot_001: SZA=72°, Y=10.5 Re. pilot_002: X=-2.2 Re. Both produce FAIL_GEOMETRY. Pipeline correctly rejects them.
2. **Cone/clock angle require BX_GSE and BY_GSM from OMNI.** Old cached data may not contain these variables — cache clear needed for live reruns.
3. **transient_flag and mixing_flag still None.** This caps all grades to Silver max. Implementing these requires physics understanding beyond Phase 1.5.
4. **Preflight thresholds are relaxed.** SZA < 60° (not blueprint's target 30°) to allow more pilots. Will need tightening for science catalogue.
5. **Sheath membership is conservative.** Only rejects obvious non-sheath. A magnetospheric interval with moderate beta might still pass. Phase 2 should improve this.

## Next incremental tasks (priority order)

1. **Curate 3-5 real dayside encounter windows** (X>8 Re, |Y|<5 Re, SZA<30°). This is the ONLY blocker for science-relevant live results.
2. **Clear live data cache** (old OMNI data lacks BX_GSE/BY_GSM) and rerun live pilots.
3. **Run blueprint pilot-analysis questions** (§11.1) on evaluable encounters.
4. **Begin development-set construction** for threshold exploration.
5. **Implement transient/mixing flags** to enable full Gold grading.

## Key files

| What | Where |
|---|---|
| Blueprint | `RP/internal_master_research_blueprint_PDL_SMILE.md` |
| Full state doc | `docs/PHASE_1_5_STATE.md` |
| Pipeline entry | `src/pdl_pilot/cli/run_pilot.py` |
| Fill masking | `src/pdl_pilot/data/masking.py` |
| Preflight | `src/pdl_pilot/qc/preflight.py` |
| Encounter model | `src/pdl_pilot/encounter/model.py` |
| Config schema | `src/pdl_pilot/config/schema.py` |
| Synthetic config | `configs/pilot_themis.yaml` |
| Live config | `configs/pilot_live.yaml` |
| Hardening tests | `tests/test_hardening.py` |

## Commands

```bash
# Synthetic pilot
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_themis.yaml

# Live pilot (diagnostic only — windows are ineligible)
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live.yaml

# Tests (96 pass, 1 skip, all offline-safe)
PYTHONPATH=src python -m pytest tests/ -v
```

## Repo stats

- 96 offline-safe tests passing (37 new for hardening)
- 2 configs (synthetic + live)
- Dependencies: numpy, scipy, matplotlib, pydantic, pyyaml + optional cdasws, cdflib
