---
name: "rar-cowork-cookbook-scheduled-brief-schedule-maintenance-jobs"
description: "Schedulable morning-brief email summarizing schedule maintenance jobs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_schedule_maintenance_jobs", "rar_sha256": "932222cb311bc92057def0b769baa6418a574b1e17213ef7bc93ff3556ae113e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_schedule_maintenance_jobs_agent.py` and embedded as the fenced Python below (sha256 932222cb311bc920…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_schedule_maintenance_jobs_agent.py` first:

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
    "version": '2.0.1',
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
