---
name: "rar-cowork-cookbook-report-re-assign-case-to-another-team-individual"
description: "Builds a structured summary report of re-assign case to another team/individual activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_re_assign_case_to_another_team_individual", "rar_sha256": "2d636fea26c38b09c4e8b280ac3ed065dfba500323db9a873ae50b49b3b93adb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_re_assign_case_to_another_team_individual`. The original RAPP
agent is preserved byte-for-byte in `report_re_assign_case_to_another_team_individual_agent.py` and in the RCI capsule.

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

Re-assign case to another team/individual Summary Report — Builds a structured summary report of re-assign case to another team/individual activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-re-assign-case-to-another-team-individual
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_re_assign_case_to_another_team_individual_agent.py` and embedded as the fenced Python below (sha256 2d636fea26c38b09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_re_assign_case_to_another_team_individual_agent.py` first:

```bash
python3 report_re_assign_case_to_another_team_individual_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_re_assign_case_to_another_team_individual_agent.py   # or on stdin
python3 report_re_assign_case_to_another_team_individual_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Re-assign case to another team/individual Summary Report — Builds a structured summary report of re-assign case to another team/individual activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-re-assign-case-to-another-team-individual
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_re_assign_case_to_another_team_individual',
    "version": '2.0.1',
    "display_name": 'Re-assign case to another team/individual Summary Report',
    "description": 'Builds a structured summary report of re-assign case to another team/individual activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-re-assign-case-to-another-team-individual',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-re-assign-case-to-another-team-individual',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b6819e9f70706b23',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/re-assign-case-to-another-team-individual'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-re-assign-case-to-another-team-individual', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportReAssignCaseToAnotherTeamIndividual(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReAssignCaseToAnotherTeamIndividual'
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
    print(ReportReAssignCaseToAnotherTeamIndividual().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
