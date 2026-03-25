"""Tests for configuration schema validation."""
import pytest
from pdl_pilot.config.schema import PipelineConfig, BinConfig, load_config


def test_default_config_valid():
    cfg = PipelineConfig()
    assert cfg.bins.near == (0.2, 0.4)
    assert cfg.boundary_models.magnetopause == "shue1998"


def test_config_hash_deterministic():
    c1 = PipelineConfig()
    c2 = PipelineConfig()
    assert c1.config_hash() == c2.config_hash()


def test_config_hash_changes():
    c1 = PipelineConfig(run_label="a")
    c2 = PipelineConfig(run_label="b")
    assert c1.config_hash() != c2.config_hash()


def test_bin_config_defaults():
    b = BinConfig()
    assert b.very_near[0] == 0.0
    assert b.very_near[1] == 0.2
    assert b.background[1] == 1.0


def test_load_config_from_file(tmp_path):
    cfg_file = tmp_path / "test.yaml"
    cfg_file.write_text("""
run_label: test_run
data_source: synthetic
encounters:
  - encounter_id: e1
    spacecraft: themis
    probe: thd
    time_start: "2012-01-01T00:00:00"
    time_end: "2012-01-01T01:00:00"
""")
    cfg = load_config(cfg_file)
    assert cfg.run_label == "test_run"
    assert len(cfg.encounters) == 1
    assert cfg.encounters[0].encounter_id == "e1"
