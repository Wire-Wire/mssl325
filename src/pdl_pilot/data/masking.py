"""
Fill-value and sentinel masking for live data.

OMNI and CDAWeb datasets use numeric sentinel fill values (e.g. 9999.99,
99999.9, 1e31) to represent missing or bad data.  These must be replaced
with NaN *before* any summary statistics, boundary-model inputs, or metric
calculations to prevent silent corruption.

Priority order:
  1. Variable metadata / attrs (FILLVAL, VALIDMIN, VALIDMAX) if available
  2. Explicit fallback tables for known OMNI / THEMIS sentinel patterns
  3. Log when fallback was used

Ref: OMNI documentation — https://omniweb.gsfc.nasa.gov/html/HRO_data.html
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field

import numpy as np

log = logging.getLogger(__name__)


# ---- Known sentinel / fill-value patterns for OMNI HRO 1-min ----
# These are OMNI's documented fill values per variable.
OMNI_FILL_VALUES: dict[str, list[float]] = {
    "BZ_GSM":     [9999.99],
    "BY_GSM":     [9999.99],
    "BX_GSE":     [9999.99],
    "F":          [9999.99],
    "Pressure":   [99.99],
    "Mach_num":   [999.9],
    "flow_speed": [99999.9],
}

# Generous fallback: any value above this is almost certainly a fill
_OMNI_GENERIC_UPPER = 9000.0

# THEMIS MOM / FGM fill patterns (CDF FILLVAL is typically -1e31 or 1e31)
_CDF_FILL_ABS_THRESHOLD = 1e30


@dataclass
class MaskingSummary:
    """Per-variable masking statistics for provenance."""
    variable: str
    n_total: int = 0
    n_masked_fill: int = 0        # masked by fill-value detection
    n_masked_range: int = 0       # masked by VALIDMIN/VALIDMAX
    n_nan_input: int = 0          # already NaN on entry
    n_valid: int = 0
    fill_method: str = "none"     # "attrs" | "omni_table" | "generic" | "none"
    notes: list[str] = field(default_factory=list)

    @property
    def masked_fraction(self) -> float:
        if self.n_total == 0:
            return 0.0
        return (self.n_masked_fill + self.n_masked_range) / self.n_total

    @property
    def valid_fraction(self) -> float:
        if self.n_total == 0:
            return 0.0
        return self.n_valid / self.n_total

    def to_dict(self) -> dict:
        return {
            "variable": self.variable,
            "n_total": self.n_total,
            "n_masked_fill": self.n_masked_fill,
            "n_masked_range": self.n_masked_range,
            "n_nan_input": self.n_nan_input,
            "n_valid": self.n_valid,
            "masked_fraction": round(self.masked_fraction, 4),
            "valid_fraction": round(self.valid_fraction, 4),
            "fill_method": self.fill_method,
            "notes": self.notes,
        }


def mask_fill_values(
    arr: np.ndarray,
    variable_name: str,
    *,
    fillval: float | None = None,
    validmin: float | None = None,
    validmax: float | None = None,
    dataset_type: str = "unknown",
) -> tuple[np.ndarray, MaskingSummary]:
    """Replace fill/sentinel values with NaN.

    Parameters
    ----------
    arr : array
        Input data (modified copy returned; original unchanged).
    variable_name : str
        CDAWeb variable name for table lookup.
    fillval : float, optional
        Explicit FILLVAL from variable metadata/attrs.
    validmin, validmax : float, optional
        Valid range from variable metadata/attrs.
    dataset_type : str
        "omni", "themis_fgm", "themis_mom", "themis_state", or "unknown".
        Used for fallback sentinel detection.

    Returns
    -------
    masked : np.ndarray
        Copy with fills replaced by NaN.
    summary : MaskingSummary
        Statistics of what was masked and how.
    """
    if arr is None or len(arr) == 0:
        return arr, MaskingSummary(variable=variable_name)

    out = arr.astype(np.float64, copy=True)
    summary = MaskingSummary(variable=variable_name, n_total=len(out))

    # Count pre-existing NaN
    nan_mask = np.isnan(out)
    summary.n_nan_input = int(np.sum(nan_mask))

    # --- Priority 1: attrs-based masking ---
    if fillval is not None:
        fill_mask = np.isclose(out, fillval, atol=0.01) & ~nan_mask
        n_fill = int(np.sum(fill_mask))
        if n_fill > 0:
            out[fill_mask] = np.nan
            summary.n_masked_fill += n_fill
            summary.fill_method = "attrs"
            log.debug("Masked %d fill values (FILLVAL=%.2f) in %s",
                      n_fill, fillval, variable_name)

    if validmin is not None:
        range_lo = (~np.isnan(out)) & (out < validmin)
        n_lo = int(np.sum(range_lo))
        if n_lo > 0:
            out[range_lo] = np.nan
            summary.n_masked_range += n_lo

    if validmax is not None:
        range_hi = (~np.isnan(out)) & (out > validmax)
        n_hi = int(np.sum(range_hi))
        if n_hi > 0:
            out[range_hi] = np.nan
            summary.n_masked_range += n_hi

    # --- Priority 2: known fill-value tables ---
    if summary.fill_method == "none" and dataset_type == "omni":
        known = OMNI_FILL_VALUES.get(variable_name)
        if known:
            for fv in known:
                fill_mask = np.isclose(out, fv, atol=0.1) & ~np.isnan(out)
                n_fv = int(np.sum(fill_mask))
                if n_fv > 0:
                    out[fill_mask] = np.nan
                    summary.n_masked_fill += n_fv
                    summary.fill_method = "omni_table"
                    summary.notes.append(f"OMNI fill {fv} hit {n_fv} points")
                    log.info("Masked %d OMNI fill values (%.1f) in %s",
                             n_fv, fv, variable_name)
        else:
            # Generic OMNI fallback
            generic = (~np.isnan(out)) & (np.abs(out) > _OMNI_GENERIC_UPPER)
            n_gen = int(np.sum(generic))
            if n_gen > 0:
                out[generic] = np.nan
                summary.n_masked_fill += n_gen
                summary.fill_method = "generic"
                summary.notes.append(f"Generic OMNI sentinel >{_OMNI_GENERIC_UPPER}")
                log.info("Masked %d generic OMNI sentinels in %s",
                         n_gen, variable_name)

    # CDF fill (THEMIS)
    if summary.fill_method == "none" and dataset_type.startswith("themis"):
        cdf_mask = (~np.isnan(out)) & (np.abs(out) > _CDF_FILL_ABS_THRESHOLD)
        n_cdf = int(np.sum(cdf_mask))
        if n_cdf > 0:
            out[cdf_mask] = np.nan
            summary.n_masked_fill += n_cdf
            summary.fill_method = "generic"
            summary.notes.append(f"CDF fill |val|>{_CDF_FILL_ABS_THRESHOLD}")
            log.info("Masked %d CDF fill values in %s", n_cdf, variable_name)

    # Final valid count
    summary.n_valid = int(np.sum(np.isfinite(out)))
    return out, summary
