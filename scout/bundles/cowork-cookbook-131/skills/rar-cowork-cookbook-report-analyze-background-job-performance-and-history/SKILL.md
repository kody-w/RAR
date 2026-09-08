---
name: "rar-cowork-cookbook-report-analyze-background-job-performance-and-history"
description: "Builds a read-only Excel summary report of background job performance and history from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_background_job_performance_and_history", "rar_sha256": "bb6fc7ccf1df635ba0311e951fe7dc9a80313ea0a065c8e5f039415c804eaf23", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

Analyze background job performance and history Summary Report — Builds a read-only Excel summary report of background job performance and history from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to query, e.g. USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "output_filename": {
      "description": "Name of the Excel workbook to produce, e.g. report-analyze-background-job-performance-and-history-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_analyze_background_job_performance_and_history_agent.py` and embedded as the fenced Python below (sha256 bb6fc7ccf1df635b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_analyze_background_job_performance_and_history_agent.py` first:

```bash
python3 report_analyze_background_job_performance_and_history_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_analyze_background_job_performance_and_history_agent.py   # or on stdin
python3 report_analyze_background_job_performance_and_history_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze background job performance and history Summary Report — Builds a read-only Excel summary report of background job performance and history from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

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
    "version": '3.0.3',
    "display_name": 'Analyze background job performance and history Summary Report',
    "description": 'Builds a read-only Excel summary report of background job performance and history from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.',
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
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa05086f636e58f6',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-analyze-background-job-performance-and-history-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where analyze background job performance and history stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of analyze background job performance and history for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-analyze-background-job-performance-and-history-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads analyze background job performance and history records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only Excel summary report of background job performance and history from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a background job performance and history summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-analyze-background-job-performance-and-history-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a background job performance/history summary report from D365 F&SCM with totals, dimension breakdowns, and a top-10-by-value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportAnalyzeBackgroundJobPerformanceAndHistory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportAnalyzeBackgroundJobPerformanceAndHistory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-analyze-background-job-performance-and-history-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
