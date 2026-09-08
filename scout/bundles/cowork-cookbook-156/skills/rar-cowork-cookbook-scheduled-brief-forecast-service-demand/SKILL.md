---
name: "rar-cowork-cookbook-scheduled-brief-forecast-service-demand"
description: "Builds a morning brief on forecast service demand from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_forecast_service_demand", "rar_sha256": "1d7534ba2ef9e0ee8924fac119fd87975df1cd7285b55b437b4443c168c68876", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_forecast_service_demand`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_forecast_service_demand_agent.py` and in the RCI capsule.

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

Forecast service demand Scheduled Email Brief — Builds a morning brief on forecast service demand from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-service-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_forecast_service_demand_agent.py` and embedded as the fenced Python below (sha256 1d7534ba2ef9e0ee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_forecast_service_demand_agent.py` first:

```bash
python3 scheduled_brief_forecast_service_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_forecast_service_demand_agent.py   # or on stdin
python3 scheduled_brief_forecast_service_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast service demand Scheduled Email Brief — Builds a morning brief on forecast service demand from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-forecast-service-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_forecast_service_demand',
    "version": '3.0.3',
    "display_name": 'Forecast service demand Scheduled Email Brief',
    "description": 'Builds a morning brief on forecast service demand from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to',
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
        "upstream_slug": 'scheduled-brief-forecast-service-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-forecast-service-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6b8d02300d471a8d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/forecast-service-demand'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-forecast-service-demand', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where forecast service demand stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on forecast service demand for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads forecast service demand, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on forecast service demand from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves a draft email to', 'example_request': 'Give me the forecast service demand morning brief for USMF and draft it to the owner.', 'inputs': [{'description': 'D365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a daily or weekly forecast service demand brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefForecastServiceDemand(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefForecastServiceDemand'
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
    print(ScheduledBriefForecastServiceDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
