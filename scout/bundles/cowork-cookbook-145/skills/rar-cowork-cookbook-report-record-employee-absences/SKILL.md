---
name: "rar-cowork-cookbook-report-record-employee-absences"
description: "Builds a structured summary report of record employee absences activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_employee_absences", "rar_sha256": "b18eede1df10d5266387221a5888987fd980bb95f3b752d7faee99cf08681878", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_record_employee_absences_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-record-employee-absences:c29a3525a060523562c17e712d82b270480a0cd3f745b06311eeec167ac429db", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_record_employee_absences`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_record_employee_absences_agent.py` is
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

Record employee absences Summary Report — Builds a structured summary report of record employee absences activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-record-employee-absences
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_record_employee_absences_agent.py` and embedded as the fenced Python below (sha256 b18eede1df10d526…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_record_employee_absences_agent.py` first:

```bash
python3 report_record_employee_absences_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_record_employee_absences_agent.py   # or on stdin
python3 report_record_employee_absences_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record employee absences Summary Report — Builds a structured summary report of record employee absences activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-record-employee-absences
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_record_employee_absences',
    "version": '2.0.0',
    "display_name": 'Record employee absences Summary Report',
    "description": 'Builds a structured summary report of record employee absences activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-record-employee-absences',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-record-employee-absences',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9cab6e79257eab1d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-time-and-attendance/record-employee-absences'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-record-employee-absences', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportRecordEmployeeAbsences(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRecordEmployeeAbsences'
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
    print(ReportRecordEmployeeAbsences().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
