---
name: "rar-cowork-cookbook-report-define-queues-and-teams"
description: "Builds a structured summary report of define queues and teams activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_queues_and_teams", "rar_sha256": "e2d593aa5bbb243d28154174431557d164c8bde90c2cb7ea405aba9510b062d0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_queues_and_teams`. The original RAPP
agent is preserved byte-for-byte in `report_define_queues_and_teams_agent.py` and in the RCI capsule.

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
