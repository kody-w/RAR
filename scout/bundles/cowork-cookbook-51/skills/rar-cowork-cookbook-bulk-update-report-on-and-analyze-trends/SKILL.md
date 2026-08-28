---
name: "rar-cowork-cookbook-bulk-update-report-on-and-analyze-trends"
description: "Applies a bulk field update across report on and analyze trends records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_report_on_and_analyze_trends", "rar_sha256": "7bf7b8e8f451559c543a9adc9ac3f48f3cfcad04f59f132c4c392c94447b8184", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_report_on_and_analyze_trends`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_report_on_and_analyze_trends_agent.py` and in the RCI capsule.

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

Report on and analyze trends Bulk Field Update — Applies a bulk field update across report on and analyze trends records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-report-on-and-analyze-trends
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_report_on_and_analyze_trends_agent.py` and embedded as the fenced Python below (sha256 7bf7b8e8f451559c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_report_on_and_analyze_trends_agent.py` first:

```bash
python3 bulk_update_report_on_and_analyze_trends_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_report_on_and_analyze_trends_agent.py   # or on stdin
python3 bulk_update_report_on_and_analyze_trends_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on and analyze trends Bulk Field Update — Applies a bulk field update across report on and analyze trends records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-report-on-and-analyze-trends
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_report_on_and_analyze_trends',
    "version": '2.0.1',
    "display_name": 'Report on and analyze trends Bulk Field Update',
    "description": 'Applies a bulk field update across report on and analyze trends records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-report-on-and-analyze-trends',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-report-on-and-analyze-trends',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0d8d2a62bf54d13b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/report-on-and-analyze-trends'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-report-on-and-analyze-trends', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateReportOnAndAnalyzeTrends(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateReportOnAndAnalyzeTrends'
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
    print(BulkUpdateReportOnAndAnalyzeTrends().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
