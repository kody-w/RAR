---
name: "rar-cowork-cookbook-teams-update-schedule-maintenance-jobs"
description: "Drafts a Teams channel post on schedule maintenance jobs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_schedule_maintenance_jobs", "rar_sha256": "9756692bed9b0f4800f88ec7551f756f89b3b02c99e7517bde7ecb316164f3cb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_schedule_maintenance_jobs_agent.py` and embedded as the fenced Python below (sha256 9756692bed9b0f48…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_schedule_maintenance_jobs_agent.py` first:

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
    "version": '2.0.1',
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
