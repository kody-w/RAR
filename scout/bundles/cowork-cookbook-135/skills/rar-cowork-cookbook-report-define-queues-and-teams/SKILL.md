---
name: "rar-cowork-cookbook-report-define-queues-and-teams"
description: "Builds a structured summary report of define queues and teams activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_queues_and_teams", "rar_sha256": "e2d593aa5bbb243d28154174431557d164c8bde90c2cb7ea405aba9510b062d0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_define_queues_and_teams_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-define-queues-and-teams:40da017e6c7fd6066365d38351b4872127000ee6a1bde0ac5ca5271a7d716506", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_define_queues_and_teams`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_define_queues_and_teams_agent.py` is
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

Define queues and teams Summary Report — Builds a structured summary report of define queues and teams activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-queues-and-teams
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_queues_and_teams_agent.py` and embedded as the fenced Python below (sha256 e2d593aa5bbb243d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_queues_and_teams_agent.py` first:

```bash
python3 report_define_queues_and_teams_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_queues_and_teams_agent.py   # or on stdin
python3 report_define_queues_and_teams_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define queues and teams Summary Report — Builds a structured summary report of define queues and teams activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-queues-and-teams
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_queues_and_teams',
    "version": '2.0.0',
    "display_name": 'Define queues and teams Summary Report',
    "description": 'Builds a structured summary report of define queues and teams activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-define-queues-and-teams',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-queues-and-teams',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '48207bc4931ad76e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-queues-and-teams'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-define-queues-and-teams', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDefineQueuesAndTeams(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineQueuesAndTeams'
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
    print(ReportDefineQueuesAndTeams().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
