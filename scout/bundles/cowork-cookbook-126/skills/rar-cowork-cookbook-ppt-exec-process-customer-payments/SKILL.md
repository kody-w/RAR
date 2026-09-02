---
name: "rar-cowork-cookbook-ppt-exec-process-customer-payments"
description: "Generates an executive-ready PowerPoint deck on process customer payments status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_process_customer_payments", "rar_sha256": "6a244c16b24ea46f087ea46d6c0b2b720950c9e06649990d39477ae13c68359e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_process_customer_payments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-process-customer-payments:1591b0ca25251d17745773ba8c9429b7646ca77e28e3638655b05ed3a1b19e4a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_process_customer_payments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_process_customer_payments_agent.py` is
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
