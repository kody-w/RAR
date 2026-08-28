---
name: "rar-cowork-cookbook-ppt-exec-send-notification-to-customer"
description: "Generates an executive-ready PowerPoint deck on send notification to customer status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_send_notification_to_customer", "rar_sha256": "c5e040bae90f1e06b92ff1d9f36a83e2cc3ec28a12908d451097836859ba9f1b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_send_notification_to_customer_agent.py` and embedded as the fenced Python below (sha256 c5e040bae90f1e06…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_send_notification_to_customer_agent.py` first:

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
    "version": '2.0.1',
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
