---
name: "rar-cowork-cookbook-report-monitor-service-quality"
description: "Builds a structured summary report of monitor service quality activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_monitor_service_quality", "rar_sha256": "c143fed57fe7c4685595318aaaf56db5c1b78dcd6558bc4047616578ec106fb1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_monitor_service_quality_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-monitor-service-quality:258da860f08b7307d028bc2657b6937bb7cedf55487a64cc5142d810bbbdca7b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_monitor_service_quality`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_monitor_service_quality_agent.py` is
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
