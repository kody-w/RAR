---
name: "rar-cowork-cookbook-report-evaluate-campaign-performance"
description: "Builds a structured summary report of evaluate campaign performance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_evaluate_campaign_performance", "rar_sha256": "2ce116c69ca08dde09470bf423d924e05d747e0290e5936e1e6ecf5df6c7dc30", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_evaluate_campaign_performance`. The original RAPP
agent is preserved byte-for-byte in `report_evaluate_campaign_performance_agent.py` and in the RCI capsule.

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

Evaluate campaign performance Summary Report — Builds a structured summary report of evaluate campaign performance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-evaluate-campaign-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_evaluate_campaign_performance_agent.py` and embedded as the fenced Python below (sha256 2ce116c69ca08dde…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_evaluate_campaign_performance_agent.py` first:

```bash
python3 report_evaluate_campaign_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_evaluate_campaign_performance_agent.py   # or on stdin
python3 report_evaluate_campaign_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate campaign performance Summary Report — Builds a structured summary report of evaluate campaign performance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-evaluate-campaign-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_evaluate_campaign_performance',
    "version": '2.0.1',
    "display_name": 'Evaluate campaign performance Summary Report',
    "description": 'Builds a structured summary report of evaluate campaign performance activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-evaluate-campaign-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-evaluate-campaign-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9da8e0f77b663fb6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/evaluate-campaign-performance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-evaluate-campaign-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.429, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis', 'word:evaluate'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ReportEvaluateCampaignPerformance(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportEvaluateCampaignPerformance'
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
    print(ReportEvaluateCampaignPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
