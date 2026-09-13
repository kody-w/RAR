"""Unit tests for scripts/build_federation.py (consolidated storefront
snapshot: peer-store catalogs projected into state/federation.json)."""

import importlib.util
import hashlib
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="module")
def fed():
    spec = importlib.util.spec_from_file_location(
        "build_federation", REPO_ROOT / "scripts" / "build_federation.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["build_federation"] = module
    spec.loader.exec_module(module)
    return module


def test_frontmatter_simple(fed):
    fm = fed.parse_frontmatter("---\nname: my-skill\ndescription: Does a thing\n---\nBody")
    assert fm["name"] == "my-skill"
    assert fm["description"] == "Does a thing"


def test_frontmatter_folded_scalar(fed):
    md = "---\nname: x\ndescription: >\n  Line one\n  line two\n---\n"
    fm = fed.parse_frontmatter(md)
    assert fm["description"] == "Line one line two"


def test_frontmatter_missing(fed):
    assert fed.parse_frontmatter("# Just a heading\n") == {}


def test_clip_truncates(fed):
    long = "word " * 100
    clipped = fed.clip(long)
    assert len(clipped) <= fed.MAX_DESCRIPTION
    assert clipped.endswith("…")


def test_clip_collapses_whitespace(fed):
    assert fed.clip("  a\n  b\t c ") == "a b c"


def test_federated_skill_projection_is_commit_and_hash_pinned(
    fed,
    monkeypatch,
):
    commit = "a" * 40
    markdown = (
        b"---\nname: portable-skill\n"
        b"description: A portable skill.\n---\n"
    )
    monkeypatch.setattr(fed, "SKILL_REPOS", [("owner/repo", "skills")])

    def fake_json(url):
        if "/commits/main" in url:
            return {"sha": commit}
        assert f"?ref={commit}" in url
        return [{"type": "dir", "name": "portable-skill"}]

    monkeypatch.setattr(fed, "fetch_json", fake_json)
    monkeypatch.setattr(fed, "fetch_bytes", lambda _url: markdown)
    [record] = fed.build_skills()
    assert record["artifact_type"] == "skill"
    assert record["catalog_origin"] == "federated-unreviewed"
    assert record["source_revision"] == commit
    assert record["skill_md_sha256"] == hashlib.sha256(markdown).hexdigest()
    assert f"/{commit}/" in record["skill_md_url"]
    assert record["protocol_conformance"]["status"] == "not_assessed"
