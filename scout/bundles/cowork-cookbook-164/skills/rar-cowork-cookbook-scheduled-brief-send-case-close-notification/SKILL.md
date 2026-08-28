---
name: "rar-cowork-cookbook-scheduled-brief-send-case-close-notification"
description: "Schedulable morning-brief email summarizing send case close notification for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_send_case_close_notification", "rar_sha256": "0bb76737f05b5718d7c862553aa1f42a68a5534f68e7f73f0b6be468713e1dc0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_send_case_close_notification_agent.py` and embedded as the fenced Python below (sha256 0bb76737f05b5718…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_send_case_close_notification_agent.py` first:

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
    "version": '2.0.0',
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
