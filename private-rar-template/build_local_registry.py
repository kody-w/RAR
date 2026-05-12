#!/usr/bin/env python3
"""
Local registry builder for a private RAR instance.

Scans agents/@<publisher>/*.py, AST-extracts each __manifest__, and
writes private-registry.json — the same shape as public RAR's
registry.json, just scoped to your private agents.

This file is intentionally small. It is NOT a replacement for the
public build_registry.py (no holo cards, no swarms, no security
scan, no provenance chain). It exists so you can `python
build_local_registry.py` to see what's in your private store.

The public RAR's brainstem does not consume this file — it consumes
stubs in public RAR, which point back to individual agent files in
this repo. private-registry.json is for YOU, not for federation.
"""
from __future__ import annotations
import ast
import hashlib
import json
from pathlib import Path
from datetime import datetime, timezone

AGENTS_DIR = Path("agents")
OUT = Path("private-registry.json")
REQUIRED = ["schema", "name", "version", "display_name",
            "description", "author", "tags", "category"]


def extract_manifest(py: Path) -> dict | None:
    try:
        tree = ast.parse(py.read_text())
    except SyntaxError:
        return None
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == "__manifest__":
                    try:
                        return ast.literal_eval(node.value)
                    except (ValueError, TypeError):
                        return None
    return None


def main() -> int:
    if not AGENTS_DIR.exists():
        print(f"No {AGENTS_DIR}/ directory found — nothing to build.")
        return 0

    agents = []
    errors = []
    for py in sorted(AGENTS_DIR.rglob("*.py")):
        if py.name in ("__init__.py", "basic_agent.py"):
            continue
        m = extract_manifest(py)
        if not m:
            continue
        missing = [f for f in REQUIRED if f not in m]
        if missing:
            errors.append(f"{py}: missing {missing}")
            continue
        m["_file"] = str(py)
        m["_sha256"] = hashlib.sha256(py.read_bytes()).hexdigest()
        m["_size_kb"] = round(py.stat().st_size / 1024, 1)
        agents.append(m)

    registry = {
        "schema": "rapp-registry/1.1",
        "role": "private",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "stats": {"total_agents": len(agents)},
        "agents": agents,
    }
    OUT.write_text(json.dumps(registry, indent=2))
    print(f"Wrote {OUT} — {len(agents)} agent(s)")
    if errors:
        print(f"\n{len(errors)} manifest error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
