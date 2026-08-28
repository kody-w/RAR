---
name: "rar-cowork-cookbook-bulk-update-define-notification-channels"
description: "Applies a bulk field update across define notification channels records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_notification_channels", "rar_sha256": "c3028f56d0774d89587355f2721108c145062596f1b08505957d74242f14fa07", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_define_notification_channels_agent.py` and embedded as the fenced Python below (sha256 c3028f56d0774d89…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_define_notification_channels_agent.py` first:

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
    "version": '2.0.1',
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
