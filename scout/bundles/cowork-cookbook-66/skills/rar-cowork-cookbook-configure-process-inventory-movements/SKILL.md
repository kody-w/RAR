---
name: "rar-cowork-cookbook-configure-process-inventory-movements"
description: "Applies a bulk configuration change to process inventory movements from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_process_inventory_movements", "rar_sha256": "e84a3e1ed2452a38c70891ac14952749a95cf997e42bbb49be0546a0d6a0d1f7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_process_inventory_movements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-process-inventory-movements:1e67cd2cf13268c31191af843722b2e9ed37cc4fb5fbb0493aa774bb013fb523", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_process_inventory_movements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_process_inventory_movements_agent.py` is
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
