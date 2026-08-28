---
name: "rar-cowork-cookbook-report-define-operating-hours"
description: "Builds a structured summary report of define operating hours activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_operating_hours", "rar_sha256": "19bef8588ad4c4f059095fc4fc372304f41678e401535f7e9181edb56f8cc19e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_operating_hours`. The original RAPP
agent is preserved byte-for-byte in `report_define_operating_hours_agent.py` and in the RCI capsule.

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

Define operating hours Summary Report — Builds a structured summary report of define operating hours activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-operating-hours
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_operating_hours_agent.py` and embedded as the fenced Python below (sha256 19bef8588ad4c4f0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_operating_hours_agent.py` first:

```bash
python3 report_define_operating_hours_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_operating_hours_agent.py   # or on stdin
python3 report_define_operating_hours_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define operating hours Summary Report — Builds a structured summary report of define operating hours activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-operating-hours
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_operating_hours',
    "version": '2.0.1',
    "display_name": 'Define operating hours Summary Report',
    "description": 'Builds a structured summary report of define operating hours activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-operating-hours',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-operating-hours',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eda323bd08f19fe4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-operating-hours'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-define-operating-hours', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.286, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportDefineOperatingHours(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineOperatingHours'
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
    print(ReportDefineOperatingHours().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
