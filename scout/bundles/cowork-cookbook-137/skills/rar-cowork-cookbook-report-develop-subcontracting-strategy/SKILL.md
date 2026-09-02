---
name: "rar-cowork-cookbook-report-develop-subcontracting-strategy"
description: "Builds a structured summary report of develop subcontracting strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_subcontracting_strategy", "rar_sha256": "756f277aaccab34abf1bcd4e426c642f0c58e4a806515f0fcbdbaaa7d1053ae8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_develop_subcontracting_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-develop-subcontracting-strategy:d7c8a326800abae039d7aec655e3d7f11a16536ab109b5ba13e3cfe10884f8f4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_develop_subcontracting_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_develop_subcontracting_strategy_agent.py` is
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
