---
name: "rar-cowork-cookbook-scheduled-brief-schedule-maintenance-jobs"
description: "Schedulable morning-brief email summarizing schedule maintenance jobs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_schedule_maintenance_jobs", "rar_sha256": "620466c98977cab9f8146fd81a47c9d247af33b8654b1cd753ac3519e9570ef3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
