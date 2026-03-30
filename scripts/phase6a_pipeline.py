"""Phase 6A pipeline: encounter universe, screening, stratification, descriptor summaries."""
import json, os, glob, csv, datetime
import numpy as np

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from pdl_pilot.data.live_provider import LiveProvider, _epoch_to_unix
from pdl_pilot.config.schema import LiveDataConfig

cfg = LiveDataConfig(cache_dir='data_cache', cache_policy='use')
prov = LiveProvider(cfg)
cdas = prov._get_cdasws()

# ===== STEP 1: BUILD ENCOUNTER UNIVERSE =====
seen = {}
for f in sorted(glob.glob('runs/*/encounter_*.json')):
    try:
        with open(f) as fh:
            enc = json.load(fh)
        eid = enc.get('encounter_id', os.path.basename(f))
        m = enc.get('metrics', {})
        u = enc.get('upstream', {})
        mp = enc.get('mapping', {})
        mem = enc.get('membership_summary', {})
        if not enc.get('evaluable'):
            continue
        if m.get('Dn') is None or m['Dn'] <= 0:
            continue
        date = enc.get('time_start', '')[:10]
        probe = enc.get('probe', '?')
        key = date + '_' + probe
        entry = {
            'eid': eid, 'probe': probe, 'date': date,
            'time_start': enc.get('time_start', ''),
            'time_end': enc.get('time_end', ''),
            'sza': enc.get('sza_deg'),
            'Dn': m.get('Dn'), 'EB': m.get('EB'),
            'delta_beta': m.get('delta_beta'),
            'dp': u.get('dp_nPa'), 'bz': u.get('bz_gsm_nT'),
            'ma': u.get('mach_alfven'),
            'near_occ': mp.get('occupancy', {}).get('near', 0),
            'bg_occ': mp.get('occupancy', {}).get('background', 0),
            'membership': mem.get('membership_fraction', 0),
            'source_file': f,
        }
        if key not in seen:
            seen[key] = entry
        elif 'usable_' in eid and 'usable_' not in seen[key]['eid']:
            seen[key] = entry
    except Exception:
        pass

universe = sorted(seen.values(), key=lambda x: x['date'])
print(f'UNIVERSE: {len(universe)} unique encounters')

# ===== STEP 2: UPSTREAM CONTEXT =====
for enc in universe:
    try:
        t1 = datetime.datetime.fromisoformat(enc['time_start'].replace('Z', ''))
        t2 = datetime.datetime.fromisoformat(enc['time_end'].replace('Z', ''))
        mid = t1 + (t2 - t1) / 2
        os_start = (mid - datetime.timedelta(minutes=30)).strftime('%Y-%m-%dT%H:%M:%S')
        os_end = (mid + datetime.timedelta(minutes=30)).strftime('%Y-%m-%dT%H:%M:%S')
    except Exception:
        os_start = enc['date'] + 'T19:00:00'
        os_end = enc['date'] + 'T21:00:00'

    try:
        st, xr = cdas.get_data('OMNI_HRO_1MIN',
                               ['BX_GSE', 'BY_GSM', 'BZ_GSM', 'Pressure'],
                               os_start, os_end)
        if xr is None:
            enc['cone_deg'] = None
            enc['clock_deg'] = None
            enc['dp_cv'] = None
            continue
        bx = xr['BX_GSE'].values.astype(float); bx[np.abs(bx) > 900] = np.nan
        by = xr['BY_GSM'].values.astype(float); by[np.abs(by) > 900] = np.nan
        bz = xr['BZ_GSM'].values.astype(float); bz[np.abs(bz) > 900] = np.nan
        dp = xr['Pressure'].values.astype(float); dp[dp > 90] = np.nan

        bx30 = float(np.nanmean(bx))
        by30 = float(np.nanmean(by))
        bz30 = float(np.nanmean(bz))
        btot = np.sqrt(bx30**2 + by30**2 + bz30**2)
        cone = float(np.degrees(np.arccos(abs(bx30) / btot))) if btot > 0 else None
        clock = float(abs(np.degrees(np.arctan2(by30, bz30))))
        dp_valid = dp[np.isfinite(dp)]
        dp_cv = float(np.std(dp_valid) / np.mean(dp_valid)) if len(dp_valid) > 5 and np.mean(dp_valid) > 0 else None

        enc['cone_deg'] = round(cone, 1) if cone else None
        enc['clock_deg'] = round(clock, 1)
        enc['dp_cv'] = round(dp_cv, 2) if dp_cv is not None else None
    except Exception:
        enc['cone_deg'] = None
        enc['clock_deg'] = None
        enc['dp_cv'] = None

# ===== STEP 3: INCLUSION SCREENS =====
exclusions = []
retained = []
for enc in universe:
    reasons = []
    if enc['sza'] is None or enc['sza'] > 30:
        reasons.append('sza_gt_30')
    if enc.get('cone_deg') is None:
        reasons.append('upstream_unavailable')
    if enc['near_occ'] < 0.05:
        reasons.append('near_occ_lt_5pct')
    if enc['bg_occ'] < 0.01:
        reasons.append('bg_occ_lt_1pct')
    if enc['membership'] < 0.5:
        reasons.append('membership_lt_50pct')
    if reasons:
        exclusions.append({'eid': enc['eid'], 'reasons': reasons})
        enc['phase6a_status'] = 'excluded'
    else:
        retained.append(enc)
        enc['phase6a_status'] = 'retained'

print(f'Retained: {len(retained)}  Excluded: {len(exclusions)}')
for ex in exclusions:
    print(f"  EXCL: {ex['eid'][:35]:35s} -> {', '.join(ex['reasons'])}")

# ===== STEP 4: STRATA =====
for enc in retained:
    cone = enc['cone_deg']
    enc['cone_regime'] = 'quasi-radial' if cone <= 30 else ('intermediate' if cone <= 60 else 'perpendicular')
    clock = enc['clock_deg']
    enc['clock_group'] = '<60' if clock < 60 else ('60-120' if clock <= 120 else '>120')
    enc['upstream_stable'] = enc.get('dp_cv') is not None and enc['dp_cv'] < 0.3

print('\nRETAINED CATALOGUE:')
for e in retained:
    print(f"  {e['eid'][:35]:35s} {e['probe']:3s} {e['date']} cone={e['cone_deg']:5.1f}({e['cone_regime'][:6]:6s}) "
          f"clock={e['clock_deg']:5.1f}({e['clock_group']:>5}) "
          f"stable={'Y' if e['upstream_stable'] else 'N'} Dn={e['Dn']:.3f} EB={e['EB']:.3f}")

# ===== STEP 5: DESCRIPTOR SUMMARIES =====
print('\nBY CONE REGIME:')
for regime in ['quasi-radial', 'intermediate', 'perpendicular']:
    grp = [e for e in retained if e['cone_regime'] == regime]
    if not grp:
        print(f'  {regime}: N=0')
        continue
    dns = [e['Dn'] for e in grp]
    ebs = [e['EB'] for e in grp]
    print(f"  {regime}: N={len(grp)} Dn med={np.median(dns):.2f} "
          f"[{np.percentile(dns,25):.2f},{np.percentile(dns,75):.2f}] "
          f"EB med={np.median(ebs):.2f} [{np.percentile(ebs,25):.2f},{np.percentile(ebs,75):.2f}]")

print('\nBY CLOCK GROUP:')
for cg in ['<60', '60-120', '>120']:
    grp = [e for e in retained if e['clock_group'] == cg]
    if not grp:
        print(f'  {cg}: N=0')
        continue
    dns = [e['Dn'] for e in grp]
    ebs = [e['EB'] for e in grp]
    print(f"  {cg}: N={len(grp)} Dn med={np.median(dns):.2f} "
          f"[{np.percentile(dns,25):.2f},{np.percentile(dns,75):.2f}] "
          f"EB med={np.median(ebs):.2f} [{np.percentile(ebs,25):.2f},{np.percentile(ebs,75):.2f}]")

# ===== STEP 6: SAVE =====
os.makedirs('reports/themis_conditioning/figures', exist_ok=True)

cat_fields = ['eid', 'probe', 'date', 'sza', 'Dn', 'EB', 'delta_beta', 'dp', 'bz', 'ma',
              'cone_deg', 'clock_deg', 'cone_regime', 'clock_group', 'upstream_stable',
              'dp_cv', 'near_occ', 'bg_occ', 'membership', 'phase6a_status']

with open('reports/themis_conditioning/encounter_catalogue.json', 'w') as f:
    json.dump([{k: e.get(k) for k in cat_fields} for e in universe], f, indent=2, default=str)

with open('reports/themis_conditioning/encounter_catalogue.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cat_fields)
    w.writeheader()
    for e in universe:
        w.writerow({k: e.get(k) for k in cat_fields})

summary = {
    'slice': 'all locally cached evaluable THEMIS encounters',
    'universe': len(universe),
    'retained': len(retained),
    'excluded': len(exclusions),
    'exclusion_details': exclusions,
    'strata': {},
}
for regime in ['quasi-radial', 'intermediate', 'perpendicular']:
    grp = [e for e in retained if e['cone_regime'] == regime]
    if not grp:
        summary['strata'][regime] = {'N': 0}
        continue
    dns = [e['Dn'] for e in grp]
    ebs = [e['EB'] for e in grp]
    summary['strata'][regime] = {
        'N': len(grp),
        'eids': [e['eid'] for e in grp],
        'Dn_median': round(float(np.median(dns)), 3),
        'Dn_IQR': [round(float(np.percentile(dns, 25)), 3), round(float(np.percentile(dns, 75)), 3)],
        'EB_median': round(float(np.median(ebs)), 3),
        'EB_IQR': [round(float(np.percentile(ebs, 25)), 3), round(float(np.percentile(ebs, 75)), 3)],
    }
with open('reports/themis_conditioning/conditioning_summary.json', 'w') as f:
    json.dump(summary, f, indent=2, default=str)

# ===== STEP 7: FIGURE =====
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1, figsize=(9, 7))
fig.suptitle('Phase 6A: Dn vs EB by IMF Cone-Angle Regime\n(controlled near-subsolar THEMIS encounters)', fontsize=11)

regime_colors = {'quasi-radial': '#d62728', 'intermediate': '#ff7f0e', 'perpendicular': '#2ca02c'}
regime_markers = {'quasi-radial': 's', 'intermediate': 'D', 'perpendicular': 'o'}

for regime in ['quasi-radial', 'intermediate', 'perpendicular']:
    grp = [e for e in retained if e['cone_regime'] == regime]
    if not grp:
        continue
    dns = [e['Dn'] for e in grp]
    ebs = [e['EB'] for e in grp]
    ax.scatter(dns, ebs, c=regime_colors[regime], marker=regime_markers[regime],
               s=100, edgecolors='k', lw=0.7, zorder=3,
               label=f"{regime} (N={len(grp)})")

ax.axhline(1, color='gray', ls='--', lw=0.5, alpha=0.5)
ax.axvline(1, color='gray', ls='--', lw=0.5, alpha=0.5)
ax.set_xlabel('Dn (near/bg density ratio)')
ax.set_ylabel('EB (near/bg |B| ratio)')
ax.legend(fontsize=9)
ax.set_xlim(-0.1, 3.2)
ax.set_ylim(0.5, 4.5)
plt.tight_layout()
plt.savefig('reports/themis_conditioning/figures/phase6a_dn_eb_by_cone.png', dpi=150)
plt.close()

print('\nAll outputs saved.')
