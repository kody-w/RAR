"""End-to-end skill-first publication invariants."""

from __future__ import annotations

import importlib.util
import hashlib
import json
from pathlib import Path
import re
import zipfile


ROOT = Path(__file__).resolve().parent.parent
SCOUT = json.loads(
    (ROOT / "scout" / "catalog" / "catalog.json").read_text()
)
REGISTRY = json.loads((ROOT / "registry.json").read_text())["agents"]
STATIC = json.loads((ROOT / "api" / "v1" / "catalog.json").read_text())
FRONT = json.loads((ROOT / "api" / "v1" / "front.json").read_text())
RAPPID = re.compile(
    r"^rappid:@[a-z0-9]+(?:-[a-z0-9]+)*/"
    r"[a-z0-9]+(?:-[a-z0-9]+)*:[0-9a-f]{64}$"
)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def api_id(identity):
    return identity.lstrip("@").replace("/", "__").replace(".", "_")


def test_public_api_uses_scout_grail_identity_and_url():
    registry_names = {entry["name"] for entry in REGISTRY}
    shared = [
        record for record in SCOUT["skills"]
        if record["identity"] in registry_names
    ]
    assert len(shared) >= 1600
    for record in shared:
        api = json.loads(
            (
                ROOT
                / "api"
                / "v1"
                / "agent"
                / f"{api_id(record['identity'])}.json"
            ).read_text()
        )
        assert api["rappid"] == record["rappid"]
        assert RAPPID.fullmatch(api["rappid"])
        assert api["default_artifact"] == "skill"
        assert api["grail_record"] == "SKILL.md"
        assert api["default_url"] == api["skill_url"]
        assert api["skill_url"].endswith("/SKILL.md")
        assert api["backup_agent_url"] == api["py_url"]
        assert api["py_url"].endswith((".py", ".py.card"))


def test_static_and_front_catalogs_select_skills_but_keep_rollback():
    scout = {item["identity"]: item for item in SCOUT["skills"]}
    static = {item["name"]: item for item in STATIC["agents"]}
    front = {
        item["ref"]: item
        for item in FRONT["items"]
        if item["origin"] == "native"
    }
    for identity in set(scout) & set(static) & set(front):
        skill = scout[identity]
        static_item = static[identity]
        front_item = front[identity]
        assert static_item["rappid"] == skill["rappid"]
        assert static_item["default_artifact"] == "skill"
        assert static_item["default_url"].endswith("/SKILL.md")
        assert static_item["backup_agent_url"].endswith((".py", ".py.card"))
        assert front_item["rappid"] == skill["rappid"]
        assert front_item["default_artifact"] == "skill"
        assert front_item["install"].endswith("/SKILL.md")
        assert front_item["backup_install"].endswith((".py", ".py.card"))


def test_workflows_bind_the_same_grail_identity():
    by_name = {item["skill_name"]: item for item in SCOUT["skills"]}
    for item in SCOUT["workflows"]:
        skill = by_name[item["skill_name"]]
        assert item["rappid"] == skill["rappid"]
        assert item["default_artifact"] == "skill"
        assert item["grail_record"] == "SKILL.md"
        assert item["grail_url"].endswith("/SKILL.md")
        assert item["backup_agent"] == skill["backup_agent"]


def test_store_and_browser_brainstem_are_skill_first():
    store = (ROOT / "store.html").read_text(encoding="utf-8")
    assert "downloadToastedSkill" in store
    assert "decodeToastedSkill" in store
    assert "Toasted SKILL.md" in store
    assert "Rollback agent.py" in store
    assert "agentSourceFor" in store

    for filename in (
        "virtual-brainstem.html",
        "virtual-brainstem-summon.html",
    ):
        browser = (ROOT / filename).read_text(encoding="utf-8")
        assert "SCOUT_CATALOG_URL" in browser
        assert "DecompressionStream('gzip')" in browser
        assert "Toasted skill agent checksum mismatch" in browser
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    assert "/scout/catalog/catalog.json" in index
    assert "Download Toasted SKILL.md" in index
    assert "rollback .py" in index
    discover = (ROOT / "discover.html").read_text(encoding="utf-8")
    assert "Toasted SKILL.md" in discover
    assert "backup_agent_url" in discover
    api = json.loads((ROOT / "api.json").read_text())
    assert api["endpoints"]["skill_catalog"]["url"].endswith(
        "/scout/catalog/catalog.json"
    )
    assert api["endpoints"]["agent_file"]["description"].startswith(
        "Rollback"
    )
    grail = (ROOT / "grail.html").read_text(encoding="utf-8")
    assert "SCOUT_CATALOG_URL" in grail
    assert "Toasted SKILL.md" in grail
    assert "Rollback .py" in grail
    front = (ROOT / "front.html").read_text(encoding="utf-8")
    assert "Toasted skill" in front
    assert "rollback .py" in front


def test_pages_keeps_brainstem_installer_agent_abi():
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    assert "registry.json" in index
    assert "a._file" in index
    api = json.loads(
        (ROOT / "api" / "v1" / "agent" / "rapp__ping_agent.json").read_text()
    )
    assert api["backup_agent_url"].endswith("/agents/@rapp/ping_agent.py")
    assert api["py_url"] == api["backup_agent_url"]
    assert api["default_url"].endswith("/SKILL.md")


def test_federation_marks_singletons_as_rollback():
    federation = json.loads(
        (ROOT / "state" / "federation.json").read_text()
    )
    for item in federation["rapplications"]:
        assert item["default_artifact"] == "skill"
        assert item["rollback_artifact"] == "singleton-agent"
        assert item["scout_identity"] == item["manifest_name"]


def test_release_staging_makes_skill_zip_primary(tmp_path, monkeypatch):
    module = load_module(
        "_release_assets_skill_first",
        ROOT / "scripts" / "stage_release_assets.py",
    )
    source = tmp_path / "agents" / "@example" / "demo_agent.py"
    source.parent.mkdir(parents=True)
    source.write_text("print('demo')\n", encoding="utf-8")
    registry = tmp_path / "registry.json"
    registry.write_text(json.dumps({"agents": [{
        "name": "@example/demo",
        "_file": "agents/@example/demo_agent.py",
        "_install_filename": "rar_example_demo_agent.py",
    }]}))
    skill_dir = tmp_path / "scout" / "starter" / "skills" / "demo"
    (skill_dir / "rapp").mkdir(parents=True)
    (skill_dir / "scripts").mkdir()
    (skill_dir / "SKILL.md").write_text("# demo\n", encoding="utf-8")
    (skill_dir / "demo_agent.py").write_bytes(source.read_bytes())
    (skill_dir / "rapp" / "agent.lock.json").write_text("{}\n")
    (skill_dir / "scripts" / "run_agent.py").write_text("pass\n")
    catalog = tmp_path / "scout" / "catalog" / "catalog.json"
    catalog.parent.mkdir(parents=True)
    catalog.write_text(json.dumps({"skills": [{
        "identity": "@example/demo",
        "skill_name": "demo",
        "bundle": "starter",
    }]}))

    monkeypatch.setattr(module, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(module, "REGISTRY_FILE", registry)
    monkeypatch.setattr(module, "SCOUT_CATALOG", catalog)
    monkeypatch.setattr(module, "SCOUT_ROOT", tmp_path / "scout")
    out = tmp_path / "dist"
    assert module.stage(out) == 0

    manifest = json.loads((out / "release-assets.json").read_text())
    assert manifest["schema"] == "rar-release-assets/2.0"
    assert manifest["default_artifact"] == "skill"
    skill_asset = manifest["skill_assets"]["@example/demo"]
    assert manifest["default_assets"]["@example/demo"] == skill_asset
    assert manifest["assets"]["@example/demo"] == "rar_example_demo_agent.py"
    with zipfile.ZipFile(out / skill_asset) as archive:
        assert "SKILL.md" in archive.namelist()
        assert "demo_agent.py" in archive.namelist()


def test_sdk_installs_toasted_skill_by_default_path(tmp_path, monkeypatch):
    sdk = load_module("_skill_first_sdk", ROOT / "rapp_sdk.py")
    source = tmp_path / "source"
    source.mkdir()
    skill = source / "SKILL.md"
    runner = source / "run_agent.py"
    skill.write_text("# demo\n", encoding="utf-8")
    runner.write_text("print('ok')\n", encoding="utf-8")
    catalog = {"skills": [{
        "identity": "@example/demo",
        "skill_name": "demo",
        "files": [
            {
                "path": "SKILL.md",
                "url": skill.as_uri(),
                "sha256": hashlib.sha256(skill.read_bytes()).hexdigest(),
            },
            {
                "path": "scripts/run_agent.py",
                "url": runner.as_uri(),
                "sha256": hashlib.sha256(runner.read_bytes()).hexdigest(),
            },
        ],
    }]}
    monkeypatch.setattr(sdk, "fetch_skill_catalog", lambda: catalog)
    monkeypatch.setattr(sdk, "_get_token", lambda: None)
    monkeypatch.setattr(sdk, "track_download", lambda _name: True)

    installed = Path(
        sdk.install_skill("@example/demo", str(tmp_path / "skills"))
    )
    assert (installed / "SKILL.md").read_bytes() == skill.read_bytes()
    assert (installed / "scripts" / "run_agent.py").read_bytes() == (
        runner.read_bytes()
    )


def test_all_agent_producers_own_skill_identity_ledger():
    workflows = {
        name: (ROOT / ".github" / "workflows" / name).read_text()
        for name in (
            "approve-agent.yml",
            "approve-agent-batch.yml",
            "aggregate.yml",
            "build-scout-exports.yml",
        )
    }
    for name, workflow in workflows.items():
        assert "state/scout_skill_identities.json" in workflow, name
    for name in (
        "approve-agent.yml",
        "approve-agent-batch.yml",
        "aggregate.yml",
    ):
        assert "--mint-skill-identities" in workflows[name]
