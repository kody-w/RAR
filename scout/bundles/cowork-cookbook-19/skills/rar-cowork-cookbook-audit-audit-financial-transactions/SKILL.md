---
name: "rar-cowork-cookbook-audit-audit-financial-transactions"
description: "Audits audit financial transactions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_audit_financial_transactions", "rar_sha256": "6a8924870614bdad72ba6f96fa2e8da245b888abf2942c0ec709768bba2413a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_audit_financial_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-audit-financial-transactions:ddaa27a893df1637a1c6576ea8a3e7ddc68c6e291b43497bc4f80787cb6fa18e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_audit_financial_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_audit_financial_transactions_agent.py` is
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

Audit financial transactions Completeness Audit — Audits audit financial transactions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-audit-financial-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_audit_financial_transactions_agent.py` and embedded as the fenced Python below (sha256 6a8924870614bdad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_audit_financial_transactions_agent.py` first:

```bash
python3 audit_audit_financial_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_audit_financial_transactions_agent.py   # or on stdin
python3 audit_audit_financial_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Audit financial transactions Completeness Audit — Audits audit financial transactions records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-audit-financial-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_audit_financial_transactions',
    "version": '2.0.0',
    "display_name": 'Audit financial transactions Completeness Audit',
    "description": 'Audits audit financial transactions records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-audit-financial-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-audit-financial-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bd2d36681c3d1df6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/audit-financial-transactions'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/audit-audit-financial-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditAuditFinancialTransactions(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAuditFinancialTransactions'
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
    print(AuditAuditFinancialTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
