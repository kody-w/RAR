---
name: "rar-cowork-cookbook-ppt-exec-process-customer-payments"
description: "Generates an executive-ready PowerPoint deck on process customer payments status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_customer_payments", "rar_sha256": "6a244c16b24ea46f087ea46d6c0b2b720950c9e06649990d39477ae13c68359e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_process_customer_payments_agent.py` and embedded as the fenced Python below (sha256 6a244c16b24ea46f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_process_customer_payments_agent.py` first:

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
    "version": '2.0.0',
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
