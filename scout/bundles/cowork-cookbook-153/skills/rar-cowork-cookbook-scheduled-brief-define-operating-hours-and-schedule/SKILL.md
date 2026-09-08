---
name: "rar-cowork-cookbook-scheduled-brief-define-operating-hours-and-schedule"
description: "Builds a morning brief on operating hours and schedule from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unsen"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_operating_hours_and_schedule", "rar_sha256": "3a72f4662eea59c02f8ac2812891c00891bbedbf0aa9d45631c4ec3bf83b8206", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_operating_hours_and_schedule`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_operating_hours_and_schedule_agent.py` and in the RCI capsule.

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

Define operating hours and schedule Scheduled Email Brief — Builds a morning brief on operating hours and schedule from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unsen

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-operating-hours-and-schedule
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
      "description": "When the brief should run, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_operating_hours_and_schedule_agent.py` and embedded as the fenced Python below (sha256 3a72f4662eea59c0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_operating_hours_and_schedule_agent.py` first:

```bash
python3 scheduled_brief_define_operating_hours_and_schedule_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_operating_hours_and_schedule_agent.py   # or on stdin
python3 scheduled_brief_define_operating_hours_and_schedule_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define operating hours and schedule Scheduled Email Brief — Builds a morning brief on operating hours and schedule from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unsen

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-operating-hours-and-schedule
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_operating_hours_and_schedule',
    "version": '3.0.3',
    "display_name": 'Define operating hours and schedule Scheduled Email Brief',
    "description": 'Builds a morning brief on operating hours and schedule from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unsen',
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
        "upstream_slug": 'scheduled-brief-define-operating-hours-and-schedule',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-operating-hours-and-schedule',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a85541bf1b1f58f8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-operating-hours-and-schedule'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-define-operating-hours-and-schedule', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to query; defaults to USMF.', 'owner': 'Responsible owner who receives the drafted email brief.', 'schedule': 'When the brief should run, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where define operating hours and schedule stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on define operating hours and schedule for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define operating hours and schedule, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on operating hours and schedule from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unsen', 'example_request': 'Send me a 7am weekday brief on operating hours and schedule in USMF, drafted to the owner.', 'inputs': [{'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Responsible owner who receives the drafted email brief.', 'name': 'owner'}, {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly operating-hours/schedule brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefDefineOperatingHoursAndSchedule(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineOperatingHoursAndSchedule'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to query; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'owner': {'description': 'Responsible owner who receives the drafted email brief.', 'type': 'string'}, 'schedule': {'description': 'When the brief should run, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefDefineOperatingHoursAndSchedule().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
