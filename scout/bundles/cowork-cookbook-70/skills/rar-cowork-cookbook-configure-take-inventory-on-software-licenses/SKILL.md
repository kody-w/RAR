---
name: "rar-cowork-cookbook-configure-take-inventory-on-software-licenses"
description: "Applies a bulk configuration change to take inventory on software licenses from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_take_inventory_on_software_licenses", "rar_sha256": "fa1ffdc963fef5841b34ea52d7eb1613877b03ba04df2c06172b717a3e8a5a86", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_take_inventory_on_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `configure_take_inventory_on_software_licenses_agent.py` and in the RCI capsule.

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

Take inventory on software licenses Configuration Bulk Setup — Applies a bulk configuration change to take inventory on software licenses from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-take-inventory-on-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_take_inventory_on_software_licenses_agent.py` and embedded as the fenced Python below (sha256 fa1ffdc963fef584…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_take_inventory_on_software_licenses_agent.py` first:

```bash
python3 configure_take_inventory_on_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_take_inventory_on_software_licenses_agent.py   # or on stdin
python3 configure_take_inventory_on_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Take inventory on software licenses Configuration Bulk Setup — Applies a bulk configuration change to take inventory on software licenses from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-take-inventory-on-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_take_inventory_on_software_licenses',
    "version": '2.0.1',
    "display_name": 'Take inventory on software licenses Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to take inventory on software licenses from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-take-inventory-on-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-take-inventory-on-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3fdc1cecb5ad3716',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/take-inventory-on-software-licenses'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/configure-take-inventory-on-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureTakeInventoryOnSoftwareLicenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureTakeInventoryOnSoftwareLicenses'
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
    print(ConfigureTakeInventoryOnSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
