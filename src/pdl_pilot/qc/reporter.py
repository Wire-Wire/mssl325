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
) -> QCFlags:
    """Compute minimal confounder flags.

    Phase-1: simple threshold-based flags, NOT final classification.
    """
    flags = QCFlags()
    warnings: list[str] = []

    # Jet flag: dynamic-pressure spike > 2× median in sheath
    if vflow is not None and enc.density_cm3 is not None:
        dp_proxy = enc.density_cm3 * vflow**2
        med_dp = np.nanmedian(dp_proxy)
        if med_dp > 0 and np.nanmax(dp_proxy) > 2.0 * med_dp:
            flags.jet_flag = True
            warnings.append("Possible jet: Pdyn spike > 2× median")

    # Wave flag: high fluctuation amplitude relative to trend
    if density_residual is not None and enc.density_trend is not None:
        trend_med = np.nanmedian(np.abs(enc.density_trend))
        if trend_med > 0:
            rel_fluct = np.nanstd(density_residual) / trend_med
            if rel_fluct > 0.3:
                flags.wave_flag = True
                warnings.append(f"High fluctuation amplitude: {rel_fluct:.2f}")

    # Motion flag: multiple crossings
    if enc.crossing_count > 2:
        flags.motion_flag = True
        warnings.append(f"Multiple crossings ({enc.crossing_count})")

    # s-sanity
    if not enc.mapping.s_sanity_ok:
        warnings.append("s-mapping sanity check failed")

    flags.warnings = warnings

    # Simple grading
    n_flags = sum([flags.jet_flag, flags.wave_flag, flags.transient_flag,
                   flags.motion_flag, flags.mixing_flag])
    if n_flags == 0:
        flags.grade = "Gold"
    elif n_flags == 1:
        flags.grade = "Silver"
    else:
        flags.grade = "Bronze"

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

    # Panel 6: metric + QC summary
    ax = axes[5]
    ax.axis("off")
    m = enc.metrics
    lines = [
        f"Dn = {m.Dn:.3f}" if m.Dn is not None else "Dn = N/A",
        f"EB = {m.EB:.3f}" if m.EB is not None else "EB = N/A",
        f"Δβ = {m.delta_beta:.3f}" if m.delta_beta is not None else "Δβ = N/A",
        f"ρ(n,B) = {m.rho_nB_trend:.3f}" if m.rho_nB_trend is not None else "ρ = N/A",
        f"Persistence = {m.persistence_frac:.2f}" if m.persistence_frac is not None else "Persist = N/A",
        f"Ptot smooth = {m.ptot_smoothness:.2f}" if m.ptot_smoothness is not None else "Ptot = N/A",
        f"Grade: {enc.qc.grade}",
        f"Flags: {'  '.join(enc.qc.warnings) if enc.qc.warnings else 'none'}",
    ]
    occupancy = enc.mapping.occupancy
    if occupancy:
        lines.append(
            f"Occupancy — very_near: {occupancy.get('very_near', 0):.1%}  "
            f"near: {occupancy.get('near', 0):.1%}  "
            f"bg: {occupancy.get('background', 0):.1%}"
        )
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
