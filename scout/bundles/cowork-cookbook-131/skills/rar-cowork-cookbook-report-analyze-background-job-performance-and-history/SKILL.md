---
name: "rar-cowork-cookbook-report-analyze-background-job-performance-and-history"
description: "Builds a structured summary report of analyze background job performance and history activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_background_job_performance_and_history", "rar_sha256": "0159cef7b97cd94608080ff593dd7453bd36e4f6d35aa3b18daf22a32fa1aab4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_background_job_performance_and_history_agent.py` and embedded as the fenced Python below (sha256 0159cef7b97cd946…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_background_job_performance_and_history_agent.py` first:

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
    "version": '2.0.1',
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
