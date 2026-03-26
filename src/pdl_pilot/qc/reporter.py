"""
QC report generator — standardized diagnostic plots and flag summary.

For each encounter, produces a multi-panel figure with:
- time series of n, |B|, beta, P_tot
- s(t) with bin boundaries
- trend vs residual decomposition
- metric summary panel
- flags / warnings panel

Ref: 2013_archer_magnetosheath-dynamic-pressure-enhancements (jet flags)
Ref: 2015_soucek_magnetosheath-plasma-stability-ulf-waves (wave flags)
Ref: 2023_blancocano_jets-mirror-mode-waves-magnetosheath
"""
from __future__ import annotations

import logging
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from pdl_pilot.encounter.model import Encounter, QCFlags, MetricBundle
from pdl_pilot.config.schema import BinConfig

log = logging.getLogger(__name__)


def compute_qc_flags(
    enc: Encounter,
    density_residual: np.ndarray | None = None,
    vflow: np.ndarray | None = None,
    grade_policy: str = "cap_silver",
) -> QCFlags:
    """Compute minimal confounder flags with tri-state logic.

    Phase-1.5: flags are True/False/None (UNKNOWN).
    NOT_IMPLEMENTED flags are None, not False.
    Grading is honest about incomplete flag coverage.

    Parameters
    ----------
    grade_policy : str
        How to handle UNKNOWN flags in grading:
        - "cap_silver": max grade is Silver if any flags are UNKNOWN
        - "preliminary": emit "Preliminary" grade label
        - "ungraded": emit "ungraded" if any flags are UNKNOWN
    """
    flags = QCFlags()
    warnings: list[str] = []

    # Jet flag: dynamic-pressure spike > 2× median in sheath
    if vflow is not None and enc.density_cm3 is not None:
        dp_proxy = enc.density_cm3 * vflow**2
        valid_dp = dp_proxy[np.isfinite(dp_proxy)]
        if len(valid_dp) > 3:
            med_dp = np.nanmedian(valid_dp)
            if med_dp > 0 and np.nanmax(valid_dp) > 2.0 * med_dp:
                flags.jet_flag = True
                warnings.append("Possible jet: Pdyn spike > 2x median")
            else:
                flags.jet_flag = False
        else:
            flags.jet_flag = None
            warnings.append("Jet flag: insufficient valid data")
    else:
        flags.jet_flag = None
        warnings.append("Jet flag: no velocity data")

    # Wave flag: high fluctuation amplitude relative to trend
    if density_residual is not None and enc.density_trend is not None:
        trend_med = np.nanmedian(np.abs(enc.density_trend))
        if trend_med > 0:
            rel_fluct = np.nanstd(density_residual) / trend_med
            if rel_fluct > 0.3:
                flags.wave_flag = True
                warnings.append(f"High fluctuation amplitude: {rel_fluct:.2f}")
            else:
                flags.wave_flag = False
        else:
            flags.wave_flag = None
    else:
        flags.wave_flag = None

    # Motion flag: multiple crossings
    if enc.crossing_count > 2:
        flags.motion_flag = True
        warnings.append(f"Multiple crossings ({enc.crossing_count})")
    else:
        flags.motion_flag = False

    # Transient flag: NOT IMPLEMENTED — honest None, not False
    flags.transient_flag = None

    # Mixing flag: NOT IMPLEMENTED — honest None, not False
    flags.mixing_flag = None

    # s-sanity
    if not enc.mapping.s_sanity_ok:
        warnings.append("s-mapping sanity check failed")

    flags.warnings = warnings

    # Honest grading: count true vs unknown flags
    all_flags = [flags.jet_flag, flags.wave_flag, flags.transient_flag,
                 flags.motion_flag, flags.mixing_flag]
    n_true = sum(1 for f in all_flags if f is True)
    n_unknown = sum(1 for f in all_flags if f is None)
    flags.n_flags_true = n_true
    flags.n_flags_unknown = n_unknown

    # Base grade from known flags
    if n_true == 0:
        base_grade = "Gold"
    elif n_true == 1:
        base_grade = "Silver"
    else:
        base_grade = "Bronze"

    # Apply policy for unknown flags
    if n_unknown > 0:
        if grade_policy == "cap_silver":
            if base_grade == "Gold":
                flags.grade = "Silver"
                flags.grade_note = (
                    f"Capped from Gold: {n_unknown} flag(s) UNKNOWN "
                    "(transient, mixing not implemented)"
                )
            else:
                flags.grade = base_grade
                flags.grade_note = f"{n_unknown} flag(s) UNKNOWN"
        elif grade_policy == "preliminary":
            flags.grade = f"Preliminary-{base_grade}"
            flags.grade_note = f"{n_unknown} flag(s) not yet implemented"
        elif grade_policy == "ungraded":
            flags.grade = "ungraded"
            flags.grade_note = f"Cannot grade: {n_unknown} flag(s) UNKNOWN"
        else:
            flags.grade = base_grade
            flags.grade_note = f"{n_unknown} flag(s) UNKNOWN"
    else:
        flags.grade = base_grade
        flags.grade_note = ""

    return flags


def generate_qc_report(
    enc: Encounter,
    output_dir: Path,
    bins: BinConfig | None = None,
) -> Path:
    """Generate a standardized multi-panel QC figure for one encounter.

    Returns the path to the saved PNG.
    """
    if bins is None:
        bins = BinConfig()

    fig, axes = plt.subplots(6, 1, figsize=(12, 16), sharex=True)
    fig.suptitle(f"QC Report — {enc.encounter_id}", fontsize=14, y=0.98)

    t = enc.time_unix
    if t is None:
        t = np.arange(100, dtype=float)

    t_rel = t - t[0]  # relative time in seconds

    # Panel 1: density
    ax = axes[0]
    if enc.density_cm3 is not None:
        ax.plot(t_rel, enc.density_cm3, "b-", lw=0.7, label="n")
        if enc.density_trend is not None:
            ax.plot(t_rel, enc.density_trend, "r-", lw=1.2, label="trend")
    ax.set_ylabel("n (cm⁻³)")
    ax.legend(loc="upper right", fontsize=8)

    # Panel 2: |B|
    ax = axes[1]
    if enc.bmag_nT is not None:
        ax.plot(t_rel, enc.bmag_nT, "b-", lw=0.7, label="|B|")
        if enc.bmag_trend is not None:
            ax.plot(t_rel, enc.bmag_trend, "r-", lw=1.2, label="trend")
    ax.set_ylabel("|B| (nT)")
    ax.legend(loc="upper right", fontsize=8)

    # Panel 3: beta
    ax = axes[2]
    if enc.beta is not None:
        ax.semilogy(t_rel, enc.beta, "g-", lw=0.7)
        ax.axhline(1.0, color="gray", ls="--", lw=0.5)
    ax.set_ylabel("beta")

    # Panel 4: total pressure
    ax = axes[3]
    if enc.ptot_nPa is not None:
        ax.plot(t_rel, enc.ptot_nPa, "k-", lw=0.7)
    ax.set_ylabel("P_tot (nPa)")

    # Panel 5: s(t)
    ax = axes[4]
    s = enc.mapping.s_array
    if s is not None:
        ax.plot(t_rel[: len(s)], s, "m-", lw=0.8)
        # Bin boundaries
        for label, (lo, hi), color in [
            ("very near", bins.very_near, "red"),
            ("near", bins.near, "orange"),
            ("background", bins.background, "blue"),
        ]:
            ax.axhspan(lo, hi, alpha=0.1, color=color, label=label)
        ax.set_ylim(-0.05, 1.05)
        ax.legend(loc="upper right", fontsize=7, ncol=3)
    ax.set_ylabel("s")

    # Panel 6: metric + QC + eligibility summary
    ax = axes[5]
    ax.axis("off")
    m = enc.metrics

    # Status header
    status_str = getattr(enc, "scientific_status", "REVIEW_NEEDED")
    evaluable_str = "YES" if getattr(enc, "evaluable", False) else "NO"

    lines = [
        f"STATUS: {status_str}  |  Evaluable: {evaluable_str}",
        "",
        f"Dn = {m.Dn:.3f}" if m.Dn is not None else "Dn = N/A (not evaluable)",
        f"EB = {m.EB:.3f}" if m.EB is not None else "EB = N/A (not evaluable)",
        f"Δβ = {m.delta_beta:.3f}" if m.delta_beta is not None else "Δβ = N/A",
        f"ρ(n,B) = {m.rho_nB_trend:.3f}" if m.rho_nB_trend is not None else "ρ = N/A",
        f"Persistence = {m.persistence_frac:.2f}" if m.persistence_frac is not None else "Persist = N/A",
        f"Ptot smooth = {m.ptot_smoothness:.2f}" if m.ptot_smoothness is not None else "Ptot = N/A",
        "",
        f"Grade: {enc.qc.grade}",
    ]
    if enc.qc.grade_note:
        lines.append(f"  ({enc.qc.grade_note})")

    # Flag summary with tri-state display
    flag_strs = []
    for name, val in [("jet", enc.qc.jet_flag), ("wave", enc.qc.wave_flag),
                      ("transient", enc.qc.transient_flag), ("motion", enc.qc.motion_flag),
                      ("mixing", enc.qc.mixing_flag)]:
        if val is True:
            flag_strs.append(f"{name}=YES")
        elif val is False:
            flag_strs.append(f"{name}=no")
        else:
            flag_strs.append(f"{name}=UNKNOWN")
    lines.append(f"Flags: {' | '.join(flag_strs)}")

    occupancy = enc.mapping.occupancy
    if occupancy:
        lines.append(
            f"Occupancy — very_near: {occupancy.get('very_near', 0):.1%}  "
            f"near: {occupancy.get('near', 0):.1%}  "
            f"bg: {occupancy.get('background', 0):.1%}"
        )

    # Preflight reasons if any
    reasons = getattr(enc, "preflight_reasons", [])
    if reasons:
        lines.append("")
        lines.append("Preflight issues:")
        for r in reasons[:5]:  # max 5 lines
            lines.append(f"  - {r}")
    ax.text(
        0.02, 0.95, "\n".join(lines),
        transform=ax.transAxes, va="top", fontsize=10, family="monospace",
    )

    axes[-2].set_xlabel("Time (s)")
    fig.tight_layout(rect=[0, 0, 1, 0.96])

    out_path = output_dir / f"qc_{enc.encounter_id}.png"
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    log.info("QC report saved → %s", out_path)
    return out_path
