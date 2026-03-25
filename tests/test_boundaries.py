"""Tests for boundary models."""
import pytest
import numpy as np
from pdl_pilot.boundaries.shue1998 import shue1998_standoff, shue1998_r
from pdl_pilot.boundaries.merka2005 import merka2005_standoff


class TestShue1998:
    def test_typical_standoff(self):
        """Typical conditions: Dp=2 nPa, Bz=0 → r0 ≈ 10.5 Re."""
        r0 = shue1998_standoff(dp_nPa=2.0, bz_nT=0.0)
        assert 9.0 < r0 < 12.0

    def test_southward_compresses(self):
        """Southward IMF should reduce standoff distance."""
        r_north = shue1998_standoff(dp_nPa=2.0, bz_nT=5.0)
        r_south = shue1998_standoff(dp_nPa=2.0, bz_nT=-5.0)
        assert r_south < r_north

    def test_higher_pressure_compresses(self):
        """Higher Dp should reduce standoff distance."""
        r_lo = shue1998_standoff(dp_nPa=1.0, bz_nT=0.0)
        r_hi = shue1998_standoff(dp_nPa=5.0, bz_nT=0.0)
        assert r_hi < r_lo

    def test_subsolar_equals_standoff(self):
        """At theta=0, r should equal r0."""
        r0 = shue1998_standoff(dp_nPa=2.0, bz_nT=0.0)
        r = shue1998_r(theta_rad=0.0, dp_nPa=2.0, bz_nT=0.0)
        assert abs(r - r0) < 1e-10

    def test_flank_larger(self):
        """Flank distance should be larger than subsolar."""
        r_sub = shue1998_r(0.0, 2.0, 0.0)
        r_flank = shue1998_r(np.pi / 2, 2.0, 0.0)
        assert r_flank > r_sub


class TestMerka2005:
    def test_bs_outside_mp(self):
        """Bow shock should always be outside magnetopause."""
        for mp in [8.0, 10.0, 12.0]:
            bs = merka2005_standoff(mp, mach_alfven=8.0)
            assert bs > mp

    def test_fallback_ratio(self):
        """Without Mach number, use fixed 1.3 ratio."""
        bs = merka2005_standoff(10.0, mach_alfven=None)
        assert abs(bs - 13.0) < 1e-10

    def test_low_mach_fallback(self):
        """Mach <= 1 should trigger fallback."""
        bs = merka2005_standoff(10.0, mach_alfven=0.5)
        assert abs(bs - 13.0) < 1e-10
