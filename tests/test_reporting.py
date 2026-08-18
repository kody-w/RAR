"""Hermetic tests for the reporting machinery.

Every test here runs offline. Nothing in this file touches the network, needs a
token, or depends on the live GitHub API — so it can run on every push without
being flaky, and a failure always means the code broke rather than the internet
did. The behaviours that genuinely require a live API are NOT faked here; they
are exercised by the documented manual scenarios in docs/REPORTING-TESTS.md.

One of these is a regression test for a bug that actually shipped (the critic
panel and its lookup regressions were retired on 2026-08-18 — RAR publishes
human signal only):

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
    card = reports.render(_sample_agent(), {}, None, None)
    for _, label in reports.SIGNAL_ROWS:
        assert label in card, f"channel '{label}' missing from the card"
    assert card.startswith(reports.START) and card.rstrip().endswith(reports.END)


def test_report_card_carries_no_negative_rows_and_no_machine_score(reports):
    """Positive by design (2026-08-18): the card lists positive outcome
    channels only and never a model-written score."""
    card = reports.render(_sample_agent(), {}, None, None)
    for gone in ("Didn't work", "Couldn't get it running", "Critic score"):
        assert gone not in card, f"{gone!r} must not appear on a report card"
    assert {k for k, _ in reports.SIGNAL_ROWS}.isdisjoint({"did_not_work", "stuck"})


def test_report_card_marks_downloads_unknown_rather_than_zero(reports):
    """No release yet is NOT the same as zero downloads. Printing 0 would be a
    claim we cannot support."""
    card = reports.render(_sample_agent(), {}, None, None)
    reach = card.split("| Reach")[1].split("| Reception")[0]
    assert "—" in reach, "unknown downloads must render as em-dash, never as 0"


def test_aggregated_card_links_home(reports):
    card = reports.render(_sample_agent(), {}, None,
        {"source_name": "cat-agent-skills", "upstream_url": "https://example.invalid/x"},
    )
    assert "cat-agent-skills" in card and "https://example.invalid/x" in card
    assert "never copied" in card, "the index-only posture must be stated on the card"
