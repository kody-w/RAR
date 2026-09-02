---
name: "rar-cowork-cookbook-audit-record-cost-accounting-transactions"
description: "Audits record cost accounting transactions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_cost_accounting_transactions", "rar_sha256": "7ef14ed8ee7a5fb674295989c2dc69864061e8ec62e89077a87e42e19d861d16", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_record_cost_accounting_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-record-cost-accounting-transactions:0f0b0664c315c637bdac5feb9bdd6de171474c014020577cd171f2ceb03c1771", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_record_cost_accounting_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_record_cost_accounting_transactions_agent.py` is
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

Record cost accounting transactions Completeness Audit — Audits record cost accounting transactions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-cost-accounting-transactions
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_record_cost_accounting_transactions_agent.py` and embedded as the fenced Python below (sha256 7ef14ed8ee7a5fb6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_record_cost_accounting_transactions_agent.py` first:

```bash
python3 audit_record_cost_accounting_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_record_cost_accounting_transactions_agent.py   # or on stdin
python3 audit_record_cost_accounting_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record cost accounting transactions Completeness Audit — Audits record cost accounting transactions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-record-cost-accounting-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_record_cost_accounting_transactions',
    "version": '2.0.0',
    "display_name": 'Record cost accounting transactions Completeness Audit',
    "description": 'Audits record cost accounting transactions records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-record-cost-accounting-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-record-cost-accounting-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4bbac9f445c02b4c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/record-cost-accounting-transactions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-record-cost-accounting-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditRecordCostAccountingTransactions(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditRecordCostAccountingTransactions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(AuditRecordCostAccountingTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
