---
name: "rar-cowork-cookbook-adaptive-card-test-notification-and-alerts"
description: "Produces a reusable Adaptive Card JSON snapshot of test notification and alerts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_test_notification_and_alerts", "rar_sha256": "74e9e52418e815d6b82533f268d893c29a84691c0acfceca9479f89b119c1319", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_test_notification_and_alerts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-test-notification-and-alerts:f8b97dc4d95c378dbe6e1bf93a8aa68a1541d3fb01074812a632b692eaf6bfea", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_test_notification_and_alerts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_test_notification_and_alerts_agent.py` is
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
