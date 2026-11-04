"""A filesystem listing is not evidence that a tool loaded."""

import importlib.util
from pathlib import Path


SOURCE = Path(__file__).resolve().parents[1] / "stacks/ticket-page/ticket_page.py"


def test_broken_agent_file_is_present_not_loaded(tmp_path, monkeypatch):
    (tmp_path / "broken_agent.py").write_text("this is not valid Python !!!")
    (tmp_path / "good_agent.py").write_text("raise RuntimeError('must not import to discover')")
    (tmp_path / "basic_agent.py").write_text("")
    monkeypatch.setenv("AGENTS_PATH", str(tmp_path))
    spec = importlib.util.spec_from_file_location("ticket_page_trust", SOURCE)
    page = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(page)
    ticket, status = page.handle("GET", "", None)
    assert status == 200
    assert "broken_agent.py" not in ticket["agents_loaded"]
    assert ticket["agent_files_present"] == ["broken_agent.py", "good_agent.py"]
    assert ticket["agents_loaded"] == []
    assert ticket["agents_loaded_status"] == "unknown"
    assert "not proof" in ticket["agents_loaded_note"].lower()
    assert "successful" in ticket["add_an_agent"]["how"].lower()
    assert not list(tmp_path.glob("__pycache__/*"))
    assert page.handle("POST", "", {})[1] == 405


def test_missing_folder_does_not_claim_runtime_has_no_tools(tmp_path, monkeypatch):
    monkeypatch.setenv("AGENTS_PATH", str(tmp_path / "absent"))
    spec = importlib.util.spec_from_file_location("ticket_page_missing", SOURCE)
    page = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(page)
    ticket, _ = page.handle("GET", "", None)
    assert ticket.get("agents_loaded_status") == "unknown"
    assert ticket["agent_files_present"] == []
