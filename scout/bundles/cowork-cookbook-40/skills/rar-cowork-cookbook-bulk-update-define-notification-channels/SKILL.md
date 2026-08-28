---
name: "rar-cowork-cookbook-bulk-update-define-notification-channels"
description: "Applies a bulk field update across define notification channels records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_notification_channels", "rar_sha256": "3b0c08f52f8d4d2939c9f806ce63cc66dab4adca7793405e0e1e2686f4cb3813", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_define_notification_channels`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_define_notification_channels_agent.py` and in the RCI capsule.

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

Define notification channels Bulk Field Update — Applies a bulk field update across define notification channels records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-notification-channels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_notification_channels_agent.py` and embedded as the fenced Python below (sha256 3b0c08f52f8d4d29…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_notification_channels_agent.py` first:

```bash
python3 bulk_update_define_notification_channels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_define_notification_channels_agent.py   # or on stdin
python3 bulk_update_define_notification_channels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define notification channels Bulk Field Update — Applies a bulk field update across define notification channels records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-define-notification-channels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_define_notification_channels',
    "version": '2.0.0',
    "display_name": 'Define notification channels Bulk Field Update',
    "description": 'Applies a bulk field update across define notification channels records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-define-notification-channels',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-define-notification-channels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aff9310f89ea6e0d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/define-notification-channels'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-define-notification-channels', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDefineNotificationChannels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDefineNotificationChannels'
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
    print(BulkUpdateDefineNotificationChannels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
