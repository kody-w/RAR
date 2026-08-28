---
name: "rar-cowork-cookbook-configure-define-operating-hours"
description: "Applies a bulk configuration change to define operating hours from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_operating_hours", "rar_sha256": "99b3609be98006e43b42c6ccb0fa0484a9876bf13604daca0591bdfb670d8ba5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
