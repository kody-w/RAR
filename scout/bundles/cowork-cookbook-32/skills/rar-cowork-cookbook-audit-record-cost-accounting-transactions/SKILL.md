---
name: "rar-cowork-cookbook-audit-record-cost-accounting-transactions"
description: "Audits record cost accounting transactions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_record_cost_accounting_transactions", "rar_sha256": "7eb6d92a0270bc6f7eeebb65325c7e14fd29258fb7ae90fd5b9d208fbff66d57", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_record_cost_accounting_transactions_agent.py` and embedded as the fenced Python below (sha256 7eb6d92a0270bc6f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_record_cost_accounting_transactions_agent.py` first:

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
    "version": '2.0.1',
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
