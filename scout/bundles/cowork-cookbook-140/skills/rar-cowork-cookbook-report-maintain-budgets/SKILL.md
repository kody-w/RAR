---
name: "rar-cowork-cookbook-report-maintain-budgets"
description: "Builds a structured summary report of maintain budgets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_budgets", "rar_sha256": "cd2434c875d3fbcdda97360431f972856f97af4fa81d0391a0a2d4480a33323c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_maintain_budgets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-maintain-budgets:bc51fc310e430b177a6fe4bfea0b7503ad885e97b02e950e84a2f160dd4955a8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_maintain_budgets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_maintain_budgets_agent.py` is
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

Maintain budgets Summary Report — Builds a structured summary report of maintain budgets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-budgets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_maintain_budgets_agent.py` and embedded as the fenced Python below (sha256 cd2434c875d3fbcd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_maintain_budgets_agent.py` first:

```bash
python3 report_maintain_budgets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_maintain_budgets_agent.py   # or on stdin
python3 report_maintain_budgets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain budgets Summary Report — Builds a structured summary report of maintain budgets activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-maintain-budgets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_maintain_budgets',
    "version": '2.0.0',
    "display_name": 'Maintain budgets Summary Report',
    "description": 'Builds a structured summary report of maintain budgets activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-maintain-budgets',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-maintain-budgets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7fd1674dca5b9cbc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/manage-budgets/maintain-budgets'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-maintain-budgets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class ReportMaintainBudgets(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMaintainBudgets'
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
    print(ReportMaintainBudgets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
