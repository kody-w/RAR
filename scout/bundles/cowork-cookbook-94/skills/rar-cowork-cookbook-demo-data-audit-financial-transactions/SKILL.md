---
name: "rar-cowork-cookbook-demo-data-audit-financial-transactions"
description: "Generates and creates realistic demo records for audit financial transactions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_financial_transactions", "rar_sha256": "a3cd84fde64eed7729be6bcb077404f10078723d5a7a85499623e59d81338668", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_audit_financial_transactions`. The original RAPP
agent is preserved byte-for-byte in `demo_data_audit_financial_transactions_agent.py` and in the RCI capsule.

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

Audit financial transactions Demo Data Generator — Generates and creates realistic demo records for audit financial transactions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_audit_financial_transactions_agent.py` and embedded as the fenced Python below (sha256 a3cd84fde64eed77…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_audit_financial_transactions_agent.py` first:

```bash
python3 demo_data_audit_financial_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_audit_financial_transactions_agent.py   # or on stdin
python3 demo_data_audit_financial_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit financial transactions Demo Data Generator — Generates and creates realistic demo records for audit financial transactions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-audit-financial-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_audit_financial_transactions',
    "version": '2.0.1',
    "display_name": 'Audit financial transactions Demo Data Generator',
    "description": 'Generates and creates realistic demo records for audit financial transactions in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-audit-financial-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-audit-financial-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '771b798ab6e1987a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/audit-financial-transactions'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-audit-financial-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataAuditFinancialTransactions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAuditFinancialTransactions'
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
    print(DemoDataAuditFinancialTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
