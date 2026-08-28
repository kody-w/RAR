---
name: "rar-cowork-cookbook-report-define-environment-strategy"
description: "Builds a structured summary report of define environment strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_environment_strategy", "rar_sha256": "720e1962226929d6a0f795623fd4b37aeb9de1601917c41e4f4e0161bcf751dc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_environment_strategy`. The original RAPP
agent is preserved byte-for-byte in `report_define_environment_strategy_agent.py` and in the RCI capsule.

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

Define environment strategy Summary Report — Builds a structured summary report of define environment strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-environment-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_environment_strategy_agent.py` and embedded as the fenced Python below (sha256 720e1962226929d6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_environment_strategy_agent.py` first:

```bash
python3 report_define_environment_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_environment_strategy_agent.py   # or on stdin
python3 report_define_environment_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define environment strategy Summary Report — Builds a structured summary report of define environment strategy activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-define-environment-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_environment_strategy',
    "version": '2.0.1',
    "display_name": 'Define environment strategy Summary Report',
    "description": 'Builds a structured summary report of define environment strategy activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-define-environment-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-environment-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '799c1948dd607dd3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-environment-strategy'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-define-environment-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportDefineEnvironmentStrategy(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineEnvironmentStrategy'
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
    print(ReportDefineEnvironmentStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
