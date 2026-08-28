---
name: "rar-cowork-cookbook-report-forecast-revenue"
description: "Builds a structured summary report of forecast revenue activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_forecast_revenue", "rar_sha256": "d724d53836bcc919b9421181f34cf5cbda6ffd5663a771923f8c8f7d241d131b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_forecast_revenue_agent.py` and embedded as the fenced Python below (sha256 d724d53836bcc919…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_forecast_revenue_agent.py` first:

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
    "version": '2.0.0',
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
