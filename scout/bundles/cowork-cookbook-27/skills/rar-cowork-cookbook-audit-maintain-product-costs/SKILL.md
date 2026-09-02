---
name: "rar-cowork-cookbook-audit-maintain-product-costs"
description: "Audits maintain product costs records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_maintain_product_costs", "rar_sha256": "83e8f270c243df7dfcbde02459a224a36632eac17d4353069a957d5307a273e5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_maintain_product_costs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-maintain-product-costs:a95a4b2c05c29114a654b3fe47628e7b72f504d5a773adf2013b36761f385dc0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_maintain_product_costs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_maintain_product_costs_agent.py` is
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

Maintain product costs Completeness Audit — Audits maintain product costs records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-maintain-product-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_maintain_product_costs_agent.py` and embedded as the fenced Python below (sha256 83e8f270c243df7d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_maintain_product_costs_agent.py` first:

```bash
python3 audit_maintain_product_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_maintain_product_costs_agent.py   # or on stdin
python3 audit_maintain_product_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain product costs Completeness Audit — Audits maintain product costs records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-maintain-product-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_maintain_product_costs',
    "version": '2.0.0',
    "display_name": 'Maintain product costs Completeness Audit',
    "description": 'Audits maintain product costs records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-maintain-product-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-maintain-product-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44111ccd0129869f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/maintain-product-costs'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-maintain-product-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditMaintainProductCosts(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMaintainProductCosts'
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
    print(AuditMaintainProductCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
