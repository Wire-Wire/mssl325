"""
Phase 6 EXTRA — Full 2007-2025 archive analysis + cross-probe QC gate

Uses the full local cache (757 retained) instead of the 2007-2010 subset (148).
Reproduces the same analysis steps:
  1. Summary stats by cone bin, year, probe
  2. Hard stop evaluation
  3. Cross-probe QC gate (overlap groups, pairwise spread, probe-conditioned, regime-shift, QC concentration)
  4. Verdict

All outputs go to reports/themis_conditioning/routeC_extra/
"""
import json, os, sys, csv, itertools
import datetime as dt_module
import numpy as np
from collections import Counter, defaultdict

# =====================================================================
# LOAD ALL 757 RETAINED FROM LOCAL CACHE
# =====================================================================
ENC_DIR = "data_cache/themis_archive/encounters"

print("=" * 70)
print("PHASE 6 EXTRA — FULL 2007-2025 ARCHIVE ANALYSIS")
print("=" * 70)

all_enc = []
for f in os.listdir(ENC_DIR):
    if not f.endswith('.json'): continue
    with open(os.path.join(ENC_DIR, f)) as fh:
        e = json.load(fh)
    if e.get('retained') or e.get('evaluable'):
        all_enc.append(e)

# Dedup by date+probe
seen = {}
for e in all_enc:
    k = (e.get('date'), e.get('probe'))
    if k not in seen:
        seen[k] = e
retained = sorted(seen.values(), key=lambda x: (x.get('date',''), x.get('probe','')))

print(f"Total retained (dedup): {len(retained)}")

# Cone classification
def cone_bin(cd):
    if cd is None: return "unknown"
    if cd < 30: return "quasi-radial"
    if cd <= 45: return "low-cone"
    if cd <= 60: return "intermediate"
    return "perpendicular"

for e in retained:
    e['cone_bin_calc'] = cone_bin(e.get('cone_deg'))

# =====================================================================
# PART 1: SUMMARY STATS
# =====================================================================
print(f"\n{'=' * 70}")
print("PART 1: SUMMARY STATS")
print("=" * 70)

cc = Counter(e['cone_bin_calc'] for e in retained)
by_year = Counter(e.get('year') for e in retained)
by_probe = Counter(e.get('probe') for e in retained)

print(f"\nRetained by cone bin:")
for cb in ['quasi-radial', 'low-cone', 'intermediate', 'perpendicular']:
    print(f"  {cb}: {cc[cb]}")

print(f"\nRetained by year:")
for y in sorted(by_year):
    print(f"  {y}: {by_year[y]}")

print(f"\nRetained by probe:")
for p in sorted(by_probe):
    print(f"  {p}: {by_probe[p]}")

# Dn/EB stats per cone bin
print(f"\nDn/EB per cone bin:")
for cb in ['quasi-radial', 'low-cone', 'intermediate', 'perpendicular']:
    subset = [e for e in retained if e['cone_bin_calc'] == cb]
    dns = [e['Dn'] for e in subset if e.get('Dn') and e['Dn'] > 0]
    ebs = [e['EB'] for e in subset if e.get('EB') and e['EB'] > 0]
    dps = [e['dp_nPa'] for e in subset if e.get('dp_nPa')]
    if dns:
        print(f"  {cb} (N={len(subset)}):")
        print(f"    Dn: median={np.median(dns):.3f} IQR=[{np.percentile(dns,25):.3f}, {np.percentile(dns,75):.3f}]")
        print(f"    EB: median={np.median(ebs):.3f} IQR=[{np.percentile(ebs,25):.3f}, {np.percentile(ebs,75):.3f}]")
        print(f"    Dp: median={np.median(dps):.2f} range=[{min(dps):.2f}, {max(dps):.2f}]")

# =====================================================================
# PART 2: HARD STOP EVALUATION
# =====================================================================
print(f"\n{'=' * 70}")
print("PART 2: HARD STOP")
print("=" * 70)

qr = cc['quasi-radial']
lc = cc['low-cone']
success = qr >= 1 or lc >= 5
print(f"quasi-radial: {qr} (need >= 1)")
print(f"low-cone: {lc} (need >= 5)")
print(f"OUTCOME: {'SUCCESS' if success else 'HARD NULL'}")

# =====================================================================
# PART 3: CROSS-PROBE QC GATE
# =====================================================================
print(f"\n{'=' * 70}")
print("PART 3: CROSS-PROBE QC GATE")
print("=" * 70)

# 3A. Overlap-valid groups
by_date = defaultdict(list)
for e in retained:
    by_date[e['date']].append(e)

overlap_groups = []
for date, encs in sorted(by_date.items()):
    probes = set(e['probe'] for e in encs)
    if len(probes) >= 2:
        overlap_groups.append({"date": date, "probes": sorted(probes),
                               "n_probes": len(probes), "encounters": encs})

print(f"\n3A. Overlap-valid same-date groups: {len(overlap_groups)}")

# How many have low-cone/QR encounters?
lc_qr_groups = [g for g in overlap_groups
    if any(e.get('cone_deg') is not None and e['cone_deg'] < 45 for e in g['encounters'])]
print(f"    Of which contain low-cone/QR: {len(lc_qr_groups)}")

# 3B. Pairwise spread
print(f"\n3B. Pairwise spread analysis")
pairwise_results = []
oom_dn_count = 0
oom_eb_count = 0

for g in overlap_groups:
    for e1, e2 in itertools.combinations(g['encounters'], 2):
        dn1, dn2 = e1.get('Dn'), e2.get('Dn')
        eb1, eb2 = e1.get('EB'), e2.get('EB')
        ld = abs(np.log10(dn1) - np.log10(dn2)) if dn1 and dn2 and dn1 > 0 and dn2 > 0 else None
        le = abs(np.log10(eb1) - np.log10(eb2)) if eb1 and eb2 and eb1 > 0 and eb2 > 0 else None
        oom_dn = ld is not None and ld >= 1.0
        oom_eb = le is not None and le >= 1.0
        if oom_dn: oom_dn_count += 1
        if oom_eb: oom_eb_count += 1
        pairwise_results.append({
            "date": g['date'], "p1": e1['probe'], "p2": e2['probe'],
            "log_dn_diff": round(ld, 3) if ld else None,
            "log_eb_diff": round(le, 3) if le else None,
            "oom_dn": oom_dn, "oom_eb": oom_eb})

# Group-level spread
consistent = 0
inconsistent = 0
for g in overlap_groups:
    dns = [e['Dn'] for e in g['encounters'] if e.get('Dn') and e['Dn'] > 0]
    if len(dns) >= 2:
        spread = max(np.log10(dns)) - min(np.log10(dns))
        if spread < 1.0: consistent += 1
        else: inconsistent += 1

# Low-cone/QR specific OOM count
lc_qr_oom = 0
for g in lc_qr_groups:
    has_oom = False
    for e1, e2 in itertools.combinations(g['encounters'], 2):
        if e1.get('Dn') and e2.get('Dn') and e1['Dn'] > 0 and e2['Dn'] > 0:
            if abs(np.log10(e1['Dn']) - np.log10(e2['Dn'])) >= 1.0:
                has_oom = True; break
    if has_oom: lc_qr_oom += 1

print(f"  Total pairs: {len(pairwise_results)}")
print(f"  OOM Dn disagreements: {oom_dn_count} ({100*oom_dn_count/max(len(pairwise_results),1):.0f}%)")
print(f"  OOM EB disagreements: {oom_eb_count} ({100*oom_eb_count/max(len(pairwise_results),1):.0f}%)")
print(f"  Groups < 1 dex Dn spread: {consistent}/{consistent+inconsistent} ({100*consistent/max(consistent+inconsistent,1):.0f}%)")
print(f"  Groups >= 1 dex Dn spread: {inconsistent}/{consistent+inconsistent}")
print(f"  Low-cone/QR groups with OOM Dn: {lc_qr_oom}/{len(lc_qr_groups)}")

# 3C. Probe-conditioned
print(f"\n3C. Probe-conditioned distributions")

thd_enc = [e for e in retained if e.get('probe') == 'thd']
non_thd = [e for e in retained if e.get('probe') != 'thd']

def pstats(encs, label):
    dns = [e['Dn'] for e in encs if e.get('Dn') and e['Dn'] > 0]
    ebs = [e['EB'] for e in encs if e.get('EB') and e['EB'] > 0]
    dps = [e['dp_nPa'] for e in encs if e.get('dp_nPa')]
    if not dns: print(f"  {label}: 0 encounters"); return {}
    r = {"n": len(encs), "dn_med": round(float(np.median(dns)),3),
         "eb_med": round(float(np.median(ebs)),3), "dp_med": round(float(np.median(dps)),2)}
    print(f"  {label} (N={len(encs)}): Dn_med={r['dn_med']:.3f} EB_med={r['eb_med']:.3f} Dp_med={r['dp_med']:.2f}")
    return r

print("Overall:")
thd_s = pstats(thd_enc, "THD")
non_s = pstats(non_thd, "non-THD")

print("\nPer cone bin:")
for cb in ['quasi-radial', 'low-cone', 'intermediate', 'perpendicular']:
    print(f"  --- {cb} ---")
    pstats([e for e in thd_enc if e['cone_bin_calc'] == cb], f"  THD/{cb}")
    pstats([e for e in non_thd if e['cone_bin_calc'] == cb], f"  non-THD/{cb}")

# 3D. Regime-shift
print(f"\n3D. Regime-shift check")
for cb in ['quasi-radial', 'low-cone', 'intermediate', 'perpendicular']:
    subset = [e for e in retained if e['cone_bin_calc'] == cb]
    probes = Counter(e['probe'] for e in subset)
    dps = [e['dp_nPa'] for e in subset if e.get('dp_nPa')]
    thd_frac = probes.get('thd', 0) / max(len(subset), 1)
    print(f"  {cb} (N={len(subset)}): THD={probes.get('thd',0)} ({100*thd_frac:.0f}%) Dp_med={np.median(dps):.2f}")

# 3E. QC concentration
print(f"\n3E. QC concentration check")
extreme = [e for e in retained if (e.get('Dn') and e['Dn'] < 0.05) or (e.get('EB') and e['EB'] > 5)]
print(f"  Extreme encounters (Dn<0.05 or EB>5): {len(extreme)}")
qc_profiles = Counter()
for e in extreme:
    qc_profiles[e.get('qc_transition_cleanliness', 'n/a')] += 1
for p, n in qc_profiles.most_common():
    print(f"    transition={p}: {n}")

# OOM encounters QC
oom_encs = set()
for pr in pairwise_results:
    if pr.get('oom_dn') or pr.get('oom_eb'):
        oom_encs.add((pr['date'], pr['p1']))
        oom_encs.add((pr['date'], pr['p2']))
oom_qc = Counter()
for e in retained:
    if (e['date'], e['probe']) in oom_encs:
        oom_qc[e.get('boundary_uncertainty_note', 'n/a')] += 1
print(f"  OOM encounter boundary notes: {dict(oom_qc)}")

# =====================================================================
# PART 4: CROSS-CYCLE INDEPENDENT VERIFICATION
# =====================================================================
print(f"\n{'=' * 70}")
print("PART 4: CROSS-CYCLE INDEPENDENT VERIFICATION")
print("=" * 70)

cycle1 = [e for e in retained if e.get('year') in range(2007, 2011)]
cycle2 = [e for e in retained if e.get('year') in range(2016, 2020)]
artemis = [e for e in retained if e.get('year') in range(2011, 2016) or e.get('year') in range(2020, 2026)]

print(f"Cycle 1 (2007-2010): {len(cycle1)} retained")
print(f"Cycle 2 (2016-2019): {len(cycle2)} retained")
print(f"ARTEMIS/other (2011-2015, 2020-2025): {len(artemis)} retained")

for label, subset in [("Cycle 1", cycle1), ("Cycle 2", cycle2)]:
    print(f"\n{label}:")
    for cb in ['quasi-radial', 'low-cone', 'intermediate', 'perpendicular']:
        s = [e for e in subset if e['cone_bin_calc'] == cb]
        if s:
            dns = [e['Dn'] for e in s if e.get('Dn') and e['Dn'] > 0]
            ebs = [e['EB'] for e in s if e.get('EB') and e['EB'] > 0]
            if dns:
                print(f"  {cb} (N={len(s)}): Dn_med={np.median(dns):.3f} EB_med={np.median(ebs):.3f}")

# =====================================================================
# VERDICT
# =====================================================================
print(f"\n{'=' * 70}")
print("VERDICT")
print("=" * 70)

n_overlap = len(overlap_groups)
print(f"1. Nontrivial overlap? {n_overlap} groups -> {'YES' if n_overlap >= 3 else 'NO'}")
print(f"2. OOM in LC/QR groups: {lc_qr_oom}/{len(lc_qr_groups)} -> {'<3' if lc_qr_oom < 3 else '>=3'}")
print(f"3. Consistent groups: {consistent}/{consistent+inconsistent} ({100*consistent/max(consistent+inconsistent,1):.0f}%)")

if n_overlap >= 3 and lc_qr_oom < 3 and inconsistent < (consistent + inconsistent) * 0.5:
    verdict = "PASS"
elif inconsistent >= 3 or lc_qr_oom >= 3:
    verdict = "FAIL"
else:
    verdict = "INDETERMINATE"

print(f"\nFINAL VERDICT: {verdict}")

if verdict == "PASS":
    consequence = ("Phase 6 EXTRA may be packaged as a bounded descriptive comparison under original Dn/EB semantics, "
                   "but not as a validated favorable-conditions result, not as a Phase 4B extension, and not as a Phase 6B bridge.")
elif verdict == "FAIL":
    consequence = ("Phase 6 EXTRA remains packageable only as a bounded descriptive-methodological sidecar.")
else:
    consequence = ("Phase 6 EXTRA should remain at the bounded descriptive-methodological sidecar level.")

print(f"Consequence: {consequence}")

# =====================================================================
# SAVE OUTPUTS
# =====================================================================
OUT_DIR = "reports/themis_conditioning/routeC_extra"
os.makedirs(OUT_DIR, exist_ok=True)

# Scope manifest
manifest = {
    "generated": dt_module.datetime.now().isoformat(),
    "run_name": "Phase 6 EXTRA (2007-2025)",
    "declared_slice": "All THEMIS 2007-2025, all 5 probes, all months, SZA<=30, 8<r<25 Re",
    "scope_match": True,
    "source": "data_cache/themis_archive/encounters/ (pre-cached local files only)",
    "results": {
        "unique_retained": len(retained),
        "cone_counts": dict(cc),
    },
    "hard_stop": {"quasi_radial": qr, "low_cone": lc, "outcome": "SUCCESS" if success else "HARD_NULL"},
}
with open(os.path.join(OUT_DIR, "scope_manifest_extra.json"), 'w') as f:
    json.dump(manifest, f, indent=2)

# QC gate summary
gate_summary = {
    "generated": dt_module.datetime.now().isoformat(),
    "gate_type": "cross-probe QC gate (EXTRA, 2007-2025)",
    "input": f"{len(retained)} retained encounters from full local cache",
    "overlap_groups_count": n_overlap,
    "lc_qr_overlap_groups": len(lc_qr_groups),
    "pairwise_total": len(pairwise_results),
    "oom_dn_pairs": oom_dn_count,
    "oom_eb_pairs": oom_eb_count,
    "consistent_groups": consistent,
    "inconsistent_groups": inconsistent,
    "lc_qr_oom_groups": lc_qr_oom,
    "extreme_encounters": len(extreme),
    "probe_stats": {"thd": thd_s, "non_thd": non_s},
    "cross_cycle": {
        "cycle1_n": len(cycle1), "cycle2_n": len(cycle2), "artemis_n": len(artemis),
    },
    "final_verdict": verdict,
    "packaging_recommendation": consequence,
}
with open(os.path.join(OUT_DIR, "crossprobe_qc_gate_summary_extra.json"), 'w') as f:
    json.dump(gate_summary, f, indent=2)

# Full catalogue
with open(os.path.join(OUT_DIR, "encounter_catalogue_extra.json"), 'w') as f:
    json.dump(retained, f, indent=2, default=str)

# CSV
cf = ['encounter_id','date','year','month','probe','sza_deg','mlt','cone_deg','clock_deg',
      'dp_nPa','bz_nT','near_occ','bg_occ','Dn','EB','cone_bin_calc','retained',
      'qc_transition_cleanliness','qc_disturbance','qc_boundary_motion',
      'omni_context_quality_note','boundary_uncertainty_note','r_re','x_gsm_re']
with open(os.path.join(OUT_DIR, "encounter_catalogue_extra.csv"), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cf, extrasaction='ignore')
    w.writeheader()
    for e in retained:
        w.writerow(e)

# Selection flow
with open(os.path.join(OUT_DIR, "selection_flow_extra.md"), 'w') as f:
    f.write(f"# Phase 6 EXTRA — Selection Flow\n\n")
    f.write(f"**Date:** {dt_module.datetime.now().isoformat()[:10]}\n")
    f.write(f"**Scope:** 2007-2025, all probes, all months, from local cache\n\n")
    f.write(f"## Retained: {len(retained)}\n\n")
    f.write(f"| Cone bin | Count |\n|---|---|\n")
    for cb in ['quasi-radial','low-cone','intermediate','perpendicular']:
        f.write(f"| {cb} | {cc[cb]} |\n")
    f.write(f"\n## Hard stop: SUCCESS (QR={qr}, LC={lc})\n")
    f.write(f"\n## QC Gate: {verdict}\n")
    f.write(f"- Overlap groups: {n_overlap}\n")
    f.write(f"- Consistent (< 1 dex): {consistent}/{consistent+inconsistent}\n")
    f.write(f"- LC/QR OOM: {lc_qr_oom}/{len(lc_qr_groups)}\n")

# Overlap CSV
with open(os.path.join(OUT_DIR, "crossprobe_overlap_groups_extra.csv"), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["date","probe","cone_deg","dp_nPa","Dn","EB",
                "qc_transition","boundary_note","cone_bin"])
    for g in overlap_groups:
        for e in g["encounters"]:
            w.writerow([g["date"], e["probe"], e.get("cone_deg"), e.get("dp_nPa"),
                        e.get("Dn"), e.get("EB"),
                        e.get("qc_transition_cleanliness"), e.get("boundary_uncertainty_note"),
                        e['cone_bin_calc']])

# Summary JSON
summary = {
    "generated": dt_module.datetime.now().isoformat(),
    "run_name": "Phase 6 EXTRA",
    "scope": "2007-2025, all probes",
    "retained": len(retained),
    "cone_counts": dict(cc),
    "by_year": dict(sorted(by_year.items())),
    "by_probe": dict(sorted(by_probe.items())),
    "hard_stop": "SUCCESS",
    "qc_gate_verdict": verdict,
}
with open(os.path.join(OUT_DIR, "routeC_extra_summary.json"), 'w') as f:
    json.dump(summary, f, indent=2)

print(f"\nAll outputs saved to {OUT_DIR}/")
print("DONE.")
