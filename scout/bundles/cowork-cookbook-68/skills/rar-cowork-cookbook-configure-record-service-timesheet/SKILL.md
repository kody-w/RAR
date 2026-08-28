---
name: "rar-cowork-cookbook-configure-record-service-timesheet"
description: "Applies a bulk configuration change to record service timesheet from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_record_service_timesheet", "rar_sha256": "7be851393fd93b0fa66e72f55b28e13abdc9c8e6b8c9d57b94e2fc638c9ebd51", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_record_service_timesheet`. The original RAPP
agent is preserved byte-for-byte in `configure_record_service_timesheet_agent.py` and in the RCI capsule.

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

Record service timesheet Configuration Bulk Setup — Applies a bulk configuration change to record service timesheet from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-record-service-timesheet
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_record_service_timesheet_agent.py` and embedded as the fenced Python below (sha256 7be851393fd93b0f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_record_service_timesheet_agent.py` first:

```bash
python3 configure_record_service_timesheet_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_record_service_timesheet_agent.py   # or on stdin
python3 configure_record_service_timesheet_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record service timesheet Configuration Bulk Setup — Applies a bulk configuration change to record service timesheet from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-record-service-timesheet
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_record_service_timesheet',
    "version": '2.0.1',
    "display_name": 'Record service timesheet Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to record service timesheet from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-record-service-timesheet',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-record-service-timesheet',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cea7d86fff51ef54',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/record-service-timesheet'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-record-service-timesheet', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureRecordServiceTimesheet(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureRecordServiceTimesheet'
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
    print(ConfigureRecordServiceTimesheet().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
