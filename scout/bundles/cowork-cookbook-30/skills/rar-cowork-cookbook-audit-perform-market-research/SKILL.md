---
name: "rar-cowork-cookbook-audit-perform-market-research"
description: "Audits perform market research records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_market_research", "rar_sha256": "45586fe2e0a9cf871317a3aa44c101e560b3da1e0be0778d6ee2aecbb7ff21f1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_perform_market_research_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-perform-market-research:2380803cd231595fd203ef0952e6e7157d7fdaf119aeb43e1223afdf1fb38096", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_perform_market_research`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_perform_market_research_agent.py` is
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

Perform market research Completeness Audit — Audits perform market research records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-market-research
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_perform_market_research_agent.py` and embedded as the fenced Python below (sha256 45586fe2e0a9cf87…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_perform_market_research_agent.py` first:

```bash
python3 audit_perform_market_research_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_perform_market_research_agent.py   # or on stdin
python3 audit_perform_market_research_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform market research Completeness Audit — Audits perform market research records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-perform-market-research
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_perform_market_research',
    "version": '2.0.0',
    "display_name": 'Perform market research Completeness Audit',
    "description": 'Audits perform market research records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-perform-market-research',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-perform-market-research',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd77b213ea3a83758',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/perform-market-research'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/audit-perform-market-research', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditPerformMarketResearch(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPerformMarketResearch'
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
    print(AuditPerformMarketResearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
