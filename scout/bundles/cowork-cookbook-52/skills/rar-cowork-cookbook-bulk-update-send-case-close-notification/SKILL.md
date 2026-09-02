---
name: "rar-cowork-cookbook-bulk-update-send-case-close-notification"
description: "Applies a bulk field update across send case close notification records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_send_case_close_notification", "rar_sha256": "af92f54b1b85eca73b7e0781b113c32b405db6d641d1a0271010d589af703fcf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_send_case_close_notification_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-send-case-close-notification:7fc2b87c3b620265c78a666b2af965ceea59841485283ac3d7f48200883a1dbf", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_send_case_close_notification`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_send_case_close_notification_agent.py` is
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

Send case close notification Bulk Field Update — Applies a bulk field update across send case close notification records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-send-case-close-notification
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_send_case_close_notification_agent.py` and embedded as the fenced Python below (sha256 af92f54b1b85eca7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_send_case_close_notification_agent.py` first:

```bash
python3 bulk_update_send_case_close_notification_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_send_case_close_notification_agent.py   # or on stdin
python3 bulk_update_send_case_close_notification_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send case close notification Bulk Field Update — Applies a bulk field update across send case close notification records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-send-case-close-notification
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_send_case_close_notification',
    "version": '2.0.0',
    "display_name": 'Send case close notification Bulk Field Update',
    "description": 'Applies a bulk field update across send case close notification records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-send-case-close-notification',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-send-case-close-notification',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0c213e5b0e57c558',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/send-case-close-notification'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/bulk-update-send-case-close-notification', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateSendCaseCloseNotification(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateSendCaseCloseNotification'
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
    print(BulkUpdateSendCaseCloseNotification().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
