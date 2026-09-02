---
name: "rar-cowork-cookbook-configure-define-operating-hours"
description: "Applies a bulk configuration change to define operating hours from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_operating_hours", "rar_sha256": "99b3609be98006e43b42c6ccb0fa0484a9876bf13604daca0591bdfb670d8ba5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_define_operating_hours_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-define-operating-hours:64ee4220d3aa7d49ae53f9f042236d085b7b3b6fa63f73229f76f6f066f8773a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_define_operating_hours`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_define_operating_hours_agent.py` is
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

Define operating hours Configuration Bulk Setup — Applies a bulk configuration change to define operating hours from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-operating-hours
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_operating_hours_agent.py` and embedded as the fenced Python below (sha256 99b3609be98006e4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_operating_hours_agent.py` first:

```bash
python3 configure_define_operating_hours_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_operating_hours_agent.py   # or on stdin
python3 configure_define_operating_hours_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define operating hours Configuration Bulk Setup — Applies a bulk configuration change to define operating hours from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-operating-hours
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_operating_hours',
    "version": '2.0.0',
    "display_name": 'Define operating hours Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to define operating hours from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-define-operating-hours',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-operating-hours',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b2fe4af23d0dafa1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-operating-hours'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/configure-define-operating-hours', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureDefineOperatingHours(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineOperatingHours'
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
    print(ConfigureDefineOperatingHours().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
