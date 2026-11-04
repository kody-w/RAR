---
name: "rar-rapp-ping"
description: "Returns 'pong'. Smoke test for the agent dispatch path."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/ping_agent", "rar_sha256": "bcd367fbb3174f0128309a6f98df1b461f012dfdea619e4dae9b301c8b607bf9", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.0.1", "author": "RAPP", "tags": ["diagnostic", "smoke-test", "minimal"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ping_agent.py` and embedded as the fenced Python below (sha256 bcd367fbb3174f01…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ping_agent.py` first:

```bash
python3 ping_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ping_agent.py   # or on stdin
python3 ping_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@rapp/ping_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/ping_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@rapp/ping_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
