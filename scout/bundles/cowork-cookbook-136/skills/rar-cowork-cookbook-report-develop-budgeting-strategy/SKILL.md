---
name: "rar-cowork-cookbook-report-develop-budgeting-strategy"
description: "Builds a structured summary report of develop budgeting strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_budgeting_strategy", "rar_sha256": "75801bc8918ebe9b66aa7eac41ff8c0d873c82a94a42758926864dd8a2dcf91b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_budgeting_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_develop_budgeting_strategy_agent.py` and in the RCI capsule.

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

Develop budgeting strategy Summary Report — Builds a structured summary report of develop budgeting strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-budgeting-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_budgeting_strategy_agent.py` and embedded as the fenced Python below (sha256 75801bc8918ebe9b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_budgeting_strategy_agent.py` first:

```bash
python3 report_develop_budgeting_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_budgeting_strategy_agent.py   # or on stdin
python3 report_develop_budgeting_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop budgeting strategy Summary Report — Builds a structured summary report of develop budgeting strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-budgeting-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_budgeting_strategy',
    "version": '2.0.0',
    "display_name": 'Develop budgeting strategy Summary Report',
    "description": 'Builds a structured summary report of develop budgeting strategy activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-develop-budgeting-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-budgeting-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a50ba7a97f79d4a0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-budgeting-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-develop-budgeting-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportDevelopBudgetingStrategy(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopBudgetingStrategy'
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
    print(ReportDevelopBudgetingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
