---
name: "rar-cowork-cookbook-audit-evaluate-marketing-financials"
description: "Audits evaluate marketing financials records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_evaluate_marketing_financials", "rar_sha256": "57d05e4296224e1337e02660fa6fd62192e9fe59e2ebe92d3db59f6113b8c92d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_evaluate_marketing_financials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-evaluate-marketing-financials:ddf9e5a1c22ef01eae6b3a2cfa2a1cb5f641aa404cca6db81c4ac04c029e9a15", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_evaluate_marketing_financials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_evaluate_marketing_financials_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_evaluate_marketing_financials_agent.py` and embedded as the fenced Python below (sha256 57d05e4296224e13…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_evaluate_marketing_financials_agent.py` first:

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
    "version": '2.0.0',
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
