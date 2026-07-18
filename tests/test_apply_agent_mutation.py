import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import apply_agent_mutation as apply
import process_issues as pi
from tests.test_process_issues import VALID_AGENT_CODE


@pytest.fixture
def mutation_repo(tmp_path, monkeypatch):
    agents = tmp_path / "agents"
    staging = tmp_path / "staging"
    state = tmp_path / "state"
    agents.mkdir()
    staging.mkdir()
    state.mkdir()
    lifecycle = state / "agent_lifecycle.json"
    lifecycle.write_text('{"agents": {}, "updated_at": ""}\n')

    for module in (pi, apply):
        monkeypatch.setattr(module, "REPO_ROOT", tmp_path)
        monkeypatch.setattr(module, "AGENTS_DIR", agents)
        monkeypatch.setattr(module, "STAGING_DIR", staging)
        monkeypatch.setattr(module, "STATE_DIR", state)
        monkeypatch.setattr(module, "LIFECYCLE_FILE", lifecycle)
    monkeypatch.setattr(apply, "RECEIPTS_DIR", state / "receipts")
    monkeypatch.setattr(apply, "REQUESTS_DIR", state / "requests")
    return tmp_path


def issue_context(number: int, body: str) -> tuple[dict, dict]:
    context = {
        "issue_number": number,
        "issue_node_id": f"I_kwDO{number}",
        "repository_id": 1234,
        "actor_id": 5678,
        "issue_updated_at": "2026-07-18T20:00:00Z",
    }
    event = {
        "issue": {
            "number": number,
            "node_id": context["issue_node_id"],
            "body": body,
            "user": {"id": 5678, "login": "testuser"},
        },
        "sender": {"id": 9001, "login": "maintainer"},
    }
    return context, event


def stage(code: str, number: int = 101, operation: str = "submit") -> tuple[dict, dict]:
    body = f"submission-{number}-{pi.sha256_bytes(code.encode())}"
    context, event = issue_context(number, body)
    payload = {
        "code": code,
        "_operation": operation,
        "_issue_body": body,
        "_context": context,
    }
    result = pi.handle_submit_agent(payload, "testuser")
    assert result["ok"] is True
    return result, event


def test_create_applies_exact_revision_and_receipt(mutation_repo):
    result, event = stage(VALID_AGENT_CODE)
    request_file = apply.find_staged_request(event)
    applied = apply.apply_request(
        request_file,
        approver_id=9001,
        approver_login="maintainer",
        workflow_run="42",
    )
    agent = mutation_repo / "agents/@testuser/my_agent.py"
    assert agent.read_text() == VALID_AGENT_CODE
    assert applied["status"] == "notarized"
    receipt = json.loads((mutation_repo / applied["receipt"]).read_text())
    assert receipt["artifact"]["digest"] == pi.sha256_bytes(agent.read_bytes())
    assert receipt["submission"]["github_id"] == 5678
    assert receipt["acceptance"]["github_id"] == 9001
    assert not request_file.parent.exists()


def test_issue_body_must_match_staged_revision(mutation_repo):
    _, event = stage(VALID_AGENT_CODE)
    event["issue"]["body"] = "edited after review"
    with pytest.raises(apply.MutationError, match="found 0"):
        apply.find_staged_request(event)


def test_update_rechecks_base_digest(mutation_repo):
    namespace = pi.AGENTS_DIR / "@testuser"
    namespace.mkdir(parents=True)
    active = namespace / "my_agent.py"
    active.write_text(VALID_AGENT_CODE)
    update = VALID_AGENT_CODE.replace('"1.0.0"', '"1.1.0"')
    _, event = stage(update, operation="update")
    request_file = apply.find_staged_request(event)
    active.write_text(VALID_AGENT_CODE + "\n# changed after review\n")
    with pytest.raises(apply.MutationError, match="Base digest changed"):
        apply.apply_request(
            request_file,
            approver_id=9001,
            approver_login="maintainer",
        )


def test_delete_writes_tombstone_and_receipt(mutation_repo):
    namespace = pi.AGENTS_DIR / "@testuser"
    namespace.mkdir(parents=True)
    active = namespace / "my_agent.py"
    active.write_text(VALID_AGENT_CODE)
    body = "delete-request"
    context, event = issue_context(102, body)
    staged = pi.handle_delete_agent({
        "agent": "@testuser/my_agent",
        "if_match": f"sha256:{pi.sha256_bytes(active.read_bytes())}",
        "reason": "retired",
        "_issue_body": body,
        "_context": context,
    }, "testuser")
    assert staged["ok"] is True
    request_file = apply.find_staged_request(event)
    result = apply.apply_request(
        request_file,
        approver_id=9001,
        approver_login="maintainer",
    )
    assert result["status"] == "deleted"
    assert not active.exists()
    lifecycle = json.loads(pi.LIFECYCLE_FILE.read_text())
    assert lifecycle["agents"]["@testuser/my_agent"]["status"] == "deleted"


def test_malformed_title_cannot_change_target(mutation_repo):
    _, event = stage(VALID_AGENT_CODE)
    event["issue"]["title"] = "[RAR] malformed title"
    request_file = apply.find_staged_request(event)
    result = apply.apply_request(
        request_file,
        approver_id=9001,
        approver_login="maintainer",
    )
    assert result["agent"] == "@testuser/my_agent"


def test_revision_digest_is_recomputed_before_apply(mutation_repo):
    result, event = stage(VALID_AGENT_CODE)
    request_file = apply.find_staged_request(event)
    request = json.loads(request_file.read_text())
    candidate = request_file.parent / "candidate.py"
    tampered = candidate.read_text() + "\n# changed after staging\n"
    candidate.write_text(tampered)
    request["candidate_sha256"] = pi.sha256_bytes(tampered.encode())
    request_file.write_text(json.dumps(request))
    with pytest.raises(apply.MutationError, match="revision digest"):
        apply.apply_request(
            request_file,
            approver_id=9001,
            approver_login="maintainer",
        )


def test_agent_identity_derives_target_path(mutation_repo):
    _, event = stage(VALID_AGENT_CODE)
    request_file = apply.find_staged_request(event)
    request = json.loads(request_file.read_text())
    request["publisher"] = "@other"
    request["slug"] = "other_agent"
    request["canonical_path"] = "agents/@other/other_agent.py"
    request["revision_id"] = pi.mutation_revision_id(request)
    request_file.write_text(json.dumps(request))
    with pytest.raises(
        apply.MutationError,
        match="request and revision IDs|does not match agent identity",
    ):
        apply.apply_request(
            request_file,
            approver_id=9001,
            approver_login="maintainer",
        )


def test_existing_receipt_makes_replay_noop(mutation_repo):
    _, event = stage(VALID_AGENT_CODE)
    request_file = apply.find_staged_request(event)
    result = apply.apply_request(
        request_file,
        approver_id=9001,
        approver_login="maintainer",
    )
    receipt_file = mutation_repo / result["receipt"]
    assert receipt_file.exists()
    archived_request = apply.find_staged_request(event)
    replay = apply.apply_request(
        archived_request,
        approver_id=9001,
        approver_login="maintainer",
    )
    assert replay["already_applied"] is True


def test_replay_rejects_incomplete_projection(mutation_repo):
    _, event = stage(VALID_AGENT_CODE)
    request_file = apply.find_staged_request(event)
    apply.apply_request(
        request_file,
        approver_id=9001,
        approver_login="maintainer",
    )
    lifecycle = json.loads(pi.LIFECYCLE_FILE.read_text())
    lifecycle["agents"].clear()
    pi.LIFECYCLE_FILE.write_text(json.dumps(lifecycle))
    archived_request = apply.find_staged_request(event)
    with pytest.raises(apply.MutationError, match="receipt ancestry"):
        apply.apply_request(
            archived_request,
            approver_id=9001,
            approver_login="maintainer",
        )


def test_restore_cas_binds_exact_tombstone(mutation_repo):
    _, create_event = stage(VALID_AGENT_CODE, number=301, operation="create")
    apply.apply_request(
        apply.find_staged_request(create_event),
        approver_id=9001,
        approver_login="maintainer",
    )
    active = pi.AGENTS_DIR / "@testuser/my_agent.py"
    delete_body = "delete-302"
    delete_context, delete_event = issue_context(302, delete_body)
    pi.handle_delete_agent({
        "agent": "@testuser/my_agent",
        "if_match": f"sha256:{pi.sha256_bytes(active.read_bytes())}",
        "reason": "CAS test",
        "_issue_body": delete_body,
        "_context": delete_context,
    }, "testuser")
    apply.apply_request(
        apply.find_staged_request(delete_event),
        approver_id=9001,
        approver_login="maintainer",
    )
    restore_code = VALID_AGENT_CODE.replace('"1.0.0"', '"1.1.0"')
    _, restore_event = stage(restore_code, number=303, operation="restore")
    restore_request = apply.find_staged_request(restore_event)
    lifecycle = json.loads(pi.LIFECYCLE_FILE.read_text())
    lifecycle["agents"]["@testuser/my_agent"]["latest_receipt"] = "rar_other"
    pi.LIFECYCLE_FILE.write_text(json.dumps(lifecycle))
    with pytest.raises(apply.MutationError, match="Lifecycle state changed"):
        apply.apply_request(
            restore_request,
            approver_id=9001,
            approver_login="maintainer",
        )


def test_applied_idempotency_key_replays_before_state_checks(mutation_repo):
    body = "versioned-create"
    context, event = issue_context(401, body)
    digest = pi.sha256_bytes(VALID_AGENT_CODE.encode())
    payload = {
        "code": VALID_AGENT_CODE,
        "agent": "@testuser/my_agent",
        "source_sha256": f"sha256:{digest}",
        "if_none_match": "*",
        "idempotency_key": "applied-create-key",
        "_versioned": True,
        "_operation": "create",
        "_issue_body": body,
        "_context": context,
    }
    staged = pi.handle_submit_agent(payload, "testuser")
    assert staged["ok"] is True
    apply.apply_request(
        apply.find_staged_request(event),
        approver_id=9001,
        approver_login="maintainer",
    )

    retry_context, _retry_event = issue_context(402, "retry transport")
    retry = pi.handle_submit_agent({
        **payload,
        "_issue_body": "retry transport",
        "_context": retry_context,
    }, "testuser")
    assert retry["ok"] is True
    assert retry["status"] == "duplicate"
    assert retry["request_id"] == staged["request_id"]


def test_historical_receipt_replays_after_later_update(mutation_repo):
    _, create_event = stage(VALID_AGENT_CODE, number=501, operation="create")
    create_request = apply.find_staged_request(create_event)
    create_result = apply.apply_request(
        create_request,
        approver_id=9001,
        approver_login="maintainer",
    )
    update_code = VALID_AGENT_CODE.replace('"1.0.0"', '"1.1.0"')
    _, update_event = stage(update_code, number=502, operation="update")
    apply.apply_request(
        apply.find_staged_request(update_event),
        approver_id=9001,
        approver_login="maintainer",
    )
    historical_request = apply.find_staged_request(create_event)
    replay = apply.apply_request(
        historical_request,
        approver_id=9001,
        approver_login="maintainer",
    )
    assert replay["already_applied"] is True
    assert replay["revision_id"] == create_result["revision_id"]


def test_nested_card_update_keeps_registered_path(mutation_repo):
    nested = pi.AGENTS_DIR / "@testuser" / "vertical" / "stack"
    nested.mkdir(parents=True)
    active = nested / "nested_agent.py.card"
    source = VALID_AGENT_CODE.replace(
        "@testuser/my_agent",
        "@testuser/nested_agent",
    )
    active.write_text(source)
    update = source.replace('"1.0.0"', '"1.1.0"')
    body = "nested-card-update"
    context, event = issue_context(601, body)
    staged = pi.handle_submit_agent({
        "code": update,
        "agent": "@testuser/nested_agent",
        "source_sha256": f"sha256:{pi.sha256_bytes(update.encode())}",
        "if_match": f"sha256:{pi.sha256_bytes(active.read_bytes())}",
        "idempotency_key": "nested-card-apply",
        "_versioned": True,
        "_operation": "update",
        "_issue_body": body,
        "_context": context,
    }, "testuser")
    assert staged["ok"] is True
    apply.apply_request(
        apply.find_staged_request(event),
        approver_id=9001,
        approver_login="maintainer",
    )
    assert '"version": "1.1.0"' in active.read_text()
    assert not (pi.AGENTS_DIR / "@testuser/nested_agent.py").exists()


def test_full_create_read_update_delete_restore_lifecycle(mutation_repo):
    _, create_event = stage(VALID_AGENT_CODE, number=201, operation="create")
    apply.apply_request(
        apply.find_staged_request(create_event),
        approver_id=9001,
        approver_login="maintainer",
    )
    first_read = pi.handle_read_agent(
        {"agent": "@testuser/my_agent"},
        "reader",
    )
    assert first_read["status"] == "active"
    assert first_read["version"] == "1.0.0"

    update_code = VALID_AGENT_CODE.replace('"1.0.0"', '"1.1.0"')
    _, update_event = stage(update_code, number=202, operation="update")
    apply.apply_request(
        apply.find_staged_request(update_event),
        approver_id=9001,
        approver_login="maintainer",
    )
    assert pi.handle_read_agent(
        {"agent": "@testuser/my_agent"},
        "reader",
    )["version"] == "1.1.0"

    active = pi.AGENTS_DIR / "@testuser/my_agent.py"
    delete_body = "delete-203"
    delete_context, delete_event = issue_context(203, delete_body)
    deletion = pi.handle_delete_agent({
        "agent": "@testuser/my_agent",
        "if_match": f"sha256:{pi.sha256_bytes(active.read_bytes())}",
        "reason": "Lifecycle test",
        "_issue_body": delete_body,
        "_context": delete_context,
    }, "testuser")
    assert deletion["ok"] is True
    apply.apply_request(
        apply.find_staged_request(delete_event),
        approver_id=9001,
        approver_login="maintainer",
    )
    deleted_read = pi.handle_read_agent(
        {"agent": "@testuser/my_agent"},
        "reader",
    )
    assert deleted_read["status"] == "deleted"

    restore_code = VALID_AGENT_CODE.replace('"1.0.0"', '"1.2.0"')
    _, restore_event = stage(restore_code, number=204, operation="restore")
    restored = apply.apply_request(
        apply.find_staged_request(restore_event),
        approver_id=9001,
        approver_login="maintainer",
    )
    assert restored["status"] == "notarized"
    restore_receipt = json.loads((mutation_repo / restored["receipt"]).read_text())
    assert restore_receipt["previous"]["version"] == "1.1.0"
    assert restore_receipt["previous"]["digest"] == deleted_read["lifecycle"]["sha256"]
    final_read = pi.handle_read_agent(
        {"agent": "@testuser/my_agent"},
        "reader",
    )
    assert final_read["status"] == "active"
    assert final_read["version"] == "1.2.0"
    assert len(list(apply.RECEIPTS_DIR.glob("*.json"))) == 4
