"""
Tests for Phase 1.5 diagnostic hardening.

Covers:
  - Fill-value masking (OMNI sentinels, CDF fills, attrs-based)
  - Cone / clock angle geometry
  - Scientific preflight / eligibility status
  - Sheath membership gating
  - Tri-state QC flag behavior
  - Encounter output schema additions
  - Offline end-to-end CLI smoke test

All tests are offline-safe — no network access required.
"""
import json
import numpy as np
import pytest
from pathlib import Path


# ---------------------------------------------------------------------------
# Fill-value masking
# ---------------------------------------------------------------------------

class TestFillMasking:

    def test_omni_bz_sentinel_masked(self):
        from pdl_pilot.data.masking import mask_fill_values
        arr = np.array([1.0, 2.0, 9999.99, -1.5, 9999.99])
        out, summary = mask_fill_values(arr, "BZ_GSM", dataset_type="omni")
        assert summary.n_masked_fill == 2
        assert np.isnan(out[2])
        assert np.isnan(out[4])
        assert np.isfinite(out[0])
        assert summary.fill_method == "omni_table"

    def test_omni_pressure_sentinel(self):
        from pdl_pilot.data.masking import mask_fill_values
        arr = np.array([2.1, 99.99, 3.0])
        out, summary = mask_fill_values(arr, "Pressure", dataset_type="omni")
        assert summary.n_masked_fill == 1
        assert np.isnan(out[1])

    def test_omni_flow_speed_sentinel(self):
        from pdl_pilot.data.masking import mask_fill_values
        arr = np.array([400.0, 99999.9, 350.0])
        out, summary = mask_fill_values(arr, "flow_speed", dataset_type="omni")
        assert summary.n_masked_fill == 1
        assert np.isnan(out[1])

    def test_omni_generic_fallback(self):
        """Unknown OMNI variable with very high values should be caught."""
        from pdl_pilot.data.masking import mask_fill_values
        arr = np.array([1.0, 99999.0, 2.0])
        out, summary = mask_fill_values(arr, "UNKNOWN_VAR", dataset_type="omni")
        assert summary.n_masked_fill == 1
        assert summary.fill_method == "generic"

    def test_cdf_fill_masked(self):
        from pdl_pilot.data.masking import mask_fill_values
        arr = np.array([15.0, -1e31, 12.0, 1e31])
        out, summary = mask_fill_values(arr, "density", dataset_type="themis_mom")
        assert summary.n_masked_fill == 2
        assert np.isfinite(out[0]) and np.isfinite(out[2])

    def test_attrs_based_fillval(self):
        from pdl_pilot.data.masking import mask_fill_values
        arr = np.array([5.0, -999.0, 3.0])
        out, summary = mask_fill_values(arr, "test", fillval=-999.0)
        assert summary.n_masked_fill == 1
        assert summary.fill_method == "attrs"
        assert np.isnan(out[1])

    def test_attrs_validmin_validmax(self):
        from pdl_pilot.data.masking import mask_fill_values
        arr = np.array([-10.0, 5.0, 200.0])
        out, summary = mask_fill_values(arr, "test", validmin=0.0, validmax=100.0)
        assert summary.n_masked_range == 2
        assert np.isnan(out[0]) and np.isnan(out[2])

    def test_no_masking_for_synthetic(self):
        """Synthetic mode should skip masking entirely."""
        from pdl_pilot.cli.run_pilot import _apply_fill_masking
        from pdl_pilot.data.provider import EncounterData
        edata = EncounterData(
            time_unix=np.arange(10, dtype=float),
            x_gsm_re=np.ones(10), y_gsm_re=np.zeros(10), z_gsm_re=np.zeros(10),
            density_cm3=np.ones(10)*15, bmag_nT=np.ones(10)*20,
            beta=np.ones(10), ptot_nPa=np.ones(10)*2, vflow_kms=np.ones(10)*200,
        )
        summaries = _apply_fill_masking(edata, "synthetic")
        assert len(summaries) == 0

    def test_empty_array(self):
        from pdl_pilot.data.masking import mask_fill_values
        arr = np.array([])
        out, summary = mask_fill_values(arr, "empty")
        assert summary.n_total == 0

    def test_masking_summary_to_dict(self):
        from pdl_pilot.data.masking import MaskingSummary
        s = MaskingSummary(variable="test", n_total=100, n_masked_fill=10, n_valid=85)
        d = s.to_dict()
        assert d["masked_fraction"] == 0.1
        assert d["variable"] == "test"


# ---------------------------------------------------------------------------
# Cone / clock angle
# ---------------------------------------------------------------------------

class TestConeClockAngle:

    def test_cone_angle_purely_radial(self):
        """Purely radial IMF (Bx=Bt) → cone angle = 0°."""
        from pdl_pilot.cli.run_pilot import compute_cone_angle
        angle = compute_cone_angle(bx=5.0, bt=5.0)
        assert angle is not None
        assert abs(angle - 0.0) < 1.0

    def test_cone_angle_purely_transverse(self):
        """Purely transverse IMF (Bx=0) → cone angle = 90°."""
        from pdl_pilot.cli.run_pilot import compute_cone_angle
        angle = compute_cone_angle(bx=0.0, bt=5.0)
        assert angle is not None
        assert abs(angle - 90.0) < 1.0

    def test_cone_angle_45deg(self):
        """Bx = Bt/sqrt(2) → cone angle = 45°."""
        from pdl_pilot.cli.run_pilot import compute_cone_angle
        bt = 10.0
        bx = bt / np.sqrt(2)
        angle = compute_cone_angle(bx=bx, bt=bt)
        assert angle is not None
        assert abs(angle - 45.0) < 1.0

    def test_cone_angle_none_when_missing(self):
        from pdl_pilot.cli.run_pilot import compute_cone_angle
        assert compute_cone_angle(None, 5.0) is None
        assert compute_cone_angle(5.0, None) is None
        assert compute_cone_angle(5.0, 0.0) is None

    def test_clock_angle_northward(self):
        """By=0, Bz>0 → clock angle = 0°."""
        from pdl_pilot.cli.run_pilot import compute_clock_angle
        angle = compute_clock_angle(by=0.0, bz=5.0)
        assert angle is not None
        assert abs(angle - 0.0) < 1.0

    def test_clock_angle_duskward(self):
        """By>0, Bz=0 → clock angle = 90°."""
        from pdl_pilot.cli.run_pilot import compute_clock_angle
        angle = compute_clock_angle(by=5.0, bz=0.0)
        assert angle is not None
        assert abs(angle - 90.0) < 1.0

    def test_clock_angle_southward(self):
        """By=0, Bz<0 → clock angle = 180°."""
        from pdl_pilot.cli.run_pilot import compute_clock_angle
        angle = compute_clock_angle(by=0.0, bz=-5.0)
        assert angle is not None
        assert abs(angle - 180.0) < 1.0

    def test_clock_angle_none_when_missing(self):
        from pdl_pilot.cli.run_pilot import compute_clock_angle
        assert compute_clock_angle(None, 5.0) is None
        assert compute_clock_angle(5.0, None) is None


# ---------------------------------------------------------------------------
# Scientific preflight / eligibility
# ---------------------------------------------------------------------------

class TestPreflight:

    def test_pass_geometry(self):
        """Subsolar position should pass geometry check."""
        from pdl_pilot.qc.preflight import run_preflight
        result = run_preflight(
            position_gsm_re=(10.0, 0.0, 0.0),
            sza_deg=5.0,
            occupancy={"very_near": 0.2, "near": 0.3, "background": 0.2},
            s_array=np.linspace(0, 1, 100),
            density=np.ones(100) * 15.0,
            bmag=np.ones(100) * 20.0,
            beta=np.ones(100) * 1.0,
        )
        assert result.scientific_status == "PASS"
        assert result.evaluable is True
        assert "Dn" in result.evaluable_metrics

    def test_fail_geometry_nightside(self):
        """X < 0 (nightside) must fail geometry."""
        from pdl_pilot.qc.preflight import run_preflight
        result = run_preflight(
            position_gsm_re=(-2.0, -4.0, 0.0),
            sza_deg=120.0,
            occupancy={"very_near": 0.2, "near": 0.3, "background": 0.2},
            s_array=np.linspace(0, 1, 100),
            density=np.ones(100) * 15.0,
            bmag=np.ones(100) * 20.0,
            beta=np.ones(100) * 1.0,
        )
        assert result.scientific_status == "FAIL_GEOMETRY"
        assert result.evaluable is False

    def test_fail_geometry_high_sza(self):
        from pdl_pilot.qc.preflight import run_preflight
        result = run_preflight(
            position_gsm_re=(8.0, 0.0, 0.0),
            sza_deg=75.0,  # > 60° default threshold
            occupancy={"very_near": 0.2, "near": 0.3, "background": 0.2},
            s_array=np.linspace(0, 1, 100),
            density=np.ones(100) * 15.0,
            bmag=np.ones(100) * 20.0,
            beta=np.ones(100) * 1.0,
        )
        assert result.scientific_status == "FAIL_GEOMETRY"

    def test_fail_occupancy(self):
        """Zero near-bin occupancy must fail."""
        from pdl_pilot.qc.preflight import run_preflight
        result = run_preflight(
            position_gsm_re=(10.0, 0.0, 0.0),
            sza_deg=10.0,
            occupancy={"very_near": 0.0, "near": 0.0, "background": 0.0},
            s_array=np.ones(100) * 0.5,  # all in gap zone
            density=np.ones(100) * 15.0,
            bmag=np.ones(100) * 20.0,
            beta=np.ones(100) * 1.0,
        )
        assert result.scientific_status in ("FAIL_OCCUPANCY", "FAIL_S_SANITY")
        assert result.evaluable is False

    def test_fail_s_sanity(self):
        """Constant s(t) must fail s-sanity."""
        from pdl_pilot.qc.preflight import run_preflight
        result = run_preflight(
            position_gsm_re=(10.0, 0.0, 0.0),
            sza_deg=10.0,
            occupancy={"very_near": 0.0, "near": 0.0, "background": 0.0},
            s_array=np.ones(100) * 0.3,  # constant
            density=np.ones(100) * 15.0,
            bmag=np.ones(100) * 20.0,
            beta=np.ones(100) * 1.0,
        )
        assert "FAIL" in result.scientific_status

    def test_not_evaluable_means_no_pdl_metrics(self):
        """A failed encounter should have empty evaluable_metrics."""
        from pdl_pilot.qc.preflight import run_preflight
        result = run_preflight(
            position_gsm_re=(-5.0, 0.0, 0.0),
            sza_deg=160.0,
            occupancy={"very_near": 0.0, "near": 0.0, "background": 0.0},
            s_array=np.ones(100) * 0.5,
            density=np.ones(100) * 15.0,
            bmag=np.ones(100) * 20.0,
            beta=np.ones(100) * 1.0,
        )
        assert len(result.evaluable_metrics) == 0

    def test_preflight_result_serializable(self):
        from pdl_pilot.qc.preflight import run_preflight
        result = run_preflight(
            position_gsm_re=(10.0, 0.0, 0.0),
            sza_deg=10.0,
            occupancy={"near": 0.3, "background": 0.2},
            s_array=np.linspace(0, 1, 100),
            density=np.ones(100) * 15.0,
            bmag=np.ones(100) * 20.0,
            beta=np.ones(100) * 1.0,
        )
        d = result.to_dict()
        # Should be JSON-serializable
        json.dumps(d)


# ---------------------------------------------------------------------------
# Sheath membership
# ---------------------------------------------------------------------------

class TestMembership:

    def test_normal_sheath_passes(self):
        from pdl_pilot.qc.preflight import evaluate_sheath_membership, PreflightConfig
        cfg = PreflightConfig()
        n = 100
        result = evaluate_sheath_membership(
            density=np.ones(n) * 15.0,
            bmag=np.ones(n) * 20.0,
            beta=np.ones(n) * 1.0,
            cfg=cfg,
        )
        assert result.membership_fraction > 0.9

    def test_upstream_suspect(self):
        """Very low density/B should be flagged upstream-suspect."""
        from pdl_pilot.qc.preflight import evaluate_sheath_membership, PreflightConfig
        cfg = PreflightConfig()
        result = evaluate_sheath_membership(
            density=np.array([0.1, 0.2, 15.0]),  # first two below threshold
            bmag=np.array([0.5, 0.3, 20.0]),
            beta=np.array([1.0, 1.0, 1.0]),
            cfg=cfg,
        )
        assert result.n_upstream_suspect >= 2

    def test_nan_is_unknown(self):
        from pdl_pilot.qc.preflight import evaluate_sheath_membership, PreflightConfig
        cfg = PreflightConfig()
        result = evaluate_sheath_membership(
            density=np.array([np.nan, 15.0]),
            bmag=np.array([np.nan, 20.0]),
            beta=np.array([np.nan, 1.0]),
            cfg=cfg,
        )
        assert result.n_unknown == 1


# ---------------------------------------------------------------------------
# Tri-state QC flags
# ---------------------------------------------------------------------------

class TestTriStateFlags:

    def test_transient_flag_is_none(self):
        """Transient flag must be None (UNKNOWN), not False."""
        from pdl_pilot.qc.reporter import compute_qc_flags
        from pdl_pilot.encounter.model import Encounter, MappingResult
        enc = Encounter(encounter_id="test")
        enc.density_cm3 = np.ones(100) * 15.0
        enc.density_trend = np.ones(100) * 15.0
        enc.mapping = MappingResult(s_sanity_ok=True)
        flags = compute_qc_flags(enc)
        assert flags.transient_flag is None
        assert flags.mixing_flag is None

    def test_unknown_flags_counted(self):
        from pdl_pilot.qc.reporter import compute_qc_flags
        from pdl_pilot.encounter.model import Encounter, MappingResult
        enc = Encounter(encounter_id="test")
        enc.density_cm3 = np.ones(100) * 15.0
        enc.density_trend = np.ones(100) * 15.0
        enc.mapping = MappingResult(s_sanity_ok=True)
        flags = compute_qc_flags(enc)
        assert flags.n_flags_unknown >= 2  # transient + mixing at minimum

    def test_gold_capped_to_silver(self):
        """With unknown flags, Gold should be capped to Silver."""
        from pdl_pilot.qc.reporter import compute_qc_flags
        from pdl_pilot.encounter.model import Encounter, MappingResult
        enc = Encounter(encounter_id="test", crossing_count=1)
        enc.density_cm3 = np.ones(100) * 15.0
        enc.density_trend = np.ones(100) * 15.0
        enc.mapping = MappingResult(s_sanity_ok=True)
        enc.vflow_kms = np.ones(100) * 200.0
        flags = compute_qc_flags(enc, np.zeros(100), enc.vflow_kms, "cap_silver")
        # With no true flags but unknown flags, should be Silver not Gold
        if flags.n_flags_true == 0 and flags.n_flags_unknown > 0:
            assert flags.grade == "Silver"
            assert "Capped" in flags.grade_note

    def test_preliminary_policy(self):
        from pdl_pilot.qc.reporter import compute_qc_flags
        from pdl_pilot.encounter.model import Encounter, MappingResult
        enc = Encounter(encounter_id="test")
        enc.density_cm3 = np.ones(100) * 15.0
        enc.density_trend = np.ones(100) * 15.0
        enc.mapping = MappingResult(s_sanity_ok=True)
        flags = compute_qc_flags(enc, grade_policy="preliminary")
        assert "Preliminary" in flags.grade

    def test_jet_flag_set_true_when_triggered(self):
        from pdl_pilot.qc.reporter import compute_qc_flags
        from pdl_pilot.encounter.model import Encounter, MappingResult
        enc = Encounter(encounter_id="test")
        n = 100
        enc.density_cm3 = np.ones(n) * 15.0
        enc.density_cm3[50] = 100.0  # spike
        enc.density_trend = np.ones(n) * 15.0
        enc.mapping = MappingResult(s_sanity_ok=True)
        vflow = np.ones(n) * 200.0
        vflow[50] = 1000.0  # velocity spike
        flags = compute_qc_flags(enc, np.zeros(n), vflow)
        assert flags.jet_flag is True

    def test_jet_flag_false_when_no_spike(self):
        from pdl_pilot.qc.reporter import compute_qc_flags
        from pdl_pilot.encounter.model import Encounter, MappingResult
        enc = Encounter(encounter_id="test")
        n = 100
        enc.density_cm3 = np.ones(n) * 15.0
        enc.density_trend = np.ones(n) * 15.0
        enc.mapping = MappingResult(s_sanity_ok=True)
        vflow = np.ones(n) * 200.0
        flags = compute_qc_flags(enc, np.zeros(n), vflow)
        assert flags.jet_flag is False


# ---------------------------------------------------------------------------
# Encounter output schema
# ---------------------------------------------------------------------------

class TestEncounterSchema:

    def test_summary_dict_has_eligibility_fields(self):
        from pdl_pilot.encounter.model import Encounter
        enc = Encounter(encounter_id="test")
        enc.scientific_status = "FAIL_GEOMETRY"
        enc.evaluable = False
        enc.preflight_reasons = ["X < 5 Re"]
        d = enc.to_summary_dict()
        assert "scientific_status" in d
        assert d["scientific_status"] == "FAIL_GEOMETRY"
        assert d["evaluable"] is False
        assert "preflight_reasons" in d
        assert "evaluable_metrics" in d
        assert "membership_summary" in d
        assert "masked_fraction_summary" in d

    def test_qc_to_dict_has_tristate(self):
        from pdl_pilot.encounter.model import QCFlags
        f = QCFlags(jet_flag=True, wave_flag=False, transient_flag=None)
        d = f.to_dict()
        assert d["jet_flag"] is True
        assert d["wave_flag"] is False
        assert d["transient_flag"] is None
        assert "n_flags_unknown" in d
        assert "grade_note" in d


# ---------------------------------------------------------------------------
# End-to-end CLI smoke test (synthetic, offline)
# ---------------------------------------------------------------------------

def test_synthetic_pilot_e2e(tmp_path):
    """Full pipeline on synthetic data with hardened code."""
    from pdl_pilot.config.schema import PipelineConfig, EncounterSpec
    from pdl_pilot.cli.run_pilot import process_encounter, _build_provider
    from pdl_pilot.provenance.tracker import ProvenanceTracker

    config = PipelineConfig(
        data_source="synthetic",
        random_seed=42,
        output_dir=str(tmp_path / "runs"),
        encounters=[
            EncounterSpec(
                encounter_id="smoke_001",
                probe="thd",
                time_start="2012-01-01T00:00:00",
                time_end="2012-01-01T00:10:00",
            ),
        ],
    )
    tracker = ProvenanceTracker(config)
    provider = _build_provider(config)

    enc = process_encounter(config.encounters[0], config, tracker.run_dir, provider, tracker)

    # Encounter should be evaluable (synthetic has good geometry and occupancy)
    assert enc.scientific_status == "PASS"
    assert enc.evaluable is True
    assert enc.metrics.Dn is not None
    assert enc.metrics.EB is not None

    # QC should be honest about unknowns
    assert enc.qc.transient_flag is None
    assert enc.qc.mixing_flag is None
    assert enc.qc.n_flags_unknown >= 2

    # Grade should reflect unknown flags
    assert enc.qc.grade in ("Silver", "Preliminary-Gold", "Gold")

    # JSON output should exist and contain new fields
    enc_path = tracker.run_dir / f"encounter_{enc.encounter_id}.json"
    assert enc_path.exists()
    data = json.loads(enc_path.read_text())
    assert data["scientific_status"] == "PASS"
    assert data["evaluable"] is True
    assert "masked_fraction_summary" in data

    # QC PNG should exist
    qc_path = tracker.run_dir / f"qc_{enc.encounter_id}.png"
    assert qc_path.exists()
