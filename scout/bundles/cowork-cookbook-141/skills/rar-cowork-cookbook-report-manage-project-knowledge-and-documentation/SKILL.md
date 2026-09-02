---
name: "rar-cowork-cookbook-report-manage-project-knowledge-and-documentation"
description: "Builds a structured summary report of manage project knowledge and documentation activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_project_knowledge_and_documentation", "rar_sha256": "3ba311286e66216ec3cab7a85da946a4d0aea61afd5bfb21c8d06eb40e70f14a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_manage_project_knowledge_and_documentation_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-manage-project-knowledge-and-documentation:39cdd2d5b2118e5932f08494406151efb5548ba3a4b181d820e4a196ed7cf91c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_manage_project_knowledge_and_documentation`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_manage_project_knowledge_and_documentation_agent.py` is
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

Manage project knowledge and documentation Summary Report — Builds a structured summary report of manage project knowledge and documentation activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-project-knowledge-and-documentation
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_project_knowledge_and_documentation_agent.py` and embedded as the fenced Python below (sha256 3ba311286e66216e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_project_knowledge_and_documentation_agent.py` first:

```bash
python3 report_manage_project_knowledge_and_documentation_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_project_knowledge_and_documentation_agent.py   # or on stdin
python3 report_manage_project_knowledge_and_documentation_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage project knowledge and documentation Summary Report — Builds a structured summary report of manage project knowledge and documentation activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-project-knowledge-and-documentation
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_project_knowledge_and_documentation',
    "version": '2.0.0',
    "display_name": 'Manage project knowledge and documentation Summary Report',
    "description": 'Builds a structured summary report of manage project knowledge and documentation activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-project-knowledge-and-documentation',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-project-knowledge-and-documentation',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1a3545cf2d05ab65',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/manage-project-knowledge-and-documentation'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-manage-project-knowledge-and-documentation', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportManageProjectKnowledgeAndDocumentation(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageProjectKnowledgeAndDocumentation'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportManageProjectKnowledgeAndDocumentation().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
