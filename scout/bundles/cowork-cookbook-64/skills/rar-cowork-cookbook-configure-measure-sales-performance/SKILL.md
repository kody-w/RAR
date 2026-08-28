---
name: "rar-cowork-cookbook-configure-measure-sales-performance"
description: "Applies a bulk configuration change to measure sales performance from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_measure_sales_performance", "rar_sha256": "10fb1e419366d3c58e97a23e8b94d72a7e4e4dfa27f6bc3df8203f035f3c2def", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_measure_sales_performance_agent.py` and embedded as the fenced Python below (sha256 10fb1e419366d3c5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_measure_sales_performance_agent.py` first:

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
    "version": '2.0.0',
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
