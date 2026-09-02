---
name: "rar-cowork-cookbook-adaptive-card-identify-notification-triggers"
description: "Produces a reusable Adaptive Card JSON snapshot of identify notification triggers status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_notification_triggers", "rar_sha256": "2eb1c80c376e8faa18ce66d4216d0440c90e844d69dc14acbcf5cab2089319df", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_identify_notification_triggers_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-identify-notification-triggers:d97b06fc32ff7d3314dd123f443724df7cdc3409bddd65124c57a4ce30f8beee", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_identify_notification_triggers`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_identify_notification_triggers_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_notification_triggers_agent.py` and embedded as the fenced Python below (sha256 2eb1c80c376e8faa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_notification_triggers_agent.py` first:

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
    "version": '2.0.0',
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
