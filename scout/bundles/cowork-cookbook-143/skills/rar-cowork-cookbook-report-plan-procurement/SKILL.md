---
name: "rar-cowork-cookbook-report-plan-procurement"
description: "Builds a structured summary report of plan procurement activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_procurement", "rar_sha256": "5711c3f7673cee4950bfbdb8f6c7e65989d3f835bcdd2bcb6f9c516c1957d8b3", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_plan_procurement`. The original RAPP
agent is preserved byte-for-byte in `report_plan_procurement_agent.py` and in the RCI capsule.

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

Plan procurement Summary Report — Builds a structured summary report of plan procurement activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-procurement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_procurement_agent.py` and embedded as the fenced Python below (sha256 5711c3f7673cee49…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_procurement_agent.py` first:

```bash
python3 report_plan_procurement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_plan_procurement_agent.py   # or on stdin
python3 report_plan_procurement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan procurement Summary Report — Builds a structured summary report of plan procurement activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-procurement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_plan_procurement',
    "version": '2.0.1',
    "display_name": 'Plan procurement Summary Report',
    "description": 'Builds a structured summary report of plan procurement activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-plan-procurement',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-plan-procurement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fe4520afca1d57ed',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-procurement'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-plan-procurement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportPlanProcurement(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPlanProcurement'
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
    print(ReportPlanProcurement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
