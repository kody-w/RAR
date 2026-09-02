---
name: "rar-cowork-cookbook-report-plan-procurement"
description: "Builds a structured summary report of plan procurement activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_procurement", "rar_sha256": "1d9f587ad4a0247c21fbd2aa2bfdf5477888c43da7e8f2bc7c6f11b071e2faf7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_plan_procurement_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-plan-procurement:1d9ae034719b1ec474c094ca8d013167532bc1e3f07707fbca8d1994714b5f32", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_plan_procurement`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_plan_procurement_agent.py` is
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

Plan procurement Summary Report — Builds a structured summary report of plan procurement activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-procurement
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_procurement_agent.py` and embedded as the fenced Python below (sha256 1d9f587ad4a0247c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_procurement_agent.py` first:

```bash
python3 report_plan_procurement_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_plan_procurement_agent.py   # or on stdin
python3 report_plan_procurement_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan procurement Summary Report — Builds a structured summary report of plan procurement activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-procurement
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_plan_procurement',
    "version": '2.0.0',
    "display_name": 'Plan procurement Summary Report',
    "description": 'Builds a structured summary report of plan procurement activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-plan-procurement',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-plan-procurement',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fe4520afca1d57ed',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/execute-sales-and-operations/plan-procurement'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-plan-procurement', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportPlanProcurement(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPlanProcurement'
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
    print(ReportPlanProcurement().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
