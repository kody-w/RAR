---
name: "rar-cowork-cookbook-bulk-update-define-notification-channels"
description: "Applies a bulk field update across define notification channels records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_define_notification_channels", "rar_sha256": "3b0c08f52f8d4d2939c9f806ce63cc66dab4adca7793405e0e1e2686f4cb3813", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_define_notification_channels_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-define-notification-channels:fab2b535fad184f71580bc4021279361162dcd60e37d480a02a0f3e703121700", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_define_notification_channels`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_define_notification_channels_agent.py` is
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
