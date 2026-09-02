"""RAPP/1 agent.py <-> Toasted SKILL.md conversion contract."""

from __future__ import annotations

import ast
import base64
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = (
    ROOT / "scout" / "starter" / "skills" / "rapp-agent-converter"
)
CLI = SKILL_DIR / "scripts" / "toast.py"
CORE = SKILL_DIR / "scripts" / "_toaster.py"
PINNED_CORE_SHA256 = (
    "d340043178aa4160f76a179b8b1086971e09207b212aff2ab2c0752b69173e17"
)
RAPPID = re.compile(
    r"^rappid:@[a-z0-9]+(?:-[a-z0-9]+)*/"
    r"[a-z0-9]+(?:-[a-z0-9]+)*:[0-9a-f]{64}$"
)
CAPSULE = re.compile(r"<!--\s*rci-capsule:v1:([A-Za-z0-9+/=]+)\s*-->")


def run_json(*args: str) -> dict:
    result = subprocess.run(
        [sys.executable, str(CLI), *map(str, args)],
        capture_output=True,
        text=True,
        timeout=90,
    )
    assert result.returncode == 0, result.stderr
    return json.loads(result.stdout)


def run_failure(*args: str) -> subprocess.CompletedProcess:
    result = subprocess.run(
        [sys.executable, str(CLI), *map(str, args)],
        capture_output=True,
        text=True,
        timeout=90,
    )
    assert result.returncode != 0
    return result


def load_core():
    spec = importlib.util.spec_from_file_location("_converter_test_core", CORE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_converter_source():
    path = ROOT / "scripts" / "rapp_agent_converter_agent.py"
    spec = importlib.util.spec_from_file_location("_converter_source_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def capsule_of(path: Path) -> dict:
    matches = CAPSULE.findall(path.read_text(encoding="utf-8"))
    assert matches
    return json.loads(gzip.decompress(base64.b64decode(matches[-1])))


def manifest_of(path: Path) -> dict:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "__manifest__"
            for target in node.targets
        ):
            return ast.literal_eval(node.value)
    raise AssertionError(f"{path} has no __manifest__")


def identity_agent(rappid: str, *, inherits=True) -> bytes:
    base = "(BasicAgent)" if inherits else ""
    return f'''"""Identity fixture."""

__manifest__ = {{
    "schema": "rapp-agent/1.0",
    "name": "@example/identity",
    "version": "1.0.0",
    "display_name": "IdentityAgent",
    "description": "Identity fixture.",
    "author": "Example",
    "tags": ["identity"],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    "rapp": {{
        "schema": "rapp/1",
        "rappid": "{rappid}",
        "kind": "agent"
    }}
}}

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            self.name = name
            self.metadata = metadata or {{}}


class IdentityAgent{base}:
    def __init__(self):
        self.name = "IdentityAgent"
        self.metadata = {{
            "name": self.name,
            "description": "Identity fixture.",
            "parameters": {{"type": "object", "properties": {{}}}}
        }}
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        return "identity"
'''.encode()


def test_converter_is_part_of_the_default_rapp_plugin():
    marketplace = json.loads(
        (ROOT / ".claude-plugin" / "marketplace.json").read_text()
    )
    [plugin] = marketplace["plugins"]
    assert plugin["skills"] == [
        "./skills/rapp-skills",
        "./skills/rapp-agent-converter",
    ]
    assert (SKILL_DIR / "SKILL.md").is_file()
    assert (SKILL_DIR / "rapp_agent_converter_agent.py").is_file()
    assert (SKILL_DIR / "scripts" / "run_agent.py").is_file()
    assert CLI.is_file()
    assert hashlib.sha256(CORE.read_bytes()).hexdigest() == PINNED_CORE_SHA256


def test_converter_skill_is_itself_rapp1_toasted():
    skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    metadata_line = re.search(r"^metadata:\s*(\{.*\})$", skill, re.MULTILINE)
    assert metadata_line
    metadata = json.loads(metadata_line.group(1))
    assert metadata["default_format"] == "skill"
    assert metadata["toasted"] is True
    assert metadata["normalization_path"] == (
        "raw-skill->rar-agent->toasted-skill"
    )
    assert metadata["rapp"]["schema"] == "rapp/1"
    assert metadata["rapp"]["kind"] == "skill"
    assert RAPPID.fullmatch(metadata["rapp"]["rappid"])

    capsule = capsule_of(SKILL_DIR / "SKILL.md")
    preserved = capsule["preserved"]["agent"]
    restored = gzip.decompress(base64.b64decode(preserved["b64"]))
    assert hashlib.sha256(restored).hexdigest() == preserved["sha256"]
    assert restored == (
        SKILL_DIR / "rapp_agent_converter_agent.py"
    ).read_bytes()


def test_every_published_rar_python_agent_is_convertible():
    converter = load_converter_source()
    registry = json.loads((ROOT / "registry.json").read_text())["agents"]
    failures = []
    for entry in registry:
        source = ROOT / str(entry.get("_file") or "")
        if (
            source.suffix != ".py"
            or not source.is_file()
            or entry.get("name") == "@rapp/basic_agent"
        ):
            continue
        data = source.read_bytes()
        manifest = converter._manifest_from_bytes(data)
        filename = converter._canonical_agent_filename(
            manifest,
            source.name,
        )
        try:
            converter._validate_rar_agent(data, filename)
        except ValueError as error:
            failures.append(f"{entry.get('name')}: {error}")
    assert not failures, "\n".join(failures)


def test_rar_agent_defaults_to_skill_and_restores_exactly(tmp_path):
    original = (ROOT / "agents" / "@rapp" / "ping_agent.py").read_bytes()
    source = tmp_path / "ping_agent.py"
    source.write_bytes(original)
    skill = tmp_path / "ping" / "SKILL.md"

    converted = run_json(str(source), "-o", str(skill))
    assert converted["status"] == "ok"
    assert converted["target_format"] == "skill"
    assert converted["default_format"] == "skill"
    assert converted["transport_fidelity"] == "byte-exact agent restore"
    assert converted["rapp"]["schema"] == "rapp/1"
    assert RAPPID.fullmatch(converted["rapp"]["rappid"])
    assert (skill.parent / source.name).read_bytes() == original

    before = skill.read_bytes()
    repeated = run_json(str(source), "-o", str(skill))
    assert repeated["rapp"]["rappid"] == converted["rapp"]["rappid"]
    assert {item["status"] for item in repeated["artifacts"]} == {"unchanged"}
    assert skill.read_bytes() == before

    restored = tmp_path / "restored_ping_agent.py"
    reverse = run_json(
        "convert",
        str(skill),
        "--to",
        "agent",
        "-o",
        str(restored),
    )
    assert reverse["restored_byte_exact"] is True
    assert restored.read_bytes() == original

    second = run_json(str(skill))
    assert second["already_toasted"] is True
    assert skill.read_bytes() == before


def test_grandfathered_rar_filename_gets_canonical_sidecar(tmp_path):
    original = (ROOT / "agents" / "@kody-w" / "buzzsaw.py").read_bytes()
    source = tmp_path / "buzzsaw.py"
    source.write_bytes(original)
    skill = tmp_path / "buzzsaw" / "SKILL.md"

    converted = run_json(str(source), "-o", str(skill))
    assert converted["status"] == "ok"
    sidecar = skill.parent / "buzzsaw_agent.py"
    assert sidecar.read_bytes() == original

    restored = tmp_path / "restored_buzzsaw_agent.py"
    run_json(str(skill), "--to", "agent", "-o", str(restored))
    assert restored.read_bytes() == original


def test_raw_skill_is_injected_into_agent_then_toasted(tmp_path):
    source = tmp_path / "SKILL.md"
    original = b"""---
name: release-notes
description: Draft release notes from a git log.
author: Example Author
tags: [\"release\", \"writing\"]
---

# Release notes

Turn the supplied git log into concise, user-facing release notes.

## Parameters

```json
{
  \"type\": \"object\",
  \"properties\": {
    \"git_log\": {
      \"type\": \"string\",
      \"description\": \"The git log to summarize.\"
    }
  },
  \"required\": [\"git_log\"]
}
```
"""
    source.write_bytes(original)

    converted = run_json(str(source), "--publisher", "@example")
    assert converted["status"] == "ok"
    assert converted["normalized_through_agent"] is True
    assert converted["source_skill_vaulted"] is True
    assert converted["target_format"] == "skill"
    assert converted["rapp"]["schema"] == "rapp/1"
    assert RAPPID.fullmatch(converted["rapp"]["rappid"])
    assert source.read_bytes() != original

    agent = tmp_path / "release_notes_agent.py"
    assert agent.is_file()
    manifest = manifest_of(agent)
    assert manifest["schema"] == "rapp-agent/1.0"
    assert manifest["name"] == "@example/release_notes"
    assert manifest["display_name"] == "ReleaseNotes"
    assert manifest["dependencies"] == ["@rapp/basic_agent"]
    assert manifest["rapp"]["schema"] == "rapp/1"
    assert manifest["rapp"]["rappid"] == converted["rapp"]["rappid"]

    runtime = subprocess.run(
        [sys.executable, str(agent), '{"git_log":"abc123 add feature"}'],
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert runtime.returncode == 0, runtime.stderr
    assert runtime.stdout.strip()

    verified = run_json("verify", str(source))
    assert verified["rapp1_toasted"] is True
    assert verified["vaulted_agent_valid_rar"] is True
    assert verified["vaulted_source_skill_valid"] is True

    restored_agent = tmp_path / "restored_release_notes_agent.py"
    run_json(
        str(source),
        "--to",
        "agent",
        "-o",
        str(restored_agent),
    )
    assert restored_agent.read_bytes() == agent.read_bytes()

    restored_raw = tmp_path / "SKILL.raw.md"
    run_json(
        "restore-raw",
        str(source),
        "-o",
        str(restored_raw),
    )
    assert restored_raw.read_bytes() == original


def test_out_of_place_raw_conversion_reuses_minted_identity(tmp_path):
    source = tmp_path / "raw" / "SKILL.md"
    source.parent.mkdir()
    original = b"""---
name: portable-note
description: Turn notes into a portable summary.
---

Summarize the supplied notes without dropping facts.
"""
    source.write_bytes(original)
    target = tmp_path / "installed" / "SKILL.md"

    first = run_json(str(source), "-o", str(target), "--publisher", "@example")
    before = target.read_bytes()
    second = run_json(str(source), "-o", str(target), "--publisher", "@example")

    assert source.read_bytes() == original
    assert first["rapp"]["rappid"] == second["rapp"]["rappid"]
    assert {item["status"] for item in second["artifacts"]} == {"unchanged"}
    assert target.read_bytes() == before


def test_metadata_only_toast_is_forced_through_a_rar_agent(tmp_path):
    core = load_core()
    rci = core.blank_rci()
    rci.update({
        "name": "MetadataOnly",
        "slug": "metadata-only",
        "description": "A capsule with flags but no implementation.",
        "instructions": "Return the supplied text.",
    })
    rci["platform"] = {
        "metadata": {
            "default_format": "skill",
            "toasted": True,
            "canonical_agent": "metadata_only_agent.py",
            "rapp": {
                "schema": "rapp/1",
                "rappid": (
                    "rappid:@example/metadata-only:" + "a" * 64
                ),
                "kind": "skill",
            },
        },
    }
    source = tmp_path / "SKILL.md"
    source.write_bytes(core.write_skill(rci))

    converted = run_json(str(source), "--publisher", "@example")
    assert converted["normalized_through_agent"] is True
    agent = tmp_path / "metadata_only_agent.py"
    assert agent.is_file()
    assert manifest_of(agent)["name"] == "@example/metadata_only"
    assert capsule_of(source)["preserved"]["agent"]


def test_legacy_skill_uses_vaulted_agent_identity_as_authority(tmp_path):
    core = load_core()
    agent_rappid = "rappid:@example/identity:" + "a" * 64
    skill_rappid = "rappid:@example/identity:" + "b" * 64
    agent = identity_agent(agent_rappid)
    rci = core.read_agent(agent, "identity_agent.py")
    rci["platform"] = {
        "metadata": {
            "default_format": "skill",
            "toasted": True,
            "canonical_agent": "identity_agent.py",
            "source_format": "agent",
            "source_sha256": hashlib.sha256(agent).hexdigest(),
            "rapp": {
                "schema": "rapp/1",
                "rappid": skill_rappid,
                "kind": "skill",
            },
        },
    }
    legacy = core.write_skill(rci)
    source = tmp_path / "SKILL.md"
    source.write_bytes(legacy)

    converted = run_json(str(source), "--publisher", "@example")
    assert converted["normalized_through_agent"] is True
    assert converted["rapp"]["rappid"] == agent_rappid
    final = capsule_of(source)
    assert final["platform"]["metadata"]["rapp"]["rappid"] == agent_rappid
    restored = gzip.decompress(
        base64.b64decode(final["preserved"]["agent"]["b64"])
    )
    assert restored == agent

    conflicting = tmp_path / "conflicting" / "SKILL.md"
    conflicting.parent.mkdir()
    conflicting.write_bytes(legacy)
    failed = run_failure(
        str(conflicting),
        "--rappid",
        skill_rappid,
        "--publisher",
        "@example",
    )
    assert "conflicts with the vaulted agent identity" in failed.stderr


def test_legacy_non_agent_sidecar_is_replaced_by_valid_rar_agent(tmp_path):
    core = load_core()
    rappid = "rappid:@example/identity:" + "c" * 64
    invalid_agent = identity_agent(rappid, inherits=False)
    rci = core.read_agent(invalid_agent, "identity_agent.py")
    rci["platform"] = {
        "metadata": {
            "default_format": "skill",
            "toasted": True,
            "canonical_agent": "identity_agent.py",
            "rapp": {
                "schema": "rapp/1",
                "rappid": rappid,
                "kind": "skill",
            },
        },
    }
    source = tmp_path / "SKILL.md"
    source.write_bytes(core.write_skill(rci))

    converted = run_json(str(source), "--publisher", "@example")
    assert converted["normalized_through_agent"] is True
    normalized = tmp_path / "identity_agent.py"
    assert normalized.read_bytes() != invalid_agent
    tree = ast.parse(normalized.read_text(encoding="utf-8"))
    agent_class = next(
        node
        for node in tree.body
        if isinstance(node, ast.ClassDef)
        and node.name == "IdentityAgent"
    )
    assert any(
        isinstance(base, ast.Name) and base.id == "BasicAgent"
        for base in agent_class.bases
    )
    assert manifest_of(normalized)["name"] == "@example/identity"


def test_packaged_generic_runner_executes_both_conversion_paths(tmp_path):
    installed = tmp_path / "rapp-agent-converter"
    shutil.copytree(SKILL_DIR, installed)
    runner = installed / "scripts" / "run_agent.py"

    original_agent = (
        ROOT / "agents" / "@rapp" / "ping_agent.py"
    ).read_bytes()
    agent_source = tmp_path / "runner_ping_agent.py"
    agent_source.write_bytes(original_agent)
    agent_skill = tmp_path / "runner-agent" / "SKILL.md"
    agent_run = subprocess.run(
        [
            sys.executable,
            str(runner),
            json.dumps({
                "path": str(agent_source),
                "out": str(agent_skill),
            }),
        ],
        cwd=installed,
        capture_output=True,
        text=True,
        timeout=90,
    )
    assert agent_run.returncode == 0, agent_run.stderr
    assert json.loads(agent_run.stdout)["target_format"] == "skill"
    assert (
        agent_skill.parent / agent_source.name
    ).read_bytes() == original_agent

    raw_skill = tmp_path / "runner-raw" / "SKILL.md"
    raw_skill.parent.mkdir()
    raw_skill.write_text(
        "---\n"
        "name: runner-raw\n"
        "description: Normalize through the packaged runner.\n"
        "---\n\n"
        "Return the supplied input.\n",
        encoding="utf-8",
    )
    raw_run = subprocess.run(
        [
            sys.executable,
            str(runner),
            json.dumps({
                "path": str(raw_skill),
                "publisher": "@example",
            }),
        ],
        cwd=installed,
        capture_output=True,
        text=True,
        timeout=90,
    )
    assert raw_run.returncode == 0, raw_run.stderr
    raw_result = json.loads(raw_run.stdout)
    assert raw_result["normalized_through_agent"] is True
    assert (raw_skill.parent / "runner_raw_agent.py").is_file()
    assert capsule_of(raw_skill)["platform"]["metadata"]["rapp"]["schema"] == (
        "rapp/1"
    )
