> **OPERATIONAL LOG ONLY.** Not a source of current project stage. For live state, read `docs/NEXT_QUESTION.md`.

# Decision Log

Chronological record of bounded project decisions.

---

| Date | Decision | Rationale | Rejected alternatives | Source docs |
|---|---|---|---|---|
| 2026-03-25 | Phase 1.5: dual-source bridge built | Blueprint required live data capability | PySPEDAS (too heavy); notebook-only (prohibited) | `RP/internal_master_research_blueprint_PDL_SMILE.md` |
| 2026-03-25 | Phase 1.5 hardening: fill masking, preflight, tri-state QC, cone-angle fix | Docs identified 5 honesty gaps (fills, membership, cone angle, stub flags, grading) | Silently ignoring fill values; binary QC flags | `docs/PHASE_1_5_STATE.md` |
| 2026-03-26 | Candidate windows: THD Oct 2008 verified as dayside but occupancy-limited | Ephemeris confirmed X=8-10 Re, SZA<30, but Dp~1 nPa prevents BG bin | Broader mission scan (prohibited) | `configs/pilot_candidates.yaml` |
| 2026-03-26 | Window-family expansion: THD Sep 3 2008 (Dp~3.5) produces first usable windows | High Dp compresses sheath; same 11.6 Re apogee spans s=0-0.67 | THC Jul 2007 (no MOM data); THB (sparse MOM) | `configs/pilot_window_families.yaml` |
| 2026-03-26 | Bank expanded to 9 windows / 7 passes across 2008+2009 THD seasons | Systematic scan of THD 2009 dayside season yielded 5 new passes | Expanding to other probes (data limitations) | `configs/pilot_live_usable.yaml` |
| 2026-03-26 | Phase 2B audit: CONDITIONAL GO | Shuffled-s, duration sensitivity, VN-bin sensitivity all pass; 6 unresolved issues carried forward | NO-GO (evidence deemed sufficient with caveats) | `docs/PHASE_2B_AUDIT.md` |
| 2026-03-26 | Phase 2C: P7 excluded as spike-dominated | Dn collapses 2.19->0.67, EB 4.22->0.97 after spike removal | Keeping P7 (metrics are spike artifacts) | `docs/PHASE_2C_CONFOUNDER_CLOSURE.md` |
| 2026-03-26 | Phase 2C: seed_D weakened (EB partially spike-dependent) | EB drops 1.96->1.46 after spike removal; Dn robust | Dropping seed_D entirely (Dn still useful) | `docs/SEED_DOSSIER.md` |
| 2026-03-26 | Phase 2D: CONDITIONAL GO for descriptive comparison only | 4 clean + 2 cautious passes span Dn 0.12-2.31; low-Dn relies on cautious passes | NO-GO (too narrow); full GO (insufficient for thresholds) | `docs/PHASE_2D_DETECTOR_READINESS_REVIEW.md` |
| 2026-03-26 | Phase 3A: descriptive Dn/EB comparison completed | Clean core spans Dn 0.94-2.31, EB 0.80-1.96; no thresholds or labels | Threshold exploration (premature); bank expansion (not needed for description) | `docs/PHASE_3A_DNEB_EXPLORATORY_COMPARISON.md` |
| 2026-03-26 | Sign-off wording harmonization | Removed all threshold-oriented language from Phase 2D and handoff | Keeping "threshold exploration" language (overstates current ceiling) | `docs/PHASE_2D_DETECTOR_READINESS_REVIEW.md`, `docs/LLM_HANDOFF.md` |
