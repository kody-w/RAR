---
name: "rar-cowork-cookbook-report-define-integration-strategy"
description: "Builds a structured summary report of define integration strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_integration_strategy", "rar_sha256": "e873a7422de4f7806a841d23978455e85a85fffded713aad335115e078baddc1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_define_integration_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-define-integration-strategy:1a675dd233d2de817736a45c1135fb69a38ebf6ae9c9c75601b76b5bfbe07181", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_define_integration_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_define_integration_strategy_agent.py` is
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
