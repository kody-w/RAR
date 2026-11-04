---
name: "rar-kody-w-hello-world"
description: "Says hello to the user."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/hello_world_agent", "rar_sha256": "dacc1cacd80777c63efa1e7ea140fca761df3a6f0df5d0bf116748ea30823009", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.3", "author": "kody-w", "tags": ["tutorial", "hello-world", "starter"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `hello_world_agent.py` and embedded as the fenced Python below (sha256 dacc1cacd80777c6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `hello_world_agent.py` first:

```bash
python3 hello_world_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 hello_world_agent.py   # or on stdin
python3 hello_world_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/hello_world_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/hello_world_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/hello_world_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
