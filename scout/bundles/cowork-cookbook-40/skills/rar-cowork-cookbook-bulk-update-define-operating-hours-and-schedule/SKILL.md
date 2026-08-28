---
name: "rar-cowork-cookbook-bulk-update-define-operating-hours-and-schedule"
description: "Applies a bulk field update across define operating hours and schedule records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_operating_hours_and_schedule", "rar_sha256": "b55c6c1788712d18c661274d470a45dcc66f64b6d0e0a3b85b4727acc179a9e0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_operating_hours_and_schedule_agent.py` and embedded as the fenced Python below (sha256 b55c6c1788712d18…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_operating_hours_and_schedule_agent.py` first:

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
    "version": '2.0.1',
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
