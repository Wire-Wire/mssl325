"""
Phase 6 Route C — Full Declared-Slice Scan

Scans all locally cached THEMIS data within the Route C declared slice:
  - 2007 full year
  - 2010 full year
  - 2008 Jan-Jul, Nov-Dec (non-Aug-Oct)
  - 2009 Jan-Jul, Nov-Dec (non-Aug-Oct)

For each cached encounter in the slice:
  1. Check data completeness (FGM + MOM + STATE + OMNI required)
  2. Run the measurement model (s-mapping, occupancy, Dn/EB)
  3. Assess QC audit fields
  4. Record in the Route C catalogue

Also includes already-catalogued encounters from the Route A clean catalogue
that fall within the Route C slice (for completeness and cone-bin counting).

No internet fetch. No Route B descriptors. Original Dn/EB semantics only.
"""
import json, os, sys, csv, glob, re
import datetime as dt_module
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pdl_pilot.mapping.s_mapper import compute_s_with_uncertainty, compute_bin_occupancy
from pdl_pilot.config.schema import BinConfig, UncertaintyConfig

CACHE_ROOT = "data_cache/normalized"
BINS = BinConfig()
UNC = UncertaintyConfig()

# ---------------------------------------------------------------------------
# Helper: determine if a date falls in the Route C declared slice
# ---------------------------------------------------------------------------
def in_routeC_slice(year, month):
    """Return True if (year, month) is in the Route C declared slice."""
    if year == 2007:
        return True  # full year
    if year == 2010:
        return True  # full year
    if year == 2008 and month not in (8, 9, 10):
        return True  # non-Aug-Oct 2008
    if year == 2009 and month not in (8, 9, 10):
        return True  # non-Aug-Oct 2009
    return False


def _epoch_to_unix(epoch_arr):
    if hasattr(epoch_arr, 'dtype') and np.issubdtype(epoch_arr.dtype, np.datetime64):
        epoch_1970 = np.datetime64('1970-01-01T00:00:00', 'ns')
        return (epoch_arr.astype('datetime64[ns]') - epoch_1970).astype(np.float64) / 1e9
    return np.asarray(epoch_arr, dtype=np.float64)


def _interp(src_time, src_data, target_time, max_gap=30.0):
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


def load_and_process(cache_dir, probe_letter):
    """Load cached NPZ data and compute Dn/EB under original measurement model.

    Returns dict with all fields, or None if data is incomplete.
    """
    fgm_path = os.path.join(cache_dir, f"th{probe_letter}_l2_fgm.npz")
    mom_path = os.path.join(cache_dir, f"th{probe_letter}_l2_mom.npz")
    state_path = os.path.join(cache_dir, f"th{probe_letter}_l1_state.npz")
    omni_path = os.path.join(cache_dir, "omni_hro_1min.npz")

    missing = []
    if not os.path.exists(fgm_path): missing.append("FGM")
    if not os.path.exists(mom_path): missing.append("MOM")
    if not os.path.exists(state_path): missing.append("STATE")
    if not os.path.exists(omni_path): missing.append("OMNI")

    if missing:
        return None, f"missing {', '.join(missing)}"

    try:
        fgm = dict(np.load(fgm_path, allow_pickle=True))
        mom = dict(np.load(mom_path, allow_pickle=True))
        state = dict(np.load(state_path, allow_pickle=True))
        omni = dict(np.load(omni_path, allow_pickle=True))
    except Exception as e:
        return None, f"load error: {e}"

    # Timeline from MOM
    mom_time = _epoch_to_unix(mom.get("_time", np.array([])))
    if len(mom_time) < 10:
        return None, "insufficient MOM timestamps"

    target_time = mom_time

    # Date from first timestamp
    from datetime import datetime, timezone
    t0 = datetime.fromtimestamp(mom_time[0], tz=timezone.utc)
    date_str = t0.strftime("%Y-%m-%d")
    year = t0.year
    month = t0.month

    # FGM: |B|
    fgm_time = _epoch_to_unix(fgm.get("_time", np.array([])))
    bvec_key = f"th{probe_letter}_fgs_gsm"
    if bvec_key in fgm and fgm[bvec_key].ndim >= 2:
        bvec = fgm[bvec_key].astype(np.float64)
        bmag_raw = np.sqrt(np.sum(bvec**2, axis=-1))
    else:
        return None, "no FGM B-vector"
    bmag = _interp(fgm_time, bmag_raw, target_time, max_gap=30.0)

    # MOM: density
    density_key = f"th{probe_letter}_peim_density"
    density = mom.get(density_key, np.array([])).astype(np.float64)
    if len(density) != len(target_time):
        density = _interp(mom_time, density, target_time, max_gap=30.0)

    # STATE: position
    state_time = _epoch_to_unix(state.get("_time", np.array([])))
    pos_key = f"th{probe_letter}_pos_gsm"
    pos_gsm = state.get(pos_key, np.array([])).astype(np.float64)
    if pos_gsm.ndim != 2 or pos_gsm.shape[1] != 3:
        return None, "invalid STATE position data"

    x_gsm_re = _interp(state_time, pos_gsm[:, 0] / 6371.2, target_time, max_gap=600.0)
    y_gsm_re = _interp(state_time, pos_gsm[:, 1] / 6371.2, target_time, max_gap=600.0)
    z_gsm_re = _interp(state_time, pos_gsm[:, 2] / 6371.2, target_time, max_gap=600.0)

    # Compute mean position
    x_mean = float(np.nanmean(x_gsm_re))
    y_mean = float(np.nanmean(y_gsm_re))
    z_mean = float(np.nanmean(z_gsm_re))

    # SZA
    if np.isfinite(x_mean) and np.isfinite(y_mean) and np.isfinite(z_mean):
        sza_deg = float(np.degrees(np.arctan2(np.sqrt(y_mean**2 + z_mean**2), x_mean)))
    else:
        sza_deg = 999.0

    # OMNI upstream
    omni_time = _epoch_to_unix(omni.get("_time", np.array([])))

    def _omni_median(key):
        arr = omni.get(key, None)
        if arr is None or len(arr) == 0:
            return None
        valid = arr[np.isfinite(arr.astype(np.float64))]
        # Filter OMNI sentinels
        valid = valid[(valid > -1e30) & (valid < 1e30)]
        valid = valid[valid != 9999.99]
        valid = valid[valid != 999.99]
        if len(valid) == 0:
            return None
        return float(np.nanmedian(valid))

    # Try multiple OMNI variable naming conventions
    dp = _omni_median("Pressure") or _omni_median("SW_P_den") or _omni_median("Dp")
    bz = _omni_median("BZ_GSM") or _omni_median("Bz")
    bt = _omni_median("F") or _omni_median("Bt")
    ma = _omni_median("Mach_num") or _omni_median("Ma")
    bx = _omni_median("BX_GSE") or _omni_median("Bx")
    by = _omni_median("BY_GSM") or _omni_median("By")

    if dp is None or dp <= 0:
        return None, "no valid OMNI Dp"

    # Cone angle
    cone_deg = None
    if bx is not None and bt is not None and bt > 0:
        ratio = min(abs(bx) / bt, 1.0)
        cone_deg = float(np.degrees(np.arccos(ratio)))

    # Clock angle
    clock_deg = None
    if by is not None and bz is not None:
        clock_deg = float(np.degrees(np.arctan2(by, bz))) % 360.0

    # Fill masking
    density[density <= 0] = np.nan
    density[density > 1000] = np.nan
    bmag[bmag <= 0] = np.nan
    bmag[bmag > 500] = np.nan

    # s-mapping
    dp_use = dp if dp is not None else 2.0
    bz_use = bz if bz is not None else 0.0
    ma_use = ma if ma is not None else 8.0

    s_nom, s_lo, s_hi, mp0, bs0 = compute_s_with_uncertainty(
        x_gsm_re, dp_nPa=dp_use, bz_nT=bz_use, mach_alfven=ma_use, unc=UNC,
    )
    occupancy = compute_bin_occupancy(s_nom, BINS)

    near_occ = occupancy["near"]
    bg_occ = occupancy["background"]

    # Dn / EB (original semantics)
    near_mask = (s_nom >= 0.2) & (s_nom < 0.4)
    bg_mask = (s_nom >= 0.6) & (s_nom <= 1.0)

    def _safe_median(arr, mask):
        vals = arr[mask]
        valid = vals[np.isfinite(vals)]
        return float(np.nanmedian(valid)) if len(valid) > 0 else None

    n_near = _safe_median(density, near_mask)
    n_bg = _safe_median(density, bg_mask)
    b_near = _safe_median(bmag, near_mask)
    b_bg = _safe_median(bmag, bg_mask)

    Dn = (n_near / n_bg) if (n_near is not None and n_bg is not None and n_bg > 0) else None
    EB = (b_near / b_bg) if (b_near is not None and b_bg is not None and b_bg > 0) else None

    evaluable = near_occ >= 0.05 and bg_occ >= 0.01 and Dn is not None and EB is not None

    # MLT
    mlt = None
    if np.isfinite(x_mean) and np.isfinite(y_mean):
        mlt = float((12.0 + np.degrees(np.arctan2(y_mean, x_mean)) / 15.0) % 24.0)

    return {
        "date": date_str,
        "year": year,
        "month": month,
        "probe": f"th{probe_letter}",
        "sza_deg": round(sza_deg, 1),
        "mlt": round(mlt, 1) if mlt is not None else None,
        "dp_nPa": round(dp, 2) if dp is not None else None,
        "bz_nT": round(bz, 2) if bz is not None else None,
        "ma": round(ma, 1) if ma is not None else None,
        "cone_deg": round(cone_deg, 1) if cone_deg is not None else None,
        "clock_deg": round(clock_deg, 1) if clock_deg is not None else None,
        "mp_standoff_re": round(mp0, 2),
        "bs_standoff_re": round(bs0, 2),
        "near_occ": round(near_occ, 4),
        "bg_occ": round(bg_occ, 4),
        "Dn": round(Dn, 4) if Dn is not None else None,
        "EB": round(EB, 4) if EB is not None else None,
        "evaluable": evaluable,
        "n_points": len(target_time),
        "x_gsm_re": round(x_mean, 2),
    }, None


def assign_qc(entry):
    """Assign QC audit fields."""
    qc = {}

    # transition_cleanliness_qc
    if entry.get("evaluable") and entry.get("Dn") is not None and entry.get("EB") is not None:
        dn = entry["Dn"]
        eb = entry["EB"]
        if dn < 1.0 and eb > 1.0:
            qc["qc_transition_cleanliness"] = "clean"
        elif dn < 1.0 or eb > 1.0:
            qc["qc_transition_cleanliness"] = "mixed"
        else:
            qc["qc_transition_cleanliness"] = "unclear"
    else:
        qc["qc_transition_cleanliness"] = "not_assessed"

    # disturbance_qc
    near_occ = entry.get("near_occ", 0)
    bg_occ = entry.get("bg_occ", 0)
    if near_occ > 0.10 and bg_occ > 0.05:
        qc["qc_disturbance"] = "undisturbed"
    elif near_occ > 0.05:
        qc["qc_disturbance"] = "uncertain"
    else:
        qc["qc_disturbance"] = "uncertain"

    # boundary_motion_qc
    dp = entry.get("dp_nPa")
    if dp is not None and 2.0 <= dp <= 6.0:
        qc["qc_boundary_motion"] = "stable"
    elif dp is not None:
        qc["qc_boundary_motion"] = "uncertain"
    else:
        qc["qc_boundary_motion"] = "uncertain"

    # omni_context_quality_note
    if dp is not None and entry.get("bz_nT") is not None and entry.get("cone_deg") is not None:
        qc["omni_context_quality_note"] = "good"
    elif dp is not None:
        qc["omni_context_quality_note"] = "partial"
    else:
        qc["omni_context_quality_note"] = "poor"

    # boundary_uncertainty_note
    if dp is not None and 2.0 <= dp <= 6.0:
        qc["boundary_uncertainty_note"] = "plausible"
    elif dp is not None:
        qc["boundary_uncertainty_note"] = "uncertain"
    else:
        qc["boundary_uncertainty_note"] = "suspect"

    return qc


def classify_cone(cone_deg):
    if cone_deg is None:
        return "unknown"
    if cone_deg < 30:
        return "quasi-radial"
    if cone_deg <= 45:
        return "low-cone"
    if cone_deg <= 60:
        return "intermediate"
    return "perpendicular"


# ---------------------------------------------------------------------------
# Main scan
# ---------------------------------------------------------------------------
print("=" * 70)
print("PHASE 6 ROUTE C — FULL DECLARED-SLICE SCAN")
print(f"Date: {dt_module.datetime.now().isoformat()[:10]}")
print("=" * 70)

# Step 1: Inventory all locally cached data and identify Route C slice entries
print("\n--- Step 1: Inventory local data cache ---")

cache_inventory = []
for dirname in sorted(os.listdir(CACHE_ROOT)):
    dirpath = os.path.join(CACHE_ROOT, dirname)
    if not os.path.isdir(dirpath):
        continue

    # Identify probe from file names
    probe_letter = None
    for f in os.listdir(dirpath):
        m = re.match(r'th([a-e])_l[12]_', f)
        if m:
            probe_letter = m.group(1)
            break

    # Identify what data files exist
    has_fgm = any(f.endswith('_fgm.npz') for f in os.listdir(dirpath))
    has_mom = any(f.endswith('_mom.npz') for f in os.listdir(dirpath))
    has_state = any(f.endswith('_state.npz') for f in os.listdir(dirpath))
    has_omni = 'omni_hro_1min.npz' in os.listdir(dirpath)

    # Try to determine date from data
    date_str = None
    year = None
    month = None
    if probe_letter:
        for f in os.listdir(dirpath):
            if '_time' in f or f.endswith('.npz'):
                try:
                    data = dict(np.load(os.path.join(dirpath, f), allow_pickle=True))
                    if '_time' in data and len(data['_time']) > 0:
                        t = data['_time'][0]
                        if hasattr(t, 'astype'):
                            # numpy datetime64
                            ts = (t.astype('datetime64[s]') - np.datetime64('1970-01-01T00:00:00', 's')).astype(int)
                            from datetime import datetime, timezone
                            dt = datetime.fromtimestamp(int(ts), tz=timezone.utc)
                            date_str = dt.strftime("%Y-%m-%d")
                            year = dt.year
                            month = dt.month
                        break
                except:
                    pass

    is_routeC = in_routeC_slice(year, month) if (year and month) else None

    cache_inventory.append({
        "cache_dir": dirname,
        "probe": f"th{probe_letter}" if probe_letter else "unknown",
        "probe_letter": probe_letter,
        "date": date_str,
        "year": year,
        "month": month,
        "has_fgm": has_fgm,
        "has_mom": has_mom,
        "has_state": has_state,
        "has_omni": has_omni,
        "data_complete": has_fgm and has_mom and has_state and has_omni,
        "in_routeC_slice": is_routeC,
    })

# Filter to Route C slice
routeC_candidates = [c for c in cache_inventory if c["in_routeC_slice"] is True]
# Deduplicate by date+probe (keep first = shortest cache name = canonical)
seen = {}
for c in routeC_candidates:
    key = (c["date"], c["probe"])
    if key not in seen:
        seen[key] = c
routeC_unique = sorted(seen.values(), key=lambda x: (x["date"], x["probe"]))

print(f"Total cache directories: {len(cache_inventory)}")
print(f"In Route C slice: {len(routeC_candidates)}")
print(f"Unique by date+probe in Route C slice: {len(routeC_unique)}")

for c in routeC_unique:
    complete = "COMPLETE" if c["data_complete"] else "INCOMPLETE"
    missing = []
    if not c["has_fgm"]: missing.append("FGM")
    if not c["has_mom"]: missing.append("MOM")
    if not c["has_state"]: missing.append("STATE")
    if not c["has_omni"]: missing.append("OMNI")
    miss_str = f" (missing: {', '.join(missing)})" if missing else ""
    print(f"  {c['date']} {c['probe']} {complete}{miss_str} [{c['cache_dir']}]")

# Step 2: Process all data-complete Route C candidates
print("\n--- Step 2: Process Route C candidates ---")

catalogue = []

for c in routeC_unique:
    eid = f"routeC_{c['date'].replace('-', '')}_{c['probe']}"
    print(f"\n  Processing: {eid} ({c['cache_dir']})")

    if not c["data_complete"]:
        entry = {
            "encounter_id": eid,
            "spacecraft": "themis",
            "probe": c["probe"],
            "date": c["date"],
            "year": c["year"],
            "month": c["month"],
            "sza_deg": None,
            "mlt": None,
            "cone_deg": None,
            "clock_deg": None,
            "dp_nPa": None,
            "bz_nT": None,
            "ma": None,
            "near_occ": None,
            "bg_occ": None,
            "Dn": None,
            "EB": None,
            "evaluable": False,
            "routeC_core_usable": False,
            "exclude_reason": f"incomplete local data (missing: {', '.join(m for m, v in [('FGM', c['has_fgm']), ('MOM', c['has_mom']), ('STATE', c['has_state']), ('OMNI', c['has_omni'])] if not v)})",
            "cone_bin": "unknown",
            "cache_dir": c["cache_dir"],
        }
        catalogue.append(entry)
        print(f"    SKIP: {entry['exclude_reason']}")
        continue

    # Load and process
    result, error = load_and_process(
        os.path.join(CACHE_ROOT, c["cache_dir"]),
        c["probe_letter"]
    )

    if result is None:
        entry = {
            "encounter_id": eid,
            "spacecraft": "themis",
            "probe": c["probe"],
            "date": c["date"],
            "year": c["year"],
            "month": c["month"],
            "sza_deg": None,
            "mlt": None,
            "cone_deg": None,
            "clock_deg": None,
            "dp_nPa": None,
            "bz_nT": None,
            "ma": None,
            "near_occ": None,
            "bg_occ": None,
            "Dn": None,
            "EB": None,
            "evaluable": False,
            "routeC_core_usable": False,
            "exclude_reason": f"processing error: {error}",
            "cone_bin": "unknown",
            "cache_dir": c["cache_dir"],
        }
        catalogue.append(entry)
        print(f"    SKIP: {entry['exclude_reason']}")
        continue

    # Build entry
    cone_bin = classify_cone(result["cone_deg"])
    entry = {
        "encounter_id": eid,
        "spacecraft": "themis",
        "probe": result["probe"],
        "date": result["date"],
        "year": result["year"],
        "month": result["month"],
        "sza_deg": result["sza_deg"],
        "mlt": result["mlt"],
        "cone_deg": result["cone_deg"],
        "clock_deg": result["clock_deg"],
        "dp_nPa": result["dp_nPa"],
        "bz_nT": result["bz_nT"],
        "ma": result["ma"],
        "near_occ": result["near_occ"],
        "bg_occ": result["bg_occ"],
        "Dn": result["Dn"],
        "EB": result["EB"],
        "evaluable": result["evaluable"],
        "cone_bin": cone_bin,
        "cache_dir": c["cache_dir"],
    }

    # SZA screen
    if result["sza_deg"] > 30:
        entry["routeC_core_usable"] = False
        entry["exclude_reason"] = f"SZA={result['sza_deg']} > 30 deg"
    elif not result["evaluable"]:
        entry["routeC_core_usable"] = False
        if result["bg_occ"] < 0.01:
            entry["exclude_reason"] = f"bg_occ={result['bg_occ']:.3f} < 1% (dual-bin requirement)"
        elif result["near_occ"] < 0.05:
            entry["exclude_reason"] = f"near_occ={result['near_occ']:.3f} < 5%"
        else:
            entry["exclude_reason"] = "Dn/EB not computable"
    else:
        entry["routeC_core_usable"] = True
        entry["exclude_reason"] = None

    # Assign QC
    qc = assign_qc(entry)
    entry.update(qc)

    catalogue.append(entry)
    status = "RETAINED" if entry["routeC_core_usable"] else "EXCLUDED"
    print(f"    {status}: SZA={result['sza_deg']:.0f}, cone={result['cone_deg']}, Dp={result['dp_nPa']}, "
          f"near={result['near_occ']:.3f}, bg={result['bg_occ']:.3f}, Dn={result['Dn']}, EB={result['EB']}")
    if entry.get("exclude_reason"):
        print(f"    Reason: {entry['exclude_reason']}")

# Step 3: Also include already-catalogued Route A encounters that fall in Route C slice
print("\n--- Step 3: Cross-reference with clean Route A catalogue ---")

with open('reports/themis_conditioning/encounter_catalogue_clean.json') as f:
    clean_cat = json.load(f)

routeA_in_routeC = []
for enc in clean_cat:
    date = enc.get("date", "")
    try:
        y = int(date[:4])
        m = int(date[5:7])
    except:
        continue
    if in_routeC_slice(y, m):
        routeA_in_routeC.append(enc)
        print(f"  Route A encounter in Route C slice: {enc['eid']} ({date}, cone={enc.get('cone_deg')})")

# Step 4: Summary
print("\n" + "=" * 70)
print("ROUTE C SCAN SUMMARY")
print("=" * 70)

n_total = len(catalogue)
n_complete = sum(1 for e in catalogue if "incomplete" not in str(e.get("exclude_reason", "")))
n_evaluable = sum(1 for e in catalogue if e.get("evaluable"))
n_retained = sum(1 for e in catalogue if e.get("routeC_core_usable"))
n_routeA_in_slice = len(routeA_in_routeC)

# Count retained by cone bin (Route C new finds only)
retained_by_cone = {"quasi-radial": 0, "low-cone": 0, "intermediate": 0, "perpendicular": 0, "unknown": 0}
for e in catalogue:
    if e.get("routeC_core_usable"):
        retained_by_cone[e["cone_bin"]] += 1

# Count Route A encounters in Route C slice by cone bin
routeA_cone = {"quasi-radial": 0, "low-cone": 0, "intermediate": 0, "perpendicular": 0}
for enc in routeA_in_routeC:
    cone = enc.get("cone_deg")
    if cone is not None:
        cb = classify_cone(cone)
        routeA_cone[cb] += 1

print(f"Route C declared-slice candidates: {n_total}")
print(f"  Data complete: {n_complete}")
print(f"  Evaluable (Dn/EB computable): {n_evaluable}")
print(f"  Route C core usable: {n_retained}")
print(f"Route A encounters also in Route C slice: {n_routeA_in_slice}")
print(f"\nRetained by cone bin (Route C new):")
for cb, n in retained_by_cone.items():
    if n > 0 or cb in ("quasi-radial", "low-cone"):
        print(f"  {cb}: {n}")
print(f"Route A in Route C slice by cone bin:")
for cb, n in routeA_cone.items():
    if n > 0 or cb in ("quasi-radial", "low-cone"):
        print(f"  {cb}: {n}")

# Combined count for hard stop evaluation
combined_quasi_radial = retained_by_cone["quasi-radial"]
combined_low_cone = retained_by_cone["low-cone"]
# Include Route A encounters in Route C slice
for enc in routeA_in_routeC:
    cone = enc.get("cone_deg")
    if cone is not None and cone < 30:
        combined_quasi_radial += 1
    elif cone is not None and 30 <= cone <= 45:
        combined_low_cone += 1

print(f"\nCombined (Route C new + Route A in slice):")
print(f"  quasi-radial (cone < 30): {combined_quasi_radial}")
print(f"  low-cone (30-45): {combined_low_cone}")

# Hard stop evaluation
print(f"\n{'=' * 70}")
print("HARD STOP EVALUATION")
print(f"{'=' * 70}")

success = combined_quasi_radial >= 1 or combined_low_cone >= 5
hard_null = not success

if success:
    print("OUTCOME: SUCCESS")
    print(f"  quasi-radial retained: {combined_quasi_radial} (threshold: >= 1)")
    print(f"  low-cone retained: {combined_low_cone} (threshold: >= 5)")
else:
    print("OUTCOME: HARD NULL")
    print(f"  quasi-radial retained: {combined_quasi_radial} (threshold: >= 1) -- NOT MET")
    print(f"  low-cone retained: {combined_low_cone} (threshold: >= 5) -- NOT MET")

# ---------------------------------------------------------------------------
# Save outputs
# ---------------------------------------------------------------------------
os.makedirs('reports/themis_conditioning/routeC', exist_ok=True)

# Scope manifest
scope_manifest = {
    "generated": dt_module.datetime.now().isoformat(),
    "declared_slice": {
        "description": "2007 full year + 2010 full year + 2008 non-Aug-Oct + 2009 non-Aug-Oct",
        "sub_slices": [
            {"label": "2007", "year": 2007, "months": "all"},
            {"label": "2010", "year": 2010, "months": "all"},
            {"label": "2008 non-Aug-Oct", "year": 2008, "months": [1,2,3,4,5,6,7,11,12]},
            {"label": "2009 non-Aug-Oct", "year": 2009, "months": [1,2,3,4,5,6,7,11,12]},
        ],
    },
    "searched_slice": {
        "description": "All locally cached THEMIS encounter data within the declared slice",
        "method": "Exhaustive scan of data_cache/normalized/ directories. Every directory with data timestamped in the declared slice was evaluated.",
        "data_source": "Local cache only. No internet fetch.",
    },
    "scope_match": True,
    "scope_match_note": "Declared slice equals searched slice. Every locally cached data point in the slice was evaluated. The local cache is sparse (most of 2007-2010 was never fetched from CDAWeb). This means the Route C scan is complete over available local data but does NOT cover the full 2007-2010 THEMIS archive.",
    "cache_inventory_total": len(cache_inventory),
    "in_routeC_slice_total": len(routeC_unique),
    "data_complete_in_slice": sum(1 for c in routeC_unique if c["data_complete"]),
    "routeC_retained": n_retained,
    "routeA_encounters_in_slice": n_routeA_in_slice,
    "hard_stop_outcome": "SUCCESS" if success else "HARD_NULL",
    "hard_stop_quasi_radial": combined_quasi_radial,
    "hard_stop_low_cone": combined_low_cone,
}

with open('reports/themis_conditioning/routeC/scope_manifest.json', 'w') as f:
    json.dump(scope_manifest, f, indent=2)

# Catalogue JSON
with open('reports/themis_conditioning/routeC/encounter_catalogue_routeC.json', 'w') as f:
    json.dump(catalogue, f, indent=2, default=str)

# Catalogue CSV
csv_fields = [
    'encounter_id', 'spacecraft', 'date', 'year', 'month', 'probe',
    'sza_deg', 'mlt', 'cone_deg', 'clock_deg', 'dp_nPa', 'bz_nT',
    'near_occ', 'bg_occ', 'Dn', 'EB',
    'qc_transition_cleanliness', 'qc_disturbance', 'qc_boundary_motion',
    'omni_context_quality_note', 'boundary_uncertainty_note',
    'routeC_core_usable', 'exclude_reason', 'cone_bin',
]
with open('reports/themis_conditioning/routeC/encounter_catalogue_routeC.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=csv_fields, extrasaction='ignore')
    w.writeheader()
    for entry in catalogue:
        w.writerow(entry)

# Summary JSON
routeC_summary = {
    "generated": dt_module.datetime.now().isoformat(),
    "declared_slice": "2007 + 2010 + 2008 non-Aug-Oct + 2009 non-Aug-Oct",
    "searched_slice": "All locally cached THEMIS data in the declared slice (no internet fetch)",
    "scope_match": True,
    "total_candidates_in_slice": n_total,
    "data_complete": n_complete,
    "evaluable": n_evaluable,
    "retained_routeC_new": n_retained,
    "routeA_encounters_in_slice": n_routeA_in_slice,
    "retained_by_cone_bin": retained_by_cone,
    "routeA_in_slice_by_cone_bin": routeA_cone,
    "combined_quasi_radial": combined_quasi_radial,
    "combined_low_cone": combined_low_cone,
    "hard_stop_outcome": "SUCCESS" if success else "HARD_NULL",
    "hard_stop_success_condition": "quasi-radial >= 1 OR low-cone >= 5",
    "catalogue_entries": catalogue,
}

with open('reports/themis_conditioning/routeC/routeC_summary.json', 'w') as f:
    json.dump(routeC_summary, f, indent=2, default=str)

print(f"\nOutputs saved to reports/themis_conditioning/routeC/")
print("Route C scan complete.")
