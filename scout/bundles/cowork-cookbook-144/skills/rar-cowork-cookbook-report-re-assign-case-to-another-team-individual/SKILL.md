---
name: "rar-cowork-cookbook-report-re-assign-case-to-another-team-individual"
description: "Builds a structured summary report of re-assign case to another team/individual activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_re_assign_case_to_another_team_individual", "rar_sha256": "c07a7a2ba01458b1067a2f72ac17b40aeac6926a5b97c0c5bf2f8215fae7ca4d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_re_assign_case_to_another_team_individual_agent.py` and embedded as the fenced Python below (sha256 c07a7a2ba01458b1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_re_assign_case_to_another_team_individual_agent.py` first:

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
    "version": '2.0.0',
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
