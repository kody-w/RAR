---
name: "rar-cowork-cookbook-adaptive-card-test-notification-and-alerts"
description: "Produces a reusable Adaptive Card JSON snapshot of test notification and alerts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_test_notification_and_alerts", "rar_sha256": "74e9e52418e815d6b82533f268d893c29a84691c0acfceca9479f89b119c1319", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_test_notification_and_alerts`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_test_notification_and_alerts_agent.py` and in the RCI capsule.

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

Test notification and alerts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of test notification and alerts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-test-notification-and-alerts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_test_notification_and_alerts_agent.py` and embedded as the fenced Python below (sha256 74e9e52418e815d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_test_notification_and_alerts_agent.py` first:

```bash
python3 adaptive_card_test_notification_and_alerts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_test_notification_and_alerts_agent.py   # or on stdin
python3 adaptive_card_test_notification_and_alerts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test notification and alerts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of test notification and alerts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-test-notification-and-alerts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_test_notification_and_alerts',
    "version": '2.0.0',
    "display_name": 'Test notification and alerts Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of test notification and alerts status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-test-notification-and-alerts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-test-notification-and-alerts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cfd08da755a920e5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/test-notification-and-alerts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-test-notification-and-alerts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardTestNotificationAndAlerts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardTestNotificationAndAlerts'
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
    print(AdaptiveCardTestNotificationAndAlerts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
