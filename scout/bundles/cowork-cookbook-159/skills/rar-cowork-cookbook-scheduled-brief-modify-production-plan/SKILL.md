---
name: "rar-cowork-cookbook-scheduled-brief-modify-production-plan"
description: "Builds a morning brief on modify production plan from Dynamics 365 ERP for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, drafted as an unsent email plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_modify_production_plan", "rar_sha256": "590bb65c5a12aff290828fa1e18afdb1c76ff5b38f653b89e322429c7b2fc36e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_modify_production_plan`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_modify_production_plan_agent.py` and in the RCI capsule.

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

Modify production plan Scheduled Email Brief — Builds a morning brief on modify production plan from Dynamics 365 ERP for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, drafted as an unsent email plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan
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
      "description": "Responsible owner who receives the drafted email.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional cadence for the scheduled task, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_modify_production_plan_agent.py` and embedded as the fenced Python below (sha256 590bb65c5a12aff2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_modify_production_plan_agent.py` first:

```bash
python3 scheduled_brief_modify_production_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_modify_production_plan_agent.py   # or on stdin
python3 scheduled_brief_modify_production_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Modify production plan Scheduled Email Brief — Builds a morning brief on modify production plan from Dynamics 365 ERP for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, drafted as an unsent email plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_modify_production_plan',
    "version": '3.0.3',
    "display_name": 'Modify production plan Scheduled Email Brief',
    "description": 'Builds a morning brief on modify production plan from Dynamics 365 ERP for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, drafted as an unsent email plus a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-modify-production-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-modify-production-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3311ce6c4ee310ca',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/modify-production-plan'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-modify-production-plan', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where modify production plan stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on modify production plan for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads modify production plan, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on modify production plan from Dynamics 365 ERP for legal entity USMF: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, drafted as an unsent email plus a', 'example_request': 'Give me the 7am morning brief on the modify production plan for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the responsible owner wants a daily or weekly (weekday 7am) production-plan brief with an email draft and Teams-ready summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefModifyProductionPlan(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefModifyProductionPlan'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefModifyProductionPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
