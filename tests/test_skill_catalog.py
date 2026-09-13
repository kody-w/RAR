"""Distinct static Skills catalog and UI contract."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "build_skills_catalog.py"


@pytest.fixture
def catalog_module():
    scripts = str(ROOT / "scripts")
    if scripts not in sys.path:
        sys.path.insert(0, scripts)
    spec = importlib.util.spec_from_file_location("_skill_catalog_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def source_bytes() -> bytes:
    return (
        b"---\n"
        b"name: workspace-refresh\n"
        b"description: Refresh a repository workspace safely.\n"
        b"---\n"
        b"\n# Workspace Refresh\n"
    )


def skill_manifest(module, *, version: str = "1.0.0") -> dict:
    data = source_bytes()
    return {
        "schema": module.SKILL_SCHEMA,
        "artifact_type": "skill",
        "name": "@tester/workspace-refresh",
        "version": version,
        "display_name": "Workspace Refresh",
        "description": "Refresh a repository workspace without replacing its layout.",
        "author": "Tester",
        "tags": ["workspace", "maintenance"],
        "category": "devtools",
        "source": {
            "repository": "tester/tools",
            "revision": "a" * 40,
            "entrypoint": "skills/workspace-refresh/SKILL.md",
            "files": [
                {
                    "path": "skills/workspace-refresh/SKILL.md",
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "media_type": "text/markdown",
                }
            ],
        },
        "install": {
            "strategy": "copy-files",
            "destination": "skills/workspace-refresh",
        },
        "compatibility": {"rapp_protocol": "optional"},
        "protocol_conformance": {
            "profile": None,
            "status": "not_assessed",
            "evidence": [],
        },
    }


def test_manifest_requires_skill_type_and_non_claiming_conformance(catalog_module):
    manifest = skill_manifest(catalog_module)
    assert catalog_module.validate_manifest(manifest) == []

    wrong_type = {**manifest, "artifact_type": "agent"}
    assert any(
        "artifact_type" in error
        for error in catalog_module.validate_manifest(wrong_type)
    )

    self_elevated = {
        **manifest,
        "protocol_conformance": {
            "profile": "RAPP/1",
            "status": "verified",
            "evidence": ["self-declared"],
        },
    }
    errors = catalog_module.validate_manifest(self_elevated)
    assert any("not_assessed" in error for error in errors)
    assert any("cannot self-assert" in error for error in errors)


@pytest.mark.parametrize(
    "mutation, expected",
    [
        (
            lambda value: value["source"].update({"revision": "main"}),
            "40-character commit",
        ),
        (
            lambda value: value["source"]["files"][0].update(
                {"path": "../SKILL.md"}
            ),
            "unsafe",
        ),
        (
            lambda value: value["source"]["files"].append(
                dict(value["source"]["files"][0])
            ),
            "unique",
        ),
        (
            lambda value: value.update({"quality_tier": "official"}),
            "Unsupported field",
        ),
    ],
)
def test_malformed_metadata_is_refused(
    catalog_module,
    mutation,
    expected,
):
    manifest = skill_manifest(catalog_module)
    mutation(manifest)
    assert any(
        expected in error
        for error in catalog_module.validate_manifest(manifest)
    )


def test_source_fetch_verifies_hash_and_frontmatter(catalog_module):
    manifest = skill_manifest(catalog_module)
    fetched = catalog_module.fetch_source_files(
        manifest,
        fetcher=lambda _url: source_bytes(),
    )
    assert fetched[manifest["source"]["entrypoint"]] == source_bytes()

    with pytest.raises(catalog_module.SkillMetadataError, match="SHA-256 mismatch"):
        catalog_module.fetch_source_files(
            manifest,
            fetcher=lambda _url: b"changed",
        )


def test_catalog_build_is_deterministic_and_links_projections(
    tmp_path,
    monkeypatch,
    catalog_module,
):
    skills_dir = tmp_path / "skills"
    manifest_path = skills_dir / "@tester" / "workspace-refresh" / "manifest.json"
    manifest_path.parent.mkdir(parents=True)
    manifest_path.write_bytes(
        catalog_module.render_manifest(skill_manifest(catalog_module))
    )
    manifest_digest = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    lifecycle_path = tmp_path / "state" / "skill_lifecycle.json"
    receipt_dir = tmp_path / "state" / "skill-receipts"
    receipt_dir.mkdir(parents=True)
    lifecycle_path.write_text(
        json.dumps(
            {
                "schema": "rar-skill-lifecycle/1.0",
                "skills": {
                    "@tester/workspace-refresh": {
                        "status": "active",
                        "version": "1.0.0",
                        "canonical_path": (
                            "skills/@tester/workspace-refresh/manifest.json"
                        ),
                        "sha256": manifest_digest,
                        "latest_receipt": "rar_skill_revision1",
                    }
                },
            }
        ),
        encoding="utf-8",
    )
    (receipt_dir / "revision1.json").write_text(
        json.dumps(
            {
                "schema": "rar-skill-receipt/1.0",
                "id": "rar_skill_revision1",
                "revision_id": "revision1",
                "skill": "@tester/workspace-refresh",
                "canonical_path": (
                    "skills/@tester/workspace-refresh/manifest.json"
                ),
                "artifact": {"digest": manifest_digest},
                "created_at": "2026-09-13T00:00:00Z",
            }
        ),
        encoding="utf-8",
    )
    scout_path = tmp_path / "scout" / "catalog" / "catalog.json"
    scout_path.parent.mkdir(parents=True)
    scout_path.write_text(
        json.dumps(
            {
                "schema": "rar-scout-catalog/1.0",
                "toaster": {"commit": "b" * 40, "sha256": "c" * 64},
                "skills": [
                    {
                        "identity": "@tester/source_agent",
                        "skill_name": "rar-tester-source",
                        "source_kind": "rar-agent",
                        "source_commit": "d" * 40,
                        "source_sha256": "e" * 64,
                        "description": "Projected source agent.",
                        "version": "1.0.0",
                        "channel": "native",
                        "bundle": "native-01",
                        "import_url": (
                            "https://github.com/kody-w/RAR/tree/main/"
                            "scout/bundles/native-01"
                        ),
                        "files": [
                            {
                                "path": "SKILL.md",
                                "sha256": "f" * 64,
                                "url": (
                                    "https://raw.githubusercontent.com/kody-w/"
                                    "RAR/main/scout/bundles/native-01/skills/"
                                    "rar-tester-source/SKILL.md"
                                ),
                            }
                        ],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(catalog_module, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(catalog_module, "SKILLS_DIR", skills_dir)
    monkeypatch.setattr(catalog_module, "SCOUT_CATALOG", scout_path)
    monkeypatch.setattr(catalog_module, "LIFECYCLE_FILE", lifecycle_path)
    monkeypatch.setattr(catalog_module, "RECEIPTS_DIR", receipt_dir)

    first = catalog_module.build_catalog()
    second = catalog_module.build_catalog()
    assert first == second
    assert first["counts"] == {
        "total": 2,
        "reviewed_submissions": 1,
        "generated_projections": 1,
    }
    projected = next(
        item
        for item in first["skills"]
        if item["catalog_origin"] == "generated-projection"
    )
    assert projected["artifact_type"] == "skill"
    assert projected["relationships"] == [
        {
            "type": "projection_of",
            "artifact_type": "agent",
            "name": "@tester/source_agent",
        }
    ]


def test_direct_manifest_without_front_door_receipt_is_refused(
    tmp_path,
    monkeypatch,
    catalog_module,
):
    skills_dir = tmp_path / "skills"
    manifest_path = skills_dir / "@tester" / "workspace-refresh" / "manifest.json"
    manifest_path.parent.mkdir(parents=True)
    manifest_path.write_bytes(
        catalog_module.render_manifest(skill_manifest(catalog_module))
    )
    lifecycle = tmp_path / "state" / "skill_lifecycle.json"
    lifecycle.parent.mkdir()
    lifecycle.write_text(
        '{"schema":"rar-skill-lifecycle/1.0","skills":{}}\n',
        encoding="utf-8",
    )
    monkeypatch.setattr(catalog_module, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(catalog_module, "SKILLS_DIR", skills_dir)
    monkeypatch.setattr(catalog_module, "SCOUT_CATALOG", tmp_path / "missing.json")
    monkeypatch.setattr(catalog_module, "LIFECYCLE_FILE", lifecycle)
    monkeypatch.setattr(
        catalog_module,
        "RECEIPTS_DIR",
        tmp_path / "state" / "skill-receipts",
    )
    with pytest.raises(
        catalog_module.SkillMetadataError,
        match="front-door lifecycle",
    ):
        catalog_module.build_catalog()


def test_committed_catalog_is_skill_only_and_agent_catalog_is_agent_only():
    skills = json.loads((ROOT / "api" / "v1" / "skills.json").read_text())
    agents = json.loads((ROOT / "api" / "v1" / "catalog.json").read_text())
    registry = json.loads((ROOT / "registry.json").read_text())

    assert skills["schema"] == "rar-skills-catalog/1.0"
    assert skills["skills"]
    assert all(item["artifact_type"] == "skill" for item in skills["skills"])
    assert all(
        item["protocol_conformance"]["status"] == "not_assessed"
        for item in skills["skills"]
    )
    assert all(item["artifact_type"] == "agent" for item in agents["agents"])
    assert all(
        item["protocol_conformance"]["status"] == "not_assessed"
        for item in agents["agents"]
    )
    assert all(
        str(item.get("_file", "")).startswith("agents/")
        for item in registry["agents"]
    )
    assert not any(
        item["name"].startswith("@rar-scout/")
        for item in registry["agents"]
    )


def test_skills_ui_reads_only_committed_static_snapshot():
    html = (ROOT / "skills.html").read_text(encoding="utf-8")
    assert "api/v1/skills.json" in html
    assert "rar-skills-catalog/1.0" in html
    assert "artifact_type" in html
    assert "protocol conformance" in html.lower()
    assert "api.github.com" not in html
    assert "generated projection" in html.lower()
    assert 'id="search"' in html

    index = (ROOT / "index.html").read_text(encoding="utf-8")
    store = (ROOT / "store.html").read_text(encoding="utf-8")
    assert 'href="skills.html"' in index
    assert 'href="skills.html"' in store
    assert "const skills = federation.skills" not in index
    assert "const skills = federation.skills" not in store
