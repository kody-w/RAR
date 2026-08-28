---
name: "rar-cowork-cookbook-report-prepare-financial-statements"
description: "Builds a structured summary report of prepare financial statements activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_prepare_financial_statements", "rar_sha256": "ce1741413f97a866adfbd9377b914abeeb732631434f13cdc85ad89425425095", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_prepare_financial_statements`. The original RAPP
agent is preserved byte-for-byte in `report_prepare_financial_statements_agent.py` and in the RCI capsule.

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
