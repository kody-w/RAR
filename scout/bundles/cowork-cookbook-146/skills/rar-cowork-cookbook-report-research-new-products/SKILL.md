---
name: "rar-cowork-cookbook-report-research-new-products"
description: "Builds a structured summary report of research new products activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_research_new_products", "rar_sha256": "6e4ea2002d6a736473e6a54326cfa52eac9342f268f7693d43be7c17245d4bdf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_research_new_products_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-research-new-products:d5d7b2b3f8bcc690dc4ccf1e9f34504a1c58b80eb87dd8e9cc0ae1d5df53680c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_research_new_products`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_research_new_products_agent.py` is
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

Research new products Summary Report — Builds a structured summary report of research new products activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-research-new-products
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_research_new_products_agent.py` and embedded as the fenced Python below (sha256 6e4ea2002d6a7364…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_research_new_products_agent.py` first:

```bash
python3 report_research_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_research_new_products_agent.py   # or on stdin
python3 report_research_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Research new products Summary Report — Builds a structured summary report of research new products activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-research-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_research_new_products',
    "version": '2.0.0',
    "display_name": 'Research new products Summary Report',
    "description": 'Builds a structured summary report of research new products activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-research-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-research-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'df2b2ec376deef8f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/research-new-products'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-research-new-products', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.429, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis', 'word:research'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ReportResearchNewProducts(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportResearchNewProducts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(ReportResearchNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
