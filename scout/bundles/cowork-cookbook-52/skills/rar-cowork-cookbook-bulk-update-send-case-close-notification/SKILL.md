---
name: "rar-cowork-cookbook-bulk-update-send-case-close-notification"
description: "Applies a bulk field update across send case close notification records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_send_case_close_notification", "rar_sha256": "b7c45437436ec4fe02cb4f8c0f88906fe3f6dad90c0238b5af0b39995853d6d2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/bulk_update_send_case_close_notification`. The original RAPP
agent is preserved byte-for-byte in `bulk_update_send_case_close_notification_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_send_case_close_notification_agent.py` and embedded as the fenced Python below (sha256 b7c45437436ec4fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_send_case_close_notification_agent.py` first:

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
    "version": '2.0.1',
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
