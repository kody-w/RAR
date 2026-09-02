---
name: "rar-cowork-cookbook-report-track-skills-and-competencies"
description: "Builds a structured summary report of track skills and competencies activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_track_skills_and_competencies", "rar_sha256": "1f43b1d9a3c679d631cc4e1a3c94a32a68f89f04b96600ea41c040e5b5485b18", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_track_skills_and_competencies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-track-skills-and-competencies:61cd31b8b78a59dddf6765b4dc3c64741338a3f787fa8b516da9dca2aec972f4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_track_skills_and_competencies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_track_skills_and_competencies_agent.py` is
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

Track skills and competencies Summary Report — Builds a structured summary report of track skills and competencies activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-track-skills-and-competencies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_track_skills_and_competencies_agent.py` and embedded as the fenced Python below (sha256 1f43b1d9a3c679d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_track_skills_and_competencies_agent.py` first:

```bash
python3 report_track_skills_and_competencies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_track_skills_and_competencies_agent.py   # or on stdin
python3 report_track_skills_and_competencies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Track skills and competencies Summary Report — Builds a structured summary report of track skills and competencies activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-track-skills-and-competencies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_track_skills_and_competencies',
    "version": '2.0.0',
    "display_name": 'Track skills and competencies Summary Report',
    "description": 'Builds a structured summary report of track skills and competencies activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-track-skills-and-competencies',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-track-skills-and-competencies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7fd32993af6a78b9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/track-skills-and-competencies'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-track-skills-and-competencies', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportTrackSkillsAndCompetencies(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTrackSkillsAndCompetencies'
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
    print(ReportTrackSkillsAndCompetencies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
