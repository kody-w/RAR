---
name: "rar-cowork-cookbook-report-research-new-products"
description: "Builds a structured summary report of research new products activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_research_new_products", "rar_sha256": "6e4ea2002d6a736473e6a54326cfa52eac9342f268f7693d43be7c17245d4bdf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_research_new_products`. The original RAPP
agent is preserved byte-for-byte in `report_research_new_products_agent.py` and in the RCI capsule.

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
