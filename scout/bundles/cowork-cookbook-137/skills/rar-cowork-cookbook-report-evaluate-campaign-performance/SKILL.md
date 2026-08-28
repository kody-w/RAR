---
name: "rar-cowork-cookbook-report-evaluate-campaign-performance"
description: "Builds a structured summary report of evaluate campaign performance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_evaluate_campaign_performance", "rar_sha256": "ffca062dc109d47d683d17057c6ccc3d42de3786dbe2db15460ff9232335adb5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_evaluate_campaign_performance_agent.py` and embedded as the fenced Python below (sha256 ffca062dc109d47d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_evaluate_campaign_performance_agent.py` first:

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
    "version": '2.0.0',
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
