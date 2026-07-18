"""
Tests for the GitHub Issues processing pipeline.

Covers: vote, review, submit_agent actions, JSON parsing, validation.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
import shutil
import pytest
from pathlib import Path

# Add scripts/ to path so we can import process_issues
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import process_issues as pi


# ──────────────────────────────────────────────────────────────────────
# Fixtures
# ──────────────────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def isolated_state(tmp_path, monkeypatch):
    """Redirect all state I/O to a temp directory."""
    state_dir = tmp_path / "state"
    state_dir.mkdir()
    agents_dir = tmp_path / "agents"
    agents_dir.mkdir()
    staging_dir = tmp_path / "staging"
    staging_dir.mkdir()

    # Write empty state files
    (state_dir / "votes.json").write_text(json.dumps({"agents": {}, "updated_at": ""}))
    (state_dir / "reviews.json").write_text(json.dumps({"agents": {}, "updated_at": ""}))
    (state_dir / "agent_lifecycle.json").write_text(
        json.dumps({"agents": {}, "updated_at": ""})
    )

    monkeypatch.setattr(pi, "STATE_DIR", state_dir)
    monkeypatch.setattr(pi, "AGENTS_DIR", agents_dir)
    monkeypatch.setattr(pi, "STAGING_DIR", staging_dir)
    monkeypatch.setattr(pi, "VOTES_FILE", state_dir / "votes.json")
    monkeypatch.setattr(pi, "REVIEWS_FILE", state_dir / "reviews.json")
    monkeypatch.setattr(pi, "LIFECYCLE_FILE", state_dir / "agent_lifecycle.json")
    monkeypatch.setattr(pi, "REPO_ROOT", tmp_path)

    return tmp_path


# ──────────────────────────────────────────────────────────────────────
# JSON parsing
# ──────────────────────────────────────────────────────────────────────

class TestExtractJson:
    def test_raw_json(self):
        body = '{"action": "vote", "payload": {"agent": "@test/a", "direction": "up"}}'
        result = pi.extract_json_from_body(body)
        assert result["action"] == "vote"

    def test_fenced_json(self):
        body = 'Some text\n```json\n{"action": "vote"}\n```\nmore text'
        result = pi.extract_json_from_body(body)
        assert result["action"] == "vote"

    def test_fenced_json_preserves_markdown_fences_inside_source(self):
        command = {
            "schema": pi.CHANGE_REQUEST_SCHEMA,
            "operation": "create",
            "resource": {"kind": "agent", "id": "@test/agent"},
            "payload": {
                "source": {
                    "content": '"""Example\\n```python\\nprint(1)\\n```\\n"""',
                    "sha256": "sha256:test",
                }
            },
        }
        body = f"```json\n{json.dumps(command, indent=2)}\n```"
        result = pi.extract_json_from_body(body)
        assert "```python" in result["payload"]["source"]["content"]

    def test_versioned_source_url_is_not_downgraded_to_legacy(self, monkeypatch):
        monkeypatch.setattr(
            pi,
            "_fetch_attachment",
            lambda _url: pytest.fail("JSON parsing must precede URL fetching"),
        )
        command = {
            "schema": pi.CHANGE_REQUEST_SCHEMA,
            "operation": "update",
            "resource": {"kind": "agent", "id": "@test/agent"},
            "preconditions": {"if_match": "sha256:" + ("a" * 64)},
            "payload": {
                "source": {
                    "url": "https://gist.githubusercontent.com/u/g/raw/s/a.py",
                    "sha256": "sha256:" + ("b" * 64),
                }
            },
        }
        body = f"```json\n{json.dumps(command)}\n```"
        assert pi.extract_json_from_body(body) == command

    def test_empty_body_raises(self):
        with pytest.raises(ValueError, match="empty"):
            pi.extract_json_from_body("")

    def test_invalid_json_raises(self):
        with pytest.raises((ValueError, json.JSONDecodeError)):
            pi.extract_json_from_body("this is not json")

    def test_whitespace_body_raises(self):
        with pytest.raises(ValueError, match="empty"):
            pi.extract_json_from_body("   \n  ")


# ──────────────────────────────────────────────────────────────────────
# Dispatch / unknown actions
# ──────────────────────────────────────────────────────────────────────

class TestDispatch:
    def test_unknown_action(self):
        result = pi.process({"action": "nonexistent"}, "user1")
        assert "error" in result
        assert "Unknown action" in result["error"]

    def test_missing_action(self):
        result = pi.process({}, "user1")
        assert "error" in result

    def test_invalid_payload_type(self):
        result = pi.process({"action": "vote", "payload": "not-a-dict"}, "user1")
        assert "error" in result

    def test_internal_mutation_action_requires_versioned_envelope(self):
        result = pi.process({
            "action": "agent.update",
            "payload": {"code": VALID_AGENT_CODE},
        }, "testuser")
        assert "validated" in result["error"].lower()


# ──────────────────────────────────────────────────────────────────────
# Vote action
# ──────────────────────────────────────────────────────────────────────

class TestVote:
    def test_upvote(self):
        result = pi.handle_vote({"agent": "@test/agent-a", "direction": "up"}, "user1")
        assert result["ok"] is True
        assert result["score"] == 1

    def test_downvote(self):
        result = pi.handle_vote({"agent": "@test/agent-a", "direction": "down"}, "user1")
        assert result["ok"] is True
        assert result["score"] == -1

    def test_toggle_vote_off(self):
        pi.handle_vote({"agent": "@test/agent-a", "direction": "up"}, "user1")
        result = pi.handle_vote({"agent": "@test/agent-a", "direction": "up"}, "user1")
        assert result["ok"] is True
        assert result["score"] == 0

    def test_switch_vote_direction(self):
        pi.handle_vote({"agent": "@test/agent-a", "direction": "up"}, "user1")
        result = pi.handle_vote({"agent": "@test/agent-a", "direction": "down"}, "user1")
        assert result["ok"] is True
        assert result["score"] == -1

    def test_multiple_voters(self):
        pi.handle_vote({"agent": "@test/agent-a", "direction": "up"}, "user1")
        pi.handle_vote({"agent": "@test/agent-a", "direction": "up"}, "user2")
        result = pi.handle_vote({"agent": "@test/agent-a", "direction": "up"}, "user3")
        assert result["score"] == 3

    def test_invalid_agent_name(self):
        result = pi.handle_vote({"agent": "bad-name", "direction": "up"}, "user1")
        assert "error" in result

    def test_invalid_direction(self):
        result = pi.handle_vote({"agent": "@test/a", "direction": "sideways"}, "user1")
        assert "error" in result

    def test_vote_persists_to_file(self):
        pi.handle_vote({"agent": "@test/agent-a", "direction": "up"}, "user1")
        votes = pi.load_json(pi.VOTES_FILE)
        assert votes["agents"]["@test/agent-a"]["up"] == 1
        assert votes["agents"]["@test/agent-a"]["voters"]["user1"] == "up"

    def test_vote_default_direction_is_up(self):
        result = pi.handle_vote({"agent": "@test/agent-a"}, "user1")
        assert result["ok"] is True
        assert result["score"] == 1

    def test_issue_redelivery_is_idempotent(self):
        payload = {
            "agent": "@test/agent-a",
            "direction": "up",
            "_issue_body": "same vote",
            "_context": {
                "issue_node_id": "I_vote",
                "source_body_sha256": pi.sha256_bytes(b"same vote"),
            },
        }
        first = pi.handle_vote(payload, "user1")
        second = pi.handle_vote(payload, "user1")
        assert first == second
        assert second["score"] == 1


# ──────────────────────────────────────────────────────────────────────
# Review action
# ──────────────────────────────────────────────────────────────────────

class TestReview:
    def test_valid_review(self):
        result = pi.handle_review({
            "agent": "@test/agent-a", "rating": 5, "text": "Great agent!"
        }, "user1")
        assert result["ok"] is True

    def test_review_persists(self):
        pi.handle_review({
            "agent": "@test/agent-a", "rating": 4, "text": "Solid work"
        }, "user1")
        reviews = pi.load_json(pi.REVIEWS_FILE)
        agent_reviews = reviews["agents"]["@test/agent-a"]
        assert len(agent_reviews) == 1
        assert agent_reviews[0]["user"] == "user1"
        assert agent_reviews[0]["rating"] == 4

    def test_review_replaces_same_user(self):
        pi.handle_review({
            "agent": "@test/agent-a", "rating": 3, "text": "Okay"
        }, "user1")
        pi.handle_review({
            "agent": "@test/agent-a", "rating": 5, "text": "Updated: great!"
        }, "user1")
        reviews = pi.load_json(pi.REVIEWS_FILE)
        agent_reviews = reviews["agents"]["@test/agent-a"]
        assert len(agent_reviews) == 1
        assert agent_reviews[0]["rating"] == 5

    def test_multiple_reviewers(self):
        pi.handle_review({"agent": "@test/a", "rating": 5, "text": "A"}, "user1")
        pi.handle_review({"agent": "@test/a", "rating": 3, "text": "B"}, "user2")
        reviews = pi.load_json(pi.REVIEWS_FILE)
        assert len(reviews["agents"]["@test/a"]) == 2

    def test_invalid_rating_too_high(self):
        result = pi.handle_review({
            "agent": "@test/a", "rating": 6, "text": "Too high"
        }, "user1")
        assert "error" in result

    def test_invalid_rating_too_low(self):
        result = pi.handle_review({
            "agent": "@test/a", "rating": 0, "text": "Too low"
        }, "user1")
        assert "error" in result

    def test_invalid_rating_not_number(self):
        result = pi.handle_review({
            "agent": "@test/a", "rating": "five", "text": "Not a number"
        }, "user1")
        assert "error" in result

    def test_empty_text(self):
        result = pi.handle_review({
            "agent": "@test/a", "rating": 5, "text": ""
        }, "user1")
        assert "error" in result

    def test_text_too_long(self):
        result = pi.handle_review({
            "agent": "@test/a", "rating": 5, "text": "x" * 2001
        }, "user1")
        assert "error" in result

    def test_invalid_agent(self):
        result = pi.handle_review({
            "agent": "bad", "rating": 5, "text": "Hello"
        }, "user1")
        assert "error" in result

    def test_issue_redelivery_preserves_review(self):
        payload = {
            "agent": "@test/a",
            "rating": 5,
            "text": "Stable review",
            "_issue_body": "same review",
            "_context": {
                "issue_node_id": "I_review",
                "source_body_sha256": pi.sha256_bytes(b"same review"),
            },
        }
        first = pi.handle_review(payload, "user1")
        saved = pi.load_json(pi.REVIEWS_FILE)
        timestamp = saved["agents"]["@test/a"][0]["timestamp"]
        second = pi.handle_review(payload, "user1")
        assert first == second
        assert pi.load_json(pi.REVIEWS_FILE)["agents"]["@test/a"][0]["timestamp"] == timestamp


# ──────────────────────────────────────────────────────────────────────
# Submit agent action
# ──────────────────────────────────────────────────────────────────────

VALID_AGENT_CODE = '''"""Test agent."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@testuser/my_agent",
    "version": "1.0.0",
    "display_name": "My Agent",
    "description": "A test agent",
    "author": "Test User",
    "tags": ["test"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": [],
}


class BasicAgent:
    pass


class MyAgent(BasicAgent):
    def perform(self, **kwargs) -> str:
        return "hello"
'''


class TestSubmitAgent:
    """Agent submission tests."""

    def test_valid_submission(self):
        result = pi.handle_submit_agent({"code": VALID_AGENT_CODE}, "testuser")
        assert result["ok"] is True
        assert result["agent"] == "@testuser/my_agent"
        assert result["status"] == "pending_review"
        # Verify file was written to staging, NOT agents
        request_file = pi.REPO_ROOT / result["file"]
        staging_file = request_file.parent / "candidate.py"
        assert request_file.exists()
        assert staging_file.exists()
        assert "__manifest__" in staging_file.read_text()
        agent_file = pi.AGENTS_DIR / "@testuser" / "my_agent.py"
        assert not agent_file.exists(), "Should be in staging, not agents"

    def test_empty_code(self):
        result = pi.handle_submit_agent({"code": ""}, "testuser")
        assert "error" in result

    def test_no_manifest(self):
        result = pi.handle_submit_agent({"code": "print('hello')"}, "testuser")
        assert "error" in result

    def test_invalid_manifest_missing_fields(self):
        code = '''__manifest__ = {"name": "@testuser/x"}'''
        result = pi.handle_submit_agent({"code": code}, "testuser")
        assert "error" in result

    def test_wrong_publisher(self):
        """Users can only submit under their own namespace."""
        code = VALID_AGENT_CODE.replace("@testuser/", "@someone_else/")
        result = pi.handle_submit_agent({"code": code}, "testuser")
        assert "error" in result
        assert "publisher" in result["error"].lower() or "Publisher" in result["error"]

    def test_version_must_increment(self):
        # Put existing agent in agents/ (simulates already-published agent)
        ns = pi.AGENTS_DIR / "@testuser"
        ns.mkdir(parents=True, exist_ok=True)
        (ns / "my_agent.py").write_text(VALID_AGENT_CODE)
        # Try to submit same version
        result = pi.handle_submit_agent({"code": VALID_AGENT_CODE}, "testuser")
        assert "error" in result
        assert "version" in result["error"].lower() or "Version" in result["error"]

    def test_version_increment_succeeds(self):
        # Put existing v1 in agents/
        ns = pi.AGENTS_DIR / "@testuser"
        ns.mkdir(parents=True, exist_ok=True)
        (ns / "my_agent.py").write_text(VALID_AGENT_CODE)
        # Submit v2
        v2_code = VALID_AGENT_CODE.replace('"1.0.0"', '"1.1.0"')
        result = pi.handle_submit_agent({"code": v2_code}, "testuser")
        assert result["ok"] is True

    def test_syntax_error_in_code(self):
        result = pi.handle_submit_agent({"code": "def broken(:"}, "testuser")
        assert "error" in result

    def test_manifest_only_file_is_not_an_agent(self):
        code = VALID_AGENT_CODE.split("class BasicAgent:", 1)[0]
        result = pi.handle_submit_agent({"code": code}, "testuser")
        assert "BasicAgent subclass" in result["error"]


# ──────────────────────────────────────────────────────────────────────
# Manifest validation
# ──────────────────────────────────────────────────────────────────────

class TestManifestValidation:
    def test_valid_manifest(self):
        m = {
            "schema": "rapp-agent/1.0", "name": "@pub/slug",
            "version": "1.0.0", "display_name": "X",
            "description": "Y", "author": "Z",
            "tags": ["a"], "category": "core",
        }
        assert pi.validate_manifest(m) == []

    def test_missing_name(self):
        m = {
            "schema": "rapp-agent/1.0", "version": "1.0.0",
            "display_name": "X", "description": "Y",
            "author": "Z", "tags": [], "category": "c",
        }
        errors = pi.validate_manifest(m)
        assert any("name" in e.lower() for e in errors)

    def test_bad_version(self):
        m = {
            "schema": "rapp-agent/1.0", "name": "@p/s",
            "version": "1.0", "display_name": "X",
            "description": "Y", "author": "Z",
            "tags": [], "category": "c",
        }
        errors = pi.validate_manifest(m)
        assert any("version" in e.lower() for e in errors)

    def test_tags_not_list(self):
        m = {
            "schema": "rapp-agent/1.0", "name": "@p/s",
            "version": "1.0.0", "display_name": "X",
            "description": "Y", "author": "Z",
            "tags": "not-a-list", "category": "c",
        }
        errors = pi.validate_manifest(m)
        assert any("tags" in e.lower() for e in errors)


# ──────────────────────────────────────────────────────────────────────
# Tier validation
# ──────────────────────────────────────────────────────────────────────

VALID_MANIFEST_BASE = {
    "schema": "rapp-agent/1.0", "name": "@pub/slug",
    "version": "1.0.0", "display_name": "X",
    "description": "Y", "author": "Z",
    "tags": ["a"], "category": "core",
}


class TestTierValidation:
    def test_community_tier_valid(self):
        m = {**VALID_MANIFEST_BASE, "quality_tier": "community"}
        assert pi.validate_manifest(m) == []

    def test_experimental_tier_valid(self):
        m = {**VALID_MANIFEST_BASE, "quality_tier": "experimental"}
        assert pi.validate_manifest(m) == []

    def test_verified_tier_valid(self):
        m = {**VALID_MANIFEST_BASE, "quality_tier": "verified"}
        assert pi.validate_manifest(m) == []

    def test_official_tier_valid(self):
        m = {**VALID_MANIFEST_BASE, "quality_tier": "official"}
        assert pi.validate_manifest(m) == []

    def test_invalid_tier_rejected(self):
        m = {**VALID_MANIFEST_BASE, "quality_tier": "platinum"}
        errors = pi.validate_manifest(m)
        assert any("quality_tier" in e for e in errors)

    def test_missing_tier_defaults_valid(self):
        m = {**VALID_MANIFEST_BASE}  # no quality_tier at all
        assert pi.validate_manifest(m) == []


class TestTierSubmissionEnforcement:
    def test_experimental_submission_allowed(self):
        code = VALID_AGENT_CODE.replace('"community"', '"experimental"')
        result = pi.handle_submit_agent({"code": code}, "testuser")
        assert result.get("ok") is True

    def test_verified_submission_downgraded(self):
        code = VALID_AGENT_CODE.replace('"community"', '"verified"')
        result = pi.handle_submit_agent({"code": code}, "testuser")
        assert result.get("ok") is True
        staged = (pi.REPO_ROOT / result["file"]).parent.joinpath("candidate.py").read_text()
        assert '"community"' in staged

    def test_official_submission_downgraded(self):
        code = VALID_AGENT_CODE.replace('"community"', '"official"')
        result = pi.handle_submit_agent({"code": code}, "testuser")
        assert result.get("ok") is True
        staged = (pi.REPO_ROOT / result["file"]).parent.joinpath("candidate.py").read_text()
        assert '"community"' in staged

    def test_invalid_tier_submission_rejected(self):
        code = VALID_AGENT_CODE.replace('"community"', '"platinum"')
        result = pi.handle_submit_agent({"code": code}, "testuser")
        assert "error" in result


# ──────────────────────────────────────────────────────────────────────
# End-to-end via process()
# ──────────────────────────────────────────────────────────────────────

class TestEndToEnd:
    def test_vote_via_process(self):
        result = pi.process({
            "action": "vote",
            "payload": {"agent": "@test/a", "direction": "up"}
        }, "user1")
        assert result["ok"] is True

    def test_review_via_process(self):
        result = pi.process({
            "action": "review",
            "payload": {"agent": "@test/a", "rating": 4, "text": "Nice"}
        }, "user1")
        assert result["ok"] is True

    def test_submit_via_process(self):
        result = pi.process({
            "action": "submit_agent",
            "payload": {"code": VALID_AGENT_CODE}
        }, "testuser")
        assert result["ok"] is True

    def test_submit_experimental_via_process(self):
        code = VALID_AGENT_CODE.replace('"community"', '"experimental"')
        result = pi.process({
            "action": "submit_agent",
            "payload": {"code": code}
        }, "testuser")
        assert result["ok"] is True


class TestCrudRequestContract:
    def context(self, issue_number: int) -> dict:
        return {
            "issue_number": issue_number,
            "issue_node_id": f"I_kwDO{issue_number}",
            "repository_id": 1234,
            "actor_id": 5678,
            "issue_updated_at": "2026-07-18T20:00:00Z",
        }

    def test_versioned_create_envelope(self):
        request = {
            "schema": pi.CHANGE_REQUEST_SCHEMA,
            "request_id": "req_create_123",
            "operation": "create",
            "resource": {"kind": "agent", "id": "@testuser/my_agent"},
            "preconditions": {"if_none_match": "*"},
            "payload": {
                "source": {
                    "content": VALID_AGENT_CODE,
                    "sha256": f"sha256:{pi.sha256_bytes(VALID_AGENT_CODE.encode())}",
                }
            },
        }
        result = pi.process(request, "testuser")
        assert result["ok"] is True
        assert result["action"] == "agent.create"
        assert result["request_id"] == "req_create_123"

    def test_same_issue_revision_is_idempotent(self):
        payload = {
            "code": VALID_AGENT_CODE,
            "_issue_body": VALID_AGENT_CODE,
            "_context": self.context(101),
        }
        first = pi.handle_submit_agent(payload, "testuser")
        second = pi.handle_submit_agent(payload, "testuser")
        assert first["request_id"] == second["request_id"]
        assert first["revision_id"] == second["revision_id"]
        assert first["file"] == second["file"]
        assert len(list((pi.STAGING_DIR / "requests").rglob("candidate.py"))) == 1

    def test_two_issues_do_not_share_candidate(self):
        first = pi.handle_submit_agent({
            "code": VALID_AGENT_CODE,
            "_issue_body": VALID_AGENT_CODE,
            "_context": self.context(101),
        }, "testuser")
        second = pi.handle_submit_agent({
            "code": VALID_AGENT_CODE,
            "_issue_body": VALID_AGENT_CODE,
            "_context": self.context(102),
        }, "testuser")
        assert first["request_id"] != second["request_id"]
        assert first["file"] != second["file"]
        assert len(list((pi.STAGING_DIR / "requests").rglob("candidate.py"))) == 2

    def test_issue_edit_supersedes_old_candidate(self):
        first = pi.handle_submit_agent({
            "code": VALID_AGENT_CODE,
            "_issue_body": "revision one",
            "_context": self.context(120),
        }, "testuser")
        second_code = VALID_AGENT_CODE.replace('"1.0.0"', '"1.1.0"')
        second = pi.handle_submit_agent({
            "code": second_code,
            "_issue_body": "revision two",
            "_context": self.context(120),
        }, "testuser")
        assert first["revision_id"] != second["revision_id"]
        candidates = list((pi.STAGING_DIR / "requests").rglob("candidate.py"))
        assert len(candidates) == 1
        archived = (
            pi.STATE_DIR
            / "requests"
            / first["request_id"]
            / f"{first['revision_id']}.json"
        )
        assert json.loads(archived.read_text())["status"] == "superseded"

    def test_closed_issue_cancels_staged_revisions(self):
        staged = pi.handle_submit_agent({
            "code": VALID_AGENT_CODE,
            "_issue_body": "cancel me",
            "_context": self.context(121),
        }, "testuser")
        result = pi.cancel_issue_requests(121, 5678)
        assert result["status"] == "cancelled"
        assert not (pi.REPO_ROOT / staged["file"]).exists()
        archived = (
            pi.STATE_DIR
            / "requests"
            / staged["request_id"]
            / f"{staged['revision_id']}.json"
        )
        assert json.loads(archived.read_text())["status"] == "cancelled"

    def test_semver_comparison_is_numeric(self):
        namespace = pi.AGENTS_DIR / "@testuser"
        namespace.mkdir(parents=True)
        existing = VALID_AGENT_CODE.replace('"1.0.0"', '"1.9.0"')
        (namespace / "my_agent.py").write_text(existing)
        update = VALID_AGENT_CODE.replace('"1.0.0"', '"1.10.0"')
        result = pi.handle_submit_agent({"code": update}, "testuser")
        assert result["ok"] is True
        assert result["action"] == "agent.update"

    def test_read_returns_hash_and_version(self):
        namespace = pi.AGENTS_DIR / "@testuser"
        namespace.mkdir(parents=True)
        path = namespace / "my_agent.py"
        path.write_text(VALID_AGENT_CODE)
        result = pi.handle_read_agent({"agent": "@testuser/my_agent"}, "reader")
        assert result["ok"] is True
        assert result["status"] == "active"
        assert result["version"] == "1.0.0"
        assert result["sha256"] == pi.sha256_bytes(path.read_bytes())

    def test_delete_stages_hash_bound_request(self):
        namespace = pi.AGENTS_DIR / "@testuser"
        namespace.mkdir(parents=True)
        path = namespace / "my_agent.py"
        path.write_text(VALID_AGENT_CODE)
        digest = pi.sha256_bytes(path.read_bytes())
        result = pi.handle_delete_agent({
            "agent": "@testuser/my_agent",
            "if_match": f"sha256:{digest}",
            "reason": "Retired by publisher",
            "_issue_body": "delete",
            "_context": self.context(103),
        }, "testuser")
        assert result["ok"] is True
        assert result["action"] == "agent.delete"
        request = json.loads((pi.REPO_ROOT / result["file"]).read_text())
        assert request["base_sha256"] == digest
        assert request["candidate_sha256"] == ""

    def test_digest_mismatch_fails_closed(self):
        result = pi.handle_submit_agent({
            "code": VALID_AGENT_CODE,
            "source_sha256": "sha256:" + ("0" * 64),
        }, "testuser")
        assert "digest mismatch" in result["error"].lower()

    def test_cross_issue_idempotency_key_deduplicates(self):
        first_payload = {
            "code": VALID_AGENT_CODE,
            "idempotency_key": "same-command-key",
            "_issue_body": "first transport",
            "_context": self.context(110),
        }
        second_payload = {
            "code": VALID_AGENT_CODE,
            "idempotency_key": "same-command-key",
            "_issue_body": "second transport",
            "_context": self.context(111),
        }
        first = pi.handle_submit_agent(first_payload, "testuser")
        second = pi.handle_submit_agent(second_payload, "testuser")
        assert first["ok"] is True
        assert second["status"] == "duplicate"
        assert second["request_id"] == first["request_id"]
        assert len(list((pi.STAGING_DIR / "requests").rglob("candidate.py"))) == 1

    def test_idempotency_key_reuse_with_different_command_fails(self):
        first = {
            "code": VALID_AGENT_CODE,
            "idempotency_key": "conflicting-key",
            "_issue_body": "first",
            "_context": self.context(112),
        }
        second = {
            "code": VALID_AGENT_CODE.replace('"1.0.0"', '"1.1.0"'),
            "idempotency_key": "conflicting-key",
            "_issue_body": "second",
            "_context": self.context(113),
        }
        assert pi.handle_submit_agent(first, "testuser")["ok"] is True
        result = pi.handle_submit_agent(second, "testuser")
        assert "idempotency key conflicts" in result["error"].lower()

    def test_publisher_uses_canonical_github_login_casing(self):
        code = VALID_AGENT_CODE.replace("@testuser/", "@TESTUSER/")
        result = pi.handle_submit_agent({"code": code}, "testuser")
        assert result["agent"] == "@testuser/my_agent"

    def test_read_rejects_path_traversal(self):
        result = pi.handle_read_agent(
            {"agent": "@testuser/../../template"},
            "reader",
        )
        assert "safe" in result["error"].lower()

    def test_read_resolves_mixed_case_publisher_safely(self):
        namespace = pi.AGENTS_DIR / "@discreetRappers"
        namespace.mkdir(parents=True)
        source = VALID_AGENT_CODE.replace(
            "@testuser/my_agent",
            "@discreetRappers/my_agent",
        )
        (namespace / "my_agent.py").write_text(source)
        result = pi.handle_read_agent(
            {"agent": "@discreetrappers/my_agent"},
            "reader",
        )
        assert result["status"] == "active"
        assert result["agent"] == "@discreetRappers/my_agent"

    def test_versioned_update_requires_if_match(self):
        namespace = pi.AGENTS_DIR / "@testuser"
        namespace.mkdir(parents=True)
        (namespace / "my_agent.py").write_text(VALID_AGENT_CODE)
        update = VALID_AGENT_CODE.replace('"1.0.0"', '"1.1.0"')
        command = {
            "schema": pi.CHANGE_REQUEST_SCHEMA,
            "request_id": "req_missing_precondition",
            "operation": "update",
            "resource": {"kind": "agent", "id": "@testuser/my_agent"},
            "preconditions": {},
            "payload": {
                "source": {
                    "content": update,
                    "sha256": f"sha256:{pi.sha256_bytes(update.encode())}",
                }
            },
        }
        result = pi.process(command, "testuser")
        assert "if_match" in result["error"]

    def test_crlf_source_uses_lf_hash_domain(self):
        crlf = VALID_AGENT_CODE.replace("\n", "\r\n")
        digest = pi.sha256_bytes(VALID_AGENT_CODE.encode())
        command = {
            "schema": pi.CHANGE_REQUEST_SCHEMA,
            "request_id": "req_crlf_source",
            "operation": "create",
            "resource": {"kind": "agent", "id": "@testuser/my_agent"},
            "preconditions": {"if_none_match": "*"},
            "payload": {
                "source": {
                    "content": crlf,
                    "sha256": f"sha256:{digest}",
                }
            },
        }
        result = pi.process(command, "testuser")
        assert result["ok"] is True

    def test_versioned_update_preserves_legacy_official_identity(self):
        namespace = pi.AGENTS_DIR / "@rapp"
        namespace.mkdir(parents=True)
        existing = (
            VALID_AGENT_CODE
            .replace("@testuser/my_agent", "@rapp/hacker_news")
            .replace('"community"', '"official"')
        )
        active = namespace / "hacker_news_agent.py"
        active.write_text(existing)
        update = existing.replace('"1.0.0"', '"1.1.0"')
        command = {
            "schema": pi.CHANGE_REQUEST_SCHEMA,
            "request_id": "req_legacy_official",
            "operation": "update",
            "resource": {"kind": "agent", "id": "@rapp/hacker_news"},
            "preconditions": {
                "if_match": f"sha256:{pi.sha256_bytes(active.read_bytes())}",
            },
            "payload": {
                "source": {
                    "content": update,
                    "sha256": f"sha256:{pi.sha256_bytes(update.encode())}",
                }
            },
        }
        result = pi.process(command, "kody-w")
        assert result["ok"] is True
        assert result["agent"] == "@rapp/hacker_news"
        request = json.loads((pi.REPO_ROOT / result["file"]).read_text())
        assert request["canonical_path"] == "agents/@rapp/hacker_news_agent.py"
        assert request["candidate_quality_tier"] == "official"

    def test_numeric_owner_survives_github_login_rename(self):
        namespace = pi.AGENTS_DIR / "@testuser"
        namespace.mkdir(parents=True)
        active = namespace / "my_agent.py"
        active.write_text(VALID_AGENT_CODE)
        digest = pi.sha256_bytes(active.read_bytes())
        pi.LIFECYCLE_FILE.write_text(json.dumps({
            "schema": "rar-agent-lifecycle/1.0",
            "agents": {
                "@testuser/my_agent": {
                    "status": "active",
                    "version": "1.0.0",
                    "quality_tier": "community",
                    "sha256": digest,
                    "latest_receipt": "rar_existing",
                    "owner_github_id": 5678,
                    "owner_github_login": "testuser",
                }
            },
        }))
        update = VALID_AGENT_CODE.replace('"1.0.0"', '"1.1.0"')
        context = self.context(130)
        result = pi.handle_submit_agent({
            "code": update,
            "agent": "@testuser/my_agent",
            "source_sha256": f"sha256:{pi.sha256_bytes(update.encode())}",
            "if_match": f"sha256:{digest}",
            "idempotency_key": "renamed-owner-update",
            "_versioned": True,
            "_operation": "update",
            "_issue_body": "renamed owner",
            "_context": context,
        }, "renamed-user")
        assert result["ok"] is True
        assert result["agent"] == "@testuser/my_agent"

    def test_reclaimed_login_cannot_bypass_numeric_owner(self):
        namespace = pi.AGENTS_DIR / "@testuser"
        namespace.mkdir(parents=True)
        active = namespace / "my_agent.py"
        active.write_text(VALID_AGENT_CODE)
        digest = pi.sha256_bytes(active.read_bytes())
        pi.LIFECYCLE_FILE.write_text(json.dumps({
            "schema": "rar-agent-lifecycle/1.0",
            "agents": {
                "@testuser/my_agent": {
                    "status": "active",
                    "version": "1.0.0",
                    "quality_tier": "community",
                    "sha256": digest,
                    "latest_receipt": "rar_existing",
                    "owner_github_id": 9999,
                    "owner_github_login": "former-owner",
                }
            },
        }))
        update = VALID_AGENT_CODE.replace('"1.0.0"', '"1.1.0"')
        context = self.context(132)
        result = pi.handle_submit_agent({
            "code": update,
            "agent": "@testuser/my_agent",
            "source_sha256": f"sha256:{pi.sha256_bytes(update.encode())}",
            "if_match": f"sha256:{digest}",
            "idempotency_key": "reclaimed-login-attempt",
            "_versioned": True,
            "_operation": "update",
            "_issue_body": "wrong owner",
            "_context": context,
        }, "testuser")
        assert "numeric owner" in result["error"].lower()

    def test_crud_resolves_nested_card_path(self):
        nested = pi.AGENTS_DIR / "@testuser" / "vertical" / "stack"
        nested.mkdir(parents=True)
        active = nested / "nested_agent.py.card"
        source = VALID_AGENT_CODE.replace(
            "@testuser/my_agent",
            "@testuser/nested_agent",
        )
        active.write_text(source)
        update = source.replace('"1.0.0"', '"1.1.0"')
        result = pi.handle_submit_agent({
            "code": update,
            "agent": "@testuser/nested_agent",
            "source_sha256": f"sha256:{pi.sha256_bytes(update.encode())}",
            "if_match": f"sha256:{pi.sha256_bytes(active.read_bytes())}",
            "idempotency_key": "nested-card-update",
            "_versioned": True,
            "_operation": "update",
            "_issue_body": "nested update",
            "_context": self.context(131),
        }, "testuser")
        assert result["ok"] is True
        request = json.loads((pi.REPO_ROOT / result["file"]).read_text())
        assert request["canonical_path"] == (
            "agents/@testuser/vertical/stack/nested_agent.py.card"
        )
        read = pi.handle_read_agent(
            {"agent": "@testuser/nested_agent"},
            "reader",
        )
        assert read["file"] == request["canonical_path"]


class TestRemoteSource:
    class Response:
        def __init__(self, content: bytes, url: str, content_length: str | None = None):
            self.content = content
            self.url = url
            self.headers = {}
            if content_length is not None:
                self.headers["Content-Length"] = content_length

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def geturl(self):
            return self.url

        def read(self, limit):
            return self.content[:limit]

    def test_rejects_non_github_host(self, monkeypatch):
        called = False

        def should_not_fetch(*_args, **_kwargs):
            nonlocal called
            called = True

        monkeypatch.setattr(pi.urllib.request, "urlopen", should_not_fetch)
        assert pi._fetch_attachment("https://example.com/agent.py") is None
        assert called is False

    def test_rejects_redirect_off_github(self, monkeypatch):
        response = self.Response(b"source", "https://example.com/agent.py")
        monkeypatch.setattr(
            pi.urllib.request,
            "urlopen",
            lambda *_args, **_kwargs: response,
        )
        assert pi._fetch_attachment(
            "https://raw.githubusercontent.com/owner/repo/sha/agent.py"
        ) is None

    def test_rejects_oversized_source(self, monkeypatch):
        response = self.Response(
            b"source",
            "https://raw.githubusercontent.com/owner/repo/sha/agent.py",
            str(pi.REMOTE_SOURCE_LIMIT + 1),
        )
        monkeypatch.setattr(
            pi.urllib.request,
            "urlopen",
            lambda *_args, **_kwargs: response,
        )
        assert pi._fetch_attachment(
            "https://raw.githubusercontent.com/owner/repo/sha/agent.py"
        ) is None

    def test_accepts_bounded_github_source(self, monkeypatch):
        response = self.Response(
            VALID_AGENT_CODE.encode(),
            "https://gist.githubusercontent.com/user/id/raw/sha/my_agent.py",
        )
        monkeypatch.setattr(
            pi.urllib.request,
            "urlopen",
            lambda *_args, **_kwargs: response,
        )
        source = pi._fetch_attachment(
            "https://gist.githubusercontent.com/user/id/raw/sha/my_agent.py"
        )
        assert source == VALID_AGENT_CODE

    def test_accepts_github_attachment_asset_redirect(self, monkeypatch):
        response = self.Response(
            VALID_AGENT_CODE.encode(),
            "https://github-production-user-asset-6210df.s3.amazonaws.com/object",
        )
        monkeypatch.setattr(
            pi.urllib.request,
            "urlopen",
            lambda *_args, **_kwargs: response,
        )
        source = pi._fetch_attachment(
            "https://github.com/user-attachments/assets/"
            "12345678-1234-1234-1234-123456789abc"
        )
        assert source == VALID_AGENT_CODE
