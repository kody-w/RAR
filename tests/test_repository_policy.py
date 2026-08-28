"""RAR keeps a complete marketplace contribution and safety surface."""

from __future__ import annotations

from pathlib import Path

import pytest


yaml = pytest.importorskip("yaml")
ROOT = Path(__file__).resolve().parent.parent


def test_repository_policy_files_are_published_and_linked():
    required = {
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "SECURITY.md",
        "SUPPORT.md",
    }
    for filename in required:
        path = ROOT / filename
        assert path.is_file() and path.stat().st_size > 0, filename
        assert "TODO" not in path.read_text(encoding="utf-8"), filename

    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    assert "rapp@rar" in contributing
    assert "security/advisories/new" in contributing
    assert "GitHub Discussions" in contributing


def test_issue_forms_cover_bug_feature_security_and_support_paths():
    directory = ROOT / ".github" / "ISSUE_TEMPLATE"
    bug = yaml.safe_load((directory / "bug_report.yml").read_text())
    feature = yaml.safe_load((directory / "feature_request.yml").read_text())
    config = yaml.safe_load((directory / "config.yml").read_text())

    assert bug["labels"] == ["bug"]
    assert feature["labels"] == ["enhancement"]
    assert any(item.get("id") == "safety" for item in bug["body"])
    assert config["blank_issues_enabled"] is True
    links = {item["name"]: item["url"] for item in config["contact_links"]}
    assert links["Security vulnerability"].endswith(
        "/security/advisories/new"
    )
    assert links["Questions and support"].endswith("/discussions")


def test_rapp_at_x_is_constitutional_and_machine_discoverable():
    constitution = (ROOT / "CONSTITUTION.md").read_text(encoding="utf-8")
    assert "Article XXV" in constitution
    assert "The `rapp@x` Marketplace Identity" in constitution
    assert "`rapp@brainstem`" in constitution
    assert "`rapp@rar`" in constitution
