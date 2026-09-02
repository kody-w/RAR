---
name: "rar-cowork-cookbook-scheduled-brief-schedule-maintenance-jobs"
description: "Schedulable morning-brief email summarizing schedule maintenance jobs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_schedule_maintenance_jobs", "rar_sha256": "620466c98977cab9f8146fd81a47c9d247af33b8654b1cd753ac3519e9570ef3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_schedule_maintenance_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-schedule-maintenance-jobs:ce999638fe20e9ab3e648f9e07e3154bd28a130fa7c2c3cc9f545d697d4681d5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_schedule_maintenance_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_schedule_maintenance_jobs_agent.py` is
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

Schedule maintenance jobs Scheduled Email Brief — Schedulable morning-brief email summarizing schedule maintenance jobs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_schedule_maintenance_jobs_agent.py` and embedded as the fenced Python below (sha256 620466c98977cab9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_schedule_maintenance_jobs_agent.py` first:

```bash
python3 scheduled_brief_schedule_maintenance_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_schedule_maintenance_jobs_agent.py   # or on stdin
python3 scheduled_brief_schedule_maintenance_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule maintenance jobs Scheduled Email Brief — Schedulable morning-brief email summarizing schedule maintenance jobs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

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
    "version": '2.0.0',
    "display_name": 'Schedule maintenance jobs Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing schedule maintenance jobs for the responsible owner; designed to run daily or weekly.',
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
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '84cdb61d95b9938e',
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


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefScheduleMaintenanceJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefScheduleMaintenanceJobs'
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
    print(ScheduledBriefScheduleMaintenanceJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
