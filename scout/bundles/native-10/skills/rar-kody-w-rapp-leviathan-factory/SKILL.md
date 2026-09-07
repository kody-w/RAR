---
name: "rar-kody-w-rapp-leviathan-factory"
description: "Retired compatibility adapter. Use @kody-w/full_rapp_leviathan for the clean-room Full RAPP Leviathan protocol."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_leviathan_factory", "rar_sha256": "e381f1fe6add6c47eec0d59307110f136103f8d349c611f7be0bff02edb0c6d0", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "version": "0.3.0", "author": "kody-w", "tags": ["retired", "compatibility", "leviathan"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rapp_leviathan_factory`. The original RAPP
agent is preserved byte-for-byte in `rapp_leviathan_factory_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

Retired compatibility adapter for the pre-protocol Leviathan factory.

The former implementation was intentionally removed. The clean-room public
protocol now lives at @kody-w/full_rapp_leviathan.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "additionalProperties": true,
  "properties": {
    "action": {
      "description": "Ignored legacy action.",
      "type": "string"
    },
    "operation": {
      "enum": [
        "retired"
      ],
      "type": "string"
    }
  },
  "required": [],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_leviathan_factory_agent.py` and embedded as the fenced Python below (sha256 e381f1fe6add6c47…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_leviathan_factory_agent.py` first:

```bash
python3 rapp_leviathan_factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_leviathan_factory_agent.py   # or on stdin
python3 rapp_leviathan_factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
