---
name: "rar-cowork-cookbook-report-plan-workforce-development"
description: "Builds a structured summary report of plan workforce development activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_workforce_development", "rar_sha256": "b11ab4d604973877d39d0dc17f83e61df32fe8a2011d145d6d35d09686c4db4e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_plan_workforce_development_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-plan-workforce-development:889e83e81fff31d0e52b8d57b1d904e9ddb35f56f8f337e1e2c26bd64099b071", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_plan_workforce_development`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_plan_workforce_development_agent.py` is
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

Plan workforce development Summary Report — Builds a structured summary report of plan workforce development activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-workforce-development
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_workforce_development_agent.py` and embedded as the fenced Python below (sha256 b11ab4d604973877…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_workforce_development_agent.py` first:

```bash
python3 report_plan_workforce_development_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_plan_workforce_development_agent.py   # or on stdin
python3 report_plan_workforce_development_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan workforce development Summary Report — Builds a structured summary report of plan workforce development activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-workforce-development
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_plan_workforce_development',
    "version": '2.0.0',
    "display_name": 'Plan workforce development Summary Report',
    "description": 'Builds a structured summary report of plan workforce development activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-plan-workforce-development',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-plan-workforce-development',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a5b14bcbf13cac5c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/conduct-financial-planning/plan-workforce-development'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-plan-workforce-development', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportPlanWorkforceDevelopment(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPlanWorkforceDevelopment'
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
    print(ReportPlanWorkforceDevelopment().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
