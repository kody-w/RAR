---
name: "rar-cowork-cookbook-report-record-employee-absences"
description: "Builds a structured summary report of record employee absences activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_employee_absences", "rar_sha256": "b18eede1df10d5266387221a5888987fd980bb95f3b752d7faee99cf08681878", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_record_employee_absences`. The original RAPP
agent is preserved byte-for-byte in `report_record_employee_absences_agent.py` and in the RCI capsule.

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
