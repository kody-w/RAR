---
name: "rar-cowork-cookbook-teams-update-audit-workplace-for-safety"
description: "Drafts a Teams channel post on audit workplace for safety status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_audit_workplace_for_safety", "rar_sha256": "6977bb9398d2c392198b19c011bb6ed521695f6d8140d8e4daaa91151942ee15", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_audit_workplace_for_safety`. The original RAPP
agent is preserved byte-for-byte in `teams_update_audit_workplace_for_safety_agent.py` and in the RCI capsule.

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
