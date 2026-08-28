---
name: "rar-cowork-cookbook-audit-assess-customer-credit-risk"
description: "Audits assess customer credit risk records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_assess_customer_credit_risk", "rar_sha256": "4d1df90b953648eed37206501c49ecfbd753b210fb5d7967aac12cf1d4b037be", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_assess_customer_credit_risk`. The original RAPP
agent is preserved byte-for-byte in `audit_assess_customer_credit_risk_agent.py` and in the RCI capsule.

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
