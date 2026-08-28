---
name: "rar-cowork-cookbook-report-analyze-costs"
description: "Builds a structured summary report of analyze costs activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_costs", "rar_sha256": "09304482f1e5cf85dd5bbed81627e2dd87b1e29be345235d6fc64d058f3673a9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_analyze_costs`. The original RAPP
agent is preserved byte-for-byte in `report_analyze_costs_agent.py` and in the RCI capsule.

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

Analyze costs Summary Report — Builds a structured summary report of analyze costs activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-costs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_costs_agent.py` and embedded as the fenced Python below (sha256 09304482f1e5cf85…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_costs_agent.py` first:

```bash
python3 report_analyze_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_analyze_costs_agent.py   # or on stdin
python3 report_analyze_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze costs Summary Report — Builds a structured summary report of analyze costs activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_analyze_costs',
    "version": '2.0.0',
    "display_name": 'Analyze costs Summary Report',
    "description": 'Builds a structured summary report of analyze costs activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-analyze-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-analyze-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '048771d92f5e8cb5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/analyze-costs'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-analyze-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.429, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis', 'word:analyze'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ReportAnalyzeCosts(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAnalyzeCosts'
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
    print(ReportAnalyzeCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
