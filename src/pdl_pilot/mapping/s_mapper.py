"""
Normalized magnetosheath coordinate: s = d_MP / (d_MP + d_BS).

s = 0 → on the magnetopause
s = 1 → on the bow shock

Phase-1 implementation: distance along the Sun-Earth line (x_GSM axis).
Local-normal variant is a TODO / interface placeholder.

Ref: blueprint §5.2
Ref: 2024_lin_magnetopause-model-performance-themis
Ref: 2024_aghabozorgi_magnetopause-location-ml-solar-wind-propagation
"""
from __future__ import annotations

import numpy as np

from pdl_pilot.boundaries.shue1998 import shue1998_standoff
from pdl_pilot.boundaries.merka2005 import merka2005_standoff
from pdl_pilot.config.schema import BinConfig, UncertaintyConfig


def compute_s(
    x_gsm_re: np.ndarray,
    mp_standoff_re: float,
    bs_standoff_re: float,
) -> np.ndarray:
    """Compute normalised magnetosheath coordinate along Sun-Earth line.

    Parameters
    ----------
    x_gsm_re : array
        Spacecraft X position in GSM (Re).  Positive sunward.
    mp_standoff_re : float
        Subsolar magnetopause standoff (Re).
    bs_standoff_re : float
        Subsolar bow-shock standoff (Re).

    Returns
    -------
    s : array
        Values in [0, 1].  Points outside the sheath are clipped.
    """
    d_mp = np.abs(x_gsm_re - mp_standoff_re)
    d_bs = np.abs(x_gsm_re - bs_standoff_re)
    denom = d_mp + d_bs
    s = np.where(denom > 0, d_mp / denom, 0.5)
    return np.clip(s, 0.0, 1.0)


def compute_s_with_uncertainty(
    x_gsm_re: np.ndarray,
    dp_nPa: float,
    bz_nT: float,
    mach_alfven: float | None,
    unc: UncertaintyConfig,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float, float]:
    """Compute s(t) with simple perturbation envelope.

    Returns (s_nominal, s_lo, s_hi, mp_standoff, bs_standoff).
    """
    mp0 = shue1998_standoff(dp_nPa, bz_nT)
    bs0 = merka2005_standoff(mp0, mach_alfven)

    s_nom = compute_s(x_gsm_re, mp0, bs0)

    # perturbed boundaries
    mp_lo = mp0 - unc.mp_standoff_delta_re
    mp_hi = mp0 + unc.mp_standoff_delta_re
    bs_lo = merka2005_standoff(mp_lo, mach_alfven) - unc.bs_standoff_delta_re
    bs_hi = merka2005_standoff(mp_hi, mach_alfven) + unc.bs_standoff_delta_re

    s_lo = compute_s(x_gsm_re, mp_hi, bs_lo)  # wider sheath → smaller s
    s_hi = compute_s(x_gsm_re, mp_lo, bs_hi)  # narrower sheath → larger s

    return s_nom, s_lo, s_hi, mp0, bs0


def compute_bin_occupancy(
    s: np.ndarray, bins: BinConfig
) -> dict[str, float]:
    """Fraction of points in each named bin."""
    n = len(s)
    if n == 0:
        return {"very_near": 0.0, "near": 0.0, "background": 0.0}
    return {
        "very_near": float(np.sum((s >= bins.very_near[0]) & (s < bins.very_near[1])) / n),
        "near": float(np.sum((s >= bins.near[0]) & (s < bins.near[1])) / n),
        "background": float(np.sum((s >= bins.background[0]) & (s <= bins.background[1])) / n),
    }
