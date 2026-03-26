"""Data adapters — fixture / synthetic / live."""
from pdl_pilot.data.synthetic import generate_synthetic_encounter
from pdl_pilot.data.provider import DataProvider, EncounterData, SourceMetadata
from pdl_pilot.data.synthetic_provider import SyntheticProvider
from pdl_pilot.data.cache import DataCache
from pdl_pilot.data.masking import mask_fill_values, MaskingSummary

__all__ = [
    "generate_synthetic_encounter",
    "DataProvider",
    "EncounterData",
    "SourceMetadata",
    "SyntheticProvider",
    "DataCache",
    "mask_fill_values",
    "MaskingSummary",
]
