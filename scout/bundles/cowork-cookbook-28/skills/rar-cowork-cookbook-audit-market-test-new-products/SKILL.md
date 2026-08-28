---
name: "rar-cowork-cookbook-audit-market-test-new-products"
description: "Audits market test new products records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_market_test_new_products", "rar_sha256": "13198f9a56d46eaff2d835c55ab2e2ec8ae031d114aa56036f5e4e1898aa4192", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_market_test_new_products`. The original RAPP
agent is preserved byte-for-byte in `audit_market_test_new_products_agent.py` and in the RCI capsule.

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

Market test new products Completeness Audit — Audits market test new products records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-market-test-new-products
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_market_test_new_products_agent.py` and embedded as the fenced Python below (sha256 13198f9a56d46eaf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_market_test_new_products_agent.py` first:

```bash
python3 audit_market_test_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_market_test_new_products_agent.py   # or on stdin
python3 audit_market_test_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Market test new products Completeness Audit — Audits market test new products records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-market-test-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_market_test_new_products',
    "version": '2.0.1',
    "display_name": 'Market test new products Completeness Audit',
    "description": 'Audits market test new products records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'audit-market-test-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-market-test-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e8c950c31127483',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/market-test-new-products'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-market-test-new-products', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditMarketTestNewProducts(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMarketTestNewProducts'
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
    print(AuditMarketTestNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
