---
name: "rar-cowork-cookbook-report-define-integration-strategy"
description: "Builds a structured summary report of define integration strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_integration_strategy", "rar_sha256": "e873a7422de4f7806a841d23978455e85a85fffded713aad335115e078baddc1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_integration_strategy_agent.py` and embedded as the fenced Python below (sha256 e873a7422de4f780…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_integration_strategy_agent.py` first:

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
    "version": '2.0.0',
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
