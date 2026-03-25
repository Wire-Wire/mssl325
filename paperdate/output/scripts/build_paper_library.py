#!/usr/bin/env python3
"""
build_paper_library.py
======================
Batch-process PDF papers into a structured local AI paper library.

Primary pipeline: Docling (structured extraction with tables, figures, captions)
Fallback pipeline: PyMuPDF (text extraction when Docling fails)

Output structure under output/:
  pdfs/       - symlinks or copies of original PDFs (visual reference layer)
  json/       - canonical structured JSON per paper
  markdown/   - human/AI-readable Markdown per paper
  chunks/     - chunked text for RAG/retrieval (optional layer)
  index/      - master_index.json + filename_mapping.json
  logs/       - processing_report.json + failures.json + skipped.json
  scripts/    - this script and helpers
"""

import json
import os
import re
import shutil
import sys
import time
import hashlib
import traceback
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # date/
OUTPUT_DIR = BASE_DIR / "output"
PDF_OUT = OUTPUT_DIR / "pdfs"
JSON_OUT = OUTPUT_DIR / "json"
MD_OUT = OUTPUT_DIR / "markdown"
CHUNK_OUT = OUTPUT_DIR / "chunks"
INDEX_OUT = OUTPUT_DIR / "index"
LOG_OUT = OUTPUT_DIR / "logs"

CHUNK_SIZE = 1500  # chars per chunk
CHUNK_OVERLAP = 200

FORCE_REPROCESS = os.environ.get("FORCE_REPROCESS", "0") == "1"

# ---------------------------------------------------------------------------
# Filename normalizer
# ---------------------------------------------------------------------------
def normalize_filename(original: str) -> str:
    """Create a clean, sortable, lowercase filename stem from the original."""
    stem = Path(original).stem
    # decode URL-encoded chars
    stem = stem.replace("+", " ").replace("%20", " ")
    # replace unicode dashes with ascii
    stem = stem.replace("\u2010", "-").replace("\u2011", "-").replace("\u2012", "-")
    stem = stem.replace("\u2013", "-").replace("\u2014", "-").replace("\u2015", "-")
    # collapse whitespace
    stem = re.sub(r"\s+", " ", stem).strip()
    # keep only alphanum, spaces, hyphens
    stem = re.sub(r"[^a-zA-Z0-9 \-]", "", stem)
    # collapse multiple spaces/hyphens
    stem = re.sub(r"[\s\-]+", "-", stem).strip("-")
    stem = stem.lower()
    # truncate to reasonable length
    if len(stem) > 120:
        stem = stem[:120].rsplit("-", 1)[0]
    return stem


# ---------------------------------------------------------------------------
# Docling converter (primary)
# ---------------------------------------------------------------------------
def convert_with_docling(pdf_path: Path):
    """Use Docling to convert PDF. Returns (doc_dict, markdown_str, method)."""
    from docling.document_converter import DocumentConverter
    from docling.datamodel.base_models import InputFormat
    from docling.document_converter import PdfFormatOption
    from docling.datamodel.pipeline_options import PdfPipelineOptions

    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = True
    pipeline_options.do_table_structure = True

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

    result = converter.convert(str(pdf_path))
    doc = result.document

    # Export to markdown
    md_text = doc.export_to_markdown()

    # Build structured JSON dict
    doc_dict = doc.export_to_dict()

    return doc_dict, md_text, "docling"


# ---------------------------------------------------------------------------
# PyMuPDF fallback
# ---------------------------------------------------------------------------
def convert_with_pymupdf(pdf_path: Path):
    """Fallback: extract text with PyMuPDF. Returns (doc_dict, markdown_str, method)."""
    import fitz  # PyMuPDF

    pdf_doc = fitz.open(str(pdf_path))
    pages = []
    full_text_parts = []

    for i, page in enumerate(pdf_doc):
        text = page.get_text("text")
        blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)["blocks"]

        page_data = {
            "page_number": i + 1,
            "width": page.rect.width,
            "height": page.rect.height,
            "text": text,
            "images_count": len(page.get_images(full=True)),
            "blocks": []
        }

        for b in blocks:
            if b["type"] == 0:  # text block
                block_text = ""
                for line in b.get("lines", []):
                    for span in line.get("spans", []):
                        block_text += span.get("text", "")
                    block_text += "\n"
                page_data["blocks"].append({
                    "type": "text",
                    "bbox": b["bbox"],
                    "text": block_text.strip()
                })
            elif b["type"] == 1:  # image block
                page_data["blocks"].append({
                    "type": "image",
                    "bbox": b["bbox"],
                    "width": b.get("width", 0),
                    "height": b.get("height", 0),
                })

        pages.append(page_data)
        full_text_parts.append(text)

    metadata = pdf_doc.metadata or {}
    pdf_doc.close()

    doc_dict = {
        "source": str(pdf_path.name),
        "extraction_method": "pymupdf",
        "metadata": {
            "title": metadata.get("title", ""),
            "author": metadata.get("author", ""),
            "subject": metadata.get("subject", ""),
            "creator": metadata.get("creator", ""),
            "producer": metadata.get("producer", ""),
            "creation_date": metadata.get("creationDate", ""),
            "page_count": len(pages),
        },
        "pages": pages,
    }

    # Build markdown from extracted text
    full_text = "\n\n".join(full_text_parts)
    title = metadata.get("title", pdf_path.stem)
    md_text = f"# {title}\n\n" + full_text

    return doc_dict, md_text, "pymupdf"


# ---------------------------------------------------------------------------
# Chunker
# ---------------------------------------------------------------------------
def make_chunks(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP):
    """Split text into overlapping chunks for RAG."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        if chunk.strip():
            chunks.append({
                "chunk_index": len(chunks),
                "char_start": start,
                "char_end": min(end, len(text)),
                "text": chunk.strip()
            })
        start += chunk_size - overlap
    return chunks


# ---------------------------------------------------------------------------
# Main processing loop
# ---------------------------------------------------------------------------
def find_all_pdfs(base: Path) -> list[Path]:
    """Recursively find all PDFs, excluding output/ directory."""
    pdfs = []
    for p in sorted(base.rglob("*.pdf")):
        # skip anything inside output/
        try:
            p.relative_to(base / "output")
            continue
        except ValueError:
            pass
        pdfs.append(p)
    return pdfs


def process_one(pdf_path: Path, norm_name: str):
    """Process a single PDF. Returns a result dict."""
    result = {
        "original_path": str(pdf_path),
        "original_filename": pdf_path.name,
        "normalized_name": norm_name,
        "json_path": None,
        "markdown_path": None,
        "chunks_path": None,
        "pdf_copy_path": None,
        "status": "pending",
        "method": None,
        "fallback_used": False,
        "warnings": [],
        "error": None,
        "processing_time_s": 0,
    }

    t0 = time.time()
    doc_dict = None
    md_text = None
    method = None

    # Try Docling first
    try:
        doc_dict, md_text, method = convert_with_docling(pdf_path)
        result["method"] = "docling"
    except Exception as e:
        result["warnings"].append(f"Docling failed: {str(e)[:300]}")
        # Fallback to PyMuPDF
        try:
            doc_dict, md_text, method = convert_with_pymupdf(pdf_path)
            result["method"] = "pymupdf"
            result["fallback_used"] = True
        except Exception as e2:
            result["status"] = "failed"
            result["error"] = f"Both pipelines failed. Docling: {result['warnings'][-1]}; PyMuPDF: {str(e2)[:300]}"
            result["processing_time_s"] = round(time.time() - t0, 2)
            return result

    # Check quality: if markdown is near-empty, mark partial
    text_len = len(md_text.strip()) if md_text else 0
    if text_len < 200:
        result["warnings"].append(f"Very short output ({text_len} chars) - possible scan-only or corrupt PDF")

    # --- Write outputs ---
    # 1. Copy PDF
    pdf_dest = PDF_OUT / f"{norm_name}.pdf"
    shutil.copy2(pdf_path, pdf_dest)
    result["pdf_copy_path"] = str(pdf_dest.relative_to(OUTPUT_DIR))

    # 2. Write JSON
    json_dest = JSON_OUT / f"{norm_name}.json"
    json_envelope = {
        "schema_version": "1.0",
        "normalized_name": norm_name,
        "original_filename": pdf_path.name,
        "extraction_method": method,
        "extracted_at": datetime.now().isoformat(),
        "content": doc_dict,
    }
    with open(json_dest, "w", encoding="utf-8") as f:
        json.dump(json_envelope, f, ensure_ascii=False, indent=2, default=str)
    result["json_path"] = str(json_dest.relative_to(OUTPUT_DIR))

    # 3. Write Markdown
    md_dest = MD_OUT / f"{norm_name}.md"
    with open(md_dest, "w", encoding="utf-8") as f:
        f.write(md_text)
    result["markdown_path"] = str(md_dest.relative_to(OUTPUT_DIR))

    # 4. Write chunks
    chunks = make_chunks(md_text)
    chunk_dest = CHUNK_OUT / f"{norm_name}_chunks.json"
    with open(chunk_dest, "w", encoding="utf-8") as f:
        json.dump({
            "normalized_name": norm_name,
            "chunk_size": CHUNK_SIZE,
            "overlap": CHUNK_OVERLAP,
            "total_chunks": len(chunks),
            "chunks": chunks,
        }, f, ensure_ascii=False, indent=2)
    result["chunks_path"] = str(chunk_dest.relative_to(OUTPUT_DIR))

    result["status"] = "success" if not result["warnings"] else "partial_success"
    result["processing_time_s"] = round(time.time() - t0, 2)
    return result


def main():
    print(f"=== Paper Library Builder ===")
    print(f"Base dir: {BASE_DIR}")
    print(f"Output dir: {OUTPUT_DIR}")
    print(f"Force reprocess: {FORCE_REPROCESS}")
    print()

    # Ensure dirs
    for d in [PDF_OUT, JSON_OUT, MD_OUT, CHUNK_OUT, INDEX_OUT, LOG_OUT]:
        d.mkdir(parents=True, exist_ok=True)

    pdfs = find_all_pdfs(BASE_DIR)
    print(f"Found {len(pdfs)} PDF files to process.\n")

    results = []
    name_map = {}  # norm_name -> original_filename
    seen_names = set()

    for i, pdf_path in enumerate(pdfs):
        norm = normalize_filename(pdf_path.name)
        # deduplicate
        if norm in seen_names:
            h = hashlib.md5(pdf_path.name.encode()).hexdigest()[:6]
            norm = f"{norm}-{h}"
        seen_names.add(norm)
        name_map[norm] = str(pdf_path.name)

        # Skip if already done (unless forced)
        if not FORCE_REPROCESS and (JSON_OUT / f"{norm}.json").exists():
            print(f"[{i+1}/{len(pdfs)}] SKIP (already done): {pdf_path.name}")
            results.append({
                "original_path": str(pdf_path),
                "original_filename": pdf_path.name,
                "normalized_name": norm,
                "json_path": f"json/{norm}.json",
                "markdown_path": f"markdown/{norm}.md",
                "chunks_path": f"chunks/{norm}_chunks.json",
                "pdf_copy_path": f"pdfs/{norm}.pdf",
                "status": "skipped",
                "method": "previously_processed",
                "fallback_used": False,
                "warnings": [],
                "error": None,
                "processing_time_s": 0,
            })
            continue

        print(f"[{i+1}/{len(pdfs)}] Processing: {pdf_path.name}")
        try:
            r = process_one(pdf_path, norm)
            results.append(r)
            status_icon = {"success": "OK", "partial_success": "WARN", "failed": "FAIL"}.get(r["status"], "?")
            print(f"  -> {status_icon} ({r['method']}, {r['processing_time_s']}s)")
            if r["warnings"]:
                for w in r["warnings"]:
                    print(f"     WARNING: {w[:100]}")
        except Exception as e:
            print(f"  -> CRASH: {e}")
            results.append({
                "original_path": str(pdf_path),
                "original_filename": pdf_path.name,
                "normalized_name": norm,
                "json_path": None,
                "markdown_path": None,
                "chunks_path": None,
                "pdf_copy_path": None,
                "status": "failed",
                "method": None,
                "fallback_used": False,
                "warnings": [],
                "error": traceback.format_exc()[:500],
                "processing_time_s": 0,
            })

    # --- Write index and logs ---

    # Master index
    master_index = {
        "generated_at": datetime.now().isoformat(),
        "total_pdfs": len(pdfs),
        "success": sum(1 for r in results if r["status"] == "success"),
        "partial_success": sum(1 for r in results if r["status"] == "partial_success"),
        "failed": sum(1 for r in results if r["status"] == "failed"),
        "skipped": sum(1 for r in results if r["status"] == "skipped"),
        "papers": results,
    }
    with open(INDEX_OUT / "master_index.json", "w", encoding="utf-8") as f:
        json.dump(master_index, f, ensure_ascii=False, indent=2)

    # Filename mapping
    with open(INDEX_OUT / "filename_mapping.json", "w", encoding="utf-8") as f:
        json.dump(name_map, f, ensure_ascii=False, indent=2)

    # Processing report
    report = {
        "run_at": datetime.now().isoformat(),
        "total": len(pdfs),
        "success": master_index["success"],
        "partial_success": master_index["partial_success"],
        "failed": master_index["failed"],
        "skipped": master_index["skipped"],
        "total_time_s": round(sum(r["processing_time_s"] for r in results), 2),
    }
    with open(LOG_OUT / "processing_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    # Failures
    failures = [r for r in results if r["status"] == "failed"]
    with open(LOG_OUT / "failures.json", "w", encoding="utf-8") as f:
        json.dump(failures, f, ensure_ascii=False, indent=2)

    # Skipped
    skipped = [r for r in results if r["status"] == "skipped"]
    with open(LOG_OUT / "skipped.json", "w", encoding="utf-8") as f:
        json.dump(skipped, f, ensure_ascii=False, indent=2)

    # Partial successes
    partials = [r for r in results if r["status"] == "partial_success"]
    with open(LOG_OUT / "partial_success.json", "w", encoding="utf-8") as f:
        json.dump(partials, f, ensure_ascii=False, indent=2)

    # Print summary
    print("\n" + "=" * 60)
    print(f"PROCESSING COMPLETE")
    print(f"  Total:           {report['total']}")
    print(f"  Success:         {report['success']}")
    print(f"  Partial success: {report['partial_success']}")
    print(f"  Failed:          {report['failed']}")
    print(f"  Skipped:         {report['skipped']}")
    print(f"  Total time:      {report['total_time_s']}s")
    print(f"  Output dir:      {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
