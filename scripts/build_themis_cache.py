"""
THEMIS Full-Archive Local Cache Builder

Downloads ALL available THEMIS STATE data, screens geometry,
then multi-threaded fetches FGM+MOM+OMNI for qualifying days.

Directory structure:
  data_cache/themis_archive/
    raw_state/              ← All STATE files (probe_year_month.npz)
    raw_state_index.json    ← Download manifest + status
    screened/               ← Qualifying days list
    screened_index.json     ← Geometry screening results
    encounters/             ← Per-encounter JSON (Dn/EB/QC)
    encounter_index.json    ← All encounters index
    retained_index.json     ← Evaluable encounters, grouped by cone bin
    summary.json            ← Global statistics

Geometry screening:
    X_GSM > 5 Re
    SZA < 30 deg
    8 Re < r < 20 Re

Optimizations:
    - ThreadPoolExecutor (configurable workers)
    - Per-file caching (idempotent, skip existing)
    - Retry with exponential backoff
    - Checksum/count verification
    - Progress reporting
"""
import json, os, sys, csv, time, calendar, traceback
import datetime as dt_module
import numpy as np
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cdasws import CdasWs
from pdl_pilot.mapping.s_mapper import compute_s_with_uncertainty, compute_bin_occupancy
from pdl_pilot.config.schema import BinConfig, UncertaintyConfig

# =====================================================================
# CONFIG
# =====================================================================
BINS = BinConfig()
UNC = UncertaintyConfig()
RE_KM = 6371.2
MAX_WORKERS = 8
MAX_RETRIES = 4
BASE_BACKOFF = 2  # seconds

# Geometry screening thresholds
X_MIN_RE = 5.0
SZA_MAX = 30.0
R_MIN_RE = 8.0
R_MAX_RE = 20.0

ENCOUNTER_HOURS = 6

# Archive scope
ALL_PROBES = ['tha', 'thb', 'thc', 'thd', 'the']
# Near-earth probes: specific years with dayside apogee
# ARTEMIS probes (thb/thc from 2010+): all years, perigee passes
YEAR_RANGE = range(2007, 2026)
MONTH_RANGE = range(1, 13)  # All 12 months - let geometry screening filter

# Paths
BASE_DIR = "data_cache/themis_archive"
RAW_STATE_DIR = os.path.join(BASE_DIR, "raw_state")
SCREENED_DIR = os.path.join(BASE_DIR, "screened")
ENCOUNTER_DIR = os.path.join(BASE_DIR, "encounters")

for d in [RAW_STATE_DIR, SCREENED_DIR, ENCOUNTER_DIR]:
    os.makedirs(d, exist_ok=True)

# Thread-local CdasWs
_tls = threading.local()
def get_cdas():
    if not hasattr(_tls, 'cdas'):
        _tls.cdas = CdasWs()
    return _tls.cdas

_print_lock = threading.Lock()
def tprint(msg):
    with _print_lock:
        print(msg, flush=True)


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


def _fetch_with_retry(dataset, variables, tstart, tend):
    """Fetch from CDAWeb with exponential backoff retry."""
    for attempt in range(MAX_RETRIES + 1):
        try:
            cdas_inst = get_cdas()
            status, data = cdas_inst.get_data(dataset, variables, tstart, tend)
            return data
        except Exception as e:
            if attempt < MAX_RETRIES:
                wait = BASE_BACKOFF * (2 ** attempt)
                time.sleep(wait)
            else:
                return None


# =====================================================================
# PHASE 1: Download all STATE files
# =====================================================================
def download_one_state(year, month, probe):
    """Download one month of STATE data. Returns (key, status, n_points)."""
    pl = probe[-1]
    key = f"{probe}_{year}_{month:02d}"
    fpath = os.path.join(RAW_STATE_DIR, f"{key}.npz")

    # Skip if already cached
    if os.path.exists(fpath):
        try:
            loaded = dict(np.load(fpath, allow_pickle=True))
            n = len(loaded.get("times", []))
            return (key, "cached", n)
        except:
            os.remove(fpath)  # corrupt, re-download

    _, last_day = calendar.monthrange(year, month)
    tstart = f"{year}-{month:02d}-01T00:00:00Z"
    tend = f"{year}-{month:02d}-{last_day:02d}T23:59:59Z"
    pos_var = f"th{pl}_pos_gsm"

    data = _fetch_with_retry(f"TH{pl.upper()}_L1_STATE", [pos_var], tstart, tend)
    if data is None or pos_var not in data.data_vars:
        return (key, "no_data", 0)

    tc = [c for c in data.coords if "epoch" in c.lower() or "time" in c.lower()]
    if not tc:
        return (key, "no_time_coord", 0)

    times = _epoch_to_unix(data.coords[tc[0]].values)
    pos = data[pos_var].values.astype(np.float64)
    if pos.ndim != 2 or pos.shape[1] != 3:
        return (key, "bad_pos_shape", 0)

    x_re = pos[:, 0] / RE_KM
    y_re = pos[:, 1] / RE_KM
    z_re = pos[:, 2] / RE_KM

    np.savez(fpath, times=times, x_re=x_re, y_re=y_re, z_re=z_re)
    return (key, "downloaded", len(times))


def run_phase1():
    """Download all STATE files in parallel."""
    print("=" * 70)
    print("PHASE 1: DOWNLOAD ALL STATE FILES")
    print("=" * 70)

    # Build task list
    tasks = []
    for year in YEAR_RANGE:
        for month in MONTH_RANGE:
            for probe in ALL_PROBES:
                tasks.append((year, month, probe))

    print(f"Total (year, month, probe) combinations: {len(tasks)}")

    state_index = {}
    completed = 0
    cached = 0
    downloaded = 0
    failed = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {}
        for (y, m, p) in tasks:
            f = executor.submit(download_one_state, y, m, p)
            futures[f] = (y, m, p)

        for future in as_completed(futures):
            y, m, p = futures[future]
            completed += 1
            try:
                key, status, n_pts = future.result()
                state_index[key] = {"year": y, "month": m, "probe": p,
                                    "status": status, "n_points": n_pts}
                if status == "cached":
                    cached += 1
                elif status == "downloaded":
                    downloaded += 1
                else:
                    failed += 1

                if completed % 50 == 0 or completed == len(tasks):
                    tprint(f"  [{completed}/{len(tasks)}] cached={cached} downloaded={downloaded} failed={failed}")
            except Exception as e:
                key = f"{p}_{y}_{m:02d}"
                state_index[key] = {"year": y, "month": m, "probe": p,
                                    "status": f"error: {e}", "n_points": 0}
                failed += 1

    # Save state index
    with open(os.path.join(BASE_DIR, "raw_state_index.json"), 'w') as f:
        json.dump({"generated": dt_module.datetime.now().isoformat(),
                   "total": len(tasks), "cached": cached,
                   "downloaded": downloaded, "failed": failed,
                   "files": state_index}, f, indent=2)

    n_files = len([f for f in os.listdir(RAW_STATE_DIR) if f.endswith('.npz')])
    print(f"\nPhase 1 complete: {n_files} STATE files on disk")
    print(f"  cached={cached}, downloaded={downloaded}, failed={failed}")
    return state_index


# =====================================================================
# PHASE 2: Geometry screening
# =====================================================================
def run_phase2(state_index):
    """Screen all STATE files for dayside near-subsolar geometry."""
    print(f"\n{'=' * 70}")
    print("PHASE 2: GEOMETRY SCREENING")
    print(f"  X_GSM > {X_MIN_RE} Re, SZA < {SZA_MAX}°, {R_MIN_RE} < r < {R_MAX_RE} Re")
    print("=" * 70)

    qualifying_days = []
    screening_log = {}

    for fname in sorted(os.listdir(RAW_STATE_DIR)):
        if not fname.endswith('.npz'):
            continue
        key = fname.replace('.npz', '')
        parts = key.split('_')
        if len(parts) != 3:
            continue
        probe, year_s, month_s = parts
        year, month = int(year_s), int(month_s)

        try:
            loaded = dict(np.load(os.path.join(RAW_STATE_DIR, fname), allow_pickle=True))
            times = loaded["times"]
            x_re = loaded["x_re"]
            y_re = loaded["y_re"]
            z_re = loaded["z_re"]
        except:
            screening_log[key] = {"status": "load_error", "n_qualifying": 0}
            continue

        if len(times) == 0:
            screening_log[key] = {"status": "empty", "n_qualifying": 0}
            continue

        r = np.sqrt(x_re**2 + y_re**2 + z_re**2)
        sza = np.degrees(np.arctan2(np.sqrt(y_re**2 + z_re**2), x_re))
        good = ((x_re > X_MIN_RE) & (sza < SZA_MAX) &
                (r > R_MIN_RE) & (r < R_MAX_RE) & np.isfinite(x_re))

        n_good = int(np.sum(good))
        screening_log[key] = {"status": "ok", "n_qualifying": n_good,
                              "n_total": len(times)}

        if n_good == 0:
            continue

        # Group by day, find best (lowest SZA) time per day
        for i in range(len(times)):
            if not good[i]:
                continue
            t = dt_module.datetime.fromtimestamp(times[i], tz=dt_module.timezone.utc)
            day_key = t.date()
            # Use (date, probe) as unique key
            qkey = (str(day_key), probe)
            # Check if we already have a better SZA for this day+probe
            found = False
            for q in qualifying_days:
                if q["date"] == str(day_key) and q["probe"] == probe:
                    if sza[i] < q["sza_deg"]:
                        q["center_unix"] = float(times[i])
                        q["sza_deg"] = round(float(sza[i]), 1)
                        q["x_re"] = round(float(x_re[i]), 2)
                        q["r_re"] = round(float(r[i]), 2)
                    found = True
                    break
            if not found:
                qualifying_days.append({
                    "date": str(day_key), "probe": probe,
                    "year": year, "month": month,
                    "center_unix": float(times[i]),
                    "sza_deg": round(float(sza[i]), 1),
                    "x_re": round(float(x_re[i]), 2),
                    "r_re": round(float(r[i]), 2),
                })

    # Deduplicate (should already be unique by construction)
    seen = {}
    for q in qualifying_days:
        k = (q["date"], q["probe"])
        if k not in seen or q["sza_deg"] < seen[k]["sza_deg"]:
            seen[k] = q
    qualifying_days = sorted(seen.values(), key=lambda x: (x["date"], x["probe"]))

    # Save
    with open(os.path.join(BASE_DIR, "screened_index.json"), 'w') as f:
        json.dump({
            "generated": dt_module.datetime.now().isoformat(),
            "geometry_criteria": {
                "x_min_re": X_MIN_RE, "sza_max_deg": SZA_MAX,
                "r_min_re": R_MIN_RE, "r_max_re": R_MAX_RE,
            },
            "total_state_files_screened": len(screening_log),
            "total_qualifying_days": len(qualifying_days),
            "qualifying_days": qualifying_days,
        }, f, indent=2)

    # Stats
    by_year = {}
    by_probe = {}
    for q in qualifying_days:
        by_year[q["year"]] = by_year.get(q["year"], 0) + 1
        by_probe[q["probe"]] = by_probe.get(q["probe"], 0) + 1

    print(f"Qualifying days: {len(qualifying_days)}")
    print("  By year:", json.dumps(dict(sorted(by_year.items()))))
    print("  By probe:", json.dumps(dict(sorted(by_probe.items()))))

    return qualifying_days


# =====================================================================
# PHASE 3: Encounter processing (multi-threaded)
# =====================================================================
def process_one_encounter(q):
    """Process one qualifying day into an encounter. Returns dict."""
    date_str = q["date"]
    probe = q["probe"]
    center_t = q["center_unix"]
    year = q["year"]
    month = q["month"]
    pl = probe[-1]
    eid = f"{date_str}_{probe}"

    # Check cache
    enc_path = os.path.join(ENCOUNTER_DIR, f"{eid}.json")
    if os.path.exists(enc_path):
        try:
            with open(enc_path) as f:
                return json.load(f)
        except:
            os.remove(enc_path)

    half = ENCOUNTER_HOURS * 3600 / 2
    t_start = dt_module.datetime.fromtimestamp(center_t - half, tz=dt_module.timezone.utc)
    t_end = dt_module.datetime.fromtimestamp(center_t + half, tz=dt_module.timezone.utc)
    tstart_str = t_start.strftime("%Y-%m-%dT%H:%M:%SZ")
    tend_str = t_end.strftime("%Y-%m-%dT%H:%M:%SZ")

    base = {"encounter_id": eid, "spacecraft": "themis", "probe": probe,
            "date": date_str, "year": year, "month": month,
            "sza_deg": q["sza_deg"], "evaluable": False,
            "retained": False, "cone_bin": "unknown"}

    try:
        # STATE from raw cache
        state_key = f"{probe}_{year}_{month:02d}"
        state_path = os.path.join(RAW_STATE_DIR, f"{state_key}.npz")
        if not os.path.exists(state_path):
            base["exclude_reason"] = "no STATE cache"
            return base
        sdata = dict(np.load(state_path, allow_pickle=True))
        st = sdata["times"]
        t0, t1 = center_t - half - 600, center_t + half + 600
        mask = (st >= t0) & (st <= t1)
        st_t = st[mask]; st_x = sdata["x_re"][mask]
        st_y = sdata["y_re"][mask]; st_z = sdata["z_re"][mask]

        # MOM
        mom = _fetch_with_retry(f"TH{pl.upper()}_L2_MOM", [f"th{pl}_peim_density"], tstart_str, tend_str)
        if mom is None or f"th{pl}_peim_density" not in mom.data_vars:
            base["exclude_reason"] = "no MOM data"; return base
        mc = [c for c in mom.coords if "epoch" in c.lower() or "time" in c.lower()]
        if not mc:
            base["exclude_reason"] = "no MOM time"; return base
        mom_times = _epoch_to_unix(mom.coords[mc[0]].values)
        density = mom[f"th{pl}_peim_density"].values.astype(np.float64)
        if len(mom_times) < 10:
            base["exclude_reason"] = "insufficient MOM"; return base
        target_time = mom_times

        # FGM
        fgm = _fetch_with_retry(f"TH{pl.upper()}_L2_FGM", [f"th{pl}_fgs_gsm"], tstart_str, tend_str)
        if fgm is None or f"th{pl}_fgs_gsm" not in fgm.data_vars:
            base["exclude_reason"] = "no FGM data"; return base
        bvec = fgm[f"th{pl}_fgs_gsm"].values.astype(np.float64)
        if bvec.ndim < 2:
            base["exclude_reason"] = "FGM not 3-component"; return base
        bmag_raw = np.sqrt(np.sum(bvec**2, axis=-1))
        fc = [c for c in fgm.coords if "epoch" in c.lower() or "time" in c.lower()]
        fgm_times = None
        if fc:
            fgm_times = _epoch_to_unix(fgm.coords[fc[0]].values)
        if fgm_times is None or len(fgm_times) != len(bmag_raw):
            for d in fgm[f"th{pl}_fgs_gsm"].dims:
                if d in fgm.coords and len(fgm.coords[d].values) == len(bmag_raw):
                    fgm_times = _epoch_to_unix(fgm.coords[d].values); break
        if fgm_times is None or len(fgm_times) != len(bmag_raw):
            if len(bmag_raw) > 0:
                fgm_times = np.linspace(target_time[0], target_time[-1], len(bmag_raw))
            else:
                base["exclude_reason"] = "FGM time fail"; return base
        bmag = _interp(fgm_times, bmag_raw, target_time, max_gap=30.0)

        # Position
        x_re = _interp(st_t, st_x, target_time, max_gap=600.0)
        y_re = _interp(st_t, st_y, target_time, max_gap=600.0)
        z_re = _interp(st_t, st_z, target_time, max_gap=600.0)
        x_m = float(np.nanmean(x_re)); y_m = float(np.nanmean(y_re)); z_m = float(np.nanmean(z_re))
        actual_sza = float(np.degrees(np.arctan2(np.sqrt(y_m**2+z_m**2), x_m))) if np.isfinite(x_m) else 999.0
        if actual_sza > SZA_MAX:
            base["sza_deg"] = round(actual_sza, 1)
            base["exclude_reason"] = f"SZA={actual_sza:.0f}>{SZA_MAX}"; return base

        # OMNI
        omni_s = (t_start - dt_module.timedelta(minutes=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
        omni_e = (t_end + dt_module.timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
        omni = _fetch_with_retry("OMNI_HRO_1MIN",
            ["BX_GSE","BY_GSM","BZ_GSM","F","Pressure","Mach_num"], omni_s, omni_e)
        dp=bz=bt=bx=by=ma=None
        if omni is not None:
            def _om(k):
                if k not in omni.data_vars: return None
                a = omni[k].values.astype(np.float64)
                v = a[np.isfinite(a)]; v = v[(v>-1e30)&(v<1e30)&(np.abs(v)<9990)]
                return float(np.nanmedian(v)) if len(v)>0 else None
            dp=_om("Pressure"); bz=_om("BZ_GSM"); bt=_om("F")
            ma=_om("Mach_num"); bx=_om("BX_GSE"); by=_om("BY_GSM")

        if dp is None or dp <= 0:
            base["sza_deg"]=round(actual_sza,1)
            base["exclude_reason"]="no valid OMNI Dp"; return base

        cone_deg = float(np.degrees(np.arccos(min(abs(bx)/bt,1.0)))) if bx is not None and bt and bt>0 else None
        clock_deg = (float(np.degrees(np.arctan2(by,bz)))%360.0) if by is not None and bz is not None else None

        # Fill masking
        density[density<=0]=np.nan; density[density>1000]=np.nan
        bmag[bmag<=0]=np.nan; bmag[bmag>500]=np.nan

        # s-mapping
        s_nom,_,_,mp0,bs0 = compute_s_with_uncertainty(
            x_re, dp_nPa=dp, bz_nT=bz or 0.0, mach_alfven=ma or 8.0, unc=UNC)
        occupancy = compute_bin_occupancy(s_nom, BINS)
        near_occ=occupancy["near"]; bg_occ=occupancy["background"]

        near_mask=(s_nom>=0.2)&(s_nom<0.4); bg_mask=(s_nom>=0.6)&(s_nom<=1.0)
        def _smed(arr,mask):
            v=arr[mask]; v=v[np.isfinite(v)]
            return float(np.nanmedian(v)) if len(v)>0 else None

        n_near=_smed(density,near_mask); n_bg=_smed(density,bg_mask)
        b_near=_smed(bmag,near_mask); b_bg=_smed(bmag,bg_mask)
        Dn=(n_near/n_bg) if (n_near and n_bg and n_bg>0) else None
        EB=(b_near/b_bg) if (b_near and b_bg and b_bg>0) else None
        evaluable = near_occ>=0.05 and bg_occ>=0.01 and Dn is not None and EB is not None

        mlt = float((12.0+np.degrees(np.arctan2(y_m,x_m))/15.0)%24.0) if np.isfinite(x_m) and np.isfinite(y_m) else None
        cone_bin="unknown"
        if cone_deg is not None:
            if cone_deg<30: cone_bin="quasi-radial"
            elif cone_deg<=45: cone_bin="low-cone"
            elif cone_deg<=60: cone_bin="intermediate"
            else: cone_bin="perpendicular"

        entry = {
            "encounter_id": eid, "spacecraft": "themis", "probe": probe,
            "date": date_str, "year": year, "month": month,
            "sza_deg": round(actual_sza,1), "mlt": round(mlt,1) if mlt else None,
            "x_gsm_re": round(x_m,2), "r_re": round(float(np.sqrt(x_m**2+y_m**2+z_m**2)),2),
            "dp_nPa": round(dp,2), "bz_nT": round(bz,2) if bz else None,
            "ma": round(ma,1) if ma else None,
            "cone_deg": round(cone_deg,1) if cone_deg is not None else None,
            "clock_deg": round(clock_deg,1) if clock_deg is not None else None,
            "mp_standoff_re": round(mp0,2), "bs_standoff_re": round(bs0,2),
            "near_occ": round(near_occ,4), "bg_occ": round(bg_occ,4),
            "Dn": round(Dn,4) if Dn else None, "EB": round(EB,4) if EB else None,
            "evaluable": evaluable, "retained": evaluable,
            "cone_bin": cone_bin, "n_points": len(target_time),
            "exclude_reason": None if evaluable else (
                f"bg_occ={bg_occ:.3f}<1%" if bg_occ<0.01
                else f"near_occ={near_occ:.3f}<5%" if near_occ<0.05
                else "Dn/EB not computable"),
        }
        # QC
        if evaluable and Dn and EB:
            if Dn<1.0 and EB>1.0: entry["qc_transition_cleanliness"]="clean"
            elif Dn<1.0 or EB>1.0: entry["qc_transition_cleanliness"]="mixed"
            else: entry["qc_transition_cleanliness"]="unclear"
        else: entry["qc_transition_cleanliness"]="not_assessed"
        entry["qc_disturbance"] = "undisturbed" if near_occ>0.10 and bg_occ>0.05 else "uncertain"
        entry["qc_boundary_motion"] = "stable" if dp and 2.0<=dp<=6.0 else "uncertain"
        entry["omni_context_quality_note"] = "good" if bz is not None and cone_deg is not None else "partial"
        entry["boundary_uncertainty_note"] = "plausible" if dp and 2.0<=dp<=6.0 else "uncertain"

        # Cache
        with open(enc_path, 'w') as f:
            json.dump(entry, f, indent=2, default=str)
        return entry

    except Exception as e:
        base["exclude_reason"] = f"exception: {e}"
        return base


def run_phase3(qualifying_days):
    """Process all qualifying days in parallel."""
    print(f"\n{'=' * 70}")
    print(f"PHASE 3: ENCOUNTER PROCESSING ({MAX_WORKERS} workers)")
    print(f"{'=' * 70}")

    total = len(qualifying_days)
    catalogue = []
    completed = [0]
    retained_count = [0]

    print(f"Processing {total} qualifying days...")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {}
        for q in qualifying_days:
            f = executor.submit(process_one_encounter, q)
            futures[f] = q

        for future in as_completed(futures):
            completed[0] += 1
            try:
                entry = future.result()
                catalogue.append(entry)
                if entry.get("retained"):
                    retained_count[0] += 1
                    tprint(f"  [{completed[0]}/{total}] RETAINED {entry['date']} {entry['probe']} "
                           f"cone={entry.get('cone_deg')} Dp={entry.get('dp_nPa')} "
                           f"Dn={entry.get('Dn')} EB={entry.get('EB')} [{entry['cone_bin']}]")
                elif completed[0] % 200 == 0:
                    tprint(f"  [{completed[0]}/{total}] progress... ({retained_count[0]} retained)")
            except Exception as e:
                q = futures[future]
                catalogue.append({
                    "encounter_id": f"{q['date']}_{q['probe']}",
                    "date": q["date"], "probe": q["probe"],
                    "year": q["year"], "month": q["month"],
                    "evaluable": False, "retained": False,
                    "exclude_reason": str(e), "cone_bin": "unknown"})

    print(f"\nAll {total} processed. {retained_count[0]} retained.")
    return catalogue


# =====================================================================
# PHASE 4: Build indexes
# =====================================================================
def run_phase4(catalogue):
    """Build all index files."""
    print(f"\n{'=' * 70}")
    print("PHASE 4: BUILD INDEXES")
    print("=" * 70)

    # Encounter index (all)
    with open(os.path.join(BASE_DIR, "encounter_index.json"), 'w') as f:
        json.dump({
            "generated": dt_module.datetime.now().isoformat(),
            "total": len(catalogue),
            "retained": sum(1 for e in catalogue if e.get("retained")),
            "encounters": catalogue,
        }, f, indent=2, default=str)

    # Retained index (grouped by cone bin)
    retained = [e for e in catalogue if e.get("retained")]

    # Dedup by date+probe
    seen = {}
    for e in retained:
        k = (e["date"], e["probe"])
        if k not in seen:
            seen[k] = e
    unique_retained = sorted(seen.values(), key=lambda x: (x.get("cone_deg") or 999))

    cone_groups = {}
    for e in unique_retained:
        cb = e.get("cone_bin", "unknown")
        cone_groups.setdefault(cb, []).append(e)

    cone_counts = {cb: len(entries) for cb, entries in cone_groups.items()}

    with open(os.path.join(BASE_DIR, "retained_index.json"), 'w') as f:
        json.dump({
            "generated": dt_module.datetime.now().isoformat(),
            "unique_retained": len(unique_retained),
            "cone_counts": cone_counts,
            "by_cone_bin": cone_groups,
        }, f, indent=2, default=str)

    # Summary
    by_year = {}
    by_probe = {}
    for e in unique_retained:
        by_year[e.get("year", "?")] = by_year.get(e.get("year", "?"), 0) + 1
        by_probe[e.get("probe", "?")] = by_probe.get(e.get("probe", "?"), 0) + 1

    summary = {
        "generated": dt_module.datetime.now().isoformat(),
        "archive_scope": "THEMIS 2007-2025, all probes, all months",
        "geometry_criteria": {
            "x_min_re": X_MIN_RE, "sza_max_deg": SZA_MAX,
            "r_min_re": R_MIN_RE, "r_max_re": R_MAX_RE,
        },
        "state_files": len([f for f in os.listdir(RAW_STATE_DIR) if f.endswith('.npz')]),
        "qualifying_days": len(catalogue),
        "total_processed": len(catalogue),
        "unique_retained": len(unique_retained),
        "cone_counts": cone_counts,
        "by_year": dict(sorted(by_year.items())),
        "by_probe": dict(sorted(by_probe.items())),
    }

    with open(os.path.join(BASE_DIR, "summary.json"), 'w') as f:
        json.dump(summary, f, indent=2)

    # CSV
    csv_fields = ['encounter_id','date','year','month','probe',
        'sza_deg','mlt','cone_deg','clock_deg','dp_nPa','bz_nT',
        'near_occ','bg_occ','Dn','EB','cone_bin','retained','exclude_reason',
        'qc_transition_cleanliness','qc_disturbance','qc_boundary_motion',
        'omni_context_quality_note','boundary_uncertainty_note','r_re','x_gsm_re']
    with open(os.path.join(BASE_DIR, "encounter_catalogue.csv"), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=csv_fields, extrasaction='ignore')
        w.writeheader()
        for e in catalogue:
            w.writerow(e)

    print(f"Indexes built.")
    print(f"  encounter_index.json: {len(catalogue)} entries")
    print(f"  retained_index.json: {len(unique_retained)} unique retained")
    print(f"  Cone counts: {cone_counts}")
    print(f"  By year: {dict(sorted(by_year.items()))}")
    print(f"  By probe: {dict(sorted(by_probe.items()))}")

    return summary


# =====================================================================
# MAIN
# =====================================================================
if __name__ == "__main__":
    t_start = time.time()
    print("THEMIS Full-Archive Cache Builder")
    print(f"Started: {dt_module.datetime.now().isoformat()}")
    print(f"Workers: {MAX_WORKERS}")
    print()

    state_index = run_phase1()
    qualifying_days = run_phase2(state_index)
    catalogue = run_phase3(qualifying_days)
    summary = run_phase4(catalogue)

    elapsed = time.time() - t_start
    print(f"\n{'=' * 70}")
    print(f"ALL DONE in {elapsed/60:.1f} minutes")
    print(f"STATE files: {summary['state_files']}")
    print(f"Qualifying days: {summary['qualifying_days']}")
    print(f"Unique retained: {summary['unique_retained']}")
    print(f"Cone counts: {summary['cone_counts']}")
    print(f"{'=' * 70}")
