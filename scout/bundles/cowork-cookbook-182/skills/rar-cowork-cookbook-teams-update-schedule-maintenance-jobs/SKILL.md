---
name: "rar-cowork-cookbook-teams-update-schedule-maintenance-jobs"
description: "Summarizes schedule maintenance jobs from Dynamics 365 F&SCM for a given legal entity and saves two artifacts: a markdown Teams channel post and an Adaptive Card JSON; nothing is posted automatically."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_schedule_maintenance_jobs", "rar_sha256": "71a5cbe578024fe975afa6eb9a8ddba6585713b0ee100cc6fd864988a7e38910", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
