---
name: "rar-cowork-cookbook-report-measure-and-analyze-procurement-spend"
description: "Builds a structured summary report of measure and analyze procurement spend activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_measure_and_analyze_procurement_spend", "rar_sha256": "65eb7958c105998e43b7526c81d0c8b6fc1b3d3fa0a4778febb72d6dc163934f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_measure_and_analyze_procurement_spend`. The original RAPP
agent is preserved byte-for-byte in `report_measure_and_analyze_procurement_spend_agent.py` and in the RCI capsule.

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

Measure and analyze procurement spend Summary Report — Builds a structured summary report of measure and analyze procurement spend activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-measure-and-analyze-procurement-spend
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_measure_and_analyze_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 65eb7958c105998e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_measure_and_analyze_procurement_spend_agent.py` first:

```bash
python3 report_measure_and_analyze_procurement_spend_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_measure_and_analyze_procurement_spend_agent.py   # or on stdin
python3 report_measure_and_analyze_procurement_spend_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure and analyze procurement spend Summary Report — Builds a structured summary report of measure and analyze procurement spend activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-measure-and-analyze-procurement-spend
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_measure_and_analyze_procurement_spend',
    "version": '2.0.1',
    "display_name": 'Measure and analyze procurement spend Summary Report',
    "description": 'Builds a structured summary report of measure and analyze procurement spend activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-measure-and-analyze-procurement-spend',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-measure-and-analyze-procurement-spend',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c24f8bbf0624031',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/measure-and-analyze-procurement-spend'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-measure-and-analyze-procurement-spend', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.5, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis', 'word:analyze', 'word:measure'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ReportMeasureAndAnalyzeProcurementSpend(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMeasureAndAnalyzeProcurementSpend'
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
    print(ReportMeasureAndAnalyzeProcurementSpend().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
