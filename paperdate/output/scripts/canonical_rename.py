#!/usr/bin/env python3
"""
canonical_rename.py
===================
Build a canonical naming layer for the local paper library.

Naming scheme:  YYYY_firstauthor_short-title-keywords
  - lowercase, underscores between major blocks, hyphens within title keywords
  - title keywords ≤ ~6 words, stop-words removed
  - disambiguate collisions with a suffix

This script:
  1. Reads hardcoded metadata (extracted from markdown/JSON headers)
  2. Generates canonical basenames
  3. Copies/renames files across all output layers (pdfs, json, markdown, chunks)
  4. Generates mapping CSV/JSON, manifest, uncertainties, and LLM status summary
  5. Does NOT modify root-directory original PDFs (safe)
"""

import json, csv, os, shutil, re, datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # project root
OUTPUT = BASE / "output"

# ── Hardcoded metadata extracted from markdown/JSON first pages ──────────────
# Each entry: (old_basename_without_ext, year, first_author_last, short_title_keywords, confidence, notes)
# confidence: "high", "medium", "low"

PAPERS = [
    ("1176347265",
     1989, "kunsch", "jackknife-bootstrap-stationary-observations", "high",
     "Kunsch 1989, Ann. Statist. OCR quality fair."),

    ("angeo-22-1001-2004",
     2004, "wang", "pdl-magnetosheath-flow-structure-forces", "high",
     "Wang et al. 2004, Ann. Geophys."),

    ("angeo-22-1347-2004",
     2004, "haaland", "four-spacecraft-magnetopause-crossing-time", "high",
     "Haaland et al. 2004, Ann. Geophys."),

    ("angeo-25-971-2007",
     2007, "dekeyser", "least-squares-gradient-multipoint-cluster", "high",
     "De Keyser et al. 2007, Ann. Geophys."),

    ("angeo-27-3949-2009",
     2009, "zhou", "error-estimation-multi-spacecraft-timing", "high",
     "Zhou et al. 2009, Ann. Geophys."),

    ("angeo-29-2239-2011",
     2011, "vogt", "accuracy-multipoint-boundary-crossing-time", "high",
     "Vogt et al. 2011, Ann. Geophys."),

    ("angeo-31-319-2013",
     2013, "archer", "magnetosheath-dynamic-pressure-enhancements", "high",
     "Archer & Horbury 2013, Ann. Geophys."),

    ("assessing-the-performance-of-magnetopause-models-based-on-themis-data",
     2024, "lin", "magnetopause-model-performance-themis", "high",
     "Lin et al. 2024, Earth Planet. Phys."),

    ("epp2023065",
     2023, "jung", "mshpy23-magnetosheath-parameterized-model", "high",
     "Jung et al. 2023, Earth Planet. Phys."),

    ("file",
     2013, "sandve", "ten-rules-reproducible-computational-research", "high",
     "Sandve et al. 2013, PLoS Comput. Biol. Original filename was 'file.pdf'."),

    ("fspas-11-1390427",
     2024, "aghabozorgi", "magnetopause-location-ml-solar-wind-propagation", "high",
     "Aghabozorgi Nafchi et al. 2024, Front. Astron. Space Sci."),

    ("fspas-11-1401078compressed",
     2024, "pi", "magnetosheath-spatial-profiles-imf-themis", "high",
     "Pi et al. 2024, Front. Astron. Space Sci."),

    ("fspas-11-1427791compressed",
     2024, "michottedewelle", "magnetosheath-density-field-imf-orientation", "high",
     "Michotte de Welle et al. 2024, Front. Astron. Space Sci."),

    ("geophysical-research-letters-2003-robertson-x-ray-emission-from-the-terrestrial-magnetosheath",
     2003, "robertson", "xray-emission-terrestrial-magnetosheath", "high",
     "Robertson & Cravens 2003, GRL."),

    ("investigationoftheoccurrenc",
     2024, "grimmich", "magnetopause-deviation-solar-wind-foreshock", "high",
     "Grimmich et al. 2024, truncated original filename."),

    ("jgr-space-physics-2015-soucek-magnetosheath-plasma-stability-and-ulf-wave-occurrence-as-a-function-of-location-in-the",
     2015, "soucek", "magnetosheath-plasma-stability-ulf-waves", "high",
     "Soucek et al. 2015, JGR Space Physics."),

    ("jgr-space-physics-2017-rezeau-analyzing-the-magnetopause-internal-structure-new-possibilities-offered-by-mms-tested",
     2017, "rezeau", "magnetopause-internal-structure-mms", "high",
     "Rezeau et al. 2017, JGR Space Physics."),

    ("jgr-space-physics-2018-denton-determining-l-m-n-current-sheet-coordinates-at-the-magnetopause-from-magnetospheric",
     2018, "denton", "lmn-current-sheet-coordinates-magnetopause", "high",
     "Denton et al. 2018, JGR Space Physics."),

    ("jgr-space-physics-2019-sun-soft-x-ray-imaging-of-the-magnetosheath-and-cusps-under-different-solar-wind-conditions",
     2019, "sun", "soft-xray-imaging-magnetosheath-cusps-mhd", "high",
     "Sun et al. 2019, JGR Space Physics."),

    ("jgr-space-physics-2019-walsh-quantifying-the-uncertainty-of-using-solar-wind-measurements-for-geospace-inputs",
     2019, "walsh", "solar-wind-measurement-uncertainty-geospace", "high",
     "Walsh et al. 2019, JGR Space Physics."),

    ("jgr-space-physics-2020-raptis-classifying-magnetosheath-jets-using-mms-statistical-properties",
     2020, "raptis", "classifying-magnetosheath-jets-mms", "high",
     "Raptis et al. 2020, JGR Space Physics."),

    ("jgr-space-physics-2020-staples-do-statistical-models-capture-the-dynamics-of-the-magnetopause-during-sudden",
     2020, "staples", "statistical-models-magnetopause-compressions", "high",
     "Staples et al. 2020, JGR Space Physics."),

    ("jgr-space-physics-2025-jiang-spatial-dependence-of-ion-kinetic-instabilities-in-the-earth-s-magnetosheath-mms",
     2025, "jiang", "ion-kinetic-instabilities-magnetosheath-mms", "high",
     "Jiang et al. 2025, JGR Space Physics."),

    ("jgra-128-e2022ja031221",
     2023, "blancocano", "jets-mirror-mode-waves-magnetosheath", "high",
     "Blanco-Cano et al. 2023, JGR Space Physics."),

    ("journal-of-geophysical-research-1896-1977-1-april-1976-zwan-depletion-of-solar-wind-plasma-near-a-planetary-boundary",
     1976, "zwan", "solar-wind-plasma-depletion-planetary-boundary", "high",
     "Zwan & Wolf 1976, JGR."),

    ("journal-of-geophysical-research-space-physics-1-april-1994-anderson-magnetic-spectral-signatures-in-the-earth-s",
     1994, "anderson", "magnetic-spectral-signatures-magnetosheath-pdl", "high",
     "Anderson et al. 1994, JGR."),

    ("journal-of-geophysical-research-space-physics-1-march-1979-crooker-observations-of-plasma-depletion-in-the",
     1979, "crooker", "plasma-depletion-observations-dayside-magnetopause", "high",
     "Crooker et al. 1979, JGR."),

    ("journal-of-geophysical-research-space-physics-1997-anderson-relationships-between-plasma-depletion-and-subsolar",
     1997, "anderson", "plasma-depletion-subsolar-reconnection", "high",
     "Anderson et al. 1997, JGR."),

    ("journal-of-geophysical-research-space-physics-1998-shue-magnetopause-location-under-extreme-solar-wind-conditions",
     1998, "shue", "magnetopause-location-extreme-solar-wind", "high",
     "Shue et al. 1998, JGR. Key Shue98 model paper."),

    ("journal-of-geophysical-research-space-physics-2005-king-solar-wind-spatial-scales-in-and-comparisons-of-hourly-wind",
     2005, "king", "solar-wind-spatial-scales-wind-ace-omni", "high",
     "King & Papitashvili 2005, JGR. OMNI dataset paper."),

    ("journal-of-geophysical-research-space-physics-2005-merka-three-dimensional-position-and-shape-of-the-bow-shock-and",
     2005, "merka", "bow-shock-3d-position-shape-mach-number", "high",
     "Merka et al. 2005, JGR."),

    ("journal-of-geophysical-research-space-physics-2008-soucek-properties-of-magnetosheath-mirror-modes-observed-by",
     2008, "soucek", "magnetosheath-mirror-modes-cluster", "high",
     "Soucek et al. 2008, JGR."),

    ("journal-of-geophysical-research-space-physics-2009-li-cold-dense-magnetopause-boundary-layer-under-northward-imf",
     2009, "li", "cold-dense-magnetopause-boundary-northward-imf", "high",
     "Li et al. 2009, JGR."),

    ("journal-of-geophysical-research-space-physics-2009-plaschke-statistical-study-of-the-magnetopause-motion-first",
     2009, "plaschke", "magnetopause-motion-statistical-study-themis", "high",
     "Plaschke et al. 2009, JGR."),

    ("s11214-021-00865-0",
     2022, "zhang", "dayside-transient-phenomena-magnetosphere-ionosphere", "high",
     "Zhang et al. 2022, Space Sci. Rev. Review paper."),

    ("space-weather-2019-vokhmyanin-on-the-evaluation-of-data-quality-in-the-omni-interplanetary-magnetic-field-database",
     2019, "vokhmyanin", "omni-imf-data-quality-evaluation", "high",
     "Vokhmyanin et al. 2019, Space Weather."),

    ("steegen-et-al-2016-increasing-transparency-through-a-multiverse-analysis",
     2016, "steegen", "multiverse-analysis-transparency", "high",
     "Steegen et al. 2016, Perspectives on Psychological Science."),
]


def make_canonical(year, author, title_kw):
    """Build canonical basename."""
    return f"{year}_{author}_{title_kw}"


def ensure_unique(names):
    """Add suffix if collision."""
    seen = {}
    result = []
    for n in names:
        if n in seen:
            seen[n] += 1
            result.append(f"{n}_{seen[n]}")
        else:
            seen[n] = 0
            result.append(n)
    return result


def safe_copy(src, dst):
    """Copy file if src exists; return True/False."""
    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        return True
    return False


def main():
    ts = datetime.datetime.now().isoformat()

    # Build canonical names
    raw_names = [make_canonical(y, a, t) for (_, y, a, t, _, _) in PAPERS]
    canonical_names = ensure_unique(raw_names)

    records = []
    uncertainties = []
    stats = {"total": len(PAPERS), "renamed": 0, "skipped": 0, "uncertain": 0}

    for i, (old_base, year, author, title_kw, confidence, notes) in enumerate(PAPERS):
        cn = canonical_names[i]
        rec = {
            "paper_id": i + 1,
            "original_root_pdf_name": old_base + ".pdf" if old_base != "fspas-11-1401078compressed" and old_base != "fspas-11-1427791compressed" else old_base.replace("compressed", "_compressed") + ".pdf",
            "original_output_basename": old_base,
            "canonical_basename": cn,
            "title_extracted": title_kw.replace("-", " "),
            "first_author": author,
            "year": year,
            "naming_confidence": confidence,
            "notes": notes,
        }

        # Map original root PDF name correctly
        # Find matching root PDF
        root_pdfs = list(BASE.glob("*.pdf"))
        root_map = {p.stem.lower().replace(" ", "").replace("+", ""): p for p in root_pdfs}
        # We'll just record the path info; the actual root PDF stays untouched

        # Rename in output layers
        layers = {
            "pdfs": (".pdf", "canonical_pdf_path"),
            "json": (".json", "canonical_json_path"),
            "markdown": (".md", "canonical_markdown_path"),
        }

        success = True
        for layer, (ext, key) in layers.items():
            src = OUTPUT / layer / (old_base + ext)
            dst = OUTPUT / layer / (cn + ext)
            if src.exists():
                if src != dst:
                    # If destination exists and is different, remove first
                    if dst.exists():
                        dst.unlink()
                    shutil.copy2(src, dst)
                    src.unlink()
                rec[key] = f"{layer}/{cn}{ext}"
            else:
                rec[key] = f"MISSING: {layer}/{old_base}{ext}"
                success = False

        # Chunks
        src_chunk = OUTPUT / "chunks" / (old_base + "_chunks.json")
        dst_chunk = OUTPUT / "chunks" / (cn + "_chunks.json")
        if src_chunk.exists():
            if src_chunk != dst_chunk:
                if dst_chunk.exists():
                    dst_chunk.unlink()
                shutil.copy2(src_chunk, dst_chunk)
                src_chunk.unlink()
            rec["canonical_chunks_path"] = f"chunks/{cn}_chunks.json"
        else:
            rec["canonical_chunks_path"] = f"MISSING: chunks/{old_base}_chunks.json"

        rec["processing_status"] = "renamed" if success else "partial"
        stats["renamed"] += 1

        if confidence != "high":
            stats["uncertain"] += 1
            uncertainties.append({
                "paper_id": i + 1,
                "canonical_basename": cn,
                "confidence": confidence,
                "reason": notes,
            })

        records.append(rec)

    # ── Write mapping CSV ────────────────────────────────────────────────────
    idx_dir = OUTPUT / "index"
    idx_dir.mkdir(exist_ok=True)

    csv_path = idx_dir / "canonical_filename_mapping.csv"
    fieldnames = [
        "paper_id", "original_root_pdf_name", "original_output_basename",
        "canonical_basename", "canonical_pdf_path", "canonical_json_path",
        "canonical_markdown_path", "canonical_chunks_path",
        "title_extracted", "first_author", "year",
        "naming_confidence", "processing_status", "notes",
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in records:
            w.writerow({k: r.get(k, "") for k in fieldnames})

    # ── Write mapping JSON ───────────────────────────────────────────────────
    with open(idx_dir / "canonical_filename_mapping.json", "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

    # ── Write manifest ───────────────────────────────────────────────────────
    manifest = {
        "generated_at": ts,
        "naming_scheme": "YYYY_firstauthor_short-title-keywords",
        "total_papers": stats["total"],
        "renamed": stats["renamed"],
        "uncertain": stats["uncertain"],
        "papers": [
            {
                "paper_id": r["paper_id"],
                "canonical_basename": r["canonical_basename"],
                "year": r["year"],
                "first_author": r["first_author"],
                "confidence": r["naming_confidence"],
            }
            for r in records
        ],
    }
    with open(idx_dir / "canonical_library_manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    # ── Write uncertainties ──────────────────────────────────────────────────
    with open(idx_dir / "naming_uncertainties.json", "w", encoding="utf-8") as f:
        json.dump(uncertainties if uncertainties else [], f, indent=2, ensure_ascii=False)

    # ── Write LLM-friendly status summary ────────────────────────────────────
    lines = []
    lines.append("# Local Paper Library — Canonical Naming Status")
    lines.append("")
    lines.append(f"**Generated:** {ts}")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- Total papers: **{stats['total']}**")
    lines.append(f"- Successfully renamed: **{stats['renamed']}**")
    lines.append(f"- Papers with naming uncertainty: **{stats['uncertain']}**")
    lines.append("")
    lines.append("## Naming Scheme")
    lines.append("```")
    lines.append("YYYY_firstauthor_short-title-keywords")
    lines.append("```")
    lines.append("- All lowercase")
    lines.append("- Underscores separate year, author, title blocks")
    lines.append("- Hyphens connect words within the title-keyword block")
    lines.append("- Title keywords ≤ 6 words, stop-words removed")
    lines.append("- Example: `1998_shue_magnetopause-location-extreme-solar-wind`")
    lines.append("")
    lines.append("## Recommended Reference Format for Prompts")
    lines.append("")
    lines.append("When referencing a paper in a prompt (Claude Code / ChatGPT Pro):")
    lines.append("```")
    lines.append("Use the canonical basename directly, e.g.:")
    lines.append("  1998_shue_magnetopause-location-extreme-solar-wind")
    lines.append("  1976_zwan_solar-wind-plasma-depletion-planetary-boundary")
    lines.append("  2024_aghabozorgi_magnetopause-location-ml-solar-wind-propagation")
    lines.append("```")
    lines.append("")
    lines.append("Short inline reference: `[shue1998]` or `[zwan1976]` for brevity,")
    lines.append("with canonical basename as the authoritative key.")
    lines.append("")
    lines.append("## Directory Structure")
    lines.append("```")
    lines.append("output/")
    lines.append("  pdfs/          — canonical-named PDF copies")
    lines.append("  json/          — structured JSON (canonical source)")
    lines.append("  markdown/      — readable Markdown layer")
    lines.append("  chunks/        — chunked JSON for retrieval")
    lines.append("  index/         — mappings, manifest, this file")
    lines.append("  scripts/       — processing scripts")
    lines.append("  logs/          — processing logs")
    lines.append("```")
    lines.append("")
    lines.append("## Root PDF Policy")
    lines.append("Original PDFs in the project root directory are **NOT renamed**.")
    lines.append("Only `output/` copies use canonical names.")
    lines.append("The mapping files provide full traceability from old → new names.")
    lines.append("")
    lines.append("## Complete Paper List")
    lines.append("")
    lines.append("| # | Canonical Basename | Year | Author | Confidence |")
    lines.append("|---|-------------------|------|--------|------------|")
    for r in records:
        lines.append(f"| {r['paper_id']} | `{r['canonical_basename']}` | {r['year']} | {r['first_author']} | {r['naming_confidence']} |")
    lines.append("")
    lines.append("## Uncertainties")
    if uncertainties:
        for u in uncertainties:
            lines.append(f"- **{u['canonical_basename']}**: {u['reason']}")
    else:
        lines.append("None — all 37 papers have high-confidence naming.")
    lines.append("")

    with open(idx_dir / "library_status_for_llm.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # ── Print report ─────────────────────────────────────────────────────────
    print(f"=== Canonical Rename Complete ===")
    print(f"Total papers:  {stats['total']}")
    print(f"Renamed:       {stats['renamed']}")
    print(f"Uncertain:     {stats['uncertain']}")
    print(f"")
    print(f"Output files:")
    print(f"  {csv_path}")
    print(f"  {idx_dir / 'canonical_filename_mapping.json'}")
    print(f"  {idx_dir / 'canonical_library_manifest.json'}")
    print(f"  {idx_dir / 'naming_uncertainties.json'}")
    print(f"  {idx_dir / 'library_status_for_llm.md'}")


if __name__ == "__main__":
    main()
