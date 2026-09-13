import hashlib
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import check_notarized_changes as check


SOURCE = b'''__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@test/example_agent",
    "version": "1.0.0",
    "display_name": "Example",
    "description": "Example.",
    "author": "Test",
    "tags": [],
    "category": "general",
}
'''

SKILL = json.dumps(
    {
        "schema": "rar-skill/1.0",
        "artifact_type": "skill",
        "name": "@test/example-skill",
        "version": "1.0.0",
    },
    sort_keys=True,
).encode()


def evidence(tmp_path: Path, *, action: str, status: str):
    digest = check.canonical_sha256(SOURCE)
    revision = "a" * 64
    receipts = tmp_path / "receipts"
    receipts.mkdir()
    (receipts / f"{revision}.json").write_text(json.dumps({
        "revision_id": revision,
        "action": action,
        "agent": "@test/example_agent",
        "artifact": {"digest": digest},
    }))
    lifecycle = {
        "agents": {
            "@test/example_agent": {
                "status": status,
                "sha256": digest,
                "latest_receipt": f"rar_{revision}",
            }
        }
    }
    return lifecycle, receipts


def test_active_change_requires_matching_receipt(tmp_path):
    lifecycle, receipts = evidence(
        tmp_path,
        action="agent.update",
        status="active",
    )
    errors = check.validate_agent_change(
        status="M",
        path="agents/@test/example_agent.py",
        current_content=SOURCE,
        previous_content=SOURCE,
        lifecycle=lifecycle,
        receipts_dir=receipts,
    )
    assert errors == []


def test_direct_change_without_lifecycle_fails(tmp_path):
    errors = check.validate_agent_change(
        status="M",
        path="agents/@test/example_agent.py",
        current_content=SOURCE,
        previous_content=SOURCE,
        lifecycle={"agents": {}},
        receipts_dir=tmp_path,
    )
    assert any("without lifecycle evidence" in error for error in errors)


def test_delete_requires_tombstone_receipt(tmp_path):
    lifecycle, receipts = evidence(
        tmp_path,
        action="agent.delete",
        status="deleted",
    )
    errors = check.validate_agent_change(
        status="D",
        path="agents/@test/example_agent.py",
        current_content=None,
        previous_content=SOURCE,
        lifecycle=lifecycle,
        receipts_dir=receipts,
    )
    assert errors == []


def test_digest_tampering_fails(tmp_path):
    lifecycle, receipts = evidence(
        tmp_path,
        action="agent.update",
        status="active",
    )
    errors = check.validate_agent_change(
        status="M",
        path="agents/@test/example_agent.py",
        current_content=SOURCE + b"# tampered\n",
        previous_content=SOURCE,
        lifecycle=lifecycle,
        receipts_dir=receipts,
    )
    assert any("digest" in error for error in errors)


def skill_evidence(tmp_path: Path):
    digest = hashlib.sha256(SKILL).hexdigest()
    revision = "b" * 64
    receipts = tmp_path / "skill-receipts"
    receipts.mkdir()
    path = "skills/@test/example-skill/manifest.json"
    (receipts / f"{revision}.json").write_text(json.dumps({
        "schema": "rar-skill-receipt/1.0",
        "id": f"rar_skill_{revision}",
        "action": "skill.create",
        "skill": "@test/example-skill",
        "canonical_path": path,
        "artifact": {"digest": digest},
    }))
    lifecycle = {
        "skills": {
            "@test/example-skill": {
                "status": "active",
                "canonical_path": path,
                "sha256": digest,
                "latest_receipt": f"rar_skill_{revision}",
            }
        }
    }
    return lifecycle, receipts, path


def test_skill_change_requires_matching_front_door_receipt(tmp_path):
    lifecycle, receipts, path = skill_evidence(tmp_path)
    assert check.validate_skill_change(
        status="A",
        path=path,
        current_content=SKILL,
        lifecycle=lifecycle,
        receipts_dir=receipts,
    ) == []


def test_direct_skill_change_without_lifecycle_fails(tmp_path):
    errors = check.validate_skill_change(
        status="A",
        path="skills/@test/example-skill/manifest.json",
        current_content=SKILL,
        lifecycle={"skills": {}},
        receipts_dir=tmp_path,
    )
    assert any("without skill lifecycle evidence" in error for error in errors)


def test_skill_manifest_deletion_is_never_a_supported_mutation(tmp_path):
    errors = check.validate_skill_change(
        status="D",
        path="skills/@test/example-skill/manifest.json",
        current_content=None,
        lifecycle={"skills": {}},
        receipts_dir=tmp_path,
    )
    assert any("cannot be deleted" in error for error in errors)
