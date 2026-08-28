---
name: "rar-cowork-cookbook-report-schedule-production-jobs"
description: "Builds a structured summary report of schedule production jobs activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_schedule_production_jobs", "rar_sha256": "64bbdd9516a7dc06fe92a2071c7b03e21bb7f90c262e5ca4e4753ef09401a419", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_schedule_production_jobs`. The original RAPP
agent is preserved byte-for-byte in `report_schedule_production_jobs_agent.py` and in the RCI capsule.

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

Schedule production jobs Summary Report — Builds a structured summary report of schedule production jobs activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-schedule-production-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_schedule_production_jobs_agent.py` and embedded as the fenced Python below (sha256 64bbdd9516a7dc06…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_schedule_production_jobs_agent.py` first:

```bash
python3 report_schedule_production_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_schedule_production_jobs_agent.py   # or on stdin
python3 report_schedule_production_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule production jobs Summary Report — Builds a structured summary report of schedule production jobs activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-schedule-production-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_schedule_production_jobs',
    "version": '2.0.0',
    "display_name": 'Schedule production jobs Summary Report',
    "description": 'Builds a structured summary report of schedule production jobs activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-schedule-production-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-schedule-production-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3ba76a74c8e9067a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/schedule-production-jobs'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-schedule-production-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.429, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ReportScheduleProductionJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportScheduleProductionJobs'
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
    print(ReportScheduleProductionJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
