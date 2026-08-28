---
name: "rar-cowork-cookbook-demo-data-return-goods-to-vendor"
description: "Generates and creates realistic demo records for return goods to vendor in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_return_goods_to_vendor", "rar_sha256": "06be59a23b52e6cc334281ddcbc72af318329f98de18f0c08b14f166186811b9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_return_goods_to_vendor`. The original RAPP
agent is preserved byte-for-byte in `demo_data_return_goods_to_vendor_agent.py` and in the RCI capsule.

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

Return goods to vendor Demo Data Generator — Generates and creates realistic demo records for return goods to vendor in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_return_goods_to_vendor_agent.py` and embedded as the fenced Python below (sha256 06be59a23b52e6cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_return_goods_to_vendor_agent.py` first:

```bash
python3 demo_data_return_goods_to_vendor_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_return_goods_to_vendor_agent.py   # or on stdin
python3 demo_data_return_goods_to_vendor_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Return goods to vendor Demo Data Generator — Generates and creates realistic demo records for return goods to vendor in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_return_goods_to_vendor',
    "version": '2.0.1',
    "display_name": 'Return goods to vendor Demo Data Generator',
    "description": 'Generates and creates realistic demo records for return goods to vendor in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'demo-data-return-goods-to-vendor',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-return-goods-to-vendor',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3bdd80779c8ef8c7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/process-outbound-goods/return-goods-to-vendor'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-return-goods-to-vendor', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataReturnGoodsToVendor(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataReturnGoodsToVendor'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(DemoDataReturnGoodsToVendor().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
