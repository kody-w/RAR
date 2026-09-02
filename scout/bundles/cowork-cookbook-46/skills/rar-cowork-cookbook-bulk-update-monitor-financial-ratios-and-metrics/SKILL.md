---
name: "rar-cowork-cookbook-bulk-update-monitor-financial-ratios-and-metrics"
description: "Applies a bulk field update across monitor financial ratios and metrics records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_monitor_financial_ratios_and_metrics", "rar_sha256": "91eab69ca4d7eb872d578353b8e4bfd51981e8697ffbf75d8d02328a75a12af5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_monitor_financial_ratios_and_metrics_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-monitor-financial-ratios-and-metrics:d4fcb3c4edd383a6afe47774ab0d4b29e0059ffe427ba8c8c0c4d4275dbaa1a6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_monitor_financial_ratios_and_metrics`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_monitor_financial_ratios_and_metrics_agent.py` is
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
