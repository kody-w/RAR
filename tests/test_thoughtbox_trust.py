"""Thoughtbox only acknowledges changes that reach durable storage."""

import importlib.util
import json
import os
import subprocess
import sys
import types
from pathlib import Path

import pytest


SOURCE = Path(__file__).resolve().parents[1] / "stacks/thoughtbox/thoughtbox_agent.py"


def load():
    spec = importlib.util.spec_from_file_location("thoughtbox_trust", SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def journal(tmp_path, monkeypatch):
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            self.name, self.metadata = name, metadata

    basic = types.ModuleType("agents.basic_agent")
    basic.BasicAgent = BasicAgent
    monkeypatch.setitem(sys.modules, "agents.basic_agent", basic)
    monkeypatch.setenv("BRAINSTEM_DATA_DIR", str(tmp_path))
    return load()


def test_default_entries_survive_module_reload(journal):
    agent = journal.ThoughtboxAgent()
    saved = json.loads(agent.perform(action="append", text="Keep this thought", tags=["work"]))
    assert saved["ok"] is True
    reloaded = load().ThoughtboxAgent()
    listed = json.loads(reloaded.perform(action="list"))
    assert listed["entries"] == [saved["entry"]]


def test_default_entries_survive_fresh_process(journal):
    saved = json.loads(journal.run(action="append", text="Across processes"))
    child = """
import importlib.util, json, sys, types
basic = types.ModuleType("agents.basic_agent")
basic.BasicAgent = type("BasicAgent", (), {})
sys.modules["agents.basic_agent"] = basic
spec = importlib.util.spec_from_file_location("thoughtbox_child", sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
print(module.run(action="list"))
"""
    result = subprocess.run(
        [sys.executable, "-c", child, str(SOURCE)],
        capture_output=True, text=True, check=True,
    )
    assert json.loads(result.stdout)["entries"] == [saved["entry"]]


def test_failed_disk_write_returns_error_without_changing_journal(journal, monkeypatch):
    saved = json.loads(journal.run(action="append", text="original"))

    def failed_replace(*args):
        raise OSError("disk full")

    monkeypatch.setattr(os, "replace", failed_replace)
    result = json.loads(journal.run(action="append", text="must not be saved"))
    assert result["ok"] is False
    assert "disk full" in result["error"]
    assert json.loads(load().run(action="list"))["entries"] == [saved["entry"]]


@pytest.mark.parametrize("failure", ["raise", "false"])
def test_failed_workspace_write_never_falls_back(journal, failure):
    def write(*args):
        if failure == "raise":
            raise RuntimeError("workspace unavailable")
        return False

    context = {"workspace_read": lambda key: None, "workspace_write": write}
    result = json.loads(journal.run(context, action="append", text="not saved"))
    assert result["ok"] is False
    assert "persist" in result["error"].lower()
    assert json.loads(journal.run(action="list"))["total"] == 0


def test_workspace_callbacks_remain_supported(journal):
    workspace = {}
    context = {
        "workspace_read": workspace.get,
        "workspace_write": lambda key, value: workspace.__setitem__(key, value),
    }
    saved = json.loads(journal.run(context, action="append", text="workspace entry"))
    assert saved["ok"] is True
    assert json.loads(load().run(context, action="list"))["entries"] == [saved["entry"]]
    assert json.loads(journal.run(action="list"))["total"] == 0


def test_broken_read_does_not_overwrite_existing_entries(journal, tmp_path):
    path = tmp_path / "thoughtbox" / "entries.json"
    path.parent.mkdir()
    path.write_text("{broken")
    result = json.loads(journal.run(action="append", text="no overwrite"))
    assert result["ok"] is False
    assert path.read_text() == "{broken"


def test_half_configured_workspace_is_an_explicit_error(journal):
    result = json.loads(journal.run(
        {"workspace_read": lambda key: None}, action="append", text="not saved",
    ))
    assert result["ok"] is False
    assert "workspace" in result["error"]


def test_import_delete_and_read_actions_use_durable_entries(journal):
    imported = json.loads(journal.run(
        action="import_json",
        blob=json.dumps([{"id": "entry-1", "text": "search me", "tags": ["work"]}]),
    ))
    assert imported["added"] == 1
    reloaded = load()
    assert json.loads(reloaded.run(action="search", query="search"))["total"] == 1
    assert json.loads(reloaded.run(action="tag", tag="work"))["total"] == 1
    assert json.loads(reloaded.run(action="stats"))["total"] == 1
    assert json.loads(reloaded.run(action="export"))["count"] == 1
    assert json.loads(reloaded.run(action="delete", id="entry-1"))["removed"] == 1
    assert json.loads(load().run(action="list"))["total"] == 0
