---
name: "rar-cowork-cookbook-report-prepare-financial-statements"
description: "Builds a structured summary report of prepare financial statements activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_prepare_financial_statements", "rar_sha256": "ce1741413f97a866adfbd9377b914abeeb732631434f13cdc85ad89425425095", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_prepare_financial_statements_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-prepare-financial-statements:d17df272028ab1b81428eae7f444e3992ae7cec3f7ce3f024f812015f66c0bb1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_prepare_financial_statements`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_prepare_financial_statements_agent.py` is
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

Prepare financial statements Summary Report — Builds a structured summary report of prepare financial statements activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-prepare-financial-statements
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_prepare_financial_statements_agent.py` and embedded as the fenced Python below (sha256 ce1741413f97a866…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_prepare_financial_statements_agent.py` first:

```bash
python3 report_prepare_financial_statements_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_prepare_financial_statements_agent.py   # or on stdin
python3 report_prepare_financial_statements_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare financial statements Summary Report — Builds a structured summary report of prepare financial statements activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-prepare-financial-statements
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_prepare_financial_statements',
    "version": '2.0.0',
    "display_name": 'Prepare financial statements Summary Report',
    "description": 'Builds a structured summary report of prepare financial statements activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-prepare-financial-statements',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-prepare-financial-statements',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8c46747fd6e6cfa9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods/prepare-financial-statements'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-prepare-financial-statements', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportPrepareFinancialStatements(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPrepareFinancialStatements'
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
    print(ReportPrepareFinancialStatements().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
