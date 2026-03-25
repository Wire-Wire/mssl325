"""
Pipeline configuration schema with Pydantic validation.

Design note: every analysis-relevant parameter lives here so that
runs are fully reproducible from config alone.
Ref: 2013_sandve_ten-rules-reproducible-computational-research
"""
from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Sub-schemas
# ---------------------------------------------------------------------------

class BinConfig(BaseModel):
    """Configurable s-bin edges.  Ref: blueprint §5.3 dual near-bin design."""
    very_near: tuple[float, float] = (0.0, 0.2)
    near: tuple[float, float] = (0.2, 0.4)
    background: tuple[float, float] = (0.6, 1.0)


class BoundaryModelConfig(BaseModel):
    """Which empirical boundary models to use."""
    magnetopause: Literal["shue1998"] = "shue1998"
    bow_shock: Literal["merka2005"] = "merka2005"
    # PROVISIONAL: distance along Sun-Earth line first (blueprint §5.1)
    distance_direction: Literal["sun_earth_line"] = "sun_earth_line"


class FilterConfig(BaseModel):
    """Trend / high-frequency separation."""
    trend_window_seconds: float = Field(
        default=120.0,
        description="Running-median window for trend extraction (seconds).",
    )
    min_sheath_duration_seconds: float = Field(
        default=300.0,
        description="Minimum usable sheath interval duration.",
    )


class UncertaintyConfig(BaseModel):
    """Phase-1 simple perturbation envelope for boundary models.
    Ref: 2019_walsh_solar-wind-measurement-uncertainty-geospace
    """
    mp_standoff_delta_re: float = Field(
        default=0.5,
        description="±perturbation on MP standoff distance (Re) for s-uncertainty.",
    )
    bs_standoff_delta_re: float = Field(
        default=1.0,
        description="±perturbation on BS standoff distance (Re) for s-uncertainty.",
    )


class EncounterSpec(BaseModel):
    """Specification of one encounter for pilot runs."""
    encounter_id: str
    spacecraft: str = "themis"
    probe: str = "thd"
    time_start: str
    time_end: str
    crossing_count: int = 1
    notes: str = ""


class LiveDataConfig(BaseModel):
    """Configuration for live THEMIS/OMNI data retrieval.

    Phase 1.5 addition.  All choices here are PROVISIONAL — they
    configure the real-data bridge but do not represent frozen science
    decisions.
    """
    backend: Literal["cdasws"] = Field(
        default="cdasws",
        description="PROVISIONAL: live data backend.  Only cdasws supported in Phase 1.5.",
    )
    # THEMIS dataset identifiers (CDAWeb naming)
    fgm_dataset: str = Field(
        default="TH{probe}_L2_FGM",
        description="CDAWeb dataset ID template for THEMIS FGM L2.  {probe} is replaced at runtime.",
    )
    mom_dataset: str = Field(
        default="TH{probe}_L2_MOM",
        description="CDAWeb dataset ID template for THEMIS MOM L2 ion moments.",
    )
    state_dataset: str = Field(
        default="TH{probe}_L1_STATE",
        description="CDAWeb dataset ID template for THEMIS STATE/ephemeris (L1 product).",
    )
    omni_dataset: str = Field(
        default="OMNI_HRO_1MIN",
        description="CDAWeb dataset ID for OMNI high-res 1-min data.",
    )

    # OMNI pre-encounter context window
    omni_pre_window_minutes: float = Field(
        default=30.0,
        description="PROVISIONAL: minutes of OMNI data to load before encounter start for upstream context.",
    )
    omni_post_window_minutes: float = Field(
        default=10.0,
        description="PROVISIONAL: minutes of OMNI data to load after encounter end.",
    )

    # Interpolation / resampling
    resample_cadence_seconds: float = Field(
        default=3.0,
        description="PROVISIONAL: target cadence for resampled analysis timeline (seconds).",
    )
    interpolation_method: Literal["linear", "nearest"] = Field(
        default="linear",
        description="PROVISIONAL: interpolation method for resampling onto analysis timeline.",
    )
    max_gap_seconds: float = Field(
        default=30.0,
        description="PROVISIONAL: gaps larger than this are filled with NaN, not interpolated.",
    )

    # Cache policy
    cache_dir: str = Field(
        default="data_cache",
        description="Local cache directory for downloaded CDF files and normalized intermediates.",
    )
    cache_policy: Literal["use", "refresh", "skip"] = Field(
        default="use",
        description="'use': reuse cached files; 'refresh': re-download; 'skip': no caching.",
    )


class PipelineConfig(BaseModel):
    """Top-level configuration for a PDL pilot run."""

    run_label: str = "pilot"
    bins: BinConfig = BinConfig()
    boundary_models: BoundaryModelConfig = BoundaryModelConfig()
    filters: FilterConfig = FilterConfig()
    uncertainty: UncertaintyConfig = UncertaintyConfig()
    encounters: list[EncounterSpec] = []
    output_dir: str = "runs"
    data_source: Literal["synthetic", "fixture", "live"] = "fixture"
    random_seed: int = 42
    live: LiveDataConfig = LiveDataConfig()

    def config_hash(self) -> str:
        blob = self.model_dump_json(indent=None).encode()
        return hashlib.sha256(blob).hexdigest()[:12]


def load_config(path: str | Path) -> PipelineConfig:
    """Load and validate a YAML config file."""
    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    return PipelineConfig(**raw)
