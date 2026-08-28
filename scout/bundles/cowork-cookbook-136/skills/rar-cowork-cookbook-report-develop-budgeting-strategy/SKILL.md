---
name: "rar-cowork-cookbook-report-develop-budgeting-strategy"
description: "Builds a structured summary report of develop budgeting strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_budgeting_strategy", "rar_sha256": "1ea076604d324fb39f8f3e5ccaca88555074aaf70e49fef287be1299d0b8548c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_budgeting_strategy_agent.py` and embedded as the fenced Python below (sha256 1ea076604d324fb3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_budgeting_strategy_agent.py` first:

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
    "version": '2.0.1',
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
