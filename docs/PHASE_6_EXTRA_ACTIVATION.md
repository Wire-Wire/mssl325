# Phase 6 EXTRA — Activation

**Date:** 2026-03-31
**Authority:** User-authorized scope expansion from 2007-2010 to 2007-2025.
**Run name:** Phase 6 EXTRA

---

## 1. Why this run exists

The Phase 6 FULL EXP (2007-2010) produced 148 retained encounters with only 4 quasi-radial and 16 low-cone. The cross-probe QC gate PASS was based on 4 LC/QR overlap groups — a thin evidence base. Meanwhile, the full local cache (2007-2025, built in the same session) contains 757 retained encounters with 28 quasi-radial and 89 low-cone, including an independent second orbital cycle (2016-2019) that provides cross-cycle verification.

This EXTRA run uses the already-cached 2007-2025 data to rerun the same analysis and QC gate on the full dataset.

---

## 2. Relationship to prior layers

| Layer | Status |
|---|---|
| Phase 6 FULL EXP (2007-2010, 148 retained) | Frozen historical. Not overwritten. |
| Phase 6 FULL EXP QC gate (PASS) | Frozen historical. Superseded by EXTRA gate. |
| Phase 6 EXTRA (2007-2025, 757 retained) | **This run.** Additive layer. |
| Phase 4B / 5A / 5B / MMS | Frozen. Unchanged. |
| Route B | Frozen sidecar. Not used. |
| Phase 6B | Blocked. |

---

## 3. Scope

- **Archive:** 2007-2025, all 5 THEMIS probes, all months
- **Geometry:** X_GSM > 5 Re, SZA < 30 deg, 8 < r < 25 Re
- **Data source:** Local cache only (`data_cache/themis_archive/encounters/`). No new CDAWeb fetch.
- **Semantics:** Original Dn/EB only. No Route B descriptors.
