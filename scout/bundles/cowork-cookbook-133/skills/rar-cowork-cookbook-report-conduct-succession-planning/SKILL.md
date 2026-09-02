---
name: "rar-cowork-cookbook-report-conduct-succession-planning"
description: "Builds a structured summary report of conduct succession planning activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_succession_planning", "rar_sha256": "8e2f49c6b6d387b8197addf8ef9639cc997d45a9d885fbe96ed118eb944cd5cf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_conduct_succession_planning_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-conduct-succession-planning:81921af11f2d98efede8e2a68a1e98366517659422a5939ade82c0a6a3f700a4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_conduct_succession_planning`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_conduct_succession_planning_agent.py` is
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

Conduct succession planning Summary Report — Builds a structured summary report of conduct succession planning activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-succession-planning
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_succession_planning_agent.py` and embedded as the fenced Python below (sha256 8e2f49c6b6d387b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_succession_planning_agent.py` first:

```bash
python3 report_conduct_succession_planning_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_conduct_succession_planning_agent.py   # or on stdin
python3 report_conduct_succession_planning_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct succession planning Summary Report — Builds a structured summary report of conduct succession planning activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-succession-planning
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_conduct_succession_planning',
    "version": '2.0.0',
    "display_name": 'Conduct succession planning Summary Report',
    "description": 'Builds a structured summary report of conduct succession planning activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-conduct-succession-planning',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-conduct-succession-planning',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd669d7786914d530',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/offboard-talent/conduct-succession-planning'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-conduct-succession-planning', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportConductSuccessionPlanning(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConductSuccessionPlanning'
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
    print(ReportConductSuccessionPlanning().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
