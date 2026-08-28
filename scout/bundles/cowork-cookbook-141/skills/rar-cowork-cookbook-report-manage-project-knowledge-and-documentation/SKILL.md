---
name: "rar-cowork-cookbook-report-manage-project-knowledge-and-documentation"
description: "Builds a structured summary report of manage project knowledge and documentation activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_project_knowledge_and_documentation", "rar_sha256": "3ba311286e66216ec3cab7a85da946a4d0aea61afd5bfb21c8d06eb40e70f14a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_project_knowledge_and_documentation`. The original RAPP
agent is preserved byte-for-byte in `report_manage_project_knowledge_and_documentation_agent.py` and in the RCI capsule.

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
