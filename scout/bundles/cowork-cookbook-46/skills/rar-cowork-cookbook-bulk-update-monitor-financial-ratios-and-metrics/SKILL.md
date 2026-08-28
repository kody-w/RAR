---
name: "rar-cowork-cookbook-bulk-update-monitor-financial-ratios-and-metrics"
description: "Applies a bulk field update across monitor financial ratios and metrics records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_financial_ratios_and_metrics", "rar_sha256": "1f21b5a52f12d973ee77dd4a5c8c9cd8e7fcde10d9be07dd67d045769170ddbc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_monitor_financial_ratios_and_metrics_agent.py` and embedded as the fenced Python below (sha256 1f21b5a52f12d973…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_monitor_financial_ratios_and_metrics_agent.py` first:

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
    "version": '2.0.1',
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
