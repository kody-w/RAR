---
name: "rar-cowork-cookbook-teams-update-schedule-maintenance-jobs"
description: "Summarizes schedule maintenance jobs from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted automatically."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_schedule_maintenance_jobs", "rar_sha256": "71a5cbe578024fe975afa6eb9a8ddba6585713b0ee100cc6fd864988a7e38910", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_schedule_maintenance_jobs`. The original RAPP
agent is preserved byte-for-byte in `teams_update_schedule_maintenance_jobs_agent.py` and in the RCI capsule.

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

Schedule maintenance jobs Teams Channel Update — Summarizes schedule maintenance jobs from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted automatically.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-schedule-maintenance-jobs
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
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-schedule-maintenance-jobs-2026-05-24-card.json.",
      "type": "string"
    },
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_schedule_maintenance_jobs_agent.py` and embedded as the fenced Python below (sha256 71a5cbe578024fe9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_schedule_maintenance_jobs_agent.py` first:

```bash
python3 teams_update_schedule_maintenance_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_schedule_maintenance_jobs_agent.py   # or on stdin
python3 teams_update_schedule_maintenance_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule maintenance jobs Teams Channel Update — Summarizes schedule maintenance jobs from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted automatically.

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
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-schedule-maintenance-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_schedule_maintenance_jobs',
    "version": '3.0.3',
    "display_name": 'Schedule maintenance jobs Teams Channel Update',
    "description": 'Summarizes schedule maintenance jobs from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted automatically.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-schedule-maintenance-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-schedule-maintenance-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c85b9600d208b319',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/schedule-maintenance-jobs'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/teams-update-schedule-maintenance-jobs', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-schedule-maintenance-jobs-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of schedule maintenance jobs. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-schedule-maintenance-jobs-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': 'm365.cloud.microsoft 2026-06-01', 'what_it_does': 'Reads schedule maintenance jobs, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes schedule maintenance jobs from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted automatically.', 'example_request': "Draft a Teams update on schedule maintenance jobs in USMF with an Adaptive Card, but don't post it.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-schedule-maintenance-jobs-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a review-ready Teams channel update on schedule maintenance jobs status, with an Adaptive Card for triage, drafted but not posted.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateScheduleMaintenanceJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateScheduleMaintenanceJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-schedule-maintenance-jobs-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(TeamsUpdateScheduleMaintenanceJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
