---
name: "rar-cowork-cookbook-bulk-update-send-case-close-notification"
description: "Applies a bulk field update across send case close notification records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_send_case_close_notification", "rar_sha256": "af92f54b1b85eca73b7e0781b113c32b405db6d641d1a0271010d589af703fcf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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
