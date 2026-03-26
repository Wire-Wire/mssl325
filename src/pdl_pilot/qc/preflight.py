"""
Scientific preflight / eligibility evaluation for encounters.

Before metrics can be meaningfully interpreted, the encounter must pass
basic checks on geometry, data completeness, sheath membership, and
bin occupancy.  An encounter that fails these checks is NOT a scientific
negative — it is *not evaluable* for PDL detection purposes.

Ref: blueprint §5.1 (sheath membership), §6.2 (sample design)
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Literal

import numpy as np

from pdl_pilot.config.schema import BinConfig

log = logging.getLogger(__name__)

# ---- Scientific status categories ----
# These must distinguish "no PDL found" from "cannot evaluate"
ScientificStatus = Literal[
    "PASS",              # all preflight checks passed — encounter is evaluable
    "FAIL_GEOMETRY",     # spacecraft not in target dayside geometry
    "FAIL_DATA_VALIDITY",  # too much missing / fill-masked data
    "FAIL_MEMBERSHIP",   # most data is not plausibly magnetosheath
    "FAIL_OCCUPANCY",    # insufficient data in near/background bins
    "FAIL_S_SANITY",     # degenerate s(t) mapping
    "REVIEW_NEEDED",     # some checks marginal — human inspection required
]


@dataclass
class PreflightConfig:
    """Thresholds for preflight eligibility checks.

    All PROVISIONAL — will be tuned from pilot experience in Phase 2.
    """
    # Geometry — target dayside near-subsolar (blueprint §6.2)
    max_sza_deg: float = 60.0         # PROVISIONAL: relaxed from §6.2's <30° target
    min_x_gsm_re: float = 5.0         # must be sunward
    max_abs_y_gsm_re: float = 15.0    # not deep flank

    # Data validity — minimum acceptable fraction of finite values
    min_valid_fraction: float = 0.5

    # Sheath membership — plasma/field basic checks
    # Conservative: only reject *obvious* non-sheath
    min_density_cm3: float = 0.5       # below this → upstream/void
    max_density_cm3: float = 200.0     # above this → likely fill artifact
    min_bmag_nT: float = 1.0           # below this → upstream-like
    max_bmag_nT: float = 200.0         # above this → likely magnetospheric
    min_beta_sheath: float = 0.01      # very low beta → magnetosphere
    max_beta_sheath: float = 100.0     # extremely high → likely artifact
    min_membership_fraction: float = 0.5  # at least half must pass

    # Bin occupancy
    min_near_occupancy: float = 0.02   # at least 2% of points in near bin
    min_bg_occupancy: float = 0.02     # at least 2% in background bin

    # s-sanity
    min_s_std: float = 0.01            # s(t) must have measurable spread

    def to_dict(self) -> dict:
        return self.__dict__.copy()


@dataclass
class MembershipResult:
    """Sheath-membership validation result."""
    n_total: int = 0
    n_sheath_plausible: int = 0
    n_magnetosphere_suspect: int = 0
    n_upstream_suspect: int = 0
    n_artifact_suspect: int = 0
    n_unknown: int = 0
    membership_fraction: float = 0.0   # fraction passing basic sheath checks
    reasons: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items()}


@dataclass
class PreflightResult:
    """Full preflight evaluation result for one encounter."""
    scientific_status: str = "REVIEW_NEEDED"
    evaluable: bool = False
    checks: dict[str, str] = field(default_factory=dict)  # check_name → PASS/FAIL/WARN
    reasons: list[str] = field(default_factory=list)
    membership: MembershipResult = field(default_factory=MembershipResult)
    masked_fraction_summary: dict[str, float] = field(default_factory=dict)
    evaluable_metrics: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "scientific_status": self.scientific_status,
            "evaluable": self.evaluable,
            "checks": self.checks,
            "reasons": self.reasons,
            "membership": self.membership.to_dict(),
            "masked_fraction_summary": self.masked_fraction_summary,
            "evaluable_metrics": self.evaluable_metrics,
        }


def evaluate_sheath_membership(
    density: np.ndarray,
    bmag: np.ndarray,
    beta: np.ndarray,
    cfg: PreflightConfig,
) -> MembershipResult:
    """Conservative sheath-membership check using plasma/field sanity.

    This is NOT a full region classifier.  It only flags *obvious*
    non-sheath data: too-low density/B (upstream), too-high B/too-low beta
    (magnetosphere), or artifact-level values.

    Parameters
    ----------
    density, bmag, beta : arrays (same length)
    cfg : PreflightConfig

    Returns
    -------
    MembershipResult
    """
    n = len(density)
    result = MembershipResult(n_total=n)
    if n == 0:
        return result

    # Per-point classification
    is_finite = np.isfinite(density) & np.isfinite(bmag)

    # Artifact-level values
    artifact = is_finite & (
        (density > cfg.max_density_cm3) |
        (bmag > cfg.max_bmag_nT) |
        (np.isfinite(beta) & (beta > cfg.max_beta_sheath))
    )

    # Upstream-suspect: very low density AND low B
    upstream = is_finite & ~artifact & (
        (density < cfg.min_density_cm3) |
        (bmag < cfg.min_bmag_nT)
    )

    # Magnetosphere-suspect: very low beta AND reasonable B
    msphere = is_finite & ~artifact & ~upstream & (
        np.isfinite(beta) & (beta < cfg.min_beta_sheath) & (bmag > 50.0)
    )

    # Sheath-plausible: finite AND not flagged above
    sheath = is_finite & ~artifact & ~upstream & ~msphere

    # Unknown: NaN / infinite values
    unknown = ~is_finite

    result.n_sheath_plausible = int(np.sum(sheath))
    result.n_magnetosphere_suspect = int(np.sum(msphere))
    result.n_upstream_suspect = int(np.sum(upstream))
    result.n_artifact_suspect = int(np.sum(artifact))
    result.n_unknown = int(np.sum(unknown))
    result.membership_fraction = float(result.n_sheath_plausible / n) if n > 0 else 0.0

    reasons = []
    if result.n_artifact_suspect > 0:
        reasons.append(f"{result.n_artifact_suspect} artifact-suspect points")
    if result.n_upstream_suspect > 0:
        reasons.append(f"{result.n_upstream_suspect} upstream-suspect points")
    if result.n_magnetosphere_suspect > 0:
        reasons.append(f"{result.n_magnetosphere_suspect} magnetosphere-suspect points")
    if result.n_unknown > 0:
        reasons.append(f"{result.n_unknown} unknown/NaN points")
    result.reasons = reasons

    return result


def run_preflight(
    *,
    position_gsm_re: tuple[float, float, float] | None,
    sza_deg: float | None,
    occupancy: dict[str, float],
    s_array: np.ndarray | None,
    density: np.ndarray | None,
    bmag: np.ndarray | None,
    beta: np.ndarray | None,
    masked_fractions: dict[str, float] | None = None,
    cfg: PreflightConfig | None = None,
    bins: BinConfig | None = None,
) -> PreflightResult:
    """Run all preflight checks and return a PreflightResult.

    Parameters
    ----------
    position_gsm_re : (x, y, z) mean position in Re
    sza_deg : solar zenith angle in degrees
    occupancy : bin occupancy dict from s-mapping
    s_array : s(t) values
    density, bmag, beta : encounter time series arrays
    masked_fractions : per-variable masked fraction from fill-value masking
    cfg : PreflightConfig (uses defaults if None)
    bins : BinConfig (uses defaults if None)
    """
    if cfg is None:
        cfg = PreflightConfig()
    if bins is None:
        bins = BinConfig()

    result = PreflightResult()
    fail_reasons: list[str] = []
    warn_reasons: list[str] = []

    # ---- 1. Geometry check ----
    if position_gsm_re is not None:
        x, y, z = position_gsm_re
        if x < cfg.min_x_gsm_re:
            result.checks["geometry_x"] = "FAIL"
            fail_reasons.append(f"X_GSM={x:.1f} Re < {cfg.min_x_gsm_re} Re (not sunward)")
        else:
            result.checks["geometry_x"] = "PASS"

        if abs(y) > cfg.max_abs_y_gsm_re:
            result.checks["geometry_y"] = "FAIL"
            fail_reasons.append(f"|Y_GSM|={abs(y):.1f} Re > {cfg.max_abs_y_gsm_re} Re (deep flank)")
        else:
            result.checks["geometry_y"] = "PASS"
    else:
        result.checks["geometry_x"] = "FAIL"
        result.checks["geometry_y"] = "FAIL"
        fail_reasons.append("No position data")

    if sza_deg is not None:
        if sza_deg > cfg.max_sza_deg:
            result.checks["geometry_sza"] = "FAIL"
            fail_reasons.append(f"SZA={sza_deg:.1f}° > {cfg.max_sza_deg}° (not dayside)")
        else:
            result.checks["geometry_sza"] = "PASS"
    else:
        result.checks["geometry_sza"] = "FAIL"
        fail_reasons.append("No SZA available")

    # Geometry pass/fail
    geom_fail = any(result.checks.get(k) == "FAIL"
                    for k in ("geometry_x", "geometry_y", "geometry_sza"))

    # ---- 2. Data validity ----
    if masked_fractions:
        result.masked_fraction_summary = masked_fractions
        for var, frac in masked_fractions.items():
            valid_frac = 1.0 - frac
            if valid_frac < cfg.min_valid_fraction:
                result.checks[f"data_{var}"] = "FAIL"
                fail_reasons.append(
                    f"{var}: valid fraction {valid_frac:.1%} < {cfg.min_valid_fraction:.0%}"
                )
            else:
                result.checks[f"data_{var}"] = "PASS"

    # ---- 3. Sheath membership ----
    if density is not None and bmag is not None and beta is not None:
        membership = evaluate_sheath_membership(density, bmag, beta, cfg)
        result.membership = membership

        if membership.membership_fraction < cfg.min_membership_fraction:
            result.checks["membership"] = "FAIL"
            fail_reasons.append(
                f"Sheath membership {membership.membership_fraction:.1%} "
                f"< {cfg.min_membership_fraction:.0%}"
            )
        else:
            result.checks["membership"] = "PASS"
    else:
        result.checks["membership"] = "FAIL"
        fail_reasons.append("Missing density/bmag/beta for membership check")

    # ---- 4. Bin occupancy ----
    near_occ = occupancy.get("near", 0.0)
    bg_occ = occupancy.get("background", 0.0)

    if near_occ < cfg.min_near_occupancy:
        result.checks["occupancy_near"] = "FAIL"
        fail_reasons.append(
            f"Near-bin occupancy {near_occ:.1%} < {cfg.min_near_occupancy:.0%}"
        )
    else:
        result.checks["occupancy_near"] = "PASS"

    if bg_occ < cfg.min_bg_occupancy:
        result.checks["occupancy_bg"] = "FAIL"
        fail_reasons.append(
            f"Background-bin occupancy {bg_occ:.1%} < {cfg.min_bg_occupancy:.0%}"
        )
    else:
        result.checks["occupancy_bg"] = "PASS"

    # ---- 5. s-sanity ----
    if s_array is not None and len(s_array) > 1:
        s_std = float(np.nanstd(s_array))
        if s_std < cfg.min_s_std:
            result.checks["s_sanity"] = "FAIL"
            fail_reasons.append(
                f"s(t) std={s_std:.4f} < {cfg.min_s_std} (degenerate mapping)"
            )
        else:
            result.checks["s_sanity"] = "PASS"
    else:
        result.checks["s_sanity"] = "FAIL"
        fail_reasons.append("No s(t) data for sanity check")

    # ---- Determine overall status ----
    if geom_fail:
        result.scientific_status = "FAIL_GEOMETRY"
    elif any(result.checks.get(k) == "FAIL" for k in result.checks if k.startswith("data_")):
        result.scientific_status = "FAIL_DATA_VALIDITY"
    elif result.checks.get("membership") == "FAIL":
        result.scientific_status = "FAIL_MEMBERSHIP"
    elif result.checks.get("occupancy_near") == "FAIL" or result.checks.get("occupancy_bg") == "FAIL":
        result.scientific_status = "FAIL_OCCUPANCY"
    elif result.checks.get("s_sanity") == "FAIL":
        result.scientific_status = "FAIL_S_SANITY"
    elif warn_reasons:
        result.scientific_status = "REVIEW_NEEDED"
    else:
        result.scientific_status = "PASS"

    result.evaluable = result.scientific_status == "PASS"
    result.reasons = fail_reasons + warn_reasons

    # Determine which metrics are evaluable
    if result.evaluable:
        result.evaluable_metrics = [
            "Dn", "EB", "delta_beta", "rho_nB_trend",
            "persistence_frac", "ptot_smoothness", "fluctuation_amp",
        ]
    elif (result.checks.get("occupancy_near") == "PASS" and
          result.checks.get("occupancy_bg") == "PASS" and
          result.checks.get("membership") == "PASS"):
        # Metrics are computable even if geometry is non-target
        result.evaluable_metrics = [
            "Dn", "EB", "delta_beta", "rho_nB_trend",
            "persistence_frac", "ptot_smoothness", "fluctuation_amp",
        ]
    else:
        result.evaluable_metrics = []

    log.info("Preflight status: %s (evaluable=%s, reasons=%d)",
             result.scientific_status, result.evaluable, len(result.reasons))
    for r in result.reasons:
        log.info("  → %s", r)

    return result
