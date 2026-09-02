---
name: "rar-cowork-cookbook-bulk-update-report-on-and-analyze-trends"
description: "Applies a bulk field update across report on and analyze trends records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_report_on_and_analyze_trends", "rar_sha256": "1945c540d71d1b8e36020943b9c5a261ce72ac8aa28789653b420408bc5cb461", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_report_on_and_analyze_trends_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-report-on-and-analyze-trends:2f24523c7fdb1030a0b431f5577efb57b5c24a1e4697bfa141357f0ebb5381d5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_report_on_and_analyze_trends`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_report_on_and_analyze_trends_agent.py` is
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
