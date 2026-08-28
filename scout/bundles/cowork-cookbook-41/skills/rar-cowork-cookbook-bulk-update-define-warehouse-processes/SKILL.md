---
name: "rar-cowork-cookbook-bulk-update-define-warehouse-processes"
description: "Applies a bulk field update across define warehouse processes records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_warehouse_processes", "rar_sha256": "313a3e051a63339cc233cbaea75352e90ce90a126e848f191daeaac571780ae5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_warehouse_processes_agent.py` and embedded as the fenced Python below (sha256 313a3e051a63339c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_warehouse_processes_agent.py` first:

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
    "version": '2.0.0',
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
