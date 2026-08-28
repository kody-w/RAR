---
name: "rar-cowork-cookbook-report-report-quality-non-conformance"
description: "Builds a structured summary report of report quality non-conformance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_quality_non_conformance", "rar_sha256": "5659366e2ab3df420254d63ecdcaec3fea1bf6e98910c9de9aaa4730275b52e2", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_report_quality_non_conformance_agent.py` and embedded as the fenced Python below (sha256 5659366e2ab3df42…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_report_quality_non_conformance_agent.py` first:

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
    "version": '2.0.1',
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
