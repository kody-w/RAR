import hashlib
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import federate


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def read(self):
        return json.dumps(self.payload).encode()


def test_semver_comparison_is_numeric():
    assert federate.is_newer_version("1.10.0", "1.9.0")
    assert not federate.is_newer_version("1.9.0", "1.10.0")
    assert not federate.is_newer_version("invalid", "1.0.0")


def test_sync_rejects_digest_mismatch(tmp_path, monkeypatch):
    registry = tmp_path / "registry.json"
    registry.write_text('{"agents": []}')
    monkeypatch.setattr(federate, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(federate, "REGISTRY_FILE", registry)
    monkeypatch.setattr(federate, "get_token", lambda: "")
    monkeypatch.setattr(
        federate,
        "fetch_json",
        lambda _url, _token: {
            "agents": [{
                "name": "@upstream/test_agent",
                "version": "1.0.0",
                "_file": "agents/@upstream/test_agent.py",
                "_sha256": "0" * 64,
                "quality_tier": "community",
            }]
        },
    )
    monkeypatch.setattr(federate, "fetch_text", lambda _url, _token: "source")
    result = federate.cmd_sync({"upstream": "owner/rar"}, pull=True)
    assert result == 1
    assert not (tmp_path / "agents/@upstream/test_agent.py").exists()


def test_sync_verifies_and_writes_atomically(tmp_path, monkeypatch):
    registry = tmp_path / "registry.json"
    registry.write_text('{"agents": []}')
    source = "verified source\n"
    digest = hashlib.sha256(source.encode()).hexdigest()
    monkeypatch.setattr(federate, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(federate, "REGISTRY_FILE", registry)
    monkeypatch.setattr(federate, "get_token", lambda: "")
    monkeypatch.setattr(
        federate,
        "fetch_json",
        lambda _url, _token: {
            "agents": [{
                "name": "@upstream/test_agent",
                "version": "1.0.0",
                "_file": "agents/@upstream/test_agent.py",
                "_sha256": digest,
                "quality_tier": "community",
            }]
        },
    )
    monkeypatch.setattr(federate, "fetch_text", lambda _url, _token: source)
    result = federate.cmd_sync({"upstream": "owner/rar"}, pull=True)
    assert result == 0
    destination = tmp_path / "agents/@upstream/test_agent.py"
    assert destination.read_text() == source
    assert not destination.with_suffix(".py.tmp").exists()


def test_federated_submit_uses_change_envelope(tmp_path, monkeypatch):
    agent_file = tmp_path / "agents/@test/test_agent.py"
    agent_file.parent.mkdir(parents=True)
    agent_file.write_text("agent source\n")
    registry = tmp_path / "registry.json"
    registry.write_text(json.dumps({
        "agents": [{
            "name": "@test/test_agent",
            "version": "1.0.0",
            "_file": "agents/@test/test_agent.py",
            "_sha256": hashlib.sha256(agent_file.read_bytes()).hexdigest(),
        }]
    }))
    monkeypatch.setattr(federate, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(federate, "REGISTRY_FILE", registry)
    monkeypatch.setattr(federate, "get_token", lambda: "test-token")
    monkeypatch.setattr(federate, "fetch_json", lambda _url, _token: {"agents": []})
    captured = {}

    def fake_urlopen(request, timeout):
        captured["payload"] = json.loads(request.data)
        return FakeResponse({"html_url": "https://example.test/issue/1"})

    monkeypatch.setattr(federate.urllib.request, "urlopen", fake_urlopen)
    result = federate.cmd_submit(
        {"upstream": "owner/rar"},
        specific_agent="@test/test_agent",
    )
    assert result == 0
    command = json.loads(
        captured["payload"]["body"].split("```json\n", 1)[1].rsplit("\n```", 1)[0]
    )
    assert command["schema"] == "rar-change-request/1.0"
    assert command["operation"] == "create"
    assert command["resource"]["id"] == "@test/test_agent"
    assert "labels" not in captured["payload"]


def test_submit_aborts_when_upstream_registry_is_unavailable(tmp_path, monkeypatch):
    registry = tmp_path / "registry.json"
    registry.write_text('{"agents": []}')
    monkeypatch.setattr(federate, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(federate, "REGISTRY_FILE", registry)
    monkeypatch.setattr(federate, "get_token", lambda: "test-token")
    monkeypatch.setattr(federate, "fetch_json", lambda _url, _token: None)
    assert federate.cmd_submit({"upstream": "owner/rar"}) == 1


def test_tombstone_refuses_tampered_local_bytes(tmp_path, monkeypatch):
    original = "original\n"
    digest = hashlib.sha256(original.encode()).hexdigest()
    destination = tmp_path / "agents/@upstream/test_agent.py"
    destination.parent.mkdir(parents=True)
    destination.write_text("locally modified\n")
    registry = tmp_path / "registry.json"
    registry.write_text(json.dumps({
        "agents": [{
            "name": "@upstream/test_agent",
            "version": "1.0.0",
            "_file": "agents/@upstream/test_agent.py",
            "_sha256": digest,
        }]
    }))
    monkeypatch.setattr(federate, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(federate, "REGISTRY_FILE", registry)
    monkeypatch.setattr(federate, "LIFECYCLE_FILE", tmp_path / "state/lifecycle.json")
    monkeypatch.setattr(federate, "RECEIPTS_DIR", tmp_path / "state/receipts")
    monkeypatch.setattr(federate, "get_token", lambda: "")
    monkeypatch.setattr(
        federate,
        "fetch_json",
        lambda _url, _token: {
            "agents": [],
            "lifecycle": {
                "tombstones": [{
                    "agent": "@upstream/test_agent",
                    "status": "deleted",
                    "version": "1.0.0",
                    "sha256": digest,
                    "latest_receipt": "rar_" + ("a" * 64),
                }]
            },
        },
    )
    assert federate.cmd_sync({"upstream": "owner/rar"}, pull=True) == 1
    assert destination.read_text() == "locally modified\n"
