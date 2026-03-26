# Wording-Drift Audit — Phase 2B

**Date:** 2026-03-26
**Scope:** All current docs, configs, and review artifacts.

---

## Audit method

Inspected all docs and config comments for language that promotes comparator windows beyond their operational role, implies physical class membership, or suggests threshold readiness.

---

## Findings

### docs/METRIC_BEHAVIOR_REVIEW.md

**Previously tightened (no further issues):**
- §3 no longer references "depletion layer" or "compressed-sheath conditions"
- §4 now explicitly notes ρ is non-discriminative
- Risk note is present and adequate
- "Supports" section uses "operationally distinguishable outputs," not "physical states"

### docs/MINI_SEED_STRATIFICATION.md

**Previously tightened (no further issues):**
- Seed rationales now use "Lowest observed Dn" not "strongest depletion"
- Is/is-not section is adequate

### docs/SEED_DOSSIER.md

**No issues found.** Prohibitions section is explicit. Per-seed caveats are adequate.

### docs/COMPARATOR_ATLAS.md

**No issues found.** Naming discipline statement is clear.

### docs/LLM_HANDOFF.md

**No issues found.** Risk section references METRIC_BEHAVIOR_REVIEW for details.

### configs/pilot_live_usable.yaml

**Two minor wording items found and flagged (not changed — config comments only):**

1. Line ~99: `"Layer-like pattern."` in usable_aug18_6h notes
   - **Risk:** "Layer-like" implies a physical interpretation
   - **Recommendation:** Change to "Low Dn / high EB observed"
   - **Status:** Flagged. These are YAML comments, not scientific claims.

2. Line ~110: `"Compressed-sheath pattern."` in usable_sep03_6h notes
   - **Risk:** "Compressed-sheath" implies a physical class
   - **Recommendation:** Change to "High Dn / low EB observed"
   - **Status:** Flagged.

### configs/pilot_window_families.yaml

**One wording item found:**

1. Line ~100: `"layer-like pattern under the measurement model, but NOT labeled"`
   - **Risk:** Even with the caveat, "layer-like pattern" implies interpretation
   - **Status:** Flagged. The caveat is present but the phrase remains suggestive.

### runs/20260326T040343Z_d0425fd4/seed_stratification.json

**One wording item:**
- Seed A rationale: "represents strongest near-MP depletion + enhancement pattern observed"
- **Risk:** "depletion + enhancement" implies physical identification
- **Status:** Flagged. The JSON is a run artifact; the SEED_DOSSIER.md already uses tighter language.

### docs/PHASE_1_5_STATE.md (older state doc)

**Contains outdated wording:**
- Line ~61: "Sep 3: Dn > 1 → compressed-sheath / Aug 18: Dn < 1 → layer-like pattern"
- **Status:** This file reflects an earlier phase state. It is not the current canonical doc (PHASE_2A_STATE.md is). Flagged but not changed — older state docs preserve history.

---

## Summary

| Source | Items flagged | Changed? | Reason |
|---|---|---|---|
| METRIC_BEHAVIOR_REVIEW.md | 0 (already tightened) | — | — |
| MINI_SEED_STRATIFICATION.md | 0 (already tightened) | — | — |
| SEED_DOSSIER.md | 0 | — | — |
| COMPARATOR_ATLAS.md | 0 | — | — |
| LLM_HANDOFF.md | 0 | — | — |
| pilot_live_usable.yaml | 2 | No | Config comments; flagged for awareness |
| pilot_window_families.yaml | 1 | No | Config comment with caveat present |
| seed_stratification.json | 1 | No | Run artifact; canonical doc is tighter |
| PHASE_1_5_STATE.md | 1 | No | Historical state doc; superseded |

**Overall assessment:** Current canonical documentation maintains conservative wording. Minor legacy phrasings exist in config comments and run artifacts but are offset by caveats and superseded by tighter canonical docs. No urgent rewrites needed.
