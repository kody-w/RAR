import importlib.util, json, sys, tempfile, pathlib, subprocess
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import tombstone


def test_stub_is_valid_python_that_declares_itself():
    src = tombstone.render_stub("@x/y_agent", "Superseded by an outside channel.", "https://example.org/y", "1.2.0")
    assert tombstone.is_tombstone(src)
    compile(src, "stub.py", "exec")
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "y_agent.py"; p.write_text(src)
        spec = importlib.util.spec_from_file_location("stub", p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        assert m.__manifest__["name"] == "@x/y_agent"
        out = m.YAgentTombstoneAgent().perform()
        assert out.startswith("RETIRED: @x/y_agent") and "example.org" in out


def test_registry_and_discovery_skip_tombstones():
    sys.path.insert(0, str(ROOT))
    import build_registry
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "gone_agent.py"
        p.write_text(tombstone.render_stub("@x/gone_agent", "retired", "", "1.0.0"))
        assert build_registry._is_tombstone_file(p)
        live = pathlib.Path(d) / "live_agent.py"; live.write_text('__manifest__ = {"name": "@x/live_agent"}\n')
        assert not build_registry._is_tombstone_file(live)


def test_url_contract_holds_for_a_stub_path():
    # the checker asks only that the path is a file — a tombstone satisfies the promise
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "agents" / "@x" / "gone_agent.py"; p.parent.mkdir(parents=True)
        p.write_text(tombstone.render_stub("@x/gone_agent", "retired", "", "1.0.0"))
        assert p.is_file()


def test_a_card_agent_retires_the_same_way(tmp_path):
    """Article XXIII.3 covers .py.card agents too: the stub at the old path is skipped, not listed."""
    sys.path.insert(0, str(ROOT))
    import build_registry
    card = tmp_path / "old_agent.py.card"
    card.write_text(tombstone.render_stub("@x/old_agent", "retired", "", "1.0.0"))
    assert build_registry._is_tombstone_file(card)
    live = tmp_path / "live_agent.py.card"
    live.write_text('"""a live card agent"""\n__manifest__ = {}\n')
    assert not build_registry._is_tombstone_file(live)


def test_removed_agents_keep_their_original_bytes():
    """The two agents removed on 2026-07-23 are kept byte for byte under versions/."""
    import hashlib
    kept = {"@borg/hacker_news_agent": "versions/@borg/hacker_news_agent/e83a236ebf1f.py",
            "@howardh/borg_agent": "versions/@howardh/borg_agent/14b1b1690457.py.card"}
    stones = {t["agent"]: t for t in json.loads((ROOT / "registry.json").read_text())["lifecycle"]["tombstones"]}
    for name, path in kept.items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == stones[name]["sha256"], f"{name}: kept bytes differ"
