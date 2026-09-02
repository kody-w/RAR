---
name: "rar-cowork-cookbook-configure-monitor-financial-ratios-and-metrics"
description: "Applies a bulk configuration change to monitor financial ratios and metrics from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_monitor_financial_ratios_and_metrics", "rar_sha256": "4ea116c6c9a26f70f30ace9c311a27d814170894e5611dd75874a3f7ace9abc0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_monitor_financial_ratios_and_metrics_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-monitor-financial-ratios-and-metrics:feabc8bfd59c2b25916272b6cd22043b9000ef54e4fc55fc933eb475285aeb5d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_monitor_financial_ratios_and_metrics`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_monitor_financial_ratios_and_metrics_agent.py` is
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
