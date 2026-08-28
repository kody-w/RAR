---
name: "rar-cowork-cookbook-report-conduct-business-performance-reviews"
description: "Builds a structured summary report of conduct business performance reviews activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_business_performance_reviews", "rar_sha256": "d4ee5e4cb2fcf0ad0afd4da2199dae4d4c0a26f3312ab02738c00eb47e5be7d2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_conduct_business_performance_reviews`. The original RAPP
agent is preserved byte-for-byte in `report_conduct_business_performance_reviews_agent.py` and in the RCI capsule.

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

Conduct business performance reviews Summary Report — Builds a structured summary report of conduct business performance reviews activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-business-performance-reviews
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_business_performance_reviews_agent.py` and embedded as the fenced Python below (sha256 d4ee5e4cb2fcf0ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_business_performance_reviews_agent.py` first:

```bash
python3 report_conduct_business_performance_reviews_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_conduct_business_performance_reviews_agent.py   # or on stdin
python3 report_conduct_business_performance_reviews_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Conduct business performance reviews Summary Report — Builds a structured summary report of conduct business performance reviews activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-conduct-business-performance-reviews
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_conduct_business_performance_reviews',
    "version": '2.0.0',
    "display_name": 'Conduct business performance reviews Summary Report',
    "description": 'Builds a structured summary report of conduct business performance reviews activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-conduct-business-performance-reviews',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-conduct-business-performance-reviews',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7e68807a572277c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/analyze-business-performance/conduct-business-performance-reviews'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/report-conduct-business-performance-reviews', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportConductBusinessPerformanceReviews(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportConductBusinessPerformanceReviews'
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
    print(ReportConductBusinessPerformanceReviews().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
