---
name: "rar-cowork-cookbook-report-define-environment-strategy"
description: "Builds a structured summary report of define environment strategy activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_environment_strategy", "rar_sha256": "7431b271b1d4fdf23e42c6d9a3c5575991a78b9b1c9582eb41685a710317653e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_define_environment_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-define-environment-strategy:1e2d5ca0a7f5fbba43674c813ed5fc5abf8998609d224f1f1bc84d92e6f3533a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_define_environment_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_define_environment_strategy_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_environment_strategy_agent.py` and embedded as the fenced Python below (sha256 7431b271b1d4fdf2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_environment_strategy_agent.py` first:

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
    "version": '2.0.0',
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
