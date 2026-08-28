---
name: "rar-cowork-cookbook-teams-update-audit-workplace-for-safety"
description: "Drafts a Teams channel post on audit workplace for safety status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_audit_workplace_for_safety", "rar_sha256": "551de87387d6ae8681e39a49f7b554b736d5a2dca586a6e72572a299ae75563c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_audit_workplace_for_safety_agent.py` and embedded as the fenced Python below (sha256 551de87387d6ae86…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_audit_workplace_for_safety_agent.py` first:

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
    "version": '2.0.1',
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
