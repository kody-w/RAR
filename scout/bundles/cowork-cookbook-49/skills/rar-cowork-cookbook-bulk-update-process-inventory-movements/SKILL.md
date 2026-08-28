---
name: "rar-cowork-cookbook-bulk-update-process-inventory-movements"
description: "Applies a bulk field update across process inventory movements records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_process_inventory_movements", "rar_sha256": "e534d59c1fb94bb926ac7f7289c18fc7fbd0faa926fc4ebfbb807871e918760b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_process_inventory_movements_agent.py` and embedded as the fenced Python below (sha256 e534d59c1fb94bb9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_process_inventory_movements_agent.py` first:

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
    "version": '2.0.0',
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
