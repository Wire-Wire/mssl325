"""Tests for metric-behavior review module (offline-safe)."""
import json
import numpy as np
import pytest


def _make_sample_bank():
    """Create a minimal synthetic bank for testing."""
    return [
        {
            "encounter_id": "win_a_6h", "time_start": "2008-09-03T19:00:00",
            "time_end": "2008-09-04T01:00:00", "probe": "thd",
            "sza_deg": 14.0, "mlt_hours": 12.0,
            "position_gsm_re": [10.0, -1.0, 0.0],
            "upstream": {"dp_nPa": 3.5, "bz_gsm_nT": 0.9, "mach_alfven": 6.0},
            "mapping": {
                "occupancy": {"very_near": 0.3, "near": 0.17, "background": 0.27},
                "s_stats": {"min": 0.0, "max": 0.67},
            },
            "membership_summary": {"membership_fraction": 1.0},
            "metrics": {"Dn": 2.3, "EB": 0.82, "delta_beta": 1.7,
                        "rho_nB_trend": -0.52, "persistence_frac": 0.0, "ptot_smoothness": 0.8},
        },
        {
            "encounter_id": "win_a_8h", "time_start": "2008-09-03T17:00:00",
            "time_end": "2008-09-04T01:00:00", "probe": "thd",
            "sza_deg": 12.0, "mlt_hours": 12.0,
            "position_gsm_re": [10.0, -1.0, 0.0],
            "upstream": {"dp_nPa": 3.5, "bz_gsm_nT": 2.6, "mach_alfven": 6.0},
            "mapping": {
                "occupancy": {"very_near": 0.23, "near": 0.13, "background": 0.40},
                "s_stats": {"min": 0.0, "max": 0.66},
            },
            "membership_summary": {"membership_fraction": 1.0},
            "metrics": {"Dn": 2.1, "EB": 0.80, "delta_beta": 1.7,
                        "rho_nB_trend": -0.51, "persistence_frac": 0.0, "ptot_smoothness": 0.8},
        },
        {
            "encounter_id": "win_b_6h", "time_start": "2008-08-18T18:00:00",
            "time_end": "2008-08-19T00:00:00", "probe": "thd",
            "sza_deg": 22.0, "mlt_hours": 13.0,
            "position_gsm_re": [10.5, -2.0, 0.0],
            "upstream": {"dp_nPa": 4.2, "bz_gsm_nT": 0.3, "mach_alfven": 11.0},
            "mapping": {
                "occupancy": {"very_near": 0.13, "near": 0.16, "background": 0.48},
                "s_stats": {"min": 0.0, "max": 0.71},
            },
            "membership_summary": {"membership_fraction": 0.86},
            "metrics": {"Dn": 0.12, "EB": 2.49, "delta_beta": -10.0,
                        "rho_nB_trend": -0.46, "persistence_frac": 0.94, "ptot_smoothness": 0.86},
        },
    ]


class TestPassIdentification:

    def test_identify_passes(self):
        from pdl_pilot.cli.metric_review import _identify_passes
        bank = _make_sample_bank()
        passes = _identify_passes(bank)
        assert len(passes) == 2  # 2 distinct dates
        assert "2008-09-03" in passes
        assert "2008-08-18" in passes
        assert len(passes["2008-09-03"]) == 2  # duration variants

    def test_build_matrix(self):
        from pdl_pilot.cli.metric_review import _identify_passes, _build_matrix
        bank = _make_sample_bank()
        passes = _identify_passes(bank)
        rows = _build_matrix(bank, passes)
        assert len(rows) == 3
        # Check pass numbering
        dates = {r["date"] for r in rows}
        assert len(dates) == 2
        # Sep 3 variants should be flagged
        sep3 = [r for r in rows if r["date"] == "2008-09-03"]
        assert all(r["is_duration_variant"] for r in sep3)
        assert all(r["n_variants_in_pass"] == 2 for r in sep3)


class TestSpreadAnalysis:

    def test_describe_spread(self):
        from pdl_pilot.cli.metric_review import _identify_passes, _build_matrix, _describe_spread
        bank = _make_sample_bank()
        passes = _identify_passes(bank)
        rows = _build_matrix(bank, passes)
        spread = _describe_spread(rows)
        assert "Dn" in spread
        assert spread["Dn"]["n"] == 3
        assert spread["Dn"]["min"] < spread["Dn"]["max"]

    def test_within_vs_between(self):
        from pdl_pilot.cli.metric_review import _identify_passes, _within_vs_between
        bank = _make_sample_bank()
        passes = _identify_passes(bank)
        wb = _within_vs_between([], passes)
        assert "Dn" in wb


class TestStratification:

    def test_stratify_seeds(self):
        from pdl_pilot.cli.metric_review import _identify_passes, _build_matrix, _stratify_seeds
        bank = _make_sample_bank()
        passes = _identify_passes(bank)
        rows = _build_matrix(bank, passes)
        seeds = _stratify_seeds(rows)
        # Should produce at least 2 seeds (low-Dn and high-Dn)
        assert len(seeds) >= 2
        # Check structure
        for s in seeds:
            assert "seed_name" in s
            assert "encounter_id" in s
            assert "rationale" in s
            assert s["seed_name"].startswith("seed_")

    def test_no_labels_in_seeds(self):
        from pdl_pilot.cli.metric_review import _identify_passes, _build_matrix, _stratify_seeds
        bank = _make_sample_bank()
        passes = _identify_passes(bank)
        rows = _build_matrix(bank, passes)
        seeds = _stratify_seeds(rows)
        forbidden = ["PDL", "non-PDL", "positive", "negative", "baseline", "control"]
        for s in seeds:
            for word in forbidden:
                assert word.lower() not in s["rationale"].lower(), f"Found forbidden label '{word}' in seed rationale"
