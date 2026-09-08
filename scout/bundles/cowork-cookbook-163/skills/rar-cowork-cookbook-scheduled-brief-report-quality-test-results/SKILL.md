---
name: "rar-cowork-cookbook-scheduled-brief-report-quality-test-results"
description: "Builds a morning brief on report quality test results from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draf"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_report_quality_test_results", "rar_sha256": "bb7d33064cd6208a938fcb4874aa5dc409336b4afa1fbfd51ff32005aaaed920", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_report_quality_test_results`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_report_quality_test_results_agent.py` and in the RCI capsule.

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

Report quality test results Scheduled Email Brief — Builds a morning brief on report quality test results from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draf

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-report-quality-test-results
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
      "description": "When to run the brief, e.g. weekday mornings at 7am (daily or weekly).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_report_quality_test_results_agent.py` and embedded as the fenced Python below (sha256 bb7d33064cd6208a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_report_quality_test_results_agent.py` first:

```bash
python3 scheduled_brief_report_quality_test_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_report_quality_test_results_agent.py   # or on stdin
python3 scheduled_brief_report_quality_test_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report quality test results Scheduled Email Brief — Builds a morning brief on report quality test results from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draf

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-report-quality-test-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_report_quality_test_results',
    "version": '3.0.3',
    "display_name": 'Report quality test results Scheduled Email Brief',
    "description": 'Builds a morning brief on report quality test results from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draf',
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
        "upstream_slug": 'scheduled-brief-report-quality-test-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-report-quality-test-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3da882574219c9c4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/report-quality-test-results'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-report-quality-test-results', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run the brief, e.g. weekday mornings at 7am (daily or weekly).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where report quality test results stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on report quality test results for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads report quality test results, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on report quality test results from Dynamics 365 ERP (legal entity USMF): top 5 items by impact today, anomalies vs the 7-day rolling average, and recommended next actions, then saves an email draf', 'example_request': 'Give me the morning brief on report quality test results from USMF and draft the email to the owner.', 'inputs': [{'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run the brief, e.g. weekday mornings at 7am (daily or weekly).', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Use for a recurring (e.g. weekday 7am) report-quality-test-results brief for the responsible owner, with an unsent email draft and a Teams channel post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefReportQualityTestResults(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReportQualityTestResults'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 F&SCM legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run the brief, e.g. weekday mornings at 7am (daily or weekly).', 'type': 'string'}},
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
    print(ScheduledBriefReportQualityTestResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
