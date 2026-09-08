---
name: "rar-cowork-cookbook-report-manage-cases-and-requests"
description: "Builds a read-only summary report of manage cases and requests from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_cases_and_requests", "rar_sha256": "2a9056fb61306a4fbb227dfcdf0d6bfac306273c219cfa9add8193261c662d6b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
