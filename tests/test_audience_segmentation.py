"""
Tests for audience segmentation — the business/consumer split.

Enterprise evaluators said plainly that a catalog mixing contract analysis with
collectible-monster agents reads as unserious. Segmentation is the answer, but
it only helps if it is right in *both* directions:

  * a game must never appear in the work view (the original objection), and
  * a real business agent must never be hidden from it (the failure mode
    introduced by over-correcting).

Both directions have already been broken once. A card-forging agent tagged
"trading-cards" slipped past a novelty set that only knew "trading-card", and a
Microsoft Power Platform blueprint agent was ruled consumer-only because it sat
in the "creative" category and its description mentioned an "adaptive card".
These tests pin both fixes.
"""

import importlib.util
import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
BUILDER = REPO_ROOT / "scripts" / "build_static_api.py"
MAP_PATH = REPO_ROOT / "api" / "v1" / "audience" / "map.json"


@pytest.fixture(scope="module")
def bsa():
    spec = importlib.util.spec_from_file_location("_bsa", BUILDER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def audience_map():
    if not MAP_PATH.exists():
        pytest.skip("audience map not built")
    return json.loads(MAP_PATH.read_text(encoding="utf-8"))


def agent(**kw):
    base = {"name": "@t/x", "display_name": "X", "description": "",
            "category": "general", "tags": []}
    base.update(kw)
    return base


# ── tag normalisation ───────────────────────────────────────────────────────

@pytest.mark.parametrize("raw,want", [
    ("trading-cards", "trading-card"),
    ("trading_card", "trading-card"),
    ("Trading Card", "trading-card"),
    ("games", "game"),
    ("GAMES", "game"),
    ("analysis", "analysis"),      # must not become "analysi"
    ("business", "business"),      # ends in "ss"
    ("status", "status"),          # ends in "us"
    ("crm", "crm"),                # too short to depluralise
])
def test_tag_normalisation(bsa, raw, want):
    assert bsa.norm_tag(raw) == want


def test_reference_sets_are_normalised(bsa):
    """A plural in the reference set would silently never match."""
    for name in ("BUSINESS_TAGS", "CONSUMER_TAGS", "NOVELTY_TAGS"):
        tags = getattr(bsa, name)
        assert tags == {bsa.norm_tag(t) for t in tags}, f"{name} is not normalised"


# ── direction 1: novelty must not reach the work view ───────────────────────

@pytest.mark.parametrize("tags", [
    ["trading-cards"], ["trading-card"], ["Games"], ["pokemon"],
    ["collectibles"], ["gaming"],
])
def test_novelty_tags_are_consumer_in_any_spelling(bsa, tags):
    verdict, _, _, _ = bsa.classify(agent(tags=tags))
    assert verdict == "consumer", f"{tags} did not classify as consumer"


def test_no_novelty_in_the_business_slice(audience_map):
    """The exact objection: games sitting next to enterprise tooling."""
    catalog = json.loads((REPO_ROOT / "api" / "v1" / "audience" / "business.json")
                         .read_text(encoding="utf-8"))
    banned = ("trading card", "pokemon", "pokedex", "text adventure",
              "colossal cave", "dungeon crawl")
    leaks = [
        a["name"] for a in catalog["agents"]
        if any(w in json.dumps(a).lower() for w in banned)
    ]
    assert not leaks, f"novelty agents leaked into the business slice: {leaks}"


# ── direction 2: business agents must not be hidden from the work view ──────

def test_creative_category_is_not_a_consumer_signal(bsa):
    """Marketing, design and blueprints are business work."""
    assert "creative" in bsa.NEUTRAL_CATEGORIES
    assert "creative" not in bsa.CATEGORY_WEIGHTS


def test_adaptive_card_wording_does_not_make_an_agent_consumer(bsa):
    """The regression that hid a Power Platform blueprint agent."""
    verdict, _, _, _ = bsa.classify(agent(
        category="creative",
        tags=["agent", "blueprint", "topics", "design", "power_platform"],
        description=("Turn a one-line use case into a build-ready Microsoft "
                     "Copilot Studio agent blueprint with an adaptive card."),
    ))
    assert verdict != "consumer", (
        "a Copilot Studio blueprint agent must stay visible in work mode"
    )


@pytest.mark.parametrize("word", ["card", "collect", "personal"])
def test_ambiguous_words_are_not_consumer_signals(bsa, word):
    """These appear constantly in enterprise copy: adaptive cards, data
    collection, personal data under GDPR."""
    assert word not in bsa.CONSUMER_WORDS


def test_enterprise_agents_stay_in_the_work_view(audience_map):
    m = audience_map["map"]
    must_be_visible = [
        "@cat-agent-skills/copilot_studio_topic_blueprint",
        "@aibast-agents-library/personalized_shopping_assistant",
    ]
    for name in must_be_visible:
        if name not in m:
            continue
        assert m[name] in ("b", "x"), (
            f"{name} is hidden from work mode (verdict {m[name]!r})"
        )


# ── the safe default ────────────────────────────────────────────────────────

def test_unknown_agents_default_to_both(bsa):
    """Hiding a useful agent is worse than showing an off-target one."""
    verdict, _, _, _ = bsa.classify(agent(description="Does a thing."))
    assert verdict == "both"


def test_both_is_the_dominant_verdict(audience_map):
    """If most agents were hard-classified, one bad rule would hide a lot."""
    counts = audience_map["counts"]
    total = sum(counts[k] for k in ("business_only", "consumer_only", "both"))
    assert counts["both"] / total > 0.5, (
        "most agents should be visible in both modes; segmentation is a filter "
        "on the extremes, not a partition of the catalog"
    )


def test_map_covers_every_catalog_agent(audience_map):
    catalog = json.loads((REPO_ROOT / "api" / "v1" / "catalog.json")
                         .read_text(encoding="utf-8"))
    missing = [a["name"] for a in catalog["agents"] if a["name"] not in audience_map["map"]]
    assert not missing, f"{len(missing)} agents missing an audience verdict"


def test_map_legend_matches_the_values_used(audience_map):
    assert set(audience_map["map"].values()) <= set(audience_map["legend"])
