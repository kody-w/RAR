---
name: "rar-cowork-cookbook-report-identify-background-jobs"
description: "Builds a read-only summary report of background job activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_background_jobs", "rar_sha256": "6c10a2d3bb12907656d132ce00afb4fb29b6f730ccc52a977cb6932dcd6e5198", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_identify_background_jobs`. The original RAPP
agent is preserved byte-for-byte in `report_identify_background_jobs_agent.py` and in the RCI capsule.

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

Identify background jobs Summary Report — Builds a read-only summary report of background job activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-background-jobs
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
    "breakdown_dimensions": {
      "description": "Dimensions for breakdowns where applicable: department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-identify-background-jobs-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to summarize; defaults to the most recent posted period available.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_identify_background_jobs_agent.py` and embedded as the fenced Python below (sha256 6c10a2d3bb129076…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_identify_background_jobs_agent.py` first:

```bash
python3 report_identify_background_jobs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_identify_background_jobs_agent.py   # or on stdin
python3 report_identify_background_jobs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify background jobs Summary Report — Builds a read-only summary report of background job activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-identify-background-jobs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_identify_background_jobs',
    "version": '3.0.3',
    "display_name": 'Identify background jobs Summary Report',
    "description": 'Builds a read-only summary report of background job activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-identify-background-jobs',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-identify-background-jobs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b26830a1326e30fe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-background-jobs/identify-background-jobs'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-identify-background-jobs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-identify-background-jobs-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where identify background jobs stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of identify background jobs for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-identify-background-jobs-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads identify background jobs records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of background job activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a background jobs summary report for USMF's latest posted period as an Excel workbook with Summary, Detail, and Top10.", 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-identify-background-jobs-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write Excel summary of D365 ERP background jobs with totals, dimension breakdowns, and a Top 10 by value section.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportIdentifyBackgroundJobs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportIdentifyBackgroundJobs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-identify-background-jobs-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportIdentifyBackgroundJobs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
