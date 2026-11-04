"""Publication scans must fail closed when any part of the tree is skipped."""

import builtins
import importlib.util
import json
import os
from pathlib import Path

import pytest


SOURCE = Path(__file__).resolve().parents[1] / "stacks/pii-scout/pii_scout_agent.py"


@pytest.fixture
def scout():
    spec = importlib.util.spec_from_file_location("pii_scout_trust", SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.PiiScoutAgent()


def test_unreadable_file_is_not_safe(scout, tmp_path, monkeypatch):
    blocked = tmp_path / "private.txt"
    blocked.write_text("ordinary text")
    real_open = builtins.open

    def unreadable(path, *args, **kwargs):
        if os.fspath(path) == str(blocked):
            raise PermissionError("permission denied")
        return real_open(path, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", unreadable)
    result = json.loads(scout.perform(path=str(tmp_path)))
    assert result["safe_to_publish"] is False
    assert result["verdict"] == "not safe to publish: scan incomplete"
    assert result["unreadable_skipped"] == 1
    assert result["scanned_files"] == 0
    assert result["skipped"][0]["file"] == "private.txt"
    assert result["patterns_checked"]


def test_excluded_directory_is_reported_as_incomplete(scout, tmp_path):
    (tmp_path / "node_modules").mkdir()
    result = json.loads(scout.perform(path=str(tmp_path)))
    assert result["safe_to_publish"] is False
    assert result["scan_complete"] is False
    assert result["skipped"] == [
        {"file": "node_modules", "reason": "excluded directory"}
    ]


def test_walk_error_is_reported(scout, tmp_path, monkeypatch):
    def failed_walk(path, onerror):
        onerror(PermissionError(13, "permission denied", str(tmp_path / "blocked")))
        return iter(())

    monkeypatch.setattr(os, "walk", failed_walk)
    result = json.loads(scout.perform(path=str(tmp_path)))
    assert result["safe_to_publish"] is False
    assert result["skipped"] == [
        {"file": "blocked", "reason": "unreadable directory"}
    ]


def test_invalid_utf8_is_not_silently_discarded(scout, tmp_path):
    (tmp_path / "binary.dat").write_bytes(b"ordinary\xfftext")
    result = json.loads(scout.perform(path=str(tmp_path)))
    assert result["safe_to_publish"] is False
    assert result["unreadable_skipped"] == 1


def test_cap_limits_output_not_scan(scout, tmp_path):
    for index in range(3):
        (tmp_path / f"{index}.txt").write_text("person@example.com")
    result = json.loads(scout.perform(path=str(tmp_path), max_findings=1))
    assert result["scanned_files"] == 3
    assert len(result["findings"]) == 1
    assert result["findings_truncated"] is True
    assert result["scan_complete"] is True
    assert result["safe_to_publish"] is False


def test_complete_scan_reports_coverage_without_echoing_secrets(scout, tmp_path):
    target = tmp_path / "notes.txt"
    target.write_text("ordinary text")
    result = json.loads(scout.perform(path=str(tmp_path), terms="ACME"))
    assert result["safe_to_publish"] is True
    assert result["scan_complete"] is True
    assert result["patterns_checked"]["supplied_names"] == 1
    secret = "ghp_" + "a" * 36
    target.write_text(secret)
    output = scout.perform(path=str(tmp_path))
    assert secret not in output
    assert json.loads(output)["safe_to_publish"] is False


def test_symlink_directory_is_not_silently_ignored(scout, tmp_path):
    (tmp_path / "real").mkdir()
    (tmp_path / "linked").symlink_to(tmp_path / "real", target_is_directory=True)
    result = json.loads(scout.perform(path=str(tmp_path)))
    assert result["safe_to_publish"] is False
    assert {"file": "linked", "reason": "symlink directory"} in result["skipped"]
