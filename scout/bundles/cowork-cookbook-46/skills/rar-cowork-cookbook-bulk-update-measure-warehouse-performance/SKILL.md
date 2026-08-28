---
name: "rar-cowork-cookbook-bulk-update-measure-warehouse-performance"
description: "Applies a bulk field update across measure warehouse performance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_measure_warehouse_performance", "rar_sha256": "b0b9fe5c857185c91ef9e2ffc6fa543fe4fa37b11fac7e55ff4df1217350d2c1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_measure_warehouse_performance_agent.py` and embedded as the fenced Python below (sha256 b0b9fe5c857185c9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_measure_warehouse_performance_agent.py` first:

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
    "version": '2.0.0',
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
