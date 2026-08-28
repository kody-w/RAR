---
name: "rar-cowork-cookbook-report-measure-sales-performance"
description: "Builds a structured summary report of measure sales performance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_measure_sales_performance", "rar_sha256": "5816a2b53aa6e510078a57a3eabad070e11a1cffd33e2e468b9cb4716aa570dd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_measure_sales_performance`. The original RAPP
agent is preserved byte-for-byte in `report_measure_sales_performance_agent.py` and in the RCI capsule.

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

Measure sales performance Summary Report — Builds a structured summary report of measure sales performance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-measure-sales-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_measure_sales_performance_agent.py` and embedded as the fenced Python below (sha256 5816a2b53aa6e510…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_measure_sales_performance_agent.py` first:

```bash
python3 report_measure_sales_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_measure_sales_performance_agent.py   # or on stdin
python3 report_measure_sales_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure sales performance Summary Report — Builds a structured summary report of measure sales performance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-measure-sales-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_measure_sales_performance',
    "version": '2.0.0',
    "display_name": 'Measure sales performance Summary Report',
    "description": 'Builds a structured summary report of measure sales performance activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-measure-sales-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-measure-sales-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8999368db27325a0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/analyze-sales-performance/measure-sales-performance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-measure-sales-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.429, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis', 'word:measure'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ReportMeasureSalesPerformance(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMeasureSalesPerformance'
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
    print(ReportMeasureSalesPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
