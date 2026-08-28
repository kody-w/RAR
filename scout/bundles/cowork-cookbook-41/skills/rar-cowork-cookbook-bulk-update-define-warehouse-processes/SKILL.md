---
name: "rar-cowork-cookbook-bulk-update-define-warehouse-processes"
description: "Applies a bulk field update across define warehouse processes records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_warehouse_processes", "rar_sha256": "c78787d1bd2c4d28a0d2a452b7e0b1464c3deee52ddc8c270cfa9f2e9334fc63", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_warehouse_processes`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_warehouse_processes_agent.py` and in the RCI capsule.

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

Define warehouse processes Bulk Field Update — Applies a bulk field update across define warehouse processes records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-warehouse-processes
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_warehouse_processes_agent.py` and embedded as the fenced Python below (sha256 c78787d1bd2c4d28…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_warehouse_processes_agent.py` first:

```bash
python3 bulk_update_define_warehouse_processes_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_warehouse_processes_agent.py   # or on stdin
python3 bulk_update_define_warehouse_processes_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define warehouse processes Bulk Field Update — Applies a bulk field update across define warehouse processes records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-warehouse-processes
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_warehouse_processes',
    "version": '2.0.1',
    "display_name": 'Define warehouse processes Bulk Field Update',
    "description": 'Applies a bulk field update across define warehouse processes records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-define-warehouse-processes',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-warehouse-processes',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a8eb01f1128b3147',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-warehouse-operations/define-warehouse-processes'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-define-warehouse-processes', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefineWarehouseProcesses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineWarehouseProcesses'
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
    print(BulkUpdateDefineWarehouseProcesses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
