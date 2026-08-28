---
name: "rar-cowork-cookbook-report-forecast-service-parts-demand"
description: "Builds a structured summary report of forecast service parts demand activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_forecast_service_parts_demand", "rar_sha256": "475e5ab030b591cc91c10585ebb00cebdd26a883a896c00ce63d7a3e2c85c4d1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_forecast_service_parts_demand`. The original RAPP
agent is preserved byte-for-byte in `report_forecast_service_parts_demand_agent.py` and in the RCI capsule.

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

Forecast service parts demand Summary Report — Builds a structured summary report of forecast service parts demand activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-forecast-service-parts-demand
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_forecast_service_parts_demand_agent.py` and embedded as the fenced Python below (sha256 475e5ab030b591cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_forecast_service_parts_demand_agent.py` first:

```bash
python3 report_forecast_service_parts_demand_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_forecast_service_parts_demand_agent.py   # or on stdin
python3 report_forecast_service_parts_demand_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast service parts demand Summary Report — Builds a structured summary report of forecast service parts demand activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-forecast-service-parts-demand
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_forecast_service_parts_demand',
    "version": '2.0.1',
    "display_name": 'Forecast service parts demand Summary Report',
    "description": 'Builds a structured summary report of forecast service parts demand activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-forecast-service-parts-demand',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-forecast-service-parts-demand',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '69de6d5b7b0297f5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/plan-service-work/forecast-service-parts-demand'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-forecast-service-parts-demand', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportForecastServicePartsDemand(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportForecastServicePartsDemand'
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
    print(ReportForecastServicePartsDemand().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
