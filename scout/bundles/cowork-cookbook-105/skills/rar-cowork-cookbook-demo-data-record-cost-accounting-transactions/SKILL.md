---
name: "rar-cowork-cookbook-demo-data-record-cost-accounting-transactions"
description: "Generates and creates realistic demo records for record cost accounting transactions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_cost_accounting_transactions", "rar_sha256": "3d1a3aee030a4715dedbb8e4d340836d343ee8b81b79c2106174ff93a88c0f05", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_record_cost_accounting_transactions`. The original RAPP
agent is preserved byte-for-byte in `demo_data_record_cost_accounting_transactions_agent.py` and in the RCI capsule.

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

Record cost accounting transactions Demo Data Generator — Generates and creates realistic demo records for record cost accounting transactions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-cost-accounting-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_record_cost_accounting_transactions_agent.py` and embedded as the fenced Python below (sha256 3d1a3aee030a4715…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_record_cost_accounting_transactions_agent.py` first:

```bash
python3 demo_data_record_cost_accounting_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_record_cost_accounting_transactions_agent.py   # or on stdin
python3 demo_data_record_cost_accounting_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record cost accounting transactions Demo Data Generator — Generates and creates realistic demo records for record cost accounting transactions in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-record-cost-accounting-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_record_cost_accounting_transactions',
    "version": '2.0.1',
    "display_name": 'Record cost accounting transactions Demo Data Generator',
    "description": 'Generates and creates realistic demo records for record cost accounting transactions in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-record-cost-accounting-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-record-cost-accounting-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1eda8307a3ec9746',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-cost-accounting-transactions'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-record-cost-accounting-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataRecordCostAccountingTransactions(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRecordCostAccountingTransactions'
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
    print(DemoDataRecordCostAccountingTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
