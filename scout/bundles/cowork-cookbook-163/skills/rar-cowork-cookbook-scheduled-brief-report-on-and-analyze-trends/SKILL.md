---
name: "rar-cowork-cookbook-scheduled-brief-report-on-and-analyze-trends"
description: "Schedulable morning-brief email summarizing report on and analyze trends for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_report_on_and_analyze_trends", "rar_sha256": "cec9479270393e8c609546c361980ed24b10ba807b4f10ca12c3ba8e51209025", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_report_on_and_analyze_trends`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_report_on_and_analyze_trends_agent.py` and in the RCI capsule.

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
