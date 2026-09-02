---
name: "rar-cowork-cookbook-demo-data-audit-financial-transactions"
description: "Generates and creates realistic demo records for audit financial transactions in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_audit_financial_transactions", "rar_sha256": "0daf3a05c492836fe9c4ee7be4f23bb3f0f1d9f843ec5ad42633fd40e380e276", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_audit_financial_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-audit-financial-transactions:7a337cc8bcbd00e34986e08ea99f2290d33d60bc4b14c936f5b05d311ee5c247", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_audit_financial_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_audit_financial_transactions_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_audit_financial_transactions_agent.py` and embedded as the fenced Python below (sha256 0daf3a05c492836f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_audit_financial_transactions_agent.py` first:

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
    "version": '2.0.0',
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
