"""
Phase 6 Route 3B — Bounded Execution

Computes the Route B auxiliary descriptors (Δn_near, Δ|B|_near) for all
Route-B-computable encounters in the clean Route A universe.

Route B descriptors:
  Δn_near  = median(density in s=[0.0, 0.2]) / median(density in s=[0.2, 0.4])
  Δ|B|_near = median(|B| in s=[0.0, 0.2]) / median(|B| in s=[0.2, 0.4])

These do NOT require background-bin occupancy.  They are explicitly NOT
Dn / EB and are NOT interchangeable with frozen Phase 4B values.

Input: 5 Route-B-computable encounters (4 tranche-1 + 1 tranche-2 recovered)
  plus 7 non-computable encounters logged as NaN for completeness.

Outputs:
  reports/themis_conditioning/route3b_ledger.json
  reports/themis_conditioning/route3b_ledger.csv
  reports/themis_conditioning/route3b_coherence_assessment.md
"""
import json, os, sys, csv, datetime, glob
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pdl_pilot.mapping.s_mapper import compute_s_with_uncertainty, compute_bin_occupancy
from pdl_pilot.config.schema import BinConfig, UncertaintyConfig
from pdl_pilot.data.masking import mask_fill_values

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
CACHE_ROOT = "data_cache/normalized"
BINS = BinConfig()  # defaults: vn=[0.0,0.2], near=[0.2,0.4], bg=[0.6,1.0]
UNC = UncertaintyConfig()  # default fractional uncertainties

# All 12 encounters: 9 clean tranche-1 + 3 tranche-2 low-cone
# Ordered: Route-B-computable first, then non-computable
ENCOUNTERS = [
    # === ROUTE B COMPUTABLE (vn_occ > 1% AND near_occ >= 1%) ===
    {"eid": "usable_aug18_6h",    "probe": "thd", "tstart": "2008-08-18T18:00:00", "tend": "2008-08-19T00:00:00",
     "dp": 4.25, "bz": 0.33, "ma": 11.2, "cone_deg": 30.7, "tranche": 1, "rb_computable": True},
    {"eid": "usable_sep03_5h",    "probe": "thd", "tstart": "2008-09-03T20:00:00", "tend": "2008-09-04T01:00:00",
     "dp": 3.69, "bz": 0.51, "ma": 5.9, "cone_deg": 56.2, "tranche": 1, "rb_computable": True},
    {"eid": "usable_sep26_09_10h","probe": "thd", "tstart": "2009-09-26T14:00:00", "tend": "2009-09-27T00:00:00",
     "dp": 3.045, "bz": 0.85, "ma": 15.05, "cone_deg": 84.6, "tranche": 1, "rb_computable": True},
    {"eid": "usable_sep27_09_10h","probe": "thd", "tstart": "2009-09-27T14:00:00", "tend": "2009-09-28T00:00:00",
     "dp": 3.12, "bz": -1.71, "ma": 20.6, "cone_deg": 56.6, "tranche": 1, "rb_computable": True},
    {"eid": "t2_20080904_thd",    "probe": "thd", "tstart": "2008-09-04T15:00:00", "tend": "2008-09-04T21:00:00",
     "dp": 2.56, "bz": -0.15, "ma": 12.7, "cone_deg": 43.3, "tranche": 2, "rb_computable": True},
    # === NOT ROUTE B COMPUTABLE (vn_occ = 0 or < 1%) ===
    {"eid": "cand4a_sep19_08_the","probe": "the", "tstart": "2008-09-19T12:00:00", "tend": "2008-09-19T18:00:00",
     "dp": 2.77, "bz": -1.82, "ma": 21.1, "cone_deg": 64.2, "tranche": 1, "rb_computable": False},
    {"eid": "usable_sep13_09_6h", "probe": "thd", "tstart": "2009-09-13T18:00:00", "tend": "2009-09-14T00:00:00",
     "dp": 3.14, "bz": -1.35, "ma": 9.4, "cone_deg": 61.2, "tranche": 1, "rb_computable": False},
    {"eid": "usable_sep20_09_6h", "probe": "thd", "tstart": "2009-09-20T18:00:00", "tend": "2009-09-21T00:00:00",
     "dp": 3.02, "bz": 1.42, "ma": 10.9, "cone_deg": 70.0, "tranche": 1, "rb_computable": False},
    {"eid": "usable_oct24_09_6h", "probe": "thd", "tstart": "2009-10-24T18:00:00", "tend": "2009-10-25T00:00:00",
     "dp": 4.23, "bz": -0.5, "ma": 11.2, "cone_deg": 86.4, "tranche": 1, "rb_computable": False},
    {"eid": "cand4a_oct23_10_thd","probe": "thd", "tstart": "2010-10-23T12:00:00", "tend": "2010-10-23T18:00:00",
     "dp": 3.11, "bz": 2.15, "ma": 8.7, "cone_deg": 35.0, "tranche": 1, "rb_computable": False},
    {"eid": "t2_20090928_thd",    "probe": "thd", "tstart": "2009-09-28T15:00:00", "tend": "2009-09-28T21:00:00",
     "dp": None, "bz": None, "ma": None, "cone_deg": 42.9, "tranche": 2, "rb_computable": False},
    {"eid": "t2_20090928_the",    "probe": "the", "tstart": "2009-09-28T15:00:00", "tend": "2009-09-28T21:00:00",
     "dp": None, "bz": None, "ma": None, "cone_deg": 43.6, "tranche": 2, "rb_computable": False},
]


def _epoch_to_unix(epoch_arr):
    """Convert np.datetime64 to POSIX seconds."""
    if hasattr(epoch_arr, 'dtype') and np.issubdtype(epoch_arr.dtype, np.datetime64):
        epoch_1970 = np.datetime64('1970-01-01T00:00:00', 'ns')
        return (epoch_arr.astype('datetime64[ns]') - epoch_1970).astype(np.float64) / 1e9
    return np.asarray(epoch_arr, dtype=np.float64)


def _interp(src_time, src_data, target_time, max_gap=30.0):
    """Linear interpolation with gap masking."""
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


def load_encounter_data(eid, probe):
    """Load cached NPZ data and return normalized arrays on common timeline."""
    cache_dir = os.path.join(CACHE_ROOT, eid)
    if not os.path.isdir(cache_dir):
        return None

    pl = probe[-1]  # e.g., "thd" -> "d"

    # Load raw NPZ
    fgm_path = os.path.join(cache_dir, f"th{pl}_l2_fgm.npz")
    mom_path = os.path.join(cache_dir, f"th{pl}_l2_mom.npz")
    state_path = os.path.join(cache_dir, f"th{pl}_l1_state.npz")
    omni_path = os.path.join(cache_dir, "omni_hro_1min.npz")

    if not all(os.path.exists(p) for p in [fgm_path, mom_path, state_path]):
        return None

    fgm = dict(np.load(fgm_path, allow_pickle=True))
    mom = dict(np.load(mom_path, allow_pickle=True))
    state = dict(np.load(state_path, allow_pickle=True))

    # Build common timeline from MOM (highest density plasma data)
    mom_time = _epoch_to_unix(mom["_time"])
    if len(mom_time) < 10:
        return None

    target_time = mom_time  # use MOM cadence as reference

    # FGM: |B| from GSM vector
    fgm_time = _epoch_to_unix(fgm["_time"])
    bvec_key = f"th{pl}_fgs_gsm"
    if bvec_key in fgm and fgm[bvec_key].ndim >= 2:
        bvec = fgm[bvec_key].astype(np.float64)
        bmag_raw = np.sqrt(np.sum(bvec**2, axis=-1))
    else:
        return None
    bmag = _interp(fgm_time, bmag_raw, target_time, max_gap=30.0)

    # MOM: density
    density_key = f"th{pl}_peim_density"
    density = mom.get(density_key, np.array([])).astype(np.float64)
    if len(density) != len(target_time):
        # Interpolate if needed
        density = _interp(mom_time, density, target_time, max_gap=30.0)

    # MOM: ptot (for QC only)
    ptot_key = f"th{pl}_peim_ptot"
    ptot_raw = mom.get(ptot_key, np.full(len(target_time), np.nan)).astype(np.float64)
    if len(ptot_raw) != len(target_time):
        ptot_raw = _interp(mom_time, ptot_raw, target_time, max_gap=30.0)

    # STATE: position (lower cadence, interpolate)
    state_time = _epoch_to_unix(state["_time"])
    pos_key = f"th{pl}_pos_gsm"
    pos_gsm = state.get(pos_key, np.array([])).astype(np.float64)
    if pos_gsm.ndim == 2 and pos_gsm.shape[1] == 3:
        # Convert from km to Re (1 Re = 6371.2 km)
        x_gsm_re = _interp(state_time, pos_gsm[:, 0] / 6371.2, target_time, max_gap=600.0)
    else:
        return None

    # Apply basic fill masking
    # OMNI-style sentinels and CDF fills
    density[density <= 0] = np.nan
    density[density > 1000] = np.nan
    bmag[bmag <= 0] = np.nan
    bmag[bmag > 500] = np.nan

    return {
        "time": target_time,
        "density": density,
        "bmag": bmag,
        "ptot": ptot_raw,
        "x_gsm_re": x_gsm_re,
        "n_points": len(target_time),
    }


def compute_route_b_descriptors(data, dp, bz, ma):
    """Compute Route B auxiliary descriptors from encounter data.

    Returns dict with per-bin medians, occupancies, and Route B ratios.
    """
    # s-mapping
    s_nom, s_lo, s_hi, mp0, bs0 = compute_s_with_uncertainty(
        data["x_gsm_re"],
        dp_nPa=dp, bz_nT=bz, mach_alfven=ma,
        unc=UNC,
    )
    occupancy = compute_bin_occupancy(s_nom, BINS)

    # Very-near bin: s in [0.0, 0.2)
    vn_mask = (s_nom >= 0.0) & (s_nom < 0.2)
    # Near bin: s in [0.2, 0.4)
    near_mask = (s_nom >= 0.2) & (s_nom < 0.4)
    # Background bin: s in [0.6, 1.0]
    bg_mask = (s_nom >= 0.6) & (s_nom <= 1.0)

    density = data["density"]
    bmag = data["bmag"]

    def _safe_median(arr, mask):
        vals = arr[mask]
        valid = vals[np.isfinite(vals)]
        if len(valid) == 0:
            return None
        return float(np.nanmedian(valid))

    def _safe_count(mask, arr):
        """Count finite values in masked array."""
        return int(np.sum(np.isfinite(arr[mask])))

    # Per-bin medians
    n_vn = _safe_median(density, vn_mask)
    n_near = _safe_median(density, near_mask)
    n_bg = _safe_median(density, bg_mask)

    b_vn = _safe_median(bmag, vn_mask)
    b_near = _safe_median(bmag, near_mask)
    b_bg = _safe_median(bmag, bg_mask)

    # Per-bin valid counts
    n_vn_count = _safe_count(vn_mask, density)
    n_near_count = _safe_count(near_mask, density)
    n_bg_count = _safe_count(bg_mask, density)
    b_vn_count = _safe_count(vn_mask, bmag)
    b_near_count = _safe_count(near_mask, bmag)

    # Route B auxiliary descriptors
    delta_n_near = None
    if n_vn is not None and n_near is not None and n_near > 0:
        delta_n_near = n_vn / n_near

    delta_b_near = None
    if b_vn is not None and b_near is not None and b_near > 0:
        delta_b_near = b_vn / b_near

    # Original Dn / EB for comparison (where computable)
    Dn_original = None
    if n_near is not None and n_bg is not None and n_bg > 0:
        Dn_original = n_near / n_bg

    EB_original = None
    if b_near is not None and b_bg is not None and b_bg > 0:
        EB_original = b_near / b_bg

    # ptot comparison for QC
    ptot = data["ptot"]
    ptot_vn = _safe_median(ptot, vn_mask)
    ptot_near = _safe_median(ptot, near_mask)

    return {
        # Boundary model
        "mp_standoff_re": round(mp0, 3),
        "bs_standoff_re": round(bs0, 3),
        # Occupancy
        "occ_very_near": round(occupancy["very_near"], 4),
        "occ_near": round(occupancy["near"], 4),
        "occ_background": round(occupancy["background"], 4),
        # Per-bin medians: density (cm^-3)
        "n_median_very_near": round(n_vn, 4) if n_vn is not None else None,
        "n_median_near": round(n_near, 4) if n_near is not None else None,
        "n_median_bg": round(n_bg, 4) if n_bg is not None else None,
        # Per-bin medians: |B| (nT)
        "b_median_very_near": round(b_vn, 4) if b_vn is not None else None,
        "b_median_near": round(b_near, 4) if b_near is not None else None,
        "b_median_bg": round(b_bg, 4) if b_bg is not None else None,
        # Per-bin valid counts
        "n_valid_very_near": n_vn_count,
        "n_valid_near": n_near_count,
        "n_valid_bg": n_bg_count,
        "b_valid_very_near": b_vn_count,
        "b_valid_near": b_near_count,
        # Route B auxiliary descriptors
        "delta_n_near": round(delta_n_near, 4) if delta_n_near is not None else None,
        "delta_b_near": round(delta_b_near, 4) if delta_b_near is not None else None,
        # Original Dn / EB (for cross-check)
        "Dn_recomputed": round(Dn_original, 4) if Dn_original is not None else None,
        "EB_recomputed": round(EB_original, 4) if EB_original is not None else None,
        # ptot medians
        "ptot_median_very_near": round(ptot_vn, 4) if ptot_vn is not None else None,
        "ptot_median_near": round(ptot_near, 4) if ptot_near is not None else None,
        # s-mapping stats
        "s_min": round(float(np.nanmin(s_nom)), 4),
        "s_max": round(float(np.nanmax(s_nom)), 4),
        "s_mean": round(float(np.nanmean(s_nom)), 4),
        "n_points": len(s_nom),
    }


def assign_qc_fields(desc, enc_spec):
    """Assign the 4 Route B QC audit fields.

    These are audit fields only — not labels or exclusion rules.
    """
    qc = {}

    # 1. transition_cleanliness_qc
    # Check if the gradient from very_near to near is monotonic in density
    # (PDL signature: density should decrease toward MP, i.e., delta_n_near < 1)
    dn = desc.get("delta_n_near")
    db = desc.get("delta_b_near")
    if dn is not None and db is not None:
        # Clean = density gradient going down, |B| going up toward MP
        if dn < 1.0 and db > 1.0:
            qc["transition_cleanliness_qc"] = "clean"
        elif dn < 1.0 or db > 1.0:
            qc["transition_cleanliness_qc"] = "mixed"
        else:
            qc["transition_cleanliness_qc"] = "unclear"
    else:
        qc["transition_cleanliness_qc"] = "not_computable"

    # 2. disturbance_qc
    # Based on n_valid counts — low counts suggest transient/jet activity
    n_vn = desc.get("n_valid_very_near", 0)
    n_near = desc.get("n_valid_near", 0)
    if n_vn > 20 and n_near > 20:
        qc["disturbance_qc"] = "undisturbed"
    elif n_vn > 5 and n_near > 10:
        qc["disturbance_qc"] = "uncertain"
    else:
        qc["disturbance_qc"] = "uncertain"

    # 3. omni_context_quality_note
    # Based on whether upstream parameters are available and stable
    dp = enc_spec.get("dp")
    if dp is not None and dp > 0:
        qc["omni_context_quality_note"] = "good"
    else:
        qc["omni_context_quality_note"] = "poor"

    # 4. boundary_uncertainty_note
    # Based on Dp range → boundary model reliability
    if dp is not None:
        if 2.0 <= dp <= 6.0:
            qc["boundary_uncertainty_note"] = "plausible"
        elif 1.0 <= dp < 2.0 or 6.0 < dp <= 8.0:
            qc["boundary_uncertainty_note"] = "uncertain"
        else:
            qc["boundary_uncertainty_note"] = "suspect"
    else:
        qc["boundary_uncertainty_note"] = "uncertain"

    return qc


# ---------------------------------------------------------------------------
# Main execution
# ---------------------------------------------------------------------------
print("=" * 70)
print("PHASE 6 ROUTE 3B — BOUNDED EXECUTION")
print(f"Date: {datetime.datetime.now().isoformat()[:10]}")
print("=" * 70)

ledger = []
computable_results = []

for enc in ENCOUNTERS:
    eid = enc["eid"]
    probe = enc["probe"]
    print(f"\n--- {eid} (tranche {enc['tranche']}, rb_computable={enc['rb_computable']}) ---")

    entry = {
        "eid": eid,
        "probe": probe,
        "date": enc["tstart"][:10],
        "cone_deg": enc["cone_deg"],
        "tranche": enc["tranche"],
        "dp_nPa": enc["dp"],
        "bz_nT": enc["bz"],
        "ma": enc["ma"],
        "route_b_computable": False,
        "route_b_descriptor_computed": False,
    }

    # Load data
    data = load_encounter_data(eid, probe)
    if data is None:
        print(f"  SKIP: no cached data found for {eid}")
        entry["skip_reason"] = "no_cached_data"
        ledger.append(entry)
        continue

    print(f"  Loaded {data['n_points']} points")

    # Can we compute Route B? (need upstream params)
    if enc["dp"] is None:
        print(f"  SKIP: no upstream parameters")
        entry["skip_reason"] = "no_upstream_params"
        ledger.append(entry)
        continue

    # Compute descriptors
    desc = compute_route_b_descriptors(data, enc["dp"], enc["bz"], enc["ma"])

    # Check Route B computability: vn_occ > 1% AND near_occ >= 1%
    vn_occ = desc["occ_very_near"]
    near_occ = desc["occ_near"]
    rb_computable = vn_occ > 0.01 and near_occ >= 0.01
    entry["route_b_computable"] = rb_computable

    if rb_computable and desc["delta_n_near"] is not None:
        entry["route_b_descriptor_computed"] = True

    # Merge descriptor into entry
    entry.update(desc)

    # Assign QC fields
    qc = assign_qc_fields(desc, enc)
    entry.update(qc)

    # Print summary
    dn = desc["delta_n_near"]
    db = desc["delta_b_near"]
    print(f"  occ: vn={vn_occ:.3f}, near={near_occ:.3f}, bg={desc['occ_background']:.3f}")
    print(f"  n_median: vn={desc['n_median_very_near']}, near={desc['n_median_near']}, bg={desc['n_median_bg']}")
    print(f"  b_median: vn={desc['b_median_very_near']}, near={desc['b_median_near']}, bg={desc['b_median_bg']}")
    print(f"  Route B: delta_n_near={dn}, delta_b_near={db}")
    print(f"  Dn_recomputed={desc['Dn_recomputed']}, EB_recomputed={desc['EB_recomputed']}")
    print(f"  QC: {qc}")

    if rb_computable:
        computable_results.append(entry)

    ledger.append(entry)

# ---------------------------------------------------------------------------
# Summary statistics
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("ROUTE B EXECUTION SUMMARY")
print("=" * 70)

n_total = len(ENCOUNTERS)
n_computed = sum(1 for e in ledger if e.get("route_b_descriptor_computed"))
n_rb_computable = sum(1 for e in ledger if e.get("route_b_computable"))
n_tranche1_rb = sum(1 for e in ledger if e.get("route_b_computable") and e["tranche"] == 1)
n_tranche2_rb = sum(1 for e in ledger if e.get("route_b_computable") and e["tranche"] == 2)

print(f"Total encounters: {n_total}")
print(f"Route B computable: {n_rb_computable} / {n_total}")
print(f"  Tranche-1: {n_tranche1_rb}")
print(f"  Tranche-2 (recovered): {n_tranche2_rb}")
print(f"Route B descriptors computed: {n_computed}")

if computable_results:
    dn_vals = [e["delta_n_near"] for e in computable_results if e.get("delta_n_near") is not None]
    db_vals = [e["delta_b_near"] for e in computable_results if e.get("delta_b_near") is not None]
    print(f"\nΔn_near values: {dn_vals}")
    print(f"Δ|B|_near values: {db_vals}")
    if dn_vals:
        print(f"  Δn_near range: [{min(dn_vals):.4f}, {max(dn_vals):.4f}], median={np.median(dn_vals):.4f}")
    if db_vals:
        print(f"  Δ|B|_near range: [{min(db_vals):.4f}, {max(db_vals):.4f}], median={np.median(db_vals):.4f}")

# ---------------------------------------------------------------------------
# Coherence assessment (4 bounded questions)
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("COHERENCE ASSESSMENT")
print("=" * 70)

coherence = {}

# Q1: Does Δn_near < 1 (density drops toward MP) correlate with Δ|B|_near > 1 (|B| rises)?
# This is the PDL signature in the inner sheath.
q1_consistent = 0
q1_mixed = 0
for e in computable_results:
    dn = e.get("delta_n_near")
    db = e.get("delta_b_near")
    if dn is not None and db is not None:
        if dn < 1.0 and db > 1.0:
            q1_consistent += 1
        else:
            q1_mixed += 1

coherence["q1_density_field_anti_correlation"] = {
    "question": "Does Δn_near < 1 (n drops toward MP) co-occur with Δ|B|_near > 1 (B rises)?",
    "n_consistent": q1_consistent,
    "n_mixed": q1_mixed,
    "n_total": len(computable_results),
    "assessment": "consistent" if q1_consistent > q1_mixed else "mixed" if q1_consistent > 0 else "inconsistent"
}
print(f"\nQ1 (density-field anti-correlation): {q1_consistent}/{len(computable_results)} consistent")

# Q2: Is the recovered low-cone encounter (t2_20080904_thd) qualitatively different from the tranche-1 set?
t2_entry = next((e for e in computable_results if e["eid"] == "t2_20080904_thd"), None)
t1_entries = [e for e in computable_results if e["tranche"] == 1]
if t2_entry and t1_entries:
    t1_dn = [e["delta_n_near"] for e in t1_entries if e.get("delta_n_near") is not None]
    t1_db = [e["delta_b_near"] for e in t1_entries if e.get("delta_b_near") is not None]
    t2_dn = t2_entry.get("delta_n_near")
    t2_db = t2_entry.get("delta_b_near")

    t2_within_range_dn = min(t1_dn) <= t2_dn <= max(t1_dn) if t1_dn and t2_dn else None
    t2_within_range_db = min(t1_db) <= t2_db <= max(t1_db) if t1_db and t2_db else None

    coherence["q2_low_cone_comparison"] = {
        "question": "Is t2_20080904_thd (cone=43°) within the range of tranche-1 values?",
        "t2_delta_n_near": t2_dn,
        "t2_delta_b_near": t2_db,
        "t1_delta_n_near_range": [min(t1_dn), max(t1_dn)] if t1_dn else None,
        "t1_delta_b_near_range": [min(t1_db), max(t1_db)] if t1_db else None,
        "t2_within_t1_range_dn": t2_within_range_dn,
        "t2_within_t1_range_db": t2_within_range_db,
    }
    print(f"Q2 (low-cone vs tranche-1): Δn within range? {t2_within_range_dn}, Δ|B| within range? {t2_within_range_db}")

# Q3: Does Route B cross-check against original Dn/EB where both are computable?
# For encounters with both Dn_recomputed and delta_n_near, check consistency
q3_entries = [e for e in computable_results if e.get("Dn_recomputed") is not None and e.get("delta_n_near") is not None]
coherence["q3_cross_check_with_original"] = {
    "question": "For encounters with both Dn and Δn_near, are the directions consistent?",
    "n_with_both": len(q3_entries),
    "entries": []
}
for e in q3_entries:
    dn_orig = e["Dn_recomputed"]
    dn_rb = e["delta_n_near"]
    # Both < 1 = density depletion; both > 1 = density enhancement; mixed
    if (dn_orig < 1.0) == (dn_rb < 1.0):
        direction = "consistent"
    else:
        direction = "divergent"
    coherence["q3_cross_check_with_original"]["entries"].append({
        "eid": e["eid"], "Dn": dn_orig, "delta_n_near": dn_rb, "direction": direction
    })
    print(f"Q3: {e['eid']} Dn={dn_orig:.3f}, Δn_near={dn_rb:.3f} → {direction}")

# Q4: What fraction of the encounter time is the spacecraft in the very-near bin?
q4_entries = [e for e in ledger if e.get("occ_very_near") is not None]
coherence["q4_very_near_residence"] = {
    "question": "What fraction of encounter time is spent in very-near bin?",
    "entries": [{
        "eid": e["eid"],
        "occ_very_near": e.get("occ_very_near"),
        "occ_near": e.get("occ_near"),
    } for e in q4_entries]
}

# ---------------------------------------------------------------------------
# Save outputs
# ---------------------------------------------------------------------------
os.makedirs('reports/themis_conditioning', exist_ok=True)

# Ledger JSON
with open('reports/themis_conditioning/route3b_ledger.json', 'w') as f:
    json.dump({
        "generated": datetime.datetime.now().isoformat(),
        "route_b_semantics": {
            "delta_n_near": "median(density in s=[0.0,0.2]) / median(density in s=[0.2,0.4])",
            "delta_b_near": "median(|B| in s=[0.0,0.2]) / median(|B| in s=[0.2,0.4])",
            "note": "NOT interchangeable with frozen Phase 4B Dn/EB",
            "bins": {"very_near": [0.0, 0.2], "near": [0.2, 0.4]},
            "computability_criterion": "very_near_occ > 1% AND near_occ >= 1%",
        },
        "summary": {
            "total_encounters": n_total,
            "route_b_computable": n_rb_computable,
            "route_b_descriptors_computed": n_computed,
            "tranche1_computable": n_tranche1_rb,
            "tranche2_recovered": n_tranche2_rb,
        },
        "coherence": coherence,
        "ledger": ledger,
    }, f, indent=2, default=str)

# Ledger CSV
csv_fields = [
    'eid', 'probe', 'date', 'cone_deg', 'tranche', 'dp_nPa', 'bz_nT', 'ma',
    'route_b_computable', 'route_b_descriptor_computed',
    'occ_very_near', 'occ_near', 'occ_background',
    'n_median_very_near', 'n_median_near', 'n_median_bg',
    'b_median_very_near', 'b_median_near', 'b_median_bg',
    'delta_n_near', 'delta_b_near',
    'Dn_recomputed', 'EB_recomputed',
    'transition_cleanliness_qc', 'disturbance_qc',
    'omni_context_quality_note', 'boundary_uncertainty_note',
]
with open('reports/themis_conditioning/route3b_ledger.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=csv_fields, extrasaction='ignore')
    w.writeheader()
    for entry in ledger:
        w.writerow(entry)

print(f"\nOutputs saved:")
print(f"  reports/themis_conditioning/route3b_ledger.json")
print(f"  reports/themis_conditioning/route3b_ledger.csv")
print("\nRoute 3B bounded execution complete.")
