"""Tests for evidence-report generation (offline-safe)."""
import json
import pytest
from pathlib import Path


class TestEvidenceSchema:

    def test_bank_manifest_exists(self):
        p = Path("runs/20260326T040343Z_d0425fd4/evidence/json/bank_manifest.json")
        if not p.exists():
            pytest.skip("Evidence not yet generated")
        with open(p) as f:
            records = json.load(f)
        assert len(records) == 9

    def test_records_have_required_fields(self):
        p = Path("runs/20260326T040343Z_d0425fd4/evidence/json/bank_manifest.json")
        if not p.exists():
            pytest.skip("Evidence not yet generated")
        with open(p) as f:
            records = json.load(f)
        required = [
            "window_id", "pass_id", "pass_date", "geometry_context",
            "upstream_summary", "measurement_model", "data_validity",
            "occupancy", "metric_values", "confounder_audit",
            "review_disposition",
        ]
        for r in records:
            for field in required:
                assert field in r, f"Missing {field} in {r['window_id']}"

    def test_no_forbidden_field_names(self):
        p = Path("runs/20260326T040343Z_d0425fd4/evidence/json/bank_manifest.json")
        if not p.exists():
            pytest.skip("Evidence not yet generated")
        with open(p) as f:
            text = f.read()
        forbidden = ["is_pdl", "positive", "negative", "baseline",
                      "ground_truth", "dev_set", "training"]
        for word in forbidden:
            assert word not in text, f"Forbidden field name '{word}' found"

    def test_review_layer_separated(self):
        p = Path("runs/20260326T040343Z_d0425fd4/evidence/json/bank_manifest.json")
        if not p.exists():
            pytest.skip("Evidence not yet generated")
        with open(p) as f:
            records = json.load(f)
        for r in records:
            # review_disposition should be the only place with evidence_status
            assert "evidence_status" in r["review_disposition"]
            # factual fields should NOT contain evidence_status
            assert "evidence_status" not in r["metric_values"]
            assert "evidence_status" not in r["occupancy"]

    def test_csv_exists(self):
        for name in ["window_matrix.csv", "confounder_register.csv", "interval_audit_matrix.csv"]:
            p = Path(f"runs/20260326T040343Z_d0425fd4/evidence/csv/{name}")
            if not p.exists():
                pytest.skip(f"{name} not yet generated")
            assert p.stat().st_size > 0

    def test_report_index_exists(self):
        p = Path("reports/current_bank/INDEX.md")
        if not p.exists():
            pytest.skip("Reports not yet generated")
        text = p.read_text(encoding="utf-8")
        assert "Evidence Report" in text


class TestEvidenceGeneratorModule:

    def test_get_status(self):
        from pdl_pilot.cli.generate_evidence import _get_status
        assert _get_status("2008-09-03") == "clean_core"
        assert _get_status("2008-08-18") == "cautious"
        assert _get_status("2009-10-24") == "excluded"
        assert _get_status("2099-01-01") == "unknown"
