---
name: "rar-cowork-cookbook-report-research-new-products"
description: "Builds a structured summary report of research new products activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_research_new_products", "rar_sha256": "c5bc9f57bdcb3ba8f6707191273c775bee7a1410030b3e48e8ca06b9669f0d1d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_research_new_products_agent.py` and embedded as the fenced Python below (sha256 c5bc9f57bdcb3ba8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_research_new_products_agent.py` first:

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
    "version": '2.0.1',
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
