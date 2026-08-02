"""
Tests for the permanent URL contract — CONSTITUTION.md Article XXIII.

Published agent paths are a public contract. People install agents by URL and
those URLs live in other people's brainstems, scripts and products. A rename is
a silent 404 on someone else's machine. These tests prove the gate that stops
that from happening actually stops it.

The violation tests run against a throwaway sandbox, never the real repository.
A test that guards against deleting agent files must not be capable of leaving
one deleted — an interrupted run would otherwise put the repo in exactly the
state the article forbids.
"""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "check_url_stability.py"
LEDGER = REPO_ROOT / "state" / "published_paths.json"

PROBE_AGENT = '''"""A throwaway agent used only to exercise the stability gate."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@probe/probe_agent",
    "version": "1.0.0",
    "display_name": "Probe",
    "description": "Test fixture.",
    "author": "tests",
    "tags": ["test"],
    "category": "core",
}
'''


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    """A self-contained repo with one published agent and a matching ledger.

    Yields (module, agents_dir). Nothing here touches the real repository, so a
    violation test can mutate freely without risk.
    """
    spec = importlib.util.spec_from_file_location("_url_stability_probe", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    agents_dir = tmp_path / "agents"
    (agents_dir / "@probe").mkdir(parents=True)
    (agents_dir / "@probe" / "probe_agent.py").write_text(PROBE_AGENT, encoding="utf-8")

    ledger_path = tmp_path / "state" / "published_paths.json"
    ledger_path.parent.mkdir(parents=True)

    monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(mod, "AGENTS_DIR", agents_dir)
    monkeypatch.setattr(mod, "LEDGER_PATH", ledger_path)

    # Publish the probe, freezing its path exactly as CI does on main.
    ledger = mod.load_ledger()
    mod.do_update(ledger)
    mod.save_ledger(ledger)

    baseline = mod.do_check(mod.load_ledger())
    assert baseline["ok"], "sandbox should start in a passing state"

    return mod, agents_dir


def run_check(*args):
    """Run the real checker against the real repo and return (returncode, output)."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=REPO_ROOT, capture_output=True, text=True, timeout=300,
    )
    return result.returncode, result.stdout + result.stderr


@pytest.mark.smoke
@pytest.mark.integrity
def test_ledger_exists_and_is_wellformed():
    """The ledger is the record of what we have promised to keep serving."""
    assert LEDGER.exists(), (
        "state/published_paths.json is missing. It is the append-only record of "
        "every agent URL we have promised to keep alive. Rebuild it with "
        "`python scripts/check_url_stability.py --update`."
    )
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    assert data["schema"] == "rar-published-paths/1.0"
    assert isinstance(data["paths"], dict)
    assert data["paths"], "the ledger records no published paths at all"
    assert data["count"] == len(data["paths"])

    for path, entry in data["paths"].items():
        assert path.startswith("agents/"), f"ledger holds a non-agent path: {path}"
        assert path.endswith(".py"), f"ledger holds a non-.py path: {path}"
        assert "first_seen" in entry, f"{path} has no first_seen date"


@pytest.mark.smoke
@pytest.mark.integrity
def test_all_published_urls_still_resolve():
    """The headline guarantee: nothing we ever published has gone missing."""
    code, output = run_check()
    assert code == 0, (
        "THE PERMANENT URL CONTRACT IS BROKEN — a published agent path no longer "
        "resolves. Every one of these is a live 404 for someone who already "
        f"installed it. Restore the file at its original path.\n\n{output}"
    )


@pytest.mark.integrity
def test_ledger_covers_every_agent_on_disk():
    """New agents must be recorded, or their paths are not yet protected."""
    code, output = run_check()
    assert "not yet in the ledger" not in output, (
        "Agents exist on disk that are not recorded in the permanent URL ledger, "
        "so nothing is stopping a future PR from renaming them. Run "
        f"`python scripts/check_url_stability.py --update`.\n\n{output}"
    )


@pytest.mark.integrity
def test_rename_is_detected(sandbox):
    """A rename must fail the gate — this is the npm-breaking move."""
    mod, agents_dir = sandbox
    victim = agents_dir / "@probe" / "probe_agent.py"

    victim.rename(victim.with_name("probe_renamed_agent.py"))

    result = mod.do_check(mod.load_ledger())
    assert not result["ok"], "renaming a published agent did NOT fail the check"
    assert len(result["missing"]) == 1
    assert result["missing"][0]["path"].endswith("probe_agent.py")
    # The checker should trace where it went, so the fix is obvious.
    assert result["missing"][0]["likely_moved_to"], (
        "checker did not report where the renamed file moved to"
    )


@pytest.mark.integrity
def test_deletion_is_detected(sandbox):
    """Deleting a published agent must fail — deprecate with a label instead."""
    mod, agents_dir = sandbox
    (agents_dir / "@probe" / "probe_agent.py").unlink()

    result = mod.do_check(mod.load_ledger())
    assert not result["ok"], "deleting a published agent did NOT fail the check"
    assert len(result["missing"]) == 1
    assert not result["missing"][0]["likely_moved_to"], (
        "a deleted file should not report a new location"
    )


@pytest.mark.integrity
def test_manifest_rename_is_detected(sandbox):
    """The manifest name is the callable tool ID — changing it breaks callers."""
    mod, agents_dir = sandbox
    victim = agents_dir / "@probe" / "probe_agent.py"
    victim.write_text(
        victim.read_text(encoding="utf-8").replace(
            '"@probe/probe_agent"', '"@probe/renamed_tool_id"'
        ),
        encoding="utf-8",
    )

    result = mod.do_check(mod.load_ledger())
    assert not result["ok"], "changing a manifest name did NOT fail the check"
    assert result["renamed_manifest"][0]["was"] == "@probe/probe_agent"
    assert result["renamed_manifest"][0]["now"] == "@probe/renamed_tool_id"


@pytest.mark.integrity
def test_edit_in_place_is_allowed(sandbox):
    """Editing an agent without moving it is explicitly permitted."""
    mod, agents_dir = sandbox
    victim = agents_dir / "@probe" / "probe_agent.py"
    victim.write_text(
        victim.read_text(encoding="utf-8").replace('"1.0.0"', '"2.0.0"')
        + "\n# behaviour improved in place\n",
        encoding="utf-8",
    )

    result = mod.do_check(mod.load_ledger())
    assert result["ok"], (
        "editing an agent in place must NOT fail the check — that is how "
        "agents are maintained"
    )

