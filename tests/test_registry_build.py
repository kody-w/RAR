"""
Test that build_registry.py runs successfully and produces valid output.
"""

import json
import hashlib
import subprocess
import sys
from pathlib import Path

import build_registry

REPO_ROOT = Path(__file__).resolve().parent.parent


def test_registry_build_exits_zero():
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "build_registry.py")],
        capture_output=True, text=True, timeout=180,
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


def test_install_filenames_are_unique_and_flat():
    reg = json.loads((REPO_ROOT / "registry.json").read_text())
    filenames = [a.get("_install_filename") for a in reg.get("agents", []) if a.get("type") != "stub"]
    assert all(name and "/" not in name and "\\" not in name for name in filenames)
    assert len(filenames) == len(set(filenames))


def test_registry_paths_and_hashes_are_platform_neutral():
    reg = json.loads((REPO_ROOT / "registry.json").read_text(encoding="utf-8"))
    for agent in reg.get("agents", []):
        file_path = agent.get("_file", "")
        assert "\\" not in file_path
        if agent.get("type") == "stub":
            continue
        source = REPO_ROOT / file_path
        canonical = source.read_bytes().replace(b"\r\n", b"\n")
        assert agent["_sha256"] == hashlib.sha256(canonical).hexdigest()
        assert agent["_size_kb"] == round(len(canonical) / 1024, 1)


def test_all_publishers_have_tool_safe_runtime_names():
    failures = []
    for path in sorted((REPO_ROOT / "agents").rglob("*_agent.py")):
        if path.name == "basic_agent.py" or "templates" in path.parts or "_sources" in path.parts:
            continue
        manifest = build_registry.extract_manifest(path)
        if manifest is None:
            continue
        for error in build_registry.validate_runtime_contract(path, manifest):
            failures.append(f"{path.relative_to(REPO_ROOT)}: {error}")
    assert not failures, "\n".join(failures)


def test_registry_has_swarms():
    """Registry must include a swarms array."""
    reg = json.loads((REPO_ROOT / "registry.json").read_text())
    assert "swarms" in reg
    assert isinstance(reg["swarms"], list)
    assert len(reg["swarms"]) > 0


def test_registry_exposes_receipt_lifecycle():
    reg = json.loads((REPO_ROOT / "registry.json").read_text())
    assert reg["lifecycle"]["schema"] == "rar-agent-lifecycle/1.0"
    assert reg["lifecycle"]["receipt_schema"] == "rar-receipt/1.0"
    assert isinstance(reg["lifecycle"]["tombstones"], list)
    assert all(
        agent.get("_lifecycle") in {"legacy_active", "notarized"}
        for agent in reg["agents"]
    )
    for agent in reg["agents"]:
        if agent.get("_lifecycle") == "notarized":
            assert agent.get("_receipt", "").startswith("rar_")


def test_missing_receipt_cannot_claim_notarized(tmp_path, monkeypatch):
    monkeypatch.setattr(build_registry, "RECEIPTS_DIR", tmp_path)
    errors = []
    metadata = build_registry._lifecycle_metadata(
        name="@test/example_agent",
        version="1.0.0",
        digest="a" * 64,
        canonical_path="agents/@test/example_agent.py",
        lifecycle_agents={
            "@test/example_agent": {
                "status": "active",
                "version": "1.0.0",
                "sha256": "a" * 64,
                "latest_receipt": "rar_" + ("b" * 64),
            }
        },
        errors=errors,
    )
    assert metadata["_lifecycle"] == "invalid"
    assert errors


def test_tombstone_cannot_coexist_with_active_file(tmp_path, monkeypatch):
    monkeypatch.setattr(build_registry, "RECEIPTS_DIR", tmp_path)
    errors = []
    metadata = build_registry._lifecycle_metadata(
        name="@test/example_agent",
        version="1.0.0",
        digest="a" * 64,
        canonical_path="agents/@test/example_agent.py",
        lifecycle_agents={
            "@test/example_agent": {
                "status": "deleted",
                "version": "1.0.0",
                "sha256": "a" * 64,
                "latest_receipt": "rar_" + ("b" * 64),
            }
        },
        errors=errors,
    )
    assert metadata["_lifecycle"] == "invalid"
    assert any("deleted" in error for error in errors)


def test_tombstone_requires_matching_delete_receipt(tmp_path, monkeypatch):
    monkeypatch.setattr(build_registry, "RECEIPTS_DIR", tmp_path)
    errors = []
    result = build_registry._validated_tombstones({
        "@test/example_agent": {
            "status": "deleted",
            "version": "1.0.0",
            "sha256": "a" * 64,
            "latest_receipt": "rar_" + ("b" * 64),
        }
    }, errors)
    assert result == []
    assert errors


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
