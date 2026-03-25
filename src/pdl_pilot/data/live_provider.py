"""
Live THEMIS + OMNI data provider via CDAWeb / cdasws.

Phase 1.5 addition.  Fetches, caches, normalizes, and returns real
spacecraft data through the same EncounterData interface as synthetic.

Datasets:
  - THEMIS FGM L2       — magnetic field
  - THEMIS MOM L2       — ion/plasma moments (default)
  - THEMIS STATE L2     — spacecraft position / ephemeris
  - OMNI HRO 1-min      — upstream solar-wind context

PROVISIONAL choices (documented, not frozen):
  - Backend: cdasws (CDAWeb SPDF REST API)
  - Resampling: linear interpolation onto common cadence
  - Gap handling: NaN fill for gaps > max_gap_seconds
"""
from __future__ import annotations

import datetime
import logging
from typing import Any

import numpy as np

from pdl_pilot.config.schema import EncounterSpec, LiveDataConfig
from pdl_pilot.data.provider import DataProvider, EncounterData, SourceMetadata
from pdl_pilot.data.cache import DataCache

log = logging.getLogger(__name__)

# Probe letter mapping: config probe "thd" → letter "d" for CDAWeb datasets
_PROBE_LETTER = {
    "tha": "a", "thb": "b", "thc": "c", "thd": "d", "the": "e",
}


def _resolve_dataset(template: str, probe_letter: str) -> str:
    """Resolve {probe} placeholder in dataset ID template.

    CDAWeb uses uppercase probe letters in dataset IDs (e.g. THD_L2_FGM).
    """
    return template.replace("{probe}", probe_letter.upper())


def _parse_time(s: str) -> datetime.datetime:
    """Parse ISO time string to UTC datetime."""
    dt = datetime.datetime.fromisoformat(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=datetime.timezone.utc)
    return dt


def _epoch_to_unix(epoch_ns: np.ndarray) -> np.ndarray:
    """Convert CDF epoch (nanoseconds since J2000 or similar) to POSIX seconds.

    cdasws returns datetimes — we handle both np.datetime64 arrays and
    raw float epoch arrays.
    """
    if hasattr(epoch_ns, 'dtype') and np.issubdtype(epoch_ns.dtype, np.datetime64):
        # numpy datetime64 → POSIX seconds
        epoch_1970 = np.datetime64('1970-01-01T00:00:00', 'ns')
        return (epoch_ns.astype('datetime64[ns]') - epoch_1970).astype(np.float64) / 1e9
    # Assume already float seconds
    return np.asarray(epoch_ns, dtype=np.float64)


def _interp_to_timeline(
    src_time: np.ndarray,
    src_data: np.ndarray,
    target_time: np.ndarray,
    method: str = "linear",
    max_gap: float = 30.0,
) -> np.ndarray:
    """Interpolate src_data onto target_time, inserting NaN for large gaps."""
    if len(src_time) == 0:
        return np.full_like(target_time, np.nan)

    if method == "nearest":
        idx = np.searchsorted(src_time, target_time)
        idx = np.clip(idx, 0, len(src_time) - 1)
        result = src_data[idx].astype(np.float64)
    else:
        result = np.interp(target_time, src_time, src_data.astype(np.float64))

    # Mask gaps: for each target point, find distance to nearest source point
    if max_gap > 0 and len(src_time) > 0:
        idx = np.searchsorted(src_time, target_time)
        idx = np.clip(idx, 0, len(src_time) - 1)
        dist = np.abs(target_time - src_time[idx])
        # Also check the previous index
        idx_prev = np.clip(idx - 1, 0, len(src_time) - 1)
        dist_prev = np.abs(target_time - src_time[idx_prev])
        min_dist = np.minimum(dist, dist_prev)
        result[min_dist > max_gap] = np.nan

    return result


class LiveProvider(DataProvider):
    """Fetches real THEMIS + OMNI data via cdasws from CDAWeb/SPDF."""

    def __init__(self, live_config: LiveDataConfig):
        self._cfg = live_config
        self._cache = DataCache(live_config.cache_dir, live_config.cache_policy)
        self._cdasws = None  # Lazy import

    @property
    def name(self) -> str:
        return "cdasws"

    def _get_cdasws(self):
        """Lazy-load cdasws to avoid import errors when not installed."""
        if self._cdasws is None:
            try:
                from cdasws import CdasWs
                self._cdasws = CdasWs()
                log.info("cdasws client initialized successfully")
            except ImportError:
                raise ImportError(
                    "Live data mode requires the 'cdasws' package. "
                    "Install with: pip install cdasws"
                )
        return self._cdasws

    def _fetch_dataset(
        self,
        dataset: str,
        variables: list[str],
        tstart: str,
        tend: str,
        encounter_id: str,
    ) -> tuple[dict[str, np.ndarray], SourceMetadata]:
        """Fetch one CDAWeb dataset, with caching."""
        cache_label = dataset.lower().replace(" ", "_")
        norm_path = self._cache.norm_path(encounter_id, cache_label)

        meta = SourceMetadata(
            provider="cdasws",
            dataset_ids=[dataset],
            variable_names=variables,
            requested_trange=(tstart, tend),
        )

        # Check normalized cache
        if self._cache.has_norm(encounter_id, cache_label):
            log.info("Cache HIT (normalized): %s / %s", encounter_id, cache_label)
            loaded = dict(np.load(str(norm_path), allow_pickle=True))
            meta.cache_hit = True
            meta.cache_path = str(norm_path)
            meta.retrieval_timestamp = datetime.datetime.now(
                datetime.timezone.utc
            ).isoformat()
            if "actual_tstart" in loaded and "actual_tend" in loaded:
                meta.actual_trange = (str(loaded["actual_tstart"]), str(loaded["actual_tend"]))
            return loaded, meta

        # Fetch from CDAWeb
        log.info("Fetching from CDAWeb: %s [%s → %s]", dataset, tstart, tend)
        cdas = self._get_cdasws()

        meta.retrieval_timestamp = datetime.datetime.now(
            datetime.timezone.utc
        ).isoformat()

        try:
            status, xr_data = cdas.get_data(dataset, variables, tstart, tend)
        except Exception as e:
            log.error("CDAWeb fetch failed for %s: %s", dataset, e)
            raise RuntimeError(f"CDAWeb fetch failed for {dataset}: {e}") from e

        if xr_data is None:
            raise RuntimeError(
                f"CDAWeb returned no data for {dataset} [{tstart} → {tend}]. "
                "Check dataset ID and time range."
            )

        meta.cache_hit = False

        # Convert xarray Dataset to dict of numpy arrays
        result: dict[str, np.ndarray] = {}
        for var in xr_data.data_vars:
            arr = xr_data[var].values
            result[var] = np.asarray(arr)

        # Extract time coordinate
        time_coords = [c for c in xr_data.coords if "epoch" in c.lower() or "time" in c.lower()]
        if time_coords:
            tc = time_coords[0]
            result["_time"] = np.asarray(xr_data.coords[tc].values)
            times = result["_time"]
            if len(times) > 0:
                meta.actual_trange = (str(times[0]), str(times[-1]))

        # Record remote file info if available
        if hasattr(xr_data, 'attrs'):
            for key in ('source', 'file', 'CDAWeb_URL'):
                if key in xr_data.attrs:
                    meta.remote_files.append(str(xr_data.attrs[key]))

        # Save to normalized cache
        if self._cfg.cache_policy != "skip":
            save_dict = dict(result)
            if meta.actual_trange[0]:
                save_dict["actual_tstart"] = meta.actual_trange[0]
                save_dict["actual_tend"] = meta.actual_trange[1]
            np.savez(str(norm_path), **{k: v for k, v in save_dict.items()
                                         if isinstance(v, np.ndarray)})
            meta.cache_path = str(norm_path)
            self._cache.record(
                f"{encounter_id}/{cache_label}",
                dataset=dataset,
                trange=(tstart, tend),
                files=[str(norm_path)],
                cache_hit=False,
            )
            log.info("Cached normalized data → %s", norm_path)

        return result, meta

    def fetch(self, spec: EncounterSpec, **kwargs) -> EncounterData:
        """Fetch and normalize THEMIS + OMNI data for one encounter."""
        probe_letter = _PROBE_LETTER.get(spec.probe, spec.probe[-1])
        probe_upper = probe_letter.upper()

        tstart = spec.time_start
        tend = spec.time_end
        dt_start = _parse_time(tstart)
        dt_end = _parse_time(tend)

        # Build analysis timeline
        duration_s = (dt_end - dt_start).total_seconds()
        cadence = self._cfg.resample_cadence_seconds
        n_pts = max(2, int(duration_s / cadence) + 1)
        t0_unix = dt_start.timestamp()
        target_time = np.linspace(t0_unix, t0_unix + duration_s, n_pts)

        all_metadata: list[SourceMetadata] = []

        # --- FGM: magnetic field ---
        fgm_ds = _resolve_dataset(self._cfg.fgm_dataset, probe_letter)
        fgm_vars = [
            f"th{probe_letter}_fgs_gsm",    # spin-fit GSM B-field vector
        ]
        try:
            fgm_data, fgm_meta = self._fetch_dataset(
                fgm_ds, fgm_vars, tstart, tend, spec.encounter_id
            )
            fgm_meta.probe = spec.probe
        except Exception as e:
            log.warning("FGM fetch failed, trying alternative variable names: %s", e)
            # Fallback: try btotal
            fgm_vars = [f"th{probe_letter}_fgs_btotal"]
            fgm_data, fgm_meta = self._fetch_dataset(
                fgm_ds, fgm_vars, tstart, tend, spec.encounter_id
            )
            fgm_meta.probe = spec.probe
            fgm_meta.fallback_used = "btotal_only"
        all_metadata.append(fgm_meta)

        # Extract |B| from FGM
        fgm_time_raw = _epoch_to_unix(fgm_data.get("_time", np.array([])))
        bvec_key = f"th{probe_letter}_fgs_gsm"
        btotal_key = f"th{probe_letter}_fgs_btotal"
        if bvec_key in fgm_data and fgm_data[bvec_key].ndim >= 2:
            bvec = fgm_data[bvec_key]
            bmag_raw = np.sqrt(np.sum(bvec**2, axis=-1))
        elif btotal_key in fgm_data:
            bmag_raw = fgm_data[btotal_key].astype(np.float64)
        else:
            log.warning("No recognized B-field variable found in FGM data")
            bmag_raw = np.array([])

        # --- MOM: plasma moments ---
        mom_ds = _resolve_dataset(self._cfg.mom_dataset, probe_letter)
        mom_vars = [
            f"th{probe_letter}_peim_density",        # ion density (cm^-3)
            f"th{probe_letter}_peim_velocity_gsm",   # bulk velocity GSM (km/s)
            f"th{probe_letter}_peim_ptot",            # total pressure (eV/cm^3)
        ]
        try:
            mom_data, mom_meta = self._fetch_dataset(
                mom_ds, mom_vars, tstart, tend, spec.encounter_id
            )
            mom_meta.probe = spec.probe
        except Exception as e:
            log.warning("MOM fetch issue: %s — trying reduced variable set", e)
            mom_vars = [f"th{probe_letter}_peim_density"]
            mom_data, mom_meta = self._fetch_dataset(
                mom_ds, mom_vars, tstart, tend, spec.encounter_id
            )
            mom_meta.probe = spec.probe
            mom_meta.fallback_used = "density_only"
        all_metadata.append(mom_meta)

        mom_time_raw = _epoch_to_unix(mom_data.get("_time", np.array([])))

        # --- STATE: ephemeris ---
        # Note: THEMIS STATE is L1, not L2 (THD_L1_STATE)
        state_ds = _resolve_dataset(self._cfg.state_dataset, probe_letter)
        state_vars = [
            f"th{probe_letter}_pos_gsm",   # position in GSM (km, converted to Re)
        ]
        try:
            state_data, state_meta = self._fetch_dataset(
                state_ds, state_vars, tstart, tend, spec.encounter_id
            )
            state_meta.probe = spec.probe
        except Exception as e:
            log.warning("STATE fetch issue: %s", e)
            state_data = {}
            state_meta = SourceMetadata(provider="cdasws", extra={"error": str(e)})
            state_meta.probe = spec.probe
        all_metadata.append(state_meta)

        state_time_raw = _epoch_to_unix(state_data.get("_time", np.array([])))

        # --- OMNI: upstream context ---
        omni_start = (dt_start - datetime.timedelta(
            minutes=self._cfg.omni_pre_window_minutes
        )).isoformat()
        omni_end = (dt_end + datetime.timedelta(
            minutes=self._cfg.omni_post_window_minutes
        )).isoformat()
        omni_vars = [
            "BZ_GSM",          # IMF Bz GSM
            "F",               # |B| total
            "Pressure",        # dynamic pressure
            "Mach_num",        # Alfven Mach number
            "flow_speed",      # solar wind speed
        ]
        try:
            omni_data, omni_meta = self._fetch_dataset(
                self._cfg.omni_dataset, omni_vars,
                omni_start, omni_end, spec.encounter_id
            )
        except Exception as e:
            log.warning("OMNI fetch issue: %s — upstream context will be partial", e)
            omni_data = {}
            omni_meta = SourceMetadata(provider="cdasws", extra={"error": str(e)})
        all_metadata.append(omni_meta)

        omni_time_raw = _epoch_to_unix(omni_data.get("_time", np.array([])))

        # ===== NORMALIZATION: resample onto target timeline =====
        max_gap = self._cfg.max_gap_seconds
        method = self._cfg.interpolation_method

        # B-field
        bmag = _interp_to_timeline(fgm_time_raw, bmag_raw, target_time, method, max_gap) \
            if len(bmag_raw) > 0 else np.full(n_pts, np.nan)

        # Density
        dens_key = f"th{probe_letter}_peim_density"
        density_raw = mom_data.get(dens_key, np.array([])).astype(np.float64)
        density = _interp_to_timeline(mom_time_raw, density_raw, target_time, method, max_gap) \
            if len(density_raw) > 0 else np.full(n_pts, np.nan)
        density = np.clip(density, 0.01, None)  # physical floor

        # Velocity
        vel_key = f"th{probe_letter}_peim_velocity_gsm"
        if vel_key in mom_data and mom_data[vel_key].ndim >= 2:
            vel_vec = mom_data[vel_key].astype(np.float64)
            vflow_raw = np.sqrt(np.sum(vel_vec**2, axis=-1))
        else:
            vflow_raw = np.full(len(mom_time_raw) if len(mom_time_raw) > 0 else 0, 200.0)
        vflow = _interp_to_timeline(mom_time_raw, vflow_raw, target_time, method, max_gap) \
            if len(vflow_raw) > 0 else np.full(n_pts, 200.0)

        # Total pressure and beta from MOM peim_ptot
        # peim_ptot is in eV/cm^3 — convert to nPa:
        #   1 eV = 1.6e-19 J,  1 cm^-3 = 1e6 m^-3
        #   P(Pa) = ptot(eV/cm^3) * 1.6e-19 * 1e6 = ptot * 1.6e-13
        #   P(nPa) = ptot * 1.6e-13 * 1e9 = ptot * 1.6e-4
        ptot_key = f"th{probe_letter}_peim_ptot"
        mu0 = 4 * np.pi * 1e-7
        p_magnetic_pa = (bmag * 1e-9)**2 / (2 * mu0)  # Pa
        p_magnetic_npa = p_magnetic_pa * 1e9             # nPa

        if ptot_key in mom_data:
            ptot_raw = mom_data[ptot_key].astype(np.float64)
            # peim_ptot is total (thermal) pressure in eV/cm^3
            ptot_evcm3 = _interp_to_timeline(mom_time_raw, ptot_raw, target_time, method, max_gap)
            p_thermal_npa = ptot_evcm3 * 1.6e-4  # nPa
            ptot = p_thermal_npa + p_magnetic_npa
            beta = np.where(p_magnetic_npa > 0, p_thermal_npa / p_magnetic_npa, np.nan)
        else:
            # Fallback: estimate from density with typical sheath temperature
            log.warning("No peim_ptot available — using T=200 eV fallback for beta/ptot")
            temp_eV = 200.0
            p_thermal_pa = density * 1e6 * temp_eV * 1.6e-19  # Pa
            ptot = (p_thermal_pa + p_magnetic_pa) * 1e9  # nPa
            beta = np.where(p_magnetic_pa > 0, p_thermal_pa / p_magnetic_pa, np.nan)

        # Position (GSM) — STATE provides km, convert to Re
        RE_KM = 6371.2
        pos_key = f"th{probe_letter}_pos_gsm"
        if pos_key in state_data and state_data[pos_key].ndim >= 2:
            pos_raw = state_data[pos_key].astype(np.float64) / RE_KM  # km → Re
            x_raw = _interp_to_timeline(state_time_raw, pos_raw[:, 0], target_time, method, max_gap)
            y_raw = _interp_to_timeline(state_time_raw, pos_raw[:, 1], target_time, method, max_gap)
            z_raw = _interp_to_timeline(state_time_raw, pos_raw[:, 2], target_time, method, max_gap)
        else:
            log.warning("No position data — using NaN placeholders")
            x_raw = np.full(n_pts, np.nan)
            y_raw = np.full(n_pts, np.nan)
            z_raw = np.full(n_pts, np.nan)

        # OMNI upstream context
        omni_bz = _interp_to_timeline(omni_time_raw, omni_data.get("BZ_GSM", np.array([])).astype(np.float64),
                                       target_time, "nearest", 120.0) \
            if "BZ_GSM" in omni_data else None
        omni_bt = _interp_to_timeline(omni_time_raw, omni_data.get("F", np.array([])).astype(np.float64),
                                       target_time, "nearest", 120.0) \
            if "F" in omni_data else None
        omni_dp = _interp_to_timeline(omni_time_raw, omni_data.get("Pressure", np.array([])).astype(np.float64),
                                       target_time, "nearest", 120.0) \
            if "Pressure" in omni_data else None
        omni_ma = _interp_to_timeline(omni_time_raw, omni_data.get("Mach_num", np.array([])).astype(np.float64),
                                       target_time, "nearest", 120.0) \
            if "Mach_num" in omni_data else None
        omni_vsw = _interp_to_timeline(omni_time_raw, omni_data.get("flow_speed", np.array([])).astype(np.float64),
                                        target_time, "nearest", 120.0) \
            if "flow_speed" in omni_data else None

        # Quality notes
        quality_notes = []
        nan_frac_b = np.sum(np.isnan(bmag)) / n_pts
        nan_frac_n = np.sum(np.isnan(density)) / n_pts
        if nan_frac_b > 0.1:
            quality_notes.append(f"FGM NaN fraction: {nan_frac_b:.1%}")
        if nan_frac_n > 0.1:
            quality_notes.append(f"MOM density NaN fraction: {nan_frac_n:.1%}")

        return EncounterData(
            time_unix=target_time,
            x_gsm_re=x_raw,
            y_gsm_re=y_raw,
            z_gsm_re=z_raw,
            density_cm3=density,
            bmag_nT=bmag,
            beta=beta,
            ptot_nPa=ptot,
            vflow_kms=vflow,
            omni_bz_gsm_nT=omni_bz,
            omni_bt_nT=omni_bt,
            omni_dp_nPa=omni_dp,
            omni_mach_alfven=omni_ma,
            omni_flow_speed_kms=omni_vsw,
            quality_notes=quality_notes,
            source_metadata=all_metadata,
        )
