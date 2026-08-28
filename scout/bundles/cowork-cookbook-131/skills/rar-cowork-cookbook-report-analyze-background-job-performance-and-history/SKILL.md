---
name: "rar-cowork-cookbook-report-analyze-background-job-performance-and-history"
description: "Builds a structured summary report of analyze background job performance and history activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_background_job_performance_and_history", "rar_sha256": "b22da71b53dcd844cf3661835f6f9e74c97b9444ed3150f1098e9780e24926ee", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_analyze_background_job_performance_and_history`. The original RAPP
agent is preserved byte-for-byte in `report_analyze_background_job_performance_and_history_agent.py` and in the RCI capsule.

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
