"""Headless tests for discover.html's client-side ranking logic.

discover.html is a static page: all ranking runs in the browser, over
catalog.json + match.json + audience/map.json, with zero backend. These
tests extract the pure ranking functions (tokenize/rawRank/diversify/
groupByStack/rank/candidatesForFacet — none of which touch the DOM) and run
them for real under Node, against small synthetic catalogs, so the
publisher-diversity cap, stack-collapsing, business-score nudge, and facet
filter are verified as executable behavior rather than eyeballed HTML/JS.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
DISCOVER = REPO_ROOT / "discover.html"

pytestmark = pytest.mark.skipif(shutil.which("node") is None, reason="node is not installed")


def _extract_pure_js() -> str:
    text = DISCOVER.read_text(encoding="utf-8")
    m = re.search(r"<script>(.*?)</script>", text, re.S)
    assert m, "discover.html has no <script> block"
    script = m.group(1)
    # Everything above this line is pure ranking logic with no DOM access;
    # everything from here down wires buttons and calls boot(), which we
    # never want to execute in a hermetic test.
    cut = script.index("$('go').onclick")
    return script[:cut]


def _run_rank(catalog_records, index, scores, query, active_facet=None):
    js = _extract_pure_js()
    harness = f"""
{js}
CATALOG = new Map({json.dumps(catalog_records)}.map(a => [a.id, a]));
INDEX = {json.dumps(index)};
SCORES = {json.dumps(scores)};
ACTIVE_FACET = {json.dumps(active_facet)};
const groups = rank({json.dumps(query)});
console.log(JSON.stringify(groups.map(g => ({{
  id: g.primary.id,
  score: g.primary.score,
  variants: g.variants.map(v => v.id),
}}))));
"""
    result = subprocess.run(["node", "-e", harness], capture_output=True, text=True, timeout=15)
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def _agent(id_, publisher, path=None, tags=None):
    return {
        "id": id_,
        "name": f"{publisher}/{id_.split('__', 1)[-1]}",
        "publisher": publisher,
        "display_name": id_,
        "description": f"synthetic agent {id_}",
        "tags": tags or [],
        "quality_tier": "community",
        "requires_env": [],
        "source": {"path": path or f"agents/{publisher}/{id_}.py", "raw": "x", "sha256": ""},
    }


def test_diversity_cap_surfaces_the_long_tail_publisher():
    """One publisher with many strong matches must not fill every slot —
    a smaller publisher's weaker-but-real match has to appear too."""
    dominant = [_agent(f"dom{i}", "@dominant") for i in range(10)]
    other = [_agent(f"oth{i}", "@other") for i in range(2)]
    catalog = dominant + other

    index = {
        "billing": (
            [f"dom{i}:10" for i in range(10)] + [f"oth{i}:2" for i in range(2)]
        )
    }

    groups = _run_rank(catalog, index, {}, "billing")
    picked_ids = {g["id"] for g in groups} | {v for g in groups for v in g["variants"]}
    assert "oth0" in picked_ids
    assert "oth1" in picked_ids
    dominant_count = sum(1 for i in picked_ids if i.startswith("dom"))
    assert dominant_count <= 8  # never more than the result slot count


def test_diversity_cap_still_returns_a_full_page_when_available():
    """The per-publisher cap must not artificially shorten results when there
    are enough other candidates to fill every slot."""
    dominant = [_agent(f"dom{i}", "@dominant") for i in range(10)]
    other = [_agent(f"oth{i}", "@other") for i in range(2)]
    catalog = dominant + other
    index = {"billing": [f"dom{i}:10" for i in range(10)] + [f"oth{i}:2" for i in range(2)]}

    groups = _run_rank(catalog, index, {}, "billing")
    total = sum(1 + len(g["variants"]) for g in groups)
    assert total == 8


def test_stack_family_collapses_into_one_group():
    """Agents sharing a declared stack directory must render as one group
    with siblings listed as variants, not as separate top-level results."""
    stack_agents = [
        _agent(f"variant{i}", "@pub", path=f"agents/@pub/x_stacks/y_stack/variant{i}_agent.py")
        for i in range(3)
    ]
    solo = _agent("solo", "@pub2")
    catalog = stack_agents + [solo]
    index = {"widget": [f"variant{i}:5" for i in range(3)] + ["solo:5"]}

    groups = _run_rank(catalog, index, {}, "widget")
    stack_groups = [g for g in groups if g["id"].startswith("variant")]
    assert len(stack_groups) == 1
    assert len(stack_groups[0]["variants"]) == 2


def test_business_score_moves_a_near_tie():
    catalog = [_agent("a", "@p1"), _agent("b", "@p2")]
    index = {"widget": ["a:10", "b:10"]}
    scores = {"@p1/a": {"b": 10, "c": 0}, "@p2/b": {"b": 0, "c": 0}}

    groups = _run_rank(catalog, index, scores, "widget")
    assert groups[0]["id"] == "a"


def test_business_score_boost_is_capped_and_cannot_flip_a_real_relevance_gap():
    catalog = [_agent("strong_match", "@p1"), _agent("weak_match_high_business", "@p2")]
    index = {"widget": ["strong_match:100", "weak_match_high_business:5"]}
    scores = {
        "@p1/strong_match": {"b": 0, "c": 0},
        "@p2/weak_match_high_business": {"b": 999, "c": 0},
    }

    groups = _run_rank(catalog, index, scores, "widget")
    assert groups[0]["id"] == "strong_match"


def test_facet_filters_to_agents_carrying_the_exact_tag():
    catalog = [
        _agent("tagged", "@p1", tags=["order_to_cash"]),
        _agent("untagged", "@p2", tags=["hire_to_retire"]),
    ]
    index = {"widget": ["tagged:5", "untagged:5"]}

    groups = _run_rank(catalog, index, {}, "widget", active_facet="order_to_cash")
    ids = {g["id"] for g in groups}
    assert ids == {"tagged"}


def test_facet_only_browsing_works_with_no_query_text():
    catalog = [
        _agent("a", "@p1", tags=["order_to_cash"]),
        _agent("b", "@p2", tags=["order_to_cash"]),
        _agent("c", "@p3", tags=["hire_to_retire"]),
    ]
    scores = {"@p1/a": {"b": 5, "c": 0}, "@p2/b": {"b": 2, "c": 0}}

    groups = _run_rank(catalog, {}, scores, "", active_facet="order_to_cash")
    ids = [g["id"] for g in groups]
    assert ids == ["a", "b"]  # sorted by business score, "c" excluded by facet


def test_empty_query_and_no_facet_returns_nothing():
    catalog = [_agent("a", "@p1")]
    groups = _run_rank(catalog, {}, {}, "")
    assert groups == []
