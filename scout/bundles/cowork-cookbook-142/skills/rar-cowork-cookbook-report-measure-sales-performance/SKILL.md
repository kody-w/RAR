---
name: "rar-cowork-cookbook-report-measure-sales-performance"
description: "Builds a structured summary report of measure sales performance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_measure_sales_performance", "rar_sha256": "5816a2b53aa6e510078a57a3eabad070e11a1cffd33e2e468b9cb4716aa570dd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_measure_sales_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-measure-sales-performance:17c9f1c956f7628396804f5caa66a58a08fe69eec362ead29f22035b3dbe4ca3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_measure_sales_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_measure_sales_performance_agent.py` is
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
