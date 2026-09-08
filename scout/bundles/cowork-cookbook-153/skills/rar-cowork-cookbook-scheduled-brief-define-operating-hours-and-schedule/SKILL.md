---
name: "rar-cowork-cookbook-scheduled-brief-define-operating-hours-and-schedule"
description: "Builds a morning brief on operating hours and schedule from Dynamics 365 F&SCM (legal entity USMF) with top 5 items by impact, anomalies vs the 7-day rolling average, and next actions; drafts an email to the owner (unsen"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_operating_hours_and_schedule", "rar_sha256": "3a72f4662eea59c02f8ac2812891c00891bbedbf0aa9d45631c4ec3bf83b8206", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
