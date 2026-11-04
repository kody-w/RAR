"""Night Watch requires current evidence before reassuring the owner."""

import importlib.util
import json
import os
import sys
import time
import types
from pathlib import Path

import pytest


SOURCE = Path(__file__).resolve().parents[1] / "stacks/night-watch/night_watch_agent.py"


@pytest.fixture
def watch(tmp_path, monkeypatch):
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            self.name, self.metadata = name, metadata

    basic = types.ModuleType("agents.basic_agent")
    basic.BasicAgent = BasicAgent
    monkeypatch.setitem(sys.modules, "agents.basic_agent", basic)
    monkeypatch.setenv("GRAIL_LAYERS_HOME", str(tmp_path))
    spec = importlib.util.spec_from_file_location("night_watch_trust", SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module.shutil, "disk_usage", lambda path: types.SimpleNamespace(
        free=100_000_000_000, total=200_000_000_000,
    ))
    monkeypatch.setattr(module, "_plist", lambda label: False)
    return module


def save_report(watch, name, data):
    path = Path(watch.HOME) / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data))
    return path


def good_drills(watch):
    for drill in ("chaos", "succession"):
        save_report(watch, f"{drill}/latest.json", {"survived": 3, "total": 3})


def test_missing_evidence_is_unknown_not_passed(watch):
    output = watch.NightWatchAgent().perform(action="check")
    assert "unknown" in output.lower()
    assert "not configured" in output.lower()
    assert "drills passed" not in output
    assert "services answer" not in output
    assert "started normally" not in output
    assert not output.startswith("All good")


def test_stale_drills_are_unknown_even_if_all_survived(watch):
    good_drills(watch)
    for drill in ("chaos", "succession"):
        path = Path(watch.HOME) / drill / "latest.json"
        old = time.time() - 3 * 24 * 3600
        os.utime(path, (old, old))
    output = watch.NightWatchAgent().perform(action="check")
    assert "stale" in output.lower()
    assert "unknown" in output.lower()
    assert "drills passed" not in output


@pytest.mark.parametrize("data", [
    {}, {"survived": 0, "total": 0}, {"survived": "3", "total": "3"},
    {"survived": True, "total": True}, {"survived": 4, "total": 3},
    {"total": 3}, ["not a report"],
])
def test_invalid_drill_evidence_is_unknown(watch, data):
    for drill in ("chaos", "succession"):
        save_report(watch, f"{drill}/latest.json", data)
    output = watch.NightWatchAgent().perform(action="check")
    assert "unknown" in output.lower()
    assert "drills passed" not in output


def test_fresh_valid_evidence_can_pass(watch, monkeypatch):
    good_drills(watch)
    save_report(watch, "last-boot.json", {"fallback": False})
    monkeypatch.setattr(watch, "_plist", lambda label: True)
    monkeypatch.setattr(watch, "_up", lambda url: True)
    output = watch.NightWatchAgent().perform(action="check")
    assert output.startswith("All good:")
    assert "drills passed" in output
    assert "services answer" in output
    assert "started normally" in output


def test_live_service_failure_is_not_reassuring(watch, monkeypatch):
    good_drills(watch)
    monkeypatch.setattr(watch, "_plist", lambda label: True)
    monkeypatch.setattr(watch, "_up", lambda url: False)
    output = watch.NightWatchAgent().perform(action="check")
    assert "not answering" in output
    assert "services answer" not in output


def test_no_declared_services_is_not_a_pass(watch, monkeypatch):
    monkeypatch.setattr(watch, "SERVICES", {})
    output = watch.NightWatchAgent().perform(action="check")
    assert "not configured" in output
    assert "services answer" not in output


def test_failed_drill_remains_a_failure(watch):
    good_drills(watch)
    save_report(watch, "chaos/latest.json", {"survived": 2, "total": 3})
    output = watch.NightWatchAgent().perform(action="check")
    assert "chaos drill passed 2 of 3" in output
    assert "drills passed" not in output


def test_system_context_reports_unknown_once(watch):
    agent = watch.NightWatchAgent()
    first = agent.system_context()
    assert "unknown" in first.lower()
    assert agent.system_context() is None


@pytest.mark.parametrize("used", [85, 110])
def test_usage_warnings_are_explicitly_local_estimates(watch, monkeypatch, used):
    save_report(watch, "spend-guard.json", {"monthly": 100})
    monkeypatch.setattr(watch, "premium_used", lambda: used)
    agent = watch.NightWatchAgent()
    for output in (agent.perform(action="spend"), agent.perform(action="check"),
                   agent.system_context() or ""):
        if output:
            assert "estimate" in output.lower()
            assert "journal" in output.lower()
            assert "billed" in output.lower()


def test_fix_does_not_restart_unconfigured_services(watch, monkeypatch):
    def forbidden(*args, **kwargs):
        pytest.fail("unconfigured services must not be restarted")

    monkeypatch.setattr(watch.subprocess, "run", forbidden)
    output = watch.NightWatchAgent().perform(action="fix")
    assert "unknown" in output.lower()
    assert "not configured" in output.lower()
