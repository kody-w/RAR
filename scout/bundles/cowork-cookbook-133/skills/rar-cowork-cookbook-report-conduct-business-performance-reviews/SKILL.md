---
name: "rar-cowork-cookbook-report-conduct-business-performance-reviews"
description: "Builds a structured summary report of conduct business performance reviews activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_conduct_business_performance_reviews", "rar_sha256": "d4ee5e4cb2fcf0ad0afd4da2199dae4d4c0a26f3312ab02738c00eb47e5be7d2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_conduct_business_performance_reviews_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-conduct-business-performance-reviews:6fe1694bd8658de094dfe1ee06bfd412f86402c691f2f5f584b0007294ca1aa7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_conduct_business_performance_reviews`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_conduct_business_performance_reviews_agent.py` is
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
