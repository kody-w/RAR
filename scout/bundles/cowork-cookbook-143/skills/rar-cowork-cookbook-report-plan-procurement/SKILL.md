---
name: "rar-cowork-cookbook-report-plan-procurement"
description: "Builds a structured summary report of plan procurement activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_procurement", "rar_sha256": "1d9f587ad4a0247c21fbd2aa2bfdf5477888c43da7e8f2bc7c6f11b071e2faf7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_procurement_agent.py` and embedded as the fenced Python below (sha256 1d9f587ad4a0247c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_procurement_agent.py` first:

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
    "version": '2.0.0',
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
