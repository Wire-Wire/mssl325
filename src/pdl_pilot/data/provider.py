"""
Source-data provider abstraction.

Thin interface so the pipeline can request magnetic field, plasma moments,
ephemeris, and upstream context without caring whether the source is
synthetic or live THEMIS/OMNI.

Phase 1.5 addition — keeps synthetic as first-class provider.
"""
from __future__ import annotations

import abc
import logging
from dataclasses import dataclass, field
from typing import Any

import numpy as np

from pdl_pilot.config.schema import EncounterSpec

log = logging.getLogger(__name__)


@dataclass
class SourceMetadata:
    """Provenance metadata for a single data retrieval."""
    provider: str = "unknown"          # "synthetic" | "cdasws" | ...
    dataset_ids: list[str] = field(default_factory=list)
    variable_names: list[str] = field(default_factory=list)
    probe: str = ""
    requested_trange: tuple[str, str] = ("", "")
    actual_trange: tuple[str, str] = ("", "")
    remote_files: list[str] = field(default_factory=list)
    retrieval_timestamp: str = ""
    cache_hit: bool = False
    cache_path: str = ""
    fallback_used: str = ""
    quality_flags_available: bool = False
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items()}


@dataclass
class EncounterData:
    """Normalized data bundle consumed by the encounter pipeline.

    All arrays share the same time axis (time_unix).
    Units are fixed:
      - time_unix: POSIX seconds (float64)
      - positions: Re in GSM
      - density: cm^-3
      - bmag: nT
      - beta: dimensionless
      - ptot: nPa
      - vflow: km/s
    """
    time_unix: np.ndarray
    x_gsm_re: np.ndarray
    y_gsm_re: np.ndarray
    z_gsm_re: np.ndarray
    density_cm3: np.ndarray
    bmag_nT: np.ndarray
    beta: np.ndarray
    ptot_nPa: np.ndarray
    vflow_kms: np.ndarray

    # Upstream context (OMNI) — may be None for synthetic
    omni_bx_gse_nT: np.ndarray | None = None    # radial component for cone angle
    omni_by_gsm_nT: np.ndarray | None = None     # transverse component for clock angle
    omni_bz_gsm_nT: np.ndarray | None = None
    omni_bt_nT: np.ndarray | None = None
    omni_dp_nPa: np.ndarray | None = None
    omni_mach_alfven: np.ndarray | None = None
    omni_flow_speed_kms: np.ndarray | None = None

    # Quality information
    density_quality: np.ndarray | None = None   # 0=good, >0=degraded
    bmag_quality: np.ndarray | None = None
    quality_notes: list[str] = field(default_factory=list)

    # Source metadata for provenance
    source_metadata: list[SourceMetadata] = field(default_factory=list)

    def to_legacy_dict(self) -> dict[str, np.ndarray]:
        """Convert to the dict format used by Phase-1 synthetic generator."""
        return {
            "time_unix": self.time_unix,
            "x_gsm_re": self.x_gsm_re,
            "y_gsm_re": self.y_gsm_re,
            "z_gsm_re": self.z_gsm_re,
            "density_cm3": self.density_cm3,
            "bmag_nT": self.bmag_nT,
            "beta": self.beta,
            "ptot_nPa": self.ptot_nPa,
            "vflow_kms": self.vflow_kms,
        }


class DataProvider(abc.ABC):
    """Abstract base for encounter data providers."""

    @abc.abstractmethod
    def fetch(self, spec: EncounterSpec, **kwargs) -> EncounterData:
        """Fetch and normalize data for one encounter specification.

        Must return an EncounterData with all required fields populated
        and source_metadata filled for provenance tracking.
        """
        ...

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Short provider name for logging and provenance."""
        ...
