---
name: "rar-cowork-cookbook-report-monitor-service-quality"
description: "Builds a structured summary report of monitor service quality activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_service_quality", "rar_sha256": "2b6021db422b3e574fc3f6f954a247af871d219f3f1888b455e368720159d0d9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_monitor_service_quality_agent.py` and embedded as the fenced Python below (sha256 2b6021db422b3e57…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_monitor_service_quality_agent.py` first:

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
    "version": '2.0.1',
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
