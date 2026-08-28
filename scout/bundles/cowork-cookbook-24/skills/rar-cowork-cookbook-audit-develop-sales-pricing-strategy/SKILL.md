---
name: "rar-cowork-cookbook-audit-develop-sales-pricing-strategy"
description: "Audits develop sales pricing strategy records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_develop_sales_pricing_strategy", "rar_sha256": "017fd25e337a86c7cf8511a9b8cc4a8f7cf2cd66faaec70e09629ce16fcbeb25", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_develop_sales_pricing_strategy_agent.py` and embedded as the fenced Python below (sha256 017fd25e337a86c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_develop_sales_pricing_strategy_agent.py` first:

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
    "version": '2.0.1',
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
