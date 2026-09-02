---
name: "rar-cowork-cookbook-report-record-service-timesheet"
description: "Builds a structured summary report of record service timesheet activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_service_timesheet", "rar_sha256": "4940f4445fe948fd5b3379ca65881d01e9634358010f9251e180c2eae8195bde", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_record_service_timesheet_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-record-service-timesheet:f64e8ba52839db9274d143f273310ebf9a90fd3bbc6b4b3b139e420d4ab509c5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_record_service_timesheet`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_record_service_timesheet_agent.py` is
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
