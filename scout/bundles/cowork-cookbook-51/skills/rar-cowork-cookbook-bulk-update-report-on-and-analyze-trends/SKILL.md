---
name: "rar-cowork-cookbook-bulk-update-report-on-and-analyze-trends"
description: "Applies a bulk field update across report on and analyze trends records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_report_on_and_analyze_trends", "rar_sha256": "1945c540d71d1b8e36020943b9c5a261ce72ac8aa28789653b420408bc5cb461", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_report_on_and_analyze_trends_agent.py` and embedded as the fenced Python below (sha256 1945c540d71d1b8e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_report_on_and_analyze_trends_agent.py` first:

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
    "version": '2.0.0',
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
