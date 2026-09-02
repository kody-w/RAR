---
name: "rar-cowork-cookbook-report-monitor-operational-performance"
description: "Builds a structured summary report of monitor operational performance activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_operational_performance", "rar_sha256": "dffa677edbc90d5efe7e4e46ab0b40fe31d4f92a9d2a45a8e0e20205929c1d7f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_monitor_operational_performance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-monitor-operational-performance:792699bfcffd230516d6b320d5afdf70af59322cb0c6c3b385255b0b3965820f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_monitor_operational_performance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_monitor_operational_performance_agent.py` is
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
