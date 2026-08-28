---
name: "rar-cowork-cookbook-report-develop-subcontracting-strategy"
description: "Builds a structured summary report of develop subcontracting strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_subcontracting_strategy", "rar_sha256": "e2fab874d67712832f176ae693f736c6c7ea897c1cad6bf48ea88f1cc78b6abb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_subcontracting_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_develop_subcontracting_strategy_agent.py` and in the RCI capsule.

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

Develop subcontracting strategy Summary Report — Builds a structured summary report of develop subcontracting strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-subcontracting-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_subcontracting_strategy_agent.py` and embedded as the fenced Python below (sha256 e2fab874d6771283…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_subcontracting_strategy_agent.py` first:

```bash
python3 report_develop_subcontracting_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_subcontracting_strategy_agent.py   # or on stdin
python3 report_develop_subcontracting_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop subcontracting strategy Summary Report — Builds a structured summary report of develop subcontracting strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-subcontracting-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_subcontracting_strategy',
    "version": '2.0.1',
    "display_name": 'Develop subcontracting strategy Summary Report',
    "description": 'Builds a structured summary report of develop subcontracting strategy activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-develop-subcontracting-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-subcontracting-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c84ab8d74db6842b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/develop-subcontracting-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-develop-subcontracting-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDevelopSubcontractingStrategy(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopSubcontractingStrategy'
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
    print(ReportDevelopSubcontractingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
