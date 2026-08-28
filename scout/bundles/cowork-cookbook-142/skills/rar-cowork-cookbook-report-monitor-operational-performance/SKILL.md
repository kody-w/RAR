---
name: "rar-cowork-cookbook-report-monitor-operational-performance"
description: "Builds a structured summary report of monitor operational performance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_operational_performance", "rar_sha256": "2acb52a39fa055576c0015fd68a476b67a531fef20e7b09b5587b80212c68453", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_monitor_operational_performance_agent.py` and embedded as the fenced Python below (sha256 2acb52a39fa05557…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_monitor_operational_performance_agent.py` first:

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
    "version": '2.0.1',
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
