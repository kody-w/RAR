---
name: "rar-cowork-cookbook-teams-update-schedule-maintenance-jobs"
description: "Drafts a Teams channel post on schedule maintenance jobs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_schedule_maintenance_jobs", "rar_sha256": "bda966bb5fb72d87bfcbec6bad2a720c8bb94de80ed9fe4ee768a53cc434f60e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_schedule_maintenance_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-schedule-maintenance-jobs:faac86050cf7967e09dbc2305d6e647774a01dc3b4d506d453fd0ad5d4109953", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_schedule_maintenance_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_schedule_maintenance_jobs_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Schedule maintenance jobs Teams Channel Update — Drafts a Teams channel post on schedule maintenance jobs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_schedule_maintenance_jobs_agent.py` and embedded as the fenced Python below (sha256 bda966bb5fb72d87…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_schedule_maintenance_jobs_agent.py` first:

```bash
python3 teams_update_schedule_maintenance_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_schedule_maintenance_jobs_agent.py   # or on stdin
python3 teams_update_schedule_maintenance_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule maintenance jobs Teams Channel Update — Drafts a Teams channel post on schedule maintenance jobs status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.0',
    "display_name": 'Schedule maintenance jobs Teams Channel Update',
    "description": 'Drafts a Teams channel post on schedule maintenance jobs status with an interactive Adaptive Card for quick triage.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6012b3db0b98fb75',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateScheduleMaintenanceJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateScheduleMaintenanceJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
