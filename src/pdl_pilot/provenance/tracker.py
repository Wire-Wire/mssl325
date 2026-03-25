"""
Provenance tracker: captures run_id, config hash, git state,
environment, and writes run manifest.

Ref: 2013_sandve_ten-rules-reproducible-computational-research
Ref: 2016_steegen_multiverse-analysis-transparency
"""
from __future__ import annotations

import datetime
import json
import logging
import platform
import shutil
import subprocess
import uuid
from pathlib import Path

import yaml

from pdl_pilot.config.schema import PipelineConfig

log = logging.getLogger(__name__)


class ProvenanceTracker:
    """Creates and manages a run output directory with full provenance."""

    def __init__(self, config: PipelineConfig):
        self.config = config
        ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        self.run_id = f"{ts}_{uuid.uuid4().hex[:8]}"
        self.run_dir = Path(config.output_dir) / self.run_id
        self.run_dir.mkdir(parents=True, exist_ok=True)
        # Phase 1.5: source-data provenance collection
        self._source_metadata: dict[str, list[dict]] = {}
        self._cache_summary: dict | None = None
        self._setup_logging()

    # ------------------------------------------------------------------
    def record_source_metadata(self, encounter_id: str, metadata_list: list) -> None:
        """Record source-data metadata for one encounter (Phase 1.5)."""
        self._source_metadata[encounter_id] = [
            m.to_dict() if hasattr(m, "to_dict") else m for m in metadata_list
        ]

    def record_cache_summary(self, summary: dict) -> None:
        """Record cache state summary (Phase 1.5)."""
        self._cache_summary = summary

    # ------------------------------------------------------------------
    def _setup_logging(self) -> None:
        fh = logging.FileHandler(self.run_dir / "run.log", encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fmt = logging.Formatter("%(asctime)s %(levelname)-8s %(name)s  %(message)s")
        fh.setFormatter(fmt)
        root = logging.getLogger()
        root.addHandler(fh)
        root.setLevel(logging.DEBUG)
        # console handler (INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(fmt)
        root.addHandler(ch)

    # ------------------------------------------------------------------
    def freeze_config(self) -> Path:
        """Write a frozen copy of the config YAML into the run directory."""
        out = self.run_dir / "config_used.yaml"
        with open(out, "w") as f:
            yaml.dump(self.config.model_dump(mode="json"), f, sort_keys=False)
        log.info("Config frozen → %s", out)
        return out

    # ------------------------------------------------------------------
    def write_manifest(self, extra: dict | None = None) -> Path:
        """Write run_manifest.json capturing full provenance."""
        manifest = {
            "run_id": self.run_id,
            "config_hash": self.config.config_hash(),
            "data_source": self.config.data_source,
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "git_commit": self._git_hash(),
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "packages": self._key_packages(),
            "encounter_ids": [e.encounter_id for e in self.config.encounters],
        }
        # Phase 1.5: include live-data source metadata if present
        if self._source_metadata:
            manifest["source_data"] = self._source_metadata
        if self._cache_summary:
            manifest["cache_summary"] = self._cache_summary
        if extra:
            manifest.update(extra)
        out = self.run_dir / "run_manifest.json"
        with open(out, "w") as f:
            json.dump(manifest, f, indent=2, default=str)
        log.info("Manifest written → %s", out)
        return out

    # ------------------------------------------------------------------
    @staticmethod
    def _git_hash() -> str | None:
        try:
            return (
                subprocess.check_output(
                    ["git", "rev-parse", "HEAD"],
                    stderr=subprocess.DEVNULL,
                )
                .decode()
                .strip()
            )
        except Exception:
            return None

    @staticmethod
    def _key_packages() -> dict[str, str]:
        pkgs: dict[str, str] = {}
        for name in ("numpy", "scipy", "matplotlib", "pydantic", "pyyaml",
                     "cdasws", "cdflib"):
            try:
                mod = __import__(name)
                pkgs[name] = getattr(mod, "__version__", "?")
            except ImportError:
                pass
        return pkgs
