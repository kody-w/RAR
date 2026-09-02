---
name: "rar-cowork-cookbook-report-define-project-stakeholders"
description: "Builds a structured summary report of define project stakeholders activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_project_stakeholders", "rar_sha256": "a25880a486953ad3c35031a1050abbe5e8c28688c997375e6cd8370b56d570d6", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_define_project_stakeholders_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-define-project-stakeholders:e8ba010bc67611f840f928aac5d49ac13891ec67e3446e85ae6373bd599d4c11", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_define_project_stakeholders`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_define_project_stakeholders_agent.py` is
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

Define project stakeholders Summary Report — Builds a structured summary report of define project stakeholders activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-project-stakeholders
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_project_stakeholders_agent.py` and embedded as the fenced Python below (sha256 a25880a486953ad3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_project_stakeholders_agent.py` first:

```bash
python3 report_define_project_stakeholders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_project_stakeholders_agent.py   # or on stdin
python3 report_define_project_stakeholders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define project stakeholders Summary Report — Builds a structured summary report of define project stakeholders activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-project-stakeholders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_project_stakeholders',
    "version": '2.0.0',
    "display_name": 'Define project stakeholders Summary Report',
    "description": 'Builds a structured summary report of define project stakeholders activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-define-project-stakeholders',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-project-stakeholders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a6e0e31b02135889',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/define-project-stakeholders'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/report-define-project-stakeholders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDefineProjectStakeholders(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineProjectStakeholders'
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
    print(ReportDefineProjectStakeholders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
