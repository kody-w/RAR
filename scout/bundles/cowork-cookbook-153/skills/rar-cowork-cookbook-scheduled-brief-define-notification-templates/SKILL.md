---
name: "rar-cowork-cookbook-scheduled-brief-define-notification-templates"
description: "Schedulable morning-brief email summarizing define notification templates for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_notification_templates", "rar_sha256": "5ab4c063d6d0a958f41b38c6c5eb3a17f1d59ab1fd7e8d6bb363df62fcd79eda", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_notification_templates`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_notification_templates_agent.py` and in the RCI capsule.

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

Define notification templates Scheduled Email Brief — Schedulable morning-brief email summarizing define notification templates for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-notification-templates
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_notification_templates_agent.py` and embedded as the fenced Python below (sha256 5ab4c063d6d0a958…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_notification_templates_agent.py` first:

```bash
python3 scheduled_brief_define_notification_templates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_notification_templates_agent.py   # or on stdin
python3 scheduled_brief_define_notification_templates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define notification templates Scheduled Email Brief — Schedulable morning-brief email summarizing define notification templates for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-notification-templates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_notification_templates',
    "version": '2.0.1',
    "display_name": 'Define notification templates Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define notification templates for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-notification-templates',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-notification-templates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '79ffc936993649c8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/define-notification-templates'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-define-notification-templates', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDefineNotificationTemplates(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineNotificationTemplates'
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
    print(ScheduledBriefDefineNotificationTemplates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
