# Phase 6 — Master Summary

> **Purpose:** One-stop reference for the entire Phase 6 branch. Read this file to understand what happened, what was found, where everything is, and what the final conclusion is. Intended for LLM handoff, thesis writing, and audit.

> **Status:** Phase 6 science closed. All sub-branches complete and frozen.

---

## 1. What Phase 6 was about

Phase 6 asked: **within the THEMIS near-subsolar dayside archive, how do continuous near-magnetopause descriptors (Dn, EB) distribute across IMF cone-angle regimes?** Specifically, can the quasi-radial (cone < 30 deg) and low-cone (30-45 deg) bins — empty in the frozen Phase 4B THD bank — be populated under the original measurement model?

---

## 2. Timeline and stages

| Stage | Date | What happened | Key outcome |
|---|---|---|---|
| **6A Tranche 1** | 2026-03-30 | Pilot encounter catalogue from local runs | 11 encounters (2 synthetic, 9 real). QR bin empty. |
| **6A Tranche 2** | 2026-03-30 | Low-cone targeted search (THD+THE, Aug-Oct 2008-09) | 3 candidates, all failed BG occupancy. Zero retained. |
| **6A Audit** | 2026-03-30 | Discovered synthetic contamination + scope mismatch | N=11 corrected to N=9 real. Declared>searched gap documented. |
| **Route A** | 2026-03-30 | Mandatory provenance repair | Synthetic removed. Clean N=9 catalogue. Scope-match discipline. |
| **Route B regression** | 2026-03-30 | Test inner-sheath descriptor (Dn_near, D\|B\|_near) | 5/12 computable. 1 low-cone recovered (no depletion). Marginal. |
| **Route B execution** | 2026-03-30 | Bounded execution on 5 encounters | 3/5 show inner-sheath gradient. Modest yield. Frozen as sidecar. |
| **Decision-space repair** | 2026-03-31 | Expanded menu to 4 options (B cont / C / D / writing-safe) | User chose Route C. |
| **Route C local-only** | 2026-03-31 | Search locally cached data in unsearched 2007-2010 slice | 3 candidates, 2 incomplete. **HARD NULL.** |
| **Route C FULL EXP** | 2026-03-31 | Full CDAWeb scan, 2007-2010, all 5 probes, Jul-Nov | **148 retained. 4 QR, 16 LC. SUCCESS.** |
| **Archive cache build** | 2026-03-31 | Expanded to 2007-2025, all probes, all months | 1135 STATE files, 757 retained, 28 QR, 89 LC. |
| **Phase 6 freeze** | 2026-03-31 | Packaged as bounded descriptive-methodological sidecar | Writing-safe. Does not strengthen Phase 4B. |
| **QC gate (2007-2010)** | 2026-03-31 | Cross-probe comparability test on FULL EXP 148 | **PASS** (1/4 LC/QR OOM groups, 77% consistent). |
| **EXTRA (2007-2025)** | 2026-03-31 | Full analysis + QC gate on 757 retained | **FAIL** (9/41 LC/QR OOM, but 78% consistent — rate same as PASS). |

---

## 3. Final numbers

### Encounter counts

| Dataset | Retained | QR (<30) | LC (30-45) | IM (45-60) | PP (>60) |
|---|---|---|---|---|---|
| Phase 4B frozen bank | 6 passes | 0 | 0 | 2 | 4 |
| Route A clean catalogue | 9 | 0 | 1 | 3 | 5 |
| FULL EXP (2007-2010) | 148 | 4 | 16 | 44 | 84 |
| **EXTRA (2007-2025)** | **757** | **28** | **89** | **199** | **441** |

### Dn/EB per cone bin (EXTRA, N=757)

| Cone bin | N | Dn median | Dn IQR | EB median | EB IQR | Dp median |
|---|---|---|---|---|---|---|
| quasi-radial | 28 | 0.891 | [0.061, 1.348] | 2.423 | [2.005, 3.155] | 1.65 |
| low-cone | 89 | 0.795 | [0.068, 1.173] | 2.545 | [1.564, 3.840] | 1.53 |
| intermediate | 199 | 0.785 | [0.121, 1.135] | 2.377 | [1.496, 4.093] | 2.25 |
| perpendicular | 441 | 0.735 | [0.143, 1.235] | 2.391 | [1.552, 4.149] | 2.44 |

### QC gate comparison

| Metric | FULL EXP (PASS) | EXTRA (FAIL) |
|---|---|---|
| Overlap groups | 26 | 208 |
| Group consistency (< 1 dex) | 77% | 78% |
| LC/QR OOM rate | 25% (1/4) | 22% (9/41) |
| Verdict | PASS | FAIL |
| Reason for difference | Small sample, absolute threshold | Same rate, larger absolute count |

---

## 4. Final conclusions

**4a. The quasi-radial and low-cone bins are fillable.** The full 2007-2025 THEMIS archive yields 28 quasi-radial and 89 low-cone encounters evaluable under original Dn/EB semantics. The earlier empty-bin finding was an artifact of searching only THD+THE in Aug-Oct 2008-2009.

**4b. Cross-probe comparability is partial.** Same-day multi-probe groups agree within 1 dex in 78% of cases. About 22% of low-cone/QR overlap groups show order-of-magnitude Dn disagreement. This rate is similar across both the 148 and 757 encounter datasets.

**4c. Dp and probe are entangled with cone bin.** Low-cone encounters systematically come from lower-Dp conditions and non-THD probes. This is a structural access effect, not a measurement error, but it complicates direct comparison with the Phase 4B THD bank (Dp > 3 nPa).

**4d. Phase 4B is unchanged and remains the claim-bearing anchor.** Phase 6 does not strengthen, extend, or validate Phase 4B claims.

**4e. Route B is a frozen sidecar.** Dn_near / D|B|_near descriptors (very-near/near ratio) showed modest inner-sheath gradients in 3/5 encounters. Not interchangeable with Dn/EB. Not incorporated into the main Phase 6 package.

**4f. The QC gate verdict depends on threshold design.** The FULL EXP (2007-2010) PASS and the EXTRA (2007-2025) FAIL reflect the same underlying consistency rate (~78%) hitting different absolute-count thresholds. This is a judgment call, not a data contradiction.

**4g. The broader upstream-conditioning question remains open.** Whether near-MP descriptor behavior shifts systematically across cone-angle regimes is not answered here. Phase 6 establishes that the required encounter population exists. Answering the conditioning question requires cross-probe validation, Dp-controlled sub-stratification, and potentially inter-probe calibration comparison.

---

## 5. File index

### Docs (20 files)

| File | Stage | Role |
|---|---|---|
| `PHASE_6A_THEMIS_UPSTREAM_CONDITIONING.md` | 6A T1 | Tranche 1 pilot (audited, contains synthetics) |
| `PHASE_6A_TRANCHE2_LOWCONE_SLICE.md` | 6A T2 | Low-cone pilot (zero retained) |
| `PHASE_6A_AUDIT_AND_RESET_NOTE.md` | 6A audit | Synthetic contamination + scope mismatch discovery |
| `PHASE_6_RESET_OPTIONS.md` | Reset | Route A/B/C/D decision space |
| `PHASE_6_ROUTE3_ACTIVATION.md` | Route A+B | Route A repair + Route B regression activation |
| `PHASE_6_ROUTE3_B_COMPATIBLE_MEASUREMENT_MODEL.md` | Route B | Inner-sheath descriptor design + regression test |
| `PHASE_6_ROUTEB_BOUNDED_EXECUTION.md` | Route B | Bounded execution results (5 encounters, 3/5 gradient) |
| `PHASE_6_POST_ROUTEB_DECISION_MEMO.md` | Decision | Four-option post-Route-B menu |
| `PHASE_6_ROUTEC_EXECUTION_PLAN.md` | Route C | Local-only Route C plan |
| `PHASE_6_ROUTEC_RESULT.md` | Route C | Local-only result (HARD NULL) |
| `PHASE_6_FULL_EXP_ACTIVATION.md` | FULL EXP | EXP activation (overrides prior closure) |
| `PHASE_6_ROUTEC_FULL_EXP_PLAN.md` | FULL EXP | Full-archive plan (2007-2010) |
| `PHASE_6_ROUTEC_FULL_EXP_RESULT.md` | FULL EXP | Full-archive result (148 retained, SUCCESS) |
| `PHASE_6_FULL_EXP_FREEZE.md` | Freeze | Package note with thesis placement |
| `PHASE_6_CROSSPROBE_QC_GATE_PLAN.md` | QC gate | Cross-probe gate plan (2007-2010) |
| `PHASE_6_CROSSPROBE_QC_GATE_REPORT.md` | QC gate | Cross-probe gate report (PASS) |
| `PHASE_6_EXTRA_ACTIVATION.md` | EXTRA | 2007-2025 scope expansion activation |
| `PHASE_6_EXTRA_PLAN.md` | EXTRA | 2007-2025 plan |
| `PHASE_6_EXTRA_RESULT.md` | EXTRA | 2007-2025 result (757 retained, SUCCESS hard stop) |
| `PHASE_6_EXTRA_QC_GATE_REPORT.md` | EXTRA | 2007-2025 QC gate (FAIL, same rate as PASS) |

### Reports

| Directory | Contents |
|---|---|
| `reports/themis_conditioning/` | Clean catalogue (N=9), selection flows, scope manifest, Route B ledger |
| `reports/themis_conditioning/tranche2/` | Tranche 2 catalogue (3 excluded candidates) |
| `reports/themis_conditioning/routeC/` | Local-only Route C (HARD NULL) |
| `reports/themis_conditioning/routeC_exp/` | FULL EXP 2007-2010 (148 retained) + QC gate |
| `reports/themis_conditioning/routeC_extra/` | EXTRA 2007-2025 (757 retained) + QC gate |

### Data cache

| Directory | Contents |
|---|---|
| `data_cache/themis_archive/raw_state/` | 1135 monthly STATE NPZ files (all probes 2007-2025) |
| `data_cache/themis_archive/encounters/` | 6118 per-encounter JSONs |
| `data_cache/themis_archive/summary.json` | Global stats |
| `data_cache/themis_archive/retained_index.json` | 757 retained, grouped by cone bin |
| `data_cache/themis_archive/encounter_index.json` | All 6903 encounters |
| `data_cache/themis_archive/encounter_catalogue.csv` | Full CSV |

See `docs/THEMIS_ARCHIVE_DATA_GUIDE.md` for detailed usage instructions.

### Scripts

| Script | Purpose |
|---|---|
| `scripts/phase6a_pipeline.py` | Tranche 1 encounter universe builder |
| `scripts/phase6a_tranche2.py` | Tranche 2 low-cone search |
| `scripts/phase6_route3_part1_part2.py` | Route A repair + Route B regression |
| `scripts/phase6_route3b_bounded_execution.py` | Route B bounded execution |
| `scripts/phase6_routeC_scan.py` | Route C local-only scan |
| `scripts/phase6_routeC_full_exp.py` | FULL EXP multi-threaded scan (2007-2010) |
| `scripts/phase6_routeC_crossprobe_qc_gate.py` | QC gate (2007-2010) |
| `scripts/phase6_extra_analysis.py` | EXTRA analysis + QC gate (2007-2025) |
| `scripts/build_themis_cache.py` | Archive cache builder v1 |
| `scripts/build_themis_cache_v2.py` | Archive cache builder v2 (32-thread, r<25) |

---

## 6. Relationship to other branches

| Branch | Relationship to Phase 6 |
|---|---|
| **Phase 4B** | Claim-bearing anchor. Phase 6 does NOT extend or validate it. |
| **Phase 5A/5B** | Editorial sidecars. Unaffected by Phase 6. |
| **MMS** | Frozen. Unaffected by Phase 6. |
| **Route B** | Frozen sidecar within Phase 6. Separate descriptor semantics. |
| **Phase 6B** | Never opened. Remains blocked. |

---

## 7. For thesis writing

Phase 6 goes **after** Phase 4B results, as a bounded descriptive-methodological sidecar. See:
- `docs/PHASE_6_FULL_EXP_FREEZE.md` for thesis placement guidance
- `docs/THEMIS_THESIS_WRITING_PACK.md` for the Phase 6 entry in the source hierarchy

**Recommended thesis sentence:**
"A full-archive search across all five THEMIS probes (2007-2025) demonstrated that the quasi-radial and low-cone IMF regimes are evaluable under the same Dn/EB measurement family. However, cross-probe comparability remains partially validated (78% of same-day multi-probe groups agree within one order of magnitude), and a direct physical comparison across cone-angle regimes is deferred to future work."

---

## 8. Open questions deferred to future work

1. Cross-probe calibration comparison (THD vs THA/THB/THC Dn/EB intercalibration)
2. Dp-controlled sub-stratification (remove Dp-cone entanglement)
3. Whether EB offset between probe families is calibration or physics
4. Whether the 22% cross-probe OOM rate is reducible with better boundary models
5. Full cone-angle-conditioned descriptive comparison (requires 1-4 resolved first)
