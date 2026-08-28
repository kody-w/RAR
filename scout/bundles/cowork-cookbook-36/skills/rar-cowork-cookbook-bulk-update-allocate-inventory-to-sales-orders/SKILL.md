---
name: "rar-cowork-cookbook-bulk-update-allocate-inventory-to-sales-orders"
description: "Applies a bulk field update across allocate inventory to sales orders records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_allocate_inventory_to_sales_orders", "rar_sha256": "b001845da98c22d8b014897017333467eee270f2491defeb937108fb2ba6fd32", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_allocate_inventory_to_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_allocate_inventory_to_sales_orders_agent.py` and in the RCI capsule.

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

Allocate inventory to sales orders Bulk Field Update — Applies a bulk field update across allocate inventory to sales orders records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-allocate-inventory-to-sales-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_allocate_inventory_to_sales_orders_agent.py` and embedded as the fenced Python below (sha256 b001845da98c22d8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_allocate_inventory_to_sales_orders_agent.py` first:

```bash
python3 bulk_update_allocate_inventory_to_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_allocate_inventory_to_sales_orders_agent.py   # or on stdin
python3 bulk_update_allocate_inventory_to_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate inventory to sales orders Bulk Field Update — Applies a bulk field update across allocate inventory to sales orders records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-allocate-inventory-to-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_allocate_inventory_to_sales_orders',
    "version": '2.0.1',
    "display_name": 'Allocate inventory to sales orders Bulk Field Update',
    "description": 'Applies a bulk field update across allocate inventory to sales orders records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-allocate-inventory-to-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-allocate-inventory-to-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '743376988b52ca53',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/allocate-inventory-to-sales-orders'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-allocate-inventory-to-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateAllocateInventoryToSalesOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAllocateInventoryToSalesOrders'
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
    print(BulkUpdateAllocateInventoryToSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
