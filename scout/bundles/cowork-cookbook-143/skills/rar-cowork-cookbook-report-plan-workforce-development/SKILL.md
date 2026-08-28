---
name: "rar-cowork-cookbook-report-plan-workforce-development"
description: "Builds a structured summary report of plan workforce development activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_workforce_development", "rar_sha256": "b11ab4d604973877d39d0dc17f83e61df32fe8a2011d145d6d35d09686c4db4e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_plan_workforce_development`. The original RAPP
agent is preserved byte-for-byte in `report_plan_workforce_development_agent.py` and in the RCI capsule.

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

Plan workforce development Summary Report — Builds a structured summary report of plan workforce development activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-workforce-development
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_workforce_development_agent.py` and embedded as the fenced Python below (sha256 b11ab4d604973877…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_workforce_development_agent.py` first:

```bash
python3 report_plan_workforce_development_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_plan_workforce_development_agent.py   # or on stdin
python3 report_plan_workforce_development_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce development Summary Report — Builds a structured summary report of plan workforce development activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-workforce-development
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_plan_workforce_development',
    "version": '2.0.0',
    "display_name": 'Plan workforce development Summary Report',
    "description": 'Builds a structured summary report of plan workforce development activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-plan-workforce-development',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-plan-workforce-development',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a5b14bcbf13cac5c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-workforce-development'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-plan-workforce-development', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportPlanWorkforceDevelopment(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPlanWorkforceDevelopment'
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
    print(ReportPlanWorkforceDevelopment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
