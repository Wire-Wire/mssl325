"""
Tests for the data provider abstraction (Phase 1.5).

All tests are offline-safe — no network access required.
"""
import numpy as np
import pytest

from pdl_pilot.config.schema import EncounterSpec, PipelineConfig, LiveDataConfig
from pdl_pilot.data.provider import DataProvider, EncounterData, SourceMetadata
from pdl_pilot.data.synthetic_provider import SyntheticProvider


# ---------------------------------------------------------------------------
# Provider interface tests
# ---------------------------------------------------------------------------

def test_synthetic_provider_returns_encounter_data():
    spec = EncounterSpec(
        encounter_id="test_001",
        probe="thd",
        time_start="2012-07-15T08:00:00",
        time_end="2012-07-15T08:10:00",
    )
    prov = SyntheticProvider(seed=42)
    edata = prov.fetch(spec)

    assert isinstance(edata, EncounterData)
    assert len(edata.time_unix) == 600
    assert len(edata.density_cm3) == 600
    assert len(edata.bmag_nT) == 600
    assert len(edata.x_gsm_re) == 600
    assert np.all(edata.density_cm3 > 0)
    assert np.all(edata.bmag_nT > 0)


def test_synthetic_provider_name():
    prov = SyntheticProvider()
    assert prov.name == "synthetic"


def test_synthetic_provider_metadata():
    spec = EncounterSpec(
        encounter_id="test_meta",
        probe="thd",
        time_start="2012-07-15T08:00:00",
        time_end="2012-07-15T08:10:00",
    )
    prov = SyntheticProvider(seed=99)
    edata = prov.fetch(spec)

    assert len(edata.source_metadata) == 1
    meta = edata.source_metadata[0]
    assert meta.provider == "synthetic"
    assert meta.probe == "thd"
    assert meta.extra["seed"] == 99
    assert not meta.cache_hit


def test_synthetic_provider_deterministic():
    spec = EncounterSpec(
        encounter_id="det",
        probe="thd",
        time_start="2012-01-01T00:00:00",
        time_end="2012-01-01T00:10:00",
    )
    prov = SyntheticProvider(seed=42)
    d1 = prov.fetch(spec)
    d2 = prov.fetch(spec)
    np.testing.assert_array_equal(d1.density_cm3, d2.density_cm3)
    np.testing.assert_array_equal(d1.bmag_nT, d2.bmag_nT)


def test_encounter_data_to_legacy_dict():
    spec = EncounterSpec(
        encounter_id="legacy",
        probe="thd",
        time_start="2012-01-01T00:00:00",
        time_end="2012-01-01T00:10:00",
    )
    prov = SyntheticProvider(seed=42)
    edata = prov.fetch(spec)
    d = edata.to_legacy_dict()

    assert set(d.keys()) == {
        "time_unix", "x_gsm_re", "y_gsm_re", "z_gsm_re",
        "density_cm3", "bmag_nT", "beta", "ptot_nPa", "vflow_kms",
    }
    assert len(d["time_unix"]) == 600


def test_source_metadata_to_dict():
    meta = SourceMetadata(
        provider="test",
        dataset_ids=["DS1"],
        probe="thd",
        cache_hit=True,
    )
    d = meta.to_dict()
    assert d["provider"] == "test"
    assert d["cache_hit"] is True
    assert d["dataset_ids"] == ["DS1"]


# ---------------------------------------------------------------------------
# Provider dispatch tests
# ---------------------------------------------------------------------------

def test_build_provider_synthetic():
    """_build_provider returns SyntheticProvider for synthetic config."""
    from pdl_pilot.cli.run_pilot import _build_provider
    config = PipelineConfig(data_source="synthetic", random_seed=42)
    prov = _build_provider(config)
    assert isinstance(prov, SyntheticProvider)
    assert prov.name == "synthetic"


def test_build_provider_fixture():
    from pdl_pilot.cli.run_pilot import _build_provider
    config = PipelineConfig(data_source="fixture", random_seed=42)
    prov = _build_provider(config)
    assert isinstance(prov, SyntheticProvider)


def test_build_provider_live_requires_cdasws():
    """Live provider import should fail gracefully if cdasws not installed."""
    from pdl_pilot.cli.run_pilot import _build_provider
    config = PipelineConfig(data_source="live")
    # This should not raise at construction time — only at fetch time
    # (lazy import of cdasws)
    prov = _build_provider(config)
    assert prov.name == "cdasws"


def test_build_provider_unknown_raises():
    from pdl_pilot.cli.run_pilot import _build_provider
    from pdl_pilot.config.schema import PipelineConfig as PC
    # We need to bypass pydantic validation for an invalid literal
    # so just test that the function handles the mismatch
    config = PipelineConfig(data_source="synthetic")
    # Force invalid
    object.__setattr__(config, "data_source", "bogus")
    with pytest.raises(ValueError, match="Unknown data_source"):
        _build_provider(config)
