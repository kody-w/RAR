---
name: "rar-cowork-cookbook-scheduled-brief-forecast-project-resources"
description: "Builds a morning brief on forecast project resources from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the ow"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_project_resources", "rar_sha256": "c4a3ddcd4512d26f9991da4993a0af0c377a4e1b5959a8985a71df3abdceea13", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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
