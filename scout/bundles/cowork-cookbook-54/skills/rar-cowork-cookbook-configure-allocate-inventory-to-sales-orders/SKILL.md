---
name: "rar-cowork-cookbook-configure-allocate-inventory-to-sales-orders"
description: "Applies a bulk configuration change to allocate inventory to sales orders from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_allocate_inventory_to_sales_orders", "rar_sha256": "e189ecb7926f9b96f57d16d896ffa5a6d7acb8a65acf0bc423e420bdbda45a30", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_allocate_inventory_to_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `configure_allocate_inventory_to_sales_orders_agent.py` and in the RCI capsule.

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

Allocate inventory to sales orders Configuration Bulk Setup — Applies a bulk configuration change to allocate inventory to sales orders from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-allocate-inventory-to-sales-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_allocate_inventory_to_sales_orders_agent.py` and embedded as the fenced Python below (sha256 e189ecb7926f9b96…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_allocate_inventory_to_sales_orders_agent.py` first:

```bash
python3 configure_allocate_inventory_to_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_allocate_inventory_to_sales_orders_agent.py   # or on stdin
python3 configure_allocate_inventory_to_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate inventory to sales orders Configuration Bulk Setup — Applies a bulk configuration change to allocate inventory to sales orders from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-allocate-inventory-to-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_allocate_inventory_to_sales_orders',
    "version": '2.0.1',
    "display_name": 'Allocate inventory to sales orders Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to allocate inventory to sales orders from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-allocate-inventory-to-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-allocate-inventory-to-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c92b42e9138b0cb6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/allocate-inventory-to-sales-orders'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-allocate-inventory-to-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAllocateInventoryToSalesOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAllocateInventoryToSalesOrders'
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
    print(ConfigureAllocateInventoryToSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
