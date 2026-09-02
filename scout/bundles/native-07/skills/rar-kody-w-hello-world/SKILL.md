---
name: "rar-kody-w-hello-world"
description: "Says hello to the user."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/hello_world_agent", "rar_sha256": "d2695f70a412909546a49586487a471e6bca9c2d215d0367d440a80473b75bd1", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "hello_world_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@kody-w/hello-world:13cc8a648bd0a09a4458f52f952b2c9e5d64ed740a9c59625238d7a943ca809a", "kind": "skill"}, "version": "1.0.3", "author": "kody-w", "tags": ["tutorial", "hello-world", "starter"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@kody-w/hello_world_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `hello_world_agent.py` is
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

Hello World Agent — A friendly greeting agent that demonstrates the basics.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "name": {
      "description": "Name to greet",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `hello_world_agent.py` and embedded as the fenced Python below (sha256 d2695f70a4129095…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `hello_world_agent.py` first:

```bash
python3 hello_world_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 hello_world_agent.py   # or on stdin
python3 hello_world_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""Hello World Agent — A friendly greeting agent that demonstrates the basics."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/hello_world_agent",
    "version": "1.0.3",
    "display_name": "Hello World",
    "description": "Greets the user by name with a canned hello message; a starter example touching no external systems.",
    "author": "kody-w",
    "tags": ["tutorial", "hello-world", "starter"],
    "category": "general",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

from agents.basic_agent import BasicAgent


class HelloWorldAgent(BasicAgent):
    def __init__(self):
        self.name = "HelloWorldAgent"
        self.metadata = {
            "name": self.name,
            "description": "Says hello to the user.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Name to greet"}
                },
                "required": []
            }
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs) -> str:
        name = kwargs.get("name", "World")
        return f"Hello, {name}! Welcome to the RAPP Agent ecosystem."
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
