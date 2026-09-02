---
name: "rar-cowork-cookbook-teams-update-audit-workplace-for-safety"
description: "Drafts a Teams channel post on audit workplace for safety status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_audit_workplace_for_safety", "rar_sha256": "6977bb9398d2c392198b19c011bb6ed521695f6d8140d8e4daaa91151942ee15", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_audit_workplace_for_safety_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-audit-workplace-for-safety:131675fb8990beb42882e6141f78f8485085ed11f96a36a70b0f1e273eabc82e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_audit_workplace_for_safety`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_audit_workplace_for_safety_agent.py` is
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

Audit workplace for safety Teams Channel Update — Drafts a Teams channel post on audit workplace for safety status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-audit-workplace-for-safety
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_audit_workplace_for_safety_agent.py` and embedded as the fenced Python below (sha256 6977bb9398d2c392…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_audit_workplace_for_safety_agent.py` first:

```bash
python3 teams_update_audit_workplace_for_safety_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_audit_workplace_for_safety_agent.py   # or on stdin
python3 teams_update_audit_workplace_for_safety_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit workplace for safety Teams Channel Update — Drafts a Teams channel post on audit workplace for safety status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-audit-workplace-for-safety
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_audit_workplace_for_safety',
    "version": '2.0.0',
    "display_name": 'Audit workplace for safety Teams Channel Update',
    "description": 'Drafts a Teams channel post on audit workplace for safety status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-audit-workplace-for-safety',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-audit-workplace-for-safety',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd2975680680d6247',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/audit-workplace-for-safety'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/teams-update-audit-workplace-for-safety', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateAuditWorkplaceForSafety(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateAuditWorkplaceForSafety'
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
    print(TeamsUpdateAuditWorkplaceForSafety().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
