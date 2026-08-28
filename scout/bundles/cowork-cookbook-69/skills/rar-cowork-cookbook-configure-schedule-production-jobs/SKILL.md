---
name: "rar-cowork-cookbook-configure-schedule-production-jobs"
description: "Applies a bulk configuration change to schedule production jobs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_schedule_production_jobs", "rar_sha256": "d927ca5086ae828524e70c8bed9cf5ffaf54eaa8131ad9e471f64ddb439478b3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_schedule_production_jobs`. The original RAPP
agent is preserved byte-for-byte in `configure_schedule_production_jobs_agent.py` and in the RCI capsule.

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
