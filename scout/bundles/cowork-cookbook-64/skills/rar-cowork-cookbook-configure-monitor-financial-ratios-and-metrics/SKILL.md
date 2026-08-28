---
name: "rar-cowork-cookbook-configure-monitor-financial-ratios-and-metrics"
description: "Applies a bulk configuration change to monitor financial ratios and metrics from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_monitor_financial_ratios_and_metrics", "rar_sha256": "99cedc01d74bb41d3be35e78f2bd3ac6edb0f90e03b6c45548478f05dbe56cf0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_monitor_financial_ratios_and_metrics`. The original RAPP
agent is preserved byte-for-byte in `configure_monitor_financial_ratios_and_metrics_agent.py` and in the RCI capsule.

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

Monitor financial ratios and metrics Configuration Bulk Setup — Applies a bulk configuration change to monitor financial ratios and metrics from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-monitor-financial-ratios-and-metrics
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_monitor_financial_ratios_and_metrics_agent.py` and embedded as the fenced Python below (sha256 99cedc01d74bb41d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_monitor_financial_ratios_and_metrics_agent.py` first:

```bash
python3 configure_monitor_financial_ratios_and_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_monitor_financial_ratios_and_metrics_agent.py   # or on stdin
python3 configure_monitor_financial_ratios_and_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor financial ratios and metrics Configuration Bulk Setup — Applies a bulk configuration change to monitor financial ratios and metrics from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-monitor-financial-ratios-and-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_monitor_financial_ratios_and_metrics',
    "version": '2.0.1',
    "display_name": 'Monitor financial ratios and metrics Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to monitor financial ratios and metrics from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-monitor-financial-ratios-and-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-monitor-financial-ratios-and-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4b0f21b79bffac97',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-financial-ratios-and-metrics'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/configure-monitor-financial-ratios-and-metrics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureMonitorFinancialRatiosAndMetrics(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMonitorFinancialRatiosAndMetrics'
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
    print(ConfigureMonitorFinancialRatiosAndMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
