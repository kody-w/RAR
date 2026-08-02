"""The published API must agree with the registry it claims to publish.

A stale static API is the worst kind of failure: nothing errors. AIdeate, the
vBrainstem and the grail brainstem keep reading `api/v1/catalog.json` and keep
serving yesterday's registry, silently, until somebody notices an agent is
missing.

That is not hypothetical. The API rebuild lives in `build-registry.yml` behind
`if: github.event_name == 'push'`, so a workflow_dispatch run rebuilds it
without committing, and a push that fails an earlier gate never reaches it. Both
happened. The API sat two versions behind main while every job reported green.

These tests make that state loud. They do not re-derive the API — they assert it
agrees with `registry.json`, which is the invariant that actually matters to a
caller.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY = REPO_ROOT / "registry.json"
CATALOG = REPO_ROOT / "api" / "v1" / "catalog.json"
AUDIENCE_MAP = REPO_ROOT / "api" / "v1" / "audience" / "map.json"
STATUS = REPO_ROOT / "api" / "v1" / "status.json"


def load(path: Path):
    if not path.exists():
        pytest.skip(f"{path.relative_to(REPO_ROOT)} not built")
    return json.loads(path.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def registry_agents():
    return {a["name"]: a for a in load(REGISTRY)["agents"]}


@pytest.fixture(scope="module")
def catalog_agents():
    return {a["name"]: a for a in load(CATALOG)["agents"]}


def test_catalog_covers_every_registered_agent(registry_agents, catalog_agents):
    missing = sorted(set(registry_agents) - set(catalog_agents))
    assert not missing, (
        f"{len(missing)} agent(s) in registry.json but absent from the published "
        f"API — hosts cannot see them: {missing[:5]}. "
        "Run: python scripts/build_static_api.py")


def test_catalog_publishes_nothing_extra(registry_agents, catalog_agents):
    extra = sorted(set(catalog_agents) - set(registry_agents))
    assert not extra, (
        f"{len(extra)} agent(s) published in the API but not in the registry: "
        f"{extra[:5]}")


def test_published_versions_match_the_registry(registry_agents, catalog_agents):
    """A stale version is how a caller installs bytes it did not ask for."""
    drift = [
        f"{name}: registry {reg['version']} vs API {catalog_agents[name]['version']}"
        for name, reg in registry_agents.items()
        if name in catalog_agents
        and catalog_agents[name].get("version") != reg.get("version")
    ]
    assert not drift, (
        f"{len(drift)} version(s) drifted between registry and API: {drift[:5]}. "
        "Run: python scripts/build_static_api.py")


def test_published_paths_match_the_registry(registry_agents, catalog_agents):
    """The API's file pointer is the URL contract's public face."""
    drift = []
    for name, reg in registry_agents.items():
        entry = catalog_agents.get(name)
        if not entry:
            continue
        api_path = (entry.get("source") or {}).get("path") or entry.get("_file")
        if api_path and reg.get("_file") and api_path != reg["_file"]:
            drift.append(f"{name}: {reg['_file']} vs {api_path}")
    assert not drift, f"path drift between registry and API: {drift[:5]}"


def test_audience_map_covers_every_published_agent(catalog_agents):
    """Segmentation fails open, but only if every agent has a verdict."""
    data = load(AUDIENCE_MAP)
    verdicts = data.get("map") or data.get("agents") or data
    if not isinstance(verdicts, dict):
        pytest.skip("audience map shape not recognised")
    missing = sorted(set(catalog_agents) - set(verdicts))
    assert not missing, (
        f"{len(missing)} published agent(s) have no audience verdict: "
        f"{missing[:5]}")


def test_status_endpoint_counts_agree(catalog_agents):
    """status.json is what hosts poll to decide whether to refetch."""
    status = load(STATUS)
    summary = status.get("summary") or {}
    counts = [
        v for k, v in summary.items()
        if k in {"agents", "agent_count", "total_agents"} and isinstance(v, int)
    ]
    for endpoint in status.get("endpoints") or []:
        if isinstance(endpoint, dict) and endpoint.get("name") == "catalog":
            if isinstance(endpoint.get("count"), int):
                counts.append(endpoint["count"])
    assert counts, "status.json reports no agent count for hosts to compare"
    for count in counts:
        assert count == len(catalog_agents), (
            f"status.json reports {count} agents, catalog has "
            f"{len(catalog_agents)} — hosts will not know to refetch")
