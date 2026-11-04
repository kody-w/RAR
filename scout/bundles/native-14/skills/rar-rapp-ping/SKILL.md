---
name: "rar-rapp-ping"
description: "Returns 'pong'. Smoke test for the agent dispatch path."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@rapp/ping_agent", "rar_sha256": "bcd367fbb3174f0128309a6f98df1b461f012dfdea619e4dae9b301c8b607bf9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.0.1", "author": "RAPP", "tags": ["diagnostic", "smoke-test", "minimal"]}
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
