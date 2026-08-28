---
name: "rar-cowork-cookbook-demo-data-track-customer-managed-inventory-and-consigned-inventory"
description: "Generates and creates realistic demo records for track customer managed inventory and consigned inventory in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_track_customer_managed_inventory_and_consigned_inventory", "rar_sha256": "1c896ca29f9df5ef4f9475a09a3ba7aca07d1ca493b71565a6556c8b285766c2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py` and embedded as the fenced Python below (sha256 1c896ca29f9df5ef…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_track_customer_managed_inventory_and_consigned_inventory_agent.py` first:

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
    "version": '2.0.1',
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
