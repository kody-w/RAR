---
name: "rar-cowork-cookbook-scheduled-brief-monitor-employee-satisfaction"
description: "Builds a morning brief on employee satisfaction from Dynamics 365 ERP data for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft pl"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_employee_satisfaction", "rar_sha256": "d873646ea6cbc1b600074d0b95e10025570ada84ecf5f2980ece76b5b1511e1d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_employee_satisfaction`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_employee_satisfaction_agent.py` and in the RCI capsule.

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

Monitor employee satisfaction Scheduled Email Brief — Builds a morning brief on employee satisfaction from Dynamics 365 ERP data for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft pl

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-employee-satisfaction
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_employee_satisfaction_agent.py` and embedded as the fenced Python below (sha256 d873646ea6cbc1b6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_employee_satisfaction_agent.py` first:

```bash
python3 scheduled_brief_monitor_employee_satisfaction_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_employee_satisfaction_agent.py   # or on stdin
python3 scheduled_brief_monitor_employee_satisfaction_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor employee satisfaction Scheduled Email Brief — Builds a morning brief on employee satisfaction from Dynamics 365 ERP data for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft pl

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-employee-satisfaction
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_employee_satisfaction',
    "version": '3.0.3',
    "display_name": 'Monitor employee satisfaction Scheduled Email Brief',
    "description": 'Builds a morning brief on employee satisfaction from Dynamics 365 ERP data for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft pl',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-monitor-employee-satisfaction',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-employee-satisfaction',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '84ec2b937d24a673',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/analyze-hr-programs/monitor-employee-satisfaction'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-monitor-employee-satisfaction', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'Optional cadence for the brief, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where monitor employee satisfaction stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on monitor employee satisfaction for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads monitor employee satisfaction, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on employee satisfaction from Dynamics 365 ERP data for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft pl', 'example_request': 'Draft my 7am weekday employee satisfaction brief from D365 USMF and email it to me as a draft.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when the responsible owner wants a daily or weekly employee-satisfaction brief drafted from D365 F&SCM data, as an unsent email draft and Teams post summary.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefMonitorEmployeeSatisfaction(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorEmployeeSatisfaction'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'Optional cadence for the brief, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefMonitorEmployeeSatisfaction().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
