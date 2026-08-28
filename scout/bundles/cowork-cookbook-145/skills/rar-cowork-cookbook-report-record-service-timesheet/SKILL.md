---
name: "rar-cowork-cookbook-report-record-service-timesheet"
description: "Builds a structured summary report of record service timesheet activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_service_timesheet", "rar_sha256": "4940f4445fe948fd5b3379ca65881d01e9634358010f9251e180c2eae8195bde", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_record_service_timesheet`. The original RAPP
agent is preserved byte-for-byte in `report_record_service_timesheet_agent.py` and in the RCI capsule.

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

Record service timesheet Summary Report — Builds a structured summary report of record service timesheet activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-record-service-timesheet
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_record_service_timesheet_agent.py` and embedded as the fenced Python below (sha256 4940f4445fe948fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_record_service_timesheet_agent.py` first:

```bash
python3 report_record_service_timesheet_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_record_service_timesheet_agent.py   # or on stdin
python3 report_record_service_timesheet_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record service timesheet Summary Report — Builds a structured summary report of record service timesheet activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-record-service-timesheet
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_record_service_timesheet',
    "version": '2.0.0',
    "display_name": 'Record service timesheet Summary Report',
    "description": 'Builds a structured summary report of record service timesheet activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-record-service-timesheet',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-record-service-timesheet',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a5383cdb93a7be49',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/record-service-timesheet'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-record-service-timesheet', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportRecordServiceTimesheet(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRecordServiceTimesheet'
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
    print(ReportRecordServiceTimesheet().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
