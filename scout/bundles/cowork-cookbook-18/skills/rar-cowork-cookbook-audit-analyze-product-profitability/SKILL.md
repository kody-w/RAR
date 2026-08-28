---
name: "rar-cowork-cookbook-audit-analyze-product-profitability"
description: "Audits analyze product profitability records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_product_profitability", "rar_sha256": "4a48877fe78b0fbc29f032ab5c0fe8a235b6a23fa2251270670e640d2a971741", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_analyze_product_profitability`. The original RAPP
agent is preserved byte-for-byte in `audit_analyze_product_profitability_agent.py` and in the RCI capsule.

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

Analyze product profitability Completeness Audit — Audits analyze product profitability records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-product-profitability
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_product_profitability_agent.py` and embedded as the fenced Python below (sha256 4a48877fe78b0fbc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_product_profitability_agent.py` first:

```bash
python3 audit_analyze_product_profitability_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_analyze_product_profitability_agent.py   # or on stdin
python3 audit_analyze_product_profitability_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze product profitability Completeness Audit — Audits analyze product profitability records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-analyze-product-profitability
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_analyze_product_profitability',
    "version": '2.0.1',
    "display_name": 'Analyze product profitability Completeness Audit',
    "description": 'Audits analyze product profitability records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-analyze-product-profitability',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-analyze-product-profitability',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '96fc385f54bd78d6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/analyze-product-performance/analyze-product-profitability'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-analyze-product-profitability', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditAnalyzeProductProfitability(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditAnalyzeProductProfitability'
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
    print(AuditAnalyzeProductProfitability().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
