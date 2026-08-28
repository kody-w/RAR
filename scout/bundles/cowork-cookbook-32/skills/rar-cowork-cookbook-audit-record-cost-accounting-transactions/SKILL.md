---
name: "rar-cowork-cookbook-audit-record-cost-accounting-transactions"
description: "Audits record cost accounting transactions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_cost_accounting_transactions", "rar_sha256": "7ef14ed8ee7a5fb674295989c2dc69864061e8ec62e89077a87e42e19d861d16", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_record_cost_accounting_transactions`. The original RAPP
agent is preserved byte-for-byte in `audit_record_cost_accounting_transactions_agent.py` and in the RCI capsule.

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
