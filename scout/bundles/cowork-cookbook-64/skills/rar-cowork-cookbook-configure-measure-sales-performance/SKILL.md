---
name: "rar-cowork-cookbook-configure-measure-sales-performance"
description: "Applies a bulk configuration change to measure sales performance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_measure_sales_performance", "rar_sha256": "de24eb8f0b90ac57c1db7008af7a77354f4c04bf17c17c74511550e236fa9887", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_measure_sales_performance`. The original RAPP
agent is preserved byte-for-byte in `configure_measure_sales_performance_agent.py` and in the RCI capsule.

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

Measure sales performance Configuration Bulk Setup — Applies a bulk configuration change to measure sales performance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-measure-sales-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_measure_sales_performance_agent.py` and embedded as the fenced Python below (sha256 de24eb8f0b90ac57…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_measure_sales_performance_agent.py` first:

```bash
python3 configure_measure_sales_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_measure_sales_performance_agent.py   # or on stdin
python3 configure_measure_sales_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure sales performance Configuration Bulk Setup — Applies a bulk configuration change to measure sales performance from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-measure-sales-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_measure_sales_performance',
    "version": '2.0.1',
    "display_name": 'Measure sales performance Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to measure sales performance from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-measure-sales-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-measure-sales-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c76fa1457d07794c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/measure-sales-performance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-measure-sales-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ConfigureMeasureSalesPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMeasureSalesPerformance'
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
    print(ConfigureMeasureSalesPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
