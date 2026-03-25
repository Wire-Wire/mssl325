"""
Merka et al. (2005) bow-shock model — simplified subsolar standoff.

Ref: 2005_merka_bow-shock-3d-position-shape-mach-number

Phase-1 implementation uses the Mach-number–dependent empirical fit
for the subsolar bow-shock standoff.  Full 3-D shape is deferred.

Simplified form (Farris & Russell 1994 baseline, Merka refinement):
    R_bs = R_mp * (1 + 1.1 * ((gamma-1)*Ma^2 + 2) / ((gamma+1)*Ma^2))

where gamma = 5/3 and Ma is the Alfvén Mach number.
When Ma is unavailable we fall back to a fixed ratio R_bs/R_mp ≈ 1.3.
"""
from __future__ import annotations


def merka2005_standoff(
    mp_standoff_re: float,
    mach_alfven: float | None = None,
    gamma: float = 5.0 / 3.0,
) -> float:
    """Return subsolar bow-shock standoff distance in Re.

    Parameters
    ----------
    mp_standoff_re : float
        Magnetopause standoff distance (Re).
    mach_alfven : float or None
        Upstream Alfvén Mach number.  If None, uses fixed ratio 1.3.
    gamma : float
        Ratio of specific heats (default 5/3).
    """
    if mach_alfven is None or mach_alfven <= 1.0:
        return float(mp_standoff_re * 1.3)

    inv_compress = ((gamma - 1) * mach_alfven**2 + 2) / (
        (gamma + 1) * mach_alfven**2
    )
    return float(mp_standoff_re * (1.0 + 1.1 * inv_compress))
