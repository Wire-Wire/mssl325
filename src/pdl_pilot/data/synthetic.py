"""
Synthetic encounter data generator for pipeline smoke-testing.

Produces a fake but physically plausible sheath traversal with an
embedded PDL-like signature (density dip + B enhancement near MP).
This is NOT science data — it exists only to prove the pipeline works.
"""
from __future__ import annotations

import numpy as np

from pdl_pilot.config.schema import EncounterSpec


def generate_synthetic_encounter(
    spec: EncounterSpec, seed: int = 42
) -> dict[str, np.ndarray]:
    """Return dict of time series arrays for one synthetic encounter.

    The spacecraft sweeps from near the bow shock toward the
    magnetopause and back, with a PDL-like signature near s=0.
    """
    rng = np.random.default_rng(seed)
    n_pts = 600  # ~10 min at 1 s cadence
    t = np.linspace(0, 600, n_pts)

    # Spacecraft X position: start ~13 Re, sweep inward to ~10 Re, back
    x_gsm = 13.0 - 3.0 * np.sin(np.pi * t / 600)

    # Ambient sheath: n ~ 15 cm^-3, B ~ 20 nT
    n_base = 15.0 + 2.0 * rng.normal(size=n_pts)
    b_base = 20.0 + 1.5 * rng.normal(size=n_pts)

    # PDL-like perturbation near the magnetopause (x ~ 10 Re)
    pdl_envelope = np.exp(-((x_gsm - 10.3) ** 2) / (2 * 0.4**2))
    density = n_base * (1.0 - 0.5 * pdl_envelope)  # depletion
    bmag = b_base * (1.0 + 0.4 * pdl_envelope)     # enhancement

    density = np.clip(density, 0.5, None)
    bmag = np.clip(bmag, 1.0, None)

    # Derived: beta = n k T / (B^2 / 2 mu0).  Use approximate scaling.
    temp_eV = 200.0  # typical sheath ion temperature
    beta = 4.03e-11 * density * 1e6 * temp_eV * 1.6e-19 / (
        (bmag * 1e-9) ** 2 / (2 * 4 * np.pi * 1e-7)
    )
    # Total pressure (thermal + magnetic) in nPa
    p_thermal = density * 1e6 * temp_eV * 1.6e-19 * 1e9  # nPa
    p_mag = (bmag * 1e-9) ** 2 / (2 * 4 * np.pi * 1e-7) * 1e9
    ptot = p_thermal + p_mag

    # Bulk flow speed
    vflow = 200.0 + 50.0 * rng.normal(size=n_pts)
    vflow = np.clip(vflow, 50.0, None)

    return {
        "time_unix": t + 1e9,  # fake epoch
        "x_gsm_re": x_gsm,
        "y_gsm_re": np.zeros(n_pts),
        "z_gsm_re": np.zeros(n_pts),
        "density_cm3": density,
        "bmag_nT": bmag,
        "beta": beta,
        "ptot_nPa": ptot,
        "vflow_kms": vflow,
    }
