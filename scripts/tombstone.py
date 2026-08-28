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
