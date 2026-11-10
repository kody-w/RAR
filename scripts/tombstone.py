#!/usr/bin/env python3
"""tombstone.py — a retired agent keeps its path.

Article XXIII: a published path may never be renamed, moved, or deleted. Article XXIII.3:
a retired agent is replaced AT ITS PATH by a tombstone stub — a valid single-file agent that
imports cleanly, says it is retired, and points where the current version lives. Anyone who
installed the old path keeps resolving it; the registry, the store and discovery skip it.
"""
from __future__ import annotations

MARKER = "RAR_TOMBSTONE"


def render_stub(name: str, reason: str, upstream: str = "", version: str = "") -> str:
    slug = name.split("/", 1)[1] if "/" in name else name
    cls = "".join(p.capitalize() for p in slug.split("_")) or "Retired"
    reason = reason.replace('"""', "'''")
    return f'''"""RETIRED: {name}

This path is a promise, so it still resolves — but the agent that lived here has been retired.
{reason}
{"Current version: " + upstream if upstream else ""}
"""

{MARKER} = {{
    "name": "{name}",
    "retired_version": "{version}",
    "upstream": "{upstream}",
}}

__manifest__ = {{
    "schema": "rapp-agent/1.0",
    "name": "{name}",
    "version": "{version or '0.0.0'}",
    "display_name": "{cls} (retired)",
    "description": "Retired tombstone: this path resolves, the agent does not run here anymore.",
    "author": "RAR",
    "tags": ["retired", "tombstone"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}}

try:
    from agents.basic_agent import BasicAgent
except Exception:  # standalone execution outside a brainstem
    class BasicAgent:  # type: ignore
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


class {cls}TombstoneAgent(BasicAgent):
    def __init__(self):
        super().__init__("{slug}", __manifest__)

    def perform(self, **kwargs) -> str:
        return "RETIRED: {name}. " + ("Current version: {upstream}" if "{upstream}" else "No successor published.")


if __name__ == "__main__":
    print({cls}TombstoneAgent().perform())
'''


def is_tombstone(source: str) -> bool:
    head = source[:4000]
    return f"\n{MARKER} = " in head or head.startswith(f"{MARKER} = ")


# ── keep every retired address alive (Article XXIII.3) ─────────────────────────
# The notary records a removal in state/agent_lifecycle.json. The main build then calls
# backfill(), which puts a stub at any retired address that has no file. Nobody places a stub by hand.
SITE = "https://kody-w.github.io/RAR/"
SUCCESSORS = {  # retired agent -> the agent that replaced it (only where one exists)
    "@borg/hacker_news_agent": "@rapp/hacker_news_agent",
    "@howardh/borg_agent": "@borg/borg_agent",
}


def retired_records(root):
    import json, pathlib
    root = pathlib.Path(root)
    f = root / "state" / "agent_lifecycle.json"
    if not f.exists():
        return []
    agents = json.loads(f.read_text(encoding="utf-8")).get("agents", {})
    return [(n, r) for n, r in sorted(agents.items())
            if r.get("status") in ("deleted", "retired") and str(r.get("canonical_path", "")).startswith("agents/")]


def stub_for(root, name, record):
    import pathlib
    root = pathlib.Path(root)
    path = record["canonical_path"]
    ext = ".py.card" if path.endswith(".py.card") else ".py"
    when = str(record.get("updated_at", ""))[:10]
    successor = SUCCESSORS.get(name, "")
    reason = f"Removed on {when}" + (f" as a duplicate of {successor}." if successor else ".")
    kept = f"versions/{name}/{str(record.get('sha256', ''))[:12]}{ext}"
    if (root / kept).exists():
        reason += f"\nThe file as it was (version {record.get('version', '')}) is kept byte for byte at {SITE}{kept}"
    upstream = ""
    if successor:
        for e in (".py", ".py.card"):
            if (root / "agents" / (successor + e)).exists():
                upstream = f"{SITE}agents/{successor}{e}"
                break
    return render_stub(name, reason, upstream, str(record.get("version", "")))


def backfill(root, write=True):
    """Put a stub at every retired address that has no file. Returns the paths written (or missing)."""
    import pathlib
    root = pathlib.Path(root)
    done = []
    for name, record in retired_records(root):
        target = root / record["canonical_path"]
        if target.exists():
            continue
        if write:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(stub_for(root, name, record), encoding="utf-8")
        done.append(record["canonical_path"])
    return done


def stub_paths(root):
    """Every retired address that currently holds a stub (what the build commits)."""
    import pathlib
    root = pathlib.Path(root)
    return [r["canonical_path"] for _, r in retired_records(root)
            if (root / r["canonical_path"]).exists()
            and is_tombstone((root / r["canonical_path"]).read_text(encoding="utf-8", errors="replace"))]


if __name__ == "__main__":
    import argparse, pathlib
    ap = argparse.ArgumentParser(description="Keep every retired agent address alive with a stub.")
    ap.add_argument("--backfill", action="store_true", help="write a stub at each retired address with no file")
    ap.add_argument("--check", action="store_true", help="exit 1 if a retired address has no file")
    ap.add_argument("--list", action="store_true", help="print the retired addresses that hold a stub")
    ap.add_argument("--root", default=str(pathlib.Path(__file__).resolve().parent.parent))
    a = ap.parse_args()
    if a.backfill:
        for p in backfill(a.root):
            print(p)
    elif a.check:
        missing = backfill(a.root, write=False)
        for p in missing:
            print(f"MISSING {p}")
        raise SystemExit(1 if missing else 0)
    elif a.list:
        for p in stub_paths(a.root):
            print(p)

