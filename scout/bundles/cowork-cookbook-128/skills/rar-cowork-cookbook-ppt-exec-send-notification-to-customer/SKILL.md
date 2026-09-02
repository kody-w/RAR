---
name: "rar-cowork-cookbook-ppt-exec-send-notification-to-customer"
description: "Generates an executive-ready PowerPoint deck on send notification to customer status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_send_notification_to_customer", "rar_sha256": "86cb0121d9c8ef46c7cc3705465e1b5fbe7ea8ddaa6ab4d86d62b7c031bde44c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_send_notification_to_customer_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-send-notification-to-customer:867c8c6e5c368730c80786ff889a1d52d9ec7ac3be6800c7a51f02f2c5473c7a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_send_notification_to_customer`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_send_notification_to_customer_agent.py` is
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
