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
