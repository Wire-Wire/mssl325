"""Tests for s-mapping."""
import numpy as np
import pytest
from pdl_pilot.mapping.s_mapper import compute_s, compute_bin_occupancy
from pdl_pilot.config.schema import BinConfig


def test_s_at_magnetopause():
    """s should be 0 at the magnetopause."""
    s = compute_s(np.array([10.0]), mp_standoff_re=10.0, bs_standoff_re=13.0)
    assert abs(s[0] - 0.0) < 1e-10


def test_s_at_bow_shock():
    """s should be 1 at the bow shock."""
    s = compute_s(np.array([13.0]), mp_standoff_re=10.0, bs_standoff_re=13.0)
    # Distance: d_mp=3, d_bs=0 → s = 3/3 = 1.0
    assert abs(s[0] - 1.0) < 1e-10


def test_s_midpoint():
    """Midpoint should give s=0.5."""
    s = compute_s(np.array([11.5]), mp_standoff_re=10.0, bs_standoff_re=13.0)
    assert abs(s[0] - 0.5) < 1e-10


def test_s_always_01():
    """s should always be in [0, 1] even outside boundaries."""
    x = np.linspace(5.0, 18.0, 100)
    s = compute_s(x, mp_standoff_re=10.0, bs_standoff_re=13.0)
    assert np.all(s >= 0.0)
    assert np.all(s <= 1.0)


def test_bin_occupancy_sums():
    """Bin occupancies should not exceed 1.0 total for non-overlapping bins."""
    s = np.linspace(0, 1, 1000)
    bins = BinConfig()
    occ = compute_bin_occupancy(s, bins)
    total = occ["very_near"] + occ["near"] + occ["background"]
    assert total <= 1.01  # allow small float rounding


def test_bin_occupancy_empty():
    occ = compute_bin_occupancy(np.array([]), BinConfig())
    assert occ["very_near"] == 0.0
