"""Layer facts are file-sourced, deterministic and checked without running layer code."""

import ast
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from tools.sync_layers import (
    END, FACTS_END, FACTS_START, MARKER, ROOT,
    engine_text, main, read_facts, stamp_source, sync,
)

SHA_A = "a" * 64
SHA_B = "b" * 64


def source(proven=(SHA_A, SHA_B)):
    hashes = "\n".join(f'    "{sha}",  # 0.6.{index + 16}' for index, sha in enumerate(proven))
    return (
        '"""Layer: example - test hook without importing it."""\n'
        'raise AssertionError("a synchronizer must never execute this file")\n'
        'TOUCHES = {"flask.Flask.__init__"}\n'
        'WRAPS = {"requests.post"}\n'
        f"PROVEN_GRAIL = {{\n{hashes}\n}}\n"
        "def apply():\n    pass\n"
    ).encode()


def save(path, data):
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


@pytest.fixture
def workspace(tmp_path):
    (tmp_path / "LAYERS.md").write_text(
        f"# Hand-written contract\n\n{FACTS_START}\n{FACTS_END}\n\nKeep this prose.\n",
        encoding="utf-8",
    )
    save(tmp_path / "registry.json", {"agents": []})
    for name in ("first", "second"):
        directory = tmp_path / "stacks" / name
        directory.mkdir(parents=True)
        (directory / "example.py").write_bytes(source())
        (directory / "wrapper.py").write_bytes(source((SHA_B,)))
        (directory / "kernel.py").write_text('"""A replacement kernel, not an apply layer."""\n')
        (directory / "notes.txt").write_text("Keep its custom metadata.\n")
        parts = [
            {"id": f"@{name}/example", "kind": "layer", "point": "agents",
             "file": "example.py", "sha256": "stale", "locator": "https://example.test/old.py",
             "proven_grail": [SHA_B], "status": "alias of a kept name"},
            {"id": f"@{name}/wrapper", "kind": "layer", "point": "transport",
             "file": "wrapper.py", "sha256": "stale", "locator": "https://example.test/wrapper.py"},
            {"id": f"@{name}/kernel", "kind": "kernel", "point": "kernel",
             "file": "kernel.py", "sha256": "stale", "proven_grail": ["legacy metadata"],
             "locator": "https://example.test/kernel.py"},
        ]
        save(directory / "pack.json", {
            "name": name, "version": "1.2.3",
            "install": {"parts": parts, "seed": [f"@{name}/example", f"@{name}/wrapper"],
                        "layers": ["example.py"], "default_enabled": ["example"],
                        "proven_grail": {"example.py": [SHA_B]}},
            "kernel": {"sha256": SHA_A, "version": "0.6.16", "file": "brainstem.py"},
            "files": {filename: {"sha256": "stale", "size": 0, "custom": True}
                      for filename in ("example.py", "wrapper.py", "kernel.py", "notes.txt")},
        })
    return tmp_path


def pack_path(root, name="first"):
    return root / "stacks" / name / "pack.json"


def snapshot(root):
    return {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}


def test_check_passes_on_repository():
    assert sync(ROOT) == ([], 0)


def test_write_is_idempotent_and_check_is_read_only(workspace):
    before = snapshot(workspace)
    drifts, changed = sync(workspace)
    assert changed == 0 and drifts
    assert snapshot(workspace) == before
    _, changed = sync(workspace, write=True)
    assert changed > 0
    after = snapshot(workspace)
    assert sync(workspace, write=True) == ([], 0)
    assert sync(workspace) == ([], 0)
    assert snapshot(workspace) == after


def test_proven_drift_fails_cli_with_plain_diagnostic(workspace):
    sync(workspace, write=True)
    path = pack_path(workspace)
    pack = json.loads(path.read_bytes())
    pack["install"]["parts"][0]["proven_grail"] = [SHA_B, "c" * 64]
    save(path, pack)
    before = snapshot(workspace)
    tools = workspace / "tools"
    tools.mkdir()
    for filename in ("sync_layers.py", "stamp_ticket.py"):
        shutil.copyfile(ROOT / "tools" / filename, tools / filename)
    result = subprocess.run(
        [sys.executable, str(tools / "sync_layers.py"), "--check"],
        capture_output=True, text=True, cwd=workspace,
    )
    assert result.returncode == 1
    assert f"example: pack.json proven_grail lacks {SHA_A} that the file declares" in result.stdout
    assert f"includes {'c' * 64} that the file does not declare" in result.stdout
    assert result.stdout.endswith("1 drifts\n")
    assert not result.stderr
    assert all((workspace / path).read_bytes() == body for path, body in before.items())


def test_generated_facts_pins_aliases_and_pages(workspace):
    originals = {name: json.loads(pack_path(workspace, name).read_bytes()) for name in ("first", "second")}
    source_before = (workspace / "stacks/first/example.py").read_bytes()
    sync(workspace, write=True)
    for name, old in originals.items():
        path = pack_path(workspace, name)
        pack = json.loads(path.read_bytes())
        assert pack["kernel"] == {**old["kernel"], "proven": [SHA_B]}
        assert pack["install"]["layers"] == old["install"]["layers"]
        assert pack["install"]["default_enabled"] == old["install"]["default_enabled"]
        assert pack["install"]["proven_grail"] == {"example.py": [SHA_A, SHA_B]}
        for part, previous in zip(pack["install"]["parts"], old["install"]["parts"]):
            body = (path.parent / part["file"]).read_bytes()
            assert part["sha256"] == hashlib.sha256(body).hexdigest()
            assert part["locator"] == previous["locator"]
            if part["kind"] == "kernel":
                assert part["proven_grail"] == previous["proven_grail"]
                assert MARKER.encode() not in body
                continue
            facts = read_facts(body, part["file"])
            assert part["proven_grail"] == facts["PROVEN_GRAIL"]
            assert part["touches"] == facts["TOUCHES"]
            assert part["wraps"] == facts["WRAPS"]
            assert part["what"] == facts["what"]
            page = workspace / "a" / part["id"]
            markdown = (page / "agent.md").read_text()
            html = (page / "index.html").read_text()
            assert f"update my Brainstem with {part['id']}" in markdown
            assert f"--remove {name}" in markdown
            assert "/api/ticket" in markdown and "[grail-layers] grail" in markdown
            assert f"{part['proven_grail'][0][:12]} (v0.6.16)" in markdown
            assert "TOUCHES (exclusive)" in markdown and "WRAPS (composable)" in markdown
            assert f"/stacks/{name}/{part['file']}" in markdown
            assert "LAYERS.md" in html and "<script" not in html
        for filename, metadata in pack["files"].items():
            body = (path.parent / filename).read_bytes()
            assert metadata == {"sha256": hashlib.sha256(body).hexdigest(), "size": len(body), "custom": True}
    stamped = (workspace / "stacks/first/example.py").read_bytes()
    assert ast.dump(ast.parse(source_before)) == ast.dump(ast.parse(stamped))
    docs = (workspace / "LAYERS.md").read_text()
    assert docs.startswith("# Hand-written contract") and docs.endswith("Keep this prose.\n")
    assert "Not a layer; no PROVEN_GRAIL declaration" in docs


@pytest.mark.parametrize("seed,expected", [([], []), (["@first/example"], [SHA_A, SHA_B]), (None, [SHA_B])])
def test_kernel_proven_is_seed_intersection(workspace, seed, expected):
    path = pack_path(workspace)
    pack = json.loads(path.read_bytes())
    if seed is None:
        del pack["install"]["seed"]
    else:
        pack["install"]["seed"] = seed
    save(path, pack)
    sync(workspace, write=True)
    assert json.loads(path.read_bytes())["kernel"]["proven"] == expected


def test_legacy_layer_filename_is_ticketed_and_pinned(workspace):
    path = pack_path(workspace)
    pack = json.loads(path.read_bytes())
    canonical = path.parent / "example_v2.py"
    canonical.write_bytes(source())
    pack["install"]["parts"][0]["file"] = canonical.name
    pack["files"][canonical.name] = {"size": 0, "sha256": "stale"}
    save(path, pack)
    sync(workspace, write=True)
    assert MARKER.encode() in (path.parent / "example.py").read_bytes()
    assert MARKER.encode() in canonical.read_bytes()
    assert sync(workspace) == ([], 0)


def test_stale_ticket_is_replaced_without_behavior_change():
    part = {"id": "@test/example", "file": "example.py"}
    body = b"\xef\xbb\xbf#!/usr/bin/env python3\r\n# coding: utf-8\r\n" + source().replace(b"\n", b"\r\n")
    facts = read_facts(body, part["file"])
    stamped = stamp_source(body, part, facts, "test")
    assert stamped.startswith(b"\xef\xbb\xbf#!/usr/bin/env python3\r\n# coding: utf-8\r\n")
    assert ast.dump(ast.parse(body)) == ast.dump(ast.parse(stamped))
    stale = stamped.replace(b"update my Brainstem", b"old instructions")
    assert stamp_source(stale, part, facts, "test") == stamped
    assert stamped.count(MARKER.encode()) == 1 and END.encode() in stamped


def test_unknown_version_is_not_guessed():
    facts = read_facts(source().replace(b"# 0.6.16", b"# public engine"), "example.py")
    assert f"{SHA_A[:12]} (version not declared)" in engine_text(facts)


@pytest.mark.parametrize("bad", [
    b"PROVEN_GRAIL = get_proof()\n",
    b'PROVEN_GRAIL = {"not a sha"}\n',
    b"PROVEN_GRAIL = 42\n",
    b"PROVEN_GRAIL = {1}\n",
    source() + b"PROVEN_GRAIL = set()\n",
])
def test_invalid_declarations_are_errors(bad):
    with pytest.raises(ValueError):
        read_facts(bad, "bad.py")


@pytest.mark.parametrize("defect", ["seed", "path", "agent-collision", "docs", "ticket"])
def test_invalid_inputs_write_nothing(workspace, defect):
    path = pack_path(workspace)
    pack = json.loads(path.read_bytes())
    if defect == "seed":
        pack["install"]["seed"] = ["@first/missing"]
    elif defect == "path":
        pack["install"]["parts"][0]["file"] = "../outside.py"
    elif defect == "agent-collision":
        save(workspace / "registry.json", {"agents": [{"name": "@first/example"}]})
    elif defect == "docs":
        (workspace / "LAYERS.md").write_text("Missing generated markers\n")
    else:
        (path.parent / "example.py").write_bytes((MARKER + "\n").encode() + source())
    save(path, pack)
    before = snapshot(workspace)
    with pytest.raises(ValueError):
        sync(workspace, write=True)
    assert snapshot(workspace) == before


def test_cli_returns_zero_for_clean_repo(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["sync_layers.py", "--check"])
    assert main() == 0
    assert capsys.readouterr().out == "0 drifts\n"
