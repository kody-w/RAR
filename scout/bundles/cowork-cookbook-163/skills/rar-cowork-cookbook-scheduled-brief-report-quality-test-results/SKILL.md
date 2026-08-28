---
name: "rar-cowork-cookbook-scheduled-brief-report-quality-test-results"
description: "Schedulable morning-brief email summarizing report quality test results for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_report_quality_test_results", "rar_sha256": "f7915d238e96904b2e00dd5a38eb08b04abb866bf2663ebae6053f8cf6a27552", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_report_quality_test_results_agent.py` and embedded as the fenced Python below (sha256 f7915d238e96904b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_report_quality_test_results_agent.py` first:

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
    "version": '2.0.1',
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
