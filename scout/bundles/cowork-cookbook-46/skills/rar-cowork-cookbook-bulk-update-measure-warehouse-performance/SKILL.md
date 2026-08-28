---
name: "rar-cowork-cookbook-bulk-update-measure-warehouse-performance"
description: "Applies a bulk field update across measure warehouse performance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_measure_warehouse_performance", "rar_sha256": "6401a68300c6ffd0d6fbabab249c54740402f15ef8e3a47bb1c6b9447b6a7955", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_measure_warehouse_performance`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_measure_warehouse_performance_agent.py` and in the RCI capsule.

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

Measure warehouse performance Bulk Field Update — Applies a bulk field update across measure warehouse performance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-warehouse-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_measure_warehouse_performance_agent.py` and embedded as the fenced Python below (sha256 6401a68300c6ffd0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_measure_warehouse_performance_agent.py` first:

```bash
python3 bulk_update_measure_warehouse_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_measure_warehouse_performance_agent.py   # or on stdin
python3 bulk_update_measure_warehouse_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure warehouse performance Bulk Field Update — Applies a bulk field update across measure warehouse performance records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-measure-warehouse-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_measure_warehouse_performance',
    "version": '2.0.1',
    "display_name": 'Measure warehouse performance Bulk Field Update',
    "description": 'Applies a bulk field update across measure warehouse performance records from an input list, with dry-run preview before commit.',
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
        "upstream_slug": 'bulk-update-measure-warehouse-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-measure-warehouse-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '07564d8ede5ab71e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/measure-warehouse-performance'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/bulk-update-measure-warehouse-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateMeasureWarehousePerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMeasureWarehousePerformance'
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
    print(BulkUpdateMeasureWarehousePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
