---
name: "rar-cowork-cookbook-scheduled-brief-manage-blanket-sales-orders"
description: "Schedulable morning-brief email summarizing manage blanket sales orders for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_blanket_sales_orders", "rar_sha256": "6f00dc2a36c46148edd63352f4e7f406cfa70accd28d7c31fab23adf3ea21bbf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_manage_blanket_sales_orders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-manage-blanket-sales-orders:49ae04cd315a14367e2a0c20f65c292af56db6db9c7c9b4af7f82b13f78dd343", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_manage_blanket_sales_orders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_manage_blanket_sales_orders_agent.py` is
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

Manage blanket sales orders Scheduled Email Brief — Schedulable morning-brief email summarizing manage blanket sales orders for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-blanket-sales-orders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_blanket_sales_orders_agent.py` and embedded as the fenced Python below (sha256 6f00dc2a36c46148…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_blanket_sales_orders_agent.py` first:

```bash
python3 scheduled_brief_manage_blanket_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_blanket_sales_orders_agent.py   # or on stdin
python3 scheduled_brief_manage_blanket_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage blanket sales orders Scheduled Email Brief — Schedulable morning-brief email summarizing manage blanket sales orders for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-blanket-sales-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_blanket_sales_orders',
    "version": '2.0.0',
    "display_name": 'Manage blanket sales orders Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage blanket sales orders for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-blanket-sales-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-blanket-sales-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a5e52941fc1b8621',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-blanket-sales-orders'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-manage-blanket-sales-orders', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefManageBlanketSalesOrders(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageBlanketSalesOrders'
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
    print(ScheduledBriefManageBlanketSalesOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
