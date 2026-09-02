---
name: "rar-cowork-cookbook-scheduled-brief-report-on-and-analyze-trends"
description: "Schedulable morning-brief email summarizing report on and analyze trends for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_report_on_and_analyze_trends", "rar_sha256": "cec9479270393e8c609546c361980ed24b10ba807b4f10ca12c3ba8e51209025", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_report_on_and_analyze_trends_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-report-on-and-analyze-trends:6a8da00677379d6341753315376ec7472a309d4e98aaa37340c4dd3ce47fbccb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_report_on_and_analyze_trends`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_report_on_and_analyze_trends_agent.py` is
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

Report on and analyze trends Scheduled Email Brief — Schedulable morning-brief email summarizing report on and analyze trends for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-report-on-and-analyze-trends
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_report_on_and_analyze_trends_agent.py` and embedded as the fenced Python below (sha256 cec9479270393e8c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_report_on_and_analyze_trends_agent.py` first:

```bash
python3 scheduled_brief_report_on_and_analyze_trends_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_report_on_and_analyze_trends_agent.py   # or on stdin
python3 scheduled_brief_report_on_and_analyze_trends_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report on and analyze trends Scheduled Email Brief — Schedulable morning-brief email summarizing report on and analyze trends for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-report-on-and-analyze-trends
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_report_on_and_analyze_trends',
    "version": '2.0.0',
    "display_name": 'Report on and analyze trends Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing report on and analyze trends for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-report-on-and-analyze-trends',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-report-on-and-analyze-trends',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2d4675d0d7a2fcd3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/report-on-and-analyze-trends'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/scheduled-brief-report-on-and-analyze-trends', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefReportOnAndAnalyzeTrends(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReportOnAndAnalyzeTrends'
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
    print(ScheduledBriefReportOnAndAnalyzeTrends().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
