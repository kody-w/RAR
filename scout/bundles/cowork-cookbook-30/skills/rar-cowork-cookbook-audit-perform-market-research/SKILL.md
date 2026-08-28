---
name: "rar-cowork-cookbook-audit-perform-market-research"
description: "Audits perform market research records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_market_research", "rar_sha256": "45586fe2e0a9cf871317a3aa44c101e560b3da1e0be0778d6ee2aecbb7ff21f1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_perform_market_research`. The original RAPP
agent is preserved byte-for-byte in `audit_perform_market_research_agent.py` and in the RCI capsule.

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
