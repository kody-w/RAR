---
name: "rar-cowork-cookbook-report-identify-continuous-improvement-opportunities"
description: "Builds a structured summary report of identify continuous improvement opportunities activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_continuous_improvement_opportunities", "rar_sha256": "233b99594ae8173d97dc1c2d897e2cfab19e3f763a95710ad41d4409ea2a4137", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_identify_continuous_improvement_opportunities_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-identify-continuous-improvement-opportunities:5384b409db4c4dfb6d68c65737a4f4e3fe53f9d0c03e392cf67ab060ed8971be", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_identify_continuous_improvement_opportunities`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_identify_continuous_improvement_opportunities_agent.py` is
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

Identify continuous improvement opportunities Summary Report — Builds a structured summary report of identify continuous improvement opportunities activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-continuous-improvement-opportunities
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_identify_continuous_improvement_opportunities_agent.py` and embedded as the fenced Python below (sha256 233b99594ae8173d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_identify_continuous_improvement_opportunities_agent.py` first:

```bash
python3 report_identify_continuous_improvement_opportunities_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_identify_continuous_improvement_opportunities_agent.py   # or on stdin
python3 report_identify_continuous_improvement_opportunities_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify continuous improvement opportunities Summary Report — Builds a structured summary report of identify continuous improvement opportunities activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-continuous-improvement-opportunities
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_identify_continuous_improvement_opportunities',
    "version": '2.0.0',
    "display_name": 'Identify continuous improvement opportunities Summary Report',
    "description": 'Builds a structured summary report of identify continuous improvement opportunities activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-identify-continuous-improvement-opportunities',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-identify-continuous-improvement-opportunities',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b41fbf421ca7d354',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/analyze-production-operations/identify-continuous-improvement-opportunities'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/report-identify-continuous-improvement-opportunities', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportIdentifyContinuousImprovementOpportunities(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportIdentifyContinuousImprovementOpportunities'
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
    print(ReportIdentifyContinuousImprovementOpportunities().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
