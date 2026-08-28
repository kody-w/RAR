---
name: "rar-cowork-cookbook-bulk-update-process-inventory-movements"
description: "Applies a bulk field update across process inventory movements records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_process_inventory_movements", "rar_sha256": "05cd8d7bf80391306b272b69b82031f4d3319a5a502a502946d0b08dd9f18528", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_process_inventory_movements`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_process_inventory_movements_agent.py` and in the RCI capsule.

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

Process inventory movements Bulk Field Update — Applies a bulk field update across process inventory movements records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-process-inventory-movements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_process_inventory_movements_agent.py` and embedded as the fenced Python below (sha256 05cd8d7bf8039130…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_process_inventory_movements_agent.py` first:

```bash
python3 bulk_update_process_inventory_movements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_process_inventory_movements_agent.py   # or on stdin
python3 bulk_update_process_inventory_movements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process inventory movements Bulk Field Update — Applies a bulk field update across process inventory movements records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-process-inventory-movements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_process_inventory_movements',
    "version": '2.0.1',
    "display_name": 'Process inventory movements Bulk Field Update',
    "description": 'Applies a bulk field update across process inventory movements records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-process-inventory-movements',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-process-inventory-movements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'abb60bf1cc7532df',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/process-inventory-movements'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-process-inventory-movements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateProcessInventoryMovements(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateProcessInventoryMovements'
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
    print(BulkUpdateProcessInventoryMovements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
