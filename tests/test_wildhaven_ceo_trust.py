"""The CEO pack wraps prompts; it does not retrieve a vault."""

import importlib.util
import json
import sys
import types
from pathlib import Path

import pytest


PACK = Path(__file__).resolve().parents[1] / "stacks/wildhaven-ceo"


@pytest.fixture
def ceo(monkeypatch):
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            self.name, self.metadata = name, metadata

    basic = types.ModuleType("agents.basic_agent")
    basic.BasicAgent = BasicAgent
    monkeypatch.setitem(sys.modules, "agents.basic_agent", basic)
    calls = []
    llm = types.ModuleType("utils.llm")

    def dispatch(messages):
        calls.append(messages)
        return "mock answer"

    llm.call_llm = dispatch
    utils = types.ModuleType("utils")
    utils.__path__ = []
    monkeypatch.setitem(sys.modules, "utils", utils)
    monkeypatch.setitem(sys.modules, "utils.llm", llm)
    spec = importlib.util.spec_from_file_location("wildhaven_ceo_trust", PACK / "wildhaven_ceo_agent.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, calls


def test_all_claim_surfaces_disclose_prompt_wrapper_and_no_retrieval(ceo):
    module, _ = ceo
    for text in (
        module.__doc__, module.__manifest__["description"],
        module.WildhavenCeoAgent().metadata["description"],
        json.loads((PACK / "pack.json").read_text())["purpose"],
        (PACK / "README.md").read_text(),
    ):
        assert "prompt wrapper" in text.lower()
        assert "no retrieval" in text.lower()
        assert "drop a vault" not in text.lower()


@pytest.mark.parametrize("action", ["ask", "decide", "respond_to", "daily_brief", "quarterly_review"])
def test_workflows_use_supplied_context_without_claiming_retrieval(ceo, action):
    module, calls = ceo
    agent = module.WildhavenCeoAgent()
    context = "Revenue $12.34. Reference: https://example.invalid/vault"
    result = agent.perform(action=action, question="How are we doing?", asker="Investor",
                           workspace_context=context, voice_style="plainspoken")
    assert result == "mock answer"
    assert len(calls) == 1
    system = calls[0][0]["content"]
    assert context in system
    assert "plainspoken" in system
    assert "no retrieval" in system.lower()
    assert "urls" in system.lower()
    assert action.upper() in system


def test_missing_context_is_explicitly_generic_not_vault_grounded(ceo):
    module, calls = ceo
    module.WildhavenCeoAgent().perform(action="daily_brief")
    system = calls[0][0]["content"]
    assert "No workspace context was provided" in system
    assert "first line" in system
    assert "no retrieval" in system.lower()
