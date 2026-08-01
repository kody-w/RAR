"""
Tests for the permanent URL contract — CONSTITUTION.md Article XXIII.

Published agent paths are a public contract. People install agents by URL and
those URLs live in other people's brainstems, scripts and products. A rename is
a silent 404 on someone else's machine. These tests prove the gate that stops
that from happening actually stops it.
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "check_url_stability.py"
LEDGER = REPO_ROOT / "state" / "published_paths.json"


def run_check(*args):
    """Run the stability checker and return (returncode, stdout)."""
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
def test_rename_is_detected(tmp_path):
    """A rename must fail the gate — this is the npm-breaking move."""
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    victim_rel = sorted(data["paths"])[0]
    victim = REPO_ROOT / victim_rel
    if not victim.exists():
        pytest.skip("ledger head entry not on disk; covered by the resolve test")

    backup = tmp_path / "victim.py"
    shutil.copy2(victim, backup)
    renamed = victim.with_name("zz_renamed_probe_agent.py")

    try:
        victim.rename(renamed)
        code, output = run_check()
        assert code == 1, "renaming a published agent did NOT fail the check"
        assert "NO LONGER RESOLVE" in output
        assert victim_rel in output
    finally:
        if renamed.exists():
            renamed.unlink()
        if not victim.exists():
            shutil.copy2(backup, victim)

    assert victim.exists(), "test failed to restore the agent file"


@pytest.mark.integrity
def test_deletion_is_detected(tmp_path):
    """Deleting a published agent must fail — deprecate with a label instead."""
    data = json.loads(LEDGER.read_text(encoding="utf-8"))
    victim_rel = sorted(data["paths"])[0]
    victim = REPO_ROOT / victim_rel
    if not victim.exists():
        pytest.skip("ledger head entry not on disk; covered by the resolve test")

    backup = tmp_path / "victim.py"
    shutil.copy2(victim, backup)

    try:
        victim.unlink()
        code, output = run_check()
        assert code == 1, "deleting a published agent did NOT fail the check"
        assert "NO LONGER RESOLVE" in output
    finally:
        if not victim.exists():
            shutil.copy2(backup, victim)

    assert victim.exists(), "test failed to restore the agent file"
