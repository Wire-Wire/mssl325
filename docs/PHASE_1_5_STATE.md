# Phase 1.5 State Document — PDL Pilot Pipeline (Hardened + Science Curation)

**Date:** 2026-03-26
**Repo:** `mssl325` (branch: `main`)
**Package:** pdl-pilot v0.1.0, Python >= 3.10

---

## 1. Current state in one sentence

Phase 1.5 hardened pipeline with candidate curation workflow: first real dayside THEMIS encounters (THD Oct 2008, X~10 Re, SZA~23°) run end-to-end with 100% sheath membership and near-bin occupancy, but background-bin occupancy remains zero because the orbital geometry keeps the spacecraft entirely within s < 0.4 during these passes.

---

## 2. What exists now

### Completed
- Synthetic dual-source pipeline (Phase 1)
- Live CDAWeb data bridge (Phase 1.5)
- Fill-value masking, scientific preflight, sheath membership, corrected angles, tri-state QC (Phase 1.5 hardening)
- Candidate-window curation manifest and validation workflow (this phase)
- Science-pilot config with verified dayside geometry windows

### First real pilot results (honest)

| Encounter | Position | SZA | Membership | Near occ. | BG occ. | Status |
|---|---|---|---|---|---|---|
| sci_oct13 (THD) | (9.8, -4.1, 0.0) Re | 22.7° | 99.4% | 0% (all very_near) | 0% | FAIL_OCCUPANCY |
| sci_oct15 (THD) | (9.6, -4.1, 0.1) Re | 23.1° | 100% | 95.6% | 0% | FAIL_OCCUPANCY |

**Key insight**: These are real dayside magnetosheath windows with correct geometry and sheath-like plasma. The occupancy failure is because the spacecraft stays at s~0.1-0.24 (very-near + near), never reaching the background zone (s>0.6). This is a physical limitation of the orbital geometry for 1-2 hour windows — the spacecraft orbital motion doesn't traverse enough radial distance to span the full sheath.

### What this means for the measurement model
The dual-bin design (blueprint §5.3) requires both near AND background occupancy for meaningful Dn, EB, delta_beta. The current windows demonstrate that near-subsolar passes at ~10 Re stay deep in the inner sheath. To populate both bins, either:
1. Use much longer encounter windows (full orbit: ~6-12 hours) to capture the inbound-to-outbound traversal
2. Or find passes where the spacecraft crosses from outer sheath (near BS) through to inner sheath (near MP) within a shorter interval

---

## 3. Repo architecture

```
src/pdl_pilot/
  cli/
    run_pilot.py               — Main pipeline (unchanged)
    validate_candidates.py     — NEW: candidate validation + promotion workflow
  (all other modules unchanged from Phase 1.5 hardening)

configs/
  pilot_themis.yaml            — Synthetic pilot
  pilot_live.yaml              — Diagnostic live (known-ineligible)
  pilot_candidates.yaml        — NEW: candidate manifest with verified dayside windows
  pilot_live_science.yaml      — NEW: promoted science pilot config

tests/
  test_curation.py             — NEW: 6 tests for curation workflow
  (all prior tests unchanged)
```

---

## 4. Candidate curation workflow

### How it works
1. Manually curate candidate windows in `configs/pilot_candidates.yaml` with position notes
2. Run `python -m pdl_pilot.cli.validate_candidates --config configs/pilot_candidates.yaml`
3. Each candidate runs through the full pipeline + curation scoring
4. Outputs: `candidate_summary.json`, `candidate_summary.md`, `candidate_summary.csv`
5. Promoted candidates move to `configs/pilot_live_science.yaml`

### Curation criteria (stricter than preflight)
- SZA < 30°, X_GSM > 8 Re, |Y| < 3 Re preferred
- Both near AND background bin occupancy
- High membership fraction
- Low masked fractions
- Wide s-range (s_max - s_min > 0.3 preferred)
- Non-null core metrics (Dn, EB, delta_beta, rho)

### Promotion threshold
Composite score >= 5.0 (configurable via `--promote-threshold`)

---

## 5. Decision status

### Frozen
(Unchanged from Phase 1.5 hardening — encounter unit, s-mapping, bins, IMF-agnostic detection, detector backbone, QC structural)

### Provisional (new/updated)
- Membership min_density_cm3: 0.3 in science config (relaxed from 0.5 for low-Dp outer sheath)
- Membership min_fraction: 0.3 in science config (relaxed from 0.5)
- min_s_std: 0.005 in science config (relaxed from 0.01)
- Curation promotion threshold: 5.0 (first-iteration default)
- Encounter window duration: 90-150 min attempted (may need full-orbit ~6h for both bins)

### Deferred
(Unchanged: thresholds, tuning, MMS, priors, etc.)

---

## 6. Remaining blockers

1. **Background bin occupancy**: Current best windows have 0% background occupancy. Need either full-orbit windows or passes with wider radial traversal.
2. **OMNI intermittency**: CDAWeb SSL connection drops during some fetches. Retries usually succeed but some candidates fail with ERROR status.
3. **Metrics not yet computed on real data**: Because Dn/EB require both near AND background medians, all live encounters produce None metrics. This is correct behavior — the measurement model is honestly enforcing bin requirements.

---

## 7. Key commands

```bash
# Synthetic pilot (unchanged)
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_themis.yaml

# Candidate validation (new)
PYTHONPATH=src python -m pdl_pilot.cli.validate_candidates --config configs/pilot_candidates.yaml

# Science pilot run (new)
PYTHONPATH=src python -m pdl_pilot.cli.run_pilot --config configs/pilot_live_science.yaml

# Tests (102 passed, 1 skipped)
PYTHONPATH=src python -m pytest tests/ -v
```

---

## 8. Next step (do not implement)

Find encounter windows where the spacecraft radial position sweeps from outer sheath (~12-13 Re, near BS) through to inner sheath (~10 Re, near MP) within a single pass. This requires either full-orbit-length windows or different orbital phases where the radial traversal rate is faster. The existing Oct 2008 passes show the spacecraft sitting at ~10 Re for hours — the s-coordinate barely varies. Seasons where the orbit apogee is 13-14 Re (nearer to BS standoff) with fast inbound/outbound legs would populate both bins.
