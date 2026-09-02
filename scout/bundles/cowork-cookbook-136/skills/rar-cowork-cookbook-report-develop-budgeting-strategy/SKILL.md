---
name: "rar-cowork-cookbook-report-develop-budgeting-strategy"
description: "Builds a structured summary report of develop budgeting strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_budgeting_strategy", "rar_sha256": "75801bc8918ebe9b66aa7eac41ff8c0d873c82a94a42758926864dd8a2dcf91b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_develop_budgeting_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-develop-budgeting-strategy:88cea0d49f3a811bde51af30458fc0e28ef4dc708435a97be3b0ff6a484689b0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_develop_budgeting_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_develop_budgeting_strategy_agent.py` is
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
