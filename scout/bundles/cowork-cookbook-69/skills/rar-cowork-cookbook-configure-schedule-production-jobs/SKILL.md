---
name: "rar-cowork-cookbook-configure-schedule-production-jobs"
description: "Applies a bulk configuration change to schedule production jobs from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_schedule_production_jobs", "rar_sha256": "57849381134500f585ff51c3acf9143f5bbb28793a1321547c78f77797001134", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_schedule_production_jobs_agent.py` and embedded as the fenced Python below (sha256 57849381134500f5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_schedule_production_jobs_agent.py` first:

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
    "version": '2.0.1',
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
