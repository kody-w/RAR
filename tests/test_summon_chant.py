"""Summon by chant: seven words bring one agent, a whole stack, or a stack with its egg.

Contract:
  * the word list is read from rapp_sdk.py, never copied;
  * every file is checked against its catalog sha256 before the Brainstem sees it;
  * only notarized agents and verified, current, non-kernel stacks install;
  * an egg is kept on the device and the catalog's own hatcher is brought to open it.
"""
import hashlib
import importlib.util
import json
import sys
import types
from pathlib import Path

import pytest

import rapp_sdk

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://catalog.test"


def _sha(b):
    return hashlib.sha256(b).hexdigest()


AGENT, A1, A2, EGG, HATCH = b"agent\n", b"one\n", b"two\n", b"egg-bytes", b"hatcher\n"
REG = {
    "agents": [
        {"name": "@t/hello_agent", "display_name": "Hello", "_seed": 111111111, "_lifecycle": "notarized",
         "_file": "agents/@t/hello_agent.py", "_install_filename": "rar_t_hello_agent.py", "_sha256": _sha(AGENT)},
        {"name": "@t/draft_agent", "_seed": 222222222, "_lifecycle": "pending",
         "_file": "agents/@t/draft_agent.py", "_install_filename": "rar_t_draft_agent.py", "_sha256": _sha(AGENT)},
        {"name": "@rapp/egg_hatcher", "_seed": 333333333, "_lifecycle": "notarized",
         "_file": "agents/@rapp/egg_hatcher_agent.py", "_install_filename": "rar_rapp_egg_hatcher_agent.py",
         "_sha256": _sha(HATCH)},
    ],
    "stack_packs": [
        {"name": "pair", "display_name": "Pair Stack", "_seed": 444444444, "_verified": True, "path": "stacks/pair",
         "files": {"a_agent.py": {"sha256": _sha(A1)}, "b_agent.py": {"sha256": _sha(A2)}, "README.md": {"sha256": "x"}}},
        {"name": "nest", "display_name": "Nest", "_seed": 555555555, "_verified": True, "path": "stacks/nest",
         "files": {"a_agent.py": {"sha256": _sha(A1)}, "nest.egg": {"sha256": _sha(EGG)}}},
        {"name": "drift", "_seed": 666666666, "_verified": False, "path": "stacks/drift",
         "files": {"a_agent.py": {"sha256": _sha(A1)}}},
        {"name": "gone", "_seed": 777777777, "_verified": True, "status": "retired", "path": "stacks/gone",
         "retired": {"reason": "Replaced.", "replacement": "pair"}, "files": {"a_agent.py": {"sha256": _sha(A1)}}},
        {"name": "whole", "_seed": 888888888, "_verified": True, "kernel": {"sha": "abc"}, "path": "stacks/whole",
         "files": {"a_agent.py": {"sha256": _sha(A1)}}},
        {"name": "bad", "_seed": 999999999, "_verified": True, "path": "stacks/bad",
         "files": {"a_agent.py": {"sha256": _sha(b"what the catalog promised")}}},
    ],
}
WEB = {
    f"{BASE}/registry.json": json.dumps(REG).encode(),
    f"{BASE}/rapp_sdk.py": (ROOT / "rapp_sdk.py").read_bytes(),
    f"{BASE}/agents/@t/hello_agent.py": AGENT,
    f"{BASE}/agents/@rapp/egg_hatcher_agent.py": HATCH,
    f"{BASE}/stacks/pair/a_agent.py": A1, f"{BASE}/stacks/pair/b_agent.py": A2,
    f"{BASE}/stacks/nest/a_agent.py": A1, f"{BASE}/stacks/nest/nest.egg": EGG,
    f"{BASE}/stacks/bad/a_agent.py": b"something else",
}


@pytest.fixture
def sc(tmp_path, monkeypatch):
    agents = types.ModuleType("agents")
    basic = types.ModuleType("agents.basic_agent")
    basic.BasicAgent = type("BasicAgent", (), {"__init__": lambda self, *a, **k: None})
    monkeypatch.setitem(sys.modules, "agents", agents)
    monkeypatch.setitem(sys.modules, "agents.basic_agent", basic)
    monkeypatch.setenv("CHANT_HOME", str(tmp_path / "home"))
    monkeypatch.setenv("RAR_BASE", BASE)
    spec = importlib.util.spec_from_file_location("summon_chant_agent", ROOT / "stacks/summon/summon_chant_agent.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.landed = []
    monkeypatch.setattr(m, "_get", lambda url, keep=None, max_age=300: WEB[url])
    monkeypatch.setattr(m, "install", lambda f, payload, sha: (m.landed.append((f, sha)), (200, {"status": "ok"}))[1])
    return m


def chant(seed):
    return rapp_sdk.seed_to_words(seed)


def test_word_list_is_the_catalogs_and_round_trips(sc):
    assert sc.words() == list(rapp_sdk.MNEMONIC_WORDS)
    for seed in (111111111, 2 ** 63 + 12345, 0):
        assert sc.chant_to_seed(chant(seed)) == str(seed)
        assert sc.seed_to_chant(seed) == chant(seed)


def test_chant_brings_one_notarized_agent(sc):
    r = sc.summon(chant(111111111))
    assert r["ok"] and r["kind"] == "agent"
    assert sc.landed == [("rar_t_hello_agent.py", _sha(AGENT))]
    assert sc.summon("@t/hello")["ok"] and sc.summon("111111111")["ok"]


def test_unnotarized_agent_is_refused(sc):
    r = sc.summon(chant(222222222))
    assert not r["ok"] and "not notarized" in r["error"] and sc.landed == []


def test_chant_brings_every_agent_file_in_a_stack(sc):
    r = sc.summon(chant(444444444))
    assert r["ok"] and r["kind"] == "stack" and r["display"] == "Pair"
    assert [f for f, _ in sc.landed] == ["a_agent.py", "b_agent.py"]
    assert "2 agents" in sc.SummonChantAgent().perform(chant=chant(444444444))


def test_stack_with_an_egg_keeps_the_egg_and_brings_the_hatcher(sc, tmp_path):
    r = sc.summon(chant(555555555))
    assert r["ok"] and [f for f, _ in sc.landed] == ["a_agent.py", "rar_rapp_egg_hatcher_agent.py"]
    kept = Path(r["eggs"][0]["path"])
    assert kept.read_bytes() == EGG and tmp_path in kept.parents


@pytest.mark.parametrize("seed,says", [(666666666, "not verified"), (777777777, "retired"),
                                       (888888888, "whole Brainstem")])
def test_unverified_retired_and_kernel_stacks_are_refused(sc, seed, says):
    r = sc.summon(chant(seed))
    assert not r["ok"] and says in r["error"] and sc.landed == []
    if seed == 777777777:
        assert "Use pair instead" in r["error"]


def test_a_file_that_does_not_match_its_fingerprint_never_lands(sc):
    r = sc.summon(chant(999999999))
    assert not r["ok"] and "fingerprint" in r["error"] and sc.landed == []


def test_bad_chants_are_answered_in_plain_words(sc):
    a = sc.SummonChantAgent()
    assert a.perform(chant="SAGE ZAP") == "A chant is exactly 7 words."
    assert "is not a chant word" in a.perform(chant="BANANA " + " ".join(chant(1).split()[1:]))
    assert a.perform(chant=chant(123456789012)) == "No card answers to that chant."
    assert sc.landed == []


def test_the_rest_of_the_song_runs_once_what_was_brought_is_live(sc, monkeypatch):
    asked = []
    monkeypatch.setattr(sc, "carry_on", lambda then: (asked.append(then), "pong")[1])
    said = sc.SummonChantAgent().perform(chant=chant(111111111), then="Check it answers. Show me. And seal.")
    assert asked == ["(Just installed and live now: rar_t_hello_agent.py.) Check it answers. Show me"]
    assert said.endswith("this came back: pong")
    asked.clear()
    assert "ready on your next message" in sc.SummonChantAgent().perform(chant=chant(111111111))
    assert sc.SummonChantAgent().perform(chant="SAGE ZAP", then="Check it answers.") == "A chant is exactly 7 words."
    assert asked == []


def test_carrying_on_never_nests(sc):
    sc._hop["busy"] = True
    assert sc.carry_on("Check it answers.") is None


SONG = "R, A, P, P, verse. Bring MANTLE JAB DUSK PULSAR FULCRUM REVOKE SHARD. Check it answers. Show me. And seal."


def _team(sc, tmp_path, name="acme/shelf"):
    """A team catalog as it sits on a device: a git clone under the chant home. No network."""
    import subprocess
    origin = tmp_path / "origin.git"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(origin)], check=True)
    folder = sc._clone(name)
    subprocess.run(["git", "clone", "-q", str(origin), str(folder)], check=True, capture_output=True)
    for k, v in (("user.email", "t@example.test"), ("user.name", "t")):
        subprocess.run(["git", "-C", str(folder), "config", k, v], check=True)
    sc.build_catalog(folder, name)
    return folder, origin


def test_keeping_a_song_makes_a_card_with_its_own_chant(sc, tmp_path):
    folder, _ = _team(sc, tmp_path)
    said = sc.SummonChantAgent().perform(keep=SONG, title="Morning Check")
    reg = json.loads((folder / "registry.json").read_text())
    [card] = reg["agents"]
    assert card["display_name"] == "Morning Check" and card["_incantation"] in said
    assert sc.chant_to_seed(card["_incantation"]) == str(card["_seed"])
    src = (folder / "agents" / "morning_check_song_agent.py").read_text()
    compile(src, "card", "exec")
    assert SONG in src and sc.landed[-1][0] == "morning_check_song_agent.py"
    assert "starts" in sc.SummonChantAgent().perform(keep="Bring it.", title="x")


def test_team_card_lands_by_chant_and_says_where_it_came_from(sc, tmp_path):
    folder, _ = _team(sc, tmp_path)
    sc.keep_song("Morning Check", SONG)
    sc.landed.clear()
    card = json.loads((folder / "registry.json").read_text())["agents"][0]
    said = sc.SummonChantAgent().perform(chant=card["_incantation"])
    assert "your team catalog acme/shelf" in said and sc.landed == [("morning_check_song_agent.py", card["_sha256"])]
    (folder / "agents" / "morning_check_song_agent.py").write_text("changed after the catalog was built")
    assert "fingerprint" in sc.SummonChantAgent().perform(chant=card["_incantation"])


def test_a_team_seed_can_never_be_a_public_seed(sc):
    assert sc.team_seed("acme/shelf", "x") >> 63 == 1
    assert sc.team_seed("acme/shelf", "x") != sc.team_seed("other/shelf", "x")


def test_publish_waits_for_a_yes_then_sends(sc, tmp_path):
    import subprocess
    folder, origin = _team(sc, tmp_path)
    sc.keep_song("Morning Check", SONG)
    a = sc.SummonChantAgent()
    assert "Say yes to send" in a.perform(publish=True)
    assert subprocess.run(["git", "-C", str(origin), "log", "--oneline"], capture_output=True).returncode != 0
    assert a.perform(publish=True, yes=True).startswith("Published to acme/shelf")
    sent = subprocess.run(["git", "-C", str(origin), "show", "--stat", "--format=", "main"], capture_output=True, text=True).stdout
    assert "morning_check_song_agent.py" in sent and "registry.json" in sent
    assert a.perform(publish=True, yes=True) == "Nothing new to publish to acme/shelf."


def test_git_never_runs_with_the_brainstems_model_token(sc, monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", "x")
    monkeypatch.setenv("GH_TOKEN", "x")
    env = sc._own_sign_in()
    assert "GITHUB_TOKEN" not in env and "GH_TOKEN" not in env
