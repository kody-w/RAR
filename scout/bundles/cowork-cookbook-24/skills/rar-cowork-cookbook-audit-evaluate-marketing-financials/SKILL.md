---
name: "rar-cowork-cookbook-audit-evaluate-marketing-financials"
description: "Audits evaluate marketing financials records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_evaluate_marketing_financials", "rar_sha256": "b48e2d08d38a4a87f26ddefc5510976baff24dc4336992a5b0e46668f830226f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_evaluate_marketing_financials`. The original RAPP
agent is preserved byte-for-byte in `audit_evaluate_marketing_financials_agent.py` and in the RCI capsule.

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

Evaluate marketing financials Completeness Audit — Audits evaluate marketing financials records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-evaluate-marketing-financials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_evaluate_marketing_financials_agent.py` and embedded as the fenced Python below (sha256 b48e2d08d38a4a87…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_evaluate_marketing_financials_agent.py` first:

```bash
python3 audit_evaluate_marketing_financials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_evaluate_marketing_financials_agent.py   # or on stdin
python3 audit_evaluate_marketing_financials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate marketing financials Completeness Audit — Audits evaluate marketing financials records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-evaluate-marketing-financials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_evaluate_marketing_financials',
    "version": '2.0.1',
    "display_name": 'Evaluate marketing financials Completeness Audit',
    "description": 'Audits evaluate marketing financials records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-evaluate-marketing-financials',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-evaluate-marketing-financials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c35d469fb6b6014b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/evaluate-marketing-financials'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-evaluate-marketing-financials', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditEvaluateMarketingFinancials(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditEvaluateMarketingFinancials'
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
    print(AuditEvaluateMarketingFinancials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
