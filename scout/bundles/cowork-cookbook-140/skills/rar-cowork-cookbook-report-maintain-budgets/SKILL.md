---
name: "rar-cowork-cookbook-report-maintain-budgets"
description: "Builds a structured summary report of maintain budgets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_budgets", "rar_sha256": "cd2434c875d3fbcdda97360431f972856f97af4fa81d0391a0a2d4480a33323c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_maintain_budgets`. The original RAPP
agent is preserved byte-for-byte in `report_maintain_budgets_agent.py` and in the RCI capsule.

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
