---
name: "rar-cowork-cookbook-adaptive-card-test-notification-and-alerts"
description: "Produces a reusable Adaptive Card JSON snapshot of test notification and alerts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_test_notification_and_alerts", "rar_sha256": "7dec299171fe0e70234ab1acb3c5a1e394b2e4892d48fa17df1993b74569dfe9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_test_notification_and_alerts_agent.py` and embedded as the fenced Python below (sha256 7dec299171fe0e70…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_test_notification_and_alerts_agent.py` first:

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
    "version": '2.0.1',
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
