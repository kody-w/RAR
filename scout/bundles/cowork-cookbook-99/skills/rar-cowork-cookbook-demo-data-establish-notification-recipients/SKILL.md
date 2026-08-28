---
name: "rar-cowork-cookbook-demo-data-establish-notification-recipients"
description: "Generates and creates realistic demo records for establish notification recipients in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_establish_notification_recipients", "rar_sha256": "b841835a513a423dfdb0db54452a4137e9638b972e17340ac18596b410efdba6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_establish_notification_recipients_agent.py` and embedded as the fenced Python below (sha256 b841835a513a423d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_establish_notification_recipients_agent.py` first:

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
    "version": '2.0.0',
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
