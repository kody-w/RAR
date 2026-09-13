"""Versioned skill submission, staging, update, and approval rules."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import apply_skill_mutation as apply
import process_issues as pi


SKILL_BYTES = (
    b"---\n"
    b"name: workspace-refresh\n"
    b"description: Refresh repository workspace files safely.\n"
    b"---\n"
    b"\n# Workspace Refresh\n"
)


def manifest(version: str = "1.0.0") -> dict:
    return {
        "schema": "rar-skill/1.0",
        "artifact_type": "skill",
        "name": "@testuser/workspace-refresh",
        "version": version,
        "display_name": "Workspace Refresh",
        "description": "Refresh a workspace additively without replacing its layout.",
        "author": "Test User",
        "tags": ["workspace", "maintenance"],
        "category": "devtools",
        "source": {
            "repository": "testuser/tools",
            "revision": "a" * 40,
            "entrypoint": "skills/workspace-refresh/SKILL.md",
            "files": [
                {
                    "path": "skills/workspace-refresh/SKILL.md",
                    "sha256": hashlib.sha256(SKILL_BYTES).hexdigest(),
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


@pytest.fixture(autouse=True)
def isolated_skill_state(tmp_path, monkeypatch):
    skills = tmp_path / "skills"
    staging = tmp_path / "staging"
    state = tmp_path / "state"
    skills.mkdir()
    staging.mkdir()
    state.mkdir()
    lifecycle = state / "skill_lifecycle.json"
    lifecycle.write_text(
        '{"schema":"rar-skill-lifecycle/1.0","skills":{},"updated_at":""}\n',
        encoding="utf-8",
    )

    monkeypatch.setattr(pi, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(pi, "SKILLS_DIR", skills)
    monkeypatch.setattr(pi, "STAGING_DIR", staging)
    monkeypatch.setattr(pi, "SKILL_STAGING_DIR", staging / "skill-requests")
    monkeypatch.setattr(pi, "STATE_DIR", state)
    monkeypatch.setattr(pi, "SKILL_REQUESTS_DIR", state / "skill-requests")
    monkeypatch.setattr(pi, "SKILL_LIFECYCLE_FILE", lifecycle)

    monkeypatch.setattr(apply, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(apply, "SKILLS_DIR", skills)
    monkeypatch.setattr(apply, "STAGING_DIR", staging / "skill-requests")
    monkeypatch.setattr(apply, "STATE_DIR", state)
    monkeypatch.setattr(apply, "LIFECYCLE_FILE", lifecycle)
    monkeypatch.setattr(apply, "RECEIPTS_DIR", state / "skill-receipts")
    monkeypatch.setattr(apply, "REQUESTS_DIR", state / "skill-requests")

    monkeypatch.setattr(pi.skill_catalog, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(pi.skill_catalog, "SKILLS_DIR", skills)
    monkeypatch.setattr(
        pi.skill_catalog,
        "SCOUT_CATALOG",
        tmp_path / "scout" / "catalog" / "catalog.json",
    )
    monkeypatch.setattr(pi.skill_catalog, "LIFECYCLE_FILE", lifecycle)
    monkeypatch.setattr(
        pi.skill_catalog,
        "RECEIPTS_DIR",
        state / "skill-receipts",
    )
    monkeypatch.setattr(
        pi.skill_catalog,
        "OUTPUT",
        tmp_path / "api" / "v1" / "skills.json",
    )
    monkeypatch.setattr(
        pi.skill_catalog,
        "fetch_source_files",
        lambda value: {value["source"]["entrypoint"]: SKILL_BYTES},
    )
    return tmp_path


def command(
    operation: str,
    artifact: dict,
    *,
    if_match: str = "",
    request_id: str = "req_skill_create",
) -> dict:
    preconditions = (
        {"if_none_match": "*"}
        if operation == "create"
        else {"if_match": f"sha256:{if_match}"}
    )
    return {
        "schema": pi.CHANGE_REQUEST_SCHEMA,
        "request_id": request_id,
        "idempotency_key": request_id,
        "operation": operation,
        "resource": {
            "kind": "skill",
            "id": artifact["name"],
        },
        "preconditions": preconditions,
        "payload": {
            "artifact": artifact,
            "artifact_sha256": (
                "sha256:" + pi.skill_catalog.manifest_sha256(artifact)
            ),
        },
    }


def stage(
    operation: str,
    artifact: dict,
    *,
    number: int,
    if_match: str = "",
) -> tuple[dict, dict]:
    request = command(
        operation,
        artifact,
        if_match=if_match,
        request_id=f"req_skill_{number}",
    )
    body = f"```json\n{json.dumps(request)}\n```"
    normalized = pi.normalize_change_request(pi.extract_json_from_body(body))
    normalized["payload"]["_issue_body"] = body
    normalized["payload"]["_context"] = {
        "issue_number": number,
        "issue_node_id": f"I_skill_{number}",
        "repository_id": 1234,
        "actor_id": 5678,
        "issue_updated_at": "2026-09-13T10:00:00Z",
    }
    result = pi.process(normalized, "testuser")
    event = {
        "issue": {
            "number": number,
            "body": body,
            "user": {"id": 5678, "login": "testuser"},
        },
        "sender": {"id": 9001, "login": "maintainer"},
    }
    return result, event


def test_versioned_parser_routes_skill_without_agent_fallback():
    request = command("create", manifest())
    parsed = pi.extract_json_from_body(
        f"```json\n{json.dumps(request)}\n```"
    )
    normalized = pi.normalize_change_request(parsed)
    assert normalized["action"] == "skill.create"
    assert normalized["payload"]["skill"] == "@testuser/workspace-refresh"
    assert "code" not in normalized["payload"]


def test_create_stages_exact_manifest_and_source_bytes(isolated_skill_state):
    result, _event = stage("create", manifest(), number=101)
    assert result["ok"] is True
    assert result["action"] == "skill.create"
    assert result["artifact"] == "@testuser/workspace-refresh"
    request_file = isolated_skill_state / result["file"]
    candidate = request_file.parent / "candidate.json"
    staged_source = (
        request_file.parent
        / "source"
        / "skills"
        / "workspace-refresh"
        / "SKILL.md"
    )
    assert candidate.read_bytes() == pi.skill_catalog.render_manifest(manifest())
    assert staged_source.read_bytes() == SKILL_BYTES
    assert not (
        isolated_skill_state
        / "skills"
        / "@testuser"
        / "workspace-refresh"
        / "manifest.json"
    ).exists()


def test_manifest_hash_mismatch_refuses_submission():
    request = command("create", manifest())
    request["payload"]["artifact_sha256"] = "sha256:" + ("0" * 64)
    result = pi.process(request, "testuser")
    assert "digest mismatch" in result["error"].lower()


def test_update_requires_hash_and_semver_increment(isolated_skill_state):
    target = (
        isolated_skill_state
        / "skills"
        / "@testuser"
        / "workspace-refresh"
        / "manifest.json"
    )
    target.parent.mkdir(parents=True)
    target.write_bytes(pi.skill_catalog.render_manifest(manifest()))

    missing_hash = pi.process(command("update", manifest("1.1.0")), "testuser")
    assert "if_match" in missing_hash["error"]

    same_version = pi.process(
        command(
            "update",
            manifest(),
            if_match=pi.sha256_bytes(target.read_bytes()),
        ),
        "testuser",
    )
    assert "greater than existing" in same_version["error"]

    result, _event = stage(
        "update",
        manifest("1.1.0"),
        number=102,
        if_match=pi.sha256_bytes(target.read_bytes()),
    )
    assert result["ok"] is True
    assert result["action"] == "skill.update"


def test_wrong_namespace_and_floating_revision_are_refused():
    wrong_namespace = manifest()
    wrong_namespace["name"] = "@someone-else/workspace-refresh"
    wrong_namespace["source"]["repository"] = "someone-else/tools"
    result = pi.process(command("create", wrong_namespace), "testuser")
    assert "Publisher must be '@testuser'" in result["error"]

    floating = manifest()
    floating["source"]["revision"] = "main"
    request = command("create", floating)
    result = pi.process(request, "testuser")
    assert "40-character commit" in result["error"]


def test_apply_publishes_only_manifest_and_receipt(isolated_skill_state):
    staged, event = stage("create", manifest(), number=201)
    request_file = apply.find_staged_request(event)
    result = apply.apply_request(
        request_file,
        approver_id=9001,
        approver_login="maintainer",
        workflow_run="42",
    )
    target = (
        isolated_skill_state
        / "skills"
        / "@testuser"
        / "workspace-refresh"
        / "manifest.json"
    )
    assert target.read_bytes() == pi.skill_catalog.render_manifest(manifest())
    assert not (target.parent / "SKILL.md").exists()
    receipt = json.loads(
        (isolated_skill_state / result["receipt"]).read_text()
    )
    assert receipt["artifact_type"] == "skill"
    assert receipt["source"]["revision"] == "a" * 40
    assert receipt["protocol_conformance"]["status"] == "not_assessed"
    assert receipt["artifact"]["digest"] == staged["manifest_sha256"]
    catalog = pi.skill_catalog.build_catalog()
    assert catalog["counts"]["reviewed_submissions"] == 1
    [published] = catalog["skills"]
    assert published["name"] == "@testuser/workspace-refresh"
    assert published["review"]["receipt"] == receipt["id"]


def test_apply_refuses_tampered_staged_source():
    _staged, event = stage("create", manifest(), number=202)
    request_file = apply.find_staged_request(event)
    source = (
        request_file.parent
        / "source"
        / "skills"
        / "workspace-refresh"
        / "SKILL.md"
    )
    source.write_bytes(source.read_bytes() + b"\nchanged\n")
    with pytest.raises(
        apply.SkillMutationError,
        match="source digest changed",
    ):
        apply.apply_request(
            request_file,
            approver_id=9001,
            approver_login="maintainer",
        )


def test_skill_front_door_is_wired_to_exact_revision_review():
    process_workflow = (
        ROOT / ".github" / "workflows" / "process-issues.yml"
    ).read_text(encoding="utf-8")
    approval_workflow = (
        ROOT / ".github" / "workflows" / "approve-skill.yml"
    ).read_text(encoding="utf-8")
    admin = (ROOT / "admin.html").read_text(encoding="utf-8")
    assert "skill-submission" in process_workflow
    assert "apply_skill_mutation.py" in approval_workflow
    assert "Issue body changed after approval was applied" in approval_workflow
    assert "check_skill_url_stability.py --update" in approval_workflow
    assert "build_skills_catalog.py" in approval_workflow
    assert "rar-notary-main" in approval_workflow
    assert "/tmp/" not in approval_workflow
    assert "skill-submission" in admin
