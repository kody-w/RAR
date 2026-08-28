---
name: "rar-cowork-cookbook-scheduled-brief-define-operating-hours-and-schedule"
description: "Schedulable morning-brief email summarizing define operating hours and schedule for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_operating_hours_and_schedule", "rar_sha256": "0ab553d774cbaa92bc12fbad3e16b2ecc7788d6b9ca2e24de05eb166b1f16e6c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_operating_hours_and_schedule`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_operating_hours_and_schedule_agent.py` and in the RCI capsule.

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
