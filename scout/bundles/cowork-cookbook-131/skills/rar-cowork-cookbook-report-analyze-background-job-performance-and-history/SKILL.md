---
name: "rar-cowork-cookbook-report-analyze-background-job-performance-and-history"
description: "Builds a structured summary report of analyze background job performance and history activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_background_job_performance_and_history", "rar_sha256": "b22da71b53dcd844cf3661835f6f9e74c97b9444ed3150f1098e9780e24926ee", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "report_analyze_background_job_performance_and_history_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/report-analyze-background-job-performance-and-history:10463f7270e93c2ef655f164f3a4a0f967834ce53df4c0b301845bc6080ab2c2", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/report_analyze_background_job_performance_and_history`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `report_analyze_background_job_performance_and_history_agent.py` is
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

Analyze background job performance and history Summary Report — Builds a structured summary report of analyze background job performance and history activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-background-job-performance-and-history
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_background_job_performance_and_history_agent.py` and embedded as the fenced Python below (sha256 b22da71b53dcd844…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_background_job_performance_and_history_agent.py` first:

```bash
python3 report_analyze_background_job_performance_and_history_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_analyze_background_job_performance_and_history_agent.py   # or on stdin
python3 report_analyze_background_job_performance_and_history_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze background job performance and history Summary Report — Builds a structured summary report of analyze background job performance and history activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a analyze capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-analyze-background-job-performance-and-history
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_analyze_background_job_performance_and_history',
    "version": '2.0.0',
    "display_name": 'Analyze background job performance and history Summary Report',
    "description": 'Builds a structured summary report of analyze background job performance and history activity with totals, trends, and breakdowns.',
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
        "upstream_slug": 'report-analyze-background-job-performance-and-history',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-analyze-background-job-performance-and-history',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '509e8d75e34bb3ff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/analyze-background-job-performance-and-history'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-analyze-background-job-performance-and-history', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ReportAnalyzeBackgroundJobPerformanceAndHistory(BasicAgent):
    """Analyze agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAnalyzeBackgroundJobPerformanceAndHistory'
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
    print(ReportAnalyzeBackgroundJobPerformanceAndHistory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
