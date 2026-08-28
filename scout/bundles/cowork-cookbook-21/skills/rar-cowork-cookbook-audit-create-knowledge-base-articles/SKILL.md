---
name: "rar-cowork-cookbook-audit-create-knowledge-base-articles"
description: "Audits create knowledge base articles records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_create_knowledge_base_articles", "rar_sha256": "df814f462348dc4c44b9c12a4db8f09035069414e74b2a90134d038f4cc16214", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_create_knowledge_base_articles_agent.py` and embedded as the fenced Python below (sha256 df814f462348dc4c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_create_knowledge_base_articles_agent.py` first:

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
    "version": '2.0.0',
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
