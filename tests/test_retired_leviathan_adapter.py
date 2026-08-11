from __future__ import annotations

import importlib.util
import json
import sys
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "agents"
    / "@kody-w"
    / "rapp_leviathan_factory_agent.py"
)


class BasicAgent:
    def __init__(self, name=None, metadata=None):
        self.name = name
        self.metadata = metadata


def load():
    agents = types.ModuleType("agents")
    basic = types.ModuleType("agents.basic_agent")
    basic.BasicAgent = BasicAgent
    agents.basic_agent = basic
    sys.modules["agents"] = agents
    sys.modules["agents.basic_agent"] = basic
    spec = importlib.util.spec_from_file_location(
        "retired_leviathan_adapter_test",
        PATH,
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_legacy_actions_return_explicit_retirement():
    module = load()
    result = json.loads(
        module.RappLeviathanFactoryAgent().perform(
            action="generate",
            name="legacy",
        )
    )
    assert result["status"] == "retired"
    assert result["replacement"] == "@kody-w/full_rapp_leviathan"
