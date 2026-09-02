---
name: "rar-cowork-cookbook-demo-data-test-notification-and-alerts"
description: "Generates and creates realistic demo records for test notification and alerts in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_test_notification_and_alerts", "rar_sha256": "d253a58f57a0bcec87a460bc7057488591da7426c5d5cc9ee948d2ea767a318d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_test_notification_and_alerts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-test-notification-and-alerts:5a1e9a73ebfb8ca346f72bc3b6b9a3e2c28fc06ebf58ee4f611c1d79e7d14d83", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_test_notification_and_alerts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_test_notification_and_alerts_agent.py` is
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
