"""Unit tests for scripts/discussion_ratings.py (Discussions as the
upvote/comment backend: snapshot at build time, positive reactions
only)."""

import importlib.util
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="module")
def dr():
    spec = importlib.util.spec_from_file_location(
        "discussion_ratings", REPO_ROOT / "scripts" / "discussion_ratings.py"
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules["discussion_ratings"] = module
    spec.loader.exec_module(module)
    return module


def make_node(title, category="Announcements", number=1, up=0, down=0,
              comments=0, url="https://example.test/d/1"):
    groups = []
    if up:
        groups.append({"content": "THUMBS_UP", "reactors": {"totalCount": up}})
    if down:
        groups.append(
            {"content": "THUMBS_DOWN", "reactors": {"totalCount": down}}
        )
    return {
        "number": number,
        "title": title,
        "url": url,
        "category": {"name": category},
        "comments": {"totalCount": comments},
        "reactionGroups": groups,
    }


# ── title filter ──────────────────────────────────────────────────────

def test_agent_titles_accepted(dr):
    assert dr.is_agent_title("@rapp/basic_agent")
    assert dr.is_agent_title("@kody-w/registry_client_agent")
    assert dr.is_agent_title("  @howardh/cardsmith_agent  ")


def test_non_agent_titles_rejected(dr):
    assert not dr.is_agent_title("Welcome to the forum")
    assert not dr.is_agent_title("@rapp/Basic_Agent")  # uppercase slug
    assert not dr.is_agent_title("rapp/basic_agent")  # missing @
    assert not dr.is_agent_title("@rapp/basic-agent")  # dash in slug
    assert not dr.is_agent_title("")


# ── positive-only counting ────────────────────────────────────────────

def test_positive_reactions_counted(dr):
    groups = [
        {"content": "THUMBS_UP", "reactors": {"totalCount": 3}},
        {"content": "HEART", "reactors": {"totalCount": 2}},
        {"content": "ROCKET", "reactors": {"totalCount": 1}},
    ]
    assert dr.positive_score(groups) == 6


def test_negative_and_neutral_ignored(dr):
    groups = [
        {"content": "THUMBS_UP", "reactors": {"totalCount": 2}},
        {"content": "THUMBS_DOWN", "reactors": {"totalCount": 50}},
        {"content": "CONFUSED", "reactors": {"totalCount": 7}},
        {"content": "EYES", "reactors": {"totalCount": 9}},
    ]
    assert dr.positive_score(groups) == 2


def test_positive_score_handles_missing(dr):
    assert dr.positive_score(None) == 0
    assert dr.positive_score([]) == 0
    assert dr.positive_score([{"content": "THUMBS_UP"}]) == 0


# ── snapshot building ─────────────────────────────────────────────────

def test_build_snapshot_filters_category_and_registry(dr):
    registry = {"@rapp/basic_agent"}
    nodes = [
        make_node("@rapp/basic_agent", up=4, comments=2, number=10),
        make_node("@rapp/basic_agent", category="General", up=99, number=11),
        make_node("@evil/spoofed_agent", up=99, number=12),  # not in registry
        make_node("Welcome thread", up=99, number=13),  # not an agent title
    ]
    snap = dr.build_snapshot(nodes, registry)
    assert set(snap) == {"@rapp/basic_agent"}
    assert snap["@rapp/basic_agent"]["upvotes"] == 4
    assert snap["@rapp/basic_agent"]["comments"] == 2


def test_build_snapshot_duplicate_earliest_wins(dr):
    registry = {"@rapp/basic_agent"}
    nodes = [
        make_node("@rapp/basic_agent", up=99, number=50),
        make_node("@rapp/basic_agent", up=1, number=3),  # seeded original
    ]
    snap = dr.build_snapshot(nodes, registry)
    assert snap["@rapp/basic_agent"]["number"] == 3
    assert snap["@rapp/basic_agent"]["upvotes"] == 1


# ── persistence (non-fatal, non-clobbering) ───────────────────────────

def test_persist_never_clobbers_with_empty(dr, tmp_path, monkeypatch):
    snapshot_file = tmp_path / "state" / "discussion_ratings.json"
    snapshot_file.parent.mkdir(parents=True)
    original = {"schema": dr.SNAPSHOT_SCHEMA, "agents": {"@a/b_agent": {}}}
    snapshot_file.write_text(json.dumps(original))
    monkeypatch.setattr(dr, "SNAPSHOT_FILE", snapshot_file)
    monkeypatch.setattr(dr, "REPO_ROOT", tmp_path)
    assert dr.persist({}) is False
    assert json.loads(snapshot_file.read_text()) == original


def test_persist_writes_sorted_snapshot(dr, tmp_path, monkeypatch):
    snapshot_file = tmp_path / "state" / "discussion_ratings.json"
    monkeypatch.setattr(dr, "SNAPSHOT_FILE", snapshot_file)
    monkeypatch.setattr(dr, "REPO_ROOT", tmp_path)
    ratings = {
        "@z/zz_agent": {"upvotes": 1, "comments": 0, "url": "", "number": 2},
        "@a/aa_agent": {"upvotes": 2, "comments": 1, "url": "", "number": 1},
    }
    assert dr.persist(ratings) is True
    written = json.loads(snapshot_file.read_text())
    assert written["schema"] == dr.SNAPSHOT_SCHEMA
    assert list(written["agents"]) == ["@a/aa_agent", "@z/zz_agent"]
    # No timestamp fields — the file must be byte-stable when counts
    # are unchanged, so the refresh workflow can skip no-op commits.
    assert "updated_at" not in written


def test_persist_same_counts_byte_stable(dr, tmp_path, monkeypatch):
    snapshot_file = tmp_path / "state" / "discussion_ratings.json"
    monkeypatch.setattr(dr, "SNAPSHOT_FILE", snapshot_file)
    monkeypatch.setattr(dr, "REPO_ROOT", tmp_path)
    ratings = {"@a/aa_agent": {"upvotes": 2, "comments": 1, "url": "", "number": 1}}
    dr.persist(ratings)
    first = snapshot_file.read_bytes()
    dr.persist(dict(ratings))
    assert snapshot_file.read_bytes() == first
