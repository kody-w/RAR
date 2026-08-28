---
name: "rar-cowork-cookbook-report-correct-project-transactions"
description: "Builds a structured summary report of correct project transactions activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_correct_project_transactions", "rar_sha256": "430fabafe3fff8a37beff7ddbd75184ab73e26e5095366b5b64bac9323d37c66", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_correct_project_transactions_agent.py` and embedded as the fenced Python below (sha256 430fabafe3fff8a3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_correct_project_transactions_agent.py` first:

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
    "version": '2.0.0',
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
