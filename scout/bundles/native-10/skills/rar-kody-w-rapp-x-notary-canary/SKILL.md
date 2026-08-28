---
name: "rar-kody-w-rapp-x-notary-canary"
description: "Validates the Issues-backed RAR notarization lifecycle."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rapp_x_notary_canary_agent", "rar_sha256": "5d34d87380925aa0f60c14e0066c8aa5e59ecd884bf19034619ebea58ad27149", "source_kind": "rar-agent", "source_commit": "6b476f64439c79606c401a412ac5f468d15459e9", "version": "1.2.0", "author": "Kody W", "tags": ["canary", "notary", "rapp_x"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rapp_x_notary_canary_agent.py` and embedded as the fenced Python below (sha256 5d34d87380925aa0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rapp_x_notary_canary_agent.py` first:

```bash
python3 rapp_x_notary_canary_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rapp_x_notary_canary_agent.py   # or on stdin
python3 rapp_x_notary_canary_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
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
