---
name: "rar-cowork-cookbook-configure-schedule-production-jobs"
description: "Applies a bulk configuration change to schedule production jobs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_schedule_production_jobs", "rar_sha256": "d927ca5086ae828524e70c8bed9cf5ffaf54eaa8131ad9e471f64ddb439478b3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_schedule_production_jobs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-schedule-production-jobs:da41f74c0d7f607f452a09cf0bb002a68ca6c6db38a7ae48670a08f9bd4ffb52", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_schedule_production_jobs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_schedule_production_jobs_agent.py` is
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

Schedule production jobs Configuration Bulk Setup — Applies a bulk configuration change to schedule production jobs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-schedule-production-jobs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_schedule_production_jobs_agent.py` and embedded as the fenced Python below (sha256 d927ca5086ae8285…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_schedule_production_jobs_agent.py` first:

```bash
python3 configure_schedule_production_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_schedule_production_jobs_agent.py   # or on stdin
python3 configure_schedule_production_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Schedule production jobs Configuration Bulk Setup — Applies a bulk configuration change to schedule production jobs from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-schedule-production-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_schedule_production_jobs',
    "version": '2.0.0',
    "display_name": 'Schedule production jobs Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to schedule production jobs from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-schedule-production-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-schedule-production-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '28f601979b788056',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/plan-production-operations/schedule-production-jobs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/configure-schedule-production-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow', 'word:schedule'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureScheduleProductionJobs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureScheduleProductionJobs'
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
    print(ConfigureScheduleProductionJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
