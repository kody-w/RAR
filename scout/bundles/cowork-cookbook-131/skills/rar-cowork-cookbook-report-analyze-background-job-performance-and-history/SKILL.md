---
name: "rar-cowork-cookbook-report-analyze-background-job-performance-and-history"
description: "Builds a read-only Excel summary report of background job performance and history from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_analyze_background_job_performance_and_history", "rar_sha256": "bb6fc7ccf1df635ba0311e951fe7dc9a80313ea0a065c8e5f039415c804eaf23", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
