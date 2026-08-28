---
name: "rar-cowork-cookbook-teams-update-record-employee-absences"
description: "Drafts a Teams channel post on record employee absences status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_record_employee_absences", "rar_sha256": "cdfe5509246f7ec2101b0e3080e0335974c349cae8ffd0ecc16877ff8bcf1f8c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_record_employee_absences`. The original RAPP
agent is preserved byte-for-byte in `teams_update_record_employee_absences_agent.py` and in the RCI capsule.

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

Record employee absences Teams Channel Update — Drafts a Teams channel post on record employee absences status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-record-employee-absences
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_record_employee_absences_agent.py` and embedded as the fenced Python below (sha256 cdfe5509246f7ec2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_record_employee_absences_agent.py` first:

```bash
python3 teams_update_record_employee_absences_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_record_employee_absences_agent.py   # or on stdin
python3 teams_update_record_employee_absences_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record employee absences Teams Channel Update — Drafts a Teams channel post on record employee absences status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-record-employee-absences
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_record_employee_absences',
    "version": '2.0.0',
    "display_name": 'Record employee absences Teams Channel Update',
    "description": 'Drafts a Teams channel post on record employee absences status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-record-employee-absences',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-record-employee-absences',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '01960b195cc10dbf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/record-employee-absences'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-record-employee-absences', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateRecordEmployeeAbsences(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateRecordEmployeeAbsences'
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
    print(TeamsUpdateRecordEmployeeAbsences().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
