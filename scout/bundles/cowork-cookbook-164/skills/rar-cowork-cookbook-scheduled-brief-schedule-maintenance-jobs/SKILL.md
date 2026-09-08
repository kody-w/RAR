---
name: "rar-cowork-cookbook-scheduled-brief-schedule-maintenance-jobs"
description: "Builds a morning brief on schedule maintenance jobs from Dynamics 365 ERP for a given legal entity: top 5 items by impact, anomalies vs the 7-day rolling average, and next actions, then saves a draft email to the owner p"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_schedule_maintenance_jobs", "rar_sha256": "094f06c51f3d615839800b3701bc3070955603a4009e52ac3951e9341cfd91c7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
