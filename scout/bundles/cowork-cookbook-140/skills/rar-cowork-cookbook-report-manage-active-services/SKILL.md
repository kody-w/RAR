---
name: "rar-cowork-cookbook-report-manage-active-services"
description: "Builds a read-only summary report of manage active services activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_active_services", "rar_sha256": "dcd71cc44469342e8b593b3db5c26ac3200cb9b6b710138f08e2217868ad7f87", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_active_services`. The original RAPP
agent is preserved byte-for-byte in `report_manage_active_services_agent.py` and in the RCI capsule.

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

Manage active services Summary Report — Builds a read-only summary report of manage active services activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-active-services
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-active-services-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_active_services_agent.py` and embedded as the fenced Python below (sha256 dcd71cc44469342e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_active_services_agent.py` first:

```bash
python3 report_manage_active_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_active_services_agent.py   # or on stdin
python3 report_manage_active_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage active services Summary Report — Builds a read-only summary report of manage active services activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-active-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_active_services',
    "version": '3.0.3',
    "display_name": 'Manage active services Summary Report',
    "description": 'Builds a read-only summary report of manage active services activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-active-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-active-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a4e6acea0a3c9dc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/manage-active-services'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/report-manage-active-services', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-active-services-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage active services stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage active services for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-active-services-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage active services records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of manage active services activity from Dynamics 365 F&SCM for a given legal entity and posted period, output as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': "Build a manage active services summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-active-services-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-modify summary of manage active services activity from D365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageActiveServices(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageActiveServices'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-active-services-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageActiveServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916abPiSJblX2Fem01mNhFPQruirMwGhCRAC1oRUkZZpPYF7QtCZOd/HxcQkZlVUdVdZvNpiHgPkNyv3/Wc68/165s79EnVvn1600O3XPBunqdJ2C7cMlgw1Vi1F/BWXTzws/Crsm9Tb+irtnv78BaEnd+mdZ9WJZi+GdI86Bbuog3d4GNV5tOiG4rCbSdwpa7aflFFi8It3ThcuH6fXsNFF7bX1A+75/e0nxZRWxWL7VS6Rep3C5TAF9z/1hlpEVVAo0UMJpWLPIzdfBGW/TxhVrOuuj4Eb2GbVsGHRTX09dAvXCC2XLA3P8wXsxkPC8a0Txb6U60Pi23Yu2n+4SHEqOoVvOiSMOy7d2BceHOLOg+7t08//+3DWwo+v3369c3P3Q5cetMeFkkPa9YPY/SXLWBq7pYxGFNPwLEl+A4UA/oX4FIQRovXtx+7MI8+LP7zPy+j28bdT58+l4vX6/Pb/E8bykWfhIu+ch/m+W7temkOjH5frPPRnTrg135oy9nnHYhLGb8/Z/4uqaoXf53v/fhc5D0O+x8/v1VABXeO2ue3nxbAsZ/f2mH+/D5LqX/86T2vxrD98aff5XSDl4V+PwsDWr9/eX1/iQUDfx+aRosvusIyr7Xa0E/rEAj/g33z66n6S9zLJV+eg3+s6g+L70ue7fkr0PeZeR6Q+32xwAdg5tt7VqXlj6812gokj1v64Y8//TOxfhL6lzzt+v+R3J+fghOQ7sBbL5f89OERvr8tli/bvsn858vWIGH+HUvA8K/LfXPUP5P9iOzfic7TEtTc11h+V9z3Jiz/uvj5n9r2ryZ8WESf37ZhDqqkdb08/LT49ZEiP/8Q/H7xh7/9BkT/t2L0amj9h4QvAEvSKOz6L19+/qF7XP7hbz//MNQgi0O3+DK0+fdkfs+vj3X+5MHXqB//PBesb5aXshrLxbcaWvxa1f+r/e19cXLzNPj9evdp8cdKnF/LxWzE10WfLvhDNXZA1z/48ae33wDulMCawX/cBvjxH/+xkFK/rboq6he6D5BuAQLcp0U4K28kabcA/2fUaEPg1y4Fjn2NA/k/R3jWGODwL//Hf2D7R/+F7dATo788AfrLE6C/fAXoX94XBhBatWmclgB8tbWifJ4Hlv28YN2G80gAUt7Uhx9BLX+cPyzScvHLv5T75SHivZ5+eWBw+kQ8jdnPaNcNefg+22UlAPWfVvgA0sNb6A9Ael75QJUoBSD9AdjbVTmglH72QXdJ83wRpABPAFU9SQL46dMs7JdffvHcLvlcPuEZXTw5rIPAgG/qLD5+BDZFeRon/ecy9JNq8cOvv/2w+K/Fv5r1ED6voQCSeEUBaHjQj/ICVNVQgGEgQCCkADIeUfj1t5dngZgSkC6IWRql4XMyyMpLGHx1s75bf0RwYuGFwL3AtcXsVoD5i7R/X+yjxTd9X2w7s0ICiHERhHVYBmHpT0CqC8z55smy6hcdSL0uAlw4dOFj1V+81n2oWIDydvtfFhKjAA6qcvBrVvMxCEyuyhS4/1sSPK8DIe0P3WLzVcT7Qp7zcFG7rVsnrftaI3KfcZlJ/TUdCHcXZTh+LmeqDWdXPYri6R4wCHjGf4X04xxz0IwAFi+D7uvajzHuzJTGgzHbz2X3Sni3nUPhAwIAi8ZDGsw08JdXSnVJNeTBw39A01nSKwrBKyqPHJS+37i8WonFsx9YfB4QeIUt/n9qhWbj1zyvsfzaYLcLVjY0+xmUuRucg/dsIB8qV+2zAH/vVb7i0VdY/lzmKciwdvrLc+QjlK8xT6gbWmCAttYe8kEegaDMch9pPqdt284F4n4uv+I/UHrxADsQaYAJoGbmVP264Hz3q6YJKPz5+++9wCMt2mA2G6Tyoh68HKRZFIaB5/oXoNUcwa9hBTkfzpEbk9RP/mTVHAIQXCB/AZRIQfEBjnj/hsnPu19V/9PEZ8szT3m0gwOo1PYhAOgRzgrOAZlDBdTrn803sPPTQwgwo6j72XYP1Aqw9HkxbMNmSLu0n3Hx6dewBoD8cX5/WjpfDW81KA/grGeSvD/LZkaUAjQ0QAeAHKCKirQEBA+c8nLCQ6BbzBgAMPbVgT4lPi6/DAoftTYz09eJsyHznJnsn8ntltMfocL4XpoAecU84rHu32fat9Vm2TNcdgDywIpf7z67gvcnsT87h8VXuZ/+YXfz47+3AXpQtfnnBPi0SPq+7j5B0JNev7LrOwAr6Klr92Laj8/6//is/49f6/9PQp/2flr8e4r9ScSrMD4tVu/wOzzfEl+J9XoBPzAfN/ZHbL77udTC33EULF8VILPmqE2A2r+R3tchgPniFkAQGPwkwW7mzhHQ9QP1QQg+l3/M9LnSAKmU8ZyZXfUHBHiwP8j6Z8S+kRO4VfZg7WDuEuNw3pc96qIL3z6VQ55/eAPwGP53+7GZfYo5l7t5CweqBsBjn4aPbx7Q7RKAav0SgFwtu2ej9evf7W233+49cuvbpG42FpCLW9dAr2dvC/jWbfuZwD4AO/owrmZ8Bf1JDaY/GjIwEbAKUKyf6ln55+ZtbvceQHXr/1GB4+ODm7+/gLr7Y/a/GGxm8D8U6dPfwM8+sPfDIgCqdDPjAn/PrpgL3O0uD4O+q8uDW748ueU7HpkJ6U/0M7cHT3Jz40dNf1iE7/H7wtQl7rsLfGt8/1G6BTqPWWBQfZpJ+MML6sA72KwAt37ddwCzXjvBx5a9HMAm++d5zzNH/TFl/gDmgLdvk7795cIL3/72Pb0eePhlzstndv29dvKMc4AHZi//HakCncG6weCHL+v/ZbF/RGCE+AjjHxHs/ZZ3t++66cnl/6iF8keq/4P3q/IvwCuRO+SgnvrqoWUxN4IgIWYS/FOLsHCvIJvmxP3O2mDxB5UAQp7d+nu8fvda9dg2PtTM3f75V45f30CxuSDf3Fe5vfYdYDhA3o/d3HVBAI7AguD7EzjAvX9vR/Ka3CUuaIrnv6z4AbnyfQzDCBrFkJDycBr10MDDfYRwfRSBYd+jPcIjV/AKpSKYChFkRVIE5QZkRJFA3hN7vsx9ZTorhNNkBNM0EmErBA6ASxEsCMAEwsdJBHZpz8XBIq73+9RLWgYvK59WzS78tjmavfEyFuAOgYGRO6zbr58vBqJXHmST3iCeIRSGNs1l0/ekTU1n3D8Lfi3X+SGON7LcJRdrmorkchB7AQ6sQBDM1OPt/XqpHZajgR4gHGfMw6kA1GnIaOlu17ws4sddsozSYEsLIT6uwumkD7mzSfgzrarNNVVvYyP6REuebOsIcRZ+yrW0hJaQBqWuBva9mqNzbM3D000OLqJn2qaTuyjb15QfYZBYnuITcnJ98iTgmSn112uL8NCOCpZh2VJqI8AbcL2odVlzDxchP5iI6urGZBx8IVqpmkNzrMNZzomw1P1hEJwbvc3ttG3FxHf6Ih/2rZhZ8nLf4aYQypfxYoROVGxZgkX1+uzuxim87rIb3RfiYQkWtfOypZc0FLBn8u4ICZe7dsEmDSoYnD+OPNOhneYm96M5GUPsXGvTPh8tImEmJJ60kMuz60UrsDRR8qTYrDnHOa1DMlLKUsR5y28q8XBrzOu5tuPzRr1NVrzGfLOtzW4Ut0Sldr6THHgux5PAuZ4mWvZug8MRKg3d95VycTZVQzCilFYpokjbu1uXbHWKa05f5eG6CPVd0d0zTeSssnOT466gnaWuaKpQxKK0Yc7L3fGkFsbV3UVFGR5xWYXbG1mkjF47hqmftKaNCWuzYa3hsslFVT04OasvWzYZfGlExyu1EpGrpucZj7gbolGvK/9mACZxcDt0a2robzKh08AHRJORF2EyGck2GaMItLwU8CTTdrf9dDg1xd6r72yYkDfykLooLCYSW66PO/dEmNvlylpxsctE68vxcLhtl3IOg66CWTl1dr31+40wBlur4LZn4bJp9VHGJhcPVnqnEbp2FMmz7XCZfA1OzslWhS6J0nJLCRpqDkZ2BAG/H7JjodyTM4WpZyy9+6rC7bptyt9tnysTjdjiMd1nPsTV6e2uOJCs1piNlPmy4FdlkrO0RGJL2X7+BDYZ1nyJHJMwuuWuEV+tzXDO4hKKy1CRSxfOkB2ijccSJTBIa6+biTpZHXfHDxeGiwmEElSdu5CdqqmJafk52hZJrE1XHVtLt1TK6JSmr1JwXvPXTk8PUb+GXVSofEYx5KBI7km9NPouYe+hEJfWxT3ZQnYK6tQ1M0YIbBVjw2pnqxuJ3MbwmuJ6f4tUejmOcHc7dGKLb3ClOCFOn97k++4aO6bgYVHEuyepPLndIRay1N9U+5Jxebl1TpXDYky/p/QrquzrVdklASZkkTCS5gU3tYY5Uy5WSV515cMiR0vEhbwSq1e35i5izo3PrbHmkLjDVM27x9qIWDmruvA23lCXvVA4o70lTnKS6Ahfbabmur4LW74axMSEMk5mpNuZkzgIjVSk7Vs1EyhpLcU386JS57wxVYwOnM6VZTn0TFGhfV2tr6p2adEspaJ8yMPjnpc21VmP/QYyN6RFG8WFGdaRVqUHeXMn78OEy7lOZDFMDmen8qiTt6z3uH1F5WrkTPWuCD20rcNNqp2I9UAp9joNqBuDCQmpsH2z5S4uqwVVR28LhiM0I+ROBCPLWu8y5MFKi0kzLUoo0TY5TpAtY1ht8Bs+VUaIW2mNXy5L7RLdDqx2krpbgkVZeQhWohCUDmdeZGVt7Xn86F/3h4ATAGsSPSGPJLXEOBI7U1dP9TBJUtHkzuo2i5gAItDrMXQlvR1YasdG3WgF9xW8h/llUyWVoveM2w0GdgjKAyHUd0oQmQMfppK4puHpcolJflO5R7+0NdBA2JVM0JEQeOQeLSC1Sm3jwPBW5YXVRFh2mwtcVffywVhWFxzZOPyqMi8Zeugkd9hjrXCIKdW1xHOkqq3RyGyhmetb3JAoopop2+ANjfI0tt4ZmabSIpMQ25PV4m5nrxHWWg3rAkeQLc8ghijm2UawEYeOygwno4iU1pqBMPodV4SarXA16u6Gt8u3leRv9nkpFrdrB7nh1jd86YikCbO5WjKoclqApdxYamcsovnKM9sjVbR7Jy+j9O4A/kwvzAo/kgkuJseeYa/ZSq+Ozajaxy3ForHWNAN8X3PBndJqRw7wrrkdsoBlfJnKckoW7KQ3Y0U97Y2xuBgqE1ubtclrKl6DNMfOtOvkkghhV/64rm6QLxerS9j7MHFfqbVfFx19XAoUs7Ib6+TFVaeNaHxj6cLCJ6qg+ZZv6OvJz+trclbU0R+DId67fKMAzGV0uFz2CXNcXZCJ2/FbnpUPLmWoZKXFh2OWRGeVEM68kzPImmP0jW5vJW4MyavtTV7KJfsbFZ3uoA+WN24sZRrC7rj9NuQ5x9XwYOLO9V2x0DPDxuTUaCvrtjrTJ9Al6OLEKixFZipu6GymXUqIzBnRFE63Uc+LcVhPY7NP1iN80DLdLXBmH+GRZ+mHQMjhSeQBUG82OkclabTDZOdwok77S3dpt5lr7hiKUstoDxDEIc+5o5X7wpnQoMCykU1izjCkVeXSU2s49niU2GtnM/lNTjg9spZ4DgM/CtbAGLBzPnvK6Shw2AFSzla6P4vJrfMKKyd8g0QE10oRIct3gTi6XFqeBu0ibdI1gZNFoW+lQ5RKARvxFkwLJX2MD4pWVBmir7DctE52TpTOWZHGbdcRh/XGPwJAFhF2aa+gi9YcQPN1061pWbN1pJe+QakWZV8ktx0jHaKrlKUycy2qJXU8e+meH/aQnW/ZkLtdEdJOD8jGXwo7azlQU4pGWnOL98e7smU8uTsbmC5vkt0ehAG9V80yy9NshGOnJtZmKdJ4ULZJEe5CLOFNchOjOMDBrWoYe8M/ubJapMiEM7jMOhJ2YrhDtL62sGmMjVOUYphwGlftV8KwqtOiDzqpJNdLlyGaJhEP29XRnaaL00yuWXFbS1+6ptGGJ8jZmwpjbY7ZcBYVzNrtDYYrTH8bpyfCSxVLlwjxRh5hz9bWW2sKy8zKKHqyNypvCsZVp9D63ke9xinQnouTg326iKs9BUeEwcMbDHIIvNLPMYoaQQmhOJ3bnpmrZHgLCk/PgpwMrz3ddJgAK3tHGXi9wbMpcPYKm0lCoAx5kt/vkCL4bGCUU29eaka7KAPKMGyqrqpaWvO5T6Lr25CrhdQljHeBAVsLrDjJNq/tt6JA9UjIOZCNoieVymBO5dxbfVTzwbNxCtS8eGeXLION2lCdZSkjLnKyLxqKR3qtu7BixNI5ZU+UhQSNM/S7Qas5tVI3IkKwiNXwSw3a6+rIagDRYoFSnc14vsC9KFyuxYkO06GP+eUJ0xHt3oZ7W+Jx0SPLgu41VthBgN2h4/kOo1VhBxtBbdYpn1J1NTIOvtvtLMHBmS3X7JvTwTu2Bkcvr9sL5kXGBVkWWxJClMkj9hNduaXm4jByd3l6LBpLYdgxh9OVnGFoROAiqxLbQLi6HLTebi61QzGDeJzg8laXKnro1Qbtc4boRTKGxwa9+iK1xu8nQ2DabXDbXjVXd/b2khX3WEFGySoJCgurCz/VzrGbRkmtiWPmMbyc2bWwq/DD2uduyTquzQPb+vZ4KI9NaDGeH0rbvjjzm3pw94m0a4kI0g4cihySU5+JaN9Uo5Muz1TR9cSmtjtaaLbWEuYAPG/0NjBdihiVnkPYM8+lw7iboBhuD1BAAuGHy9Dhbpma9kVt1QvqGbsNrNFxuo9T5Y7SVKiIcUQw9xwp7NOG45baPl+TmWdY19FNxROz55YZjO7vmxHDQmlzTNAY6TP46qr2tesnKmRYOPaybRAXOCUsO3HXdHsKgRjjvKMJlJy8o9TVrRBsd80NRleXfH+WuEn00YLeIYOZBJVhI0d978CU4eUm3rhtEB6wxlYaa3k+qSekuRSNd5SvAps3Ry3KsxCSOZTyrkZ46DS1NoU1yynHrsdqLXa9HvKn1V4E6mwkgVeVZnWQpdyuTYcVRkm9mNZtuZaOmjuSDYsdbBghetLocwIQ3zT1adtt1yOGJ3SRxwwCgxxmsX3e3GpztWMOE1NUXHwGOznDtFK48jzzRpArzzO6bmPmbJC4frvZHOLRKC0Hr90o2h6vZ2efbE04O9/DXdISGG5IcdejRbqO98TNaKcyr4BKtoX0XV7Gl0MSGztYojYR4MmJx9R6uYkKokH3S0PRAUKveChn8/EYIBmEUPLKRnmPU9R+iVh31g/W8og22FITD/Z0TGicpW1HXRdMdcmJqLpjWKlWcUoYaI3qwuStbroNAsMtQR4OJRKoadMqTIgOXrxijYZfrYmq58W6huOqALt0eJ3uyfO0d3qzWx6Q9oYj3a4a2y0ALY046ytIzdeyrdwAPTlH4jCuLegWSS2RAZcjyXDBC0FC/TuJJtwJ8TITQVo/8/bQhrrfJDlBFD2A246NTna5jOHwQizPI4UEV8ndqteiQkQMKJpUcna37+2puW531t1ymKhf4bAxDV5CmGcSd/dkh5oU4pR2KIfBjTKzs3ZWW/sYL7PVijumoIM5ymGtbFnHODTNHgZ94E6nN9GW53yGMmBDjk/06tystSAairbHXMeYFIzE8lYRypNXWcvDdSVGzEnPPBbfiY5Cx6BROdiZ3Wug8wr6SuLztVXAUA+X2m152BwjTNxQalgOjQBpwYHxKglVdCy/I+vsmqpD4DQrjPIkBEIsTkuWfNb11FYeWcyrKXuLULslfoeW2ZVOK1zwWzmnIBfCUGwz8eiqO0PtpCdOi9obWK17sXdlJggNpzPjlWJiK8KW8GzYKI3ibFtaEeVqt5SC1Z2/lalSuYq6O0j6cYPbOAQXNsS3VnmbusnfEZmNSurkjWGQELDdhxySBcgZ9+6bHRt4djdR9imboDopsL6Fm6xPwjO33cSCegr46HokCIGiZSxm6GHP7ShRBwAlWdaePvANJThrV7n5VmpADRIjpJvTeIom5nl7vlKWrBLHWvVbbVnmUTMts51HbXj1tGnk/aZQ92U5Upv+ih6sgA8olSW4zEI6erw0lQqHk90tu8BCVtdtbDZJWZ74bb3VWk/SFW9551tovRND3ohrxENQbtgrWCrmesTKZ4/VB9B/pvyN30wOVDlHxz02JrNVJRCOmxEuB8H2V7Qg3w14U1c4Ns5nooeKqSlhLV/5uLN2XXJcnnnz4iMUlviKdxHS63VrWee8N7LryiwPIxUtW/yqJBtCRI6XvpyISzvQjE/IVw1PA+06FXsF32mYdQZ7Tqjujnh4KOVxucKmJXWY+ACJ+P6EHmGY3gbJKd0T9FY4WhNWbMpa1By5IsbrQUMvV9YECN2UF8Ud4KOontdBX5wmFI8R76h3yX1Itg7G0GIloxhGjEPcUBFMeoWXTcY1QgulgL0T3no7utkMLnVvDQ3qmars15iGNPfrJpKhZiJF0+Ir3zuInaJp/lUlcJ92BmydClUwNCblLUebu2yXhLI0b2FRHbJ9uF3iY87K2tUcMzrYWQbici4db41dDzVq5yl4Zl1zk2wJf9Wu7sGxg4JyYwbL+1bZEgFyjKKqz0Xpfhy207Kn1pd1IPIkRC1PJ39syVQ+rvqebJvVPSX7q0Q3AlYJuu+1K+MYyihx5hwDVequPao6FAe22nRrk7p7Ln2SCWxJr9rT3hJN4tRm5nYoJNoNqeXtgOHghXgYbNyFs03iNLO9Ssn6XHM3fpUcL2HB0zy6C/ab9LQMdGm4RrKgkHcq3rc2J/M7R76qeqZfi35kJJFLrLBiJTuaNJUgrtOZrWzCJ4wjh1881KjPmoaIdRldWDNiSsS6+UGZdohoeLpAIoWGDWMkjg0zKQa9KqQbhDRXe6LZXbiMeXUnif5EDszeMM39tgNAq9AnmpQUe9wdco3ObDHRoAi6HNIojdw+FSAhjSmLz72Buk4GqdPrxuisSWEgh99fQnFlBEekq2/30BpyT+vvvU9GZjOYeQfCR26ly3mFe7zbqyZi8DZEchf7SF4tRx7CGkdv99y/r7btKW+8eBCv9u7GpBKf7fHiiiF+TyNY3vn6uSZv1uEQ4dia6I2p2OhUPVaUMFSRuZL2nYt4VluZZS2jSX3n4bNvhOFdWLU+gUOgq2irneOTVbBqTaSGMouEKVwm6H289iB8P/k3pNtP+/tt0xyAqy4xS9m8YRzFgQwhqiWF26qFj1BE7MhMdhO/ZzFo23rBWajv1i4ifVDTqUfAjTqGZ9oTAxuivBzVS1kMVJK9EuEBv+SMkh9hibmDto9js2uSuCf8Cvov2/AGnkolWDHEepWt6nBJkyIEsnAP552tVZVxdLrggHoSFMKDgZNx3gU3YkNu1rdpgiV233HEDTZUhQ2hs7oZCdmLb/rOqXuEkqzgUOE3JYditvGVc8iDyibrQCTWkX5vXNF2CQ3i6mrX7pgr7WpnmKScE9q3y6QXKKK4+woJeJGgRfbskRSHDk7VkctM5VFxRcJiGZvyktoWO29quKtXO37NmcEKXtW+A+VXZsgG8S4cKmh1X3IXcoXkVrfy4iW1C+2WnnqU68n+XhRcKEB4w/c+uvPAHnRJU1HN75BEVLqrWss5TQw4S5A7yNCvOrY0hvXWuITMWki8paEdWXjkNGVjcjC3vOSoRvg8nZJVgbZnXb1g/o2E6xJDYtLW4YtdHclkaWaTrt3DzNeXuH0utXVLUjcEdrEoWg4RyYeiotooPd7JUhdD5BJupwY1t7WLQefBOW+8SRyVMV0N9Wl9lkJ470pNgoXC2LZ5BCmoMgr+ZlDlnR9VG1nRuAK7G3txI2ArepkVBE5tt8jO3JrufUTarAqhDY3sdK68X+bjk7/+9e3D2+/HdW//s0fO5mOb/2enR8+Dnq9PlTwOIUM3+PRY69P/UJ+/fXhr/RRo8zwb6/Ihfh0m/d3J2Md/eag4T52ez299PU1+HpX3bjw/zfyWlsHQ9e30pavyx9MkYIY3dPMzkN38mCyQ0f3x/PS52tvjdNoP6/5LXwFb2ks4X0vL+RmRMEjdPnx9jV+nhB/egtfTS19QAv8StvVs4uuBBGAZ+g6/o2+//V+7xsgDgi4AAA== -->
