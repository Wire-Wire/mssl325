"""
Tests for window-family validation workflow.

All tests offline-safe — uses synthetic data only.
"""
import json
import numpy as np
import pytest
from datetime import datetime, timezone


class TestWindowGeneration:

    def test_generate_centered_specs(self):
        from pdl_pilot.cli.validate_families import _generate_window_specs
        fam = {
            "seed_id": "test_fam",
            "probe": "thd",
            "center": "2008-10-13T19:00:00",
            "anchor": "centered",
            "durations_minutes": [30, 90, 180],
        }
        specs = _generate_window_specs(fam)
        assert len(specs) == 3
        assert specs[0].encounter_id == "test_fam_30m"
        assert specs[1].encounter_id == "test_fam_90m"
        assert specs[2].encounter_id == "test_fam_180m"
        # 30-min centered: 18:45 to 19:15
        assert specs[0].time_start == "2008-10-13T18:45:00"
        assert specs[0].time_end == "2008-10-13T19:15:00"

    def test_generate_fixed_start_specs(self):
        from pdl_pilot.cli.validate_families import _generate_window_specs
        fam = {
            "seed_id": "test_fs",
            "probe": "thc",
            "center": "2007-07-15T12:00:00",
            "anchor": "fixed_start",
            "durations_minutes": [60, 120],
        }
        specs = _generate_window_specs(fam)
        assert specs[0].time_start == "2007-07-15T12:00:00"
        assert specs[0].time_end == "2007-07-15T13:00:00"
        assert specs[1].time_end == "2007-07-15T14:00:00"

    def test_probe_normalization(self):
        from pdl_pilot.cli.validate_families import _generate_window_specs
        fam = {
            "seed_id": "test",
            "probe": "thc",
            "center": "2007-07-15T12:00:00",
            "durations_minutes": [30],
        }
        specs = _generate_window_specs(fam)
        assert specs[0].probe == "thc"

        fam["probe"] = "c"
        specs = _generate_window_specs(fam)
        assert specs[0].probe == "thc"


class TestWindowScoring:

    def test_good_window_scores_high(self):
        from pdl_pilot.cli.validate_families import _compute_window_score
        summary = {
            "scientific_status": "PASS",
            "evaluable": True,
            "sza_deg": 20.0,
            "position_gsm_re": [12.0, -1.0, 0.0],
            "mapping": {
                "occupancy": {"very_near": 0.2, "near": 0.3, "background": 0.2},
                "s_stats": {"min": 0.1, "max": 0.8},
            },
            "membership_summary": {"membership_fraction": 0.9},
            "metrics": {"Dn": 0.8, "EB": 1.2, "delta_beta": -0.3, "rho_nB_trend": -0.7},
        }
        result = _compute_window_score(summary)
        assert result["usable"] is True
        assert result["score"] > 8.0

    def test_no_background_not_usable(self):
        from pdl_pilot.cli.validate_families import _compute_window_score
        summary = {
            "scientific_status": "FAIL_OCCUPANCY",
            "evaluable": False,
            "sza_deg": 20.0,
            "position_gsm_re": [10.0, -2.0, 0.0],
            "mapping": {
                "occupancy": {"very_near": 0.5, "near": 0.3, "background": 0.0},
                "s_stats": {"min": 0.05, "max": 0.35},
            },
            "membership_summary": {"membership_fraction": 0.95},
            "metrics": {"Dn": None, "EB": None},
        }
        result = _compute_window_score(summary)
        assert result["usable"] is False

    def test_error_window(self):
        from pdl_pilot.cli.validate_families import _compute_window_score
        summary = {"scientific_status": "ERROR"}
        result = _compute_window_score(summary)
        assert result["usable"] is False
        assert result["score"] == -1.0


class TestFamilyConfig:

    def test_load_family_config(self):
        from pdl_pilot.cli.validate_families import _load_family_config
        raw = _load_family_config("configs/pilot_window_families.yaml")
        assert "families" in raw
        families = raw["families"]
        assert len(families) >= 2  # at least oct08_thd and jul07_thc
        # Check structure
        for fam in families:
            assert "seed_id" in fam
            assert "probe" in fam
            assert "center" in fam
            assert "durations_minutes" in fam

    def test_family_ids_unique(self):
        from pdl_pilot.cli.validate_families import _load_family_config
        raw = _load_family_config("configs/pilot_window_families.yaml")
        ids = [f["seed_id"] for f in raw["families"]]
        assert len(ids) == len(set(ids)), "Duplicate seed_ids"


class TestSyntheticFamilyE2E:

    def test_synthetic_family_e2e(self, tmp_path):
        """End-to-end synthetic family test (offline)."""
        from pdl_pilot.config.schema import PipelineConfig, EncounterSpec
        from pdl_pilot.cli.run_pilot import _build_provider, process_encounter
        from pdl_pilot.cli.validate_families import _compute_window_score
        from pdl_pilot.provenance.tracker import ProvenanceTracker

        config = PipelineConfig(
            data_source="synthetic",
            random_seed=42,
            output_dir=str(tmp_path / "runs"),
        )
        tracker = ProvenanceTracker(config)
        provider = _build_provider(config)

        spec = EncounterSpec(
            encounter_id="fam_test_30m",
            probe="thd",
            time_start="2008-01-01T00:00:00",
            time_end="2008-01-01T00:30:00",
        )
        enc = process_encounter(spec, config, tracker.run_dir, provider, tracker)
        summary = enc.to_summary_dict()

        # Score it
        score = _compute_window_score(summary)
        assert "usable" in score
        assert "score" in score
        assert isinstance(score["score"], float)
