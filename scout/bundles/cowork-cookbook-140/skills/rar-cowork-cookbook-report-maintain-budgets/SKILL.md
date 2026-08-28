---
name: "rar-cowork-cookbook-report-maintain-budgets"
description: "Builds a structured summary report of maintain budgets activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_maintain_budgets", "rar_sha256": "fd26b7a76c69100cc0c99ff9864629b3e748532953c4607e6cc2ccdb85056137", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_maintain_budgets_agent.py` and embedded as the fenced Python below (sha256 fd26b7a76c69100c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_maintain_budgets_agent.py` first:

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
    "version": '2.0.1',
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
