---
name: "rar-cowork-cookbook-scheduled-brief-report-quality-test-results"
description: "Schedulable morning-brief email summarizing report quality test results for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_report_quality_test_results", "rar_sha256": "b296cf9ae1918e6e10024a61df1dc0796512203c114965a94c007bc7633cf339", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_report_quality_test_results`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_report_quality_test_results_agent.py` and in the RCI capsule.

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

Report quality test results Scheduled Email Brief — Schedulable morning-brief email summarizing report quality test results for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-report-quality-test-results
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_report_quality_test_results_agent.py` and embedded as the fenced Python below (sha256 b296cf9ae1918e6e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_report_quality_test_results_agent.py` first:

```bash
python3 scheduled_brief_report_quality_test_results_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_report_quality_test_results_agent.py   # or on stdin
python3 scheduled_brief_report_quality_test_results_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report quality test results Scheduled Email Brief — Schedulable morning-brief email summarizing report quality test results for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-report-quality-test-results
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_report_quality_test_results',
    "version": '2.0.0',
    "display_name": 'Report quality test results Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing report quality test results for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-report-quality-test-results',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-report-quality-test-results',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '53a68ce91ec68f40',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/control-production-quality/report-quality-test-results'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/scheduled-brief-report-quality-test-results', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefReportQualityTestResults(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefReportQualityTestResults'
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
    print(ScheduledBriefReportQualityTestResults().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
