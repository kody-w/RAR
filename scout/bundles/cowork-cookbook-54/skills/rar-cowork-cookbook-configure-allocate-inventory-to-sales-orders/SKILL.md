---
name: "rar-cowork-cookbook-configure-allocate-inventory-to-sales-orders"
description: "Applies a bulk configuration change to allocate inventory to sales orders from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_allocate_inventory_to_sales_orders", "rar_sha256": "9e581c7977ef53e383a398a6299c78735fb49634a188a19e3fa692fb5601c77d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_allocate_inventory_to_sales_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-allocate-inventory-to-sales-orders:49f547370c52592cc6a69dca5416ed3a6699b84a5836b55767daae118e0c3734", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_allocate_inventory_to_sales_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_allocate_inventory_to_sales_orders_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
