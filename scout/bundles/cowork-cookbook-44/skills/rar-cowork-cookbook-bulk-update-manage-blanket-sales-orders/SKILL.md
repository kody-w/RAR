---
name: "rar-cowork-cookbook-bulk-update-manage-blanket-sales-orders"
description: "Applies a bulk field update across manage blanket sales orders records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_manage_blanket_sales_orders", "rar_sha256": "5b806b91562910546dba6bc21b183e5114933c1e38e3d91731a88b4ca98b5bd0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_manage_blanket_sales_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-manage-blanket-sales-orders:798168804cbd278b5506aa2fb07c6e697a14b3d2f9678ad40328ddba32c48b1e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_manage_blanket_sales_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_manage_blanket_sales_orders_agent.py` is
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
