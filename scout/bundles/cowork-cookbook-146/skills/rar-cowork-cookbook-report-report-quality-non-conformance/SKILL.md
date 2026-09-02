---
name: "rar-cowork-cookbook-report-report-quality-non-conformance"
description: "Builds a structured summary report of report quality non-conformance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_report_quality_non_conformance", "rar_sha256": "0c607b459cff2597b62f08ddcc31d6e5ab91f2f89a5cf965b3e1a18b3626e51c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_report_quality_non_conformance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-report-quality-non-conformance:8d4982b91f21ffaebc92b58ee52216d77c6d6e0474a3905b68278f90bb520ed5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_report_quality_non_conformance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_report_quality_non_conformance_agent.py` is
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
