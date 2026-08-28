---
name: "rar-cowork-cookbook-report-correct-project-transactions"
description: "Builds a structured summary report of correct project transactions activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_correct_project_transactions", "rar_sha256": "e566e92a87d3d82f80b2430bfb9817aa0e07c855f313fa0027641aab6c8171bd", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_correct_project_transactions`. The original RAPP
agent is preserved byte-for-byte in `report_correct_project_transactions_agent.py` and in the RCI capsule.

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

Correct project transactions Summary Report — Builds a structured summary report of correct project transactions activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-correct-project-transactions
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_correct_project_transactions_agent.py` and embedded as the fenced Python below (sha256 e566e92a87d3d82f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_correct_project_transactions_agent.py` first:

```bash
python3 report_correct_project_transactions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_correct_project_transactions_agent.py   # or on stdin
python3 report_correct_project_transactions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Correct project transactions Summary Report — Builds a structured summary report of correct project transactions activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-correct-project-transactions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_correct_project_transactions',
    "version": '2.0.1',
    "display_name": 'Correct project transactions Summary Report',
    "description": 'Builds a structured summary report of correct project transactions activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-correct-project-transactions',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-correct-project-transactions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f33793b05438a850',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-financials/correct-project-transactions'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-correct-project-transactions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportCorrectProjectTransactions(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCorrectProjectTransactions'
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
    print(ReportCorrectProjectTransactions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
