---
name: "rar-cowork-cookbook-scheduled-brief-manage-blanket-sales-orders"
description: "Schedulable morning-brief email summarizing manage blanket sales orders for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_blanket_sales_orders", "rar_sha256": "6f00dc2a36c46148edd63352f4e7f406cfa70accd28d7c31fab23adf3ea21bbf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_blanket_sales_orders`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_blanket_sales_orders_agent.py` and in the RCI capsule.

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
