# Phase 3B — P1/P3 Retention Audit (Report)

**Decision vocabulary:** confirmed-cautious or downgraded only.

---

## Dispositions

| Pass | Dn | EB | Disposition | Key caveat |
|---|---|---|---|---|
| P1 (aug18_6h) | 0.12 | 2.49 | **confirmed-cautious** | Near-bin density CV=0.93; Dn driven by noisy median; 14% NaN |
| P3 (sep13_09_6h) | 0.39 | 1.96 | **confirmed-cautious** | EB spike-dependent (Δ=0.50); mapping sensitivity ±0.23 at Dp=3.1 |

---

## Review summary

| Dimension | P1 | P3 |
|---|---|---|
| Mapping sensitivity (±1 nPa) | ±0.16 s shift | ±0.23 s shift (largest in bank) |
| Near-bin spike contamination | 0 spikes in near bin | 10 spikes in ~380 near points |
| Near-bin density CV | 0.93 (extreme) | 0.47 (moderate) |
| Membership | 86% (291 NaN) | 100% |
| Mixing risk | Low | Low |
| Dn spike-removal robustness | 0.12 → 0.17 | 0.39 → 0.41 |
| EB spike-removal robustness | 2.49 → 2.29 | 1.96 → 1.46 (Δ=0.50) |

---

## What remains supportable

The six-pass bank (4 clean core + 2 confirmed-cautious) remains defensible as a descriptive comparator bank. Clean core spans Dn 0.94–2.31. Low-Dn evidence (Dn < 0.5) is cautious-only and must always be reported as such.

## What is not supportable

Confounder-tested evidence for Dn < 0.5. Both low-Dn passes carry unresolvable caveats under the frozen measurement model.

---

Full audit: `docs/PHASE_3B_P1P3_RETENTION_AUDIT.md`
