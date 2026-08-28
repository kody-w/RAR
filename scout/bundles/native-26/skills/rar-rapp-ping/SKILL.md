---
name: "rar-rapp-ping"
description: "Returns 'pong'. Smoke test for the agent dispatch path."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/ping_agent", "rar_sha256": "4761dcecf8af3893153407860dc6786ac8cd7d3654966bb57923143db885f0af", "source_kind": "rar-agent", "source_commit": "ce4d2aa63a3ebb409c34534643e32ab7cccd8aa2", "version": "1.0.1", "author": "RAPP", "tags": ["diagnostic", "smoke-test", "minimal"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@rapp/ping_agent`. The original RAPP
agent is preserved byte-for-byte in `ping_agent.py` and in the RCI capsule.

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

ping_agent — Returns 'pong'. Smoke test for agent dispatch.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ping_agent.py` and embedded as the fenced Python below (sha256 4761dcecf8af3893…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ping_agent.py` first:

```bash
python3 ping_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ping_agent.py   # or on stdin
python3 ping_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""ping_agent — Returns 'pong'. Smoke test for agent dispatch."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@rapp/ping_agent",
    "version": "1.0.1",
    "display_name": "Ping",
    "description": "Returns 'pong'. The smallest possible agent — useful as a smoke test that the brainstem can discover, load, and dispatch a tool call end-to-end.",
    "author": "RAPP",
    "tags": ["diagnostic", "smoke-test", "minimal"],
    "category": "devtools",
    "quality_tier": "official",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    try:
        from basic_agent import BasicAgent
    except ImportError:
        from openrappter.agents.basic_agent import BasicAgent


class PingAgent(BasicAgent):
    def __init__(self):
        self.name = "Ping"
        self.metadata = {
            "name": self.name,
            "description": "Returns 'pong'. Smoke test for the agent dispatch path.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        }
        super().__init__(self.name, self.metadata)

    def perform(self, **kwargs):
        return "pong"
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
