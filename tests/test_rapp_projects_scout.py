"""Projection contract for the RAPP Projects Scout skill and workflow."""

from __future__ import annotations

import base64
import gzip
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCOUT = ROOT / "scout"
IDENTITY = "@kody-w/rapp_projects"
SKILL_NAME = "rar-kody-w-rapp-projects"
SOURCE = ROOT / "agents" / "@kody-w" / "rapp_projects_agent.py"
CATALOG_PATH = SCOUT / "catalog" / "catalog.json"
RAW_PREFIX = "https://raw.githubusercontent.com/kody-w/RAR/main/scout/"
CAPSULE = re.compile(r"<!--\s*rci-capsule:v1:([A-Za-z0-9+/=]+)\s*-->")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def lf(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def primary_skill_dir(record: dict) -> Path:
    if record["bundle"] == "starter":
        return SCOUT / "starter" / "skills" / record["skill_name"]
    return (
        SCOUT
        / "bundles"
        / record["bundle"]
        / "skills"
        / record["skill_name"]
    )


def restore_toaster_agent(skill: bytes) -> bytes:
    matches = CAPSULE.findall(skill.decode("utf-8"))
    assert matches, "generated SKILL.md is missing its Toaster capsule"
    capsule = json.loads(gzip.decompress(base64.b64decode(matches[-1])))
    preserved = capsule["preserved"]["agent"]
    restored = gzip.decompress(base64.b64decode(preserved["b64"]))
    assert sha256(restored) == preserved["sha256"]
    return restored


def test_rapp_projects_scout_projection():
    quickstart = (
        ROOT / "docs" / "rapp-projects-skill.md"
    ).read_text(encoding="utf-8")
    assert "<GENERATED_" not in quickstart

    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    registry = json.loads(
        (ROOT / "registry.json").read_text(encoding="utf-8")
    )["agents"]
    [registry_entry] = [
        item for item in registry if item["name"] == IDENTITY
    ]
    [record] = [
        item for item in catalog["skills"] if item["identity"] == IDENTITY
    ]

    assert record["skill_name"] == SKILL_NAME
    assert record["linked_agent"] == SOURCE.name
    assert "rapplication" in registry_entry["tags"]

    skill_dir = primary_skill_dir(record)
    skill_path = skill_dir / "SKILL.md"
    linked_agent = skill_dir / SOURCE.name
    lock_path = skill_dir / "rapp" / "agent.lock.json"
    runner = skill_dir / "scripts" / "run_agent.py"
    assert skill_path.is_file()
    assert linked_agent.is_file()
    assert lock_path.is_file()
    assert runner.is_file()

    source_bytes = SOURCE.read_bytes()
    skill_bytes = skill_path.read_bytes()
    linked_bytes = linked_agent.read_bytes()
    assert linked_bytes == source_bytes
    assert b"## Parameters" in skill_bytes
    assert re.search(
        rf'^name:\s*"{re.escape(SKILL_NAME)}"$',
        skill_bytes.decode("utf-8"),
        re.MULTILINE,
    )
    assert restore_toaster_agent(skill_bytes) == source_bytes

    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    source_digest = sha256(lf(source_bytes))
    assert lock["agent"] == IDENTITY
    assert lock["agent_file"] == SOURCE.name
    assert lock["agent_sha256"] == source_digest
    assert lock["digest_algorithm"] == "sha256-lf-v1"
    assert record["source_sha256"] == source_digest
    assert registry_entry["_sha256"] == source_digest
    assert record["skill_sha256"] == sha256(skill_bytes)

    tool = subprocess.run(
        [sys.executable, str(SOURCE), "--tool"],
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert tool.returncode == 0, tool.stderr
    tool_contract = json.loads(tool.stdout)["function"]["parameters"]
    assert record["parameters"] == tool_contract
    assert record["parameters"]["anyOf"] == [
        {"required": ["operation"]},
        {"required": ["action"]},
    ]

    for file_record in record["files"]:
        generated = skill_dir / file_record["path"]
        assert generated.is_file(), generated
        assert sha256(generated.read_bytes()) == file_record["sha256"]
        assert file_record["url"].startswith(RAW_PREFIX)
        assert not file_record["url"].startswith("file:")

    preflight = subprocess.run(
        [sys.executable, str(runner), "--preflight"],
        cwd=skill_dir,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert preflight.returncode == 0, preflight.stderr
    assert preflight.stdout.strip().startswith(
        ("RAPP_READY", "RAPP_DEGRADED:")
    )

    [workflow_record] = [
        item for item in catalog["workflows"]
        if item["identity"] == IDENTITY
    ]
    workflow_root = SCOUT / "workflows" / SKILL_NAME
    workflow_path = workflow_root / f"workflow--{SKILL_NAME}.json"
    expected_id = sha256(
        f"rar-scout-workflow/1\n{IDENTITY}".encode("utf-8")
    )[:16]
    assert workflow_record["skill_name"] == SKILL_NAME
    assert workflow_record["file"] == workflow_path.name
    assert workflow_record["id"] == expected_id
    assert workflow_path.is_file()
    workflow_skill = workflow_root / "skills" / SKILL_NAME
    assert (workflow_skill / "SKILL.md").read_bytes() == skill_bytes
    assert (workflow_skill / SOURCE.name).read_bytes() == source_bytes
    assert (workflow_skill / "rapp" / "agent.lock.json").read_bytes() == (
        lock_path.read_bytes()
    )
    assert (workflow_skill / "scripts" / "run_agent.py").read_bytes() == (
        runner.read_bytes()
    )

    workflow = json.loads(workflow_path.read_text(encoding="utf-8"))
    assert workflow["id"] == expected_id
    assert workflow["skillNames"] == [SKILL_NAME]

    published = json.dumps(
        {"skill": record, "workflow": workflow_record},
        sort_keys=True,
    )
    assert "file://" not in published
    assert str(ROOT) not in published
