---
name: "rar-cowork-cookbook-report-schedule-production-jobs"
description: "Builds a structured summary report of schedule production jobs activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_schedule_production_jobs", "rar_sha256": "64bbdd9516a7dc06fe92a2071c7b03e21bb7f90c262e5ca4e4753ef09401a419", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_schedule_production_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-schedule-production-jobs:abc77791edacc85f029c1758469e96fe905cd4782c34a374bdaf0bde86345515", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_schedule_production_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_schedule_production_jobs_agent.py` is
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
