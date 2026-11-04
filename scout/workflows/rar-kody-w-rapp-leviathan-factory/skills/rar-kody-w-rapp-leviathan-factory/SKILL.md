---
name: "rar-kody-w-rapp-leviathan-factory"
description: "Retired compatibility adapter. Use @kody-w/full_rapp_leviathan for the clean-room Full RAPP Leviathan protocol."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_leviathan_factory", "rar_sha256": "ec4a05f14e2149e80674ca6270942c3650539f20ea584de7cd3055c247e8c194", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "0.3.0", "author": "kody-w", "tags": ["retired", "compatibility", "leviathan"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_leviathan_factory_agent.py` and embedded as the fenced Python below (sha256 ec4a05f14e2149e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_leviathan_factory_agent.py` first:

```bash
python3 rapp_leviathan_factory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_leviathan_factory_agent.py   # or on stdin
python3 rapp_leviathan_factory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
