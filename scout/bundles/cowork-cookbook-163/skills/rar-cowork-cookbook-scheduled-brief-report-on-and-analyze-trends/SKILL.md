---
name: "rar-cowork-cookbook-scheduled-brief-report-on-and-analyze-trends"
description: "Builds a morning brief on trends from Dynamics 365 ERP data for a given legal entity and owner \u2014 top 5 items by impact, anomalies vs the 7-day rolling average, and next actions \u2014 then saves an email draft (unsent) plus a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_report_on_and_analyze_trends", "rar_sha256": "998274b0f42b7e32e719d9c123be2eff24b3ce45980903ec6af52ad086b6725b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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
