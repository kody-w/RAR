---
name: "rar-cowork-cookbook-report-define-research-and-development-approach"
description: "Builds a structured summary report of define research and development approach activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_research_and_development_approach", "rar_sha256": "11f2d48696b986a240c72d5e9e5ac72fc714ab5c23f340e2ff78aa30fc549596", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_research_and_development_approach`. The original RAPP
agent is preserved byte-for-byte in `report_define_research_and_development_approach_agent.py` and in the RCI capsule.

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

Define research and development approach Summary Report — Builds a structured summary report of define research and development approach activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-research-and-development-approach
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_research_and_development_approach_agent.py` and embedded as the fenced Python below (sha256 11f2d48696b986a2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_research_and_development_approach_agent.py` first:

```bash
python3 report_define_research_and_development_approach_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_research_and_development_approach_agent.py   # or on stdin
python3 report_define_research_and_development_approach_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define research and development approach Summary Report — Builds a structured summary report of define research and development approach activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-research-and-development-approach
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_research_and_development_approach',
    "version": '2.0.1',
    "display_name": 'Define research and development approach Summary Report',
    "description": 'Builds a structured summary report of define research and development approach activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-research-and-development-approach',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-research-and-development-approach',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e58557424f1dab33',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/define-research-and-development-approach'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-define-research-and-development-approach', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.375, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis', 'word:research'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ReportDefineResearchAndDevelopmentApproach(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineResearchAndDevelopmentApproach'
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
    print(ReportDefineResearchAndDevelopmentApproach().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
