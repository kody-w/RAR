"""Agent files and shared links are self-contained loading tickets."""

import ast
import codecs
import hashlib
import json
import random
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

import pytest

import build_registry
from tools.build_agent_pages import agent_markdown, build_agent_pages
from tools.stamp_ticket import ROOT, SITE, page_url, stamp_source, strip_ticket, ticket_text

AGENTS = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))["agents"]
EXAMPLE = {
    "name": "@test/example_agent",
    "_file": "agents/@test/example_agent.py",
    "version": "1.0.0",
    "display_name": "Example <agent>",
    "description": 'An example with <markup> & "quotes".',
}


@pytest.mark.parametrize("agent", random.Random(0).sample(AGENTS, 50), ids=lambda a: a["name"])
def test_real_file_ast_equivalence_and_idempotency(agent):
    source = (ROOT / agent["_file"]).read_bytes()
    original = strip_ticket(source, agent)
    stamped = stamp_source(original, agent)
    assert ast.dump(ast.parse(original)) == ast.dump(ast.parse(stamped))
    assert stamped == source
    assert stamp_source(stamped, agent) == stamped
    assert strip_ticket(stamped, agent) == original


@pytest.mark.parametrize("header", [
    b"",
    b"#!/usr/bin/env python3\n",
    b"# -*- coding: utf-8 -*-\n",
    b"#!/usr/bin/env python3\n# coding=utf-8\n",
    b"# A heading\n# coding: utf-8\n",
    codecs.BOM_UTF8,
    codecs.BOM_UTF8 + b"#!/usr/bin/env python3\n",
    b"#!/usr/bin/env python3\r\n# coding: utf-8\r\n",
])
def test_headers_docstrings_and_future_imports_are_unchanged(header):
    source = header + b'"""Module documentation."""\nfrom __future__ import annotations\nVALUE = 1\n'
    stamped = stamp_source(source, EXAMPLE)
    assert stamped.startswith(header)
    assert ast.dump(ast.parse(source)) == ast.dump(ast.parse(stamped))
    assert strip_ticket(stamped, EXAMPLE) == source
    assert stamp_source(stamped, EXAMPLE) == stamped
    if b"\r\n" in header:
        assert b"in three steps:\r\n" in stamped


def test_stamper_rejects_non_utf8_cookie():
    with pytest.raises(ValueError, match="UTF-8"):
        stamp_source(b"# coding: latin-1\nVALUE = 1\n", EXAMPLE)


@pytest.mark.parametrize("agent", AGENTS, ids=lambda a: a["name"])
def test_every_registry_artifact_has_exact_ticket_and_static_pages(agent):
    source = (ROOT / agent["_file"]).read_bytes()
    assert strip_ticket(source, agent) != source
    directory = ROOT / "a" / agent["name"]
    markdown = (directory / "agent.md").read_text(encoding="utf-8")
    html = (directory / "index.html").read_text(encoding="utf-8")
    assert markdown == agent_markdown(agent)
    assert agent["name"] in markdown
    assert agent["description"] in markdown
    assert "<script" not in html.lower()
    assert 'href="agent.md"' in html
    assert "/#agent/" + agent["name"] in html
    assert 'POST /chat {"user_input": "..."}' in markdown
    assert "localhost:7071/health" in markdown
    for line in ticket_text(agent).splitlines():
        for word in line.split():
            if word.startswith("https://"):
                parsed = urlsplit(word)
                assert parsed.scheme == "https"
                assert parsed.hostname == "kody-w.github.io"
                assert not parsed.fragment
                assert parsed.path.startswith(("/RAR/", "/rapp-installer/"))
                assert all(token not in word for token in ("FILE", "PATH", "/ID/"))
    assert page_url(agent) == f"{SITE}/a/{agent['name']}/"


class PageText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def test_static_page_is_readable_without_javascript_and_build_is_idempotent(tmp_path):
    assert build_agent_pages([EXAMPLE], tmp_path) == 2
    directory = tmp_path / "a" / EXAMPLE["name"]
    paths = [directory / "index.html", directory / "agent.md"]
    before = [(p.read_bytes(), p.stat().st_mtime_ns) for p in paths]
    assert build_agent_pages([EXAMPLE], tmp_path) == 0
    assert before == [(p.read_bytes(), p.stat().st_mtime_ns) for p in paths]
    parser = PageText()
    parser.feed(paths[0].read_text())
    text = "".join(parser.parts)
    assert EXAMPLE["display_name"] in text
    assert EXAMPLE["description"] in text
    for step in ("1. Brainstem", "2. Hot-load", "3. Use it", "Can't run commands"):
        assert step in text


def test_gated_tickets_do_not_install_metadata_as_code():
    for agent in AGENTS:
        if agent.get("type") == "stub":
            markdown = agent_markdown(agent)
            assert "NOT executable agent code" in markdown
            assert f"rar install {agent['name']}" in markdown
            assert f"curl -fsSL {SITE}/{agent['_file']}" not in markdown


def test_card_page_explains_python_loader_filename():
    for agent in AGENTS:
        if agent["_file"].endswith(".py.card"):
            assert "rename" in agent_markdown(agent)
            assert Path(agent["_file"]).name.removesuffix(".card") in agent_markdown(agent)

def test_legacy_filename_pages_explain_python_loader_suffix():
    for agent in AGENTS:
        if agent["_file"].endswith(".py") and not agent["_file"].endswith("_agent.py"):
            assert "rename" in agent_markdown(agent)
            assert agent["_install_filename"] in agent_markdown(agent)


def test_check_cli_is_read_only():
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "stamp_ticket.py"), "--check"],
        cwd=ROOT, capture_output=True, text=True, timeout=30,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert f"0 agents missing a ticket ({len(AGENTS)} checked)" in result.stdout


def test_version_gate_allows_only_exact_ticket_insertion(tmp_path, monkeypatch):
    path = tmp_path / "agents" / "@test" / "example_agent.py"
    path.parent.mkdir(parents=True)
    source = b'"""Original documentation."""\nVALUE = 1\n'
    registry = tmp_path / "registry.json"
    entry = {
        **EXAMPLE,
        "_sha256": hashlib.sha256(source).hexdigest(),
    }
    registry.write_text(json.dumps({"agents": [entry]}))
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(build_registry, "REGISTRY_FILE", registry)
    stamped = stamp_source(source, EXAMPLE)
    path.write_bytes(stamped)
    assert build_registry.check_version_immutability(
        entry["name"], entry["version"], hashlib.sha256(stamped).hexdigest(), entry["_file"]
    ) is None
    for tampered in (
        stamped.replace(b"VALUE = 1", b"VALUE = 2"),
        stamped.replace(b"Original documentation", b"Modified documentation"),
        stamped.replace(b"# If your person", b"# A modified ticket"),
        stamped + b"# An unrelated comment\n",
    ):
        path.write_bytes(tampered)
        assert build_registry.check_version_immutability(
            entry["name"], entry["version"], hashlib.sha256(tampered).hexdigest(), entry["_file"]
        )


def test_homepage_ai_rule_and_share_links_keep_legacy_alias():
    homepage = (ROOT / "index.html").read_text()
    static_html = homepage.split("<body>", 1)[1].split("<script", 1)[0]
    assert '<h2 id="for-ais-title">For AIs</h2>' in static_html
    assert "https://kody-w.github.io/RAR/a/@pub/name/agent.md" in static_html
    assert "function shareAgent(name)" in homepage
    assert "new URL('a/' + name + '/'" in homepage
    assert "h.startsWith('#agent/')" in homepage
    advanced = (ROOT / "store.html").read_text()
    assert "new URL('a/' + name + '/'" in advanced
    assert "hash.startsWith('#agent/')" in advanced
