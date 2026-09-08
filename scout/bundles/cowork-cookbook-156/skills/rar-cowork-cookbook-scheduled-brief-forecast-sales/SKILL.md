---
name: "rar-cowork-cookbook-scheduled-brief-forecast-sales"
description: "Builds a forecast sales morning brief from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions; drafts an email to the owner (saved to d"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_sales", "rar_sha256": "5c4b9965a35562526216308283bd2f66895ed1bfb9ad8aab538d8f8671fb81e4", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
