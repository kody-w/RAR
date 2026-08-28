---
name: "rar-cowork-cookbook-demo-data-record-cost-accounting-transactions"
description: "Generates and creates realistic demo records for record cost accounting transactions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_cost_accounting_transactions", "rar_sha256": "b2c4cd83729dc4566e1ebdff5224bcebbe02aec59740daff97588eb467ee941f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_record_cost_accounting_transactions_agent.py` and embedded as the fenced Python below (sha256 b2c4cd83729dc456…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_record_cost_accounting_transactions_agent.py` first:

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
    "version": '2.0.0',
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
