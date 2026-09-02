---
name: "rar-cowork-cookbook-report-report-production-output"
description: "Builds a structured summary report of report production output activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_production_output", "rar_sha256": "b1abf7063bb42c1aeaed214bc0f75312b75a6e06c34c99e2672c0cf1ae8c0d6d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_report_production_output_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-report-production-output:5d816e2abff38cb59782d9b375d1e084040485856f7b5a001d1e0bc29213ab0f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_report_production_output`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_report_production_output_agent.py` is
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
