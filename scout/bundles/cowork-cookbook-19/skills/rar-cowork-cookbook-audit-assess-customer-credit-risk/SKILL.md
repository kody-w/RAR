---
name: "rar-cowork-cookbook-audit-assess-customer-credit-risk"
description: "Audits assess customer credit risk records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_assess_customer_credit_risk", "rar_sha256": "4d1df90b953648eed37206501c49ecfbd753b210fb5d7967aac12cf1d4b037be", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_assess_customer_credit_risk_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-assess-customer-credit-risk:0e7ccf6cf0fcf1d842c23d29d379a03a4aad22bbae9ab78dc50702c407dbb53c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_assess_customer_credit_risk`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_assess_customer_credit_risk_agent.py` is
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

Assess customer credit risk Completeness Audit — Audits assess customer credit risk records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-assess-customer-credit-risk
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_assess_customer_credit_risk_agent.py` and embedded as the fenced Python below (sha256 4d1df90b953648ee…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_assess_customer_credit_risk_agent.py` first:

```bash
python3 audit_assess_customer_credit_risk_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_assess_customer_credit_risk_agent.py   # or on stdin
python3 audit_assess_customer_credit_risk_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess customer credit risk Completeness Audit — Audits assess customer credit risk records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-assess-customer-credit-risk
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_assess_customer_credit_risk',
    "version": '2.0.0',
    "display_name": 'Assess customer credit risk Completeness Audit',
    "description": 'Audits assess customer credit risk records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-assess-customer-credit-risk',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-assess-customer-credit-risk',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6e8f6fa66640407a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/assess-customer-credit-risk'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-assess-customer-credit-risk', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.545, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:assess', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditAssessCustomerCreditRisk(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAssessCustomerCreditRisk'
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
    print(AuditAssessCustomerCreditRisk().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
