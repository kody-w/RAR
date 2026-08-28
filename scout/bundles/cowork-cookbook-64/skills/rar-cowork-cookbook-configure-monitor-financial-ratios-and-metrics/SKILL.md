---
name: "rar-cowork-cookbook-configure-monitor-financial-ratios-and-metrics"
description: "Applies a bulk configuration change to monitor financial ratios and metrics from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_monitor_financial_ratios_and_metrics", "rar_sha256": "4ea116c6c9a26f70f30ace9c311a27d814170894e5611dd75874a3f7ace9abc0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_monitor_financial_ratios_and_metrics_agent.py` and embedded as the fenced Python below (sha256 4ea116c6c9a26f70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_monitor_financial_ratios_and_metrics_agent.py` first:

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
    "version": '2.0.0',
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
