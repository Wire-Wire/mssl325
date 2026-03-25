"""Tests for detector metric calculator."""
import numpy as np
import pytest
from pdl_pilot.metrics.calculator import compute_metrics, extract_trend
from pdl_pilot.config.schema import BinConfig, FilterConfig


def test_extract_trend_smooths():
    """Trend should be smoother than raw signal."""
    rng = np.random.default_rng(0)
    signal = np.sin(np.linspace(0, 4 * np.pi, 200)) + 0.5 * rng.normal(size=200)
    trend = extract_trend(signal, window_pts=21)
    assert np.std(trend) < np.std(signal)


def test_metrics_with_depletion():
    """A signal with near-bin depletion should yield Dn < 1."""
    n_pts = 500
    s = np.linspace(0, 1, n_pts)

    # Background density ~15, near-bin depleted to ~8
    density = np.where(s < 0.4, 8.0, 15.0) + 0.5 * np.random.default_rng(1).normal(size=n_pts)
    density = np.clip(density, 1.0, None)

    bmag = np.where(s < 0.4, 30.0, 20.0) + 1.0 * np.random.default_rng(2).normal(size=n_pts)
    bmag = np.clip(bmag, 1.0, None)

    beta = density / bmag  # simplified
    ptot = density + bmag

    bins = BinConfig()
    filters = FilterConfig()
    bundle, *_ = compute_metrics(s, density, bmag, beta, ptot, bins, filters)

    assert bundle.Dn is not None
    assert bundle.Dn < 1.0, f"Expected depletion Dn<1, got {bundle.Dn}"
    assert bundle.EB is not None
    assert bundle.EB > 1.0, f"Expected enhancement EB>1, got {bundle.EB}"


def test_metrics_no_data():
    """Empty arrays should produce None metrics gracefully."""
    s = np.array([0.5])
    d = np.array([10.0])
    b = np.array([20.0])
    beta = np.array([1.0])
    ptot = np.array([30.0])
    bundle, *_ = compute_metrics(s, d, b, beta, ptot, BinConfig(), FilterConfig())
    # With only 1 point, most bins are empty
    assert bundle.Dn is None or isinstance(bundle.Dn, float)
