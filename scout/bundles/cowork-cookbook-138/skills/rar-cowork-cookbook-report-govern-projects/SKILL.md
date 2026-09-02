---
name: "rar-cowork-cookbook-report-govern-projects"
description: "Builds a structured summary report of govern projects activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_govern_projects", "rar_sha256": "9eb84b632b246a3b372b392a203f6cd3783ee6ea7897c90d46d33181a9a48600", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_govern_projects_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-govern-projects:48900b582159218733838f6d2befbc062c3eba09359b3fcad0308e95b8535c99", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_govern_projects`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_govern_projects_agent.py` is
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

Govern projects Summary Report — Builds a structured summary report of govern projects activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-govern-projects
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_govern_projects_agent.py` and embedded as the fenced Python below (sha256 9eb84b632b246a3b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_govern_projects_agent.py` first:

```bash
python3 report_govern_projects_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_govern_projects_agent.py   # or on stdin
python3 report_govern_projects_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Govern projects Summary Report — Builds a structured summary report of govern projects activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-govern-projects
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_govern_projects',
    "version": '2.0.0',
    "display_name": 'Govern projects Summary Report',
    "description": 'Builds a structured summary report of govern projects activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-govern-projects',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-govern-projects',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '57acd2619178a5de',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery/govern-projects'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-govern-projects', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportGovernProjects(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportGovernProjects'
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
    print(ReportGovernProjects().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
