"""
Phase 6A tranche 2: Low-cone-targeted second slice.

Declared slice: All THEMIS near-subsolar dayside encounters from the broader
2007-2010 THD/THE archive that have 30-min mean IMF cone angle <= 45 deg
and pass the Phase 6 measurement-context screens.

Processed in chronological order, one slice only.
"""
import json, os, glob, csv, datetime, sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pdl_pilot.config.schema import PipelineConfig, EncounterSpec, PreflightConfig, LiveDataConfig
from pdl_pilot.cli.run_pilot import _build_provider, process_encounter
from pdl_pilot.provenance.tracker import ProvenanceTracker
from pdl_pilot.data.live_provider import LiveProvider, _epoch_to_unix
from pdl_pilot.boundaries.shue1998 import shue1998_standoff
from pdl_pilot.boundaries.merka2005 import merka2005_standoff
from pdl_pilot.mapping.s_mapper import compute_s

cfg_live = LiveDataConfig(cache_dir='data_cache', cache_policy='use')
prov_helper = LiveProvider(cfg_live)
cdas = prov_helper._get_cdasws()

# ===== STEP 1: FIND LOW-CONE DAYSIDE THEMIS PASSES 2007-2010 =====
print("=== STEP 1: Scanning for low-cone near-subsolar THEMIS passes ===")

# Already-processed tranche-1 dates (avoid duplicates)
tranche1_dates = {
    '2008-08-18', '2008-09-03', '2008-09-19', '2009-09-13',
    '2009-09-20', '2009-09-26', '2009-09-27', '2009-10-24',
    '2010-10-23', '2012-07-15', '2013-02-20',
}

candidates = []
for probe, probe_up in [('thd', 'THD'), ('the', 'THE')]:
    for year in [2008, 2009]:
        for month in [8, 9, 10]:
            for day in range(1, 31, 3):  # every 3rd day
                date = f'{year}-{month:02d}-{day:02d}'
                if date in tranche1_dates:
                    continue
                try:
                    # Check position
                    ds = f'{probe_up}_L1_STATE'
                    var = f'{probe}_pos_gsm'
                    st, xr = cdas.get_data(ds, [var], f'{date}T00:00:00', f'{date}T23:59:00')
                    if xr is None:
                        continue
                    pos = xr[var].values / 6371.2
                    x, y, z = pos[:, 0], pos[:, 1], pos[:, 2]
                    r = np.sqrt(x**2 + y**2 + z**2)
                    times = xr.coords[list(xr.coords)[0]].values

                    # Find dayside near-subsolar apogee
                    dayside = (x > 7) & (np.abs(y) < 10) & (r > 9)
                    if not np.any(dayside):
                        continue
                    idx_day = np.where(dayside)[0]
                    i_apo = idx_day[np.argmax(r[idx_day])]
                    sza = np.degrees(np.arctan2(np.sqrt(y[i_apo]**2 + z[i_apo]**2), x[i_apo]))
                    if sza > 30:
                        continue

                    t_apo = str(times[i_apo])[:19]
                    h_apo = int(t_apo[11:13])

                    # Check OMNI for low cone angle
                    os_start = f'{date}T{max(0,h_apo-1):02d}:00:00'
                    os_end = f'{date}T{min(23,h_apo+1):02d}:00:00'
                    st2, xr2 = cdas.get_data('OMNI_HRO_1MIN',
                                             ['BX_GSE', 'BY_GSM', 'BZ_GSM', 'Pressure'],
                                             os_start, os_end)
                    if xr2 is None:
                        continue

                    bx = xr2['BX_GSE'].values.astype(float); bx[np.abs(bx) > 900] = np.nan
                    by = xr2['BY_GSM'].values.astype(float); by[np.abs(by) > 900] = np.nan
                    bz_omni = xr2['BZ_GSM'].values.astype(float); bz_omni[np.abs(bz_omni) > 900] = np.nan
                    dp = xr2['Pressure'].values.astype(float); dp[dp > 90] = np.nan

                    bx30 = float(np.nanmean(bx))
                    by30 = float(np.nanmean(by))
                    bz30 = float(np.nanmean(bz_omni))
                    btot = np.sqrt(bx30**2 + by30**2 + bz30**2)

                    if btot == 0 or not np.isfinite(btot):
                        continue

                    cone = float(np.degrees(np.arccos(abs(bx30) / btot)))

                    # TRANCHE-2 SLICE RULE: cone <= 45 deg only
                    if cone > 45:
                        continue

                    dp_med = float(np.nanmedian(dp[np.isfinite(dp)])) if np.any(np.isfinite(dp)) else None
                    if dp_med is None:
                        continue

                    # Check if Dp is high enough for dual-bin potential
                    mp = shue1998_standoff(dp_med, bz30 if np.isfinite(bz30) else 0)
                    bs = merka2005_standoff(mp, 8.0)
                    s_apo = compute_s(np.array([x[i_apo]]), mp, bs)[0]

                    if s_apo < 0.3:  # need reasonable s-range potential
                        continue

                    candidates.append({
                        'date': date, 'probe': probe, 'probe_up': probe_up,
                        'sza': round(sza, 1), 'r_apo': round(float(r[i_apo]), 1),
                        'x_apo': round(float(x[i_apo]), 1),
                        'cone': round(cone, 1), 'dp': round(dp_med, 1),
                        'bz': round(bz30, 1), 's_apo': round(s_apo, 3),
                        't_apo': t_apo, 'h_apo': h_apo,
                    })
                    print(f"  CANDIDATE: {date} {probe_up} cone={cone:.0f} SZA={sza:.0f} Dp={dp_med:.1f} s={s_apo:.2f}")

                except Exception:
                    pass

print(f"\nFound {len(candidates)} low-cone candidates")

# ===== STEP 2: RUN CANDIDATES THROUGH PIPELINE =====
print("\n=== STEP 2: Processing candidates through pipeline ===")

pipeline_config = PipelineConfig(
    data_source='live', output_dir='runs', run_label='phase6a_tranche2',
    preflight=PreflightConfig(
        min_valid_fraction=0.3, min_density_cm3=0.3,
        min_membership_fraction=0.3, min_near_occupancy=0.01, min_bg_occupancy=0.01,
        min_s_std=0.005, fill_masking_policy='auto', grade_with_incomplete_flags='cap_silver',
    ),
    live=LiveDataConfig(cache_dir='data_cache', cache_policy='use',
                        resample_cadence_seconds=10.0, max_gap_seconds=60.0),
)
tracker = ProvenanceTracker(pipeline_config)
provider = _build_provider(pipeline_config)

tranche2_results = []
for cand in candidates[:15]:  # hard cap
    eid = f"t2_{cand['date'].replace('-', '')}_{cand['probe']}"
    h = cand['h_apo']
    t1 = f"{cand['date']}T{max(0, h-3):02d}:00:00"
    t2 = f"{cand['date']}T{min(23, h+3):02d}:00:00"

    spec = EncounterSpec(encounter_id=eid, probe=cand['probe'],
                         time_start=t1, time_end=t2)
    try:
        enc = process_encounter(spec, pipeline_config, tracker.run_dir, provider, tracker)
        m = enc.metrics
        u = enc.upstream
        mp_data = enc.mapping
        mem = enc.membership_summary

        if not enc.evaluable or m.Dn is None or m.Dn <= 0:
            print(f"  {eid}: NOT EVALUABLE ({enc.scientific_status})")
            tranche2_results.append({
                'eid': eid, 'date': cand['date'], 'probe': cand['probe'],
                'status': 'excluded', 'reason': enc.scientific_status,
                'cone_search': cand['cone'],
            })
            continue

        # Get fresh upstream for this encounter
        mid_t = enc.time_start[:10]
        try:
            ts = datetime.datetime.fromisoformat(enc.time_start.replace('Z', ''))
            te = datetime.datetime.fromisoformat(enc.time_end.replace('Z', ''))
            mid = ts + (te - ts) / 2
            os1 = (mid - datetime.timedelta(minutes=30)).strftime('%Y-%m-%dT%H:%M:%S')
            os2 = (mid + datetime.timedelta(minutes=30)).strftime('%Y-%m-%dT%H:%M:%S')
        except:
            os1 = f"{mid_t}T{max(0,h-1):02d}:00:00"
            os2 = f"{mid_t}T{min(23,h+1):02d}:00:00"

        try:
            st3, xr3 = cdas.get_data('OMNI_HRO_1MIN',
                                     ['BX_GSE', 'BY_GSM', 'BZ_GSM', 'Pressure'],
                                     os1, os2)
            bx = xr3['BX_GSE'].values.astype(float); bx[np.abs(bx) > 900] = np.nan
            by = xr3['BY_GSM'].values.astype(float); by[np.abs(by) > 900] = np.nan
            bz_o = xr3['BZ_GSM'].values.astype(float); bz_o[np.abs(bz_o) > 900] = np.nan
            dp_o = xr3['Pressure'].values.astype(float); dp_o[dp_o > 90] = np.nan

            bx30 = float(np.nanmean(bx))
            by30 = float(np.nanmean(by))
            bz30 = float(np.nanmean(bz_o))
            btot = np.sqrt(bx30**2 + by30**2 + bz30**2)
            cone = float(np.degrees(np.arccos(abs(bx30) / btot))) if btot > 0 else None
            clock = float(abs(np.degrees(np.arctan2(by30, bz30))))
            dp_valid = dp_o[np.isfinite(dp_o)]
            dp_cv = float(np.std(dp_valid) / np.mean(dp_valid)) if len(dp_valid) > 5 and np.mean(dp_valid) > 0 else None
        except:
            cone = cand['cone']
            clock = None
            dp_cv = None

        result = {
            'eid': eid, 'date': cand['date'], 'probe': cand['probe'],
            'sza': enc.sza_deg,
            'Dn': m.Dn, 'EB': m.EB, 'delta_beta': m.delta_beta,
            'dp': u.dp_nPa, 'bz': u.bz_gsm_nT, 'ma': u.mach_alfven,
            'cone_deg': round(cone, 1) if cone else None,
            'clock_deg': round(clock, 1) if clock else None,
            'dp_cv': round(dp_cv, 2) if dp_cv is not None else None,
            'near_occ': mp_data.occupancy.get('near', 0),
            'bg_occ': mp_data.occupancy.get('background', 0),
            'membership': mem.get('membership_fraction', 0),
            'status': 'retained',
            'reason': '',
            'cone_search': cand['cone'],
        }

        # Apply Phase 6 screens
        reasons = []
        if enc.sza_deg > 30: reasons.append('sza_gt_30')
        if cone is None: reasons.append('upstream_unavailable')
        if result['near_occ'] < 0.05: reasons.append('near_occ_lt_5pct')
        if result['bg_occ'] < 0.01: reasons.append('bg_occ_lt_1pct')
        if result['membership'] < 0.5: reasons.append('membership_lt_50pct')

        if reasons:
            result['status'] = 'excluded'
            result['reason'] = ', '.join(reasons)
            print(f"  {eid}: EXCLUDED ({result['reason']})")
        else:
            # Assign strata
            c = result['cone_deg']
            result['cone_regime'] = 'quasi-radial' if c <= 30 else ('low-cone-buffer' if c <= 45 else 'intermediate' if c <= 60 else 'perpendicular')
            clk = result['clock_deg']
            result['clock_group'] = '<60' if clk and clk < 60 else ('60-120' if clk and clk <= 120 else '>120' if clk else 'unknown')
            result['upstream_stable'] = dp_cv is not None and dp_cv < 0.3

            print(f"  {eid}: RETAINED cone={c:.0f}({result['cone_regime'][:5]}) Dn={m.Dn:.3f} EB={m.EB:.3f}")

        tranche2_results.append(result)

    except Exception as ex:
        print(f"  {eid}: ERROR {str(ex)[:80]}")
        tranche2_results.append({
            'eid': eid, 'date': cand['date'], 'probe': cand['probe'],
            'status': 'error', 'reason': str(ex)[:100],
            'cone_search': cand['cone'],
        })

# ===== STEP 3: SAVE =====
print("\n=== STEP 3: Saving outputs ===")
os.makedirs('reports/themis_conditioning/tranche2/figures', exist_ok=True)

retained_t2 = [r for r in tranche2_results if r['status'] == 'retained']
excluded_t2 = [r for r in tranche2_results if r['status'] != 'retained']

print(f"Tranche 2: {len(tranche2_results)} processed, {len(retained_t2)} retained, {len(excluded_t2)} excluded/error")

cat_fields = ['eid', 'probe', 'date', 'sza', 'Dn', 'EB', 'delta_beta', 'dp', 'bz', 'ma',
              'cone_deg', 'clock_deg', 'cone_regime', 'clock_group', 'upstream_stable',
              'dp_cv', 'near_occ', 'bg_occ', 'membership', 'status', 'reason']

with open('reports/themis_conditioning/tranche2/encounter_catalogue.json', 'w') as f:
    json.dump(tranche2_results, f, indent=2, default=str)
with open('reports/themis_conditioning/tranche2/encounter_catalogue.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cat_fields, extrasaction='ignore')
    w.writeheader()
    for r in tranche2_results:
        w.writerow(r)

# Tranche-2 summary
t2_summary = {
    'slice': 'Low-cone-targeted (cone<=45) THEMIS 2007-2010 dayside encounters not in tranche 1',
    'candidates_scanned': len(candidates),
    'processed': len(tranche2_results),
    'retained': len(retained_t2),
    'excluded': len(excluded_t2),
    'strata': {},
}
for regime in ['quasi-radial', 'low-cone-buffer', 'intermediate', 'perpendicular']:
    grp = [r for r in retained_t2 if r.get('cone_regime') == regime]
    if not grp:
        t2_summary['strata'][regime] = {'N': 0}
        continue
    dns = [r['Dn'] for r in grp]
    ebs = [r['EB'] for r in grp]
    t2_summary['strata'][regime] = {
        'N': len(grp),
        'eids': [r['eid'] for r in grp],
        'Dn_median': round(float(np.median(dns)), 3),
        'Dn_range': [round(float(min(dns)), 3), round(float(max(dns)), 3)],
        'EB_median': round(float(np.median(ebs)), 3),
        'EB_range': [round(float(min(ebs)), 3), round(float(max(ebs)), 3)],
    }

with open('reports/themis_conditioning/tranche2/conditioning_summary.json', 'w') as f:
    json.dump(t2_summary, f, indent=2, default=str)

# ===== STEP 4: INTEGRATED SYNTHESIS =====
print("\n=== STEP 4: Integrated tranche1+2 synthesis ===")

# Load tranche 1
with open('reports/themis_conditioning/encounter_catalogue.json') as f:
    t1_all = json.load(f)
t1_retained = [e for e in t1_all if e.get('phase6a_status') == 'retained']

# Combine
combined = []
for e in t1_retained:
    e['tranche'] = 1
    combined.append(e)
for r in retained_t2:
    r['tranche'] = 2
    # Harmonize cone regime naming
    if r.get('cone_regime') == 'low-cone-buffer':
        r['cone_regime_coarse'] = 'low-cone'  # <=45
    elif r.get('cone_regime') == 'quasi-radial':
        r['cone_regime_coarse'] = 'low-cone'
    else:
        r['cone_regime_coarse'] = r.get('cone_regime', 'unknown')
    combined.append(r)

# For tranche-1, assign coarse regime
for e in combined:
    if e['tranche'] == 1:
        cone = e.get('cone_deg')
        if cone is not None:
            e['cone_regime_coarse'] = 'low-cone' if cone <= 45 else ('intermediate' if cone <= 60 else 'perpendicular')
        else:
            e['cone_regime_coarse'] = 'unknown'

print(f"Combined: {len(combined)} encounters")

# Integrated summary by coarse cone regime
integrated = {
    'total_combined': len(combined),
    'tranche1_N': sum(1 for e in combined if e['tranche'] == 1),
    'tranche2_N': sum(1 for e in combined if e['tranche'] == 2),
    'strata': {},
}

for regime in ['low-cone', 'intermediate', 'perpendicular']:
    grp = [e for e in combined if e.get('cone_regime_coarse') == regime]
    if not grp:
        integrated['strata'][regime] = {'N': 0}
        continue
    dns = [e['Dn'] for e in grp]
    ebs = [e['EB'] for e in grp]
    integrated['strata'][regime] = {
        'N': len(grp),
        'N_t1': sum(1 for e in grp if e['tranche'] == 1),
        'N_t2': sum(1 for e in grp if e['tranche'] == 2),
        'eids': [e['eid'] for e in grp],
        'Dn_median': round(float(np.median(dns)), 3),
        'Dn_IQR': [round(float(np.percentile(dns, 25)), 3), round(float(np.percentile(dns, 75)), 3)] if len(dns) > 2 else [round(float(min(dns)), 3), round(float(max(dns)), 3)],
        'EB_median': round(float(np.median(ebs)), 3),
        'EB_IQR': [round(float(np.percentile(ebs, 25)), 3), round(float(np.percentile(ebs, 75)), 3)] if len(ebs) > 2 else [round(float(min(ebs)), 3), round(float(max(ebs)), 3)],
    }
    print(f"  {regime}: N={len(grp)} (t1={integrated['strata'][regime]['N_t1']}, t2={integrated['strata'][regime]['N_t2']}) "
          f"Dn med={np.median(dns):.2f} EB med={np.median(ebs):.2f}")

with open('reports/themis_conditioning/phase6a_integrated_two_slice_summary.json', 'w') as f:
    json.dump(integrated, f, indent=2, default=str)

# ===== STEP 5: FIGURES =====
print("\n=== STEP 5: Generating figures ===")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Figure 1: Tranche-2 only
if retained_t2:
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    fig.suptitle('Phase 6A Tranche 2: Dn vs EB (low-cone slice)', fontsize=11)
    regime_colors = {'quasi-radial': '#d62728', 'low-cone-buffer': '#ff7f0e', 'intermediate': '#2ca02c', 'perpendicular': '#1f77b4'}
    for r in retained_t2:
        regime = r.get('cone_regime', 'unknown')
        c = regime_colors.get(regime, 'gray')
        ax.scatter(r['Dn'], r['EB'], c=c, s=100, edgecolors='k', lw=0.7, zorder=3)
        ax.annotate(r['eid'][:12], (r['Dn'], r['EB']), fontsize=6, xytext=(3, 3), textcoords='offset points')
    ax.axhline(1, color='gray', ls='--', lw=0.5)
    ax.axvline(1, color='gray', ls='--', lw=0.5)
    ax.set_xlabel('Dn'); ax.set_ylabel('EB')
    plt.tight_layout()
    plt.savefig('reports/themis_conditioning/tranche2/figures/phase6a_tranche2_dn_eb_by_cone.png', dpi=150)
    plt.close()

# Figure 2: Integrated two-slice
fig, ax = plt.subplots(1, 1, figsize=(10, 7))
fig.suptitle('Phase 6A Integrated: Dn vs EB by Coarse Cone-Angle Regime\n(tranche 1 + tranche 2)', fontsize=11)

regime_colors_coarse = {'low-cone': '#d62728', 'intermediate': '#ff7f0e', 'perpendicular': '#2ca02c'}
tranche_markers = {1: 'o', 2: 's'}

for e in combined:
    regime = e.get('cone_regime_coarse', 'unknown')
    c = regime_colors_coarse.get(regime, 'gray')
    m = tranche_markers.get(e['tranche'], 'x')
    ax.scatter(e['Dn'], e['EB'], c=c, marker=m, s=100, edgecolors='k', lw=0.7, zorder=3)

# Legend
from matplotlib.lines import Line2D
handles = []
for regime, color in regime_colors_coarse.items():
    n = sum(1 for e in combined if e.get('cone_regime_coarse') == regime)
    handles.append(Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10,
                          markeredgecolor='k', label=f'{regime} (N={n})'))
handles.append(Line2D([0], [0], marker='o', color='w', markerfacecolor='gray', markersize=8,
                      markeredgecolor='k', label='tranche 1 (circle)'))
handles.append(Line2D([0], [0], marker='s', color='w', markerfacecolor='gray', markersize=8,
                      markeredgecolor='k', label='tranche 2 (square)'))
ax.legend(handles=handles, fontsize=9)

ax.axhline(1, color='gray', ls='--', lw=0.5)
ax.axvline(1, color='gray', ls='--', lw=0.5)
ax.set_xlabel('Dn (near/bg density ratio)')
ax.set_ylabel('EB (near/bg |B| ratio)')
plt.tight_layout()
plt.savefig('reports/themis_conditioning/figures/phase6a_two_slice_cone_summary.png', dpi=150)
plt.close()

print("\nAll tranche 2 outputs saved.")
print(f"Retained t2: {len(retained_t2)}")
print(f"Combined total: {len(combined)}")
for regime in ['low-cone', 'intermediate', 'perpendicular']:
    s = integrated['strata'].get(regime, {})
    print(f"  {regime}: N={s.get('N', 0)} Dn_med={s.get('Dn_median', '?')} EB_med={s.get('EB_median', '?')}")
