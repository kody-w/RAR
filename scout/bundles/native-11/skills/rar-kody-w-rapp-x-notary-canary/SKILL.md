---
name: "rar-kody-w-rapp-x-notary-canary"
description: "Validates the Issues-backed RAR notarization lifecycle."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_x_notary_canary_agent", "rar_sha256": "c006e2637b31eb84db60a7832d730b37cd004d497b7d7ae589f2464706f03918", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "1.2.0", "author": "Kody W", "tags": ["canary", "notary", "rapp_x"]}
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
