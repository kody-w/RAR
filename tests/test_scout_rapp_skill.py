"""RAR -> Microsoft Scout projection, hotload, and workflow gates."""

from __future__ import annotations

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
import zipfile

import pytest


ROOT = Path(__file__).resolve().parent.parent
SCOUT = ROOT / "scout"
CATALOG_PATH = SCOUT / "catalog" / "catalog.json"
CATALOG = json.loads(CATALOG_PATH.read_text())
REGISTRY = json.loads((ROOT / "registry.json").read_text())["agents"]
AGGREGATED = json.loads(
    (ROOT / "state" / "aggregated.json").read_text()
)["items"]
FEDERATION = json.loads(
    (ROOT / "state" / "federation.json").read_text()
)["rapplications"]
CAPSULE = re.compile(r"<!--\s*rci-capsule:v1:([A-Za-z0-9+/=]+)\s*-->")


def lf(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def capsule_of(skill_text: str) -> dict:
    matches = CAPSULE.findall(skill_text)
    assert matches, "Toasted skill is missing its RCI capsule"
    return json.loads(gzip.decompress(base64.b64decode(matches[-1])))


def skill_name(skill_text: str) -> str:
    match = re.search(r'^name:\s*"([^"]+)"$', skill_text, re.MULTILINE)
    assert match, "skill frontmatter has no quoted name"
    return match.group(1)


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


def load_rapp_skill_module():
    path = ROOT / "rapp_skill_agent.py"
    spec = importlib.util.spec_from_file_location("_rapp_skill_test", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def local_catalog(tmp_path: Path, *records: dict) -> Path:
    localized = []
    for record in records:
        source = primary_skill_dir(record)
        item = dict(record)
        item["files"] = [
            {
                "path": file["path"],
                "sha256": file["sha256"],
                "url": (source / file["path"]).as_uri(),
            }
            for file in record["files"]
        ]
        localized.append(item)
    path = tmp_path / "catalog.json"
    path.write_text(json.dumps({
        "schema": "rar-scout-catalog/1.0",
        "skills": localized,
    }))
    return path


def test_top_level_is_catalog_not_an_import_root():
    assert not list(SCOUT.glob("*.json"))
    assert CATALOG_PATH.is_file()
    assert (SCOUT / "starter" / "skills" / "rapp-skills").is_dir()


def test_copilot_plugin_marketplace_installs_the_unified_rapp_plugin():
    marketplace = json.loads(
        (ROOT / ".claude-plugin" / "marketplace.json").read_text()
    )
    [plugin] = marketplace["plugins"]
    starter_manifest = json.loads(
        (
            SCOUT
            / "starter"
            / ".claude-plugin"
            / "plugin.json"
        ).read_text()
    )
    foundation = next(
        item
        for item in CATALOG["skills"]
        if item["skill_name"] == "rapp-skills"
    )
    assert marketplace["name"] == "rar"
    assert plugin["name"] == "rapp"
    assert plugin["source"] == "./scout/starter"
    assert plugin["skills"] == [
        "./skills/rapp-skills"
    ]
    assert plugin["version"] == foundation["version"]
    assert starter_manifest["name"] == "rapp"
    assert starter_manifest["version"] == foundation["version"]


def test_bundles_stay_within_scout_import_budget():
    assert CATALOG["bundles"]
    for bundle in CATALOG["bundles"]:
        assert len(bundle["skills"]) <= 8
        assert bundle["files"] <= 40
        assert bundle["bytes"] <= 2_000_000
        assert bundle["import_url"].startswith(
            "https://github.com/kody-w/RAR/tree/main/scout/"
        )


@pytest.mark.parametrize("filename", ["rapp_skill.md", "rapp_skills.md"])
def test_root_rapp_skills_restore_the_same_agent(filename):
    skill = (ROOT / filename).read_text(encoding="utf-8")
    capsule = capsule_of(skill)
    preserved = capsule["preserved"]["agent"]
    restored = gzip.decompress(base64.b64decode(preserved["b64"]))
    assert sha256(restored) == preserved["sha256"]
    assert restored == (ROOT / "rapp_skill_agent.py").read_bytes()


def test_plural_skill_has_hotload_and_bootstrap_contract():
    skill = (ROOT / "rapp_skills.md").read_text(encoding="utf-8")
    assert skill_name(skill) == "rapp-skills"
    assert '"sync"' in skill
    assert '"install"' in skill
    assert '"remove"' in skill
    assert '"verify"' in skill
    assert '"allow_install"' in skill


def test_every_primary_skill_is_reversible_and_exactly_pinned():
    assert len(CATALOG["skills"]) >= 300
    for record in CATALOG["skills"]:
        directory = primary_skill_dir(record)
        skill_path = directory / "SKILL.md"
        lock_path = directory / "rapp" / "agent.lock.json"
        runner_path = directory / "scripts" / "run_agent.py"
        assert skill_path.is_file(), directory
        assert lock_path.is_file(), directory
        assert runner_path.is_file(), directory

        skill = skill_path.read_text(encoding="utf-8")
        lock = json.loads(lock_path.read_text())
        capsule = capsule_of(skill)
        preserved = capsule["preserved"]["agent"]
        linked = directory / preserved["filename"]

        assert skill_name(skill) == directory.name
        assert linked.is_file()
        assert linked.read_bytes() == gzip.decompress(
            base64.b64decode(preserved["b64"])
        )
        assert sha256(linked.read_bytes()) == preserved["sha256"]
        assert sha256(lf(linked.read_bytes())) == lock["agent_sha256"]
        assert lock["agent_file"] == linked.name
        assert lock["agent"] == capsule["platform"]["metadata"]["rar_agent"]
        assert lock["entry_class"]
        assert record["files"]
        for file in record["files"]:
            target = directory / file["path"]
            assert target.is_file()
            assert sha256(target.read_bytes()) == file["sha256"]


def test_drifted_current_files_use_notarized_historical_bytes():
    registry_by_name = {entry["name"]: entry for entry in REGISTRY}
    catalog_by_name = {entry["identity"]: entry for entry in CATALOG["skills"]}
    recovered = [
        "@kody-w/connected_solution_agent",
        "@kody-w/copilot_studio_forge_agent",
        "@rapp/learn_new",
    ]
    for identity in recovered:
        record = catalog_by_name[identity]
        registry = registry_by_name[identity]
        assert record["source_sha256"] == registry["_sha256"]
        assert re.fullmatch(r"[a-f0-9]{40}", record["source_commit"])


def test_powercat_channel_projects_every_aggregated_skill():
    projected = {
        item["identity"]
        for item in CATALOG["skills"]
        if item["channel"] == "powercat"
    }
    expected = {
        entry["name"]
        for entry in REGISTRY
        if entry["name"].startswith("@cat-agent-skills/")
    }
    assert projected == expected
    missing = {
        item["identity"]
        for item in CATALOG["skipped"]
        if item.get("aggregate_id")
    }
    aggregate_refs = {
        item["ref"]
        for item in AGGREGATED
        if str(item.get("ref") or "").startswith("@cat-agent-skills/")
    }
    assert aggregate_refs == projected
    assert not missing


def test_cowork_cookbook_channel_projects_every_recipe():
    projected = {
        item["identity"]
        for item in CATALOG["skills"]
        if item["channel"] == "cowork-cookbook"
    }
    expected = {
        entry["name"]
        for entry in REGISTRY
        if entry["name"].startswith("@cowork-cookbook/")
    }
    assert len(expected) == 1481
    assert projected == expected
    aggregate_refs = {
        item["ref"]
        for item in AGGREGATED
        if str(item.get("ref") or "").startswith("@cowork-cookbook/")
    }
    assert aggregate_refs == projected


def test_workflow_bundles_contain_only_the_bound_skill():
    available = {item["skill_name"] for item in CATALOG["skills"]}
    assert len(CATALOG["workflows"]) >= 1
    for item in CATALOG["workflows"]:
        root = SCOUT / "workflows" / item["skill_name"]
        workflow_files = list(root.glob("*.json"))
        skill_dirs = [
            path
            for path in (root / "skills").iterdir()
            if path.is_dir()
        ]
        assert [path.name for path in workflow_files] == [item["file"]]
        assert [path.name for path in skill_dirs] == [item["skill_name"]]
        workflow = json.loads(workflow_files[0].read_text())
        assert workflow["skillNames"] == [item["skill_name"]]
        assert set(workflow["skillNames"]).issubset(available)
        assert workflow["enabled"] is False
        assert workflow["triggerType"] in {"schedule", "condition"}
        assert workflow["steps"]


def test_bookfactory_exact_entrypoint_workflow_and_failure_shape():
    item = next(
        entry
        for entry in CATALOG["workflows"]
        if entry["identity"] == "@rarbookworld/bookfactory"
    )
    root = SCOUT / "workflows" / item["skill_name"]
    skill_dir = root / "skills" / item["skill_name"]
    lock = json.loads(
        (skill_dir / "rapp" / "agent.lock.json").read_text()
    )
    workflow = json.loads((root / item["file"]).read_text())

    assert lock["entry_class"] == "BookFactory"
    assert lock["runtime_name"] == "BookFactory"
    assert lock["tool_schema"]["required"] == ["source"]
    assert "input" not in lock["tool_schema"]["properties"]
    assert workflow["name"] == "BookFactory - RAPP Test Chapter"
    assert "The Wire That Carries Agents" in workflow["steps"][0]["prompt"]

    environment = {
        key: value
        for key, value in os.environ.items()
        if not key.startswith("AZURE_OPENAI")
        and key not in {"OPENAI_API_KEY", "OPENAI_MODEL"}
    }
    run = subprocess.run(
        [
            sys.executable,
            str(skill_dir / "scripts" / "run_agent.py"),
            json.dumps({"source": "test", "chapter_title": "Test"}),
        ],
        cwd=skill_dir,
        env=environment,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert run.returncode == 0, run.stderr
    output = json.loads(run.stdout)
    assert output["status"] == "error"
    assert output["failed_stage"] == "writer"


def test_bookfactory_tamper_refusal(tmp_path):
    record = next(
        entry
        for entry in CATALOG["skills"]
        if entry["identity"] == "@rarbookworld/bookfactory"
    )
    source = primary_skill_dir(record)
    bundle = tmp_path / source.name
    shutil.copytree(source, bundle)
    runner = bundle / "scripts" / "run_agent.py"

    before = subprocess.run(
        [sys.executable, str(runner), "--preflight"],
        cwd=bundle,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert before.returncode == 0
    linked = bundle / "bookfactory_agent.py"
    linked.write_bytes(linked.read_bytes() + b"\n# mutation\n")
    after = subprocess.run(
        [sys.executable, str(runner), "--preflight"],
        cwd=bundle,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert after.returncode == 3
    assert "RAPP_UNAVAILABLE:integrity-mismatch" in after.stderr


def test_runner_awaits_async_agent_perform():
    record = next(
        entry
        for entry in CATALOG["skills"]
        if entry["identity"] == "@kody-w/agent_workbench"
    )
    directory = primary_skill_dir(record)
    process = subprocess.run(
        [
            sys.executable,
            str(directory / "scripts" / "run_agent.py"),
            json.dumps({"action": "scaffold"}),
        ],
        cwd=directory,
        capture_output=True,
        text=True,
        timeout=60,
    )
    assert process.returncode == 0, process.stderr
    assert "coroutine" not in process.stderr.lower()
    assert process.stdout.strip()


def test_starter_injects_checksum_pinned_platform_installers():
    record = next(
        entry
        for entry in CATALOG["skills"]
        if entry["skill_name"] == "rapp-skills"
    )
    directory = primary_skill_dir(record)
    expected = {
        "install.sh": "cc586dd1752520d05fbff99a637eef308bb7051ffae457b7d037aa0574341794",
        "install.ps1": "747a5a8b2e6a41292a4b8b1a719fea588bdd21c523e3a3edb474dd651a8a2fda",
        "install.cmd": "9d4695f8ef7401d8098f2f0ed3bafddd916098d73892f0310f19c7729b514940",
    }
    for filename, digest in expected.items():
        path = directory / "installer" / filename
        assert path.is_file()
        assert sha256(path.read_bytes()) == digest


def test_rapp_skill_hotloads_verifies_replaces_and_removes(
    tmp_path,
    monkeypatch,
):
    module = load_rapp_skill_module()
    agent = module.RappSkillAgent()
    record = next(
        entry
        for entry in CATALOG["skills"]
        if entry["identity"] == "@rarbookworld/bookfactory"
    )
    catalog = local_catalog(tmp_path, record)
    skills_dir = tmp_path / "skills"
    state_dir = tmp_path / "state"
    monkeypatch.setenv("RAPP_SKILLS_STATE_DIR", str(state_dir))

    installed = json.loads(agent.perform(
        operation="install",
        agent=record["identity"],
        catalog_url=str(catalog),
        skills_dir=str(skills_dir),
    ))
    assert installed["status"] == "ok"
    target = skills_dir / record["skill_name"]
    assert (target / ".rar-managed.json").is_file()

    verified = json.loads(agent.perform(
        operation="verify",
        catalog_url=str(catalog),
        skills_dir=str(skills_dir),
    ))
    assert verified["status"] == "ok"
    assert record["skill_name"] in verified["verified"]

    marker_path = target / ".rar-managed.json"
    marker = json.loads(marker_path.read_text())
    marker["files"] = []
    marker["skill_sha256"] = record["skill_sha256"]
    marker_path.write_text(json.dumps(marker), encoding="utf-8")
    marker_attack = json.loads(agent.perform(
        operation="verify",
        catalog_url=str(catalog),
        skills_dir=str(skills_dir),
    ))
    assert marker_attack["status"] == "error"
    assert "marker: no file records" in marker_attack["failures"][0]["failures"]
    refused_marker = json.loads(agent.perform(
        operation="sync",
        channel=record["channel"],
        catalog_url=str(catalog),
        skills_dir=str(skills_dir),
    ))
    assert refused_marker["code"] == "managed-skill-modified"
    marker_restored = json.loads(agent.perform(
        operation="sync",
        channel=record["channel"],
        catalog_url=str(catalog),
        skills_dir=str(skills_dir),
        force=True,
    ))
    assert marker_restored["status"] == "ok"

    valid_marker = marker_path.read_text(encoding="utf-8")
    marker_path.write_text("{not json", encoding="utf-8")
    malformed_marker = json.loads(agent.perform(
        operation="verify",
        catalog_url=str(catalog),
        skills_dir=str(skills_dir),
    ))
    assert malformed_marker["status"] == "error"
    assert "no valid RAR marker" in malformed_marker["failures"][0]["failures"][0]
    marker_path.unlink()
    missing_marker = json.loads(agent.perform(
        operation="verify",
        catalog_url=str(catalog),
        skills_dir=str(skills_dir),
    ))
    assert missing_marker["status"] == "error"
    assert "no valid RAR marker" in missing_marker["failures"][0]["failures"][0]
    marker_path.write_text(valid_marker, encoding="utf-8")

    linked = target / record["linked_agent"]
    linked.write_bytes(linked.read_bytes() + b"\n# local mutation\n")
    refused = json.loads(agent.perform(
        operation="sync",
        channel=record["channel"],
        catalog_url=str(catalog),
        skills_dir=str(skills_dir),
    ))
    assert refused["status"] == "error"
    assert refused["code"] == "managed-skill-modified"

    restored = json.loads(agent.perform(
        operation="sync",
        channel=record["channel"],
        catalog_url=str(catalog),
        skills_dir=str(skills_dir),
        force=True,
    ))
    assert restored["status"] == "ok"
    assert record["skill_name"] in restored["installed"]

    removed = json.loads(agent.perform(
        operation="remove",
        agent=record["identity"],
        catalog_url=str(catalog),
        skills_dir=str(skills_dir),
    ))
    assert removed["status"] == "ok"
    assert not target.exists()
    assert Path(removed["backup"]).is_dir()


def test_verify_rejects_cross_skill_marker_substitution(
    tmp_path,
    monkeypatch,
):
    module = load_rapp_skill_module()
    agent = module.RappSkillAgent()
    first = next(
        entry
        for entry in CATALOG["skills"]
        if entry["identity"] == "@rarbookworld/bookfactory"
    )
    second = next(
        entry
        for entry in CATALOG["skills"]
        if entry["identity"] == "@cowork-cookbook/account_360_briefing"
    )
    catalog = local_catalog(tmp_path, first, second)
    skills_dir = tmp_path / "skills"
    monkeypatch.setenv(
        "RAPP_SKILLS_STATE_DIR",
        str(tmp_path / "state"),
    )
    installed = json.loads(agent.perform(
        operation="install",
        agent=first["identity"],
        catalog_url=str(catalog),
        skills_dir=str(skills_dir),
    ))
    assert installed["status"] == "ok"

    staging = tmp_path / "substitution"
    staging.mkdir()
    localized_second = next(
        entry
        for entry in json.loads(catalog.read_text())["skills"]
        if entry["identity"] == second["identity"]
    )
    second_dir, _ = agent._stage_catalog_skill(
        localized_second,
        str(catalog),
        staging,
        30,
    )
    target = skills_dir / first["skill_name"]
    shutil.rmtree(target)
    shutil.move(str(second_dir), str(target))

    verified = json.loads(agent.perform(
        operation="verify",
        catalog_url=str(catalog),
        skills_dir=str(skills_dir),
    ))
    assert verified["status"] == "error"
    problems = verified["failures"][0]["failures"]
    assert any("marker skill_name" in problem for problem in problems)
    assert first["skill_name"] not in verified["verified"]


def test_manual_export_writes_verified_cross_platform_html_package(tmp_path):
    module = load_rapp_skill_module()
    agent = module.RappSkillAgent()
    record = next(
        entry
        for entry in CATALOG["skills"]
        if entry["identity"] == "@cowork-cookbook/account_360_briefing"
    )
    catalog = local_catalog(tmp_path, record)
    output = tmp_path / "manual-export"

    exported = json.loads(agent.perform(
        operation="manual_export",
        agent=record["identity"],
        platform="cowork",
        catalog_url=str(catalog),
        output_dir=str(output),
    ))
    assert exported["status"] == "ok"
    assert exported["platform"] == "cowork"
    assert exported["source_sha256"] == record["source_sha256"]
    assert exported["skill_sha256"] == record["skill_sha256"]
    assert exported["cowork_limits"]["within_limits"] is True

    guide = (output / "guide.html").read_text(encoding="utf-8")
    assert "Microsoft Scout" in guide
    assert "Microsoft Copilot Cowork" in guide
    assert "Microsoft Copilot Studio" in guide
    assert "/Documents/Cowork/skills/" in guide
    assert "pac copilot push" in guide
    assert record["identity"] in guide
    assert record["source_sha256"] in guide

    skill_dir = output / "skill" / record["skill_name"]
    assert not (skill_dir / ".rar-managed.json").exists()
    preflight = subprocess.run(
        [
            sys.executable,
            str(skill_dir / "scripts" / "run_agent.py"),
            "--preflight",
        ],
        cwd=skill_dir,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert preflight.returncode == 0
    assert preflight.stdout.strip() == "RAPP_READY"

    with zipfile.ZipFile(output / f"{record['skill_name']}.zip") as archive:
        names = set(archive.namelist())
    assert "SKILL.md" in names
    assert "rapp/agent.lock.json" in names
    assert "scripts/run_agent.py" in names
    assert record["linked_agent"] in names
    assert ".rar-managed.json" not in names

    refused = json.loads(agent.perform(
        operation="manual_export",
        agent=record["identity"],
        catalog_url=str(catalog),
        output_dir=str(output),
    ))
    assert refused["code"] == "export-exists"
    replaced = json.loads(agent.perform(
        operation="manual_export",
        agent=record["identity"],
        catalog_url=str(catalog),
        output_dir=str(output),
        force=True,
    ))
    assert replaced["status"] == "ok"
    assert Path(replaced["backup"]).is_dir()


def test_manual_export_rejects_executable_import_urls():
    module = load_rapp_skill_module()
    rendered = module._manual_export_html({
        "identity": "@test/demo",
        "skill_name": "test-demo",
        "version": "1.0.0",
        "channel": "native",
        "description": "demo",
        "source_sha256": "a" * 64,
        "skill_sha256": "b" * 64,
        "import_url": "javascript:alert(document.domain)",
        "files": [],
    }, "scout")
    assert 'href="javascript:' not in rendered
    assert "No safe HTTPS bundle URL is published." in rendered


def test_bootstrap_callback_installs_only_the_pinned_dropin(
    tmp_path,
    monkeypatch,
):
    module = load_rapp_skill_module()
    agent = module.RappSkillAgent()
    brainstem_dir = tmp_path / "brainstem"
    agents_dir = brainstem_dir / "agents"
    agents_dir.mkdir(parents=True)
    grail = brainstem_dir / "brainstem.py"
    grail.write_text("GRAIL_SENTINEL\n", encoding="utf-8")
    source = (
        ROOT / "agents" / "@rapp" / "mcp_callback_agent.py"
    ).read_bytes()
    home = tmp_path / "home"
    scout_config = home / ".scout" / "m-mcp-servers.json"

    monkeypatch.setenv("HOME", str(home))
    monkeypatch.setenv("RAPP_MCP_NODE", sys.executable)
    monkeypatch.setenv(
        "RAPP_MCP_ADAPTER_DIR",
        str(home / ".copilot" / "mcp-servers" / "rapp-brainstem"),
    )
    monkeypatch.setenv(
        "RAPP_MCP_BIN_DIR",
        str(home / ".copilot" / "bin"),
    )
    monkeypatch.setenv("RAPP_SCOUT_MCP_CONFIG", str(scout_config))
    monkeypatch.setattr(
        agent,
        "_health_payload",
        lambda _kwargs: (
            {
                "base_url": "http://localhost:7071",
                "timeout_seconds": 30,
                "secret": "",
            },
            {"brainstem_dir": str(brainstem_dir), "agents": []},
        ),
    )
    monkeypatch.setattr(module, "_fetch_verified", lambda *_args: source)
    monkeypatch.setattr(
        module,
        "_request_json",
        lambda *_args, **_kwargs: {
            "brainstem_dir": str(brainstem_dir),
            "agents": ["McpCallback"],
        },
    )

    installed = json.loads(agent.perform(operation="bootstrap_callback"))
    assert installed["status"] == "ok"
    assert installed["grail_modified"] is False
    assert installed["agent_visible"] is True
    assert installed["sha256"] == module.MCP_CALLBACK_SHA256
    assert (agents_dir / "mcp_callback_agent.py").read_bytes() == source
    assert grail.read_text(encoding="utf-8") == "GRAIL_SENTINEL\n"
    assert scout_config.is_file()

    destination = agents_dir / "mcp_callback_agent.py"
    destination.write_text("local variant\n", encoding="utf-8")
    refused = json.loads(agent.perform(operation="bootstrap_callback"))
    assert refused["code"] == "existing-callback-agent-differs"
    replaced = json.loads(agent.perform(
        operation="bootstrap_callback",
        force=True,
    ))
    assert replaced["status"] == "ok"
    assert Path(replaced["backup"]).read_text() == "local variant\n"
    assert destination.read_bytes() == source
    assert grail.read_text(encoding="utf-8") == "GRAIL_SENTINEL\n"


def test_fresh_install_requires_explicit_authorization(monkeypatch, tmp_path):
    module = load_rapp_skill_module()
    agent = module.RappSkillAgent()
    missing = tmp_path / "missing-launcher"

    def unavailable(_kwargs):
        raise module.BridgeRequestError("unreachable", "offline")

    monkeypatch.setattr(agent, "_status", unavailable)
    denied = json.loads(agent._ensure({
        "launcher": str(missing),
    }))
    assert denied["code"] == "brainstem-not-installed"

    monkeypatch.setattr(
        agent,
        "_bootstrap_global_brainstem",
        lambda _kwargs, _url: json.dumps({
            "status": "installing",
            "operation": "ensure",
        }),
    )
    allowed = json.loads(agent._ensure({
        "launcher": str(missing),
        "allow_install": True,
    }))
    assert allowed["status"] == "installing"


def test_catalog_coverage_and_explicit_exclusions():
    projected = {
        item["identity"]
        for item in CATALOG["skills"]
        if item["source_kind"] != "foundation"
    }
    skipped = {item["identity"] for item in CATALOG["skipped"]}
    registry_expected = {
        entry["name"]
        for entry in REGISTRY
        if entry["name"] != "@rapp/basic_agent"
        and not str(entry.get("_file") or "").endswith(".stub")
    }
    assert registry_expected.issubset(projected)

    federation_covered = {
        item["federation_id"]
        for item in CATALOG["skills"]
        if item.get("federation_id")
    } | {
        item["federation_id"]
        for item in CATALOG["skipped"]
        if item.get("federation_id")
    }
    assert {entry["id"] for entry in FEDERATION}.issubset(
        federation_covered
    )
    assert skipped
    assert all(item.get("reason") for item in CATALOG["skipped"])
