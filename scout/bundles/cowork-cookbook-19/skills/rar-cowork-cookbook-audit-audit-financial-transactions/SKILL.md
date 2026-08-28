---
name: "rar-cowork-cookbook-audit-audit-financial-transactions"
description: "Audits audit financial transactions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_audit_financial_transactions", "rar_sha256": "6a8924870614bdad72ba6f96fa2e8da245b888abf2942c0ec709768bba2413a3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_audit_financial_transactions`. The original RAPP
agent is preserved byte-for-byte in `audit_audit_financial_transactions_agent.py` and in the RCI capsule.

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
