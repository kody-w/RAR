---
name: "rar-cowork-cookbook-report-identify-background-jobs"
description: "Builds a read-only summary report of background job activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_identify_background_jobs", "rar_sha256": "6c10a2d3bb12907656d132ce00afb4fb29b6f730ccc52a977cb6932dcd6e5198", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
