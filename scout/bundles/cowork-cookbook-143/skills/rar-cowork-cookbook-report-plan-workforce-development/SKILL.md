---
name: "rar-cowork-cookbook-report-plan-workforce-development"
description: "Builds a structured summary report of plan workforce development activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_workforce_development", "rar_sha256": "84b41169417dd1b249896bbe647dc03bdb962b4fc29835f7de883df0b41e4242", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_workforce_development_agent.py` and embedded as the fenced Python below (sha256 84b41169417dd1b2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_workforce_development_agent.py` first:

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
    "version": '2.0.1',
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
