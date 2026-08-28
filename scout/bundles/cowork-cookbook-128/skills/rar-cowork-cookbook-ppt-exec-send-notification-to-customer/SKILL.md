---
name: "rar-cowork-cookbook-ppt-exec-send-notification-to-customer"
description: "Generates an executive-ready PowerPoint deck on send notification to customer status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_send_notification_to_customer", "rar_sha256": "86cb0121d9c8ef46c7cc3705465e1b5fbe7ea8ddaa6ab4d86d62b7c031bde44c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_send_notification_to_customer`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_send_notification_to_customer_agent.py` and in the RCI capsule.

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

Send notification to customer Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on send notification to customer status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-send-notification-to-customer
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_send_notification_to_customer_agent.py` and embedded as the fenced Python below (sha256 86cb0121d9c8ef46…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_send_notification_to_customer_agent.py` first:

```bash
python3 ppt_exec_send_notification_to_customer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_send_notification_to_customer_agent.py   # or on stdin
python3 ppt_exec_send_notification_to_customer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Send notification to customer Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on send notification to customer status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-send-notification-to-customer
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_send_notification_to_customer',
    "version": '2.0.0',
    "display_name": 'Send notification to customer Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on send notification to customer status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-send-notification-to-customer',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-send-notification-to-customer',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '61bf5fbebc6bac2e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/send-notification-to-customer'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-send-notification-to-customer', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecSendNotificationToCustomer(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecSendNotificationToCustomer'
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
    print(PptExecSendNotificationToCustomer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
