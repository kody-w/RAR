---
name: "rar-cowork-cookbook-report-define-integration-strategy"
description: "Builds a structured summary report of define integration strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_integration_strategy", "rar_sha256": "ee89163d0c7f961e4ee9946df07ffbfed3dbfa853adbaff8b7e2f33e698847ce", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_integration_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_define_integration_strategy_agent.py` and in the RCI capsule.

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

Define integration strategy Summary Report — Builds a structured summary report of define integration strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-integration-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_integration_strategy_agent.py` and embedded as the fenced Python below (sha256 ee89163d0c7f961e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_integration_strategy_agent.py` first:

```bash
python3 report_define_integration_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_integration_strategy_agent.py   # or on stdin
python3 report_define_integration_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define integration strategy Summary Report — Builds a structured summary report of define integration strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-integration-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_integration_strategy',
    "version": '2.0.1',
    "display_name": 'Define integration strategy Summary Report',
    "description": 'Builds a structured summary report of define integration strategy activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-integration-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-integration-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '704d7abe534fcb6f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-integration-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-define-integration-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDefineIntegrationStrategy(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineIntegrationStrategy'
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
    print(ReportDefineIntegrationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
