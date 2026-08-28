---
name: "rar-cowork-cookbook-adaptive-card-identify-notification-triggers"
description: "Produces a reusable Adaptive Card JSON snapshot of identify notification triggers status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_notification_triggers", "rar_sha256": "6e58cac74c8e2897237cc6a855305ca2887d75a5a7d77b45f8953a6effd692a2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_notification_triggers_agent.py` and embedded as the fenced Python below (sha256 6e58cac74c8e2897…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_notification_triggers_agent.py` first:

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
    "version": '2.0.1',
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
