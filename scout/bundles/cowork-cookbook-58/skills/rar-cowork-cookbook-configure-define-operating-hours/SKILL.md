---
name: "rar-cowork-cookbook-configure-define-operating-hours"
description: "Applies a bulk configuration change to define operating hours from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_operating_hours", "rar_sha256": "be7e7f2e762a52c796a8ec451ebd04530dbfe794154d29cc22329035287e69af", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_operating_hours`. The original RAPP
agent is preserved byte-for-byte in `configure_define_operating_hours_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_operating_hours_agent.py` and embedded as the fenced Python below (sha256 be7e7f2e762a52c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_operating_hours_agent.py` first:

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
    "version": '2.0.1',
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
