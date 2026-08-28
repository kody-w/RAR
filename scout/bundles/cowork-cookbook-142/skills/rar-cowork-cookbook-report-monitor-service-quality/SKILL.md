---
name: "rar-cowork-cookbook-report-monitor-service-quality"
description: "Builds a structured summary report of monitor service quality activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_service_quality", "rar_sha256": "c143fed57fe7c4685595318aaaf56db5c1b78dcd6558bc4047616578ec106fb1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_monitor_service_quality`. The original RAPP
agent is preserved byte-for-byte in `report_monitor_service_quality_agent.py` and in the RCI capsule.

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

Monitor service quality Summary Report — Builds a structured summary report of monitor service quality activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-service-quality
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_monitor_service_quality_agent.py` and embedded as the fenced Python below (sha256 c143fed57fe7c468…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_monitor_service_quality_agent.py` first:

```bash
python3 report_monitor_service_quality_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_monitor_service_quality_agent.py   # or on stdin
python3 report_monitor_service_quality_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor service quality Summary Report — Builds a structured summary report of monitor service quality activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-monitor-service-quality
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_monitor_service_quality',
    "version": '2.0.0',
    "display_name": 'Monitor service quality Summary Report',
    "description": 'Builds a structured summary report of monitor service quality activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-monitor-service-quality',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-monitor-service-quality',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '12ada7560f200d6b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/monitor-service-quality'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-monitor-service-quality', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportMonitorServiceQuality(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportMonitorServiceQuality'
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
    print(ReportMonitorServiceQuality().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
