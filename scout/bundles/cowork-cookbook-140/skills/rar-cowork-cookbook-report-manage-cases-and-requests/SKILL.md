---
name: "rar-cowork-cookbook-report-manage-cases-and-requests"
description: "Builds a read-only summary report of manage cases and requests from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_cases_and_requests", "rar_sha256": "2a9056fb61306a4fbb227dfcdf0d6bfac306273c219cfa9add8193261c662d6b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_cases_and_requests`. The original RAPP
agent is preserved byte-for-byte in `report_manage_cases_and_requests_agent.py` and in the RCI capsule.

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

Manage cases and requests Summary Report — Builds a read-only summary report of manage cases and requests from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-cases-and-requests
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
      "description": "Dimensions to break down by where applicable: department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-cases-and-requests-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_cases_and_requests_agent.py` and embedded as the fenced Python below (sha256 2a9056fb61306a4f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_cases_and_requests_agent.py` first:

```bash
python3 report_manage_cases_and_requests_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_cases_and_requests_agent.py   # or on stdin
python3 report_manage_cases_and_requests_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage cases and requests Summary Report — Builds a read-only summary report of manage cases and requests from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-cases-and-requests
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_cases_and_requests',
    "version": '3.0.3',
    "display_name": 'Manage cases and requests Summary Report',
    "description": 'Builds a read-only summary report of manage cases and requests from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-cases-and-requests',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-cases-and-requests',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '16493cb43fd050ff',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-workplace-compliance/manage-cases-and-requests'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/report-manage-cases-and-requests', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-cases-and-requests-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage cases and requests stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage cases and requests for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-cases-and-requests-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage cases and requests records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of manage cases and requests from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a manage cases and requests summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-cases-and-requests-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write case/request activity summary from D365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageCasesAndRequests(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageCasesAndRequests'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-cases-and-requests-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageCasesAndRequests().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
