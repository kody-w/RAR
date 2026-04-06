"""
Tests for the GitHub Issues processing pipeline.

Covers: vote, review, submit_agent actions, JSON parsing, validation.
"""

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
    (state_dir / "binder_ledger.json").write_text(json.dumps({"binders": {}, "updated_at": ""}))

    monkeypatch.setattr(pi, "STATE_DIR", state_dir)
    monkeypatch.setattr(pi, "AGENTS_DIR", agents_dir)
    monkeypatch.setattr(pi, "STAGING_DIR", staging_dir)
    monkeypatch.setattr(pi, "VOTES_FILE", state_dir / "votes.json")
    monkeypatch.setattr(pi, "REVIEWS_FILE", state_dir / "reviews.json")
    monkeypatch.setattr(pi, "LEDGER_FILE", state_dir / "binder_ledger.json")
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


class MyAgent:
    def perform(self, **kwargs) -> str:
        return "hello"
'''


# ──────────────────────────────────────────────────────────────────────
# Binder registration
# ──────────────────────────────────────────────────────────────────────

class TestRegisterBinder:
    def test_register_new_binder(self):
        result = pi.handle_register_binder({"namespace": "@testuser"}, "testuser")
        assert result["ok"] is True
        assert result["status"] == "registered"
        assert result["namespace"] == "@testuser"

    def test_register_already_registered(self):
        pi.handle_register_binder({"namespace": "@testuser"}, "testuser")
        result = pi.handle_register_binder({"namespace": "@testuser"}, "testuser")
        assert result["ok"] is True
        assert result["status"] == "already_registered"

    def test_register_with_repo(self):
        result = pi.handle_register_binder(
            {"namespace": "@alice", "repo": "https://github.com/alice/my-binder"},
            "alice"
        )
        assert result["ok"] is True
        # Verify persisted
        assert pi.is_binder_registered("alice")

    def test_register_auto_namespace(self):
        result = pi.handle_register_binder({}, "bob")
        assert result["namespace"] == "@bob"

    def test_submit_requires_registration(self):
        """Unregistered users cannot submit agents."""
        result = pi.handle_submit_agent({"code": VALID_AGENT_CODE}, "unregistered_user")
        assert "error" in result
        assert "register" in result["error"].lower() or "binder" in result["error"].lower()

    def test_registered_user_can_submit(self):
        pi.handle_register_binder({"namespace": "@testuser"}, "testuser")
        result = pi.handle_submit_agent({"code": VALID_AGENT_CODE}, "testuser")
        assert result.get("ok") is True


class TestSubmitAgent:
    """All submit tests register the binder first."""

    @pytest.fixture(autouse=True)
    def _register_binder(self):
        pi.handle_register_binder({"namespace": "@testuser"}, "testuser")

    def test_valid_submission(self):
        result = pi.handle_submit_agent({"code": VALID_AGENT_CODE}, "testuser")
        assert result["ok"] is True
        assert result["agent"] == "@testuser/my_agent"
        assert result["status"] == "pending_review"
        # Verify file was written to staging, NOT agents
        staging_file = pi.STAGING_DIR / "@testuser" / "my_agent.py"
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
    @pytest.fixture(autouse=True)
    def _register_binder(self):
        pi.handle_register_binder({"namespace": "@testuser"}, "testuser")

    def test_experimental_submission_allowed(self):
        code = VALID_AGENT_CODE.replace('"community"', '"experimental"')
        result = pi.handle_submit_agent({"code": code}, "testuser")
        assert result.get("ok") is True

    def test_verified_submission_downgraded(self):
        code = VALID_AGENT_CODE.replace('"community"', '"verified"')
        result = pi.handle_submit_agent({"code": code}, "testuser")
        assert result.get("ok") is True
        staged = (pi.STAGING_DIR / "@testuser" / "my_agent.py").read_text()
        assert '"community"' in staged

    def test_official_submission_downgraded(self):
        code = VALID_AGENT_CODE.replace('"community"', '"official"')
        result = pi.handle_submit_agent({"code": code}, "testuser")
        assert result.get("ok") is True

    def test_invalid_tier_submission_rejected(self):
        code = VALID_AGENT_CODE.replace('"community"', '"platinum"')
        result = pi.handle_submit_agent({"code": code}, "testuser")
        assert "error" in result


# ──────────────────────────────────────────────────────────────────────
# End-to-end via process()
# ──────────────────────────────────────────────────────────────────────

class TestEndToEnd:
    @pytest.fixture(autouse=True)
    def _register_binder(self):
        pi.handle_register_binder({"namespace": "@testuser"}, "testuser")

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
