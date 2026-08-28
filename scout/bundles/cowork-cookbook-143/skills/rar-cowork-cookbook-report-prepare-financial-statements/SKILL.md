---
name: "rar-cowork-cookbook-report-prepare-financial-statements"
description: "Builds a structured summary report of prepare financial statements activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_prepare_financial_statements", "rar_sha256": "5ad9c8be5ef781f419ed0e68615dd96826bbfe94d4e675ba43879eef3340d73d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_prepare_financial_statements_agent.py` and embedded as the fenced Python below (sha256 5ad9c8be5ef781f4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_prepare_financial_statements_agent.py` first:

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
    "version": '2.0.1',
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
