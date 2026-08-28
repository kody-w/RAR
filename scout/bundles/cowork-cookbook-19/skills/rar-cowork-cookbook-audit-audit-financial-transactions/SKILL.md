---
name: "rar-cowork-cookbook-audit-audit-financial-transactions"
description: "Audits audit financial transactions records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_audit_financial_transactions", "rar_sha256": "b58a58383c152a05ca66fc9929f2d4ab14470e5d9163e96b838d92d3e0043ad3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_audit_financial_transactions_agent.py` and embedded as the fenced Python below (sha256 b58a58383c152a05…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_audit_financial_transactions_agent.py` first:

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
    "version": '2.0.1',
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
