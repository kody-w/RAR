"""The clutter ratchet: counts may shrink, never grow."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import check_ratchet as r  # noqa: E402

FILES = ["README.md", "index.html", "pitch.html", "agents/@a/x_agent.py", "stacks/s/stack.json", "docs/a.md"]
REGISTRY = {"schema": "x", "agents": [{"quality_tier": "official", "category": "core"},
                                      {"quality_tier": "community", "category": "general"}],
            "stack_packs": [{"name": "s"}], "swarms": [], "releases": [{"tag": "v1"}]}


def limits(**over):
    base = r.measure(FILES, REGISTRY)
    base.update(over)
    return {k: {"limit": v, "ruling": "test"} for k, v in base.items()}


def test_measure_counts_what_a_visitor_meets():
    assert r.measure(FILES, REGISTRY) == {"root_files": 3, "root_pages": 2, "top_folders": 3,
                                          "entry_kinds": 2, "quality_tiers": 2, "categories": 2}


def test_at_the_limit_passes():
    assert r.compare(r.measure(FILES, REGISTRY), limits()) == ({}, {})


def test_one_more_root_page_is_over():
    over, _ = r.compare(r.measure(FILES + ["ode.html"], REGISTRY), limits())
    assert over == {"root_files": (4, 3), "root_pages": (3, 2)}


def test_a_new_kind_or_tier_is_over():
    grown = dict(REGISTRY, eggs=[{"quality_tier": "frontier"}])
    over, _ = r.compare(r.measure(FILES, grown), limits())
    assert set(over) == {"entry_kinds", "quality_tiers"}


def test_shrinking_is_reported_so_it_can_be_locked_in():
    _, under = r.compare(r.measure([f for f in FILES if f != "pitch.html"], REGISTRY), limits())
    assert under == {"root_files": (2, 3), "root_pages": (1, 2)}


def test_the_repo_is_within_its_own_limits():
    counts = r.measure(r.tracked(), json.loads((ROOT / "registry.json").read_text()))
    stored = json.loads(r.LIMITS.read_text())["limits"]
    over, _ = r.compare(counts, stored)
    assert over == {}, f"RAR grew where it may only shrink: {over}"
    assert set(stored) == set(r.WHAT) and all(v.get("ruling") for v in stored.values())
