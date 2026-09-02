---
name: "rar-cowork-cookbook-report-correct-project-transactions"
description: "Builds a structured summary report of correct project transactions activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_correct_project_transactions", "rar_sha256": "430fabafe3fff8a37beff7ddbd75184ab73e26e5095366b5b64bac9323d37c66", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_correct_project_transactions_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-correct-project-transactions:330074d8aa195ddfbba76416d39cd9e737064de575fea8aa056427ae6c498ef7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_correct_project_transactions`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_correct_project_transactions_agent.py` is
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
