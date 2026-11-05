# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/rapp_leviathan_factory_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rapp_leviathan_factory_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/rapp_leviathan_factory/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""Retired compatibility adapter for the pre-protocol Leviathan factory.

The former implementation was intentionally removed. The clean-room public
protocol now lives at @kody-w/full_rapp_leviathan.
"""

from __future__ import annotations

import json

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            self.name = name
            self.metadata = metadata


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/rapp_leviathan_factory",
    "version": "0.3.0",
    "display_name": "RappLeviathanFactory",
    "description": (
        "Retired compatibility adapter. Use @kody-w/full_rapp_leviathan "
        "for the clean-room Full RAPP Leviathan protocol."
    ),
    "author": "kody-w",
    "industry": "meta",
    "tags": ["retired", "compatibility", "leviathan"],
    "category": "core",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}


class RappLeviathanFactoryAgent(BasicAgent):
    def __init__(self):
        self.name = "RappLeviathanFactory"
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["retired"],
                    },
                    "action": {
                        "type": "string",
                        "description": "Ignored legacy action.",
                    },
                },
                "required": [],
                "additionalProperties": True,
            },
        }
        super().__init__(self.name, self.metadata)

    def perform(self, operation="retired", action="", **kwargs):
        return json.dumps({
            "status": "retired",
            "package": "@kody-w/rapp_leviathan_factory",
            "replacement": "@kody-w/full_rapp_leviathan",
            "message": (
                "This package no longer implements Leviathan generation. "
                "Install the clean-room Full RAPP Leviathan protocol package."
            ),
        }, indent=2)


if __name__ == "__main__":
    print(RappLeviathanFactoryAgent().perform())
