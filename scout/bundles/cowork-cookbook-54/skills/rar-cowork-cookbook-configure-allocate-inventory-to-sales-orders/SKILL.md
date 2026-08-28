---
name: "rar-cowork-cookbook-configure-allocate-inventory-to-sales-orders"
description: "Applies a bulk configuration change to allocate inventory to sales orders from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_allocate_inventory_to_sales_orders", "rar_sha256": "9e581c7977ef53e383a398a6299c78735fb49634a188a19e3fa692fb5601c77d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_allocate_inventory_to_sales_orders_agent.py` and embedded as the fenced Python below (sha256 9e581c7977ef53e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_allocate_inventory_to_sales_orders_agent.py` first:

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
    "version": '2.0.0',
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
