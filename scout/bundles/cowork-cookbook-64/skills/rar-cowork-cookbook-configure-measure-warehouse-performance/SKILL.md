---
name: "rar-cowork-cookbook-configure-measure-warehouse-performance"
description: "Applies a bulk configuration change to measure warehouse performance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_measure_warehouse_performance", "rar_sha256": "2a314dc6a1b98ffb6975000261b7f26970825750159d4287de69c486417a859a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_measure_warehouse_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-measure-warehouse-performance:6e35688a55d5e03fac90c1c7347d4d21520b9c56d74be4ca353fb9c9fb57f8d1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_measure_warehouse_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_measure_warehouse_performance_agent.py` is
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

Measure warehouse performance Configuration Bulk Setup — Applies a bulk configuration change to measure warehouse performance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-measure-warehouse-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_measure_warehouse_performance_agent.py` and embedded as the fenced Python below (sha256 2a314dc6a1b98ffb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_measure_warehouse_performance_agent.py` first:

```bash
python3 configure_measure_warehouse_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_measure_warehouse_performance_agent.py   # or on stdin
python3 configure_measure_warehouse_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure warehouse performance Configuration Bulk Setup — Applies a bulk configuration change to measure warehouse performance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-measure-warehouse-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_measure_warehouse_performance',
    "version": '2.0.0',
    "display_name": 'Measure warehouse performance Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to measure warehouse performance from an input Excel file, with validation and rollback support.',
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
        "upstream_slug": 'configure-measure-warehouse-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-measure-warehouse-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1d62c60ec1432b1f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/measure-warehouse-performance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-measure-warehouse-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureMeasureWarehousePerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMeasureWarehousePerformance'
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
    print(ConfigureMeasureWarehousePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
