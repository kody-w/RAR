---
name: "rar-cowork-cookbook-report-conduct-succession-planning"
description: "Builds a structured summary report of conduct succession planning activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_succession_planning", "rar_sha256": "8e2f49c6b6d387b8197addf8ef9639cc997d45a9d885fbe96ed118eb944cd5cf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_conduct_succession_planning`. The original RAPP
agent is preserved byte-for-byte in `report_conduct_succession_planning_agent.py` and in the RCI capsule.

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
