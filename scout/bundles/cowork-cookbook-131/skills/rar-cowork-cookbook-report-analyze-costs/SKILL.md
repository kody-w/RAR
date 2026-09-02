---
name: "rar-cowork-cookbook-report-analyze-costs"
description: "Builds a structured summary report of analyze costs activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_costs", "rar_sha256": "09304482f1e5cf85dd5bbed81627e2dd87b1e29be345235d6fc64d058f3673a9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_analyze_costs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-analyze-costs:e2b2fd336201f6be3517da6a07420cd2786b902f86b7b18c011536ace222668d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_analyze_costs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_analyze_costs_agent.py` is
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

Analyze costs Summary Report — Builds a structured summary report of analyze costs activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-costs
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
    "data_source": {
      "description": "Optional. Where the evidence comes from.",
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
      "description": "The question to answer, stated as a question.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_costs_agent.py` and embedded as the fenced Python below (sha256 09304482f1e5cf85…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_costs_agent.py` first:

```bash
python3 report_analyze_costs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_analyze_costs_agent.py   # or on stdin
python3 report_analyze_costs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze costs Summary Report — Builds a structured summary report of analyze costs activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-costs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_analyze_costs',
    "version": '2.0.0',
    "display_name": 'Analyze costs Summary Report',
    "description": 'Builds a structured summary report of analyze costs activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'report-analyze-costs',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-analyze-costs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '048771d92f5e8cb5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/analyze-financial-performance/analyze-costs'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/report-analyze-costs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'analyze', 'checks': ['The question is falsifiable and answered directly.', 'The decision threshold was stated before the result.', 'Missing evidence is named rather than silently excluded.', 'Uncertainty is quantified.'], 'confidence': 0.429, 'deliverable': 'A decision-grade answer: one-sentence verdict, method, evidence, uncertainty, and what would change the conclusion.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'data_source': 'Optional. Where the evidence comes from.', 'subject': 'The question to answer, stated as a question.'}, 'refined_by': 'rules', 'signals': ['tag:analysis', 'word:analyze'], 'steps': ["Restate the question so it is falsifiable. 'Is X better?' becomes 'Does X reduce Y by more than Z?'", 'Declare in advance what result would change the decision — this is what separates analysis from justification.', 'Identify the evidence available and, explicitly, the evidence that is missing.', 'Compute the comparison, holding the method constant across every option.', 'Quantify uncertainty. A point estimate with no interval invites false confidence.', 'Answer the original question in one sentence, then show the working beneath it.'], 'subject_label': 'question under analysis', 'verb': 'Analyze'}


class ReportAnalyzeCosts(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAnalyzeCosts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'data_source': {'description': 'Optional. Where the evidence comes from.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The question to answer, stated as a question.', 'type': 'string'}},
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
    print(ReportAnalyzeCosts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
