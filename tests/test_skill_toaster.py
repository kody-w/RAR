"""Aggregated entries must be real agents, not shells.

The whole point of putting an upstream skill in an agent.py container is that a
caller can invoke it. A container whose perform() returns a blurb and a link is a
bookmark — it fails the one promise the container makes.

These tests pin that: every aggregated agent is callable, takes parameters, binds
its output to what the caller passed, and still points home to its source. They
also pin the toaster's determinism, because the generator's drift gate is only
meaningful if the same input always toasts to the same bytes.
"""

from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
AGG_DIR = REPO_ROOT / "agents" / "@cat-agent-skills"
TOASTER_PATH = REPO_ROOT / "agents" / "@kody-w" / "skill_toaster_agent.py"
GENERATOR_PATH = REPO_ROOT / "scripts" / "generate_aggregated_agents.py"
AGGREGATED_JSON = REPO_ROOT / "state" / "aggregated.json"

AGG_FILES = sorted(AGG_DIR.glob("*_agent.py")) if AGG_DIR.exists() else []


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(f"_m_{path.stem}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def agent_of(mod):
    for obj in vars(mod).values():
        if (isinstance(obj, type) and obj.__module__ == mod.__name__
                and hasattr(obj, "perform")):
            return obj()
    raise AssertionError("no agent class found")


@pytest.fixture(scope="module")
def toaster():
    return load_module(TOASTER_PATH)


@pytest.fixture(scope="module")
def generator():
    return load_module(GENERATOR_PATH)


# ── the toaster engine ──────────────────────────────────────────────────────

def test_toaster_exists():
    assert TOASTER_PATH.exists(), "the toaster engine is missing"


def test_every_rule_is_well_formed(toaster):
    rules = toaster.SkillToasterEngine.RULES
    assert rules, "no archetypes defined"
    for aid, rule in rules.items():
        for key in ("verb", "subject_label", "match", "words", "params",
                    "steps", "checks", "deliverable"):
            assert key in rule, f"{aid} missing {key}"
        assert rule["steps"], f"{aid} has no procedure"
        assert rule["checks"], f"{aid} has no acceptance checks"
        assert "subject" in rule["params"], f"{aid} takes no subject"
        assert len(rule["steps"]) >= 3, f"{aid} procedure is too thin to be useful"


def test_analysis_is_deterministic(toaster):
    item = toaster.DEMO_ITEM
    first = toaster.analyze_skill(item)
    for _ in range(5):
        assert toaster.analyze_skill(item) == first, "analysis is not deterministic"


def test_toast_is_deterministic(toaster):
    item = toaster.DEMO_ITEM
    first = json.dumps(toaster.toast_skill(item), sort_keys=True)
    for _ in range(5):
        assert json.dumps(toaster.toast_skill(item), sort_keys=True) == first


def test_container_version_advances_only_when_bytes_change(generator):
    assert generator.choose_container_version(
        "1.0.0",
        None,
        False,
    ) == "2.0.0"
    assert generator.choose_container_version(
        "1.0.0",
        "2.0.1",
        True,
    ) == "2.0.1"
    assert generator.choose_container_version(
        "1.0.0",
        "2.0.1",
        False,
    ) == "2.0.2"
    assert generator.choose_container_version(
        "1.1.0",
        "2.0.9",
        False,
    ) == "2.1.0"
    published = generator.latest_container_version(None, "2.0.9")
    assert published == "2.0.9"
    assert generator.choose_container_version(
        "1.0.0",
        published,
        False,
    ) == "2.0.10"


def test_generated_version_reads_only_the_manifest(generator):
    source = '''"""Untrusted text.
    "version": "99.0.0",
"""
__manifest__ = {
    "name": "@test/example",
    "version": "2.0.0",
}
'''
    assert generator.generated_version(source) == "2.0.0"
    duplicate = source + '\n__manifest__ = {"version": "99.0.0"}\n'
    assert generator.generated_version(duplicate) is None

    injected = 'text"""; __manifest__ = {"version": "99.0.0"}; """'
    safe = generator.doc_fragment(injected)
    compile(f'"""{safe}"""', "<doc-fragment>", "exec")


def test_analysis_recognises_shape(toaster):
    """A capability whose tags say 'testing/quality' must not toast to prose."""
    result = toaster.analyze_skill(toaster.DEMO_ITEM)
    assert result["archetype"] in {"review", "analyze", "design"}
    assert result["signals"], "classified with no supporting evidence"


def test_unknown_shape_falls_back_not_crashes(toaster):
    result = toaster.analyze_skill({"name": "zzz", "description": "", "tags": []})
    assert result["archetype"] == "general"
    assert result["confidence"] == 0.0


def test_toaster_operations_all_return_text(toaster):
    agent = toaster.SkillToasterEngine()
    ops = agent.metadata["parameters"]["properties"]["operation"]["enum"]
    for op in ops:
        out = agent.perform(operation=op)
        assert isinstance(out, str) and out.strip(), f"{op} returned nothing"


def test_toaster_runs_standalone():
    proc = subprocess.run([sys.executable, str(TOASTER_PATH)],
                          capture_output=True, text=True, timeout=60)
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip()


# ── the toasted agents ──────────────────────────────────────────────────────

def test_aggregated_agents_exist():
    assert AGG_FILES, "no aggregated agents found"


@pytest.mark.parametrize("path", AGG_FILES, ids=lambda p: p.stem)
def test_agent_is_callable_not_a_shell(path):
    """Every operation returns real text, and the agent takes parameters."""
    agent = agent_of(load_module(path))
    props = agent.metadata["parameters"]["properties"]

    assert "operation" in props, "no operation parameter — this is a shell"
    ops = props["operation"]["enum"]
    assert len(ops) >= 2, "a single operation is not an interface"
    assert "subject" in props, "takes no subject — nothing to act on"

    for op in ops:
        out = agent.perform(operation=op)
        assert isinstance(out, str), f"{op} did not return a string"
        assert out.strip(), f"{op} returned an empty string"


@pytest.mark.parametrize("path", AGG_FILES, ids=lambda p: p.stem)
def test_agent_output_is_bound_to_caller_input(path):
    """The output must reflect what the caller asked about, not a fixed blurb."""
    agent = agent_of(load_module(path))
    subject = "the RAR aggregation pipeline"
    out = agent.perform(operation="run", subject=subject)
    assert subject in out, "output ignores the caller's subject"

    other = agent.perform(operation="run", subject="a completely different thing")
    assert out != other, "output does not vary with input — this is a shell"


@pytest.mark.parametrize("path", AGG_FILES, ids=lambda p: p.stem)
def test_agent_does_real_work(path):
    """A procedure and acceptance checks, not a description and a link."""
    agent = agent_of(load_module(path))
    out = agent.perform(operation="run", subject="x")
    assert "Procedure:" in out, "no procedure"
    assert "Acceptance checks:" in out, "no acceptance checks"
    assert "Deliverable:" in out, "no stated deliverable"
    assert len(out.splitlines()) >= 12, "too thin to be a capability"


@pytest.mark.parametrize("path", AGG_FILES, ids=lambda p: p.stem)
def test_agent_still_credits_upstream(path):
    """Toasting must not erase provenance — the source still gets the credit."""
    mod = load_module(path)
    src = mod.__manifest__["source"]
    assert src["aggregated"] is True
    assert src["upstream_url"].startswith("http")

    out = agent_of(mod).perform(operation="describe")
    assert src["upstream_url"] in out, "describe() hides the source"
    assert src["source_name"] in out


@pytest.mark.parametrize("path", AGG_FILES, ids=lambda p: p.stem)
def test_container_version_is_distinct_from_upstream(path):
    """Container immutability requires RAR's version to be its own.

    build_registry.check_version_immutability forbids republishing different
    content under a published version. The container therefore carries its own
    version while recording upstream's verbatim.
    """
    m = load_module(path).__manifest__
    assert re.fullmatch(r"\d+\.\d+\.\d+", m["version"])
    upstream = m["source"]["upstream_version"]
    assert re.fullmatch(r"\d+\.\d+\.\d+", upstream)
    assert int(m["version"].split(".")[0]) > int(upstream.split(".")[0]), (
        "container version must outrank upstream so a toaster change can ship "
        "without violating content immutability")


def test_every_aggregated_item_has_an_agent():
    """Indexing something and never toasting it leaves a hole in the catalog."""
    if not AGGREGATED_JSON.exists():
        pytest.skip("no aggregated snapshot")
    items = json.loads(AGGREGATED_JSON.read_text()).get("items", [])
    assert len(AGG_FILES) == len(items), (
        f"{len(items)} indexed entries but {len(AGG_FILES)} agents")


def test_generator_reports_no_drift():
    """Regeneration must be byte-stable, or the drift gate means nothing."""
    proc = subprocess.run(
        [sys.executable, "scripts/generate_aggregated_agents.py", "--check"],
        cwd=REPO_ROOT, capture_output=True, text=True, timeout=300)
    assert proc.returncode == 0, proc.stdout + proc.stderr
