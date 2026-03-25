"""
Local data cache for live THEMIS/OMNI downloads.

Phase 1.5 addition.  Provides deterministic cache paths, safe re-use
across runs, and explicit cache hit/miss reporting.

Design:
  data_cache/
    raw/                  ← CDF files as downloaded
      THD_L2_FGM/
        thd_l2_fgm_20120715_v01.cdf
    normalized/           ← Intermediate pandas/numpy artefacts
      <encounter_id>/
        fgm.npz
        mom.npz
        state.npz
        omni.npz
    cache_index.json      ← Metadata: what was cached when, from where
"""
from __future__ import annotations

import datetime
import hashlib
import json
import logging
from pathlib import Path
from typing import Any

log = logging.getLogger(__name__)


def _cache_key(dataset: str, tstart: str, tend: str, probe: str = "") -> str:
    """Deterministic cache key from query parameters."""
    blob = f"{dataset}|{tstart}|{tend}|{probe}".encode()
    return hashlib.sha256(blob).hexdigest()[:16]


class DataCache:
    """Minimal file-based cache with metadata tracking."""

    def __init__(self, cache_dir: str | Path, policy: str = "use"):
        self.root = Path(cache_dir)
        self.raw_dir = self.root / "raw"
        self.norm_dir = self.root / "normalized"
        self.index_path = self.root / "cache_index.json"
        self.policy = policy  # "use" | "refresh" | "skip"
        self._index: dict[str, Any] = {}
        self._load_index()

    def _load_index(self) -> None:
        if self.index_path.exists():
            try:
                with open(self.index_path, encoding="utf-8") as f:
                    self._index = json.load(f)
            except (json.JSONDecodeError, OSError):
                self._index = {}

    def _save_index(self) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        with open(self.index_path, "w", encoding="utf-8") as f:
            json.dump(self._index, f, indent=2)

    def raw_path(self, dataset: str, filename: str) -> Path:
        """Deterministic path for a raw CDF file."""
        d = self.raw_dir / dataset
        d.mkdir(parents=True, exist_ok=True)
        return d / filename

    def norm_path(self, encounter_id: str, label: str) -> Path:
        """Deterministic path for a normalized intermediate file."""
        d = self.norm_dir / encounter_id
        d.mkdir(parents=True, exist_ok=True)
        return d / f"{label}.npz"

    def has_raw(self, dataset: str, filename: str) -> bool:
        if self.policy == "skip":
            return False
        if self.policy == "refresh":
            return False
        return self.raw_path(dataset, filename).exists()

    def has_norm(self, encounter_id: str, label: str) -> bool:
        if self.policy in ("skip", "refresh"):
            return False
        return self.norm_path(encounter_id, label).exists()

    def record(
        self,
        key: str,
        *,
        dataset: str,
        trange: tuple[str, str],
        probe: str = "",
        files: list[str] | None = None,
        cache_hit: bool = False,
    ) -> None:
        """Record a cache entry in the index."""
        self._index[key] = {
            "dataset": dataset,
            "trange": list(trange),
            "probe": probe,
            "files": files or [],
            "cache_hit": cache_hit,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
        self._save_index()

    def get_record(self, key: str) -> dict | None:
        return self._index.get(key)

    def summary(self) -> dict:
        """Return a summary of cache state for provenance."""
        n_raw = sum(1 for _ in self.raw_dir.rglob("*") if _.is_file()) if self.raw_dir.exists() else 0
        n_norm = sum(1 for _ in self.norm_dir.rglob("*") if _.is_file()) if self.norm_dir.exists() else 0
        return {
            "cache_dir": str(self.root),
            "policy": self.policy,
            "raw_files_cached": n_raw,
            "normalized_files_cached": n_norm,
            "index_entries": len(self._index),
        }

    def clear(self) -> None:
        """Remove all cached files and reset index."""
        import shutil
        if self.raw_dir.exists():
            shutil.rmtree(self.raw_dir)
        if self.norm_dir.exists():
            shutil.rmtree(self.norm_dir)
        self._index = {}
        self._save_index()
        log.info("Cache cleared: %s", self.root)
