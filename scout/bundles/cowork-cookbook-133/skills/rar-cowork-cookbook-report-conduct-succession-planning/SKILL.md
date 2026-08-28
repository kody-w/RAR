---
name: "rar-cowork-cookbook-report-conduct-succession-planning"
description: "Builds a structured summary report of conduct succession planning activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_succession_planning", "rar_sha256": "121913b49fd63420f63ae8380341dc054634c4be06b3d99bfed6de6989a0eb06", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_succession_planning_agent.py` and embedded as the fenced Python below (sha256 121913b49fd63420…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_succession_planning_agent.py` first:

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
    "version": '2.0.1',
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
