---
name: "rar-cowork-cookbook-demo-data-track-customer-managed-inventory-and-consigned-inventory"
description: "Generates and creates realistic demo records for track customer managed inventory and consigned inventory in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_customer_managed_inventory_and_consigned_inventory", "rar_sha256": "98d8b7b128e14a39e7fe75b50b3ec6bf408e1c528b269cf262bbf13271384f1c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_track_customer_managed_inventory_and_consigned_inventory`. The original RAPP
agent is preserved byte-for-byte in `demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py` and in the RCI capsule.

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

Track customer managed inventory and consigned inventory Demo Data Generator — Generates and creates realistic demo records for track customer managed inventory and consigned inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-customer-managed-inventory-and-consigned-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py` and embedded as the fenced Python below (sha256 98d8b7b128e14a39…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py` first:

```bash
python3 demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py   # or on stdin
python3 demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track customer managed inventory and consigned inventory Demo Data Generator — Generates and creates realistic demo records for track customer managed inventory and consigned inventory in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-track-customer-managed-inventory-and-consigned-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_track_customer_managed_inventory_and_consigned_inventory',
    "version": '2.0.0',
    "display_name": 'Track customer managed inventory and consigned inventory Demo Data Generator',
    "description": 'Generates and creates realistic demo records for track customer managed inventory and consigned inventory in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-track-customer-managed-inventory-and-consigned-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-track-customer-managed-inventory-and-consigned-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37c9688d71c299cc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/track-customer-managed-inventory-and-consigned-inventory'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/demo-data-track-customer-managed-inventory-and-consigned-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataTrackCustomerManagedInventoryAndConsignedInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTrackCustomerManagedInventoryAndConsignedInventory'
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
    print(DemoDataTrackCustomerManagedInventoryAndConsignedInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
