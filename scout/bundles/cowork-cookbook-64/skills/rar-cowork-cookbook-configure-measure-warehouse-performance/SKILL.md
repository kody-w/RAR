---
name: "rar-cowork-cookbook-configure-measure-warehouse-performance"
description: "Applies a bulk configuration change to measure warehouse performance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_measure_warehouse_performance", "rar_sha256": "1b550024728d9dacf1083515adedfab99d621d03b97f36248e006f91bb682315", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_measure_warehouse_performance`. The original RAPP
agent is preserved byte-for-byte in `configure_measure_warehouse_performance_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_measure_warehouse_performance_agent.py` and embedded as the fenced Python below (sha256 1b550024728d9dac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_measure_warehouse_performance_agent.py` first:

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
    "version": '2.0.1',
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
