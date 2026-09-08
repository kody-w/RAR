---
name: "rar-cowork-cookbook-scheduled-brief-finalize-work-orders"
description: "Builds a finalize-work-orders morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus an email saved to drafts."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_finalize_work_orders", "rar_sha256": "2addd3d2fc2939e36a87aaf2e9bf46c3faa091d132655bd69068842bc35d3dad", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_finalize_work_orders`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_finalize_work_orders_agent.py` and in the RCI capsule.

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

Finalize work orders Scheduled Email Brief — Builds a finalize-work-orders morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus an email saved to drafts.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-finalize-work-orders
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
      "description": "Optional cadence for the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_finalize_work_orders_agent.py` and embedded as the fenced Python below (sha256 2addd3d2fc2939e3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_finalize_work_orders_agent.py` first:

```bash
python3 scheduled_brief_finalize_work_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_finalize_work_orders_agent.py   # or on stdin
python3 scheduled_brief_finalize_work_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize work orders Scheduled Email Brief — Builds a finalize-work-orders morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus an email saved to drafts.

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-finalize-work-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_finalize_work_orders',
    "version": '3.0.3',
    "display_name": 'Finalize work orders Scheduled Email Brief',
    "description": 'Builds a finalize-work-orders morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus an email saved to drafts.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-finalize-work-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-finalize-work-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9838790fb0c7d6df',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/finalize-work-orders'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-finalize-work-orders', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where finalize work orders stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on finalize work orders for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads finalize work orders, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a finalize-work-orders morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact, anomalies vs 7-day rolling average, and next actions, plus an email saved to drafts.', 'example_request': 'Give me the finalize work orders morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the responsible owner wants a daily or weekly finalize-work-orders brief with a draft email and a Teams-ready summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefFinalizeWorkOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefFinalizeWorkOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefFinalizeWorkOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
