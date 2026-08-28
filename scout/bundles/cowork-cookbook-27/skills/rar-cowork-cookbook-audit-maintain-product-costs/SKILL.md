---
name: "rar-cowork-cookbook-audit-maintain-product-costs"
description: "Audits maintain product costs records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_maintain_product_costs", "rar_sha256": "83e8f270c243df7dfcbde02459a224a36632eac17d4353069a957d5307a273e5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_maintain_product_costs`. The original RAPP
agent is preserved byte-for-byte in `audit_maintain_product_costs_agent.py` and in the RCI capsule.

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
