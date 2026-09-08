---
name: "rar-cowork-cookbook-report-define-operating-hours"
description: "Builds a read-only Excel summary report of define operating hours activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_define_operating_hours", "rar_sha256": "b0dad0a90a57e0be2c6f0e6bfc621263ac00f14320dc5975426ece8e6091e433", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_define_operating_hours`. The original RAPP
agent is preserved byte-for-byte in `report_define_operating_hours_agent.py` and in the RCI capsule.

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

Define operating hours Summary Report — Builds a read-only Excel summary report of define operating hours activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-operating-hours
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
      "description": "Excel workbook name, e.g. report-define-operating-hours-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_define_operating_hours_agent.py` and embedded as the fenced Python below (sha256 b0dad0a90a57e0be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_define_operating_hours_agent.py` first:

```bash
python3 report_define_operating_hours_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_define_operating_hours_agent.py   # or on stdin
python3 report_define_operating_hours_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define operating hours Summary Report — Builds a read-only Excel summary report of define operating hours activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-define-operating-hours
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_define_operating_hours',
    "version": '3.0.3',
    "display_name": 'Define operating hours Summary Report',
    "description": 'Builds a read-only Excel summary report of define operating hours activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-define-operating-hours',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-define-operating-hours',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31f97c942743f266',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-operating-hours'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/report-define-operating-hours', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-define-operating-hours-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where define operating hours stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of define operating hours for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-define-operating-hours-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define operating hours records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only Excel summary report of define operating hours activity from Dynamics 365 F&SCM for a given legal entity and posted period, with Summary, Detail, and Top10 sheets.', 'example_request': "Build a define operating hours summary report for USMF's latest posted period as an Excel workbook with Summary, Detail, and Top10 sheets.", 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook name, e.g. report-define-operating-hours-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary report of define operating hours with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDefineOperatingHours(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDefineOperatingHours'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-define-operating-hours-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportDefineOperatingHours().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6adOjVrLmX9G8N2JsX6pesYPqRkcMICSEBEgsYnE5yuwgVrEK+fZ/n4OkKtvd1X27I+bLqMqWgHNyz3wy6/Dbm9t3SdW8fXrTQrdcbN08T5OwWbhlsOCqsWoy8FVlHvhv4Vdl16Re31VN+/bhLQhbv0nrLq1KsJ3t0zxoF+6iCd3gY1Xm04K/+WG+aPuicJsJ3K+rpltU0SIIo7QMF1UdNm6XlvEiqfoGbPW7dEi7aRE1VbFYT6VbpH67wEhisfnfGictogrItYjTISwXeRi7+SIsu3nDLGxdtV0IvsImrYIPizHtkoX2ZP1hsQ47N80/PBbqVY3AizYJw659B2qEN7eo87B9+/TzLx/eUvD77dNvb37utuDWm/qQev2QWPkqsDDLC7bmbhmDNfUETFiCa/AcyFiAW0DFxevqxzbMow+L//zPbHSbuP3p0+dy8fp8fpv/qH256JJw0VXuQwXfrV0vzYFi7wsmH92pBbbr+qacrdsCD5Tx+3Pn75SqevGX+dmPTybvcdj9+PntZeGq/Pz20wIY7/Nb08+/32cq9Y8/vefVGDY//vQ7nbb3LqHfzcSA1O9fXtcvsmDh70vTaPFFO/Lci1cT+mkdAuJ/0G/+PEV/kXuZ5Mtz8Y9V/WHxfcqzPn8B8j5jzAN0v08W2ADsfHu/VGn544tHU4EAcUs//PGnf0TWT0I/y9O2+5fo/vwknIDABtZ6meSnDw/3/bKAXrp9o/mP2dYgYP4dTcDyr+y+Geof0X549m9I5yBo22++/C65722A/rL4+R/q9s82fFhEn9/WYQ4ytHG9PPy0+O0RIj//EPx+84df/gpI/49kNJBj/oPCl8It0yhsuy9ffv6hfdz+4Zeff+hrEMWhW3zpm/x7NL9n1wefP1nwterHP+8F/I0yK6uxXHzLocVvVf2/mr++L85unga/328/Lf6YifMHWsxKfGX6NMEfsrEFsv7Bjj+9/RXUnRJo0/uPx6B+/Md/LKTUb6q2irqF5ld9twAO7tIinIXXk7RdgL9z1WhCYNc2BYZ9rQPxP3t4lhjU2l//j/+o4h/9VxVfPuvwl2cR/vKtCH95FOFf3xc6IFo1aZyWoMCqzPH4uXRjUGhnhnUTtmEzgCLlTV34EeTyx/nHIi0Xv/5Tul8eJN7r6ddHDU6fFU/ldnO1a/s8fJ/1MhNQ2Z9a+ACMwlvo94B6XvlAlCgFRfoD0Let8gFUy9kGbZbm+SJIQT0BoPQEAmCnTzOxX3/91XPb5HP5LM/Y4olW7RIs+CbO4uNHoFOUp3HSfS5DP6kWP/z21x8W/734Z7sexGceRwASLy8ACUVNkRcgq/oCLAMOAi4FJePhhd/++rIsIFMCeAU+S6M0fG4GUZmFwVczawLzESXIhRcC8wLTFrNZZ5RMu/fFLlp8k/eFqDMqJAD8AKzWYRmEpT8Bqi5Q55sly6pbtMAbbQSwsG/DB9dfvcZ9iFiA9Ha7XxcSdwQYVOXgf7OYj0Vgc1WmwPzfguB5HxBpfmgX7FcS7wt5jsNF7TZunTTui0fkPv0yA/drOyDuLspw/FzOUBvOpnokxdM8YBGwjP9y6cfZ56DtACheBu1X3o817oyU+gMxm89l+wp4t5ld4QMAAEzjPg1mGPivV0i1IBLz4GE/IOlM6eWF4OWVRwyuv9+cvFqJxbMfWHzuURjBF/9/Nj2zmsx2q/JbRufXC17WVftp/rnDm930bAofYlXNM9V+70q+Vp6vBfhzmacglprpv54rH057rXkWtb4BQqqM+qAPIgaYf6b7COg5QJtmTgX3c/m10gOhF4+yBnwKsh9kxxyUXxnOT79KmoAUn69/R/1HADTBrDYI2kXdezkIqCgMA8/1MyDV7KuvDgTRHc7eGZPUT/6k1Wxm4EBAfwGESEGaATR4/1Z9n0+/iv6njc/mZt7yaPx6kJPNgwCQI5wFnB0yuwqI1z0baqDnpwcRoEZRd7PuHogSoOnzZtiE1z5t026ugE+7hjUovR/n76em893wVoNEAMYC4V73wLqPBJmDrQCtC5ABRCHIlyItAZQDo7yM8CDoFnO2g2r66jWfFB+3XwqFj6yaMejrxlmRec8M688Adsvpj0VB/16YAHrFvOLB928j7Ru3mfZcGFuQKIDj16dP/H9/QvizR1h8pfvp7yaWH/+9oeYBysafA+DTIum6uv20XD6B9CuOvoOytHzK2r4w9eMzxz9+y/GPjxz/E9Gnvp8W/55gfyLxSoxPC+QdfofnR4dXYL0+wA7cR9b+iM9PP5dq+HvFBOyrAsg2e20CIP4N3r4uARgXN6DMgMVPuGtnlBwBMD/qO3DB5/KPkT5nGoCPMp4js63+UAEeOA+i/umxbzAEHpUd4B3M/WAczhPYIy/a8O1T2ef5hzdQAsP/afKacaaYY7mdhzWQNWBBl4aPKw/IlgUgW78EIFbL9tlS/fY38+r627NHbH3b1M7KAhhx6xrI9exiAbK6TTdD1QegRxfG1VxfQSdSg+2P1gtsBPgBBOumehb+OabNjd2jUN26vxdAefxw8/dXoW7/GP0vrJqx+g9J+rQ3sLMP9P2wCIAo7YytwN6zKeYEd9vsodB3ZXngx5cnfnzHIjPo/Ali5kbgCWBu/MjpD4vwPX5fGJq0+S6Dby3u31M3QY8xEwyqTzPcfniVOvANxhJg1q8TBlDrNfM9hvOyB+P0z/N0M3v9sWX+AfaAr2+bvv1rhBe+/fI9uR718Mscl8/o+lvpnqg9J+Aj9+ZFL13/aWp/RGGU/AgTH1H8/Za3t+8a5YnOf8/z+Efwnk3zbBrSO+hYADu3z0H2dNXD88Xc4AH3z5D3J9BfuAOInTlMv8MbMH8AB4Df2Yi/e+d3G1WPcfAhZu52z3+9+O0NpJYLost9JddrngDLQZ392M7d1BIUH8AQXD/LBHj2700ar81t4oJmF+z24MANYHcFuwQVwl6I+mQEh6QX+SSKoCTm+jAcITiGwoFPrCgCR0lgDjok4RUS4hgG6D0rzZe5X0xngcCyCF6t0AhHwC4gBooHAU3SpE9QKGDluYRHrFzv961ZWgYvLZ9azSb8NvTM1ngpC6oMiYOVAt7umOeHW64QcJPyJtGCGjKsHJs753xqUF6W0GV1C5qo2+4uQtL1ui0zqrurWs2ZCo0hD9TBRWGDCXcZZIurcij31zRN9DNmOYVzkSiaZzTTsq7IIacJ5HAue1/We+M6ufqOQ4rt2dl3N80dtMlSyB5GDwKwuXaf2uSwXB7b5e0gkZop5adc2EsiVZhepd/vq62UWPsLhyGoMOZ4Sab2+ZTncIHwZDtheKNbqtNncCoeKArSmjt+pxQdQffnnOSWekrkYr4n1rmUtHhVJJsMVPfbmU+gST+K+O5Kam5xdMpdopv2WVT6LUstjyl+UhI5F80poaWyIWgopIiJjIaSgPbEClpFy3B9WBFDvbtMDSPe+MA7iynk7LVb6Km7vGqYXQ7n+/uSa8aeIw32jA4qmk3egQ+rJTJuTE27tDwDXatr1o2QQtXKZEen2M4zGL5a1HQ9HeKWHzNifXCS/Dpl15Ybe1HLtVJslR3dS4dhX0AWGMDOd56s5KVG7QV5J7ZwwmH5Jrw1es44lDXdNSBgsw/ZfLuBOBGRtP2EHbSbUfueI1bwqjqmarhnUJhl691eQHxHPbphcI0i0yE8mGInI0vdnXw8q7LqHPg+XCd21hrOdccY8jirgJ4D25bvdSxAHXzeFAjFyQd2szxzJn31ScPIcsTXd8bN0wmT2JfUbROm8XJz2aU7+tJcr3GCHAPiKl+YrthIS2k97fO8z6Y7i+MJdqd17qCfwjrN8ATHJ9lMw+KK7KTDSbf5yyQq++hWBQdXTDvZv6F4nom5vU8a3U2a3GSQ2t7Sohj0aG3uOrHOcrhSmLPZovT5yGladoBPzvJ2Nvf13XfEiAiNzXHYH8QIt6q75Dj9Lof4FuXXN5Vi8KRFBZYgDTeGPMyzsePNda/cxYzu2j7cijkR1ergELUqB0foKFvKcYv6od8olHwwQgI96OjxUJssbXN4CMVLmsUudweVd8RlucO3OkntojrHYiLkIktK5cJmElvpIO5wPph6esNO2Tk3cvXqVD6PW3XAZNUInHsLIcNSqJizClnlB4yRzW66bmPdKfrpRBhUlFHeTj1aaSUiziYPOftsmbaZ2zhr9rbNHe018GnaJmPIhty+Z6mTqMOGZ+5ibIPgzqY1DdTJk9uK4IfRD7VmDKJrf5aasys51a7jXE5NJNZFxcpJWoev+GEnGQN1lHDDMFwqFg/LM7nD4Mk0r9yW3tJ3trvI7rrPI2ty66Ahzl5iFgIM6Yc9MDTWMrVZXrbYOlXj3sUNeX8zGDwVafiiyMGgdfJ2dx6nxJCul6kS9Z7iThdcFG9M1iPDys+UCCblarff7RMmb8+jbaV7SSCD/D64ua6UeFSUylXdbXJNJERsPXoBkqQByjDSEDJ5FmSFZ9419zCp49HumeWg+xDhSkFjS2dVrPXlQYJlSOxg5ES3hsBTW07Z8fpZXcbHiCva9MJiJm/HHr1yCoj3bnlqrtbpTmF5VDgMdJ4kSmVcVNWP1xbSFFk76Uyd+k7R7rslvqXaayFHUI2icXyS6AhZmn4jLmvaFzR33CDRgcVDHicRJoChzDEdv15748ZfIeL5QrJa3yJ3rz2nQldiDRYPBgfllLuW8LtJpZyyhOvD7SSid6xPM3fSjgnGU5Ka+UGwVm41s8cD5m75ZNxdDU5wbn66D5caN6ZsWuvn5Joz1IVns62NK3pU3RBDWl3k68VqVhSl5PwdsmEpU7u6Ok3n6bwrMF/js0TYBOuro4nHo8DdmqpKeCvxp6ARmvSwQ8OTyBd1jQi0sm/v6TmMrbhp9V6+l5uSa3zZpC4hzaz3t6oK+7gKK+xMTkZjMkKKxF7ipH7HEHEHYyNRIbd81QeWSENLBet6/tRQrOjQQm6mhm1E9HSPhHxdST6DN9LeEcLl8rpj7zKOB91my8erZo2o0DKNKJxw5WEYbukqvDQNjgSFAZpROqNp9LjZxKdTjN5FlBbk9M6es4aBTRfVrjzJxpG8xnk0qVsbYjAG2azoJAadu3dGkgtz3fl44DPaSnY38RrOFWYlqoyZ+QwXO2xhKOpprMLkuNT3NU1Ch9XI5vuToou904zwmLmqQjg6KuWGV7UwBmcgh/Z0sjnbAmxLBYvdyPjcFPDYt8rmogjBOhdyhzo1kzKFe1ljT4lsbq3BGMMTqMq7lOPl8ya7ujAc9gnWkicbp+1TRhywC11u8go+t4cSgY97Adt1nhsnI1vfKlbi7yHVcU3hpJtuJ0q6pUN5ILNuLHUnk2+2MbNMyrPWhpYNhuGkmSgqkU5H8bxzS+faUNp1vKoyJ254DdKM3NI52S2xCCq3sSHmKq0jWxqVOaKxWUuDdyOjtQWxrg94QBniHlUPuW8agbHvGf5w5YZCvpGQ2tq1BcpXc5ArO2zWK0HYNtpmn7VFcBa0kCjk3HA5T9ldGQ/mbety9U5D0GR7XzKPrH3Y8lfJrVWHGoeoPo2NlphWIvWt18jlNDApvYeK80XlD93VvsrYLkWUDhkz+X72zzWemmcaNCcGj8WgQVIVnz4jwVVpO4xPTNVbZ01kuMey2+uxrd52Rkrfe4nMg2WO2K0PH3v6sBG2Emd26RHlQ1uW2m2rsvt4zILrMTgiYLBmeY/dEtN+vYUoARZG7Oae9CtzrPBom5V2tV6lGVLj1Ea1V5Be7JLVypZJYtUfjjIhN6jd4jxzPCxNNIo2RrGO1ZiYukChW5LobPlylSoj22qt4KCQXxIEHlIpHJ7owvTPsN7JAVOwyOTgm60XHWzkMI6ar7enahfLWhjrN/pcbzWzu44WH/qquT+msevZy9j0hvUqPlxTfFvZOZ3xh3Pqbg1SlEG13cJNoAjiEjurSKIqXFPdQ4saDXoNbHbjbvvt+q66N+lmleJeFsllOLWwXawb4nC6XSzoYoyKUUMsf3cGuVCdnbHMLtnEVLFp5mde15Yi756wYSwOaL9Xz6YvQ9IyWq5dlTqbdxHm8XOpJFsncjnMu4uEWe3N+5IRc2TMc6nQI5GbjNPFP9ytzO8vFoFP8VDlRsPpmaqgLmekJ9muJcbMfc7abPr6REqVmvfyWXWYTB+qJHGM2GkP4+TswvKuLUEnp0injWI22wznTKS7lChn85ak45p8YRU80arx6G5CnvP2WZ1h7snuaNtr8Psa0U/FFRPwo9TEbn0qOKtTFLg0jlIr7fg63RWH3Z4J8Fhbp0N1IQD8kraFkPsJZXTCSg6OoHRoEo9e2gy+BK+uVXFadpWFEaDfvW42d73aaRuDP2XqZgOR2U4jcNm+3JpNe4GOuhrDQaTfVrRsYXAd0bezCjkDR+3SsPY6eAcGBrXcHbOoPvjxljt0xqDaIVVcNTbmYRfbW5Vm8dyxvu3Dk2ehLrK/NeEWBgl3DSl3W4/act0pTjBU2m3Uk3zLK1NBnpjzFeGymEbT03qz9qiDuqFqNs2cmyhsWVOkN/mRYkclVdnWUHWvP3I7o6lZs9qwG6tVO9HiCq6/aj5Dc+1N3jKOax5UnGsca3kaIbh1HLtfW1qb02Snrg/Lu3xbMVRmKeONWVvRCq+N0151r/fyfpFMTLB3UoTuSaYXVj0CkGoIR13c5QhmGdD+wqcbm0dNuFdE+6KxvMpKknW830j6yHikcjtvrmdEX29Xpz5jqNLT2WvtW2yVNAqkckJhJ5pIH30uZW4njxwde7/zBhre0RHPivFgbx2296Go4VTOs13G55N6mUHtkZL7Ne8ahHPYWYhzsC7WpRJTrXOaa+mUMm5IjZycQTc31+51sdKPqZlD1jXQCgrKjjWKsyfqrKnnbthiObtHyl0/3ZglmVCQfIRiWGFPjrFnOPq4bwNCVEGOd0ttwvyrVIw4XYEeimdI+Gb69oTEG6sY1esVbuP1oTRbLgOd1SCvimtkoHi4EwvJX9rXA3OXlK0bKeWBCXKWjW8SPujnbp8JOMwr1hpqp2YcJAOpPD/rOxL2IrNtTRMtcmWTTC4vhNxN2eBFC7qmxh44Zy0oV67vM2GNLddLc83hLLdpx3EHp2ozYl0BA8cw22RIozgtb7RG8zudhbkkHO5NGd9IjOG2cW304aXTlvgd93AZDIVW7DbJGkLDI0ZTqZgNlbn0Sp33Wr9D/RpdBtZUUd36DjtXA2PZA3OqS7RPJmSECjCZZ5dBhxIf7vrMDg31dLiN+HggpymyamN3G7pdWEADvAQN2H4L7bbaWuPCLSc1nGySlbNDDQTV+1JcylggKWxy3o5LSGD2yythQ7v6tJEwJTltRiVoEXwNwf02UE8Ysh9Ol9N5Ne2dI94RNhZN4nl9dFe3m7SjhfuRv5uejYjwjRmTlZhGBKW6GkZE7NpBKUAtUfsAFfFyPyT45iLgTXO+U6xQMJijRR1CgOHzqNkrj1r5wTZEQddL8QSCYVbu74J9zsgGyaJNaKx6Ri/UO3KNMUW9sZw7tnsMBj22rixl83SLbCLYKrxlbaI0IUba6K36gvnBvjmXk0yu3LsGcpLMh7iRnYCRfaoM5N2EOsuy4l0u3cJLRgW90UkLeFRHVqVE8RbcCp3uD+jFJqFtvPe7Za6vIyfkihtRSq51lET6Kq+bLiTpiUY1+XgJt5c2gDgphifvfHLX8E2H6uUSWg9QaiMSR4nBMpIw2qdZL5EbfT8QeFq1CF2xvrQ3Oaq4uKUOJorNTrgjigAVh2MhxN50qXfkUi87J1meysC6dTV+IbcXmJ10AVQQU4lWm0K6XZEatLnHkoUqU4ZGuKCF0g679KAnZXV3ckjwbZu47O/bArszuzCCzkQouh1BUycruZ1Gm9NE6xZhQxCcw7D09SQU+PUFYmt5ItZs5h419Tpo/YnVaZ2osiVZp0WvEIfQ7vDzZkQoOjvByuVqCHs0AnWEdiLz0kH8ZSnFrZDx0463JlzhMayJG+WOhbwqJ/a5a46+uL+eEKEFKnuC2nWHEd/sq9BBzjHJoD4VpioVYdU5IhlHHyealVYhhHc3dslDfqXjSUXZ6fnWw65uMpOiC6uDSLE3y6hOJFuuV+LOs5CbrhZDJQ61xmxkYaUwsF+oUqzK0UnscHI72gq0oWwEgAjl3DlxXBV+uQ/hnqg5ASG2SyQew6MwFFBD0aAbpnXxINL25mAPJ9AOHODQztCBdtI1pMLhJkd0OyKCBMBOW3dIMQgl1im7Sy/g8rWFGmsDBxNu4pdq8ivc36yky+BbnOw3BduJbJJ3W2m/Qsci7tkUVu6WdcrbHHFX1Ol+ZkTfcK3yJBRefA8v+sCRaTMuk7x1oMNeWZWRDtnrTigubYSwW/FyV8A0DGFK7FTiXZbVItQgdxltEBOvpBNNJAf/qIb+cCoIH8yiOJtuK68vYTrAbImb2OVKWEoZejd4tjiymI9P121lFeZtuU2voodxcgg6/QZdjrYpC/CtwQg3kFdHH0JM7N5ImJ1ZwnHQ7yPoYO8XlCxAw0xDTWxcrhjk5sRNRyDgmusasSOfakyk7O4ePPiRMTgWw1j57qB7ln21hrE/alTqakRgJ17ClwSoKWIzyrJfhIN2r63CurakuhsLyzqC8V0i5R4mqhrHV7RPyRR5JHIBHdu+ZDFgviCOHV2ZynR95qAhSLetMLoXWL5HV+wSgv4lOnD4xATBBtYPeA7GcQpqmYQTo7K8OtxWoDMDSisaWe23YiOBLsZ3tgRcIJOpa5OL1RtBYPJlklnlslXLGxjtVMFFpmiDrgk3V4vzXdtWt0JfulcibWAmoECUM1F4ng49vkvkExQrUz+eVohptePqwvjkWSji+LoRVkua8I+03qidahGOUcYjfHHQ/BZGrtDmmlhgZqVT/kh3t7D1EMqb4lImbPLcbSkFuXf0VBGaOaoNJkmTGlkgfq4I27SgnmDwYTdGGJRNHr063YersyfKq4AOomQB3SFEjje8q+g7shhgqkdhgp4mWfTIlb1WyiMPc7qZkHo8BFKcBSJmildG26LBWT4UtHgHE8QJJ25DTyeX88WFEL2gqZWnH7XkrpWrJYAgWrFwZAKDDma1THvcREbhohZ25h3xamdwHKkMhSeiy/qweFstCQvLlzW9O0BNhfaHDbmeyrK5KHKMQoRWWgqJEoEXGstzYuQ5fUxT0yUotIyabGgySiX3kQFiVVYM5Sq2DnKxJV3kL6FKu5tbd78sfbG7c2Gy9QQihckbiQxHL8+HVoyyUEOlHWyIFwkNY/IM8Na15NUq1jClItjVGNuE6Aocr3ErmxTHNdwOCMz4ysXEJSMxg6DH+qteIQLrwDltdXri3u9WKVhBk0Sny2QEXtUn5HlDb6+XsPX3y3MuRHp5z8uQHHYh2uiDP+EqRrorVOql3lqiYq+vdWe4e/GqR/dYbB7x3lkxsiwJ5bnpoTGtoH3lnq8Hkrrjl9ueBNhvi4MAKdHUlmGPI+6oQgI5dqt0wLaIT6I9zIbOGb9Eerv2iIIv+WhYUvFdl8ptYA5e6JGm5529RF/FK4SMdqYwRaPv2vnptDYaa/LhUQ0YladlwzyVkGMFQj1S5EG5eZ1ptqmIUzFG6BJovtGTci0r/EiwkBFrpOGVVnkQ6OtuHQ6ojOoeR0UdtrQHxNkLQGg39N3Aw/jhHm44IgkO6va6wg740TsBvfktcdvjZpFuc+G0gZW1GgqBj63wHlqyd1yeWBhPOymSMznqpCzjxv1FPuL3+4rvkNuwHWJz51RwieaWEC/pDdOB8dxhOYZh/vL24e33w7m3f+1VsvnY5v/Z6dHzoOfrOySPI8fQDT49eH36F+X55cNb46dAmufZWJv38esw6W9Oxj7+00PFeev0fC/r69nx82C8c+P5LeW3tAz6tmumL22VP94dATu8vp3fbWzn11998P3H09Int/m81G3DL1315fEO3dedaTm/EhIGqduFr8v4dUz44S14vZD0BSOJL2FTzzq+3j8AqmHv8Dsw3f8FYaT4SkUuAAA= -->
