"""
Test that build_registry.py runs successfully and produces valid output.
"""

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_registry_build_exits_zero():
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "build_registry.py")],
        capture_output=True, text=True, timeout=60,
        cwd=str(REPO_ROOT),
    )
    assert result.returncode == 0, (
        f"build_registry.py failed (exit {result.returncode})\n"
        f"stdout: {result.stdout[:500]}\n"
        f"stderr: {result.stderr[:500]}"
    )


def test_no_seed_collisions():
    """Every agent in the registry must have a unique seed."""
    reg = json.loads((REPO_ROOT / "registry.json").read_text())
    seen = {}
    for a in reg.get("agents", []):
        seed = a.get("_seed")
        if seed is None:
            continue
        assert seed not in seen, (
            f"Seed collision: {a['name']} and {seen[seed]} "
            f"both have seed {seed}"
        )
        seen[seed] = a["name"]


def test_registry_has_swarms():
    """Registry must include a swarms array."""
    reg = json.loads((REPO_ROOT / "registry.json").read_text())
    assert "swarms" in reg
    assert isinstance(reg["swarms"], list)
    assert len(reg["swarms"]) > 0


def test_no_seed_collisions_across_agents_and_swarms():
    """Seeds must be unique across both agents AND converged swarms."""
    reg = json.loads((REPO_ROOT / "registry.json").read_text())
    seen = {}
    for item in reg.get("agents", []) + reg.get("swarms", []):
        seed = item.get("_seed")
        if seed is None:
            continue
        assert seed not in seen, (
            f"Seed collision: {item['name']} and {seen[seed]} "
            f"both have seed {seed}"
        )
        seen[seed] = item["name"]
