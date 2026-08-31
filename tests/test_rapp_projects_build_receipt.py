"""Exact RAPP/1 receipt for the ten-frame RAPP Projects skill build."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from datetime import datetime
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
AGENT = ROOT / "agents" / "@kody-w" / "rapp_projects_agent.py"
RECEIPT = ROOT / "docs" / "rapp-projects-skill-build.rapp.json"
CATALOG = ROOT / "scout" / "catalog" / "catalog.json"
API_RECORD = ROOT / "api" / "v1" / "agent" / "kody-w__rapp_projects.json"
FRONT = ROOT / "api" / "v1" / "front.json"
IDENTITY = "@kody-w/rapp_projects"
FRAME_KEYS = {
    "spec",
    "kind",
    "stream_id",
    "seq",
    "utc",
    "payload",
    "payload_hash",
    "frame_hash",
    "prev",
    "prev_wave",
    "sig",
}
SOURCE_COMMITS = [
    "3f0a4dacbf782b21798e00695c03689dd776272d",
    "5c5f0322218bc68045a3338d15befabd4e33578b",
    "c72e7521be9a7143a28934650963d9b9c480dd11",
    "bb78f67a928eebb8526746429b9c06affad5fcb5",
    "c128767574c7e5d290764e6c6e5d7157b3ecfe46",
    "00dd8de13c549252fa60722058de7cc6e957ed74",
    "90ba975aa831f2e50acd72e41bd0b205d79ed6eb",
    "7d63bcfc271070cff83d5f773ff3f04c1eb4d637",
    "fa28d1f78812d8fcec697fdeb5a2067b0f2efd58",
    "a3391b199669c48572aabdab2087b8c6733f0964",
]


def load_agent_module():
    spec = importlib.util.spec_from_file_location(
        "_rapp_projects_build_receipt",
        AGENT,
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_ten_frame_build_receipt_is_exact_and_linked():
    module = load_agent_module()
    frames = json.loads(RECEIPT.read_text(encoding="utf-8"))

    assert isinstance(frames, list)
    assert len(frames) == 10
    assert [frame["seq"] for frame in frames] == list(range(10))
    assert [frame["payload"]["frame"] for frame in frames] == list(range(1, 11))
    assert [frame["payload"]["source_commit"] for frame in frames] == (
        SOURCE_COMMITS
    )
    assert len({frame["stream_id"] for frame in frames}) == 1
    assert re.fullmatch(
        r"rappid:@rapp/rapp-projects-skill-build:[0-9a-f]{64}:build",
        frames[0]["stream_id"],
    )

    previous = None
    for frame in frames:
        assert set(frame) == FRAME_KEYS
        assert frame["spec"] == "rapp/1"
        assert frame["kind"] == "build.frame"
        assert frame["prev_wave"] is None
        assert frame["sig"] is None
        assert frame["prev"] == (
            None if previous is None else previous["payload_hash"]
        )
        assert frame["payload_hash"] == module.H(
            "rapp/1:particle",
            frame["payload"],
        )
        preimage = {
            key: value
            for key, value in frame.items()
            if key not in {"frame_hash", "sig"}
        }
        assert frame["frame_hash"] == module.H("rapp/1:wave", preimage)
        commit = frame["payload"]["source_commit"]
        exists = subprocess.run(
            ["git", "cat-file", "-e", f"{commit}^{{commit}}"],
            cwd=ROOT,
            capture_output=True,
            timeout=30,
        )
        assert exists.returncode == 0, commit
        committed_at = subprocess.run(
            ["git", "show", "-s", "--format=%cI", commit],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        ).stdout.strip()
        frame_utc = datetime.fromisoformat(
            frame["utc"].replace("Z", "+00:00")
        )
        assert frame_utc >= datetime.fromisoformat(committed_at)
        previous = frame


def test_build_receipt_binds_the_generated_publication():
    frames = json.loads(RECEIPT.read_text(encoding="utf-8"))
    evidence = frames[-1]["payload"]["evidence"]
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    [record] = [
        item for item in catalog["skills"] if item["identity"] == IDENTITY
    ]
    [rapp_skill_record] = [
        item
        for item in catalog["skills"]
        if item["identity"] == "@kody-w/rapp_skill_agent"
    ]
    skill = (
        ROOT
        / "scout"
        / "bundles"
        / record["bundle"]
        / "skills"
        / record["skill_name"]
        / "SKILL.md"
    )

    source_sha256 = hashlib.sha256(
        AGENT.read_bytes().replace(b"\r\n", b"\n")
    ).hexdigest()
    skill_sha256 = hashlib.sha256(skill.read_bytes()).hexdigest()
    api_sha256 = hashlib.sha256(API_RECORD.read_bytes()).hexdigest()
    api = json.loads(API_RECORD.read_text(encoding="utf-8"))
    front = json.loads(FRONT.read_text(encoding="utf-8"))
    [front_record] = [
        item for item in front["items"] if item["ref"] == IDENTITY
    ]
    assert evidence["agent_version"] == "1.0.3"
    assert evidence["source_sha256"] == source_sha256
    assert evidence["skill_sha256"] == skill_sha256
    assert evidence["api_sha256"] == api_sha256
    assert api["version"] == "1.0.3"
    assert front_record["audience"] == evidence["front_audience"] == "both"
    assert record["source_sha256"] == source_sha256
    assert record["skill_sha256"] == skill_sha256
    assert record["source_commit"] == evidence["agent_source_commit"]
    assert evidence["source_tests"] >= 97
    assert evidence["targeted_tests"] >= 98
    assert evidence["publication_release_tests"] >= 179
    assert evidence["integration_tests"] >= 8102
    assert evidence["build_receipt_tests"] == 2
    assert evidence["privacy_mutations"] == 17
    assert evidence["runner_preflight"] == "RAPP_READY"
    assert evidence["transfer_byte_identical"] is True
    assert evidence["artifact_body_in_egg"] is False
    assert evidence["source_verdict"] == "pass"
    assert evidence["import_verdict"] == "pass"
    assert evidence["rapp1_commit"] == (
        "caf6ef276cafa92aa744499af90dc1a28559941a"
    )
    assert evidence["rapp_sdk_sha256"] == (
        "aba04a57390d98276eadd9c7decd821bb53549730daec3491cffee45ada48eb2"
    )
    assert evidence["rapp_skill_version"] == "1.3.1"
    assert evidence["rapp_skill_source_sha256"] == (
        rapp_skill_record["source_sha256"]
    )
    assert evidence["rapp_skill_skill_sha256"] == (
        rapp_skill_record["skill_sha256"]
    )
    assert evidence["rapp_proof"] == "pass"
