---
name: "rar-cowork-cookbook-audit-use-the-knowledge-base-to-find-a-solution"
description: "Audits use the knowledge base to find a solution records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_use_the_knowledge_base_to_find_a_solution", "rar_sha256": "9d6dfc105e765e68b57caca978e307d600ab3004e2b762476e48a3187a469f31", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_use_the_knowledge_base_to_find_a_solution`. The original RAPP
agent is preserved byte-for-byte in `audit_use_the_knowledge_base_to_find_a_solution_agent.py` and in the RCI capsule.

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

Use the knowledge base to find a solution Completeness Audit — Audits use the knowledge base to find a solution records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-use-the-knowledge-base-to-find-a-solution
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_use_the_knowledge_base_to_find_a_solution_agent.py` and embedded as the fenced Python below (sha256 9d6dfc105e765e68…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_use_the_knowledge_base_to_find_a_solution_agent.py` first:

```bash
python3 audit_use_the_knowledge_base_to_find_a_solution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_use_the_knowledge_base_to_find_a_solution_agent.py   # or on stdin
python3 audit_use_the_knowledge_base_to_find_a_solution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Use the knowledge base to find a solution Completeness Audit — Audits use the knowledge base to find a solution records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-use-the-knowledge-base-to-find-a-solution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_use_the_knowledge_base_to_find_a_solution',
    "version": '2.0.1',
    "display_name": 'Use the knowledge base to find a solution Completeness Audit',
    "description": 'Audits use the knowledge base to find a solution records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-use-the-knowledge-base-to-find-a-solution',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-use-the-knowledge-base-to-find-a-solution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'afe979484d3e65e7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/use-the-knowledge-base-to-find-a-solution'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-use-the-knowledge-base-to-find-a-solution', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditUseTheKnowledgeBaseToFindASolution(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditUseTheKnowledgeBaseToFindASolution'
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
    print(AuditUseTheKnowledgeBaseToFindASolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
