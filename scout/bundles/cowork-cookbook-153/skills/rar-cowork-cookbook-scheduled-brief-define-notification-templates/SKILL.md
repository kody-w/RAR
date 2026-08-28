---
name: "rar-cowork-cookbook-scheduled-brief-define-notification-templates"
description: "Schedulable morning-brief email summarizing define notification templates for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_notification_templates", "rar_sha256": "9e7be4ca5be4a89d7726e00865debb3d950dcb675edb163f416ff7f692058e7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_notification_templates_agent.py` and embedded as the fenced Python below (sha256 9e7be4ca5be4a89d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_notification_templates_agent.py` first:

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
    "version": '2.0.0',
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
