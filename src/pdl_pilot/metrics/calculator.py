"""
Minimal PDL detector metric calculator.

Computes backbone metrics from encounter data using robust
statistics (medians / quantiles).  Phase-1 only — no classification
thresholds are finalized here.

Ref: blueprint §6.3 (core PDL criteria)
Ref: 1976_zwan_solar-wind-plasma-depletion-planetary-boundary
Ref: 1997_anderson_plasma-depletion-subsolar-reconnection
Ref: 2004_wang_pdl-magnetosheath-flow-structure-forces
"""
from __future__ import annotations

import logging

import numpy as np
from scipy.ndimage import median_filter
from scipy.stats import spearmanr

from pdl_pilot.config.schema import BinConfig, FilterConfig
from pdl_pilot.encounter.model import MetricBundle

log = logging.getLogger(__name__)


def _select_bin(s: np.ndarray, lo: float, hi: float) -> np.ndarray:
    """Boolean mask for points within [lo, hi)."""
    return (s >= lo) & (s < hi)


def _safe_median(arr: np.ndarray, mask: np.ndarray) -> float | None:
    vals = arr[mask]
    if len(vals) == 0:
        return None
    return float(np.nanmedian(vals))


def extract_trend(signal: np.ndarray, window_pts: int) -> np.ndarray:
    """Running median trend extraction."""
    if window_pts < 3:
        window_pts = 3
    if window_pts % 2 == 0:
        window_pts += 1
    return median_filter(signal, size=window_pts, mode="reflect")


def compute_metrics(
    s: np.ndarray,
    density: np.ndarray,
    bmag: np.ndarray,
    beta: np.ndarray,
    ptot: np.ndarray,
    bins: BinConfig,
    filters: FilterConfig,
    cadence_seconds: float = 1.0,
) -> MetricBundle:
    """Compute encounter-level PDL detector metrics.

    Uses the *near* bin [0.2, 0.4] as the primary robust bin and
    the background bin for normalization.

    Parameters
    ----------
    s : array
        Normalized magnetosheath coordinate.
    density, bmag, beta, ptot : arrays
        Physical quantities at each time step.
    bins : BinConfig
    filters : FilterConfig
    cadence_seconds : float
    """
    near_mask = _select_bin(s, *bins.near)
    bg_mask = _select_bin(s, *bins.background)

    n_near = _safe_median(density, near_mask)
    n_bg = _safe_median(density, bg_mask)
    b_near = _safe_median(bmag, near_mask)
    b_bg = _safe_median(bmag, bg_mask)
    beta_near = _safe_median(beta, near_mask)
    beta_bg = _safe_median(beta, bg_mask)

    # Dn = median(n_near) / median(n_bg)
    Dn = (n_near / n_bg) if (n_near is not None and n_bg is not None and n_bg > 0) else None
    # EB = median(|B|_near) / median(|B|_bg)
    EB = (b_near / b_bg) if (b_near is not None and b_bg is not None and b_bg > 0) else None
    # Delta_beta
    delta_beta = (
        (beta_near - beta_bg)
        if (beta_near is not None and beta_bg is not None)
        else None
    )

    # Trend extraction
    window_pts = max(3, int(filters.trend_window_seconds / cadence_seconds))
    n_trend = extract_trend(density, window_pts)
    b_trend = extract_trend(bmag, window_pts)

    # Trend-scale anti-correlation rho(n_trend, |B|_trend)
    # (use combined near+very-near region)
    near_all = _select_bin(s, bins.very_near[0], bins.near[1])
    rho = None
    if np.sum(near_all) > 10:
        r, _ = spearmanr(n_trend[near_all], b_trend[near_all])
        rho = float(r) if np.isfinite(r) else None

    # Total-pressure smoothness: CV of ptot in the near region
    ptot_vals = ptot[near_all]
    ptot_smooth = None
    if len(ptot_vals) > 3:
        mean_p = np.nanmean(ptot_vals)
        if mean_p > 0:
            ptot_smooth = float(1.0 - np.nanstd(ptot_vals) / mean_p)

    # Persistence: fraction of near-bin points showing density < background median
    persist = None
    if n_bg is not None and np.sum(near_mask) > 0:
        persist = float(np.sum(density[near_mask] < n_bg) / np.sum(near_mask))

    # Fluctuation amplitude summary
    n_resid = density - n_trend
    fluct_amp = float(np.nanstd(n_resid)) if len(n_resid) > 0 else None

    bundle = MetricBundle(
        Dn=Dn,
        EB=EB,
        delta_beta=delta_beta,
        rho_nB_trend=rho,
        ptot_smoothness=ptot_smooth,
        persistence_frac=persist,
        fluctuation_amp=fluct_amp,
    )
    log.info("Metrics: Dn=%.3f  EB=%.3f  Δβ=%.3f  ρ=%.3f",
             Dn or 0, EB or 0, delta_beta or 0, rho or 0)
    return bundle, n_trend, b_trend, n_resid, density - n_trend
