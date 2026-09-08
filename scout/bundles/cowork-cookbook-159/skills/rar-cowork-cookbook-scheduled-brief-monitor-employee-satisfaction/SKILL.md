---
name: "rar-cowork-cookbook-scheduled-brief-monitor-employee-satisfaction"
description: "Builds a morning brief on employee satisfaction from Dynamics 365 ERP data for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and recommended next actions, saved as an email draft pl"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_employee_satisfaction", "rar_sha256": "d873646ea6cbc1b600074d0b95e10025570ada84ecf5f2980ece76b5b1511e1d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
