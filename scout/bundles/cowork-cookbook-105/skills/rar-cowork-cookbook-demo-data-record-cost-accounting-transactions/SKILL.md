---
name: "rar-cowork-cookbook-demo-data-record-cost-accounting-transactions"
description: "Generates and creates realistic demo records for record cost accounting transactions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_record_cost_accounting_transactions", "rar_sha256": "b2c4cd83729dc4566e1ebdff5224bcebbe02aec59740daff97588eb467ee941f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_record_cost_accounting_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-record-cost-accounting-transactions:f25c2f9ebbd684713469f4393bbef3b0a09f1d0a40bceb84b5f1fc48e5bacebc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_record_cost_accounting_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_record_cost_accounting_transactions_agent.py` is
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
