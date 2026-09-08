---
name: "rar-cowork-cookbook-scheduled-brief-manage-blanket-sales-orders"
description: "Builds a morning brief on blanket sales orders from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner and a Teams"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_blanket_sales_orders", "rar_sha256": "b48da0277a22816d389d2c54ec48f2b11f164836e94ce8a76abc8d6323fef20d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

Manage blanket sales orders Scheduled Email Brief — Builds a morning brief on blanket sales orders from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner and a Teams

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query; defaults to USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "owner": {
      "description": "Responsible owner who receives the drafted email brief.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run, e.g. weekday mornings at 7am, daily or weekly.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_blanket_sales_orders_agent.py` and embedded as the fenced Python below (sha256 b48da0277a22816d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_blanket_sales_orders_agent.py` first:

```bash
python3 scheduled_brief_manage_blanket_sales_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_blanket_sales_orders_agent.py   # or on stdin
python3 scheduled_brief_manage_blanket_sales_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage blanket sales orders Scheduled Email Brief — Builds a morning brief on blanket sales orders from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner and a Teams

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "version": '3.0.3',
    "display_name": 'Manage blanket sales orders Scheduled Email Brief',
    "description": 'Builds a morning brief on blanket sales orders from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner and a Teams',
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7e623ad7c694f318',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am, daily or weekly.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where manage blanket sales orders stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on manage blanket sales orders for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage blanket sales orders, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on blanket sales orders from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then drafts an email to the owner and a Teams', 'example_request': 'Give me the 7am blanket sales order brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly blanket sales order brief for the responsible owner, as an email draft plus a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefManageBlanketSalesOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageBlanketSalesOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am, daily or weekly.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
