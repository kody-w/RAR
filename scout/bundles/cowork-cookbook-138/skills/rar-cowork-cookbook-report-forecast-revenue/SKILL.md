---
name: "rar-cowork-cookbook-report-forecast-revenue"
description: "Builds a structured summary report of forecast revenue activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_forecast_revenue", "rar_sha256": "0abe8dca70d0ce433f4f67aa380b3ad41933fd745d1f246818a9b44b2cc0299a", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_forecast_revenue`. The original RAPP
agent is preserved byte-for-byte in `report_forecast_revenue_agent.py` and in the RCI capsule.

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

Forecast revenue Summary Report — Builds a structured summary report of forecast revenue activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-forecast-revenue
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_forecast_revenue_agent.py` and embedded as the fenced Python below (sha256 0abe8dca70d0ce43…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_forecast_revenue_agent.py` first:

```bash
python3 report_forecast_revenue_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_forecast_revenue_agent.py   # or on stdin
python3 report_forecast_revenue_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Forecast revenue Summary Report — Builds a structured summary report of forecast revenue activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-forecast-revenue
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_forecast_revenue',
    "version": '2.0.1',
    "display_name": 'Forecast revenue Summary Report',
    "description": 'Builds a structured summary report of forecast revenue activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-forecast-revenue',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-forecast-revenue',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '29d6b85f804d5267',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/forecast-revenue'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-forecast-revenue', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportForecastRevenue(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportForecastRevenue'
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
    print(ReportForecastRevenue().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
