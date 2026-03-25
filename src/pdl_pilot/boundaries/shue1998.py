"""
Shue et al. (1998) magnetopause model.

Ref: 1998_shue_magnetopause-location-extreme-solar-wind

The model gives the magnetopause standoff distance r0 and flaring
exponent alpha as functions of solar-wind dynamic pressure Dp (nPa)
and IMF Bz (nT, GSM).  The surface is then:

    r(theta) = r0 * (2 / (1 + cos(theta)))^alpha

where theta is the angle from the Earth-Sun line.

Phase-1 note: we default to distance along the Sun-Earth line
(theta=0 ⇒ r = r0).  Local-normal variant is a TODO placeholder.
"""
from __future__ import annotations
import numpy as np


def shue1998_standoff(dp_nPa: float, bz_nT: float) -> float:
    """Return subsolar magnetopause standoff distance r0 in Re.

    Parameters
    ----------
    dp_nPa : float
        Solar-wind dynamic pressure in nPa.
    bz_nT : float
        IMF Bz in nT (GSM).
    """
    if bz_nT >= 0:
        r0 = (11.4 + 0.013 * bz_nT) * dp_nPa ** (-1.0 / 6.6)
    else:
        r0 = (11.4 + 0.140 * bz_nT) * dp_nPa ** (-1.0 / 6.6)
    return float(r0)


def shue1998_alpha(dp_nPa: float, bz_nT: float) -> float:
    """Return flaring exponent alpha."""
    return float((0.58 - 0.010 * bz_nT) * (1.0 + 0.010 * dp_nPa))


def shue1998_r(theta_rad: float, dp_nPa: float, bz_nT: float) -> float:
    """Return magnetopause distance at angle theta from the Sun-Earth line."""
    r0 = shue1998_standoff(dp_nPa, bz_nT)
    alpha = shue1998_alpha(dp_nPa, bz_nT)
    return float(r0 * (2.0 / (1.0 + np.cos(theta_rad))) ** alpha)
