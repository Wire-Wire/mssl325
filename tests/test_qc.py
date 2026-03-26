"""Tests for QC flags and report generation."""
import numpy as np
import pytest
from pathlib import Path
from pdl_pilot.encounter.model import Encounter, MappingResult
from pdl_pilot.qc.reporter import compute_qc_flags, generate_qc_report
from pdl_pilot.config.schema import BinConfig


def _make_enc() -> Encounter:
    enc = Encounter(encounter_id="test_001")
    n = 100
    enc.time_unix = np.arange(n, dtype=float)
    enc.density_cm3 = 15.0 + np.random.default_rng(0).normal(size=n)
    enc.bmag_nT = 20.0 + np.random.default_rng(1).normal(size=n)
    enc.density_trend = np.full(n, 15.0)
    enc.mapping = MappingResult(s_array=np.linspace(0, 1, n), occupancy={"very_near": 0.2, "near": 0.2, "background": 0.4})
    return enc


def test_qc_flags_no_jet():
    enc = _make_enc()
    vflow = np.full(100, 200.0)
    flags = compute_qc_flags(enc, enc.density_cm3 - enc.density_trend, vflow)
    assert flags.grade in ("Gold", "Silver", "Bronze", "ungraded")


def test_qc_flags_motion():
    enc = _make_enc()
    enc.crossing_count = 5
    flags = compute_qc_flags(enc)
    assert flags.motion_flag is True
    assert any("Multiple crossings" in w for w in flags.warnings)


def test_qc_report_generates_png(tmp_path):
    enc = _make_enc()
    from pdl_pilot.encounter.model import MetricBundle, QCFlags
    enc.metrics = MetricBundle(Dn=0.6, EB=1.3, delta_beta=-0.5)
    enc.qc = QCFlags(grade="Gold")
    enc.beta = np.ones(100)
    enc.ptot_nPa = np.ones(100) * 5.0

    path = generate_qc_report(enc, tmp_path, BinConfig())
    assert path.exists()
    assert path.suffix == ".png"


def test_provenance_manifest(tmp_path):
    from pdl_pilot.config.schema import PipelineConfig
    from pdl_pilot.provenance.tracker import ProvenanceTracker

    cfg = PipelineConfig(output_dir=str(tmp_path / "runs"))
    tracker = ProvenanceTracker(cfg)
    tracker.freeze_config()
    manifest_path = tracker.write_manifest()
    assert manifest_path.exists()
    import json
    data = json.loads(manifest_path.read_text())
    assert "run_id" in data
    assert "config_hash" in data
    assert "python_version" in data
