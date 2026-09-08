---
name: "rar-cowork-cookbook-scheduled-brief-measure-plan-adherence"
description: "Builds a morning brief on measure plan adherence from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draft to"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_measure_plan_adherence", "rar_sha256": "6c7e12bb364b8d8bd05dbd04640471a17fe190fb6ba133e425b786c686d719f9", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
