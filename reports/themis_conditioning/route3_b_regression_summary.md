# Route 3B Regression Test Summary

**Date:** 2026-03-30

## Test scope
- Clean tranche-1 real encounters: 9
- Tranche-2 low-cone candidates: 3
- Total tested: 12

## Route B auxiliary descriptor
Primary: very_near / near density and |B| ratios (does not require BG bin).
Requires: very_near [0.0, 0.2] > 1% AND near [0.2, 0.4] >= 1% occupancy.

## Results
- Route B computable: 5 / 12
- Low-cone (cone <= 45) Route B computable: 2
- Low-cone RECOVERED by Route B (not evaluable under original dual-bin): 1

## Verdict
**Route B is viable enough for bounded execution**

Route B recovers 1 low-cone encounter(s) that were previously excluded.
