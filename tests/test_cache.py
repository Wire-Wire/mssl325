"""
Tests for the data cache layer (Phase 1.5).

All tests are offline-safe — no network access required.
"""
import json
import numpy as np
import pytest

from pdl_pilot.data.cache import DataCache, _cache_key


def test_cache_key_deterministic():
    k1 = _cache_key("THD_L2_FGM", "2012-01-01", "2012-01-02", "thd")
    k2 = _cache_key("THD_L2_FGM", "2012-01-01", "2012-01-02", "thd")
    assert k1 == k2
    assert len(k1) == 16


def test_cache_key_varies():
    k1 = _cache_key("THD_L2_FGM", "2012-01-01", "2012-01-02", "thd")
    k2 = _cache_key("THE_L2_FGM", "2012-01-01", "2012-01-02", "the")
    assert k1 != k2


def test_cache_raw_path(tmp_path):
    cache = DataCache(tmp_path / "cache", policy="use")
    p = cache.raw_path("THD_L2_FGM", "file.cdf")
    assert p.parent.name == "THD_L2_FGM"
    assert p.name == "file.cdf"
    assert p.parent.exists()


def test_cache_norm_path(tmp_path):
    cache = DataCache(tmp_path / "cache", policy="use")
    p = cache.norm_path("enc_001", "fgm")
    assert p.name == "fgm.npz"
    assert "enc_001" in str(p)
    assert p.parent.exists()


def test_cache_has_raw_miss(tmp_path):
    cache = DataCache(tmp_path / "cache", policy="use")
    assert not cache.has_raw("THD_L2_FGM", "missing.cdf")


def test_cache_has_raw_hit(tmp_path):
    cache = DataCache(tmp_path / "cache", policy="use")
    p = cache.raw_path("THD_L2_FGM", "file.cdf")
    p.write_text("dummy")
    assert cache.has_raw("THD_L2_FGM", "file.cdf")


def test_cache_policy_refresh_ignores_existing(tmp_path):
    cache = DataCache(tmp_path / "cache", policy="refresh")
    p = cache.raw_path("THD_L2_FGM", "file.cdf")
    p.write_text("dummy")
    assert not cache.has_raw("THD_L2_FGM", "file.cdf")


def test_cache_policy_skip_ignores_existing(tmp_path):
    cache = DataCache(tmp_path / "cache", policy="skip")
    p = cache.raw_path("THD_L2_FGM", "file.cdf")
    p.write_text("dummy")
    assert not cache.has_raw("THD_L2_FGM", "file.cdf")


def test_cache_record_and_retrieve(tmp_path):
    cache = DataCache(tmp_path / "cache", policy="use")
    cache.record(
        "test_key",
        dataset="THD_L2_FGM",
        trange=("2012-01-01", "2012-01-02"),
        probe="thd",
        cache_hit=False,
    )
    rec = cache.get_record("test_key")
    assert rec is not None
    assert rec["dataset"] == "THD_L2_FGM"
    assert rec["cache_hit"] is False

    # Verify index persisted to disk
    cache2 = DataCache(tmp_path / "cache", policy="use")
    rec2 = cache2.get_record("test_key")
    assert rec2 is not None


def test_cache_summary(tmp_path):
    cache = DataCache(tmp_path / "cache", policy="use")
    s = cache.summary()
    assert s["policy"] == "use"
    assert s["raw_files_cached"] == 0
    assert s["index_entries"] == 0


def test_cache_clear(tmp_path):
    cache = DataCache(tmp_path / "cache", policy="use")
    p = cache.raw_path("DS", "file.cdf")
    p.write_text("dummy")
    cache.record("k", dataset="DS", trange=("a", "b"))
    assert cache.has_raw("DS", "file.cdf")

    cache.clear()
    assert not cache.has_raw("DS", "file.cdf")
    assert cache.get_record("k") is None
    assert cache.summary()["raw_files_cached"] == 0


def test_cache_norm_roundtrip(tmp_path):
    cache = DataCache(tmp_path / "cache", policy="use")
    p = cache.norm_path("enc_001", "test_data")

    # Save some numpy data
    arr = np.array([1.0, 2.0, 3.0])
    np.savez(str(p), values=arr)

    assert cache.has_norm("enc_001", "test_data")

    # Load it back
    loaded = dict(np.load(str(p)))
    np.testing.assert_array_equal(loaded["values"], arr)
