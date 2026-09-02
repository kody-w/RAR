---
name: "rar-cowork-cookbook-teams-update-manage-accruals"
description: "Drafts a Teams channel post on manage accruals status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_manage_accruals", "rar_sha256": "0634902fb7ba457eeea18575c68304f36184799511838abc187527876a892d97", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_manage_accruals_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-manage-accruals:9aa05d6ca4ce00cffc5f5af9792c5df16b85599e16fd7ce713a7f861da94f6c2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_manage_accruals`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_manage_accruals_agent.py` is
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

Manage accruals Teams Channel Update — Drafts a Teams channel post on manage accruals status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-accruals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_manage_accruals_agent.py` and embedded as the fenced Python below (sha256 0634902fb7ba457e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_manage_accruals_agent.py` first:

```bash
python3 teams_update_manage_accruals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_manage_accruals_agent.py   # or on stdin
python3 teams_update_manage_accruals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage accruals Teams Channel Update — Drafts a Teams channel post on manage accruals status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-manage-accruals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_manage_accruals',
    "version": '2.0.0',
    "display_name": 'Manage accruals Teams Channel Update',
    "description": 'Drafts a Teams channel post on manage accruals status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'teams-update-manage-accruals',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-manage-accruals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '006824224e9350fc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/manage-accruals'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/teams-update-manage-accruals', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class TeamsUpdateManageAccruals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateManageAccruals'
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
    print(TeamsUpdateManageAccruals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
