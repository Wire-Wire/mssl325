"""
Tests for candidate curation and validation workflow.

All tests are offline-safe — uses synthetic data only.
"""
import json
import numpy as np
import pytest
from pathlib import Path


class TestCurationScore:
    """Tests for candidate promotion scoring logic."""

    def test_good_candidate_scores_high(self):
        from pdl_pilot.cli.validate_candidates import _compute_curation_score
        summary = {
            "evaluable": True,
            "sza_deg": 15.0,
            "position_gsm_re": (10.0, -1.0, 0.5),
            "mapping": {
                "occupancy": {"near": 0.3, "background": 0.2},
                "s_stats": {"min": 0.05, "max": 0.8, "mean": 0.4},
            },
            "membership_summary": {"membership_fraction": 0.95},
            "masked_fraction_summary": {"density": 0.01, "bmag": 0.0},
            "metrics": {"Dn": 0.8, "EB": 1.2, "delta_beta": -0.3, "rho_nB_trend": -0.7},
        }
        result = _compute_curation_score(summary)
        assert result["promotable"] is True
        assert result["rank_score"] > 5.0

    def test_non_evaluable_not_promoted(self):
        from pdl_pilot.cli.validate_candidates import _compute_curation_score
        summary = {
            "evaluable": False,
            "scientific_status": "FAIL_GEOMETRY",
        }
        result = _compute_curation_score(summary)
        assert result["promotable"] is False
        assert result["rank_score"] == -1.0

    def test_poor_geometry_low_score(self):
        from pdl_pilot.cli.validate_candidates import _compute_curation_score
        summary = {
            "evaluable": True,
            "sza_deg": 55.0,
            "position_gsm_re": (6.0, 10.0, 5.0),
            "mapping": {
                "occupancy": {"near": 0.03, "background": 0.03},
                "s_stats": {"min": 0.3, "max": 0.4, "mean": 0.35},
            },
            "membership_summary": {"membership_fraction": 0.6},
            "masked_fraction_summary": {},
            "metrics": {"Dn": None, "EB": None, "delta_beta": None, "rho_nB_trend": None},
        }
        result = _compute_curation_score(summary)
        assert result["rank_score"] < 5.0

    def test_no_occupancy_low_score(self):
        from pdl_pilot.cli.validate_candidates import _compute_curation_score
        summary = {
            "evaluable": True,
            "sza_deg": 20.0,
            "position_gsm_re": (10.0, 0.0, 0.0),
            "mapping": {
                "occupancy": {"near": 0.0, "background": 0.0},
                "s_stats": {"min": 0.5, "max": 0.5, "mean": 0.5},
            },
            "membership_summary": {"membership_fraction": 0.9},
            "masked_fraction_summary": {},
            "metrics": {"Dn": None, "EB": None, "delta_beta": None, "rho_nB_trend": None},
        }
        result = _compute_curation_score(summary)
        assert result["criteria"]["occupancy"] == 0.0


class TestCurationWorkflow:
    """Tests for the candidate validation workflow."""

    def test_synthetic_candidate_validation_e2e(self, tmp_path):
        """Run validation on synthetic data to test the workflow."""
        from pdl_pilot.config.schema import PipelineConfig, EncounterSpec
        from pdl_pilot.cli.run_pilot import _build_provider, process_encounter
        from pdl_pilot.cli.validate_candidates import _compute_curation_score
        from pdl_pilot.provenance.tracker import ProvenanceTracker

        config = PipelineConfig(
            data_source="synthetic",
            random_seed=42,
            output_dir=str(tmp_path / "runs"),
            encounters=[
                EncounterSpec(
                    encounter_id="val_001",
                    probe="thd",
                    time_start="2012-01-01T00:00:00",
                    time_end="2012-01-01T00:10:00",
                ),
            ],
        )
        tracker = ProvenanceTracker(config)
        provider = _build_provider(config)
        enc = process_encounter(config.encounters[0], config, tracker.run_dir, provider, tracker)
        summary = enc.to_summary_dict()

        # Synthetic should be evaluable
        assert summary["evaluable"] is True

        # Compute curation score
        score = _compute_curation_score(summary)
        assert "rank_score" in score
        assert "promotable" in score
        assert score["rank_score"] > 0

    def test_summary_md_generation(self, tmp_path):
        """Test markdown summary generation."""
        from pdl_pilot.cli.validate_candidates import _generate_summary_md

        results = [
            {
                "encounter_id": "test_001",
                "probe": "thd",
                "sza_deg": 20.0,
                "position_gsm_re": (10.0, 0.0, 0.0),
                "scientific_status": "PASS",
                "evaluable": True,
                "mlt_hours": 12.0,
                "mapping": {
                    "occupancy": {"near": 0.3, "background": 0.2, "very_near": 0.1},
                    "s_stats": {"min": 0.0, "max": 0.9, "mean": 0.4},
                },
                "membership_summary": {"membership_fraction": 0.95},
                "masked_fraction_summary": {},
                "metrics": {"Dn": 0.8, "EB": 1.2},
                "preflight_reasons": [],
                "curation": {"promotable": True, "rank_score": 12.0, "notes": []},
            },
        ]
        md_path = _generate_summary_md(results, tmp_path)
        assert md_path.exists()
        content = md_path.read_text()
        assert "test_001" in content
        assert "PASS" in content
        assert "Promoted" in content
