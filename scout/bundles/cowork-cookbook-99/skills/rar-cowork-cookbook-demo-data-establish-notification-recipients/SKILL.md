---
name: "rar-cowork-cookbook-demo-data-establish-notification-recipients"
description: "Generates and creates realistic demo records for establish notification recipients in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_establish_notification_recipients", "rar_sha256": "b841835a513a423dfdb0db54452a4137e9638b972e17340ac18596b410efdba6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_establish_notification_recipients_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-establish-notification-recipients:dd95798d603a6afdaea5ab13c3a063f014f940f359a3420aab7729db812df2a1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_establish_notification_recipients`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_establish_notification_recipients_agent.py` is
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
