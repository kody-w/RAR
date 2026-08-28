---
name: "rar-cowork-cookbook-audit-assess-customer-credit-risk"
description: "Audits assess customer credit risk records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_assess_customer_credit_risk", "rar_sha256": "6d525218754ef5a0707654a056f217a349a8f5576b59d0a916588fc7d7d014c9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_assess_customer_credit_risk_agent.py` and embedded as the fenced Python below (sha256 6d525218754ef5a0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_assess_customer_credit_risk_agent.py` first:

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
    "version": '2.0.1',
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
