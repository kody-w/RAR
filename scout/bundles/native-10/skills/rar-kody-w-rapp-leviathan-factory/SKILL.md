---
name: "rar-kody-w-rapp-leviathan-factory"
description: "Retired compatibility adapter. Use @kody-w/full_rapp_leviathan for the clean-room Full RAPP Leviathan protocol."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_leviathan_factory", "rar_sha256": "ec4a05f14e2149e80674ca6270942c3650539f20ea584de7cd3055c247e8c194", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "0.3.0", "author": "kody-w", "tags": ["retired", "compatibility", "leviathan"]}
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
