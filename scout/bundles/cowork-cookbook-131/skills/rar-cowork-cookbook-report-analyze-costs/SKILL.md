---
name: "rar-cowork-cookbook-report-analyze-costs"
description: "Builds a structured summary report of analyze costs activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_costs", "rar_sha256": "3625f7f128a0346d12c18275b7dfd86dd334bdd7cfed02dd0a16d055f3ecb89f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_costs_agent.py` and embedded as the fenced Python below (sha256 3625f7f128a0346d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_costs_agent.py` first:

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
    "version": '2.0.1',
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
