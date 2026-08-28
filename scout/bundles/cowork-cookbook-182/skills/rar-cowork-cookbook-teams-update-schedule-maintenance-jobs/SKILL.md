---
name: "rar-cowork-cookbook-teams-update-schedule-maintenance-jobs"
description: "Drafts a Teams channel post on schedule maintenance jobs status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_schedule_maintenance_jobs", "rar_sha256": "bda966bb5fb72d87bfcbec6bad2a720c8bb94de80ed9fe4ee768a53cc434f60e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
