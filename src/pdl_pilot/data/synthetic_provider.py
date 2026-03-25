"""
Synthetic data provider — wraps the existing generator behind the
DataProvider interface.

Phase 1.5: preserves the existing synthetic path as a first-class provider.
"""
from __future__ import annotations

import datetime
import logging

from pdl_pilot.config.schema import EncounterSpec
from pdl_pilot.data.provider import DataProvider, EncounterData, SourceMetadata
from pdl_pilot.data.synthetic import generate_synthetic_encounter

log = logging.getLogger(__name__)


class SyntheticProvider(DataProvider):
    """Generates synthetic encounter data using the Phase-1 generator."""

    def __init__(self, seed: int = 42):
        self._seed = seed

    @property
    def name(self) -> str:
        return "synthetic"

    def fetch(self, spec: EncounterSpec, **kwargs) -> EncounterData:
        log.info("SyntheticProvider: generating data for %s (seed=%d)",
                 spec.encounter_id, self._seed)

        data = generate_synthetic_encounter(spec, seed=self._seed)

        metadata = SourceMetadata(
            provider="synthetic",
            dataset_ids=["synthetic_fixture"],
            variable_names=list(data.keys()),
            probe=spec.probe,
            requested_trange=(spec.time_start, spec.time_end),
            actual_trange=(spec.time_start, spec.time_end),
            retrieval_timestamp=datetime.datetime.now(
                datetime.timezone.utc
            ).isoformat(),
            cache_hit=False,
            quality_flags_available=False,
            extra={"seed": self._seed},
        )

        return EncounterData(
            time_unix=data["time_unix"],
            x_gsm_re=data["x_gsm_re"],
            y_gsm_re=data["y_gsm_re"],
            z_gsm_re=data["z_gsm_re"],
            density_cm3=data["density_cm3"],
            bmag_nT=data["bmag_nT"],
            beta=data["beta"],
            ptot_nPa=data["ptot_nPa"],
            vflow_kms=data["vflow_kms"],
            source_metadata=[metadata],
        )
