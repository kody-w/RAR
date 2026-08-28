---
name: "rar-cowork-cookbook-report-forecast-service-parts-demand"
description: "Builds a structured summary report of forecast service parts demand activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_forecast_service_parts_demand", "rar_sha256": "a43bbf8a356570952434a42d396e21f79a167878b165d5ccf42319d96107b7ba", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_forecast_service_parts_demand_agent.py` and embedded as the fenced Python below (sha256 a43bbf8a35657095…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_forecast_service_parts_demand_agent.py` first:

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
    "version": '2.0.0',
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
