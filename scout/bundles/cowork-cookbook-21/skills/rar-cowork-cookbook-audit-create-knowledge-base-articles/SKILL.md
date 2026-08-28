---
name: "rar-cowork-cookbook-audit-create-knowledge-base-articles"
description: "Audits create knowledge base articles records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_create_knowledge_base_articles", "rar_sha256": "15b4d5ae5150b6dadb6667a2312a85f6239d3d2d94047a0f48dc3860ed211c87", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_create_knowledge_base_articles`. The original RAPP
agent is preserved byte-for-byte in `audit_create_knowledge_base_articles_agent.py` and in the RCI capsule.

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

Create knowledge base articles Completeness Audit — Audits create knowledge base articles records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-create-knowledge-base-articles
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_create_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 15b4d5ae5150b6da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_create_knowledge_base_articles_agent.py` first:

```bash
python3 audit_create_knowledge_base_articles_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_create_knowledge_base_articles_agent.py   # or on stdin
python3 audit_create_knowledge_base_articles_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Create knowledge base articles Completeness Audit — Audits create knowledge base articles records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-create-knowledge-base-articles
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_create_knowledge_base_articles',
    "version": '2.0.1',
    "display_name": 'Create knowledge base articles Completeness Audit',
    "description": 'Audits create knowledge base articles records for completeness and policy compliance against rule-based checks.',
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
        "upstream_slug": 'audit-create-knowledge-base-articles',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-create-knowledge-base-articles',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dfc60312d96b3201',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/establish-a-knowledge-base/create-knowledge-base-articles'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/audit-create-knowledge-base-articles', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AuditCreateKnowledgeBaseArticles(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditCreateKnowledgeBaseArticles'
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
    print(AuditCreateKnowledgeBaseArticles().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
