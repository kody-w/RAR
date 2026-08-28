---
name: "rar-cowork-cookbook-demo-data-test-notification-and-alerts"
description: "Generates and creates realistic demo records for test notification and alerts in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_test_notification_and_alerts", "rar_sha256": "d253a58f57a0bcec87a460bc7057488591da7426c5d5cc9ee948d2ea767a318d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_test_notification_and_alerts`. The original RAPP
agent is preserved byte-for-byte in `demo_data_test_notification_and_alerts_agent.py` and in the RCI capsule.

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

Test notification and alerts Demo Data Generator — Generates and creates realistic demo records for test notification and alerts in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-test-notification-and-alerts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_test_notification_and_alerts_agent.py` and embedded as the fenced Python below (sha256 d253a58f57a0bcec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_test_notification_and_alerts_agent.py` first:

```bash
python3 demo_data_test_notification_and_alerts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_test_notification_and_alerts_agent.py   # or on stdin
python3 demo_data_test_notification_and_alerts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test notification and alerts Demo Data Generator — Generates and creates realistic demo records for test notification and alerts in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-test-notification-and-alerts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_test_notification_and_alerts',
    "version": '2.0.0',
    "display_name": 'Test notification and alerts Demo Data Generator',
    "description": 'Generates and creates realistic demo records for test notification and alerts in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-test-notification-and-alerts',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-test-notification-and-alerts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '97106cdde10f4bbb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/test-notification-and-alerts'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-test-notification-and-alerts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataTestNotificationAndAlerts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataTestNotificationAndAlerts'
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
    print(DemoDataTestNotificationAndAlerts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
