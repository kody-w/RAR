"""Hermetic tests for the reporting machinery.

Every test here runs offline. Nothing in this file touches the network, needs a
token, or depends on the live GitHub API — so it can run on every push without
being flaky, and a failure always means the code broke rather than the internet
did. The behaviours that genuinely require a live API are NOT faked here; they
are exercised by the documented manual scenarios in docs/REPORTING-TESTS.md.

Two of these are regression tests for bugs that actually shipped:

  test_critic_lookup_resolves_dashed_publishers
      state/critic_reviews.json keys its map with an UNDERSCORE-normalized name
      while each record's own `name` field holds the real dashed one. A lookup
      by dict key silently returned nothing for every publisher with a dash —
      which is most of the registry — so every report card read "not yet
      scored" while 79 agents had real scores. It failed silently and looked
      exactly like "no data yet", which is the worst way for a metric to break.

  test_splice_replaces_block_when_end_marker_is_missing
      If a human truncated the report block, START survived without END and the
      splice appended a SECOND block instead of replacing the first — so cards
      would accumulate on every run, forever.
"""
from __future__ import annotations

import importlib.util
import json
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = REPO_ROOT / "scripts"


def _load(name: str):
    """Import a script by path — scripts/ is not a package."""
    path = SCRIPTS / f"{name}.py"
    if not path.exists():
        pytest.skip(f"{path.relative_to(REPO_ROOT)} not present")
    spec = importlib.util.spec_from_file_location(f"_rar_{name}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def reports():
    return _load("publish_reports")


@pytest.fixture(scope="module")
def ratings():
    return _load("discussion_ratings")


# ── splice(): the report block must be replaceable, exactly once, forever ────

def test_splice_appends_when_no_block_present(reports):
    out = reports.splice("Human wrote this.", "<!-- rar:report:start -->X<!-- rar:report:end -->")
    assert "Human wrote this." in out
    assert out.count("rar:report:start") == 1


def test_splice_is_idempotent(reports):
    """Re-splicing must not stack blocks — this is what makes a daily rewrite
    safe to run forever."""
    block = "<!-- rar:report:start -->\nA\n<!-- rar:report:end -->"
    once = reports.splice("Intro.", block)
    twice = reports.splice(once, block)
    assert twice.count("rar:report:start") == 1
    assert twice.count("rar:report:end") == 1


def test_splice_preserves_human_text_on_both_sides(reports):
    """A maintainer's words must survive CI rewriting the card next to them."""
    block = "<!-- rar:report:start -->\nOLD\n<!-- rar:report:end -->"
    body = f"Above the card.\n\n{block}\n\nBelow the card."
    new = reports.splice(body, "<!-- rar:report:start -->\nNEW\n<!-- rar:report:end -->")
    assert "Above the card." in new
    assert "Below the card." in new
    assert "NEW" in new and "OLD" not in new


def test_splice_replaces_block_when_end_marker_is_missing(reports):
    """REGRESSION. A truncated block leaves START without END. The block must
    still be replaced — appending a second one makes cards accumulate on every
    daily run."""
    truncated = "Intro.\n\n<!-- rar:report:start -->\nhalf a card, no end marker"
    out = reports.splice(truncated, "<!-- rar:report:start -->\nFRESH\n<!-- rar:report:end -->")
    assert out.count("rar:report:start") == 1, "a second block was appended instead of replacing"
    assert "FRESH" in out
    assert "half a card" not in out
    assert "Intro." in out


# ── the critic-score join: the bug that read as "no data" ────────────────────

def test_critic_index_resolves_a_dashed_publisher(reports):
    """REGRESSION, exercising the SHIPPED code.

    The first version of this test re-implemented both lookups inside the test
    body and compared them to each other. It therefore asserted a property of
    critic_reviews.json, not of publish_reports.py, and stayed green with the
    bug fully reintroduced — while every card silently reverted to "not yet
    scored". A regression test that cannot fail is worse than no test, because
    the documentation then cites it as proof.

    This calls reports.critic_index directly, on a fixture shaped like the real
    file: key underscore-normalized, record's own `name` dashed.
    """
    raw = {
        "@aibast_agents_library/account_intelligence": {
            "name": "@aibast-agents-library/account_intelligence",
            "critic_avg": 80.0,
            "critic_count": 2,
        }
    }
    idx = reports.critic_index(raw)
    assert "@aibast-agents-library/account_intelligence" in idx, (
        "critic records are not indexed by their authoritative dashed `name` — "
        "every dashed publisher resolves to nothing and reads 'not yet scored'"
    )
    assert idx["@aibast-agents-library/account_intelligence"]["critic_avg"] == 80.0


def test_a_scored_agent_renders_its_score_not_not_yet_scored(reports):
    """End-to-end over render(): a resolved critic record must reach the card.

    Pins the observable symptom rather than the mechanism, so any future way of
    breaking the join — not just the key/name one — still fails here.
    """
    agent = {"name": "@aibast-agents-library/account_intelligence", "version": "1.0.0",
             "category": "core", "quality_tier": "community"}
    raw = {"@aibast_agents_library/account_intelligence": {
        "name": "@aibast-agents-library/account_intelligence",
        "critic_avg": 80.0, "critic_count": 2}}
    critic = reports.critic_index(raw).get(agent["name"], {})
    card = reports.render(agent, {}, critic, None, None)
    assert "80/100" in card, f"scored agent rendered without its score:\n{card}"
    assert "not yet scored" not in card


# ── the seven feedback channels must agree everywhere they are written ──────

def test_signal_channels_agree_across_surfaces(reports, ratings):
    """The 7 channels are declared in three places — the collector, the report
    card, and stats.html. They are a contract: if they drift, a reaction is
    counted under one name and displayed under another, and the number silently
    stops meaning what the label says."""
    collector = set(getattr(ratings, "SIGNAL_MAP", {}).values())
    card = {k for k, _ in getattr(reports, "SIGNAL_ROWS", [])}
    if not collector or not card:
        pytest.skip("signal tables not exposed by these modules")

    assert card == collector, (
        f"report card and collector disagree: "
        f"card-only={card - collector} collector-only={collector - card}"
    )

    stats = REPO_ROOT / "stats.html"
    if stats.exists():
        html = stats.read_text(encoding="utf-8")
        missing = [c for c in collector if c not in html]
        assert not missing, f"stats.html is missing channel(s): {missing}"


def test_every_signal_channel_maps_to_a_distinct_reaction(ratings):
    """Two channels sharing one emoji would make them permanently
    indistinguishable — nobody could ever separate the counts again."""
    sig = getattr(ratings, "SIGNAL_MAP", {})
    if not sig:
        pytest.skip("SIGNAL_MAP not exposed")
    assert len(set(sig.keys())) == len(sig), "a reaction is mapped twice"
    assert len(set(sig.values())) == len(sig), "two channels share one reaction"


# ── snapshots must never destroy real data on a bad API day ─────────────────

def test_download_snapshot_refuses_to_write_zeroes():
    """A failed fetch must leave yesterday's real counts alone. Overwriting them
    with zeroes is indistinguishable from 'nobody downloaded anything', and the
    loss is permanent."""
    src = (SCRIPTS / "fetch_download_counts.py")
    if not src.exists():
        pytest.skip("fetch_download_counts.py absent")
    text = src.read_text(encoding="utf-8")
    assert re.search(r"assets_published.*==\s*0", text), (
        "the zeroed-snapshot guard is gone — a bad API day can now erase real counts"
    )


def test_aggregated_crawl_refuses_to_empty_the_catalog():
    src = SCRIPTS / "crawl_sources.py"
    if not src.exists():
        pytest.skip("crawl_sources.py absent")
    text = src.read_text(encoding="utf-8")
    assert "keeping existing snapshot" in text, (
        "crawl_sources lost its guard against replacing a real catalog with an empty one"
    )


# ── the report card itself ──────────────────────────────────────────────────

def _sample_agent():
    return {
        "name": "@acme/widget", "version": "1.2.3", "quality_tier": "community",
        "category": "devtools", "platforms": ["Copilot Studio"],
        "_sha256": "a" * 64,
    }


def test_report_card_renders_every_channel(reports):
    card = reports.render(_sample_agent(), {}, {}, None, None)
    for _, label in reports.SIGNAL_ROWS:
        assert label in card, f"channel '{label}' missing from the card"
    assert card.startswith(reports.START) and card.rstrip().endswith(reports.END)


def test_report_card_states_critic_score_when_present(reports):
    card = reports.render(_sample_agent(), {}, {"critic_avg": 80.0, "critic_count": 2}, None, None)
    assert "80/100" in card and "2 independent" in card


def test_report_card_says_not_scored_when_absent(reports):
    card = reports.render(_sample_agent(), {}, {}, None, None)
    assert "not yet scored" in card


def test_report_card_marks_downloads_unknown_rather_than_zero(reports):
    """No release yet is NOT the same as zero downloads. Printing 0 would be a
    claim we cannot support."""
    card = reports.render(_sample_agent(), {}, {}, None, None)
    reach = card.split("| Reach")[1].split("| Reception")[0]
    assert "—" in reach, "unknown downloads must render as em-dash, never as 0"


def test_aggregated_card_links_home(reports):
    card = reports.render(
        _sample_agent(), {}, {}, None,
        {"source_name": "cat-agent-skills", "upstream_url": "https://example.invalid/x"},
    )
    assert "cat-agent-skills" in card and "https://example.invalid/x" in card
    assert "never copied" in card, "the index-only posture must be stated on the card"
