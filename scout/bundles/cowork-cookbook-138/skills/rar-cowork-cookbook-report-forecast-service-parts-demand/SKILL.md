---
name: "rar-cowork-cookbook-report-forecast-service-parts-demand"
description: "Builds a structured summary report of forecast service parts demand activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_forecast_service_parts_demand", "rar_sha256": "a43bbf8a356570952434a42d396e21f79a167878b165d5ccf42319d96107b7ba", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_forecast_service_parts_demand_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-forecast-service-parts-demand:a1fd1d23d13d0b5fcc6800316d87497bdbe5c2170517580fdf68f08ec03ecd6f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_forecast_service_parts_demand`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_forecast_service_parts_demand_agent.py` is
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
