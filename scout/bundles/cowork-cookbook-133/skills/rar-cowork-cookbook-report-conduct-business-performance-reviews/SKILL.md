---
name: "rar-cowork-cookbook-report-conduct-business-performance-reviews"
description: "Builds a structured summary report of conduct business performance reviews activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_business_performance_reviews", "rar_sha256": "7999e61567a841231ef7c82db33ce5f24b2e4894b9cb45be11ffccbb5fd09b16", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_conduct_business_performance_reviews_agent.py` and embedded as the fenced Python below (sha256 7999e61567a84123…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_conduct_business_performance_reviews_agent.py` first:

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
    "version": '2.0.1',
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
