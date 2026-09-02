---
name: "rar-cowork-cookbook-audit-develop-sales-pricing-strategy"
description: "Audits develop sales pricing strategy records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_sales_pricing_strategy", "rar_sha256": "6aeda032b42088508a86fe2e3e53777cb8745dc680b703488f921d59b136330f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_develop_sales_pricing_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-develop-sales-pricing-strategy:d48616107bc0da8d8a21b8539d6af9d5cf74089ae8439e1728dea16d2ff50060", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_develop_sales_pricing_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_develop_sales_pricing_strategy_agent.py` is
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

Develop sales pricing strategy Completeness Audit — Audits develop sales pricing strategy records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-sales-pricing-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_sales_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 6aeda032b4208850…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_sales_pricing_strategy_agent.py` first:

```bash
python3 audit_develop_sales_pricing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_develop_sales_pricing_strategy_agent.py   # or on stdin
python3 audit_develop_sales_pricing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales pricing strategy Completeness Audit — Audits develop sales pricing strategy records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-develop-sales-pricing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_develop_sales_pricing_strategy',
    "version": '2.0.0',
    "display_name": 'Develop sales pricing strategy Completeness Audit',
    "description": 'Audits develop sales pricing strategy records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-develop-sales-pricing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-develop-sales-pricing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '52e4d331fe44a14b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-sales-pricing-strategy'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/audit-develop-sales-pricing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AuditDevelopSalesPricingStrategy(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditDevelopSalesPricingStrategy'
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
    print(AuditDevelopSalesPricingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
