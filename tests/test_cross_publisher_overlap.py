"""Tests for scripts/check_cross_publisher_overlap.py — the external,
report-only, cross-publisher-only complement to check_near_duplicates.py.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "check_cross_publisher_overlap.py"


@pytest.fixture(scope="module")
def mod():
    spec = importlib.util.spec_from_file_location("_cpo", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _agent(id_, publisher, display_name=None, description=""):
    return {
        "id": id_,
        "name": f"{publisher}/{id_.split('__', 1)[-1]}",
        "publisher": publisher,
        "display_name": display_name or id_,
        "description": description,
    }


def test_flags_true_cross_publisher_duplicate(mod):
    a = _agent("rapp__rapp_dogg_agent", "@rapp",
               description="Hotload one file and a brainstem knows rapp/1 exactly instead of guessing.")
    b = _agent("rapter__rapp_dogg_agent", "@rapter",
               description="Hotload one file and a brainstem knows rapp/1 exactly instead of guessing.")
    overlaps = mod.find_cross_publisher_overlap([a, b], min_jaccard=0.5)
    assert len(overlaps) == 1
    assert overlaps[0]["jaccard"] > 0.85


def test_never_flags_same_publisher_pairs(mod):
    """The whole point of this script vs. the general dedup check: it only
    ever reports pairs across two different publishers."""
    a = _agent("cowork__bulk_update_analyze_revenue", "@cowork",
               description="Applies a bulk field update across analyze revenue records with dry-run preview.")
    b = _agent("cowork__bulk_update_analyze_revenue_v2", "@cowork",
               description="Applies a bulk field update across analyze revenue records with dry-run preview and retry.")
    overlaps = mod.find_cross_publisher_overlap([a, b], min_jaccard=0.5)
    assert overlaps == []


def test_does_not_flag_genuinely_different_agents(mod):
    a = _agent("p1__billing", "@p1", description="Handles invoices and billing reconciliation.")
    b = _agent("p2__weather", "@p2", description="Reports current weather for a location.")
    overlaps = mod.find_cross_publisher_overlap([a, b], min_jaccard=0.5)
    assert overlaps == []


def test_report_formatting_mentions_manifest_resolution_mechanism(mod):
    a = _agent("rapp__x", "@rapp", description="does the exact same thing every time reliably")
    b = _agent("other__x", "@other", description="does the exact same thing every time reliably")
    overlaps = mod.find_cross_publisher_overlap([a, b], min_jaccard=0.3)
    report = mod.format_report(overlaps, scanned=2, min_jaccard=0.3)
    assert "supersedes" in report
    assert "distinct_from" in report


def test_empty_report_when_nothing_found(mod):
    report = mod.format_report([], scanned=5, min_jaccard=0.5)
    assert "No cross-publisher overlap found" in report


def test_main_against_local_catalog_never_fails_ci(mod, monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["check_cross_publisher_overlap.py", "--min-jaccard", "0.9"])
    exit_code = mod.main()
    assert exit_code == 0
    out = capsys.readouterr().out
    assert out  # produced some report, one way or another
