---
name: "rar-cowork-cookbook-bulk-update-define-operating-hours-and-schedule"
description: "Applies a bulk field update across define operating hours and schedule records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_operating_hours_and_schedule", "rar_sha256": "96fed5d82271cfffa186f23a1df15c34b8bafefdf81619c820d67a35c7f739b9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_define_operating_hours_and_schedule_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-define-operating-hours-and-schedule:e4d6eec838867c24e9d7b4b7af055431894d92472c2a58acb5a604e516f536f3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_define_operating_hours_and_schedule`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_define_operating_hours_and_schedule_agent.py` is
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

Define operating hours and schedule Bulk Field Update — Applies a bulk field update across define operating hours and schedule records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-operating-hours-and-schedule
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_operating_hours_and_schedule_agent.py` and embedded as the fenced Python below (sha256 96fed5d82271cfff…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_operating_hours_and_schedule_agent.py` first:

```bash
python3 bulk_update_define_operating_hours_and_schedule_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_operating_hours_and_schedule_agent.py   # or on stdin
python3 bulk_update_define_operating_hours_and_schedule_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define operating hours and schedule Bulk Field Update — Applies a bulk field update across define operating hours and schedule records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-operating-hours-and-schedule
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_operating_hours_and_schedule',
    "version": '2.0.0',
    "display_name": 'Define operating hours and schedule Bulk Field Update',
    "description": 'Applies a bulk field update across define operating hours and schedule records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-operating-hours-and-schedule',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-operating-hours-and-schedule',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa0daceea3994513',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-operating-hours-and-schedule'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/bulk-update-define-operating-hours-and-schedule', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.875, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefineOperatingHoursAndSchedule(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineOperatingHoursAndSchedule'
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
    print(BulkUpdateDefineOperatingHoursAndSchedule().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
