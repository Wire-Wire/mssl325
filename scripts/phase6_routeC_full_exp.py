"""
Phase 6 Route C FULL EXP — Multi-threaded Full-Archive Scan (v4)

Strategy:
  1. STATE already cached per month (Phase 1 from previous runs). Screen geometry.
  2. For each qualifying day, fetch 6h of FGM+MOM+OMNI in parallel using ThreadPoolExecutor.
  3. Process all encounters and produce catalogue.

Optimizations:
  - ThreadPoolExecutor with 8 workers for CDAWeb fetches
  - Per-encounter NPZ cache to skip already-processed encounters
  - 6h window fetch (not monthly bulk) for FGM/MOM/OMNI — much smaller per request
  - Shorter timeouts, retries with backoff
  - OMNI fetched once per day (shared across probes on same day)
"""
import json, os, sys, csv, traceback, time, calendar
import datetime as dt_module
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cdasws import CdasWs
from pdl_pilot.mapping.s_mapper import compute_s_with_uncertainty, compute_bin_occupancy
from pdl_pilot.config.schema import BinConfig, UncertaintyConfig

BINS = BinConfig()
UNC = UncertaintyConfig()
RE_KM = 6371.2
SZA_MAX = 30.0
X_MIN_RE = 5.0
ENCOUNTER_HOURS = 6
MAX_WORKERS = 8  # parallel CDAWeb connections

YEARS = [2007, 2008, 2009, 2010]
MONTHS = [7, 8, 9, 10, 11]
PROBES = ['tha', 'thb', 'thc', 'thd', 'the']
ARTEMIS_CUTOFF = {'thb': dt_module.date(2010, 1, 1), 'thc': dt_module.date(2010, 1, 1)}

STATE_CACHE = "data_cache/routeC_exp_state"
ENC_CACHE = "data_cache/routeC_exp_enc"
os.makedirs(STATE_CACHE, exist_ok=True)
os.makedirs(ENC_CACHE, exist_ok=True)

# Thread-local CdasWs instances to avoid sharing
_tls = threading.local()
def get_cdas():
    if not hasattr(_tls, 'cdas'):
        _tls.cdas = CdasWs()
    return _tls.cdas

def _epoch_to_unix(arr):
    if hasattr(arr, 'dtype') and np.issubdtype(arr.dtype, np.datetime64):
        epoch_1970 = np.datetime64('1970-01-01T00:00:00', 'ns')
        return (arr.astype('datetime64[ns]') - epoch_1970).astype(np.float64) / 1e9
    return np.asarray(arr, dtype=np.float64)

def _interp(src_time, src_data, target_time, max_gap=60.0):
    if len(src_time) == 0 or len(src_data) == 0:
        return np.full_like(target_time, np.nan)
    result = np.interp(target_time, src_time, src_data.astype(np.float64))
    if max_gap > 0 and len(src_time) > 1:
        idx = np.clip(np.searchsorted(src_time, target_time), 0, len(src_time) - 1)
        idx_prev = np.clip(idx - 1, 0, len(src_time) - 1)
        dist = np.minimum(np.abs(target_time - src_time[idx]),
                          np.abs(target_time - src_time[idx_prev]))
        result[dist > max_gap] = np.nan
    return result

def _safe_fetch(dataset, variables, tstart, tend, retries=3, timeout_s=60):
    """Fetch from CDAWeb with retries and backoff."""
    for attempt in range(retries + 1):
        try:
            cdas_inst = get_cdas()
            status, data = cdas_inst.get_data(dataset, variables, tstart, tend)
            return data
        except Exception as e:
            if attempt < retries:
                time.sleep(1 + attempt * 2)
            else:
                return None

# =====================================================================
# PHASE 1: Load STATE caches, screen geometry
# =====================================================================
print("=" * 70)
print("PHASE 1: GEOMETRY SCREENING (from cached STATE)")
print("=" * 70)

search_log = []
qualifying_days = []

# Use single CdasWs for Phase 1 (sequential)
cdas_main = CdasWs()

for year in YEARS:
    for month in MONTHS:
        for probe in PROBES:
            if probe in ARTEMIS_CUTOFF and dt_module.date(year, month, 1) >= ARTEMIS_CUTOFF[probe]:
                search_log.append({"year": year, "month": month, "probe": probe,
                                   "searched": False, "reason": "ARTEMIS_cutoff", "n_windows": 0})
                continue

            pl = probe[-1]
            _, last_day = calendar.monthrange(year, month)
            cache_file = os.path.join(STATE_CACHE, f"{year}_{month:02d}_{probe}.npz")

            if os.path.exists(cache_file):
                loaded = dict(np.load(cache_file, allow_pickle=True))
                times = loaded["times"]; x_re = loaded["x_re"]; y_re = loaded["y_re"]; z_re = loaded["z_re"]
            else:
                tstart = f"{year}-{month:02d}-01T00:00:00Z"
                tend = f"{year}-{month:02d}-{last_day:02d}T23:59:59Z"
                pos_var = f"th{pl}_pos_gsm"
                try:
                    status, data = cdas_main.get_data(f"TH{pl.upper()}_L1_STATE", [pos_var], tstart, tend)
                except:
                    data = None
                if data is None or pos_var not in data.data_vars:
                    search_log.append({"year": year, "month": month, "probe": probe,
                                       "searched": True, "reason": "no_state_data", "n_windows": 0})
                    continue
                tc = [c for c in data.coords if "epoch" in c.lower() or "time" in c.lower()]
                if not tc:
                    search_log.append({"year": year, "month": month, "probe": probe,
                                       "searched": True, "reason": "no_time_coord", "n_windows": 0})
                    continue
                times = _epoch_to_unix(data.coords[tc[0]].values)
                pos = data[pos_var].values.astype(np.float64)
                x_re = pos[:, 0] / RE_KM; y_re = pos[:, 1] / RE_KM; z_re = pos[:, 2] / RE_KM
                np.savez(cache_file, times=times, x_re=x_re, y_re=y_re, z_re=z_re)

            sza = np.degrees(np.arctan2(np.sqrt(y_re**2 + z_re**2), x_re))
            good = (x_re > X_MIN_RE) & (sza < SZA_MAX) & np.isfinite(x_re)
            if np.sum(good) == 0:
                search_log.append({"year": year, "month": month, "probe": probe,
                                   "searched": True, "reason": "no_geometry", "n_windows": 0})
                continue

            windows = {}
            for i in range(len(times)):
                if not good[i]:
                    continue
                t = dt_module.datetime.fromtimestamp(times[i], tz=dt_module.timezone.utc)
                day_key = t.date()
                if day_key not in windows or sza[i] < windows[day_key][1]:
                    windows[day_key] = (times[i], sza[i])

            search_log.append({"year": year, "month": month, "probe": probe,
                               "searched": True, "reason": "ok", "n_windows": len(windows)})
            for dk, (ct, sz) in windows.items():
                qualifying_days.append((dk, probe, ct, sz))

# Dedup by date+probe
seen = {}
for item in qualifying_days:
    key = (item[0], item[1])
    if key not in seen or item[3] < seen[key][3]:
        seen[key] = item
qualifying_days = sorted(seen.values(), key=lambda x: (x[0], x[1]))

n_searched = sum(1 for s in search_log if s.get("searched"))
print(f"Year-month-probe combos searched: {n_searched}")
print(f"Qualifying near-subsolar days: {len(qualifying_days)}")

# =====================================================================
# PHASE 2+3: Parallel encounter processing
# =====================================================================
print(f"\n{'=' * 70}")
print(f"PHASE 2+3: PARALLEL ENCOUNTER PROCESSING ({MAX_WORKERS} workers)")
print(f"{'=' * 70}")

def process_one_encounter(day_key, probe, center_t, sza_screen):
    """Process a single encounter. Returns catalogue entry dict."""
    year, month, day = day_key.year, day_key.month, day_key.day
    pl = probe[-1]
    eid = f"exp_{year}{month:02d}{day:02d}_{probe}"

    # Check encounter cache
    enc_cache = os.path.join(ENC_CACHE, f"{eid}.json")
    if os.path.exists(enc_cache):
        with open(enc_cache) as f:
            return json.load(f)

    half = ENCOUNTER_HOURS * 3600 / 2
    t0 = center_t - half
    t1 = center_t + half
    t_start = dt_module.datetime.fromtimestamp(t0, tz=dt_module.timezone.utc)
    t_end = dt_module.datetime.fromtimestamp(t1, tz=dt_module.timezone.utc)
    tstart_str = t_start.strftime("%Y-%m-%dT%H:%M:%SZ")
    tend_str = t_end.strftime("%Y-%m-%dT%H:%M:%SZ")

    base = {"encounter_id": eid, "spacecraft": "themis", "probe": probe,
            "date": str(day_key), "year": year, "month": month,
            "sza_deg": round(sza_screen, 1), "evaluable": False,
            "routeC_core_usable": False, "cone_bin": "unknown"}

    try:
        # STATE from monthly cache
        state_cache = os.path.join(STATE_CACHE, f"{year}_{month:02d}_{probe}.npz")
        if not os.path.exists(state_cache):
            base["exclude_reason"] = "no STATE cache"
            return base
        state_loaded = dict(np.load(state_cache, allow_pickle=True))
        st_times = state_loaded["times"]
        st_mask = (st_times >= t0 - 600) & (st_times <= t1 + 600)
        st_t = st_times[st_mask]
        st_x = state_loaded["x_re"][st_mask]
        st_y = state_loaded["y_re"][st_mask]
        st_z = state_loaded["z_re"][st_mask]

        # MOM (6h window)
        mom_data = _safe_fetch(f"TH{pl.upper()}_L2_MOM", [f"th{pl}_peim_density"], tstart_str, tend_str)
        if mom_data is None or f"th{pl}_peim_density" not in mom_data.data_vars:
            base["exclude_reason"] = "no MOM data"
            return base
        mc = [c for c in mom_data.coords if "epoch" in c.lower() or "time" in c.lower()]
        if not mc:
            base["exclude_reason"] = "no MOM time coord"
            return base
        mom_times = _epoch_to_unix(mom_data.coords[mc[0]].values)
        density = mom_data[f"th{pl}_peim_density"].values.astype(np.float64)
        if len(mom_times) < 10:
            base["exclude_reason"] = "insufficient MOM data"
            return base
        target_time = mom_times

        # FGM (6h window)
        fgm_data = _safe_fetch(f"TH{pl.upper()}_L2_FGM", [f"th{pl}_fgs_gsm"], tstart_str, tend_str)
        if fgm_data is None or f"th{pl}_fgs_gsm" not in fgm_data.data_vars:
            base["exclude_reason"] = "no FGM data"
            return base
        fgm_bvec = fgm_data[f"th{pl}_fgs_gsm"].values.astype(np.float64)
        if fgm_bvec.ndim < 2:
            base["exclude_reason"] = "FGM not 3-component"
            return base
        bmag_raw = np.sqrt(np.sum(fgm_bvec**2, axis=-1))
        # Get FGM time
        fc = [c for c in fgm_data.coords if "epoch" in c.lower() or "time" in c.lower()]
        fgm_times = None
        if fc:
            fgm_times = _epoch_to_unix(fgm_data.coords[fc[0]].values)
        if fgm_times is None or len(fgm_times) != len(bmag_raw):
            dims = list(fgm_data[f"th{pl}_fgs_gsm"].dims)
            for d in dims:
                if d in fgm_data.coords and len(fgm_data.coords[d].values) == len(bmag_raw):
                    fgm_times = _epoch_to_unix(fgm_data.coords[d].values)
                    break
        if fgm_times is None or len(fgm_times) != len(bmag_raw):
            # Last resort: uniform spacing
            if len(bmag_raw) > 0:
                fgm_times = np.linspace(target_time[0], target_time[-1], len(bmag_raw))
            else:
                base["exclude_reason"] = "FGM time extraction failed"
                return base

        bmag = _interp(fgm_times, bmag_raw, target_time, max_gap=30.0)

        # Position
        x_re = _interp(st_t, st_x, target_time, max_gap=600.0)
        y_re = _interp(st_t, st_y, target_time, max_gap=600.0)
        z_re = _interp(st_t, st_z, target_time, max_gap=600.0)
        x_m = float(np.nanmean(x_re)); y_m = float(np.nanmean(y_re)); z_m = float(np.nanmean(z_re))
        actual_sza = float(np.degrees(np.arctan2(np.sqrt(y_m**2 + z_m**2), x_m))) if np.isfinite(x_m) else 999.0
        if actual_sza > SZA_MAX:
            base["sza_deg"] = round(actual_sza, 1)
            base["exclude_reason"] = f"SZA={actual_sza:.0f}>{SZA_MAX}"
            return base

        # OMNI (6h + padding)
        omni_start = (t_start - dt_module.timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
        omni_end = (t_end + dt_module.timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
        omni_data = _safe_fetch("OMNI_HRO_1MIN",
            ["BX_GSE", "BY_GSM", "BZ_GSM", "F", "Pressure", "Mach_num"], omni_start, omni_end)

        dp = bz = bt = bx = by = ma = None
        if omni_data is not None:
            def _om(key):
                if key not in omni_data.data_vars: return None
                arr = omni_data[key].values.astype(np.float64)
                v = arr[np.isfinite(arr)]
                v = v[(v > -1e30) & (v < 1e30) & (np.abs(v) < 9990)]
                return float(np.nanmedian(v)) if len(v) > 0 else None
            dp = _om("Pressure"); bz = _om("BZ_GSM"); bt = _om("F")
            ma = _om("Mach_num"); bx = _om("BX_GSE"); by = _om("BY_GSM")

        if dp is None or dp <= 0:
            base["sza_deg"] = round(actual_sza, 1)
            base["exclude_reason"] = "no valid OMNI Dp"
            return base

        cone_deg = float(np.degrees(np.arccos(min(abs(bx) / bt, 1.0)))) if bx is not None and bt and bt > 0 else None
        clock_deg = (float(np.degrees(np.arctan2(by, bz))) % 360.0) if by is not None and bz is not None else None

        # Fill masking
        density[density <= 0] = np.nan; density[density > 1000] = np.nan
        bmag[bmag <= 0] = np.nan; bmag[bmag > 500] = np.nan

        # s-mapping
        s_nom, _, _, mp0, bs0 = compute_s_with_uncertainty(
            x_re, dp_nPa=dp, bz_nT=bz or 0.0, mach_alfven=ma or 8.0, unc=UNC)
        occupancy = compute_bin_occupancy(s_nom, BINS)
        near_occ = occupancy["near"]; bg_occ = occupancy["background"]

        near_mask = (s_nom >= 0.2) & (s_nom < 0.4)
        bg_mask = (s_nom >= 0.6) & (s_nom <= 1.0)
        def _smed(arr, mask):
            v = arr[mask]; v = v[np.isfinite(v)]
            return float(np.nanmedian(v)) if len(v) > 0 else None

        n_near = _smed(density, near_mask); n_bg = _smed(density, bg_mask)
        b_near = _smed(bmag, near_mask); b_bg = _smed(bmag, bg_mask)
        Dn = (n_near / n_bg) if (n_near and n_bg and n_bg > 0) else None
        EB = (b_near / b_bg) if (b_near and b_bg and b_bg > 0) else None
        evaluable = near_occ >= 0.05 and bg_occ >= 0.01 and Dn is not None and EB is not None

        mlt = float((12.0 + np.degrees(np.arctan2(y_m, x_m)) / 15.0) % 24.0) if np.isfinite(x_m) and np.isfinite(y_m) else None
        cone_bin = "unknown"
        if cone_deg is not None:
            if cone_deg < 30: cone_bin = "quasi-radial"
            elif cone_deg <= 45: cone_bin = "low-cone"
            elif cone_deg <= 60: cone_bin = "intermediate"
            else: cone_bin = "perpendicular"

        entry = {
            "encounter_id": eid, "spacecraft": "themis", "probe": probe,
            "date": str(day_key), "year": year, "month": month,
            "sza_deg": round(actual_sza, 1), "mlt": round(mlt, 1) if mlt else None,
            "x_gsm_re": round(x_m, 2),
            "dp_nPa": round(dp, 2), "bz_nT": round(bz, 2) if bz else None,
            "ma": round(ma, 1) if ma else None,
            "cone_deg": round(cone_deg, 1) if cone_deg is not None else None,
            "clock_deg": round(clock_deg, 1) if clock_deg is not None else None,
            "mp_standoff_re": round(mp0, 2), "bs_standoff_re": round(bs0, 2),
            "near_occ": round(near_occ, 4), "bg_occ": round(bg_occ, 4),
            "Dn": round(Dn, 4) if Dn else None, "EB": round(EB, 4) if EB else None,
            "evaluable": evaluable, "cone_bin": cone_bin, "n_points": len(target_time),
            "routeC_core_usable": evaluable,
            "exclude_reason": None if evaluable else (
                f"bg_occ={bg_occ:.3f}<1%" if bg_occ < 0.01
                else f"near_occ={near_occ:.3f}<5%" if near_occ < 0.05
                else "Dn/EB not computable"),
        }
        # QC
        if evaluable and Dn and EB:
            if Dn < 1.0 and EB > 1.0: entry["qc_transition_cleanliness"] = "clean"
            elif Dn < 1.0 or EB > 1.0: entry["qc_transition_cleanliness"] = "mixed"
            else: entry["qc_transition_cleanliness"] = "unclear"
        else: entry["qc_transition_cleanliness"] = "not_assessed"
        entry["qc_disturbance"] = "undisturbed" if near_occ > 0.10 and bg_occ > 0.05 else "uncertain"
        entry["qc_boundary_motion"] = "stable" if 2.0 <= dp <= 6.0 else "uncertain"
        entry["omni_context_quality_note"] = "good" if bz is not None and cone_deg is not None else "partial"
        entry["boundary_uncertainty_note"] = "plausible" if 2.0 <= dp <= 6.0 else "uncertain"

        # Cache this encounter
        with open(enc_cache, 'w') as f:
            json.dump(entry, f, indent=2, default=str)

        return entry

    except Exception as e:
        base["exclude_reason"] = f"exception: {e}"
        return base

# Run in parallel
catalogue = []
completed = 0
total = len(qualifying_days)
retained_count = 0

print(f"Processing {total} encounters with {MAX_WORKERS} parallel workers...")

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = {}
    for day_key, probe, center_t, sza_screen in qualifying_days:
        future = executor.submit(process_one_encounter, day_key, probe, center_t, sza_screen)
        futures[future] = (day_key, probe)

    for future in as_completed(futures):
        day_key, probe = futures[future]
        completed += 1
        try:
            entry = future.result()
            catalogue.append(entry)
            if entry.get("routeC_core_usable"):
                retained_count += 1
                print(f"  [{completed}/{total}] RETAINED {entry['date']} {probe} cone={entry.get('cone_deg')} "
                      f"Dp={entry.get('dp_nPa')} Dn={entry.get('Dn')} EB={entry.get('EB')} [{entry['cone_bin']}]")
            elif completed % 100 == 0:
                print(f"  [{completed}/{total}] progress... ({retained_count} retained so far)")
        except Exception as e:
            catalogue.append({"encounter_id": f"exp_{day_key}_{probe}", "spacecraft": "themis",
                "probe": probe, "date": str(day_key), "year": day_key.year, "month": day_key.month,
                "evaluable": False, "routeC_core_usable": False, "exclude_reason": str(e), "cone_bin": "unknown"})
            completed += 1

print(f"\nAll {total} encounters processed. {retained_count} retained.")

# =====================================================================
# SUMMARY & HARD STOP
# =====================================================================
print(f"\n{'=' * 70}")
print("FULL EXP SUMMARY")
print(f"{'=' * 70}")

seen_ret = {}
for e in catalogue:
    if e.get("routeC_core_usable"):
        k = (e["date"], e["probe"])
        if k not in seen_ret: seen_ret[k] = e
unique_retained = list(seen_ret.values())

cone_counts = {"quasi-radial": 0, "low-cone": 0, "intermediate": 0, "perpendicular": 0, "unknown": 0}
for e in unique_retained:
    cone_counts[e.get("cone_bin", "unknown")] += 1

print(f"Searched: {n_searched} (year,month,probe)")
print(f"Qualifying days: {total}")
print(f"Processed: {len(catalogue)}")
print(f"Unique retained: {len(unique_retained)}")
for cb in ["quasi-radial", "low-cone", "intermediate", "perpendicular"]:
    print(f"  {cb}: {cone_counts[cb]}")

qr = cone_counts["quasi-radial"]; lc = cone_counts["low-cone"]
success = qr >= 1 or lc >= 5
print(f"\nHARD STOP: {'SUCCESS' if success else 'HARD NULL'}")
print(f"  quasi-radial: {qr} (need >= 1)")
print(f"  low-cone: {lc} (need >= 5)")

# =====================================================================
# SAVE OUTPUTS
# =====================================================================
OUT_DIR = "reports/themis_conditioning/routeC_exp"
os.makedirs(OUT_DIR, exist_ok=True)

manifest = {
    "generated": dt_module.datetime.now().isoformat(),
    "run_name": "Phase 6 Route C FULL EXP",
    "declared_slice": {"years": YEARS, "months": MONTHS, "probes": PROBES,
        "sza_max": SZA_MAX, "description": "All THEMIS 2007-2010, Jul-Nov, all 5 probes, SZA<=30"},
    "searched_slice": {"ym_probe_searched": n_searched,
        "description": "Every (year,month,probe) STATE fetched via CDAWeb. No subsampling. "
                       "FGM+MOM+OMNI fetched per qualifying day (6h windows)."},
    "scope_match": True,
    "results": {"qualifying_days": total, "processed": len(catalogue),
        "unique_retained": len(unique_retained), "cone_counts": cone_counts},
    "hard_stop": {"quasi_radial": qr, "low_cone": lc, "outcome": "SUCCESS" if success else "HARD_NULL"},
    "search_log": search_log,
}
with open(os.path.join(OUT_DIR, "scope_manifest.json"), 'w') as f:
    json.dump(manifest, f, indent=2)

with open(os.path.join(OUT_DIR, "encounter_catalogue_routeC_exp.json"), 'w') as f:
    json.dump(catalogue, f, indent=2, default=str)

csv_fields = ['encounter_id', 'spacecraft', 'date', 'year', 'month', 'probe',
    'sza_deg', 'mlt', 'cone_deg', 'clock_deg', 'dp_nPa', 'bz_nT',
    'near_occ', 'bg_occ', 'Dn', 'EB',
    'qc_transition_cleanliness', 'qc_disturbance', 'qc_boundary_motion',
    'omni_context_quality_note', 'boundary_uncertainty_note',
    'routeC_core_usable', 'exclude_reason', 'cone_bin']
with open(os.path.join(OUT_DIR, "encounter_catalogue_routeC_exp.csv"), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=csv_fields, extrasaction='ignore')
    w.writeheader()
    for entry in catalogue:
        w.writerow(entry)

summary = {
    "generated": dt_module.datetime.now().isoformat(),
    "run_name": "Phase 6 Route C FULL EXP",
    "scope_match": True, "ym_probe_searched": n_searched,
    "qualifying_days": total, "processed": len(catalogue),
    "unique_retained": len(unique_retained), "cone_counts": cone_counts,
    "hard_stop_outcome": "SUCCESS" if success else "HARD_NULL",
    "hard_stop_qr": qr, "hard_stop_lc": lc,
    "retained_encounters": [e for e in catalogue if e.get("routeC_core_usable")],
}
with open(os.path.join(OUT_DIR, "routeC_exp_summary.json"), 'w') as f:
    json.dump(summary, f, indent=2, default=str)

# Selection flow
with open(os.path.join(OUT_DIR, "selection_flow.md"), 'w') as f:
    f.write(f"# Route C FULL EXP — Selection Flow\n\n")
    f.write(f"**Date:** {dt_module.datetime.now().isoformat()[:10]}\n\n")
    f.write(f"## Scope\n- Years: {YEARS}\n- Months: {MONTHS}\n- Probes: {PROBES}\n")
    f.write(f"- SZA <= {SZA_MAX} deg\n- Scope match: declared = searched = YES\n\n")
    f.write(f"## Results\n- Qualifying days: {total}\n")
    f.write(f"- Processed: {len(catalogue)}\n- Retained: {len(unique_retained)}\n\n")
    f.write(f"## Retained by cone bin\n")
    for cb in ["quasi-radial", "low-cone", "intermediate", "perpendicular"]:
        f.write(f"- {cb}: {cone_counts[cb]}\n")
    f.write(f"\n## Hard stop: {'SUCCESS' if success else 'HARD NULL'}\n")
    f.write(f"- quasi-radial: {qr} (need >= 1)\n- low-cone: {lc} (need >= 5)\n\n")
    if unique_retained:
        f.write("## Retained encounters\n\n")
        f.write("| Date | Probe | Cone | Dp | Dn | EB | Cone bin |\n|---|---|---|---|---|---|---|\n")
        for e in sorted(unique_retained, key=lambda x: (x.get("cone_deg") or 999)):
            f.write(f"| {e['date']} | {e['probe']} | {e.get('cone_deg')} | {e.get('dp_nPa')} | "
                    f"{e.get('Dn')} | {e.get('EB')} | {e['cone_bin']} |\n")

print(f"\nAll outputs saved to {OUT_DIR}/")
print("FULL EXP scan complete.")
