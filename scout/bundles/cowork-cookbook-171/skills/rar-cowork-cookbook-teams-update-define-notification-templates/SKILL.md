---
name: "rar-cowork-cookbook-teams-update-define-notification-templates"
description: "Drafts a Teams channel post on define notification templates status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_notification_templates", "rar_sha256": "e5665b7bc9bd947c9722eb48a52d705f3be268dbbe5b6c6d24d86a041e53f3f3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_notification_templates_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-notification-templates:e726a86bbf8d8d3685a542c9ab84fbba8a2f7f8201e6db8a22cb2cf29558d645", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_notification_templates`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_notification_templates_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_notification_templates_agent.py` and embedded as the fenced Python below (sha256 e5665b7bc9bd947c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_notification_templates_agent.py` first:

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
    "version": '2.0.0',
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
