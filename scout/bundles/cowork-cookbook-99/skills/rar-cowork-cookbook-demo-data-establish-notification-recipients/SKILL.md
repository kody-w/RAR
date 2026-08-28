---
name: "rar-cowork-cookbook-demo-data-establish-notification-recipients"
description: "Generates and creates realistic demo records for establish notification recipients in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_establish_notification_recipients", "rar_sha256": "cb6114045d6e9abf91d857a2d8e3085f7b44616d2bc77ec9816734b485c5be0e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_establish_notification_recipients`. The original RAPP
agent is preserved byte-for-byte in `demo_data_establish_notification_recipients_agent.py` and in the RCI capsule.

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

Establish notification recipients Demo Data Generator — Generates and creates realistic demo records for establish notification recipients in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-establish-notification-recipients
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_establish_notification_recipients_agent.py` and embedded as the fenced Python below (sha256 cb6114045d6e9abf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_establish_notification_recipients_agent.py` first:

```bash
python3 demo_data_establish_notification_recipients_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_establish_notification_recipients_agent.py   # or on stdin
python3 demo_data_establish_notification_recipients_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish notification recipients Demo Data Generator — Generates and creates realistic demo records for establish notification recipients in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-establish-notification-recipients
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_establish_notification_recipients',
    "version": '2.0.1',
    "display_name": 'Establish notification recipients Demo Data Generator',
    "description": 'Generates and creates realistic demo records for establish notification recipients in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-establish-notification-recipients',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-establish-notification-recipients',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c7507630b6d3dfb1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/establish-notification-recipients'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-establish-notification-recipients', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataEstablishNotificationRecipients(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataEstablishNotificationRecipients'
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
    print(DemoDataEstablishNotificationRecipients().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
