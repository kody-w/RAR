---
name: "rar-cowork-cookbook-scheduled-brief-send-case-close-notification"
description: "Schedulable morning-brief email summarizing send case close notification for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_send_case_close_notification", "rar_sha256": "a241fbbd3657d393986fb6105e54060daa3061296bb2ccb3b5204cb3762e1143", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_send_case_close_notification`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_send_case_close_notification_agent.py` and in the RCI capsule.

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

Send case close notification Scheduled Email Brief — Schedulable morning-brief email summarizing send case close notification for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-send-case-close-notification
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_send_case_close_notification_agent.py` and embedded as the fenced Python below (sha256 a241fbbd3657d393…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_send_case_close_notification_agent.py` first:

```bash
python3 scheduled_brief_send_case_close_notification_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_send_case_close_notification_agent.py   # or on stdin
python3 scheduled_brief_send_case_close_notification_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send case close notification Scheduled Email Brief — Schedulable morning-brief email summarizing send case close notification for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-send-case-close-notification
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_send_case_close_notification',
    "version": '2.0.1',
    "display_name": 'Send case close notification Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing send case close notification for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-send-case-close-notification',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-send-case-close-notification',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '90574b1db3f34fd9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/send-case-close-notification'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-send-case-close-notification', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefSendCaseCloseNotification(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefSendCaseCloseNotification'
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
    print(ScheduledBriefSendCaseCloseNotification().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
