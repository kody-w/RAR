---
name: "rar-cowork-cookbook-bulk-update-allocate-inventory-to-sales-orders"
description: "Applies a bulk field update across allocate inventory to sales orders records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_allocate_inventory_to_sales_orders", "rar_sha256": "9d9f4dc7be1b06462beb3e38a05de0df88a45eb1f15a73a05f69ea237b254aee", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_allocate_inventory_to_sales_orders_agent.py` and embedded as the fenced Python below (sha256 9d9f4dc7be1b0646…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_allocate_inventory_to_sales_orders_agent.py` first:

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
    "version": '2.0.0',
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
