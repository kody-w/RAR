---
name: "rar-cowork-cookbook-bulk-update-process-inventory-movements"
description: "Applies a bulk field update across process inventory movements records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_process_inventory_movements", "rar_sha256": "e534d59c1fb94bb926ac7f7289c18fc7fbd0faa926fc4ebfbb807871e918760b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_process_inventory_movements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-process-inventory-movements:18b4c694c5660ecd27f8441845adb3bf8a111b0103e253fa78a94c028df8dd4a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_process_inventory_movements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_process_inventory_movements_agent.py` is
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
