---
name: "rar-cowork-cookbook-bulk-update-define-operating-hours-and-schedule"
description: "Applies a bulk field update across define operating hours and schedule records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_operating_hours_and_schedule", "rar_sha256": "96fed5d82271cfffa186f23a1df15c34b8bafefdf81619c820d67a35c7f739b9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_operating_hours_and_schedule`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_operating_hours_and_schedule_agent.py` and in the RCI capsule.

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
