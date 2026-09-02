---
name: "rar-kody-w-rapp-leviathan-factory"
description: "Retired compatibility adapter. Use @kody-w/full_rapp_leviathan for the clean-room Full RAPP Leviathan protocol."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_leviathan_factory", "rar_sha256": "e381f1fe6add6c47eec0d59307110f136103f8d349c611f7be0bff02edb0c6d0", "source_kind": "rar-agent", "source_commit": "d16979f79339ed06511e0bc50c363f1286d140c7", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "rapp_leviathan_factory_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/rapp-leviathan-factory:4cc795daafd85d336d022195c77fd9da590130de92426f4790c9d7811f1695f5", "kind": "skill"}, "version": "0.3.0", "author": "kody-w", "tags": ["retired", "compatibility", "leviathan"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/rapp_leviathan_factory`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `rapp_leviathan_factory_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
