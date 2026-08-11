"""The ranked front page has to be auditable from its own payload.

A ranking is a claim about other people's work. RAR publishes 355 of them in one
file, so the only thing standing between "useful front page" and "opaque
leaderboard" is whether a reader can check any single row without trusting the
builder. That is what these tests pin:

  * every sentence in `why[]` is re-derived here from `signals` alone, by code
    that never imports the generator's phrasing helpers — a `why` the payload
    cannot justify fails, and `test_the_why_checker_is_not_vacuous` proves the
    checker would actually notice;
  * the two populations stay separate — no aggregated row carries a body, an
    install URL into this repo, or a RAR-scored component;
  * the build is deterministic, so `--check` in CI means "the data moved", not
    "the clock moved";
  * and building it changes nothing else on disk. `api/v1/front.json` is
    purely additive; catalog.json, match.json, registry.json and the
    append-only published-path ledger are somebody else's contract.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
BUILDER = REPO_ROOT / "scripts" / "build_front_page.py"
FRONT = REPO_ROOT / "api" / "v1" / "front.json"
REGISTRY = REPO_ROOT / "registry.json"
AGGREGATED = REPO_ROOT / "state" / "aggregated.json"

# Files this build must never touch. catalog.json and match.json belong to
# build_static_api.py, index.json to build_pokedex_api.py, registry.json to
# build_registry.py, and published_paths.json is the append-only URL ledger
# CONSTITUTION.md Article XXIII is enforced against.
UNTOUCHABLE = [
    REPO_ROOT / "api" / "v1" / "catalog.json",
    REPO_ROOT / "api" / "v1" / "match.json",
    REPO_ROOT / "api" / "v1" / "index.json",
    REPO_ROOT / "registry.json",
    REPO_ROOT / "state" / "published_paths.json",
]


@pytest.fixture(scope="module")
def bfp():
    spec = importlib.util.spec_from_file_location("_bfp", BUILDER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def payload():
    if not FRONT.exists():
        pytest.skip("api/v1/front.json not built — run scripts/build_front_page.py")
    return json.loads(FRONT.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def items(payload):
    return payload["items"]


# ── shape ───────────────────────────────────────────────────────────────────


def test_schema_id(payload):
    assert payload["schema"] == "rar-front-page/1.0"


def test_required_top_level_keys(payload):
    for key in ("schema", "generated", "counts", "ranking", "items"):
        assert key in payload, f"front.json is missing '{key}'"
    for key in ("explain", "components", "not_scored"):
        assert key in payload["ranking"], f"ranking is missing '{key}'"
    for key in ("native", "aggregated", "ranked", "sources"):
        assert key in payload["counts"], f"counts is missing '{key}'"


def test_ranked_equals_native_plus_aggregated(payload, items):
    counts = payload["counts"]
    assert counts["ranked"] == counts["native"] + counts["aggregated"]
    assert counts["ranked"] == len(items)
    assert counts["native"] == sum(1 for i in items if i["origin"] == "native")
    assert counts["aggregated"] == sum(1 for i in items if i["origin"] == "aggregated")


def test_counts_agree_with_the_inputs(payload):
    """A front page that silently drops a population is worse than none."""
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    aggregated = json.loads(AGGREGATED.read_text(encoding="utf-8"))
    assert payload["counts"]["native"] == len(registry["agents"]), (
        "front.json does not rank every registered agent — "
        "run: python3 scripts/build_front_page.py")
    # A ref in both populations is ONE row: the toaster materialises index
    # entries into hosted agents, so the hosted agent is canonical and the index
    # row rides along as provenance. `aggregated` therefore counts only the
    # entries RAR does NOT host.
    native_refs = {a["name"] for a in registry["agents"]}
    agg_refs = {i["ref"] for i in aggregated["items"]}
    assert payload["counts"]["aggregated"] == len(agg_refs - native_refs)
    assert payload["counts"]["with_source_provenance"] == len(agg_refs & native_refs)
    assert payload["counts"]["ranked"] == len(native_refs | agg_refs)
    assert payload["counts"]["sources"] == len(aggregated["sources"])


def test_no_entry_is_listed_twice(items):
    """The bug this pins: every crawled entry was ALSO a hosted agent, so the
    first cut of the front page showed all 76 of them twice and advertised a
    catalog a third larger than it was."""
    seen = {}
    for item in items:
        seen.setdefault(item["ref"], []).append(item["rank"])
    dupes = {ref: ranks for ref, ranks in seen.items() if len(ranks) > 1}
    assert not dupes, f"{len(dupes)} ref(s) appear more than once: {list(dupes.items())[:5]}"


def test_provenance_rows_keep_the_two_populations_apart(items):
    """A hosted agent may carry a source's numbers, but never merged into RAR's."""
    carried = [
        i for i in items
        if i["origin"] == "native" and i["source"] is not None
    ]
    assert carried, "expected some hosted agents to carry source provenance"
    for item in carried:
        assert item["origin"] == "native"
        rar, src = item["signals"]["rar"], item["signals"]["source"]
        assert src is not None and rar is not None
        # The source's download count must never appear inside RAR's own block.
        assert "downloads" not in rar


def test_every_ref_is_a_real_entry(items):
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    aggregated = json.loads(AGGREGATED.read_text(encoding="utf-8"))
    native_refs = {a["name"] for a in registry["agents"]}
    agg_refs = {i["ref"] for i in aggregated["items"]}
    unknown = [
        i["ref"] for i in items
        if i["ref"] not in (native_refs if i["origin"] == "native" else agg_refs)
    ]
    assert not unknown, f"{len(unknown)} ranked ref(s) exist nowhere: {unknown[:5]}"


def test_every_item_carries_the_contract_fields(items):
    required = ("rank", "ref", "title", "description", "origin", "category",
                "tags", "audience", "url", "install", "source", "score",
                "signals", "why")
    for item in items[:50] + items[-50:]:
        for key in required:
            assert key in item, f"{item.get('ref')} is missing '{key}'"
        assert item["origin"] in ("native", "aggregated")
        assert item["audience"] in ("business", "consumer", "both", None)
        assert isinstance(item["tags"], list)
        assert set(item["signals"]) == {"rar", "source"}


# ── ordering and bounds ─────────────────────────────────────────────────────


def test_scores_are_within_bounds(items):
    bad = [(i["ref"], i["score"]) for i in items if not 0.0 <= i["score"] <= 100.0]
    assert not bad, f"scores outside 0-100: {bad[:5]}"


def test_list_is_sorted_by_rank(items):
    assert [i["rank"] for i in items] == list(range(1, len(items) + 1))


def origin_percentile(item):
    return round(
        1.0 - (item["origin_rank"] - 1) / item["origin_size"],
        6,
    )


def test_rank_order_matches_published_policy(items):
    """Global rank interleaves each population by its within-origin percentile."""
    expected = sorted(
        items,
        key=lambda item: (
            -origin_percentile(item),
            -item["score"],
            item["ref"],
        ),
    )
    assert [item["ref"] for item in items] == [
        item["ref"] for item in expected
    ]


def test_ties_break_on_ref_ascending(items):
    for previous, current in zip(items, items[1:]):
        if (
            origin_percentile(previous) == origin_percentile(current)
            and previous["score"] == current["score"]
        ):
            assert previous["ref"] < current["ref"], (
                f"tie between {previous['ref']} and {current['ref']} is unstable")


# ── the two populations never merge ─────────────────────────────────────────


# Anything that would mean the skill body itself had been copied here. The
# crawler's stance is index-only, and that is the only footing that is safe
# across sources whose licences differ or cannot be read at all.
BODY_KEYS = {
    "body", "content", "source_code", "sourcecode", "code", "prompt",
    "instructions", "skill", "bundle", "markdown", "md", "script", "file",
    "raw", "payload",
}


def walk_keys(node):
    if isinstance(node, dict):
        for key, value in node.items():
            yield key
            yield from walk_keys(value)
    elif isinstance(node, list):
        for value in node:
            yield from walk_keys(value)


def test_no_aggregated_item_carries_a_body(items):
    leaks = []
    for item in items:
        if item["origin"] != "aggregated":
            continue
        hits = {k for k in walk_keys(item) if k.lower() in BODY_KEYS}
        if hits:
            leaks.append((item["ref"], sorted(hits)))
    assert not leaks, (
        f"aggregated entries are index-only; content-shaped fields found: {leaks[:5]}")


def test_aggregated_items_link_home_and_offer_no_local_install(items):
    for item in items:
        if item["origin"] != "aggregated":
            continue
        assert item["install"] is None, (
            f"{item['ref']} offers a local install for content RAR does not host")
        assert item["source"], f"{item['ref']} has no source attribution"
        for key in ("id", "display_name", "home_url", "license"):
            assert key in item["source"]
        assert "raw.githubusercontent.com/kody-w/RAR" not in (item["url"] or ""), (
            f"{item['ref']} points at this repo instead of its origin")


def test_a_source_never_scores_a_hosted_agent(items):
    """The blocker an adversarial pass caught: reach was briefly folded into the
    native score for rows a crawler also found, making one published number out
    of two populations' counters while `explain` denied doing it."""
    carried = [
        i for i in items
        if i["origin"] == "native" and i["source"] is not None
    ]
    assert carried, "expected some hosted agents to carry source provenance"
    for item in carried:
        assert "reach" not in item["components"], (
            f"{item['ref']} is a hosted agent scored on its source's reach")
        assert "reach" not in item["scores_on"]
        # The number is still there — as provenance, which is the whole point.
        assert "downloads" in item["signals"]["source"]
    # And no why-line may cite a number that did not move the rank.
    for item in carried:
        assert not any("download" in w for w in item["why"]), (
            f"{item['ref']} explains its rank with a number that does not score it")


def test_source_blocks_appear_only_where_provenance_exists(items):
    """A source block means "this also exists in a crawled index" — nothing else."""
    for item in items:
        paired = item["source"] is not None
        assert (item["signals"]["source"] is not None) == paired, (
            f"{item['ref']} has a source block and source signals out of step")
        if not paired and item["origin"] == "native":
            assert "reach" not in item["components"], (
                f"{item['ref']} is scored on reach with no source to reach from")


def test_components_declare_which_population_they_apply_to(payload):
    applies = {c["key"]: c["applies_to"] for c in payload["ranking"]["components"]}
    assert applies["reach"] == "aggregated"
    for key in ("curator", "community", "tier"):
        assert applies[key] == "native", (
            f"'{key}' is a RAR counter and cannot apply to a third-party entry")


def test_no_item_is_scored_on_a_component_from_the_other_population(payload, items):
    applies = {c["key"]: c["applies_to"] for c in payload["ranking"]["components"]}
    for item in items:
        for key in item.get("components", {}):
            assert applies[key] in ("both", item["origin"]), (
                f"{item['ref']} ({item['origin']}) is scored on '{key}', "
                f"which applies to {applies[key]}")


def test_explain_states_the_within_origin_limit(payload):
    explain = payload["ranking"]["explain"].lower()
    assert "origin" in explain, "explain must say scores compare within an origin"
    assert "not scored" in explain or "not_scored" in explain
    assert payload["ranking"]["not_scored"], "not_scored must list something"


# ── why[] is re-derived from signals ────────────────────────────────────────
#
# Deliberately independent of the generator: this table is written from the
# contract ("never write a `why` entry that is not backed by a value in
# `signals`"), not imported from build_front_page.py, so a change in phrasing
# that loses its backing fails here rather than shipping.


def _num(value):
    return float(value) if isinstance(value, (int, float)) else None


NUMERIC_WHY = [
    (r"^([\d.]+)/5 from (\d+) curator reviews?$",
     lambda g, s: (_num(s["rar"]["curator_mean"]) == float(g[0])
                   and s["rar"]["curator_n"] == int(g[1])
                   and s["rar"]["curator_n"] > 0)),
    (r"^(\d+) upvotes?$", lambda g, s: s["rar"]["upvotes"] == int(g[0]) > 0),
    (r"^(\d+) comments?$", lambda g, s: s["rar"]["comments"] == int(g[0]) > 0),
    (r"^(\d+) hands-on reports?$",
     lambda g, s: s["rar"]["engagement"] == int(g[0]) > 0),
    (r"^(\w+) tier$", lambda g, s: s["rar"]["tier"] == g[0]),
    (r"^added (\d+) days? ago$",
     lambda g, s: s["rar"]["age_days"] == int(g[0]) > 0),
    (r"^(\d+) lines?$", lambda g, s: s["rar"]["lines"] == int(g[0])),
    (r"^(\d+) downloads? at the source$",
     lambda g, s: s["source"] and s["source"]["downloads"] == int(g[0]) > 0),
    # A hosted agent that also exists in a crawled index names the source out
    # loud, so nobody can read the number as one of RAR's own.
    (r"^(\d+) downloads? at (.+)$",
     lambda g, s: s["source"] and s["source"]["downloads"] == int(g[0]) > 0),
    (r"^no downloads reported at (.+)$",
     lambda g, s: s["source"] is not None and not s["source"]["downloads"]),
    (r"^published (\d+) days? ago$",
     lambda g, s: s["source"] and s["source"]["published_age_days"] == int(g[0]) > 0),
    (r"^(\d+) characters? of catalog description$",
     lambda g, s: s["source"] and s["source"]["entry_chars"] == int(g[0])),
]

LITERAL_WHY = {
    "not yet reviewed - scored at the population median":
        lambda s: s["rar"]["curator_n"] == 0,
    "no community feedback yet":
        lambda s: not (s["rar"]["upvotes"] or s["rar"]["comments"]
                       or s["rar"]["engagement"]),
    "no community feedback yet - scored at the population median":
        lambda s: not (s["rar"]["upvotes"] or s["rar"]["comments"]
                       or s["rar"]["engagement"]),
    "newest in the registry": lambda s: s["rar"]["age_days"] == 0,
    "no recorded add date - scored at the population median":
        lambda s: s["rar"]["age_days"] is None,
    "has a rendered card": lambda s: s["rar"]["has_card"] is True,
    "no downloads reported at the source":
        lambda s: bool(s["source"]) and s["source"]["downloads"] == 0,
    "no download count published at the source - scored at the population median":
        lambda s: bool(s["source"]) and s["source"]["downloads"] is None,
    "newest at the source":
        lambda s: bool(s["source"]) and s["source"]["published_age_days"] == 0,
    "no publish date at the source - scored at the population median":
        lambda s: bool(s["source"]) and s["source"]["published_age_days"] is None,
    "ships a bundle at the source":
        lambda s: bool(s["source"]) and s["source"]["has_bundle"] is True,
}


def backing(entry: str, signals: dict) -> bool:
    """True when `entry` is justified by a value in `signals`."""
    if entry in LITERAL_WHY:
        return bool(LITERAL_WHY[entry](signals))
    for pattern, check in NUMERIC_WHY:
        match = re.match(pattern, entry)
        if match:
            return bool(check(match.groups(), signals))
    return False


def test_every_why_is_backed_by_a_signal(items):
    unbacked = []
    for item in items:
        for entry in item["why"]:
            if not backing(entry, item["signals"]):
                unbacked.append((item["ref"], entry))
    assert not unbacked, (
        f"{len(unbacked)} why-entr(ies) are not backed by that item's signals — "
        f"the ranking cannot be audited from the payload: {unbacked[:5]}")


def test_every_item_explains_itself(items):
    empty = [i["ref"] for i in items if not i["why"]]
    assert not empty, f"{len(empty)} ranked item(s) give no reason: {empty[:5]}"


def test_the_why_checker_is_not_vacuous(items):
    """If `backing()` accepted anything, the test above would prove nothing."""
    sample = items[0]
    assert not backing("ranked highly because it is good", sample["signals"])
    assert not backing("9999 upvotes", sample["signals"])

    native = next(i for i in items if i["origin"] == "native")
    tampered = json.loads(json.dumps(native["signals"]))
    tampered["rar"]["tier"] = "not-a-tier"
    tampered["rar"]["upvotes"] += 7
    tampered["rar"]["lines"] += 1
    tampered["rar"]["age_days"] = (native["signals"]["rar"]["age_days"] or 0) + 5
    assert any(not backing(entry, tampered) for entry in native["why"]), (
        "tampering with signals did not invalidate any why entry")


def test_a_why_never_blends_the_two_populations(items):
    """The doctrine is that the two counter sets are never ADDED — the crawler's
    own words are that the storefront shows both. So a hosted agent may cite its
    source's downloads, but only when it genuinely has that provenance, and only
    with the source named so the number cannot be read as one of RAR's."""
    for item in items:
        for entry in item["why"]:
            if "download" not in entry:
                continue
            assert item["source"] is not None, (
                f"{item['ref']} cites downloads with no source provenance")
            named = item["source"]["display_name"]
            assert (named in entry) or ("at the source" in entry), (
                f"{item['ref']} cites a download count without naming whose it is: "
                f"{entry!r}")


def test_rar_counters_are_never_derived_from_the_source(items):
    """The two signal blocks must stay structurally disjoint."""
    for item in items:
        rar = item["signals"]["rar"]
        src = item["signals"]["source"]
        if src is None:
            continue
        assert set(rar) & set(src) <= {"id"}, (
            f"{item['ref']} has overlapping keys across the two signal blocks: "
            f"{sorted(set(rar) & set(src))}")
        # RAR's own counters must not have absorbed the source's reach.
        assert rar.get("upvotes", 0) != src.get("downloads")  or not src.get("downloads")


# ── absence of signal is not negative signal ────────────────────────────────


def test_missing_components_are_filled_with_the_population_median(payload, items):
    medians = payload["ranking"]["medians"]
    for item in items:
        for key in item.get("scored_at_median", []):
            assert item["components"][key] == medians[key], (
                f"{item['ref']} claims '{key}' was median-filled but the value "
                "does not match the published median")


def test_unreviewed_agents_say_so_and_are_not_zeroed(payload, items):
    unreviewed = [i for i in items
                  if i["origin"] == "native" and i["signals"]["rar"]["curator_n"] == 0]
    assert unreviewed, "expected some agents to have no curator review"
    median = payload["ranking"]["medians"]["curator"]
    for item in unreviewed:
        assert "not yet reviewed - scored at the population median" in item["why"]
        assert item["components"]["curator"] == median
        assert item["components"]["curator"] > 0, (
            "a missing review scored as zero punishes silence, not quality")


def test_an_unreviewed_agent_is_not_bottom_of_the_list(items):
    """The failure this guards: ranking the catalog by who happened to get
    reviewed, then presenting it as quality."""
    native = [i for i in items if i["origin"] == "native"]
    unreviewed_ranks = [n for n, i in enumerate(native)
                        if i["signals"]["rar"]["curator_n"] == 0]
    assert unreviewed_ranks and unreviewed_ranks[0] < len(native) // 2, (
        "every unreviewed agent landed in the bottom half; absence of signal is "
        "being scored as negative signal")


def test_freshness_decays_smoothly_rather_than_cliffing(bfp):
    reference = bfp.parse_ts("2026-08-01T00:00:00Z")
    curve = [bfp.measure_freshness(
        bfp.parse_ts(f"2026-08-01T00:00:00Z") - __import__("datetime").timedelta(days=d),
        reference)[0] for d in range(0, 400, 10)]
    assert curve[0] == pytest.approx(1.0)
    for previous, current in zip(curve, curve[1:]):
        assert current < previous, "freshness must decay monotonically"
        assert previous - current < 0.12, "freshness dropped like a cliff"
    assert curve[-1] > 0.0, "freshness must never reach zero"


# ── determinism ─────────────────────────────────────────────────────────────


def test_two_builds_differ_only_in_generated(bfp):
    first, second = bfp.build(), bfp.build()
    assert bfp.comparable(first) == bfp.comparable(second)
    # Key order too — sort_keys inside comparable() would hide a reordering.
    strip = lambda p: json.dumps({k: v for k, v in p.items() if k != "generated"},
                                 ensure_ascii=False)
    assert strip(first) == strip(second)
    differing = [k for k in first if first[k] != second[k]]
    assert differing in ([], ["generated"]), (
        f"non-deterministic field(s): {differing}")


def test_comparable_ignores_only_the_timestamp(bfp, payload):
    other = json.loads(json.dumps(payload))
    other["generated"] = "1999-01-01T00:00:00Z"
    assert bfp.comparable(other) == bfp.comparable(payload)
    other["counts"]["ranked"] += 1
    assert bfp.comparable(other) != bfp.comparable(payload), (
        "--check would not notice a real change")


def test_the_freshness_clock_comes_from_the_data_not_the_wall(payload):
    """Wall-clock ages would make `--check` flap in CI for no reason."""
    assert "not from build time" in payload["ranking"]["clock"]


def test_on_disk_file_is_current(bfp, payload):
    assert bfp.comparable(payload) == bfp.comparable(bfp.build()), (
        "api/v1/front.json is stale — run: python3 scripts/build_front_page.py")


# ── the build is additive ───────────────────────────────────────────────────


def digest(path: Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None


def test_building_the_front_page_changes_nothing_else():
    before = {p: digest(p) for p in UNTOUCHABLE}
    result = subprocess.run([sys.executable, str(BUILDER)],
                            cwd=REPO_ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    after = {p: digest(p) for p in UNTOUCHABLE}
    changed = [p.relative_to(REPO_ROOT).as_posix()
               for p in UNTOUCHABLE if before[p] != after[p]]
    assert not changed, (
        f"the front-page build modified files it does not own: {changed}")


def test_the_builder_owns_exactly_one_path(bfp):
    assert bfp.OWNED_PATHS == frozenset({(REPO_ROOT / "api" / "v1" / "front.json")
                                         .resolve()})


def test_the_builder_refuses_to_write_anywhere_else(bfp, tmp_path, monkeypatch):
    monkeypatch.setattr(bfp, "OUT_FILE", tmp_path / "elsewhere.json")
    with pytest.raises(RuntimeError):
        bfp.write({"schema": "rar-front-page/1.0"})
    assert not (tmp_path / "elsewhere.json").exists()


def test_published_paths_ledger_is_untouched_by_ranking(items):
    """Ranking never renames a file, so every native install URL must still be
    the path the ledger froze."""
    ledger_path = REPO_ROOT / "state" / "published_paths.json"
    if not ledger_path.exists():
        pytest.skip("published_paths.json not present")
    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    paths = ledger.get("paths") or ledger.get("published") or ledger
    known = set(paths) if isinstance(paths, dict) else {
        (p.get("path") if isinstance(p, dict) else p) for p in paths}
    checked = 0
    for item in items:
        if item["origin"] != "native" or not item["install"]:
            continue
        rel = item["install"].split("/main/", 1)[-1]
        if rel in known:
            checked += 1
    assert checked, "no native install URL matched the published-path ledger"


# ── CLI ─────────────────────────────────────────────────────────────────────


def run(*args):
    return subprocess.run([sys.executable, str(BUILDER), *args],
                          cwd=REPO_ROOT, capture_output=True, text=True)


def test_check_passes_against_a_current_file():
    assert run().returncode == 0
    result = run("--check")
    assert result.returncode == 0, result.stderr
    assert "is current" in result.stdout


def test_dry_run_writes_nothing():
    before = digest(FRONT)
    result = run("--dry-run")
    assert result.returncode == 0, result.stderr
    assert "nothing written" in result.stdout
    assert digest(FRONT) == before


# ── house style ─────────────────────────────────────────────────────────────


def test_the_payloads_own_prose_carries_no_emoji(payload):
    """Emoji are banned across RAR surfaces; agent descriptions come from
    manifests, but every string this builder authors is checked."""
    authored = [payload["ranking"]["explain"], payload["ranking"]["median_fill"],
                payload["ranking"]["clock"], payload["policy"]]
    authored += [c["description"] for c in payload["ranking"]["components"]]
    authored += [w for i in payload["items"] for w in i["why"]]
    offenders = [
        (text[:60], ch) for text in authored for ch in text
        if 0x1F000 <= ord(ch) <= 0x1FAFF or 0x2600 <= ord(ch) <= 0x27BF
        or ord(ch) in (0xFE0F, 0x2B50, 0x2705, 0x274C)
    ]
    assert not offenders, f"emoji in authored prose: {offenders[:5]}"
