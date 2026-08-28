---
name: "rar-cowork-cookbook-audit-develop-sales-pricing-strategy"
description: "Audits develop sales pricing strategy records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_sales_pricing_strategy", "rar_sha256": "6aeda032b42088508a86fe2e3e53777cb8745dc680b703488f921d59b136330f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_develop_sales_pricing_strategy`. The original RAPP
agent is preserved byte-for-byte in `audit_develop_sales_pricing_strategy_agent.py` and in the RCI capsule.

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
