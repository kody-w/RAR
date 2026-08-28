---
name: "rar-cowork-cookbook-report-record-employee-absences"
description: "Builds a structured summary report of record employee absences activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_employee_absences", "rar_sha256": "ffb4fb18e4fe6ed8bed3f7d77a8160be3f024f815c00d93f9ea5760c8fab0cf8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_record_employee_absences_agent.py` and embedded as the fenced Python below (sha256 ffb4fb18e4fe6ed8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_record_employee_absences_agent.py` first:

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
    "version": '2.0.1',
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
