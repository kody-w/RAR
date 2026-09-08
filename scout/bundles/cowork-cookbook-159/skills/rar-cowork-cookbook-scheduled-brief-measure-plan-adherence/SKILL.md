---
name: "rar-cowork-cookbook-scheduled-brief-measure-plan-adherence"
description: "Builds a morning brief on measure plan adherence from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draft to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_plan_adherence", "rar_sha256": "6c7e12bb364b8d8bd05dbd04640471a17fe190fb6ba133e425b786c686d719f9", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_measure_plan_adherence`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_measure_plan_adherence_agent.py` and in the RCI capsule.

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

Measure plan adherence Scheduled Email Brief — Builds a morning brief on measure plan adherence from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draft to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-plan-adherence
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
      "description": "Optional cadence for the recurring run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_measure_plan_adherence_agent.py` and embedded as the fenced Python below (sha256 6c7e12bb364b8d8b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_measure_plan_adherence_agent.py` first:

```bash
python3 scheduled_brief_measure_plan_adherence_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_measure_plan_adherence_agent.py   # or on stdin
python3 scheduled_brief_measure_plan_adherence_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure plan adherence Scheduled Email Brief — Builds a morning brief on measure plan adherence from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draft to

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-measure-plan-adherence
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_measure_plan_adherence',
    "version": '3.0.3',
    "display_name": 'Measure plan adherence Scheduled Email Brief',
    "description": 'Builds a morning brief on measure plan adherence from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draft to',
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
        "upstream_slug": 'scheduled-brief-measure-plan-adherence',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-measure-plan-adherence',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dfe494d5c5b97909',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/measure-plan-adherence'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-measure-plan-adherence', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the recurring run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where measure plan adherence stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on measure plan adherence for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads measure plan adherence, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on measure plan adherence from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draft to', 'example_request': 'Draft my daily measure plan adherence brief for USMF and email the owner a draft.', 'inputs': [{'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the recurring run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a responsible owner needs a daily or weekly measure plan adherence brief drafted from D365 ERP data, including a scheduled 7am weekday run.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefMeasurePlanAdherence(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMeasurePlanAdherence'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the recurring run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefMeasurePlanAdherence().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
