---
name: "rar-cowork-cookbook-audit-analyze-product-profitability"
description: "Audits analyze product profitability records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_analyze_product_profitability", "rar_sha256": "9986b320a3c586268f3d22f5d9cca468edd7a68bfcbe4ffcea53cd7e03b8d947", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_analyze_product_profitability_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-analyze-product-profitability:4404abc29222908f8ac9b6100072a47b20d71a23adbce5bc88c6485085019409", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_analyze_product_profitability`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_analyze_product_profitability_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_analyze_product_profitability_agent.py` and embedded as the fenced Python below (sha256 9986b320a3c58626…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_analyze_product_profitability_agent.py` first:

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
    "version": '2.0.0',
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
