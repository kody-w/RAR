---
name: "rar-rapp-ping"
description: "Returns 'pong'. Smoke test for the agent dispatch path."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/ping_agent", "rar_sha256": "4761dcecf8af3893153407860dc6786ac8cd7d3654966bb57923143db885f0af", "source_kind": "rar-agent", "source_commit": "ce4d2aa63a3ebb409c34534643e32ab7cccd8aa2", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ping_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@rapp/ping:60a2b0dc6971cb2e241533502dfa0fa4950230132a9e94d7b94c0fad576d6891", "kind": "skill"}, "version": "1.0.1", "author": "RAPP", "tags": ["diagnostic", "smoke-test", "minimal"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@rapp/ping_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ping_agent.py` is
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
