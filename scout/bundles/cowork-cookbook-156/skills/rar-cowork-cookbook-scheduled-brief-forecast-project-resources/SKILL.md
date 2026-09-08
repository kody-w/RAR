---
name: "rar-cowork-cookbook-scheduled-brief-forecast-project-resources"
description: "Builds a morning brief on forecast project resources from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the ow"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_project_resources", "rar_sha256": "c4a3ddcd4512d26f9991da4993a0af0c377a4e1b5959a8985a71df3abdceea13", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_forecast_project_resources`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_forecast_project_resources_agent.py` and in the RCI capsule.

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

Forecast project resources Scheduled Email Brief — Builds a morning brief on forecast project resources from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the ow

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-project-resources
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
      "description": "Dynamics 365 F&SCM legal entity to query; defaults to USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_project_resources_agent.py` and embedded as the fenced Python below (sha256 c4a3ddcd4512d26f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_project_resources_agent.py` first:

```bash
python3 scheduled_brief_forecast_project_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_forecast_project_resources_agent.py   # or on stdin
python3 scheduled_brief_forecast_project_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast project resources Scheduled Email Brief — Builds a morning brief on forecast project resources from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the ow

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-project-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_forecast_project_resources',
    "version": '3.0.3',
    "display_name": 'Forecast project resources Scheduled Email Brief',
    "description": 'Builds a morning brief on forecast project resources from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the ow',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-forecast-project-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-forecast-project-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '17237b5c32dc047d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/plan-projects/forecast-project-resources'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/scheduled-brief-forecast-project-resources', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where forecast project resources stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on forecast project resources for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast project resources, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on forecast project resources from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the ow', 'example_request': 'Give me the 7am forecast project resources brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly forecast-project-resources brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefForecastProjectResources(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefForecastProjectResources'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the scheduled task, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefForecastProjectResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
