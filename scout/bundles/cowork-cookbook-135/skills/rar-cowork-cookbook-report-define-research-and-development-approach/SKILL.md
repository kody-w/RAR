---
name: "rar-cowork-cookbook-report-define-research-and-development-approach"
description: "Builds a structured summary report of define research and development approach activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_research_and_development_approach", "rar_sha256": "f7bd291394fbfc1bc4e5047e1552a1d627185ac3405d83eac9939ff89e18b0ac", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_define_research_and_development_approach_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-define-research-and-development-approach:84a0ff9581e8a1394b8dd0ac39901cc8bbef42315ce534fd3b9ca4e09fb2a07b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_define_research_and_development_approach`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_define_research_and_development_approach_agent.py` is
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
