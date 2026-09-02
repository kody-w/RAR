---
name: "rar-cowork-cookbook-report-forecast-revenue"
description: "Builds a structured summary report of forecast revenue activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_forecast_revenue", "rar_sha256": "d724d53836bcc919b9421181f34cf5cbda6ffd5663a771923f8c8f7d241d131b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_forecast_revenue_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-forecast-revenue:f98f74de5a3da6e3ec43d5c5d235b7cddc2f359ee5a92108296684ddd7d4119c", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_forecast_revenue`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_forecast_revenue_agent.py` is
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
