---
name: "rar-cowork-cookbook-report-monitor-operational-performance"
description: "Builds a structured summary report of monitor operational performance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_operational_performance", "rar_sha256": "dffa677edbc90d5efe7e4e46ab0b40fe31d4f92a9d2a45a8e0e20205929c1d7f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_monitor_operational_performance`. The original RAPP
agent is preserved byte-for-byte in `report_monitor_operational_performance_agent.py` and in the RCI capsule.

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

Monitor operational performance Summary Report — Builds a structured summary report of monitor operational performance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-operational-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_monitor_operational_performance_agent.py` and embedded as the fenced Python below (sha256 dffa677edbc90d5e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_monitor_operational_performance_agent.py` first:

```bash
python3 report_monitor_operational_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_monitor_operational_performance_agent.py   # or on stdin
python3 report_monitor_operational_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor operational performance Summary Report — Builds a structured summary report of monitor operational performance activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-operational-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_monitor_operational_performance',
    "version": '2.0.0',
    "display_name": 'Monitor operational performance Summary Report',
    "description": 'Builds a structured summary report of monitor operational performance activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-monitor-operational-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-monitor-operational-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'da0cce4cb391c3c6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/monitor-operational-performance'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-monitor-operational-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportMonitorOperationalPerformance(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMonitorOperationalPerformance'
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
    print(ReportMonitorOperationalPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
