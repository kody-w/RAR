---
name: "rar-cowork-cookbook-teams-update-define-notification-templates"
description: "Drafts a Teams channel post on define notification templates status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_notification_templates", "rar_sha256": "4f4ad8b3ecf12e3b6de3666974396fb91642fe2747960c8c6f53afb8010b2525", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_notification_templates`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_notification_templates_agent.py` and in the RCI capsule.

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

Define notification templates Teams Channel Update — Drafts a Teams channel post on define notification templates status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-notification-templates
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_notification_templates_agent.py` and embedded as the fenced Python below (sha256 4f4ad8b3ecf12e3b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_notification_templates_agent.py` first:

```bash
python3 teams_update_define_notification_templates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_notification_templates_agent.py   # or on stdin
python3 teams_update_define_notification_templates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define notification templates Teams Channel Update — Drafts a Teams channel post on define notification templates status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-notification-templates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_notification_templates',
    "version": '2.0.1',
    "display_name": 'Define notification templates Teams Channel Update',
    "description": 'Drafts a Teams channel post on define notification templates status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-notification-templates',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-notification-templates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4f6d3c36cfa81a1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/define-notification-templates'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-define-notification-templates', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateDefineNotificationTemplates(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineNotificationTemplates'
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
    print(TeamsUpdateDefineNotificationTemplates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
