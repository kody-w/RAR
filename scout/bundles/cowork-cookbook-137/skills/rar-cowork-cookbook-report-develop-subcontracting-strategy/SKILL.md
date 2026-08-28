---
name: "rar-cowork-cookbook-report-develop-subcontracting-strategy"
description: "Builds a structured summary report of develop subcontracting strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_subcontracting_strategy", "rar_sha256": "756f277aaccab34abf1bcd4e426c642f0c58e4a806515f0fcbdbaaa7d1053ae8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_subcontracting_strategy_agent.py` and embedded as the fenced Python below (sha256 756f277aaccab34a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_subcontracting_strategy_agent.py` first:

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
    "version": '2.0.0',
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
