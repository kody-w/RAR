---
name: "rar-cowork-cookbook-scheduled-brief-schedule-maintenance-jobs"
description: "Builds a morning brief on schedule maintenance jobs from Dynamics 365 ERP for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_schedule_maintenance_jobs", "rar_sha256": "094f06c51f3d615839800b3701bc3070955603a4009e52ac3951e9341cfd91c7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_schedule_maintenance_jobs`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_schedule_maintenance_jobs_agent.py` and in the RCI capsule.

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

Schedule maintenance jobs Scheduled Email Brief — Builds a morning brief on schedule maintenance jobs from Dynamics 365 ERP for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner p

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-schedule-maintenance-jobs
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
      "description": "D365 F&SCM legal entity to query, e.g. USMF.",
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
    "responsible_owner": {
      "description": "Person the brief is addressed to and whose draft email is created.",
      "type": "string"
    },
    "schedule": {
      "description": "Optional run cadence, e.g. weekday mornings at 7am.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_schedule_maintenance_jobs_agent.py` and embedded as the fenced Python below (sha256 094f06c51f3d6158…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_schedule_maintenance_jobs_agent.py` first:

```bash
python3 scheduled_brief_schedule_maintenance_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_schedule_maintenance_jobs_agent.py   # or on stdin
python3 scheduled_brief_schedule_maintenance_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule maintenance jobs Scheduled Email Brief — Builds a morning brief on schedule maintenance jobs from Dynamics 365 ERP for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner p

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
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-schedule-maintenance-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_schedule_maintenance_jobs',
    "version": '3.0.3',
    "display_name": 'Schedule maintenance jobs Scheduled Email Brief',
    "description": 'Builds a morning brief on schedule maintenance jobs from Dynamics 365 ERP for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner p',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-schedule-maintenance-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-schedule-maintenance-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '076c79d92c7f33a2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/schedule-maintenance-jobs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-schedule-maintenance-jobs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 F&SCM legal entity to query, e.g. USMF.', 'responsible_owner': 'Person the brief is addressed to and whose draft email is created.', 'schedule': 'Optional run cadence, e.g. weekday mornings at 7am.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Replaces a daily manual spreadsheet stitch with an automatic brief so owners walk into standup already knowing where schedule maintenance jobs stands.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': 'Using the Dynamics 365 ERP plugin against legal entity USMF, build a short morning brief on schedule maintenance jobs for the responsible owner. Include: (a) top 5 items by impact today, (b) any anomalies vs the 7-day rolling average, (c) recommended next actions. Draft an email to the owner (save to drafts, do not send). Also produce a Communications-ready summary suitable for a Teams channel post. This recipe is a strong candidate for a Cowork scheduled task - schedule for weekday mornings at 7am.', 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads schedule maintenance jobs, computes a short brief, drafts an email, and is a strong candidate for a Cowork scheduled task.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a morning brief on schedule maintenance jobs from Dynamics 365 ERP for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner p', 'example_request': 'Give me the 7am morning brief on schedule maintenance jobs in USMF and draft it to the owner.', 'inputs': [{'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Person the brief is addressed to and whose draft email is created.', 'name': 'responsible_owner'}, {'description': 'Optional run cadence, e.g. weekday mornings at 7am.', 'name': 'schedule'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a daily or weekly schedule-maintenance-jobs brief for the responsible owner, drafted as an email and a Teams channel post.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ScheduledBriefScheduleMaintenanceJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefScheduleMaintenanceJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 F&SCM legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'responsible_owner': {'description': 'Person the brief is addressed to and whose draft email is created.', 'type': 'string'}, 'schedule': {'description': 'Optional run cadence, e.g. weekday mornings at 7am.', 'type': 'string'}},
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
    print(ScheduledBriefScheduleMaintenanceJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
