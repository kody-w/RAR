---
name: "rar-cowork-cookbook-report-identify-continuous-improvement-opportunities"
description: "Builds a structured summary report of identify continuous improvement opportunities activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_continuous_improvement_opportunities", "rar_sha256": "688386b1ebed64e25d821125df32b5e3ea8e993f6cad87a955a47db68e344780", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_identify_continuous_improvement_opportunities_agent.py` and embedded as the fenced Python below (sha256 688386b1ebed64e2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_identify_continuous_improvement_opportunities_agent.py` first:

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
    "version": '2.0.1',
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
