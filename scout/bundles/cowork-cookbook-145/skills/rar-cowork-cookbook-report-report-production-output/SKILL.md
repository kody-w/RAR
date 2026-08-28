---
name: "rar-cowork-cookbook-report-report-production-output"
description: "Builds a structured summary report of report production output activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_production_output", "rar_sha256": "b1abf7063bb42c1aeaed214bc0f75312b75a6e06c34c99e2672c0cf1ae8c0d6d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_report_production_output`. The original RAPP
agent is preserved byte-for-byte in `report_report_production_output_agent.py` and in the RCI capsule.

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

Report production output Summary Report — Builds a structured summary report of report production output activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-report-production-output
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_report_production_output_agent.py` and embedded as the fenced Python below (sha256 b1abf7063bb42c1a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_report_production_output_agent.py` first:

```bash
python3 report_report_production_output_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_report_production_output_agent.py   # or on stdin
python3 report_report_production_output_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report production output Summary Report — Builds a structured summary report of report production output activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-report-production-output
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_report_production_output',
    "version": '2.0.0',
    "display_name": 'Report production output Summary Report',
    "description": 'Builds a structured summary report of report production output activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-report-production-output',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-report-production-output',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '745bfebdd5536d9a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/run-production-operations/report-production-output'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-report-production-output', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportReportProductionOutput(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReportProductionOutput'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportReportProductionOutput().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
