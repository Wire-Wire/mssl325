"""
Encounter data model.

The encounter — not the raw crossing — is the statistical unit.
Ref: blueprint §6.1–6.6

Each encounter object carries metadata, upstream context, mapping,
metrics, and QC in a single serialisable container.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any

import numpy as np


@dataclass
class UpstreamSummary:
    """Averaged OMNI / upstream context for pre-encounter window.
    Ref: 2019_vokhmyanin_omni-imf-data-quality-evaluation
    """
    bz_gsm_nT: float | None = None
    bt_nT: float | None = None
    cone_angle_deg: float | None = None
    clock_angle_deg: float | None = None
    dp_nPa: float | None = None
    mach_alfven: float | None = None
    stability_flag: str = "unknown"  # stable / variable / unknown


@dataclass
class MappingResult:
    """Boundary model outputs and s(t) mapping.
    Ref: 1998_shue_magnetopause-location-extreme-solar-wind
    Ref: 2005_merka_bow-shock-3d-position-shape-mach-number
    """
    mp_model: str = "shue1998"
    bs_model: str = "merka2005"
    mp_standoff_re: float | None = None
    bs_standoff_re: float | None = None
    s_array: np.ndarray | None = None       # s(t), values in [0,1]
    s_sanity_ok: bool = True
    s_uncertainty_lo: np.ndarray | None = None
    s_uncertainty_hi: np.ndarray | None = None
    occupancy: dict[str, float] = field(default_factory=dict)
    model_inputs: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        d = {
            "mp_model": self.mp_model,
            "bs_model": self.bs_model,
            "mp_standoff_re": self.mp_standoff_re,
            "bs_standoff_re": self.bs_standoff_re,
            "s_sanity_ok": self.s_sanity_ok,
            "occupancy": self.occupancy,
            "model_inputs": self.model_inputs,
        }
        if self.s_array is not None:
            d["s_stats"] = {
                "min": float(np.nanmin(self.s_array)),
                "max": float(np.nanmax(self.s_array)),
                "mean": float(np.nanmean(self.s_array)),
                "n_points": int(self.s_array.size),
            }
        return d


@dataclass
class MetricBundle:
    """Core PDL detector metrics.  Ref: blueprint §6.3."""
    Dn: float | None = None             # median(n_near) / median(n_bg)
    EB: float | None = None             # median(|B|_near) / median(|B|_bg)
    delta_beta: float | None = None     # median(beta_near) - median(beta_bg)
    rho_nB_trend: float | None = None   # trend-scale anti-correlation
    ptot_smoothness: float | None = None
    persistence_frac: float | None = None
    fluctuation_amp: float | None = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items()}


@dataclass
class QCFlags:
    """Confounder and quality flags.
    Ref: 2013_archer_magnetosheath-dynamic-pressure-enhancements (jets)
    Ref: 2008_soucek_magnetosheath-mirror-modes-cluster (mirror modes)
    Ref: 2020_raptis_classifying-magnetosheath-jets-mms (jets)
    """
    jet_flag: bool = False
    wave_flag: bool = False
    transient_flag: bool = False
    motion_flag: bool = False
    mixing_flag: bool = False
    grade: str = "ungraded"  # Gold / Silver / Bronze / ungraded
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items()}


@dataclass
class Encounter:
    """Top-level encounter container — the project's statistical unit."""
    encounter_id: str
    spacecraft: str = "themis"
    probe: str = ""
    time_start: str = ""
    time_end: str = ""
    crossing_count: int = 1

    # Geometry metadata
    position_gsm_re: tuple[float, float, float] | None = None
    mlt_hours: float | None = None
    sza_deg: float | None = None
    abs_z_re: float | None = None

    # Sub-blocks
    upstream: UpstreamSummary = field(default_factory=UpstreamSummary)
    mapping: MappingResult = field(default_factory=MappingResult)
    metrics: MetricBundle = field(default_factory=MetricBundle)
    qc: QCFlags = field(default_factory=QCFlags)

    # Time series (not serialised to JSON directly)
    time_unix: np.ndarray | None = None
    density_cm3: np.ndarray | None = None
    bmag_nT: np.ndarray | None = None
    beta: np.ndarray | None = None
    ptot_nPa: np.ndarray | None = None
    vflow_kms: np.ndarray | None = None

    # Trend / residual decomposition
    density_trend: np.ndarray | None = None
    bmag_trend: np.ndarray | None = None
    density_residual: np.ndarray | None = None
    bmag_residual: np.ndarray | None = None

    # Artifact paths
    artifact_paths: dict[str, str] = field(default_factory=dict)

    def to_summary_dict(self) -> dict:
        """Serialisable summary (no large arrays)."""
        return {
            "encounter_id": self.encounter_id,
            "spacecraft": self.spacecraft,
            "probe": self.probe,
            "time_start": self.time_start,
            "time_end": self.time_end,
            "crossing_count": self.crossing_count,
            "position_gsm_re": self.position_gsm_re,
            "mlt_hours": self.mlt_hours,
            "sza_deg": self.sza_deg,
            "abs_z_re": self.abs_z_re,
            "upstream": self.upstream.__dict__,
            "mapping": self.mapping.to_dict(),
            "metrics": self.metrics.to_dict(),
            "qc": self.qc.to_dict(),
            "artifact_paths": self.artifact_paths,
        }

    def save_json(self, path: Path) -> None:
        with open(path, "w") as f:
            json.dump(self.to_summary_dict(), f, indent=2, default=str)
