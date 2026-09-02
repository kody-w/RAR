---
name: "rar-cowork-cookbook-teams-update-record-employee-absences"
description: "Drafts a Teams channel post on record employee absences status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_record_employee_absences", "rar_sha256": "cdfe5509246f7ec2101b0e3080e0335974c349cae8ffd0ecc16877ff8bcf1f8c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_record_employee_absences_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-record-employee-absences:b513f1e368b61809a538e0d7267e837142f0ed38a520e1f0b41f850fe70adafc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_record_employee_absences`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_record_employee_absences_agent.py` is
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
