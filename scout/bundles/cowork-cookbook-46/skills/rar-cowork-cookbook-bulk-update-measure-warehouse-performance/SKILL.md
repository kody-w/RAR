---
name: "rar-cowork-cookbook-bulk-update-measure-warehouse-performance"
description: "Applies a bulk field update across measure warehouse performance records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_measure_warehouse_performance", "rar_sha256": "b0b9fe5c857185c91ef9e2ffc6fa543fe4fa37b11fac7e55ff4df1217350d2c1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_measure_warehouse_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-measure-warehouse-performance:6b3741862d6a6e08e52e5807851875c364d77fd4d06d04f308e9b4b15115c003", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_measure_warehouse_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_measure_warehouse_performance_agent.py` is
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
