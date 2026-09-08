---
name: "rar-cowork-cookbook-scheduled-brief-plan-budgets"
description: "Builds a morning brief on plan budgets from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-re"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_plan_budgets", "rar_sha256": "16f029116eb5b6aba86f2e9114dc4fc1a9540919e31be4144b72f79f7e98545e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_plan_budgets`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_plan_budgets_agent.py` and in the RCI capsule.

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

Plan budgets Scheduled Email Brief — Builds a morning brief on plan budgets from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-re

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-budgets
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
      "description": "Dynamics 365 legal entity to query; defaults to USMF.",
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
      "description": "When to run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_plan_budgets_agent.py` and embedded as the fenced Python below (sha256 16f029116eb5b6ab…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_plan_budgets_agent.py` first:

```bash
python3 scheduled_brief_plan_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_plan_budgets_agent.py   # or on stdin
python3 scheduled_brief_plan_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan budgets Scheduled Email Brief — Builds a morning brief on plan budgets from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-re

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-plan-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_plan_budgets',
    "version": '3.0.3',
    "display_name": 'Plan budgets Scheduled Email Brief',
    "description": 'Builds a morning brief on plan budgets from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-re',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-plan-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-plan-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0e46c6cf1cf197b1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/plan-budgets'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/scheduled-brief-plan-budgets', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When to run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where plan budgets stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on plan budgets for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-05-25', 'what_it_does': 'Reads plan budgets, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on plan budgets from Dynamics 365 ERP (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner plus a Teams-re', 'example_request': 'Give me the plan budgets morning brief for USMF and draft it to the owner, weekdays at 7am.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When to run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when someone wants a recurring daily or weekly plan-budget brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefPlanBudgets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPlanBudgets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When to run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefPlanBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
