---
name: "rar-cowork-cookbook-scheduled-brief-report-quality-test-results"
description: "Schedulable morning-brief email summarizing report quality test results for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_report_quality_test_results", "rar_sha256": "b296cf9ae1918e6e10024a61df1dc0796512203c114965a94c007bc7633cf339", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_report_quality_test_results_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-report-quality-test-results:b1a83274a78ce14c5b255d648ed6bbbacf2e2d32e9cbe8296a2d488d23fb304e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_report_quality_test_results`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_report_quality_test_results_agent.py` is
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
