---
name: "rar-cowork-cookbook-audit-create-knowledge-base-articles"
description: "Audits create knowledge base articles records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_create_knowledge_base_articles", "rar_sha256": "df814f462348dc4c44b9c12a4db8f09035069414e74b2a90134d038f4cc16214", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "audit_create_knowledge_base_articles_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/audit-create-knowledge-base-articles:6ad26c072b1c35a3660fc74f88e4a3acc718389aa98207fb384008c230289237", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/audit_create_knowledge_base_articles`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `audit_create_knowledge_base_articles_agent.py` is
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
