---
name: "rar-cowork-cookbook-audit-perform-market-research"
description: "Audits perform market research records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_perform_market_research", "rar_sha256": "82cfe17fcc7b5cb1dcd2fd9d58988061f2dd57d8128b88aae9add2022ed348e8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_perform_market_research_agent.py` and embedded as the fenced Python below (sha256 82cfe17fcc7b5cb1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_perform_market_research_agent.py` first:

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
    "version": '2.0.1',
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
