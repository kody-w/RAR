---
name: "rar-kody-w-hello-world"
description: "Says hello to the user."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/hello_world_agent", "rar_sha256": "d2695f70a412909546a49586487a471e6bca9c2d215d0367d440a80473b75bd1", "source_kind": "rar-agent", "source_commit": "026f18b4093e3ec07c2f359dd9618438e020a0be", "version": "1.0.3", "author": "kody-w", "tags": ["tutorial", "hello-world", "starter"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/hello_world_agent`. The original RAPP
agent is preserved byte-for-byte in `hello_world_agent.py` and in the RCI capsule.

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
