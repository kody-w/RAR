---
name: "rar-cowork-cookbook-audit-use-the-knowledge-base-to-find-a-solution"
description: "Audits use the knowledge base to find a solution records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_use_the_knowledge_base_to_find_a_solution", "rar_sha256": "e8a88322482652b9f7349783b4372dfb6f860218406fd2a105ae7b2990dbe13e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_use_the_knowledge_base_to_find_a_solution_agent.py` and embedded as the fenced Python below (sha256 e8a88322482652b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_use_the_knowledge_base_to_find_a_solution_agent.py` first:

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
    "version": '2.0.0',
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
