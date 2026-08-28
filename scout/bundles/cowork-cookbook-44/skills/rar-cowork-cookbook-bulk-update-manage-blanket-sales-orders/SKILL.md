---
name: "rar-cowork-cookbook-bulk-update-manage-blanket-sales-orders"
description: "Applies a bulk field update across manage blanket sales orders records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_blanket_sales_orders", "rar_sha256": "5b806b91562910546dba6bc21b183e5114933c1e38e3d91731a88b4ca98b5bd0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_manage_blanket_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_manage_blanket_sales_orders_agent.py` and in the RCI capsule.

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

Manage blanket sales orders Bulk Field Update — Applies a bulk field update across manage blanket sales orders records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-blanket-sales-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_blanket_sales_orders_agent.py` and embedded as the fenced Python below (sha256 5b806b9156291054…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_blanket_sales_orders_agent.py` first:

```bash
python3 bulk_update_manage_blanket_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_manage_blanket_sales_orders_agent.py   # or on stdin
python3 bulk_update_manage_blanket_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage blanket sales orders Bulk Field Update — Applies a bulk field update across manage blanket sales orders records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-manage-blanket-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_manage_blanket_sales_orders',
    "version": '2.0.0',
    "display_name": 'Manage blanket sales orders Bulk Field Update',
    "description": 'Applies a bulk field update across manage blanket sales orders records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-manage-blanket-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-manage-blanket-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ed7a1a33434ccdc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-blanket-sales-orders'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/bulk-update-manage-blanket-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateManageBlanketSalesOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateManageBlanketSalesOrders'
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
    print(BulkUpdateManageBlanketSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
