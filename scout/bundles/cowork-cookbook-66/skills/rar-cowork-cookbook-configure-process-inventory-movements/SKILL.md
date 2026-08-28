---
name: "rar-cowork-cookbook-configure-process-inventory-movements"
description: "Applies a bulk configuration change to process inventory movements from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_inventory_movements", "rar_sha256": "e84a3e1ed2452a38c70891ac14952749a95cf997e42bbb49be0546a0d6a0d1f7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_process_inventory_movements`. The original RAPP
agent is preserved byte-for-byte in `configure_process_inventory_movements_agent.py` and in the RCI capsule.

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

Process inventory movements Configuration Bulk Setup — Applies a bulk configuration change to process inventory movements from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-inventory-movements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_process_inventory_movements_agent.py` and embedded as the fenced Python below (sha256 e84a3e1ed2452a38…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_process_inventory_movements_agent.py` first:

```bash
python3 configure_process_inventory_movements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_process_inventory_movements_agent.py   # or on stdin
python3 configure_process_inventory_movements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process inventory movements Configuration Bulk Setup — Applies a bulk configuration change to process inventory movements from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-process-inventory-movements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_process_inventory_movements',
    "version": '2.0.0',
    "display_name": 'Process inventory movements Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to process inventory movements from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-process-inventory-movements',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-process-inventory-movements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '32335170b0634c57',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/process-inventory-movements'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-process-inventory-movements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureProcessInventoryMovements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureProcessInventoryMovements'
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
    print(ConfigureProcessInventoryMovements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
