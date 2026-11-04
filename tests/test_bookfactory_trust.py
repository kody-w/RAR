"""BookFactory must stop when any persona or nested specialist fails."""

import builtins
import importlib.util
import json
import sys
import types
from pathlib import Path

import pytest


SOURCE = Path(__file__).resolve().parents[1] / "stacks/bookfactory/bookfactory_agent.py"
STAGES = ["Writer"] + ["Editor"] * 5 + ["CEO"] * 2 + ["Publisher", "Reviewer"]


@pytest.fixture
def factory(monkeypatch):
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            self.name, self.metadata = name, metadata

    basic = types.ModuleType("agents.basic_agent")
    basic.BasicAgent = BasicAgent
    monkeypatch.setitem(sys.modules, "agents.basic_agent", basic)
    utils = types.ModuleType("utils")
    utils.__path__ = []
    llm = types.ModuleType("utils.llm")
    monkeypatch.setitem(sys.modules, "utils", utils)
    monkeypatch.setitem(sys.modules, "utils.llm", llm)
    spec = importlib.util.spec_from_file_location("bookfactory_trust", SOURCE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, llm


@pytest.mark.parametrize("fail_at", range(10), ids=lambda i: f"{i + 1}-{STAGES[i]}")
def test_dispatch_failure_aborts_at_each_nested_stage(factory, tmp_path, fail_at):
    module, llm = factory
    calls = []

    def dispatch(messages):
        index = len(calls)
        calls.append(messages)
        if index == fail_at:
            raise RuntimeError("synthetic dispatch failure")
        return f"valid content {index}"

    llm.call_llm = dispatch
    result = module.BookFactory().perform(source="real notes", workspace=str(tmp_path))
    assert "incomplete" in result.lower()
    assert STAGES[fail_at].lower() in result.lower()
    assert "synthetic dispatch failure" in result
    assert "Book factory complete." not in result
    assert len(calls) == fail_at + 1
    assert not (tmp_path / "04-final-chapter.md").exists()
    assert not (tmp_path / "05-review.md").exists()
    status = json.loads((tmp_path / "run-status.json").read_text())
    assert status["status"] == "incomplete"
    assert status["stage"] == STAGES[fail_at]


@pytest.mark.parametrize("bad", [None, "", "   ", {"error": "failed"},
                                       "(LLM dispatch error: failed)", "(LLM error: failed)",
                                       "(LLM dispatch unavailable: failed)"])
def test_invalid_dispatch_output_is_not_a_final_chapter(factory, tmp_path, bad):
    module, llm = factory
    llm.call_llm = lambda messages: bad
    result = module.BookFactory().perform(source="notes", workspace=str(tmp_path))
    assert "incomplete" in result.lower()
    assert not (tmp_path / "04-final-chapter.md").exists()


def test_missing_dispatch_shim_is_incomplete(factory, tmp_path):
    module, _ = factory
    result = module.BookFactory().perform(source="notes", workspace=str(tmp_path))
    assert "incomplete" in result.lower()
    assert "Writer" in result
    assert not (tmp_path / "04-final-chapter.md").exists()


def test_success_and_failed_rerun_have_unambiguous_status(factory, tmp_path):
    module, llm = factory
    llm.call_llm = lambda messages: "real chapter content"
    result = module.BookFactory().perform(source="notes", workspace=str(tmp_path))
    assert "Book factory complete." in result
    final = tmp_path / "04-final-chapter.md"
    assert final.read_text() == "real chapter content"
    assert json.loads((tmp_path / "run-status.json").read_text())["status"] == "complete"
    llm.call_llm = lambda messages: ""
    result = module.BookFactory().perform(source="new notes", workspace=str(tmp_path))
    assert "incomplete" in result.lower()
    assert final.read_text() == "real chapter content"
    assert json.loads((tmp_path / "run-status.json").read_text())["status"] == "incomplete"


@pytest.mark.parametrize("filename", ["01-draft.md", "04-final-chapter.md", "run-status.json"])
def test_artifact_write_failures_are_explicit(factory, tmp_path, monkeypatch, filename):
    module, llm = factory
    llm.call_llm = lambda messages: "real content"

    def write_error(path, *args, **kwargs):
        if Path(path).name == filename:
            raise PermissionError("synthetic write denied")
        return builtins.open(path, *args, **kwargs)

    monkeypatch.setattr(module, "open", write_error, raising=False)
    result = module.BookFactory().perform(source="notes", workspace=str(tmp_path))
    assert "incomplete" in result.lower()
    assert "synthetic write denied" in result
    if filename == "run-status.json":
        assert "Could not write run-status.json" in result
    else:
        assert json.loads((tmp_path / "run-status.json").read_text())["status"] == "incomplete"
