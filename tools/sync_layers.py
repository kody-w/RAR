#!/usr/bin/env python3
"""Synchronize layer declarations, tickets, pack pins, pages and LAYERS.md (stdlib only).

Run python3 tools/sync_layers.py --write after editing a part; --check never writes.
Layer source is parsed with AST, never imported or executed.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from html import escape
from pathlib import Path
from urllib.parse import quote

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools.stamp_ticket import ticket_position

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://kody-w.github.io/RAR"
PROTOCOL = "https://github.com/kody-w/rapp-1/tree/main/protocols/rapp-layer/1"
MARKER = "# ── RAPP layer ticket"
END = "# ── End RAPP layer ticket"
FACTS_START = "<!-- BEGIN GENERATED LAYER FACTS -->"
FACTS_END = "<!-- END GENERATED LAYER FACTS -->"
DECLARATIONS = ("PROVEN_GRAIL", "TOUCHES", "WRAPS")


def local_file(directory: Path, filename: str) -> Path:
    path = directory / filename
    if Path(filename).is_absolute() or ".." in Path(filename).parts:
        raise ValueError(f"{directory.name}: unsafe file path {filename}")
    if not path.resolve().is_relative_to(directory.resolve()):
        raise ValueError(f"{directory.name}: file escapes pack: {filename}")
    return path


def read_facts(source: bytes, label: str) -> dict:
    tree = ast.parse(source, filename=label)
    facts = {}
    versions = {}
    lines = source.decode("utf-8-sig").splitlines()
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        names = {target.id for target in node.targets if isinstance(target, ast.Name)}
        for name in names.intersection(DECLARATIONS):
            if name in facts:
                raise ValueError(f"{label}: duplicate {name} declaration")
            value = ast.literal_eval(node.value)
            if not isinstance(value, (set, list, tuple)) or not all(
                isinstance(item, str) and item for item in value
            ):
                raise ValueError(f"{label}: {name} must be a literal collection of strings")
            facts[name] = sorted(set(value))
            if name == "PROVEN_GRAIL":
                for sha in value:
                    if not re.fullmatch(r"[0-9a-f]{64}", sha):
                        raise ValueError(f"{label}: invalid PROVEN_GRAIL sha256 {sha}")
                for element in getattr(node.value, "elts", []):
                    comment = lines[element.end_lineno - 1].split("#", 1)[-1]
                    match = re.search(r"\b\d+\.\d+\.\d+(?:[-+][\w.-]+)?\b", comment)
                    if match:
                        versions[element.value] = match.group()
    facts["versions"] = versions
    doc = ast.get_docstring(tree) or ""
    facts["docstring"] = doc
    facts["what"] = doc.splitlines()[0] if doc else ""
    facts["apply"] = any(
        isinstance(node, ast.FunctionDef) and node.name == "apply" for node in tree.body
    )
    return facts


def engine_text(facts: dict) -> str:
    return ", ".join(
        f"{sha[:12]} (v{facts['versions'][sha]})" if sha in facts["versions"]
        else f"{sha[:12]} (version not declared)"
        for sha in facts["PROVEN_GRAIL"]
    ) or "None declared"


def commands(pack_name: str) -> tuple[str, str]:
    add = f"curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- {pack_name}"
    return add, f"curl -fsSL https://kody-w.github.io/grail-layers/add.sh | bash -s -- --remove {pack_name}"


def ticket_text(part: dict, facts: dict, pack_name: str) -> str:
    add, remove = commands(pack_name)
    return (
        f"{MARKER} ── {part['id']}\n"
        f"# What: {facts['what']}\n"
        f"# Add in chat: update my Brainstem with {part['id']}\n"
        f"# Or add the pack (its seeded parts): {add}\n"
        "# Check: GET http://localhost:7071/api/ticket (when the ticket-page pack is installed);\n"
        "#   confirm this file's label is in the supervisor log: [grail-layers] grail <sha>; applied: [...]; skipped: ...\n"
        f"#   Label: {Path(part['file']).stem}. Health alone is not proof; test /chat and /chat/stream.\n"
        f"# Remove the pack (keeps shared/user files): {remove}\n"
        "#   For a part added individually in chat, ask to remove its id or undo that shape change.\n"
        f"# Rules: {SITE}/LAYERS.md ; rapp/1 protocols/rapp-layer/1: {PROTOCOL}\n"
        f"{END}\n"
    )


def stamp_source(source: bytes, part: dict, facts: dict, pack_name: str) -> bytes:
    offset = ticket_position(source)
    before, body = source[:offset], source[offset:]
    newline = b"\r\n" if b"\r\n" in source else b"\n"
    if before and not before.endswith((b"\n", b"\xef\xbb\xbf")):
        raise ValueError(f"{part['file']}: protected header has no final newline")
    if body.startswith(MARKER.encode()):
        lines = body.splitlines(keepends=True)
        end = next((i for i, line in enumerate(lines) if line.rstrip() == END.encode()), None)
        if end is None or any(not line.startswith(b"#") for line in lines[:end + 1]):
            raise ValueError(f"{part['file']}: malformed layer ticket")
        body = b"".join(lines[end + 1:])
    if MARKER.encode() in body:
        raise ValueError(f"{part['file']}: misplaced layer ticket")
    ticket = ticket_text(part, facts, pack_name).encode().replace(b"\n", newline)
    result = before + ticket + body
    if ast.dump(ast.parse(source)) != ast.dump(ast.parse(result)):
        raise ValueError(f"{part['file']}: ticket changed the AST")
    return result


def page_contents(part: dict, facts: dict, pack_path: Path, root: Path, pack_name: str) -> dict:
    url = f"{SITE}/a/{quote(part['id'], safe='@/')}/"
    raw = f"{SITE}/{quote((pack_path.parent / part['file']).relative_to(root).as_posix(), safe='@/')}"
    markdown = (
        f"# {part['id']} - RAPP layer ticket\n\n"
        f"## What it changes\n\n{facts['docstring']}\n\n"
        f"Pack: {pack_name}\nKind: layer\nPoint: {part['point']}\n"
        f"Status: {part.get('status', 'current')}\n"
        f"TOUCHES (exclusive): {', '.join(facts.get('TOUCHES', [])) or 'None'}\n"
        f"WRAPS (composable): {', '.join(facts.get('WRAPS', [])) or 'None'}\n"
        f"Proven engines: {engine_text(facts)}\n\n"
        "## Add, check, remove\n\n"
        + "\n".join(line.removeprefix("# ") for line in ticket_text(part, facts, pack_name).splitlines()[2:-1])
        + "\n\nA pack command installs only its seeded parts; it does not select an unseeded alias. "
        "Use the publisher-scoped chat id for an individual part. Only load code you trust.\n\n"
        f"Raw file: {raw}\nPage: {url}\nPlain text for AIs: {url}agent.md\n"
        "\nFull PROVEN_GRAIL sha256 values:\n"
        + "\n".join(f"- {sha}" for sha in facts["PROVEN_GRAIL"]) + "\n"
    )
    html = (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{escape(part['id'])} - RAPP layer ticket</title>\n"
        f'<meta name="description" content="{escape(facts["what"], quote=True)}">\n'
        f'<link rel="canonical" href="{escape(url, quote=True)}">\n</head>\n<body>\n<main>\n'
        f"<h1>{escape(part['id'])}</h1>\n<p>{escape(facts['what'])}</p>\n"
        "<h2>Add, check, remove this layer</h2>\n"
        f'<pre style="white-space:pre-wrap">{escape(markdown)}</pre>\n'
        f'<p><a href="{escape(raw, quote=True)}">Raw file</a> | '
        '<a href="agent.md">Plain text for AIs</a> | '
        f'<a href="{SITE}/LAYERS.md">Write a layer</a></p>\n'
        "</main>\n</body>\n</html>\n"
    )
    return {"agent.md": markdown, "index.html": html}


def sync(root: Path = ROOT, *, write: bool = False) -> tuple[list[str], int]:
    """Plan all outputs before writing; return human-readable drifts and changed-file count."""
    outputs: dict[Path, bytes] = {}
    drifts = []
    rows = []
    pages = set()
    registry = json.loads((root / "registry.json").read_bytes())
    agent_names = {agent["name"] for agent in registry["agents"]}

    def output(path: Path, content: bytes, message: str) -> None:
        if path in outputs and outputs[path] != content:
            raise ValueError(f"{path.relative_to(root)}: conflicting generated outputs")
        outputs[path] = content
        if not path.exists() or path.read_bytes() != content:
            drifts.append(message)

    def field(entry: dict, key: str, expected, label: str) -> None:
        if entry.get(key) != expected:
            if key == "proven_grail":
                old = entry.get(key) or []
                details = [f"lacks {sha} that the file declares" for sha in expected if sha not in old]
                details += [f"includes {sha} that the file does not declare" for sha in old if sha not in expected]
                detail = "; ".join(details) or "is not the file's sorted PROVEN_GRAIL"
                drifts.append(f"{label}: pack.json proven_grail {detail}")
            else:
                drifts.append(f"{label}: pack.json {key} differs from generated file facts")
            entry[key] = expected

    for pack_path in sorted((root / "stacks").glob("*/pack.json")):
        pack = json.loads(pack_path.read_bytes())
        install = pack.get("install") or {}
        if "parts" not in install:
            continue
        pack_name = pack_path.parent.name
        if not re.fullmatch(r"[A-Za-z0-9_-]+", pack_name):
            raise ValueError(f"{pack_path}: unsafe pack name")
        facts_by_id = {}
        part_files = set()
        ids = set()
        for part in install["parts"]:
            identity = part["id"]
            if not re.fullmatch(r"@[A-Za-z0-9_-]+/[A-Za-z0-9_-]+", identity) or identity in ids:
                raise ValueError(f"{pack_name}: invalid or duplicate part id {identity}")
            ids.add(identity)
            path = local_file(pack_path.parent, part["file"])
            part_files.add(part["file"])
            source = path.read_bytes()
            facts = read_facts(source, str(path))
            if part["kind"] == "layer":
                if "PROVEN_GRAIL" not in facts or not facts["what"] or not facts["apply"]:
                    raise ValueError(f"{identity}: layer requires PROVEN_GRAIL, a docstring and apply()")
                facts_by_id[identity] = facts
                source = stamp_source(source, part, facts, pack_name)
                output(path, source, f"{identity}: {part['file']} ticket differs from file facts")
                field(part, "what", facts["what"], identity)
                for key in ("TOUCHES", "WRAPS"):
                    field(part, key.lower(), facts.get(key, []), identity)
                directory = root / "a" / identity
                if directory in pages or identity in agent_names:
                    raise ValueError(f"{identity}: layer ticket page collides with another part or agent")
                pages.add(directory)
                for filename, content in page_contents(part, facts, pack_path, root, pack_name).items():
                    output(directory / filename, content.encode(), f"{identity}: {filename} ticket page differs from file facts")
            if "PROVEN_GRAIL" in facts:
                field(part, "proven_grail", facts["PROVEN_GRAIL"], identity)
            field(part, "sha256", hashlib.sha256(source).hexdigest(), identity)
            proof = engine_text(facts) if "PROVEN_GRAIL" in facts else "Not a layer; no PROVEN_GRAIL declaration"
            seeded = install.get("seed")
            seed_label = "yes" if seeded is None or identity in seeded else "no"
            rows.append(
                f"| [{identity}](stacks/{pack_name}/{part['file']}) | {pack_name} | "
                f"{part['kind']} / {part['point']} | {seed_label} | {part.get('status', 'current')} | {proof} |"
            )

        # Published pre-parts filenames remain loadable and get the same comment-only ticket.
        for filename in sorted(set(pack.get("files", {})) - part_files):
            if not filename.endswith(".py"):
                continue
            path = local_file(pack_path.parent, filename)
            source = path.read_bytes()
            facts = read_facts(source, str(path))
            if "PROVEN_GRAIL" not in facts:
                continue
            matches = [p for p in install["parts"] if p["kind"] == "layer" and p["id"].split("/")[1] == path.stem]
            if len(matches) != 1:
                raise ValueError(f"{path}: legacy layer needs an unambiguous canonical part id")
            legacy = {**matches[0], "file": filename}
            output(path, stamp_source(source, legacy, facts, pack_name), f"{filename}: legacy layer ticket differs from file facts")

        legacy_proven = install.get("proven_grail")
        if isinstance(legacy_proven, dict):
            for filename in legacy_proven:
                path = local_file(pack_path.parent, filename)
                facts = read_facts(outputs.get(path, path.read_bytes()), str(path))
                if "PROVEN_GRAIL" not in facts:
                    raise ValueError(f"{filename}: legacy proven alias has no file declaration")
                field(legacy_proven, filename, facts["PROVEN_GRAIL"], f"{pack_name}: legacy proven_grail")
        seeded = install.get("seed")
        if seeded is not None and (not isinstance(seeded, list) or set(seeded) - ids):
            raise ValueError(f"{pack_name}: seed must list known part ids")
        proofs = [set(facts["PROVEN_GRAIL"]) for identity, facts in facts_by_id.items()
                  if seeded is None or identity in seeded]
        if "kernel" in pack:
            field(pack["kernel"], "proven", sorted(set.intersection(*proofs)) if proofs else [], f"{pack_name}: kernel")
        for filename, metadata in pack.get("files", {}).items():
            path = local_file(pack_path.parent, filename)
            source = outputs.get(path, path.read_bytes())
            field(metadata, "sha256", hashlib.sha256(source).hexdigest(), filename)
            field(metadata, "size", len(source), filename)
        content = (json.dumps(pack, indent=2, ensure_ascii=True) + "\n").encode()
        outputs[pack_path] = content
        if pack_path.read_bytes() != content and json.loads(pack_path.read_bytes()) == pack:
            drifts.append(f"{pack_name}: pack.json formatting differs")

    docs_path = root / "LAYERS.md"
    docs = docs_path.read_text(encoding="utf-8")
    if docs.count(FACTS_START) != 1 or docs.count(FACTS_END) != 1:
        raise ValueError("LAYERS.md: expected exactly one generated layer facts section")
    start = docs.index(FACTS_START) + len(FACTS_START)
    end = docs.index(FACTS_END)
    if end < start:
        raise ValueError("LAYERS.md: generated section markers are reversed")
    table = (
        "\n\nGenerated from `stacks/*/pack.json` identities/points and each part file's declarations. "
        "Versions come from comments beside the declared engine SHA, not from a guessed kernel pin.\n\n"
        "| Part / source | Pack | Kind / point | Seeded | Status | Proven engines (sha256 prefix / version) |\n"
        "|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n\n"
    )
    output(docs_path, (docs[:start] + table + docs[end:]).encode(), "LAYERS.md: generated part table differs from file facts")
    changed = 0
    if write:
        for path, content in outputs.items():
            if not path.exists() or path.read_bytes() != content:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
                changed += 1
    return drifts, changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="regenerate changed outputs")
    mode.add_argument("--check", action="store_true", help="report drift without writing")
    args = parser.parse_args()
    try:
        drifts, changed = sync(write=args.write)
    except (OSError, ValueError, SyntaxError) as error:
        print(f"Layer sync failed: {' '.join(str(error).splitlines())}", file=sys.stderr)
        return 1
    if args.check:
        for drift in drifts:
            print(drift)
        print(f"{len(drifts)} drifts")
        return int(bool(drifts))
    print(f"Updated {changed} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
