---
name: "rar-cowork-cookbook-scheduled-brief-report-on-and-analyze-trends"
description: "Builds a morning brief on trends from Dynamics 365 ERP data for a given legal entity and owner \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and next actions \u2014 then saves an email draft (unsent) plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_report_on_and_analyze_trends", "rar_sha256": "998274b0f42b7e32e719d9c123be2eff24b3ce45980903ec6af52ad086b6725b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_report_on_and_analyze_trends`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_report_on_and_analyze_trends_agent.py` and in the RCI capsule.

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

Report on and analyze trends Scheduled Email Brief — Builds a morning brief on trends from Dynamics 365 ERP data for a given legal entity and owner — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft (unsent) plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-report-on-and-analyze-trends
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Responsible owner who receives the drafted brief email.",
      "type": "string"
    },
    "schedule": {
      "description": "When to run it, e.g. weekday mornings at 7am.",
      "type": "string"
    },
    "topic": {
      "description": "Subject area of the trend analysis to report on.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_report_on_and_analyze_trends_agent.py` and embedded as the fenced Python below (sha256 998274b0f42b7e32…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_report_on_and_analyze_trends_agent.py` first:

```bash
python3 scheduled_brief_report_on_and_analyze_trends_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_report_on_and_analyze_trends_agent.py   # or on stdin
python3 scheduled_brief_report_on_and_analyze_trends_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on and analyze trends Scheduled Email Brief — Builds a morning brief on trends from Dynamics 365 ERP data for a given legal entity and owner — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft (unsent) plus a

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-report-on-and-analyze-trends
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_report_on_and_analyze_trends',
    "version": '3.0.3',
    "display_name": 'Report on and analyze trends Scheduled Email Brief',
    "description": 'Builds a morning brief on trends from Dynamics 365 ERP data for a given legal entity and owner — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft (unsent) plus a',
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
        "upstream_slug": 'scheduled-brief-report-on-and-analyze-trends',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-report-on-and-analyze-trends',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9d002862cb42ac6a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/report-on-and-analyze-trends'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-report-on-and-analyze-trends', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted brief email.', 'schedule': 'When to run it, e.g. weekday mornings at 7am.', 'topic': 'Subject area of the trend analysis to report on.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where report on and analyze trends stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on report on and analyze trends for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads report on and analyze trends, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on trends from Dynamics 365 ERP data for a given legal entity and owner — top 5 items by impact, anomalies vs the 7-day rolling average, and next actions — then saves an email draft (unsent) plus a', 'example_request': 'Draft my 7am weekday trend brief from D365 USMF for the ops owner, with anomalies and next actions.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted brief email.', 'name': 'owner'}, {'description': 'Subject area of the trend analysis to report on.', 'name': 'topic'}, {'description': 'When to run it, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a user wants a daily or weekly D365 ERP trend brief drafted as an email to the responsible owner plus a Teams-ready summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefReportOnAndAnalyzeTrends(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReportOnAndAnalyzeTrends'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted brief email.', 'type': 'string'}, 'schedule': {'description': 'When to run it, e.g. weekday mornings at 7am.', 'type': 'string'}, 'topic': {'description': 'Subject area of the trend analysis to report on.', 'type': 'string'}},
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
    print(ScheduledBriefReportOnAndAnalyzeTrends().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
