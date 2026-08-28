---
name: "rar-cowork-cookbook-configure-allocate-or-assign-software-licenses"
description: "Applies a bulk configuration change to allocate or assign software licenses from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_allocate_or_assign_software_licenses", "rar_sha256": "0f0c918983e874e67b632113eed1e83834bfd5b4f94e6b4c7980b2b5c992c632", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_allocate_or_assign_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `configure_allocate_or_assign_software_licenses_agent.py` and in the RCI capsule.

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

Allocate or assign software licenses Configuration Bulk Setup — Applies a bulk configuration change to allocate or assign software licenses from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-allocate-or-assign-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_allocate_or_assign_software_licenses_agent.py` and embedded as the fenced Python below (sha256 0f0c918983e874e6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_allocate_or_assign_software_licenses_agent.py` first:

```bash
python3 configure_allocate_or_assign_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_allocate_or_assign_software_licenses_agent.py   # or on stdin
python3 configure_allocate_or_assign_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Allocate or assign software licenses Configuration Bulk Setup — Applies a bulk configuration change to allocate or assign software licenses from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-allocate-or-assign-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_allocate_or_assign_software_licenses',
    "version": '2.0.1',
    "display_name": 'Allocate or assign software licenses Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to allocate or assign software licenses from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-allocate-or-assign-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-allocate-or-assign-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e21b2795dd2559e4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/allocate-or-assign-software-licenses'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-allocate-or-assign-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureAllocateOrAssignSoftwareLicenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAllocateOrAssignSoftwareLicenses'
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
    print(ConfigureAllocateOrAssignSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
