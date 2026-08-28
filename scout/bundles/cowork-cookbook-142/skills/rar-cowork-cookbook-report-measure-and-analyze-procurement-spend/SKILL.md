---
name: "rar-cowork-cookbook-report-measure-and-analyze-procurement-spend"
description: "Builds a structured summary report of measure and analyze procurement spend activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_measure_and_analyze_procurement_spend", "rar_sha256": "4e3f11dd06968a606b590b9362a505da527068385e661f609b92e12e9947bc36", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_measure_and_analyze_procurement_spend_agent.py` and embedded as the fenced Python below (sha256 4e3f11dd06968a60…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_measure_and_analyze_procurement_spend_agent.py` first:

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
    "version": '2.0.0',
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
