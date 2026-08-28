---
name: "rar-cowork-cookbook-scheduled-brief-manage-blanket-sales-orders"
description: "Schedulable morning-brief email summarizing manage blanket sales orders for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_blanket_sales_orders", "rar_sha256": "db681cbe3ff1436198cb37f8f0de35a104fdecb466e0cd2bff3ca39a0381e565", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_blanket_sales_orders_agent.py` and embedded as the fenced Python below (sha256 db681cbe3ff14361…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_blanket_sales_orders_agent.py` first:

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
    "version": '2.0.1',
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
