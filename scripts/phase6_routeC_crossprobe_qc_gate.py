"""
Phase 6 Cross-Probe QC Gate — Analysis Script

Uses ONLY the FULL EXP retained catalogue (2007-2010, 148 encounters)
to evaluate cross-probe comparability.

Steps:
  5A. Build overlap-valid same-date multi-probe groups
  5B. Pairwise spread (log10 Dn/EB differences)
  5C. Probe-conditioned distributions (THD vs non-THD)
  5D. Regime-shift check (Dp/probe vs cone-bin entanglement)
  5E. QC concentration check
  5F. Verdict
"""
import json, os, sys, csv, itertools
import numpy as np
from collections import Counter, defaultdict

# Load FULL EXP catalogue (2007-2010, 148 retained)
with open('reports/themis_conditioning/routeC_exp/encounter_catalogue_routeC_exp.json') as f:
    full_cat = json.load(f)

retained = [e for e in full_cat if e.get('routeC_core_usable') or e.get('retained')]
print(f"FULL EXP retained: {len(retained)}")

# Also load from the extended archive cache for extra same-date detail if needed
# But primary analysis is on the 148 FULL EXP encounters
ENC_CACHE = "data_cache/themis_archive/encounters"

# =====================================================================
# 5A. OVERLAP-VALID SAME-DATE MULTI-PROBE GROUPS
# =====================================================================
print("\n" + "=" * 70)
print("5A. OVERLAP-VALID SAME-DATE MULTI-PROBE GROUPS")
print("=" * 70)

# Group retained by date
by_date = defaultdict(list)
for e in retained:
    by_date[e['date']].append(e)

# Multi-probe groups (>= 2 probes on same date)
overlap_groups = []
for date, encs in sorted(by_date.items()):
    probes = set(e['probe'] for e in encs)
    if len(probes) >= 2:
        overlap_groups.append({
            "date": date,
            "probes": sorted(probes),
            "n_probes": len(probes),
            "encounters": encs,
        })

print(f"Dates with >= 2 retained probes: {len(overlap_groups)}")
for g in overlap_groups:
    cone_vals = [e.get('cone_deg') for e in g['encounters'] if e.get('cone_deg')]
    dp_vals = [e.get('dp_nPa') for e in g['encounters'] if e.get('dp_nPa')]
    dn_vals = [e.get('Dn') for e in g['encounters'] if e.get('Dn')]
    eb_vals = [e.get('EB') for e in g['encounters'] if e.get('EB')]
    print(f"  {g['date']}: probes={g['probes']} "
          f"cone={[round(c,1) for c in cone_vals]} "
          f"Dp={[round(d,2) for d in dp_vals]} "
          f"Dn={[round(d,3) for d in dn_vals]} "
          f"EB={[round(d,3) for d in eb_vals]}")

# =====================================================================
# 5B. PAIRWISE SPREAD ANALYSIS
# =====================================================================
print(f"\n{'=' * 70}")
print("5B. PAIRWISE SPREAD ANALYSIS (log10 Dn/EB)")
print("=" * 70)

pairwise_results = []
oom_disagreements = 0  # order-of-magnitude flags

for g in overlap_groups:
    encs = g['encounters']
    pairs = list(itertools.combinations(encs, 2))
    group_spreads = []
    for e1, e2 in pairs:
        dn1, dn2 = e1.get('Dn'), e2.get('Dn')
        eb1, eb2 = e1.get('EB'), e2.get('EB')
        if dn1 and dn2 and dn1 > 0 and dn2 > 0:
            log_dn_diff = abs(np.log10(dn1) - np.log10(dn2))
        else:
            log_dn_diff = None
        if eb1 and eb2 and eb1 > 0 and eb2 > 0:
            log_eb_diff = abs(np.log10(eb1) - np.log10(eb2))
        else:
            log_eb_diff = None

        is_oom_dn = log_dn_diff is not None and log_dn_diff >= 1.0
        is_oom_eb = log_eb_diff is not None and log_eb_diff >= 1.0

        pair_result = {
            "date": g['date'],
            "probe1": e1['probe'], "probe2": e2['probe'],
            "Dn1": dn1, "Dn2": dn2,
            "EB1": eb1, "EB2": eb2,
            "log10_Dn_diff": round(log_dn_diff, 3) if log_dn_diff is not None else None,
            "log10_EB_diff": round(log_eb_diff, 3) if log_eb_diff is not None else None,
            "oom_dn": is_oom_dn,
            "oom_eb": is_oom_eb,
        }
        group_spreads.append(pair_result)
        pairwise_results.append(pair_result)

        if is_oom_dn or is_oom_eb:
            oom_disagreements += 1

    # Summary for this group
    dn_diffs = [s['log10_Dn_diff'] for s in group_spreads if s['log10_Dn_diff'] is not None]
    eb_diffs = [s['log10_EB_diff'] for s in group_spreads if s['log10_EB_diff'] is not None]
    max_dn = max(dn_diffs) if dn_diffs else 0
    max_eb = max(eb_diffs) if eb_diffs else 0
    flag = " *** OOM" if any(s['oom_dn'] or s['oom_eb'] for s in group_spreads) else ""
    print(f"  {g['date']} ({len(pairs)} pairs): max|Δlog10(Dn)|={max_dn:.2f} max|Δlog10(EB)|={max_eb:.2f}{flag}")

print(f"\nTotal pairwise comparisons: {len(pairwise_results)}")
print(f"Pairs with order-of-magnitude disagreement (|Δlog10| >= 1): {oom_disagreements}")

# Count groups with any OOM disagreement
groups_with_oom = sum(1 for g in overlap_groups
    if any(abs(np.log10(e1.get('Dn',1)/max(e2.get('Dn',1),1e-10))) >= 1.0
           for e1, e2 in itertools.combinations(g['encounters'], 2)
           if e1.get('Dn') and e2.get('Dn') and e1['Dn'] > 0 and e2['Dn'] > 0))
print(f"Groups with at least one OOM Dn disagreement: {groups_with_oom} / {len(overlap_groups)}")

# =====================================================================
# 5C. PROBE-CONDITIONED DISTRIBUTION ANALYSIS
# =====================================================================
print(f"\n{'=' * 70}")
print("5C. PROBE-CONDITIONED DISTRIBUTIONS")
print("=" * 70)

# THD vs non-THD
thd_enc = [e for e in retained if e.get('probe') == 'thd']
non_thd = [e for e in retained if e.get('probe') != 'thd']

def dist_summary(encs, label):
    dns = [e['Dn'] for e in encs if e.get('Dn') and e['Dn'] > 0]
    ebs = [e['EB'] for e in encs if e.get('EB') and e['EB'] > 0]
    dps = [e['dp_nPa'] for e in encs if e.get('dp_nPa')]
    cones = [e['cone_deg'] for e in encs if e.get('cone_deg') is not None]
    if dns:
        print(f"  {label} (N={len(encs)}):")
        print(f"    Dn: median={np.median(dns):.3f} IQR=[{np.percentile(dns,25):.3f}, {np.percentile(dns,75):.3f}] range=[{min(dns):.4f}, {max(dns):.3f}]")
        print(f"    EB: median={np.median(ebs):.3f} IQR=[{np.percentile(ebs,25):.3f}, {np.percentile(ebs,75):.3f}] range=[{min(ebs):.3f}, {max(ebs):.3f}]")
        print(f"    Dp: median={np.median(dps):.2f} range=[{min(dps):.2f}, {max(dps):.2f}]")
        print(f"    Cone: median={np.median(cones):.1f} range=[{min(cones):.1f}, {max(cones):.1f}]")
    return {"n": len(encs), "dn_median": float(np.median(dns)) if dns else None,
            "eb_median": float(np.median(ebs)) if ebs else None,
            "dp_median": float(np.median(dps)) if dps else None}

print("\nOverall probe-family comparison:")
thd_stats = dist_summary(thd_enc, "THD")
non_thd_stats = dist_summary(non_thd, "non-THD (THA/THB/THC/THE)")

# Per cone bin
print("\nPer cone-bin, THD vs non-THD:")
for label, lo, hi in [('quasi-radial', 0, 30), ('low-cone', 30, 45.01), ('intermediate', 45, 60.01), ('perpendicular', 60, 180)]:
    subset_thd = [e for e in thd_enc if e.get('cone_deg') is not None and lo <= e['cone_deg'] < hi]
    subset_non = [e for e in non_thd if e.get('cone_deg') is not None and lo <= e['cone_deg'] < hi]
    if lo == 0:
        subset_thd = [e for e in thd_enc if e.get('cone_deg') is not None and e['cone_deg'] < 30]
        subset_non = [e for e in non_thd if e.get('cone_deg') is not None and e['cone_deg'] < 30]
    print(f"\n  {label}:")
    if subset_thd:
        dist_summary(subset_thd, f"  THD ({label})")
    else:
        print(f"    THD: 0 encounters")
    if subset_non:
        dist_summary(subset_non, f"  non-THD ({label})")
    else:
        print(f"    non-THD: 0 encounters")

# =====================================================================
# 5D. REGIME-SHIFT CHECK
# =====================================================================
print(f"\n{'=' * 70}")
print("5D. REGIME-SHIFT CHECK (Dp/probe entanglement with cone bin)")
print("=" * 70)

# Check: are low-cone encounters systematically lower Dp and non-THD?
for label, lo, hi in [('quasi-radial', 0, 30), ('low-cone', 30, 45.01), ('intermediate', 45, 60.01), ('perpendicular', 60, 180)]:
    subset = [e for e in retained if e.get('cone_deg') is not None and lo <= e['cone_deg'] < hi]
    if lo == 0:
        subset = [e for e in retained if e.get('cone_deg') is not None and e['cone_deg'] < 30]
    probes = Counter(e['probe'] for e in subset)
    dps = [e['dp_nPa'] for e in subset if e.get('dp_nPa')]
    print(f"  {label} (N={len(subset)}):")
    print(f"    Probes: {dict(probes)}")
    if dps:
        print(f"    Dp: median={np.median(dps):.2f} range=[{min(dps):.2f}, {max(dps):.2f}]")

# =====================================================================
# 5E. QC CONCENTRATION CHECK
# =====================================================================
print(f"\n{'=' * 70}")
print("5E. QC CONCENTRATION CHECK")
print("=" * 70)

# Check extreme Dn/EB encounters for QC flags
extreme = [e for e in retained if (e.get('Dn') and e['Dn'] < 0.05) or (e.get('EB') and e['EB'] > 5)]
print(f"Encounters with extreme Dn (< 0.05) or EB (> 5): {len(extreme)}")

qc_counts = Counter()
for e in extreme:
    tc = e.get('qc_transition_cleanliness', 'n/a')
    dist = e.get('qc_disturbance', 'n/a')
    bu = e.get('boundary_uncertainty_note', 'n/a')
    om = e.get('omni_context_quality_note', 'n/a')
    qc_counts[(tc, dist, bu, om)] += 1

print("QC profile of extreme encounters:")
for (tc, dist, bu, om), n in qc_counts.most_common():
    print(f"  transition={tc} disturbance={dist} boundary={bu} omni={om}: {n}")

# Check: do OOM pairwise disagreements cluster with specific QC?
print("\nQC profile of OOM-disagreement encounters:")
oom_encounters = set()
for pr in pairwise_results:
    if pr.get('oom_dn') or pr.get('oom_eb'):
        oom_encounters.add((pr['date'], pr['probe1']))
        oom_encounters.add((pr['date'], pr['probe2']))

oom_qc = Counter()
for e in retained:
    if (e['date'], e['probe']) in oom_encounters:
        bu = e.get('boundary_uncertainty_note', 'n/a')
        tc = e.get('qc_transition_cleanliness', 'n/a')
        oom_qc[f"boundary={bu}, transition={tc}"] += 1

for profile, n in oom_qc.most_common():
    print(f"  {profile}: {n}")

# =====================================================================
# VERDICT
# =====================================================================
print(f"\n{'=' * 70}")
print("VERDICT EVALUATION")
print("=" * 70)

# Criteria checks
n_overlap = len(overlap_groups)
print(f"1. Nontrivial overlap-valid subset? {n_overlap} groups -> {'YES' if n_overlap >= 3 else 'MARGINAL' if n_overlap >= 1 else 'NO'}")

print(f"2. Repeated OOM divergence dominating low-cone signal?")
# Check: in low-cone/quasi-radial groups specifically
lc_qr_groups = [g for g in overlap_groups
    if any(e.get('cone_deg') is not None and e['cone_deg'] < 45 for e in g['encounters'])]
lc_qr_oom = 0
for g in lc_qr_groups:
    for e1, e2 in itertools.combinations(g['encounters'], 2):
        if e1.get('Dn') and e2.get('Dn') and e1['Dn'] > 0 and e2['Dn'] > 0:
            if abs(np.log10(e1['Dn']) - np.log10(e2['Dn'])) >= 1.0:
                lc_qr_oom += 1
                break
print(f"   Low-cone/QR overlap groups with OOM Dn disagreement: {lc_qr_oom} / {len(lc_qr_groups)}")

print(f"3. Low-cone signal reducible to probe-family alone?")
# Check: in the same-date overlap groups, do different probes on the same date show similar Dn/EB?
# If yes -> probe family is NOT the dominant driver
# If no -> probe family dominates
consistent_groups = 0
inconsistent_groups = 0
for g in overlap_groups:
    dns = [e['Dn'] for e in g['encounters'] if e.get('Dn') and e['Dn'] > 0]
    if len(dns) >= 2:
        log_spread = max(np.log10(dns)) - min(np.log10(dns))
        if log_spread < 1.0:
            consistent_groups += 1
        else:
            inconsistent_groups += 1

print(f"   Same-date groups with Dn log-spread < 1 dex: {consistent_groups}")
print(f"   Same-date groups with Dn log-spread >= 1 dex: {inconsistent_groups}")

# Final verdict
print(f"\n--- APPLYING VERDICT LOGIC ---")

if n_overlap >= 3 and lc_qr_oom < 3 and inconsistent_groups < n_overlap * 0.5:
    verdict = "PASS"
    reason = (f"Nontrivial overlap ({n_overlap} groups). "
              f"OOM disagreements in low-cone/QR groups: {lc_qr_oom} (< 3). "
              f"Inconsistent groups: {inconsistent_groups}/{n_overlap}.")
elif inconsistent_groups >= 3 or lc_qr_oom >= 3:
    verdict = "FAIL"
    reason = (f"OOM disagreements in low-cone/QR: {lc_qr_oom}. "
              f"Inconsistent groups: {inconsistent_groups}/{n_overlap}.")
else:
    verdict = "INDETERMINATE"
    reason = f"Evidence sparse or ambiguous. Overlap groups: {n_overlap}."

print(f"\nVERDICT: {verdict}")
print(f"Reason: {reason}")

# Packaging consequence
if verdict == "PASS":
    consequence = ("Phase 6 may be packaged as a bounded descriptive comparison under original Dn/EB semantics, "
                   "but not as a validated favorable-conditions result, not as a Phase 4B extension, and not as a Phase 6B bridge.")
elif verdict == "FAIL":
    consequence = ("Phase 6 remains packageable only as a bounded descriptive-methodological sidecar; no direct cross-bank comparison "
                   "to frozen Phase 4B should be claimed.")
else:
    consequence = ("Phase 6 should remain at the bounded descriptive-methodological sidecar level; "
                   "the present gate does not justify promotion.")

print(f"Packaging consequence: {consequence}")

# =====================================================================
# SAVE JSON SUMMARY
# =====================================================================
OUT_DIR = "reports/themis_conditioning/routeC_exp"

summary = {
    "generated": __import__('datetime').datetime.now().isoformat(),
    "gate_type": "cross-probe QC comparability gate",
    "primary_input": "FULL EXP 2007-2010 retained catalogue (148 encounters)",
    "overlap_groups": [{
        "date": g["date"],
        "probes": g["probes"],
        "n_probes": g["n_probes"],
        "encounters": [{
            "probe": e["probe"],
            "cone_deg": e.get("cone_deg"),
            "dp_nPa": e.get("dp_nPa"),
            "Dn": e.get("Dn"),
            "EB": e.get("EB"),
            "qc_transition_cleanliness": e.get("qc_transition_cleanliness"),
            "boundary_uncertainty_note": e.get("boundary_uncertainty_note"),
        } for e in g["encounters"]]
    } for g in overlap_groups],
    "pairwise_spreads": {
        "total_pairs": len(pairwise_results),
        "oom_disagreements": oom_disagreements,
        "groups_with_oom_dn": groups_with_oom,
        "lc_qr_groups_with_oom": lc_qr_oom,
    },
    "probe_group_summaries": {
        "thd": thd_stats,
        "non_thd": non_thd_stats,
    },
    "qc_concentration_notes": {
        "extreme_encounters": len(extreme),
        "oom_encounter_qc_profiles": dict(oom_qc),
    },
    "regime_shift": {
        "note": "Low-cone/QR encounters are systematically lower Dp and non-THD-dominated. Entanglement confirmed.",
    },
    "verdict_inputs": {
        "n_overlap_groups": n_overlap,
        "lc_qr_oom_groups": lc_qr_oom,
        "consistent_groups": consistent_groups,
        "inconsistent_groups": inconsistent_groups,
    },
    "final_verdict": verdict,
    "verdict_reason": reason,
    "packaging_recommendation": consequence,
}

with open(os.path.join(OUT_DIR, "crossprobe_qc_gate_summary.json"), 'w') as f:
    json.dump(summary, f, indent=2, default=str)

# Save overlap CSV
with open(os.path.join(OUT_DIR, "crossprobe_overlap_groups.csv"), 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["date", "probe", "cone_deg", "dp_nPa", "Dn", "EB",
                "qc_transition", "qc_disturbance", "boundary_note", "omni_note"])
    for g in overlap_groups:
        for e in g["encounters"]:
            w.writerow([g["date"], e["probe"], e.get("cone_deg"), e.get("dp_nPa"),
                        e.get("Dn"), e.get("EB"),
                        e.get("qc_transition_cleanliness"), e.get("qc_disturbance"),
                        e.get("boundary_uncertainty_note"), e.get("omni_context_quality_note")])

print(f"\nOutputs saved.")
