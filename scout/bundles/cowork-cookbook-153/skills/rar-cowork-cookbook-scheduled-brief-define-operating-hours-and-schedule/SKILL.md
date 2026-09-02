---
name: "rar-cowork-cookbook-scheduled-brief-define-operating-hours-and-schedule"
description: "Schedulable morning-brief email summarizing define operating hours and schedule for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_operating_hours_and_schedule", "rar_sha256": "0ab553d774cbaa92bc12fbad3e16b2ecc7788d6b9ca2e24de05eb166b1f16e6c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_define_operating_hours_and_schedule_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-define-operating-hours-and-schedule:695acad152eae833635ef66a3ec78958548ec1f4840b93c32010b69451fc1f9d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_define_operating_hours_and_schedule`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_define_operating_hours_and_schedule_agent.py` is
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

Define operating hours and schedule Scheduled Email Brief — Schedulable morning-brief email summarizing define operating hours and schedule for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-operating-hours-and-schedule
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_operating_hours_and_schedule_agent.py` and embedded as the fenced Python below (sha256 0ab553d774cbaa92…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_operating_hours_and_schedule_agent.py` first:

```bash
python3 scheduled_brief_define_operating_hours_and_schedule_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_operating_hours_and_schedule_agent.py   # or on stdin
python3 scheduled_brief_define_operating_hours_and_schedule_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define operating hours and schedule Scheduled Email Brief — Schedulable morning-brief email summarizing define operating hours and schedule for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-operating-hours-and-schedule
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_operating_hours_and_schedule',
    "version": '2.0.0',
    "display_name": 'Define operating hours and schedule Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define operating hours and schedule for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'scheduled-brief-define-operating-hours-and-schedule',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-operating-hours-and-schedule',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ccf094b32e61c95',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-operating-hours-and-schedule'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/scheduled-brief-define-operating-hours-and-schedule', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.833, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDefineOperatingHoursAndSchedule(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineOperatingHoursAndSchedule'
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
    print(ScheduledBriefDefineOperatingHoursAndSchedule().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
