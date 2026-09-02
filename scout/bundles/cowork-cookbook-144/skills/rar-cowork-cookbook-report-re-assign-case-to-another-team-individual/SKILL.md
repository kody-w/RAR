---
name: "rar-cowork-cookbook-report-re-assign-case-to-another-team-individual"
description: "Builds a structured summary report of re-assign case to another team/individual activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_re_assign_case_to_another_team_individual", "rar_sha256": "c07a7a2ba01458b1067a2f72ac17b40aeac6926a5b97c0c5bf2f8215fae7ca4d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_re_assign_case_to_another_team_individual_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-re-assign-case-to-another-team-individual:857581eb3a18d443f61795d005547184a2aa05a743d1273122d53e017c728ead", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_re_assign_case_to_another_team_individual`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_re_assign_case_to_another_team_individual_agent.py` is
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
