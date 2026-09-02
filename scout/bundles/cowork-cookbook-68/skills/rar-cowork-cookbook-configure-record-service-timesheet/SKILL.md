---
name: "rar-cowork-cookbook-configure-record-service-timesheet"
description: "Applies a bulk configuration change to record service timesheet from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_record_service_timesheet", "rar_sha256": "abeb7f420887e505dfa58193300eeefee66b87a32a10ab18f4df11494d6d9864", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_record_service_timesheet_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-record-service-timesheet:2ae379bdb761b2bd0e73a08aaa8d9767c4c9d42bf3f8d88c0180df1d84508973", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_record_service_timesheet`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_record_service_timesheet_agent.py` is
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
