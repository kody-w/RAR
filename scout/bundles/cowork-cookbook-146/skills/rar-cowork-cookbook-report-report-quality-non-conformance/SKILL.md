---
name: "rar-cowork-cookbook-report-report-quality-non-conformance"
description: "Builds a structured summary report of report quality non-conformance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_quality_non_conformance", "rar_sha256": "0c607b459cff2597b62f08ddcc31d6e5ab91f2f89a5cf965b3e1a18b3626e51c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_report_quality_non_conformance`. The original RAPP
agent is preserved byte-for-byte in `report_report_quality_non_conformance_agent.py` and in the RCI capsule.

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

Report quality non-conformance Summary Report — Builds a structured summary report of report quality non-conformance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-report-quality-non-conformance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_report_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 0c607b459cff2597…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_report_quality_non_conformance_agent.py` first:

```bash
python3 report_report_quality_non_conformance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_report_quality_non_conformance_agent.py   # or on stdin
python3 report_report_quality_non_conformance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Report quality non-conformance Summary Report — Builds a structured summary report of report quality non-conformance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-report-quality-non-conformance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_report_quality_non_conformance',
    "version": '2.0.0',
    "display_name": 'Report quality non-conformance Summary Report',
    "description": 'Builds a structured summary report of report quality non-conformance activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-report-quality-non-conformance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-report-quality-non-conformance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '60c361c5267dbec1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/report-quality-non-conformance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-report-quality-non-conformance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportReportQualityNonConformance(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReportQualityNonConformance'
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
    print(ReportReportQualityNonConformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
