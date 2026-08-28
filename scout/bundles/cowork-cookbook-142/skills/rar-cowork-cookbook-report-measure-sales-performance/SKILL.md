---
name: "rar-cowork-cookbook-report-measure-sales-performance"
description: "Builds a structured summary report of measure sales performance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_measure_sales_performance", "rar_sha256": "980bf3e1f9ce3cbf61ade4efcdec963fc55030a6f0dabd2cff530314ba96dfd9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_measure_sales_performance_agent.py` and embedded as the fenced Python below (sha256 980bf3e1f9ce3cbf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_measure_sales_performance_agent.py` first:

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
    "version": '2.0.1',
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
