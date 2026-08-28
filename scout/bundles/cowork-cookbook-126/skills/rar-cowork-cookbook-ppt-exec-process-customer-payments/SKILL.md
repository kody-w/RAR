---
name: "rar-cowork-cookbook-ppt-exec-process-customer-payments"
description: "Generates an executive-ready PowerPoint deck on process customer payments status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_customer_payments", "rar_sha256": "df95d0ad6b8c69b17e17b6339380eb9390fcb10821f2585ad79c69a5f3fa39bd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_process_customer_payments`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_process_customer_payments_agent.py` and in the RCI capsule.

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

Process customer payments Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on process customer payments status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-process-customer-payments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_process_customer_payments_agent.py` and embedded as the fenced Python below (sha256 df95d0ad6b8c69b1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_process_customer_payments_agent.py` first:

```bash
python3 ppt_exec_process_customer_payments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_process_customer_payments_agent.py   # or on stdin
python3 ppt_exec_process_customer_payments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process customer payments Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on process customer payments status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-process-customer-payments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_process_customer_payments',
    "version": '2.0.1',
    "display_name": 'Process customer payments Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on process customer payments status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'ppt-exec-process-customer-payments',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-process-customer-payments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5dbc0067da4de41b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-accounts-receivable/process-customer-payments'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/ppt-exec-process-customer-payments', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecProcessCustomerPayments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecProcessCustomerPayments'
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
    print(PptExecProcessCustomerPayments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
