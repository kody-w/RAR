---
name: "rar-cowork-cookbook-audit-market-test-new-products"
description: "Audits market test new products records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_market_test_new_products", "rar_sha256": "ba3b8b713f073c7c11cc4b90580535e3b50494144203b008512d04b57cae805a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_market_test_new_products_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-market-test-new-products:00d0125cd38c86bbc2f1f53e38d05e97e0b3282b4c788c95a83478bc0e405629", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_market_test_new_products`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_market_test_new_products_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_market_test_new_products_agent.py` and embedded as the fenced Python below (sha256 ba3b8b713f073c7c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_market_test_new_products_agent.py` first:

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
    "version": '2.0.0',
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
