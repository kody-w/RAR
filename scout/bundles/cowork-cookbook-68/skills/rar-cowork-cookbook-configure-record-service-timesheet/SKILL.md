---
name: "rar-cowork-cookbook-configure-record-service-timesheet"
description: "Applies a bulk configuration change to record service timesheet from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_record_service_timesheet", "rar_sha256": "abeb7f420887e505dfa58193300eeefee66b87a32a10ab18f4df11494d6d9864", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_record_service_timesheet_agent.py` and embedded as the fenced Python below (sha256 abeb7f420887e505…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_record_service_timesheet_agent.py` first:

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
    "version": '2.0.0',
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
