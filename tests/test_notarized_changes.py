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
