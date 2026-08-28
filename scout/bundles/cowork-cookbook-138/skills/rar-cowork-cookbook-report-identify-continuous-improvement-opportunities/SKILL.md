---
name: "rar-cowork-cookbook-report-identify-continuous-improvement-opportunities"
description: "Builds a structured summary report of identify continuous improvement opportunities activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_continuous_improvement_opportunities", "rar_sha256": "233b99594ae8173d97dc1c2d897e2cfab19e3f763a95710ad41d4409ea2a4137", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_identify_continuous_improvement_opportunities`. The original RAPP
agent is preserved byte-for-byte in `report_identify_continuous_improvement_opportunities_agent.py` and in the RCI capsule.

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
