---
name: "rar-cowork-cookbook-report-record-service-timesheet"
description: "Builds a read-only summary report of record service timesheet activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_record_service_timesheet", "rar_sha256": "e3983f3bbe7f3fda15aa31d47e3d6e8b8b88fa52cc21124ac21520f86faea16e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_record_service_timesheet`. The original RAPP
agent is preserved byte-for-byte in `report_record_service_timesheet_agent.py` and in the RCI capsule.

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

Record service timesheet Summary Report — Builds a read-only summary report of record service timesheet activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-record-service-timesheet
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
      "description": "Name of the Excel workbook to produce, e.g. report-record-service-timesheet-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_record_service_timesheet_agent.py` and embedded as the fenced Python below (sha256 e3983f3bbe7f3fda…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_record_service_timesheet_agent.py` first:

```bash
python3 report_record_service_timesheet_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_record_service_timesheet_agent.py   # or on stdin
python3 report_record_service_timesheet_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Record service timesheet Summary Report — Builds a read-only summary report of record service timesheet activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-record-service-timesheet
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_record_service_timesheet',
    "version": '3.0.3',
    "display_name": 'Record service timesheet Summary Report',
    "description": 'Builds a read-only summary report of record service timesheet activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-record-service-timesheet',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-record-service-timesheet',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e851e33689a35412',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/deliver-services/record-service-timesheet'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/report-record-service-timesheet', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-record-service-timesheet-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where record service timesheet stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of record service timesheet for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-record-service-timesheet-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads record service timesheet records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of record service timesheet activity from Dynamics 365 F&SCM for a given legal entity and posted period, delivering an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a record service timesheet summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-record-service-timesheet-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write timesheet summary from D365 ERP with totals, by-dimension breakdowns, and a Top 10 by value list exported to Excel.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportRecordServiceTimesheet(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportRecordServiceTimesheet'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions to break down by where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-record-service-timesheet-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportRecordServiceTimesheet().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adOiWLbuX/G+J+JW1THzZUbJjo64IIqiIDKJVHZkMc8zyFCn/vvdqJlV1Z19+nTE/XTNAYG9117j86wt/PpmdW1Y1G+f3hTPyheclaZR6NULK3cXm6Iv6gQcisQG/xZOkbd1ZHdtUTdvH95cr3HqqGyjIgfTmS5K3WZhLWrPcj8WeToumi7LrHoEV8qibheFD745Re0uGq++R463aKPMa0LPaxeW00b3qB0Xfl1kC3bMrSxymgVGEovd/1Y2wsIvgE6LILp7+SL1AitdeHk7T5gVLYum9cDBq6PC/bBwvRSMq6M8AHcX28Hx0sVsycOIPmrDhfLU7MOC9VorSj88pKhFicCLhz7NO7DPG6ysTL3m7dPPf/vwFoHvb59+fXNSqwGX3uSHUfLDIOVpj/rVHDA5tfIAjCpH4N0cnAPdgAkZuOR6/uJ19mPjpf6HxX/+Z9JbddD89Olzvnh9Pr/Nf+QuX7QhcFRhPSx0rNKyoxTY/b6g094aG+DStqvz2fFNO5v8/pz5u6SiXPx1vvfjc5H3wGt//PxWABWsOXSf335aAN9+fqu7+fv7LKX88af3tOi9+seffpfTdHbsOe0sDGj9/uV1/hILBv4+NPIXXxRpu3mtBaIelR4Q/gf75s9T9Ze4l0u+PAf/WJQfFt+XPNvzV6DvM/1sIPf7YoEPwMy397iI8h9fa9QFyB8rd7wff/pnYp3Qc5I0atr/kdyfn4JDkPPAWy+X/PThEb6/LZYv277J/OfLliBh/h1LwPCvy31z1D+T/Yjs34lOo9xrvsXyu+K+N2H518XP/9S2/27Ch4X/+Y19FqZlp96nxa+PFPn5B/f3iz/87Tcg+l+KUYqudh4SvmRWHvle03758vMPzePyD3/7+YeuBFnsWdmXrk6/J/N7fn2s8ycPvkb9+Oe5YH0tT/Kizxffamjxa1H+r/q394VupZH7+/Xm0+KPlTh/lovZiK+LPl3wh2psgK5/8ONPb78B5MmBNZ3zuA3w4z/+YyFETl00hd8uFKfo2gUI8Ayls/JqGDUL8HdGjdoDfm0i4NjXOJD/c4RnjQEY//J/nAfAf3ReAA89gfrLE6W/vFD6yzeU/uV9oQKxRR0FUQ4QWKYl6XNuBQCJ5yXL2punAJiyx9b7CKr54/xlEeWLX/6F5C8PIe/l+MsDiaMn6smbw4x4TZd677Nt1xCA/9MSBwC7N3hOB+SnhQOU8SMA1R+AzU2R3gFizn5okihNF24ElgWc9eQK4KtPs7BffvnFtprwc/6EaGzxJLMGAgO+qbP4+BFY5adRELafc88Ji8UPv/72w+K/Fv/drIfweQ0JUMUrEkBDXjmLC1BZXQaGgSCBsALYeETi199evgVicsC+M3v5kfecDDIz8dyvjlb29EeUIBe2BxwMnJvNjp2pLmrfFwd/8U3fF+3OzBACfgSsWHq56+XOCKRawJxvnsyLdtGA9Gt8wIhd4z1W/cWurYeKGShxq/1lIWwkwENFCv6b1XwMApOLPALu/5YGz+tASP1Ds2C+inhfiHMuLkqrtsqwtl5r+NYzLjO3v6YD4dYi9/rP+Uy43uyqR2E83QMGAc84r5B+nGMOuhLA5bnbfF37Mcaa2VJ9sGb9OW9eSW/V3qMFAaqMi6CL3JkK/vJKqSYsutR9+A9oOkt6RcF9ReWRg/I/62BeLcXi2RcsPncojOCL/8+6otkDNMfJW45Wt+xiK6ry7RmZuTecI/hsJx86F/WzCn9vWr4C01d8/pynEUizevzLc+Qjnq8xT8zramCBTMsP+SCZQGRmuY9cn3O3rucqsT7nX4kAKL14oB4INwAGUDhzvn5dcL77VdMQVP98/ntT8DUQwGyQz4uys1OQa77nubblJECrOYhfIwsS35uD14eRE/7JqjkGIL5A/gIoEYEKBGTx/g2cn3e/qv6nic/eZ57y6As7UK71QwDQw5sVnAMyhwqo1z5bcWDnp4cQYEZWtrPtNigYYOnzold7VRc1UTuD49OvXglw+eN8fFo6X/WGEtQIcBaohLID3n3UzpwrGehsgA4gfUApZVEOmB445eWEh0Arm4EAAO2rFX1KfFx+GeQ9Cm7O668TZ0PmOTPrP7Pbysc/4oX6vTQB8rJ5xGPdv8+0b6vNsmfMbADugRW/3n22B+9Phn+2EIuvcj/9w17nx39vO/TgbO3PCfBpEbZt2XyCoCfPfqXZd4BY0FPX5kW5H5+Z9/EFAR+/QcCfxD4t/rT491T7k4hXaXxaIO/wOzzfOr1S6/UBnth8ZG4f8fnuDHe/wylYvshAbs1xGwHHf+O+r0MAAQY1QCEw+MmFzUyhPWDtB/iDIHzO/5jrc60BbsmDOTeb4g8Y8GgCQN4/Y/aNo8CtvAVruzOQBd68SXtURuO9fcq7NP3wBhDS+9ebs5mGsjmfm3lHByoHYGQbeY8zG2iXuKBiv7hgRt48u65f/263y367N8PLY85injS7BRgMeMYqS6Dbs9UF1GvV7cxlH4AtrRcUM8qCVqUEAh79GZgKCAao1o7lbMBzLzd3fw+4Gtp/VOH8+GKl7y+4bv5YAy8ym8n8D6X69DnwtQMsBowAVGlm8gU+n50xl7nVgLoBJfNdXR4U8+VJMd/xycxLf2Ih4Jqq82ZbvffgfaEpwu67cr+1v/8o9Ap6j1mOW3yaafjDC+fAEWxZgDe/7j5mfnvuBx9b97wDW+2f553PHO7HlPkLmAMO3yZ9+xHD9t7+9j29HmD4ZU7JZ2L9vXbiDHKABGbn/h2jAp3Bum7neC/r/0Wlf0RhlPwIEx9R/H1Im+G7jnpy+T/qIf2R6h8N2qu5yP8C/OJbXdo+EnXWM5ubQaDFzIF/ahEW1h2k0Zyx31kbLP5gEsDHs2N/j9jvfise28eHmqnVPn/t+PUN1JkFEs16Vdpr/wGGA+D92MydFwSwCCwIzp+oAe79uzuT1/QmtEBrDOZ7GLXGfMy2vZWP+a6FEJaFIS6+8jCX9NY2+LP2LQJ1HBRBUNwCBwKF/TXpW56FkB6Q94SeL3N3Gc0qEdTKhykK9XEEhV3gVBR33TW5Jh1ihcIWZVuETVCW/fvUJMrdl51Pu2Ynftskzf54mQtAh8TByD3eHOjnZwNRiA2hK1vhT0sDhuSh189wRWzP6zSxkyWx31hDrrA0n0m3PIWF+4HfJApaDoPK30wRZQSJlprLEldXvJ8armpuNVPtzJGaOobeJomL6YhvxNUAuVQ83t3RZsXDcpveM2RTaQWyq6vUVHbnDWSQI+tH7NksjSSE7hx2x+9GeSvi0+UojyNtlXC23rrVeWzQwj3s7l4fcDeL63R7K0fT4EZLUdxWg14J18kmlicRogj/Lnsn8eC0vF9doxuArybYxYfS2h4v8oY/ucp+OBhnXY4EeZTj2Cm1Zq1bjk+X6YlbKRBXeWXqR3Ko1QNEHfZCE2kSd6j0MUFNke39obhT7ory7RZ1clsfnHxYnpJ+bZjxisSv20Quk4xJNf2yqxrYxFfM1d4p10Jmds2gqwLUV2s2EFphN5z23XCtvNsKNsyO2QzuQexv9HgSCmfFL6lzJo2BViZTJuv4rcWYS5x35vFiX9cuzxWhe+E4xrAK/VKW5Xmrm6FbtvJIucbY0TUaYUjmXXKZoavU5q/sSVL7O7HaHgftdLQYcqsvNzwlOJbq8tuk5Ts9Kh3RN9mmcL2L3tG0bgT4aDHjhijcpQXSPBlYpatV8bDlFIorkj7KfBFuNhte1A/s0QqM3fbaEdmVYTXyxtxD3+z11gtXtL210cKZ0ok0lKpkSPMMegdotxZIU8KiA5Xy65Ezj7uSu8qpzFayXBdBN8R7DWwI4DFLpNTiL5V0oXBq29+v8D64DEvaOSclXGNl1Y4nBj7YbbZxZGi6LLOtxNpCyTQhd3fIQGOPqLixry1dq1fxsDFssdVb+SjHqT6WjlYN17qrtdVJ4pXLXWZzaKfhVSgOKX/S8VFAyniNp9Bm3y4ZqVYYvGgD75LZbJBQk3RRxT1RWDke6tpVJp2cvqwb9TLdJdbdIwEnavuhxfZDM3FI6+9TCzIqs3bVRs0F3cpvJyQ4lCs8hPAQu098Vp4oZkycWIegs4RzJ3yXK33ub5pAa/YKGUaZ3MVmxNaXo0No+rKhxexinMwLmfRXZj34JJKjWMDuI1HWcvxul2ECd7tqZMwkMqr2bJctA49OJVTo1lPKg3HxeE27skVU78pNKOOXdvLss7z0J0c+OW4Xq0ZAGsKOux/yfh2xJ2DLmTbsJnaGVX80tihEYHKExOUAMJ/IQxs1EcFqYdj2p1pW+IGVDmszXe2jzB2cXUZ0ASREjAaTmlxFBsX1jWyXPhdxGZujPmfnuHxi9cyATH1ban0lIEI57VgDWyfLu6gcBqKQLsImvEeJ2d8EUm87QsHI9LpSMxd2JF3jcbMSdsJ0g/TVpouwYdyWAxPlZ5NfISVh5dvz2bBsMjRcI9PZCTLom0ZyDJ/kzhlClsbGJHH6Np069zJl+qQSlaUr14vS8Mvthl7BmNSdT1IZ7LNA52J/WokAz1yhMu95VPRI0cAx0+OV5GxQ/FoSTOjoXXrY7u5Xxgg90bxl9wsehvJmzRK7YNn3eSCc+u5+YWpSjNXcPG01nOSd06X2z5G0EswAm7K0KYTDUTpBB2XKrXssxeZYjEFW4NaewnLpjKRdCsebacpo26PXOaJo+FIYUEMhaozeEtiUI/iouVygrSpRDqPzcS3hocxw6wSXzxSuTqp2yY3ycOX3fNWtVvZdvnAnkyFHL1PY+ae/29Bysiehcb/ho2LnMnZGryP6kBxuvdRehtQ680uu3sl3g8Jws3WmyqSFhCVNQVWQyZI5W59269IQRbHklVYf6/NU0/DUb+OjGUVJ4neH+0kpme3FQjHd7/mjeuTNjLltxuFMGMfLNT20AKQ7cdXTl5yrItJAJGRbdYaDWAPT9O3JKdw9qws4R3slJLBKBuJ6VzvyrLLLW8oevV71JD7VDym3NYZjginUhdyzzPEcgPg6nrTOWWtcVVTKbOH8UJwvfj4t5YkgqOXah9gSp6ClzWtoa7glb+DqSYJ2Ss9c9gdAV6O3Zye+iBCeHfQI147jEOBnMdlhQ1hV3TAxFZ7hgTjap8FMe4MjmXQworPR64LOWh3tBWOwD8VLNoY0feWuJcIkec8fiKtRosKVtq5wwJgFhferpsREbd2uqThu09Dk9UkfNXILVYkTLU/szez0W3vd6cscQHSUEsha2gb2YSOElQqntzJGG6SVcHmE86sf4FNxGcIJiy571xYhfm2f0IlIt1YiH68X6jIovBmZokBP/gm6rhI72oeb49IvcL+It7vUxoeA2MRkMJyvvGIBGGGKnL0u46bbERt6p4UtUlc1s2k25WF1kJ0LaA7baC+ctvEBgozjoS9UPgnZ+jw4DLHRmI1QFpdNlhCCu71AKHW93DinMli60eVkNW4Sm2APntSDNqvF+eUxUIWjXl4cVh24QAi1uFDh+5hEKd6wqUT7kUQrW1rnBfqanLCyBfUroL2CDgHAMnhrEJR9o/OmCwpOHtSOPZG1uSrj/s5IFLnayiwB5LPOUr+zUe5VVGGdiuK828F3prge3Y4gIZ08sHXYWWYkrNLlSRFkq8FM8tqS1KHyqI0ibIh94MuV3vjjZZdRCn5u+bw6325ayW3dhk/6cnmok0szJJWqqDiNCHttffEj1dhsh1xz2O4KtdtLDlsBV20kzHS7Q2DhNRVpgowbXG1Rkbm/Icmm8GpypVSSuDxbNKP2U4+dJ1tfrrfx7SZv2PzY4vsRaqobjaA0qR8vXIr6eTm658zE3RXMmGrDsa5+MQRxAA2dO4QFaOhE+wyfElgOpuhy0Ephs7zLsgyXmeUgoMHYWkGsH9dZdiTRcz/6DUUU/LHek5cDtJscTmNFkKcNvGWzo4fcWEDkMbpJGPYackGHTyLO8bwa7fJE2EcRMspgg67cLH508kvFcmJAnq/IFl+tsbVM7Y5xLCdoObWhrriXzeUUbrSOrzgigOCtWLEDOiCqmt3De5OtpLUfU+fe4M8hijCr2+koBjgEU/d2u++8gFDFdR9pRpTyaBJAo1CUE0oapCH562XZywjnK6lyTfjNZTl5h4PCMxoAfcbSp9HZwmQ63kZmn/ViukvY8LyMQEs40l1/P5kJwA79hFbDWgmZfh0SGrdPaq7DN1ekC0p0Y273TYwrpzgS8LAh6MtuZ2x2Yjp1k20fDtelSdTEhkVt+1qSBOyDXjCtws32bhWD6RzibUNfhIRGlHXGBuIlVOroXhbEtTiuYet2NPD8dBvi3NvtUreAbQ6LwyQ+ABxYrXDcnyhuFOPdnQSlphYXQoC2TMwQt0jWO004hgykH2wFzpMgPyz9fbyi3HzCfWmCOYhSaxYC2WpyJaGfSVhbbQ23DbrLDr9GtHzokFs6eLvxYvRdyzXKcmPBkYacRRXa385qXGCp3Q15YrdTY8q6uzIuwJ9TC23W2aYUiiAgeONI78ZTcKoGnL7LUd0uEbj2siNeoo7t2YG58UNeVvvA3pjX4dSXMMYzW3PXByO8YaJE4T0YC9Srr4k5N+1uwmZcNzrLnuMKovYhpoQpEuEitBkzyq72lE3v1qeKhmkS0w4bsu59cauxh1a/1ertft0fp7ZLXILGY7SHD1LlloSiQptzk1jGAZFHVLoEQ6EqYZVfivOqCC2ZVuW1g4J2fOlDjAdTEc7j0zE67JbBjWagDON2hnXaCCPMBceiFUC1O+toW0/3S0uL1YWSyE2iQocG2yawsJE6QUY3y7yvyb64Vljq2pBKs4W0sgm+IFQlA06o7ruwvTf8xupup+xqlhIplWc+WimZnDjFZUXgeb+75GXRgS4tGYJ16fDn69m3KsUiGoL0NF7VnJg57eOltb/j+DJrenxLZ31B08qa7KfRDWl4ZS3TuOY1Qwp55DIyrcBgRNAchszkuFGgA8MQjQ2HHVsfkVknzyzbdUAjYK7DOz4oVNQ3rDjdbFLKGK/ft6qIB16zokmPDLfUVt2iwyQKYwBRRdEvibIi0NI4x9bNG6pDTaP8GLMmH2bnBJ+0gvJbEmwqhYFK4NKwr/xyBe1AdjPuiT3f4iQe+HNzPC8RxpSorXUkTPRoH447aaT7dOVtDlh2le/aNtWOBYpcqRNcUBKNTI09XhSDRjFFIv1wOVl4fBvIXY1aSyeJCx09t+pupPwTx8BGbufV3ttu8R3L5Sqxxwya3G9pS/GWErlT1PPywpimRUMKGzpxyw+TRxxr0D4akRbAjZqe15KkEHC7Oe4LTnG4ErsEU0aaJWyuRKaKtOlW3hWngrGKGGDhdBj5O8zdQAu75teqxl0nv2r32uaIsTf6vnR6E9NZTBtY2mUwaWkWq3IqkNSYAoqt7XYjtvGa7SUYxgB5qMimG4nWjTzLVkg1Jn19f0MFtBYjrI6LfO0bEObdc5uzLcnENZw4ro8x0d2vt6tB8dJ1XBonK28TUKCDWJ+QelpKY3LFz6Rglpp09byghC2+G/Uak1dBeDRR3cuEc3/XjKLug6EOkGgZ2U0iNqR786QaQTE3Z9VjpkMXbaoPOwLZAf6FcN1SI/paymBXyaRtjPGXY8KNddPS1k0qBTO+5YRan5aI5J44XCNYiGy4PiA70LNT+rY4oDTmuHmmScVGWJrHFYzmdog24+p0GXWOxW/LAEkEPFbDYxhOK+sOQXvsvuSgq5Dgh0lAJWjdQq3bY/TNRwll2QX5WFqr8Hy7BsdVFgq5EaD2/nCasPNpmZ3Ot3tgkzF6AQ3DyFoyNBquxzQ3PCY5FmZGhWEDTzv7FJ+IgHFLK9tlYGeg2WciyWyPQhqRC3bl0K/tbsR474aT7EndZVhMe56/VMvz6SoeS1szUlLubxuXN2QIq1tX9rxsrQ6eUYB6ZkoXu3Kn46lLJtkjtEAAnj9Zpg+2b3eH2pAUaV3aU1ij6+pauGBDctZLn7eMdXcvBhSi5Qjsi1iFNpMNT6wlemVT0TWXU387SOENEeu9czxWmrtvspNU7+W2VSd3ZxUmgcgByKgKnbZxBjVDBfXMiIUJvnUzqlHsKF4eRlzLhw2CDts6kgo8FDyszQziyKx4OdOaC8nELCUq7gnFy8HW4dRO4l68yJoa3fe7UMW3/Q3eWB7CWkLu05QwnnnfvZuMQ55FzghznR8tLaMgriU8KYYrD1oRQZcf6Mo8ycvW5Ih7kIpxjYs35GY7BMosI9wtUUS5QauS7S6xpSandrm933Ut2AM+hBBzqpG9jB0tOxJreWSzpjMTkwQJ5R6P7UlRG94eVps7X4Pyg2tRhBEEIVS+9kTPR8guqQ7CKuxYmzFMn+lQhr9ecU5SUdfeDr4H+yYnDEtEVUAPdoOEnp+MLLZveRjqW7TaK1sUdJonc59fsNIJep29X001Im0mJCn7xE4MTGtWylKElrcyBhrpwIdMSkkvfXVoxHDV7/aobOjdqCg5Og3mzsJDFaPbk2d0NTvk11xcrq6qldZU316pNdWL15YbWUhcu2hlOzjVHaM0MzrKuS0dleZKx/E7/7TirAMVGPkRRyidcPHhIGFoh+rr285VsBKKW13ISXuf+ojIe510awO2XsfqYYvgXFatLkaNRkahVndLvvWVYXWutWnI2xnGJ2al2+WIrYr4PlmSQ5ixxEKHjsZ2zJjpyV7jqi1l21vXEYOUM23oWiwp0GSl6/tpRW/EwtCke56Fm5MY9dbqwANHF7fjzR899cilU7rUhJ1iHgYDdDgEvESmTFd6SyKY/YpOobQxLPXW3KMEwyJvyFLv1O6iYQrWNcqIOqj9NayvOKzAfBS0EzQR2JnM9pfNMVNpMXeDEKruhhmsOBwXKglsbW5HabWirnjOB2hsR1I/lhATlFesPTXwEobMMTnx9/gSYeG446LaxVy3PQrrVVqbGmo7k37OKbHeHSwmu7v9xO+p7jpkgBIQDcnO58Hi2AxHUMPKj563JhFdaJ09wt8yPLYgjMEvxbSpRkCBy/R+8s2Ot1d4TnqwFo0GZV6Ohda0lHZnPAWii8pABFvZb9vcrEidx9UWN52s3GOYkTRKa2No5ZIrvyYvpHa2LAg9HjMoUKCq00IKuum0G+MIoZgkum+3ZhLqCWisxsPeB4xW7M1q7bPLHUX45HbDQuHxfIp9L2jKFKeG2KTuSKmXuSs59xY0VaTS2WMHNt627ixJ9Y5Fhgi7fbybf7Mpsb2g6nvUIXtHwA5b1tBMd0mihQwhfNtrS3dn74kArtAVAh0tEVl7PBSIyvUgwjATChkXWxTqe5Yqum6iYlwBMTEc3XjGXkWHy8a1bR4/kZxfU3TBsGJvSu46v648W9tvNFGICQcPzskuhdjI45qVYbnBCb+TVoRxx8IbPI8hA6GGTsfjMl9FmyWFe7AIwm5c6wFeFieIC2/Z3pdyiYr4XQpgmkYJr+tCx9lQnRTc+pUnM93KPNXhoYqrKmvtUGwg6FDYDcSsuGPbQKG5RpwSWYnXYndnsLu6cup2qK+Ew7ehEe2XtlxfRdDcRG5891dLNWzzeLJO0z6WXa9ueLGtKUuBXHJ5ihl25bqbyyEQK11dwnCvyzSzBZzqqWC3h7r7eCSr4z02FKElBHlA+XxEZ9zchnV1je9rbUeoA2/Ga9IlJDuV1Tvchd2k3lSb6pbkbnk/XO7+MKlYrNceniztZbE/SKUNI0bnet7d202CE2CS7G1STYbxkS7DqVIxv84af4dha9E/V/IZo7VyWoJViSIZK3OyJrALWUMM5HvuEJNsdKx0HbfMAUOhIA+uNtdh8Pz45K9/ffvw9vsju7f/6atn84Ob/2fPj56Per6+WPJ4FOlZ7qfHWp/+xxr97cNb7URAn+cTsibtgtcDpb97PvbxXzxcnCePz3e5vj5Ofj4vb61gfr/5Lcrdrmnr8UtTpI+XSsAMu2vmdyKb+bVZBxz/+CT1ud4s9qv2xZfXC0Zv8xuL87sinhtZrfc6DV6PCz+8ua/XmL5gJPHFq8vZytdrCcA47B1+x95++78GOsyNmC4AAA== -->
