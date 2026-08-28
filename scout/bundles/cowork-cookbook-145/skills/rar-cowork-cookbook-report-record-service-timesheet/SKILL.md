---
name: "rar-cowork-cookbook-report-record-service-timesheet"
description: "Builds a structured summary report of record service timesheet activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_service_timesheet", "rar_sha256": "909e10e2bce560a7055e2e5357bb11dde11c8278233f0ec8c14dde6d30873b24", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_record_service_timesheet_agent.py` and embedded as the fenced Python below (sha256 909e10e2bce560a7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_record_service_timesheet_agent.py` first:

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
    "version": '2.0.1',
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
