"""The notary refreshes declared copies so a source change never strands its copy."""
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import sync_declared_copies as sdc


def _tree(tmp):
    (tmp / "agents").mkdir()
    (tmp / "agents" / "a_agent.py").write_bytes(b"new bytes, longer\n")
    s = tmp / "stacks" / "one"
    s.mkdir(parents=True)
    (s / "a_agent.py").write_bytes(b"old\n")
    (s / "own.py").write_bytes(b"mine\n")
    (s / "pack.json").write_text(json.dumps({"files": {
        "a_agent.py": {"source": "agents/a_agent.py", "size": 4, "sha256": hashlib.sha256(b"old\n").hexdigest()},
        "own.py": {"sha256": hashlib.sha256(b"mine\n").hexdigest()}}}, indent=2))
    return s


def test_refresh_copies_the_source_and_resigns_only_that_entry(tmp_path):
    s = _tree(tmp_path)
    assert sdc.sync(tmp_path, write=False) == ["one/a_agent.py"] and (s / "a_agent.py").read_bytes() == b"old\n"
    assert sdc.sync(tmp_path) == ["one/a_agent.py"]
    files = json.loads((s / "pack.json").read_text())["files"]
    body = b"new bytes, longer\n"
    assert (s / "a_agent.py").read_bytes() == body
    assert files["a_agent.py"] == {"source": "agents/a_agent.py", "size": len(body), "sha256": hashlib.sha256(body).hexdigest()}
    assert files["own.py"]["sha256"] == hashlib.sha256(b"mine\n").hexdigest() and (s / "own.py").read_bytes() == b"mine\n"
    assert sdc.sync(tmp_path) == []
    assert sdc.declared(tmp_path) == ["stacks/one/a_agent.py"]


def test_the_catalog_has_no_drifted_copy_today():
    assert sdc.sync(Path("."), write=False) == []
