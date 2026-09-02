---
name: "rar-cowork-cookbook-report-measure-and-analyze-procurement-spend"
description: "Builds a structured summary report of measure and analyze procurement spend activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_measure_and_analyze_procurement_spend", "rar_sha256": "4e3f11dd06968a606b590b9362a505da527068385e661f609b92e12e9947bc36", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_measure_and_analyze_procurement_spend_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-measure-and-analyze-procurement-spend:b3b26a7347e1788c9a3e173cadff5eacb6782b9ef6e8daa944dc773511ca191f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_measure_and_analyze_procurement_spend`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_measure_and_analyze_procurement_spend_agent.py` is
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
