"""Privacy policy uncertainty must never dispatch a chat."""

import importlib.util
import json
import sys
import types
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def privacy(tmp_path, monkeypatch):
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            self.name, self.metadata = name, metadata

    basic = types.ModuleType("agents.basic_agent")
    basic.BasicAgent = BasicAgent
    monkeypatch.setitem(sys.modules, "agents.basic_agent", basic)
    monkeypatch.setenv("GRAIL_LAYERS_HOME", str(tmp_path))

    def load(name, path):
        spec = importlib.util.spec_from_file_location(name, ROOT / path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    return (
        load("private_policy_provider", "stacks/grail-layers/providers_1_1.py"),
        load("private_policy_editor", "stacks/private-mode/private_mode_agent.py"),
        tmp_path / "private-topics.json",
    )


@pytest.mark.parametrize("policy", [
    "{broken", "[]", "{}", '{"topics":"health"}', '{"topics":[42]}',
    '{"topics":[""]}', '{"topics":["health"],"model":42}',
])
def test_invalid_policy_refuses_without_dispatch_or_overwrite(privacy, monkeypatch, policy):
    provider, editor, path = privacy
    path.write_text(policy)
    calls = []
    monkeypatch.setattr(provider, "_post_local", lambda *a, **k: calls.append(k))
    response = provider._post_private("https://cloud/chat/completions", json={
        "model": "cloud", "messages": [{"role": "user", "content": "hello"}],
    })
    assert response is not None, "invalid policy fell through to ordinary routing"
    assert response.status_code == 503
    assert "privacy policy" in response.json()["error"]["message"].lower()
    assert not calls
    agent = editor.PrivateModeAgent()
    assert "error" in agent.perform(action="add_topic", topic="money").lower()
    assert "refus" in agent.system_context().lower()
    assert path.read_text() == policy


def test_unreadable_policy_refuses(privacy, monkeypatch):
    provider, editor, path = privacy
    path.mkdir()
    calls = []
    monkeypatch.setattr(provider, "_post_local", lambda *a, **k: calls.append(k))
    response = provider._post_private("https://cloud/chat/completions", json={"model": "cloud"})
    assert response is not None, "unreadable policy fell through to ordinary routing"
    assert response.status_code == 503
    assert not calls
    assert "error" in editor.PrivateModeAgent().perform(action="list").lower()


def test_absent_policy_keeps_ordinary_routing(privacy, monkeypatch):
    provider, editor, _ = privacy
    sentinel = object()
    monkeypatch.setattr(provider, "_post_local", lambda *a, **k: sentinel)
    assert provider._post_private("https://cloud/chat/completions", json={"model": "cloud"}) is sentinel
    assert "none yet" in editor.PrivateModeAgent().perform()


def test_private_chat_local_only_and_no_local_refusal(privacy, monkeypatch):
    provider, _, path = privacy
    path.write_text(json.dumps({"topics": ["health"], "model": "ollama/test"}))
    calls = []
    monkeypatch.setattr(provider, "_ollama_models", lambda: [{"id": "ollama/test"}])
    monkeypatch.setattr(provider, "_prev_post", lambda url, *a, **kw: calls.append((url, kw)))
    body = {"model": "cloud", "messages": [{"role": "user", "content": [{"text": "HEALTH notes"}]}]}
    provider._post_private("https://cloud/chat/completions", json=body,
                           headers={"Authorization": "secret", "X-Test": "yes"})
    assert len(calls) == 1
    assert calls[0][0] == provider.OLLAMA + "/v1/chat/completions"
    assert calls[0][1]["json"]["model"] == "test"
    assert calls[0][1]["headers"] == {"X-Test": "yes"}
    calls.clear()
    monkeypatch.setattr(provider, "_ollama_models", lambda: [])
    response = provider._post_private("https://cloud/chat/completions", json=body)
    assert "did not send" in response.json()["choices"][0]["message"]["content"]
    assert not calls


def test_local_failure_never_retries_cloud(privacy, monkeypatch):
    provider, _, path = privacy
    path.write_text('{"topics":["health"]}')
    monkeypatch.setattr(provider, "_ollama_models", lambda: [{"id": "ollama/test"}])
    calls = []

    def fail(url, *args, **kwargs):
        calls.append(url)
        raise provider.requests.ConnectionError("local unavailable")

    monkeypatch.setattr(provider, "_prev_post", fail)
    response = provider._post_private("https://cloud/chat/completions", json={
        "model": "cloud", "messages": [{"role": "user", "content": "health"}],
    })
    assert response.status_code == 503
    assert calls == [provider.OLLAMA + "/v1/chat/completions"]


def test_editor_explains_substring_and_provider_prerequisite(privacy):
    _, editor, _ = privacy
    agent = editor.PrivateModeAgent()
    added = agent.perform(action="add_topic", topic="health")
    assert "providers" in added.lower()
    checked = agent.perform(action="check", text="health question")
    assert "substring" in checked.lower()
    assert "cannot verify" in checked.lower()


def test_apply_preserves_layer_contract_and_enforces_policy(privacy, monkeypatch):
    provider, _, path = privacy
    proven = set(provider.PROVEN_GRAIL)
    touches = set(provider.TOUCHES)
    monkeypatch.setattr(provider.requests, "get", provider.requests.get)
    monkeypatch.setattr(provider.requests, "post", provider.requests.post)
    path.write_text("{broken")
    provider.apply()
    assert provider.requests.get is provider._get_local
    assert provider.requests.post is provider._post_private
    response = provider.requests.post("https://cloud/chat/completions", json={"model": "ollama/test"})
    assert response.status_code == 503
    assert provider.PROVEN_GRAIL == proven
    assert provider.TOUCHES == touches
