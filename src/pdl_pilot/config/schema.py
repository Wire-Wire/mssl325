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

    def config_hash(self) -> str:
        blob = self.model_dump_json(indent=None).encode()
        return hashlib.sha256(blob).hexdigest()[:12]


def load_config(path: str | Path) -> PipelineConfig:
    """Load and validate a YAML config file."""
    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    return PipelineConfig(**raw)
