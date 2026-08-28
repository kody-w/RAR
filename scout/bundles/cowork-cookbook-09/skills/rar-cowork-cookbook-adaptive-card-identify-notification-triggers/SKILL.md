---
name: "rar-cowork-cookbook-adaptive-card-identify-notification-triggers"
description: "Produces a reusable Adaptive Card JSON snapshot of identify notification triggers status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_notification_triggers", "rar_sha256": "2eb1c80c376e8faa18ce66d4216d0440c90e844d69dc14acbcf5cab2089319df", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_identify_notification_triggers`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_identify_notification_triggers_agent.py` and in the RCI capsule.

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

Identify notification triggers Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify notification triggers status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-notification-triggers
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_notification_triggers_agent.py` and embedded as the fenced Python below (sha256 2eb1c80c376e8faa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_notification_triggers_agent.py` first:

```bash
python3 adaptive_card_identify_notification_triggers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_notification_triggers_agent.py   # or on stdin
python3 adaptive_card_identify_notification_triggers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify notification triggers Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify notification triggers status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-notification-triggers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_notification_triggers',
    "version": '2.0.0',
    "display_name": 'Identify notification triggers Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of identify notification triggers status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-identify-notification-triggers',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-notification-triggers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c62844be20012103',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/identify-notification-triggers'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-identify-notification-triggers', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardIdentifyNotificationTriggers(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyNotificationTriggers'
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
    print(AdaptiveCardIdentifyNotificationTriggers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
