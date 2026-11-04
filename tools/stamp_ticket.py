#!/usr/bin/env python3
"""Stamp registry-listed artifacts with comment-only RAPP loading tickets.

Run from any directory: python3 tools/stamp_ticket.py [--check].
Only registry.json's canonical files are stamped; helpers and withheld agents
are not discovered independently. Rebuild with python3 build_registry.py after
minting matching maintainer receipts for the changed public agents.
"""

from __future__ import annotations

import argparse
import ast
import codecs
import json
import re
import tokenize
from io import BytesIO
from pathlib import Path, PurePosixPath
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://kody-w.github.io/RAR"
MARKER = "# ── RAPP ticket"
CODING = re.compile(br"^[ \t\f]*#.*?coding[:=][ \t]*([-\w.]+)")


def agent_path(agent: dict) -> PurePosixPath:
    path = PurePosixPath(agent["_file"])
    name = agent["name"]
    if (
        path.is_absolute()
        or ".." in path.parts
        or path.parts[0] != "agents"
        or not re.fullmatch(r"@[A-Za-z0-9_-]+/[A-Za-z0-9_-]+", name)
    ):
        raise ValueError(f"Unsafe ticket identity or path: {name}: {path}")
    return path


def page_url(agent: dict) -> str:
    agent_path(agent)
    return f"{SITE}/a/{quote(agent['name'], safe='@/')}/"


def ticket_text(agent: dict) -> str:
    path = agent_path(agent)
    return f"""# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL {SITE}/{path} -o ~/.brainstem/src/rapp_brainstem/agents/{path.name}
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {{"user_input": "..."}}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: {page_url(agent)}
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""


def ticket_position(source: bytes) -> int:
    """Keep the BOM, shebang and PEP 263 cookie in their original positions."""
    bom = len(codecs.BOM_UTF8) if source.startswith(codecs.BOM_UTF8) else 0
    lines = source[bom:].splitlines(keepends=True)
    keep = 1 if lines and lines[0].startswith(b"#!") else 0
    for index, line in enumerate(lines[:2]):
        if CODING.match(line):
            keep = max(keep, index + 1)
    return bom + sum(len(line) for line in lines[:keep])


def ticket_bytes(source: bytes, agent: dict) -> bytes:
    encoding, _ = tokenize.detect_encoding(BytesIO(source).readline)
    if codecs.lookup(encoding).name not in {"utf-8", "utf-8-sig", "ascii"}:
        raise ValueError(f"{agent['_file']}: Unicode ticket requires a UTF-8 source")
    newline = "\r\n" if b"\r\n" in source else "\n"
    return ticket_text(agent).replace("\n", newline).encode("utf-8")


def strip_ticket(source: bytes, agent: dict) -> bytes:
    offset = ticket_position(source)
    block = ticket_bytes(source, agent)
    if source[offset:offset + len(block)] == block:
        return source[:offset] + source[offset + len(block):]
    return source


def stamp_source(source: bytes, agent: dict) -> bytes:
    if MARKER.encode("utf-8") in source:
        return source
    offset = ticket_position(source)
    if offset and not source[:offset].endswith((b"\n", codecs.BOM_UTF8)):
        raise ValueError(f"{agent['_file']}: protected header has no final newline")
    result = source[:offset] + ticket_bytes(source, agent) + source[offset:]
    if ast.dump(ast.parse(source)) != ast.dump(ast.parse(result)):
        raise ValueError(f"{agent['_file']}: ticket changed the AST")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check without writing")
    args = parser.parse_args()
    agents = json.loads((ROOT / "registry.json").read_text(encoding="utf-8"))["agents"]
    missing = changed = 0
    for agent in agents:
        path = ROOT / agent_path(agent)
        source = path.read_bytes()
        if strip_ticket(source, agent) != source:
            continue
        missing += 1
        if args.check:
            print(f"Missing or invalid ticket: {agent['_file']}")
            continue
        result = stamp_source(source, agent)
        if result == source:
            raise ValueError(f"{path}: existing marker does not match the expected ticket")
        path.write_bytes(result)
        changed += 1
    if args.check:
        print(f"{missing} agents missing a ticket ({len(agents)} checked)")
        return int(bool(missing))
    print(f"Stamped {changed} files ({len(agents)} registry agents checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
