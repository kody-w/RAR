---
name: "rar-cowork-cookbook-scheduled-brief-forecast-sales"
description: "Builds a forecast sales morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the owner (saved to d"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_sales", "rar_sha256": "5c4b9965a35562526216308283bd2f66895ed1bfb9ad8aab538d8f8671fb81e4", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_forecast_sales`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_forecast_sales_agent.py` and in the RCI capsule.

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

Forecast sales Scheduled Email Brief — Builds a forecast sales morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the owner (saved to d

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-sales
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
      "description": "D365 F&SCM legal entity to query; defaults to USMF.",
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
      "description": "When to run the brief, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_sales_agent.py` and embedded as the fenced Python below (sha256 5c4b9965a3556252…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_sales_agent.py` first:

```bash
python3 scheduled_brief_forecast_sales_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_forecast_sales_agent.py   # or on stdin
python3 scheduled_brief_forecast_sales_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast sales Scheduled Email Brief — Builds a forecast sales morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the owner (saved to d

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-sales
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_forecast_sales',
    "version": '3.0.3',
    "display_name": 'Forecast sales Scheduled Email Brief',
    "description": 'Builds a forecast sales morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the owner (saved to d',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-forecast-sales',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-forecast-sales',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9b07b4fc7df0fc3a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-sales-and-operations-planning/forecast-sales'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-forecast-sales', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where forecast sales stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on forecast sales for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast sales, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a forecast sales morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the owner (saved to d', 'example_request': 'Give me the forecast sales morning brief for USMF and draft the email to the owner.', 'inputs': [{'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly forecast sales morning brief for the responsible owner, as an email draft and Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefForecastSales(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefForecastSales'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefForecastSales().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
