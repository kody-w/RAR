---
name: "rar-cowork-cookbook-bulk-update-manage-blanket-sales-orders"
description: "Applies a bulk field update across manage blanket sales orders records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_blanket_sales_orders", "rar_sha256": "77aed2e683060e000ffeac35730651dd4d23c3537b4a48af962f0b7dcd7e80f4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_manage_blanket_sales_orders_agent.py` and embedded as the fenced Python below (sha256 77aed2e683060e00…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_manage_blanket_sales_orders_agent.py` first:

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
    "version": '2.0.1',
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
