---
name: "rar-cowork-cookbook-scheduled-brief-define-operating-hours-and-schedule"
description: "Schedulable morning-brief email summarizing define operating hours and schedule for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_operating_hours_and_schedule", "rar_sha256": "c8f2d96d5a35d1f2b25f259f0657cd9d92a190b05dc74951c30531f9aa002e6d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_operating_hours_and_schedule_agent.py` and embedded as the fenced Python below (sha256 c8f2d96d5a35d1f2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_operating_hours_and_schedule_agent.py` first:

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
    "version": '2.0.1',
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
