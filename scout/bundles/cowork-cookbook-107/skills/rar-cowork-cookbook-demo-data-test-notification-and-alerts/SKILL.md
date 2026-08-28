---
name: "rar-cowork-cookbook-demo-data-test-notification-and-alerts"
description: "Generates and creates realistic demo records for test notification and alerts in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_test_notification_and_alerts", "rar_sha256": "a024557b828c48460928ff13d046e94f7bcf4a674cf79aaf256c73e1dea42b76", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_test_notification_and_alerts_agent.py` and embedded as the fenced Python below (sha256 a024557b828c4846…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_test_notification_and_alerts_agent.py` first:

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
    "version": '2.0.1',
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
