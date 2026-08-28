---
name: "rar-cowork-cookbook-bulk-update-monitor-financial-ratios-and-metrics"
description: "Applies a bulk field update across monitor financial ratios and metrics records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_financial_ratios_and_metrics", "rar_sha256": "91eab69ca4d7eb872d578353b8e4bfd51981e8697ffbf75d8d02328a75a12af5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_monitor_financial_ratios_and_metrics`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_monitor_financial_ratios_and_metrics_agent.py` and in the RCI capsule.

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

Monitor financial ratios and metrics Bulk Field Update — Applies a bulk field update across monitor financial ratios and metrics records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-financial-ratios-and-metrics
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_financial_ratios_and_metrics_agent.py` and embedded as the fenced Python below (sha256 91eab69ca4d7eb87…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_financial_ratios_and_metrics_agent.py` first:

```bash
python3 bulk_update_monitor_financial_ratios_and_metrics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_monitor_financial_ratios_and_metrics_agent.py   # or on stdin
python3 bulk_update_monitor_financial_ratios_and_metrics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor financial ratios and metrics Bulk Field Update — Applies a bulk field update across monitor financial ratios and metrics records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-monitor-financial-ratios-and-metrics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_monitor_financial_ratios_and_metrics',
    "version": '2.0.0',
    "display_name": 'Monitor financial ratios and metrics Bulk Field Update',
    "description": 'Applies a bulk field update across monitor financial ratios and metrics records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-monitor-financial-ratios-and-metrics',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-monitor-financial-ratios-and-metrics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd1dc98d11321f31e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/monitor-financial-ratios-and-metrics'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/bulk-update-monitor-financial-ratios-and-metrics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateMonitorFinancialRatiosAndMetrics(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateMonitorFinancialRatiosAndMetrics'
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
    print(BulkUpdateMonitorFinancialRatiosAndMetrics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
