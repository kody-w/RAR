---
name: "rar-kody-w-rapp-x-notary-canary"
description: "Validates the Issues-backed RAR notarization lifecycle."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_x_notary_canary_agent", "rar_sha256": "c006e2637b31eb84db60a7832d730b37cd004d497b7d7ae589f2464706f03918", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.2.0", "author": "Kody W", "tags": ["canary", "notary", "rapp_x"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rapp_x_notary_canary_agent`. The original RAPP
agent is preserved byte-for-byte in `rapp_x_notary_canary_agent.py` and in the RCI capsule.

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

RAPP + X notarization canary for end-to-end registry validation.

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_x_notary_canary_agent.py` and embedded as the fenced Python below (sha256 c006e2637b31eb84…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_x_notary_canary_agent.py` first:

```bash
python3 rapp_x_notary_canary_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_x_notary_canary_agent.py   # or on stdin
python3 rapp_x_notary_canary_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/rapp_x_notary_canary_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rapp_x_notary_canary_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/rapp_x_notary_canary_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""RAPP + X notarization canary for end-to-end registry validation."""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/rapp_x_notary_canary_agent",
    "version": "1.2.0",
    "display_name": "RAPP X Notary Canary",
    "description": "Validates the Issues-backed RAR notarization lifecycle.",
    "author": "Kody W",
    "tags": ["canary", "notary", "rapp_x"],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


class RappXNotaryCanaryAgent(BasicAgent):
    def __init__(self):
        self.name = "RappXNotaryCanaryAgent"
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {"type": "object", "properties": {}},
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs) -> str:
        return f"RAPP + X canary v1.2 restored: {kwargs.get('message', 'ok')}"


if __name__ == "__main__":
    print(RappXNotaryCanaryAgent().perform())
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
