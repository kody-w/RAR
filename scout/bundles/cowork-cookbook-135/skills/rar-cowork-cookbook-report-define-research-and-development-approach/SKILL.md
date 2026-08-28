---
name: "rar-cowork-cookbook-report-define-research-and-development-approach"
description: "Builds a structured summary report of define research and development approach activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_research_and_development_approach", "rar_sha256": "f7bd291394fbfc1bc4e5047e1552a1d627185ac3405d83eac9939ff89e18b0ac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_research_and_development_approach_agent.py` and embedded as the fenced Python below (sha256 f7bd291394fbfc1b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_research_and_development_approach_agent.py` first:

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
    "version": '2.0.0',
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
