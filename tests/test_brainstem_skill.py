"""Brainstem skill: one page hatches any AI into a Brainstem, permanently, with a clean off switch."""
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

import pytest

STACK = Path(__file__).resolve().parent.parent / "stacks" / "brainstem-skill"
PAGE = (STACK / "SKILL.md").read_text()
FENCE = "`" * 4


def test_the_page_carries_the_exact_loop_and_states_its_fingerprint():
    start = PAGE.index("<!-- file: rapp/kernel.py -->\n" + FENCE + "python\n") + len("<!-- file: rapp/kernel.py -->\n" + FENCE + "python\n")
    block = PAGE[start:PAGE.index(FENCE + "\n<!-- end -->", start)]
    assert block == (STACK / "kernel.py").read_text()
    stated = re.search(r"sha256 must be\s+`([0-9a-f]{64})`", PAGE).group(1)
    assert stated == hashlib.sha256(block.encode()).hexdigest()


def test_the_page_asks_for_a_yes_before_anything_is_written():
    assert PAGE.index("wait for a yes") < PAGE.index("Then do this, in order")


ECHO = '''from agents.basic_agent import BasicAgent


class EchoAgent(BasicAgent):
    def __init__(self):
        super().__init__("Echo", {"name": "Echo", "description": "d", "parameters": {}})

    def perform(self, **kw):
        return "echo " + kw.get("say", "")
'''


@pytest.fixture
def home(tmp_path, monkeypatch):
    (tmp_path / "rapp" / "agents").mkdir(parents=True)
    (tmp_path / "rapp" / "kernel.py").write_text((STACK / "kernel.py").read_text())
    monkeypatch.delenv("CHANT_HOME", raising=False)
    for m in [m for m in sys.modules if m == "agents" or m.startswith("agents.")]:
        monkeypatch.delitem(sys.modules, m)
    monkeypatch.setattr(sys, "path", list(sys.path))
    spec = importlib.util.spec_from_file_location("rapp_kernel_under_test", tmp_path / "rapp" / "kernel.py")
    k = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(k)
    (k.AGENTS / "basic_agent.py").write_text(k.BASIC)
    (k.AGENTS / "echo_agent.py").write_text(ECHO)
    return tmp_path, k


def _remove_agents(k):
    for f in k.AGENTS.rglob("*"):
        if f.is_file():
            f.unlink()
    for d in sorted([d for d in k.AGENTS.rglob("*") if d.is_dir()], reverse=True):
        d.rmdir()
    k.AGENTS.rmdir()


def test_agents_load_fresh_from_the_folder_every_time(home):
    root, k = home
    found, broken = k.load()
    assert sorted(found) == ["Echo"] and broken == {} and found["Echo"].perform(say="hi") == "echo hi"
    (k.AGENTS / "echo_agent.py").unlink()
    assert k.load()[0] == {}


def test_staying_is_idempotent_and_keeps_what_was_there(home):
    root, k = home
    (root / "CLAUDE.md").write_text("# Mine\n\nBe kind.\n")
    assert k.stay() == ["CLAUDE.md"] and k.stay() == ["CLAUDE.md"]
    text = (root / "CLAUDE.md").read_text()
    assert text.startswith("# Mine\n\nBe kind.\n") and text.count("<!-- rapp:begin -->") == 1
    assert not (root / "AGENTS.md").exists()


def test_with_no_instructions_file_it_makes_one(home):
    root, k = home
    assert k.stay() == ["AGENTS.md"] and "rapp/kernel.py tools" in (root / "AGENTS.md").read_text()


def test_the_note_names_python_by_a_plain_command_never_a_path(home):
    assert home[1]._py() in ("python3", "python", "py -3")


def test_deleting_the_agents_folder_puts_everything_back(home, capsys):
    root, k = home
    before = "# Mine\n\nBe kind.\n"
    (root / "AGENTS.md").write_text(before)
    k.stay()
    _remove_agents(k)
    assert k.main(["kernel.py", "tools"]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["tools"] == [] and "off" in out
    assert (root / "AGENTS.md").read_text() == before and not k.AGENTS.exists()


def test_a_note_file_it_created_is_removed_again(home, capsys):
    root, k = home
    k.stay()
    _remove_agents(k)
    k.main(["kernel.py", "tools"])
    assert not (root / "AGENTS.md").exists()


def test_import_checks_the_fingerprint(home):
    root, k = home
    body = b"x = 1\n"
    assert k.add("new_agent.py", body, "0" * 64)[0] == 400 and not (k.AGENTS / "new_agent.py").exists()
    assert k.add("new_agent.py", body, hashlib.sha256(body).hexdigest())[0] == 200
    assert k.add("../../escape.py", body)[0] == 400


def test_the_door_answers_in_a_brainstems_shape(home):
    k = home[1]
    out = k.envelope('noise {"not": "it"} then {"response": "pong", "agent_logs": "[Ping] pong", "model": "m"} bye', "s-1")
    assert sorted(out) == ["agent_logs", "model", "requested_model", "response", "session_id", "voice_mode"]
    assert out["response"] == "pong" and out["session_id"] == "s-1"
    assert k.envelope("just words", "s-2")["response"] == "just words"


def test_the_page_never_writes_into_a_rapp_folder_that_is_not_its_own():
    assert "Never write into it. Use `rapp-skill/` instead" in PAGE


def test_the_note_names_the_folder_it_actually_lives_in(tmp_path, monkeypatch):
    home = tmp_path / "rapp-skill"
    (home / "agents").mkdir(parents=True)
    (home / "kernel.py").write_text((STACK / "kernel.py").read_text())
    monkeypatch.delenv("CHANT_HOME", raising=False)
    spec = importlib.util.spec_from_file_location("rapp_kernel_other_home", home / "kernel.py")
    k = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(k)
    k.stay()
    note = (tmp_path / "AGENTS.md").read_text()
    assert "rapp-skill/kernel.py tools" in note and "`rapp-skill/agents/`" in note
    assert "rapp/kernel.py" not in note.replace("rapp-skill/kernel.py", "")
