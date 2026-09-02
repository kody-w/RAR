"""RAPP/1 agent.py <-> Toasted SKILL.md conversion contract."""

from __future__ import annotations

import ast
import base64
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

import pytest


ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = (
    ROOT / "scout" / "starter" / "skills" / "rapp-agent-converter"
)
CLI = SKILL_DIR / "scripts" / "toast.py"
PINNED_CORE_SHA256 = (
    "d340043178aa4160f76a179b8b1086971e09207b212aff2ab2c0752b69173e17"
)
RAPPID = re.compile(
    r"^rappid:@[a-z0-9]+(?:-[a-z0-9]+)*/"
    r"[a-z0-9]+(?:-[a-z0-9]+)*:[0-9a-f]{64}$"
)
CAPSULE = re.compile(r"<!--\s*rci-capsule:v1:([A-Za-z0-9+/=]+)\s*-->")


@pytest.fixture(autouse=True)
def isolated_converter_homes(tmp_path, monkeypatch):
    monkeypatch.setenv("RAPP_DATA_HOME", str(tmp_path / ".rapp-data"))
    monkeypatch.setenv("RAPP_CACHE_HOME", str(tmp_path / ".rapp-cache"))
    monkeypatch.setenv("RAPP_CONFIG_HOME", str(tmp_path / ".rapp-config"))
    monkeypatch.setenv("RAPP_LOCK_HOME", str(tmp_path / ".rapp-locks"))


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
    module = load_converter_skill()
    return module._load_core()


def load_converter_skill():
    path = SKILL_DIR / "rapp_agent_converter_agent.py"
    spec = importlib.util.spec_from_file_location("_converter_skill_test", path)
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


def load_converter_source():
    path = ROOT / "scripts" / "rapp_agent_converter_agent.py"
    spec = importlib.util.spec_from_file_location("_converter_source_test", path)
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
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


def identity_agent(
    rappid: str,
    *,
    inherits=True,
    package="identity",
    runtime="IdentityAgent",
) -> bytes:
    base = "(BasicAgent)" if inherits else ""
    return f'''"""Identity fixture."""

__manifest__ = {{
    "schema": "rapp-agent/1.0",
    "name": "@example/{package}",
    "version": "1.0.0",
    "display_name": "{runtime}",
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


class {runtime}{base}:
    def __init__(self):
        self.name = "{runtime}"
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
    assert not (SKILL_DIR / "scripts" / "_toaster.py").exists()
    converter = load_converter_skill()
    embedded = gzip.decompress(
        base64.b64decode(converter.EMBEDDED_TOASTER_GZIP_BASE64)
    )
    assert hashlib.sha256(embedded).hexdigest() == PINNED_CORE_SHA256
    assert CLI.stat().st_size < 1000


def test_converter_ci_runs_on_linux_macos_and_windows():
    workflow = (
        ROOT / ".github" / "workflows" / "build-scout-exports.yml"
    ).read_text(encoding="utf-8")
    assert "ubuntu-latest, macos-latest, windows-latest" in workflow
    assert "publish:" in workflow
    assert "needs: build" in workflow
    assert "Rebuild after compatibility matrix" in workflow
    assert "github.ref == 'refs/heads/main'" in workflow
    assert 'git rev-parse origin/main' in workflow
    assert "git pull --rebase" not in workflow


def test_converter_skill_is_itself_rapp1_toasted():
    skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    metadata_line = re.search(r"^metadata:\s*(\{.*\})$", skill, re.MULTILINE)
    assert metadata_line
    metadata = json.loads(metadata_line.group(1))
    assert metadata["default_format"] == "skill"
    assert metadata["canonical_format"] == "skill"
    assert metadata["grail_record"] is True
    assert metadata["materializes"] == ["agent"]
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
    assert run_json("verify", str(SKILL_DIR / "SKILL.md"))["status"] == "ok"


def test_self_contained_converter_agent_needs_no_skill_sidecars(tmp_path):
    standalone = tmp_path / "rapp_agent_converter_agent.py"
    standalone.write_bytes(
        (SKILL_DIR / "rapp_agent_converter_agent.py").read_bytes()
    )
    source = tmp_path / "raw" / "SKILL.md"
    source.parent.mkdir()
    source.write_text(
        "---\n"
        "name: self-contained\n"
        "description: Convert with one agent file.\n"
        "---\n\n"
        "Return the input.\n",
        encoding="utf-8",
    )
    result = subprocess.run(
        [
            sys.executable,
            str(standalone),
            str(source),
            "--publisher",
            "@example",
        ],
        capture_output=True,
        text=True,
        timeout=90,
        env=os.environ.copy(),
    )
    assert result.returncode == 0, result.stderr
    converted = json.loads(result.stdout)
    assert Path(converted["canonical_grail"]).is_file()
    assert not (standalone.parent / "_toaster.py").exists()


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


def test_public_agent_resolver_ignores_internal_perform_helpers():
    converter = load_converter_skill()
    core = converter._load_core()
    source = (
        ROOT / "agents" / "@kody-w" / "copilot_studio_deploy_agent.py"
    )
    record = converter._read_public_agent(
        core,
        source.read_bytes(),
        source.name,
    )
    assert record["name"] == "CopilotStudioDeploy"
    assert "engine" in record["parameters"]["properties"]
    assert record["impl"]["class"] == "CopilotStudioDeployAgent"


def test_rar_agent_defaults_to_skill_and_restores_exactly(tmp_path):
    original = (ROOT / "agents" / "@rapp" / "ping_agent.py").read_bytes()
    source = tmp_path / "ping_agent.py"
    source.write_bytes(original)
    skill = tmp_path / "ping" / "SKILL.md"

    converted = run_json(str(source), "-o", str(skill))
    assert converted["status"] == "ok"
    assert converted["target_format"] == "skill"
    assert converted["canonical_grail"] == str(skill)
    assert converted["selected_artifact"] == str(skill)
    assert converted["transport_fidelity"] == "byte-exact agent restore"
    assert converted["rapp"]["schema"] == "rapp/1"
    assert RAPPID.fullmatch(converted["rapp"]["rappid"])
    assert not (skill.parent / source.name).exists()

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
    assert not sidecar.exists()

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
    assert converted["source_unchanged"] is True
    assert source.read_bytes() == original
    grail = Path(converted["canonical_grail"])
    assert grail.is_file()
    pinned = load_core()
    pinned_record = pinned.read_skill(grail.read_bytes(), str(grail))
    assert pinned.restore(pinned_record, "agent") is not None

    agent = tmp_path / "release_notes_agent.py"
    assert not agent.exists()
    run_json(
        "materialize",
        str(grail),
        "-o",
        str(agent),
    )
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

    verified = run_json("verify", str(grail))
    assert verified["rapp1_toasted"] is True
    assert verified["vaulted_agent_valid_rar"] is True
    assert verified["vaulted_source_skill_valid"] is True

    restored_agent = tmp_path / "restored_release_notes_agent.py"
    run_json(
        str(grail),
        "--to",
        "agent",
        "-o",
        str(restored_agent),
    )
    assert restored_agent.read_bytes() == agent.read_bytes()

    restored_result = run_json("restore-raw", str(grail))
    restored_raw = Path(restored_result["restored"])
    assert restored_raw.name == "SKILL.raw.md"
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
    assert source.read_bytes() != Path(converted["canonical_grail"]).read_bytes()
    grail = Path(converted["canonical_grail"])
    agent = tmp_path / "metadata_only_agent.py"
    assert not agent.exists()
    run_json("materialize", str(grail), "-o", str(agent))
    assert manifest_of(agent)["name"] == "@example/metadata_only"
    assert capsule_of(grail)["preserved"]["agent"]


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
    assert source.read_bytes() == legacy
    grail = Path(converted["canonical_grail"])
    final = capsule_of(grail)
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
    assert "conflicts with the authoritative agent identity" in failed.stderr


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
    grail = Path(converted["canonical_grail"])
    normalized = tmp_path / "identity_agent.py"
    run_json("materialize", str(grail), "-o", str(normalized))
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
    assert not (agent_skill.parent / agent_source.name).exists()
    restored = tmp_path / "runner_restored_agent.py"
    restore_run = subprocess.run(
        [
            sys.executable,
            str(runner),
            json.dumps({
                "operation": "materialize",
                "path": str(agent_skill),
                "out": str(restored),
            }),
        ],
        cwd=installed,
        capture_output=True,
        text=True,
        timeout=90,
    )
    assert restore_run.returncode == 0, restore_run.stderr
    assert restored.read_bytes() == original_agent

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
    assert raw_skill.read_text(encoding="utf-8").startswith("---\nname: runner-raw")
    raw_grail = Path(raw_result["canonical_grail"])
    assert not (raw_skill.parent / "runner_raw_agent.py").exists()
    assert capsule_of(raw_grail)["platform"]["metadata"]["rapp"]["schema"] == (
        "rapp/1"
    )


def test_global_default_can_flip_to_agent_without_moving_the_grail(
    tmp_path,
    monkeypatch,
):
    configured = run_json("config", "--default-format", "agent")
    assert configured["effective"]["default_format"] == "agent"
    source = tmp_path / "SKILL.md"
    original = b"""---
name: global-flip
description: Prove global agent materialization.
---

Return the supplied input.
"""
    source.write_bytes(original)

    converted = run_json(str(source), "--publisher", "@example")
    assert converted["target_format"] == "agent"
    assert converted["source_unchanged"] is True
    grail = Path(converted["canonical_grail"])
    materialized = Path(converted["selected_artifact"])
    assert grail.is_file()
    assert materialized.is_file()
    assert source.read_bytes() == original
    assert materialized.parent != grail.parent
    assert capsule_of(grail)["platform"]["metadata"]["grail_record"] is True

    monkeypatch.setenv("RAPP_DEFAULT_FORMAT", "skill")
    override = tmp_path / "override" / "SKILL.md"
    override.parent.mkdir()
    override.write_bytes(original.replace(b"global-flip", b"global-override"))
    selected = run_json(str(override), "--publisher", "@example")
    assert selected["target_format"] == "skill"


def test_identity_ledger_survives_deleted_and_relocated_outputs(tmp_path):
    source = tmp_path / "first" / "SKILL.md"
    source.parent.mkdir()
    source.write_text(
        "---\n"
        "name: durable-identity\n"
        "description: Keep one identity across materializations.\n"
        "---\n\n"
        "Return the input.\n",
        encoding="utf-8",
    )
    first = run_json(str(source), "--publisher", "@example")
    first_id = first["rapp"]["rappid"]
    first_grail = Path(first["canonical_grail"])
    shutil.rmtree(first_grail.parent)

    second = run_json(str(source), "--publisher", "@example")
    assert second["rapp"]["rappid"] == first_id

    moved = tmp_path / "second" / "SKILL.md"
    moved.parent.mkdir()
    moved.write_bytes(source.read_bytes())
    third = run_json(str(moved), "--publisher", "@example")
    assert third["rapp"]["rappid"] == first_id

    ledger = (
        Path(os.environ["RAPP_DATA_HOME"]) / "identities.json"
    ).read_text(encoding="utf-8")
    assert str(source) not in ledger
    assert first_id in ledger
    parsed = json.loads(ledger)
    assert all(
        set(entry) == {"rappid", "created_at"}
        for entry in parsed["entries"].values()
    )

    conflicting = run_failure(
        str(source),
        "--publisher",
        "@example",
        "--rappid",
        "rappid:@example/durable-identity:" + "f" * 64,
    )
    assert "already binds this capability" in conflicting.stderr


def test_grail_evolves_under_one_identity_with_immutable_history(tmp_path):
    source = tmp_path / "SKILL.md"
    source.write_text(
        "---\n"
        "name: evolving-grail\n"
        "description: First revision.\n"
        "---\n\n"
        "Return revision one.\n",
        encoding="utf-8",
    )
    first = run_json(str(source), "--publisher", "@example")
    grail = Path(first["canonical_grail"])
    first_bytes = grail.read_bytes()
    first_sha = hashlib.sha256(first_bytes).hexdigest()

    source.write_text(
        "---\n"
        "name: evolving-grail-renamed\n"
        "description: Second revision.\n"
        "---\n\n"
        "Return revision two.\n",
        encoding="utf-8",
    )
    second = run_json(str(source), "--publisher", "@example")

    assert second["rapp"]["rappid"] == first["rapp"]["rappid"]
    assert grail.read_bytes() != first_bytes
    assert (
        grail.parent / "history" / f"{first_sha}.SKILL.md"
    ).read_bytes() == first_bytes


def test_nameless_skill_identity_does_not_leak_parent_path(tmp_path):
    source = tmp_path / "private-customer-codename" / "SKILL.md"
    source.parent.mkdir()
    source.write_text(
        "# Nameless skill\n\nReturn the input.\n",
        encoding="utf-8",
    )
    first = run_json(str(source), "--publisher", "@example")
    assert "/imported-skill:" in first["rapp"]["rappid"]
    assert "private-customer-codename" not in first["rapp"]["rappid"]

    moved = tmp_path / "other-secret-name" / "SKILL.md"
    moved.parent.mkdir()
    moved.write_bytes(source.read_bytes())
    second = run_json(str(moved), "--publisher", "@example")
    assert second["rapp"]["rappid"] == first["rapp"]["rappid"]
    ledger = (
        Path(os.environ["RAPP_DATA_HOME"]) / "identities.json"
    ).read_text(encoding="utf-8")
    assert "private-customer-codename" not in ledger
    assert "other-secret-name" not in ledger


def test_legacy_mode_keeps_adjacent_pair_and_exact_backup(tmp_path):
    source = tmp_path / "SKILL.md"
    original = b"""---
name: legacy-pair
description: Preserve the old adjacent-pair behavior.
---

Return the input.
"""
    source.write_bytes(original)

    converted = run_json(
        str(source),
        "--publisher",
        "@example",
        "--legacy",
    )
    assert converted["mode"] == "legacy"
    assert converted["source_unchanged"] is False
    assert source.read_bytes() != original
    assert (tmp_path / "legacy_pair_agent.py").is_file()
    assert (tmp_path / "rapp" / "source" / "SKILL.md").read_bytes() == original


def test_output_routing_never_implicitly_mutates_or_duplicates(tmp_path):
    raw = tmp_path / "SKILL.md"
    original = b"""---
name: routing-proof
description: Reject ambiguous output routing.
---

Return the input.
"""
    raw.write_bytes(original)
    same = run_failure(
        str(raw),
        "-o",
        str(raw),
        "--publisher",
        "@example",
    )
    assert "without --in-place" in same.stderr
    assert raw.read_bytes() == original

    other = tmp_path / "other" / "SKILL.md"
    legacy = run_failure(
        str(raw),
        "--legacy",
        "-o",
        str(other),
        "--publisher",
        "@example",
    )
    assert "--legacy cannot be combined with --out" in legacy.stderr
    assert raw.read_bytes() == original

    run_json("config", "--default-format", "agent")
    grandfathered = tmp_path / "buzzsaw.py"
    grandfathered.write_bytes(
        (ROOT / "agents" / "@kody-w" / "buzzsaw.py").read_bytes()
    )
    selected = run_json(str(grandfathered))
    materialized = Path(selected["selected_artifact"])
    assert materialized.name == "buzzsaw_agent.py"
    assert materialized.parent != grandfathered.parent
    assert not grandfathered.with_name("buzzsaw_agent.py").exists()

    rappid = "rappid:@example/automatic-grail:" + "5" * 64
    automatic = (
        Path(os.environ["RAPP_DATA_HOME"])
        / "grail"
        / ("5" * 64)
        / "SKILL.md"
    )
    automatic.parent.mkdir(parents=True)
    automatic_raw = original.replace(b"routing-proof", b"automatic-grail")
    automatic.write_bytes(automatic_raw)
    collision = run_failure(
        str(automatic),
        "--publisher",
        "@example",
        "--rappid",
        rappid,
    )
    assert "automatic Grail path resolves to the source" in collision.stderr
    assert automatic.read_bytes() == automatic_raw


def test_unknown_rapp_major_is_refused_without_rewriting(tmp_path):
    core = load_core()
    rci = core.blank_rci()
    rci.update({
        "name": "FutureSkill",
        "slug": "future-skill",
        "description": "A future major version.",
        "instructions": "Do not reinterpret this.",
    })
    rci["platform"] = {
        "metadata": {
            "default_format": "skill",
            "toasted": True,
            "rapp": {
                "schema": "rapp/2",
                "rappid": "rappid:@example/future-skill:" + "d" * 64,
                "kind": "skill",
            },
        },
    }
    source = tmp_path / "SKILL.md"
    original = core.write_skill(rci)
    source.write_bytes(original)

    failed = run_failure(str(source), "--publisher", "@example")
    assert "unsupported RAPP skill schema" in failed.stderr
    assert source.read_bytes() == original


def test_unknown_rapp_major_agent_is_not_relabeled(tmp_path):
    source = tmp_path / "future_agent.py"
    future = identity_agent(
        "rappid:@example/identity:" + "e" * 64
    ).replace(b'"schema": "rapp/1"', b'"schema": "rapp/2"', 1)
    source.write_bytes(future)

    failed = run_failure(str(source))
    assert "unsupported agent manifest RAPP schema" in failed.stderr
    assert source.read_bytes() == future


def test_nested_or_ambiguous_capsules_cannot_hijack_raw_skill(tmp_path):
    inner = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    outer = tmp_path / "outer" / "SKILL.md"
    outer.parent.mkdir()
    outer.write_text(
        "---\n"
        "name: outer-wrapper\n"
        "description: Treat the nested skill only as an example.\n"
        "---\n\n"
        "~~~~~markdown\n"
        + inner
        + "\n~~~~~\n",
        encoding="utf-8",
    )
    converted = run_json(str(outer), "--publisher", "@example")
    materialized = tmp_path / "outer_wrapper_agent.py"
    run_json(
        "materialize",
        converted["canonical_grail"],
        "-o",
        str(materialized),
    )
    assert manifest_of(materialized)["name"] == "@example/outer_wrapper"

    [payload] = CAPSULE.findall(inner)
    ambiguous = tmp_path / "ambiguous" / "SKILL.md"
    ambiguous.parent.mkdir()
    ambiguous.write_text(
        "---\nname: ambiguous\ndescription: Reject two capsules.\n---\n\n"
        f"<!-- rci-capsule:v1:{payload} -->\n"
        f"<!-- rci-capsule:v1:{payload} -->\n",
        encoding="utf-8",
    )
    failed = run_failure(str(ambiguous), "--publisher", "@example")
    assert "multiple active RCI capsules" in failed.stderr

    nonterminal = tmp_path / "nonterminal" / "SKILL.md"
    nonterminal.parent.mkdir()
    nonterminal.write_text(
        "---\nname: nonterminal\ndescription: Reject trailing data.\n---\n\n"
        f"<!-- rci-capsule:v1:{payload} -->\n"
        "trailing text\n",
        encoding="utf-8",
    )
    failed = run_failure(str(nonterminal), "--publisher", "@example")
    assert "must be terminal" in failed.stderr


def test_capsule_decompression_is_bounded_and_single_member():
    converter = load_converter_skill()
    oversized = gzip.compress(b"x" * 1025, mtime=0)
    with pytest.raises(ValueError, match="exceeds"):
        converter._bounded_gzip(oversized, 1024, "fixture")
    concatenated = gzip.compress(b"a", mtime=0) + gzip.compress(
        b"b",
        mtime=0,
    )
    with pytest.raises(ValueError, match="canonical gzip member"):
        converter._bounded_gzip(concatenated, 1024, "fixture")


def test_hotload_casefolds_sacred_kernel_filenames(tmp_path):
    source = tmp_path / "Basic_agent.py"
    source.write_bytes(identity_agent(
        "rappid:@example/basic:" + "4" * 64,
        package="basic",
    ))
    failed = run_failure(
        "hotload",
        str(source),
        "--brainstem-dir",
        str(tmp_path / "brainstem"),
    )
    assert "sacred kernel agent basic_agent.py" in failed.stderr


def test_legacy_command_aliases_and_catalog_remain_available(tmp_path):
    source = tmp_path / "SKILL.md"
    source.write_text(
        "---\n"
        "name: alias-proof\n"
        "description: Exercise legacy command aliases.\n"
        "---\n\n"
        "Return the input.\n",
        encoding="utf-8",
    )
    toasted = run_json("toast", str(source), "--publisher", "@example")
    grail = Path(toasted["canonical_grail"])
    assert run_json("roundtrip", str(grail))["status"] == "ok"
    assert run_json("soak", str(grail))["status"] == "ok"

    catalog = json.loads(
        (ROOT / "scout" / "catalog" / "catalog.json").read_text()
    )
    names = {item["skill_name"] for item in catalog["skills"]}
    assert "rapp-agent-converter" in names
    assert "rappstore-rapp-toaster" in names
    assert (ROOT / "rapp_skill.md").is_file()
    assert (ROOT / "rapp_skills.md").is_file()


def test_read_only_crlf_skill_toasts_without_touching_source(tmp_path):
    source_dir = tmp_path / "readonly"
    source_dir.mkdir()
    source = source_dir / "SKILL.md"
    original = (
        b"---\r\n"
        b"name: crlf-readonly\r\n"
        b"description: Preserve CRLF source bytes.\r\n"
        b"---\r\n\r\n"
        b"Return the input.\r\n"
    )
    source.write_bytes(original)
    source.chmod(0o444)
    source_dir.chmod(0o555)
    try:
        converted = run_json(str(source), "--publisher", "@example")
        assert source.read_bytes() == original
        grail = Path(converted["canonical_grail"])
        restored = tmp_path / "restored.raw.md"
        run_json("restore-raw", str(grail), "-o", str(restored))
        assert restored.read_bytes() == original
    finally:
        source_dir.chmod(0o755)
        source.chmod(0o644)


@pytest.mark.skipif(os.name == "nt", reason="symlink privileges vary on Windows")
def test_in_place_conversion_refuses_symlink_source(tmp_path):
    real = tmp_path / "real" / "SKILL.md"
    real.parent.mkdir()
    original = b"""---
name: symlink-proof
description: Refuse implicit symlink mutation.
---

Return the input.
"""
    real.write_bytes(original)
    link = tmp_path / "SKILL.md"
    link.symlink_to(real)

    converted = run_json(str(link), "--publisher", "@example")
    assert Path(converted["canonical_grail"]).is_file()
    assert real.read_bytes() == original
    failed = run_failure(
        str(link),
        "--publisher",
        "@example",
        "--in-place",
    )
    assert "through a symlink" in failed.stderr
    assert real.read_bytes() == original


def test_concurrent_conversion_converges_on_one_identity(tmp_path):
    source = tmp_path / "SKILL.md"
    source.write_text(
        "---\n"
        "name: concurrent-proof\n"
        "description: Converge concurrent conversions.\n"
        "---\n\n"
        "Return the input.\n",
        encoding="utf-8",
    )
    command = [
        sys.executable,
        str(CLI),
        str(source),
        "--publisher",
        "@example",
    ]
    processes = [
        subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=os.environ.copy(),
        )
        for _ in range(2)
    ]
    results = []
    for process in processes:
        stdout, stderr = process.communicate(timeout=90)
        assert process.returncode == 0, stderr
        results.append(json.loads(stdout))
    assert results[0]["rapp"]["rappid"] == results[1]["rapp"]["rappid"]
    assert results[0]["canonical_grail"] == results[1]["canonical_grail"]
    assert run_json("verify", results[0]["canonical_grail"])["status"] == "ok"


def test_concurrent_grail_revisions_preserve_every_version(tmp_path):
    rappid = "rappid:@example/shared-grail:" + "1" * 64

    def skill(path: Path, name: str, body: str):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "---\n"
            f"name: {name}\n"
            f"description: {body}\n"
            "---\n\n"
            f"{body}\n",
            encoding="utf-8",
        )

    base = tmp_path / "base" / "SKILL.md"
    left = tmp_path / "left" / "SKILL.md"
    right = tmp_path / "right" / "SKILL.md"
    skill(base, "shared-grail", "base revision")
    skill(left, "shared-grail-left", "left revision")
    skill(right, "shared-grail-right", "right revision")

    initial = run_json(
        str(base),
        "--publisher",
        "@example",
        "--rappid",
        rappid,
    )
    grail = Path(initial["canonical_grail"])
    commands = [
        [
            sys.executable,
            str(CLI),
            str(source),
            "--publisher",
            "@example",
            "--rappid",
            rappid,
        ]
        for source in (left, right)
    ]
    processes = [
        subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=os.environ.copy(),
        )
        for command in commands
    ]
    for process in processes:
        stdout, stderr = process.communicate(timeout=90)
        assert process.returncode == 0, stderr
        assert Path(json.loads(stdout)["canonical_grail"]) == grail

    observed = {grail.read_bytes()}
    history = grail.parent / "history"
    observed.update(path.read_bytes() for path in history.glob("*.SKILL.md"))
    assert len(observed) == 3
    joined = b"\n".join(observed)
    assert b"base revision" in joined
    assert b"left revision" in joined
    assert b"right revision" in joined


def test_concurrent_hotloads_cannot_duplicate_runtime_name(tmp_path):
    first = tmp_path / "alpha_agent.py"
    second = tmp_path / "beta_agent.py"
    first.write_bytes(identity_agent(
        "rappid:@example/alpha:" + "2" * 64,
        package="alpha",
        runtime="CollisionAgent",
    ))
    second.write_bytes(identity_agent(
        "rappid:@example/beta:" + "3" * 64,
        package="beta",
        runtime="CollisionAgent",
    ))
    brainstem = tmp_path / "brainstem"
    commands = [
        [
            sys.executable,
            str(CLI),
            "hotload",
            str(source),
            "--brainstem-dir",
            str(brainstem),
        ]
        for source in (first, second)
    ]
    processes = [
        subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=os.environ.copy(),
        )
        for command in commands
    ]
    results = [process.communicate(timeout=90) for process in processes]
    codes = [process.returncode for process in processes]
    assert sorted(codes) == [0, 1], results
    installed = list((brainstem / "agents").glob("*_agent.py"))
    assert len(installed) == 1


def test_brainstem_hotloads_raw_toasted_and_agent_inputs(tmp_path):
    raw = tmp_path / "raw" / "SKILL.md"
    raw.parent.mkdir()
    raw.write_text(
        "---\n"
        "name: hotload-proof\n"
        "description: Hotload every supported representation.\n"
        "---\n\n"
        "Return the input.\n",
        encoding="utf-8",
    )
    first_brainstem = tmp_path / "brainstem-raw"
    raw_hotload = run_json(
        "hotload",
        str(raw),
        "--brainstem-dir",
        str(first_brainstem),
        "--publisher",
        "@example",
    )
    raw_agent = Path(raw_hotload["path"])
    assert raw_agent.is_file()
    assert raw_hotload["hotload"].startswith("No restart required")
    assert raw_agent.with_suffix(".py.origin.json").is_file()

    toasted = Path(raw_hotload["canonical_grail"])
    core = load_core()
    legacy_record = core.read_agent(raw_agent.read_bytes(), raw_agent.name)
    legacy_record["platform"]["metadata"] = {"projection": "legacy-rci/1"}
    legacy = tmp_path / "legacy" / "SKILL.md"
    legacy.parent.mkdir()
    legacy.write_bytes(core.write_skill(legacy_record))
    legacy_hotload = run_json(
        "hotload",
        str(legacy),
        "--brainstem-dir",
        str(first_brainstem),
    )
    assert legacy_hotload["result"] == "already-installed"

    toasted_hotload = run_json(
        "hotload",
        str(toasted),
        "--brainstem-dir",
        str(first_brainstem),
    )
    assert toasted_hotload["result"] == "already-installed"
    assert Path(toasted_hotload["path"]).read_bytes() == raw_agent.read_bytes()

    agent_hotload = run_json(
        "hotload",
        str(raw_agent),
        "--brainstem-dir",
        str(first_brainstem),
    )
    assert agent_hotload["result"] == "already-installed"
    assert Path(agent_hotload["path"]).read_bytes() == raw_agent.read_bytes()

    repeated = run_json(
        "hotload",
        str(raw),
        "--brainstem-dir",
        str(first_brainstem),
        "--publisher",
        "@example",
    )
    assert repeated["result"] == "already-installed"

    grail_before_rejection = toasted.read_bytes()
    agent_before_rejection = raw_agent.read_bytes()
    raw.write_text(
        "---\n"
        "name: hotload-proof\n"
        "description: A changed revision must require approval.\n"
        "---\n\n"
        "Return the changed input.\n",
        encoding="utf-8",
    )
    rejected = run_failure(
        "hotload",
        str(raw),
        "--brainstem-dir",
        str(first_brainstem),
        "--publisher",
        "@example",
    )
    assert "differs; pass force=true" in rejected.stderr
    assert toasted.read_bytes() == grail_before_rejection
    assert raw_agent.read_bytes() == agent_before_rejection


def test_single_converter_agent_becomes_brainstem_format_membrane(tmp_path):
    agents = tmp_path / "brainstem" / "agents"
    agents.mkdir(parents=True)
    converter = agents / "rapp_agent_converter_agent.py"
    converter.write_bytes(
        (SKILL_DIR / "rapp_agent_converter_agent.py").read_bytes()
    )
    raw = tmp_path / "incoming" / "SKILL.md"
    raw.parent.mkdir()
    raw.write_text(
        "---\n"
        "name: brainstem-membrane\n"
        "description: Hotload through one converter agent.\n"
        "---\n\n"
        "Return the input.\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            str(converter),
            "hotload",
            str(raw),
            "--publisher",
            "@example",
        ],
        capture_output=True,
        text=True,
        timeout=90,
        env=os.environ.copy(),
    )
    assert result.returncode == 0, result.stderr
    payload = json.loads(result.stdout)
    assert Path(payload["path"]).parent == agents
    assert Path(payload["path"]).name == "brainstem_membrane_agent.py"
    assert Path(payload["canonical_grail"]).is_file()


def test_in_process_agent_contains_core_system_exit_errors(tmp_path):
    converter = load_converter_skill().RappAgentConverterAgent()
    unsupported = tmp_path / "not-a-capability.txt"
    unsupported.write_text("nope", encoding="utf-8")
    result = json.loads(converter.perform(path=str(unsupported)))
    assert result["status"] == "error"
    assert "cannot detect format" in result["message"]

    malformed = tmp_path / "broken_agent.py"
    malformed.write_text("def broken(:\n", encoding="utf-8")
    result = json.loads(converter.perform(path=str(malformed)))
    assert result["status"] == "error"
    assert "SyntaxError" in result["message"] or "parseable Python" in result["message"]
