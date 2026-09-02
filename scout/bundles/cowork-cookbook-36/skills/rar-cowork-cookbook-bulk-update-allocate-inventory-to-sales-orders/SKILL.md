---
name: "rar-cowork-cookbook-bulk-update-allocate-inventory-to-sales-orders"
description: "Applies a bulk field update across allocate inventory to sales orders records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_allocate_inventory_to_sales_orders", "rar_sha256": "9d9f4dc7be1b06462beb3e38a05de0df88a45eb1f15a73a05f69ea237b254aee", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_allocate_inventory_to_sales_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-allocate-inventory-to-sales-orders:2878836c2b662200fd47b9ee8d97de21aac066b7318008ce638a00421ab72e8f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_allocate_inventory_to_sales_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_allocate_inventory_to_sales_orders_agent.py` is
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
