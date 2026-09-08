---
name: "rar-cowork-cookbook-report-manage-the-recurring-synchronization-of-data"
description: "Builds a read-only Excel summary report of recurring data synchronization activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_the_recurring_synchronization_of_data", "rar_sha256": "5ccf883eb549a1aca0e1f91fc1266ace8728061e037de6d7e73e626950f30299", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_the_recurring_synchronization_of_data`. The original RAPP
agent is preserved byte-for-byte in `report_manage_the_recurring_synchronization_of_data_agent.py` and in the RCI capsule.

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

Manage the recurring synchronization of data Summary Report — Builds a read-only Excel summary report of recurring data synchronization activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-the-recurring-synchronization-of-data
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
      "description": "Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on (e.g. USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-the-recurring-synchronization-of-data-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_the_recurring_synchronization_of_data_agent.py` and embedded as the fenced Python below (sha256 5ccf883eb549a1ac…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_the_recurring_synchronization_of_data_agent.py` first:

```bash
python3 report_manage_the_recurring_synchronization_of_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_the_recurring_synchronization_of_data_agent.py   # or on stdin
python3 report_manage_the_recurring_synchronization_of_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage the recurring synchronization of data Summary Report — Builds a read-only Excel summary report of recurring data synchronization activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-the-recurring-synchronization-of-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_the_recurring_synchronization_of_data',
    "version": '3.0.3',
    "display_name": 'Manage the recurring synchronization of data Summary Report',
    "description": "Builds a read-only Excel summary report of recurring data synchronization activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, with Summary, Detail, and Top10 sheets.",
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
        "upstream_slug": 'report-manage-the-recurring-synchronization-of-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-the-recurring-synchronization-of-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b4ac1f6946419a6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-data/manage-the-recurring-synchronization-of-data'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-manage-the-recurring-synchronization-of-data', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (e.g. USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-the-recurring-synchronization-of-data-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage the recurring synchronization of data stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage the recurring synchronization of data for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-the-recurring-synchronization-of-data-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage the recurring synchronization of data records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': "Builds a read-only Excel summary report of recurring data synchronization activity from Dynamics 365 F&SCM for a legal entity's most recent posted period, with Summary, Detail, and Top10 sheets.", 'example_request': "Build a recurring data sync summary report for USMF's latest posted period as an Excel workbook.", 'inputs': [{'description': 'D365 legal entity to report on (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-the-recurring-synchronization-of-data-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals/trends/breakdown report of recurring data synchronization activity from D365 ERP exported as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageTheRecurringSynchronizationOfData(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageTheRecurringSynchronizationOfData'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-the-recurring-synchronization-of-data-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageTheRecurringSynchronizationOfData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6adOjVpbmX9G8HTG2m8wXBEJAdlTEIITYtCA2IZwVafZV7Ks89d/nIikzbZerZ6q6v4xyEcu95571ec4V/Ppmd21U1G+f3lTfzhecnWVx5NcLO/cWTDEUdQq+itQB/xZukbd17HRtUTdvH948v3HruGzjIgfTN12cec3CXtS+7X0s8mxasKPrZ4umu93segLXy6JuF0UAjtyuruM8XHh2ay+aKXejusjjuz3LWthuG/dxOy2CurgttlNu32K3WWBrfLH7nypzWAQF0G+R+aGdLfy8BUN/aBa3omlnyeDCogTHvrco/TouvA+LIW6jhfpU48Ni67d2nH14WKgV5RJZNJHvt807MMkf7VuZ+c3bp5//+uEtBsdvn359czO7AZfelIcFBzu3Q1+LfOWrGervDTgFW2AWkJbZeQimlRPwcA7OgT5A9Ru45PnB4nX2Y+NnwYfFv/97Oth12Pz06XO+eH0+v81/lC5ftJG/aAv7YZVrl7YTZ8Dq9wWdDfbUALPbrs5n5zftrND7c+Z3SUW5+Mt878fnIu+h3/74+a0AKjw0/vz20wL49PNb3c3H77OU8sef3rNi8Osff/oup+mcxHfbWRjQ+v3L6/wlFgz8PjQOFl9UmWVea4HIxKUPhP/GvvnzVP0l7uWSL8/BPxblh8WfS57t+QvQ95mCDpD752KBD8DMt/ekiPMfX2vURe/ndu76P/70j8S6ke+mWdy0/09yf34KjkDeA2+9XPLTh0f4/rqAXrZ9k/mPly1BwvwzloDhX5f75qh/JPsR2T+IzuLcb77F8k/F/dkE6C+Ln/+hbf/ZhA+L4PPb1s/iHuSdk/mfFr8+UuTnH7zvF3/469+A6P+rGLXoavch4cvNzuPAb9ovX37+oXlc/uGvP//QlSCLffv2pauzP5P5Z359rPM7D75G/fj7uWB9PU/zYsgX32po8WtR/o/6b+8Lw85i7/v15tPit5U4f6DFbMTXRZ8u+E01NkDX3/jxp7e/ASjKgTWd+7gN8OPf/m1xiN26aIqgXahu0QHo6wAS3vxZeS2KmwX4O6NG7QO/NjFw7GscyP85wrPGAIp/+V/uA+Q/ui+Qh58wPTsVoNwXIOLLN7j+8gek/lIEX2YE/+V9AeAQIEgcxjnAZIWW5c/zdADFQI2y9hu/7gF0OVPrfwQV/nE+WMT54pd/YbUvD8Hv5fTLA8LjJzoqjDAjY9Nl/vvsg0vk5y+LXcBr/gjEgjWzwgUKBjHA+A/AN02R9QBZZ381aZxlCy8G6wN+mx6ygU8/zcJ++eUXx26iz/kTyrHFk/gaGAz4ps7i40dgaZDFYdR+zn03KhY//Pq3Hxb/e/GfzXoIn9eQAce8IgY0FNXTcQEqsLuBYSCYIPwAXh4R+/VvL38DMTlgahDfOIj952SQwanvfXW+ytMfUXy9cHzgdODw2+zsmXfj9n0hBItv+r7IeWaQaOZRzy/93PNzdwJSbWDON0/mRbtoQDyaAFBp1/iPVX9xavuh4g1Agd3+sjgwMuCrIgP/zWo+BoHJIJbA/d9S43kdCKkBf2++inhfHOecXZR2bZdRbb/WCOxnXGbuf00Hwu1F7g+f85mp/dlVj0x5ugcMAp5xXyH9OMccdDCgCci95uvajzH2zKrag13rz3nzKg67nkPhArIAi4Zd7M2U8R+vlGqiosu8h/+AprOkVxS8V1QeOfjsFF5B/dry/LHbASF9dEGv/mTxbDIWnzsUWa4W//93VbMjaI5TWI7W2O2CPWrK9RmguZ2c5T470IdqRf0sxu89zlcc+wrnn/MsBtlWT//xHPkI62vMEyK7Giip0MpDPsgpEKBZ7iPl5xQGPgLFYn/Ov/IGUHrxAEngJYAPoH7mtP264Hz3q6YRAIH5/HsP8UiR2pvNBmm9KDsnAykX+L7n2G4KtJrj9jWYIP/9OVJDFLvR76yaHQ6CCeQvgBIxKETALe/fsPx596vqv5v4bJXmKY82sgNVWz8EAD38WcE5IHOogHrts3sHdn56CAFm3Mp2tt0BOQIsfV70a7/q4iZuZ4x8+tUvAWR/nL+fls5X/bEEpQKcBQqi7IB3HyU0598NNEJAB4AioKJucQ4aA+CUlxMeAu3bjAcAb1+d61Pi4/LLIP9RdzOjfZ04GzLPmZuEZxLb+fRb2ND+LE2AvNs84rHuHzPt22qz7Bk6GwB/YMWvd5/dxPuzIXh2HIuvcj/93fbox39uB/WgeP33CfBpEbVt2XyC4Sctf2XldwBc8FPX5sXQH5+c+RHo+fFb6X/8Q9V/LIKPMxr8bqmnFz4t/jl1fyfiVS6fFst35B2Zb+1f6fb6AO8wHzfXj6v57udc8b8jLVi+uAHt5lhOoCX4RotfhwBuDGsAQ2DwkyabmV0HQOgPXgAGf85/m/9z/QHaycM5X5viN7jw6A9ALTzj+I2+wK28BWt7c88Z+vPG71Etjf/2Ke+y7MMbAEf/X9jwzZR1m5O+mbeNoLwAVrax/zhzgLqpB8r6iweSOm+endyvf9hFb7/deyTht0mzZR0ADQAQgJvtup3J7gOwqPXDYsZfMBi0MyWY+Oj1wBS//jA7DdCYXZbAvrluZlPbqZxte+4U597ygW5j+/fKnB4Hdvb+QvfmtyXzosC5BfhNZT/DAZR1ge0fZiYCgAV0A+GY3TKjgt2kD+P+VJcH/Xx50s+feGdmq98y1KO/eDEg6NL99/B9oauH3U9/Kvxbh/33ki+gbZmFecWnmcE/vLARfINdEfDz1w0OMOm15Xz8XJB3YDf/87y5mqP/mDIfgDng69ukb7+VOP7bX/9MrweAfplT9pl4f9TuOAMjII7Zw0/6n+v0UaJAZ7Cu17nA2w/z/wV0+Igi6Pojgn9EV+9j1ox/6rwn7f+9bvJvu4JZnWdnEt9Bs+T5gd1loADb4qH7P+wmFnYP8usfZChY/MFIgNdnZ3+P4ndfFo9d60PNzG6fP7L8+gZK0Z7texXja9sDhgMA/9jMjRwM8AssCM6fSAPu/XdsiF4im8gG3TeQibtuQJKY7+Aryl7aro34y4BaBu4SXa9t1ycJlETWSx/BCM9fe4RPYP4aXVM4EmAISlFA3hPCvswNbDyriVNEgFAUGqyWKOIBR6MrzyPX5NrFCRSxKcfGHZyyne9T0zj3XrY/bZ0d+21vNvvo5QKAVesVGMmvGoF+fhiYWjrrK+FMexOq134xDYyScfEoK3igCKt+7Nbo9iyPYbf2N8LpdBYDIc00bXfIovSyqpOzM7F8zsiHnLpXaawYor7HiUNWsPze2hklsvZwrd1n2l1eE6jRGEOZ2pAx7ZSzJd5OBik2K5TxRIeHInJcskWbSrpkqdjOdrbXCV0VWqZa1r4nqDsGibvV5XSOD6nVtEN+0BSjvpO8FAnc1kUb9Li5pn4QO7qZ6lwnQxkp4ZbVRDyPLqPO47asgUDQrqKgAKsRI5607all7VhPCl9wz3DLORtJY1GdZJkUqpZMKrVH8bSRzFMGmXsBZhu3ypLUYsaKXamUxG9XiiXhF0e1YQyWzTrF/T7HIUreXHsMR71g6yrWuOHTwxnXLWPXp6vJCocDzrWtwmy0zqMV2T1gaYYqt2hQUfkc9248YNmBcKU0Mc7EJmT2QjwMbp4M8DUQ1XEqkyapgnjr4gx7pJlu3zgXtcnIOr3uIlIv04jRDdEVeMs3hFZBqb3cBmp9yohbfAkM5p6E24ttMbu2uwb5qO7V0AirnYqnLs35Kndpxm0s7i554Vbo1rscYJELC9Y577gjjcPZnWOPqUW4a0jCsk47yNIp05Gzbu5TNYl1Tid5dSiuBaaf6bqaQOwpSQhZPBy3AQOrpmxTtMSFKmZHU6nJo2avd5OVWqdcbfw9YSUQGTllEVRuVTAHgcmnVtic76NYurWEJ+dJ5EeuMjnd4S8Nuc0TTGPHruBZS/Fp91SUxxqrq7ba08jOpgX3osU8ae/H4HzYdU2yD2LlbAOLuePR5lDjur1EoTOkN5SosmuMlNxpvxqv4jJuA65ThbDRLQZmJZPURe9indiiS6GBCXBpvwlWZrg8ZFeYteFTutywpI4isuDskkG92FwhZ60OHe6NS9yXh+mGrOh8cyN8kQ1BlnXFzagD/kZez6QVutkdh/ZJhnXH9KTaWL2mUlGjNQo9oVqzw8d0IPPtdJUPjNPfk7vbU5tDGiQ7Cjry0DEjELXdyeMxzbNwfTlvxzTeXQj+ykRAXoMd2809nii9oiklPGxxRrzZqtOxoS8sd6rKUV3NabfBqDkbFoApKokR9ja6QYZCNWKx1sxNTMb5oeEv1fmCcC3fMCsc7jIM7iCfsTu/Pov3QalRAcHY5eqGYNqBYKfxilIpNhzKnUegPcFVXOmv3b4eaxMnydNoQv3OgXpOK3V4vdY6W6tFlop7gar6ybejI9fcWnNN4AIk8gBfrJXXZ/2RghQmX1471Cn5M8xM5C4lO2Pw7/e+ILZ0baOUjqgHY48qawmW6DsT3VmI3sq0iZW3xjpAlk6wRUxtY+xakbDMaksBdbAquiIiswNcRC31mwpXUYq7sh+klQq393Fp0yTodEBJcXZ+qNqcLETB4GTKl44DzKKb88h47vHKaHIm7wxYyNHjmjwIhi7seI522b3cX2ABq9y9bSph7m3uZ4zM5UxRnFiAumhbRGMNZRjErkhWaUb1kvowLzpJpWNW2kl60oZsm8TVMhWxFqGFOjkEw+DTTCntJhU7bry0VA7uHTmU5MpA9X4DyxfPRiyDjRkASVah24SH2WSNHOpKcAiqD/jMIMymXJ9SXb8gLu2c9wNUWarsrMVYCU4QfUyJtYedxgISRAuplwWzDxGRYhk3GNNqSOjGI1Y3zuyKLriaDYmqngEvp6O8canzzhXvFpnB6dU5JYW6v6+0G60ctE1987JQYE8iJdhRKTrEllty6VVpAg4OcnbZZF2sStNFue0yhbal5raC7Yuyy86FU7ZHKZTK3L5Q15000CtcB6h/yI/Kzl6JtB4n3rTWUH50lbDsBiG8oDy2XinMZVpj2bXZwPo546oYNpcyzFSNySxtglaljmc2p2QsbwdjyU4XUYq9PbJHoZNZr4jASBmuv4qYnE5Vek4yHNJOx7zR/XBQCam3tQwCjt2IGWESEiOeOOWcjLZsBZsB8hU5ASkf9GEOuZqVWX1qKNvT4Q7nDsvS8iG+pDTv9qKk6FeV8OtcPyvsZo8GhLBZbjTLoKBuU4ntKvJJ39GsXZLsd0rAul2kezWXXTdQFNNybNHtwG2vhR+IxibN0f1xn00HElXcqGhxR512pXvcluR6e7luMbK74jaeHe4qtdV46pKgWmc5+HHyqGqw8QnOtBtAI+Pupeb5PBUckhjmKSyKG2h2zofi0ObIyWREGQD6lcsAjgo741qTsFTKJz2KxzM1ybGorY+tPkBEYoVLLyHPR3GrjZR+RLgVgley2k7nM7pcyVu8MCPEyly8MjJ4td7vKgU7KVKS+Gm14U+itdHLJI+zA36SaTxOxushYEqFN+jpqLPoxTUNhd5PZ7ix2QvrHB1B2/Vkt7yLOwxXTaHeavgmjC0VUni+prgS9LQxG150YUo2qCewsqLyKreTG3SvM158AYWgY6xNn1a0TNgH72JiuFaJ3ME9WFd1LMjzoIw5VYdjIImZhtZpWHDWsrsvtQzEI7gfOkWX07DW95B1IU87g6jQrGiaAb+rI96qo7rJTW8NG7R3sO6OtyyqVWtnsYxEiezuYK04aVgpKaFZNI4jMkNMqYRoTia9Kj0r6iVRMrIdwTgHqQqlpbFfyfWwEV2TNrqTrlzv7KbiDluuWnFIDyMWLSb6ljqbMGriV+1gb8mYXVqrCbCLhG8PkURUYbtcJq6pOqFnIrg17Fce2Fu3GqncV2eRZ3gxw8xlna5ZySlkqpDKRJdFWSYG8tQHjcvB0A7wJOcES8U8HMcjAlH3rFhuC9E866cUOZ+1URf0qmGhcgrd+pLdV85SaISU5lo9oRi9KXtGTODyoHj6Ujay6KZOypY1lycuzrmdbcnLMwNN97opd5tQ2x3L8X6YuF008VFkRbtNccj9FInvaXeKXWefDjAjhDaqpSsH6RPsmHn05Tye7tLdzrleMHhEKDdXVnSYJhZK85aQwxkNZb6WtaNvKptu5TQwBZhizVzTE0c0+2nJXQGnwwiVo02SyOdbsiGH+GLemoJOQ2o6CZXYrc21yRIULA7Kkj+4K0PiM+GcgvS+0+c8VktWEQRsL0l4t5vW7JSOnbNRrEE49+cstNwwbJzxbsE5v0wCz9jaMlkXNKVe5TbUQREIFMupGU8XR0VfX66VlOaRmlbCNOqc1fCy0KeD0o6nc9hSOFE7UXY0t1m9LpGi5N2dHQ3sIJWKFTYFuRFpLj5V3bTb72k0Gkr26Hlx2l22vq+mXZ1h7ApCFdjTa+dW5llkUHvaqpoSMAkCB31U2qlz6IKdYIXKTvHZ4LqhydS5jUm41zhFU4Sz0kbslb6L/XnHmjC5PnCJCB14c0UGsoWTSTPmVnNAaS5ZbuHLiWaWRTfu1zwZy7Sjq77VReN4Nbb5WY3kgdWNdmnufHFrdTtCya402iJbL4KqsobT1SBljVVzjH+4uOkZyeB6d4zR7HhGx/aqIPuQgvRbrVK9Lxr9FZO8JESGaFtleOQiO7SsMosRCmO76WL/zLbaXt3f1lJoQJreQtxp4q61ku0vgpVpvujkwZoJspFzuH005skRy5C6McLaXCVcC237QHBTibnAR/usCy1ASc2S6zrRMP6ckWWn2MhdSHLC6g0FbLEPJyMdVDyW1FMi4dyGDvTjCvQuKuLYRYTsiTXRctsIJvcaIOpwHQoS6Dh026dxCF2FDWvjRbrRi6uHMTwvweyJh4OzE8JNVF9xETHhPZvvQPOghzuQvKqzBbsDtpNCfkLRjRqQML0hqI64HkZzx/jaIWPzCsedA1s0we4oBkuHr3t9vJihN6HMSJfplfAtJtY3sV8btroyEEPCVGsX9YiTJiYxDJ40RNVJ5fNSgdusCVMYbUDrE4WrNJR937PFazZFttYFGluWegkn/qhIx2xzXgqVwWRGcSaG5U5U8Hy1UXDBoapUi4Kkd7z+5lYhG6wv3bWhvfjqb/fw5W4poMHj9JIg6eAqiehWjVmIqcXszpT7OFL15HhR0Gxb97VwtEc2s6rDmSYO++2tF3qUP1Xb8/4AWlOTQG4FhDlqDVduEMAqVrvRKZpSxEIqYVslsJEdSYdAu9O617w4EZhYG8NT5k9RTGWYmuGXcclEjW8s9TWB3UHDkEmSUvLbI2bvCX4Fr1vX8JyWWxIMpKxLpWm1U7/vcSjJpiUuuXcTNFkHenerqkRj7HyvrVywX9uWsMJ5BLbPzaV4irEwuk4E7iiqXVQl2ySn1ujLeD8NEcekMl4127YZhmt/llAH7Ki24TE/6rKrRAkHXMasT7SkOIEw3IHPbvl515ktTbDmBTCtbCd4JVzibomh/JH1BwVvs2teWuLpBpV4f584JLQJoohq34z9DVahtHaqLlHQHXZwk9yWtubQIk8ZKAU83VvKml8b8B5xiF6X26xqucP6SlLr5YVLjKBd4dUaDfY4iZok7BzGImtsdN+aZuNnhIf0pIBoDVNRlHYvGNmPZLNLAovXj+umaUFXvFk1aU4qAlM4x9rZDuSaqNYydpKrcg0VJyerMqogj0mE1AaNnve9CBfDypIER0wOa1mpWw1AY5HyubU78DeT7dmsMMYmyFUvLcwYa47hktoZJyxswcYTZkC+ld1mPRC5CwWTYEGUQZSdj2Ut3uun6lwc+GHIt5qKALhmmwsve/4Whm0KXpXUtZrCDCKsIBhl2G6TXiiTulpS7nQbMzvh6OYUMY6dknwedfuteE3uxyt0Y2QdjjSAzrQNm3FnXHdEeixppCXDjt2mm0E95okP9h5rjQ62Y6JS7faY+xPoQqi+QZdEfVVPBQD0CJed7CSR4/iAsGPPSTEpk77Y7SUKxKvIl5AWnjdHI4hgM++90vBOq5iG+5XFAxSqT+nhZIeUyFXkFMrD3dWIPgV9M+1sWwMlIXvV7aNkSYhx4RF6d1q23liYuA17UattNngqpCdhczsLeT6QXNujou3xBqmx6O6mo403FBUAvni6NlDjncBO+0iaVbQ0QUora+qCXhEXpdCjCamnC+kmdALdm5vmmsGo5SoCCRI0CZmrUQLSxljSDPD54MmFtytTJrwOdw2hXM3VDbypTjVh6UJZrAqw6y4HMWVK6kQDjwztjW8iBs4veuqizQpyeSs9pH1Po5ciadV7P7oyn4zro5gdCNpjiJXB+c2Un9EbfiR5vPW8Tc1VIp9Lg3rteN9r9ZsMrc+4obQWuup6Psf6E32P7rhQs9Stqksiux9GwwzxzV03D9OJOjn3LttdPMJE0+7chHy6ZJERiy4V5KzXVJlOHdfLa+o6XVguGCrNpLHznenQ3f7CITsswRJHX7p+6hMVtCMvSVwf91eCOh/v5q23r3xQGDpa5NfD8uKtRSv3Lhh+jofltrXEOlrvx2h9NPfb5NDT10QSiHol233LbSwaThJcbvmxYISJl63OtRRKd1DxDJvWzhjRSO2vNDISHuUeOQpylvVUyFJ3W/qQi2lx3/PX5tJbUQ5RsmPKHeLqzd2dnN4jtySXsp5rriRB7OG21HDJd+vEXJrt0mYJL2B5DyMGY6l0N36z0xrtWCPd1qBdKIc6kd5Dm2XEVMNGG+XEqWrTKY/YpdWha6aVl255NtuD5boeDksR6jnUEg3wEGyOfYgAu1eGvKdbUciUzFLwbRXJBjoyCD/YSVNitd5fWo70+z2DT7Rj7pbqfgX22gnoT88QwwV5DuiL48lQR+OSRNxsuzNvquBiFoeDzTmVGepgY7jI83QEJ41pWxbbxymCxf445f623cbDPSbrLtoHrCUTmnkwPY6CnfO9odGwyw/Ybi9I5wuNKtjGXBex120a0JFNAj61GFvA7N1NEPzWrsVWgKU6OUjblLDv3aRSJbTMhJPpXyK+22Z+s5Ogbk3YRine96epbdEsstbwQHlpWXLSeN+SrotaAW+1V9CI+dbK2dRXXwvN0itdHF9PpYdMxtjrRqPG674JeO+auFIhlqft+kK2FIrc+va2KfeethcIJBtuoRojsuruiMJlkiJaIe21OKNUVVpWzrjw/pTuDkRUkUmy7C3IcOok5Yi8w+nbRV6vlc5j3PtQG4Xv3qjAWDFHGD9PEtzaG0S5xZ6urh1MoC1oOFSh57cTBK9N7Hgv5MIidaTHDtKSxp1xcggOJfpMq2l5e8Mtx3cxOdKjlOyr+GKPZILVcSoHExGi+wDZYIQkSZ3kNdauWlmcLXFyRxIG3o8ZVmhOhq9ZqwluzN2ULxF+txrcG2Uyi9UxvNzCg3gbEcfsKOqu4HXdMBd8yQkyQO2tsA9cJaa1mlfEDWzdISsELb7SbXG4TdeYcx8snN8aAlT4olZtrGDA86w+LdH8uoGk061ox7jiG5M6y5fLzsRdxUTupG1g/b5pW7tZr+9u7lC7YLXcc45DkAbmWQVZQ/WZxfaYhezz8HyESObGEVOxw5xRcced7hnIsnRFP4et49Yz0Us6UMs7tEvvy3VmNggRdiTvB3tv6rBdSwxTfhP9PYbct2hnJPuIJ4YRRpFkg4liiZnd5cZgseneeglDEo3XDpDW0RpiCSxtMARZ3TyxDaX4xJRSIdx0E8waPGzf1ZV/9ATmno08b98CZs0cI1m9xLXdYe1ZLjfssjreRSLb+h7r9z7BORs58nqUIBp93bSbbcDLcnfUW6JS8JOUuOdTFiaej2cUfhSCQ8dsfTjVRWPcnpOCQXmol6muszoyCMxQJyk39E+rXqtdP94fqyzBME9ajTC77XDMvggrSeOSS29blIdHBExuan8gtHTD0jT9l7cPb98fC779V96Wmx8E/bc9j3o+Ovr6EszjEahve58ea336L2n51w9vtRsDHZ9P5pqsC18Prf7wXO7jv/CgcxY4PV9T+/rM+/m8v7XD+Z3vtzj3uqatpy9NkT1elAEznK6ZXwtt5jeHXfD92ye9Tx3Age0933Px6y9t8eX5iNJ/m9/bnF+B8b34+2n4enr54c17vYT1BVvjX/y6nI1/vVkBbMbekXfs7W//B3jUjKCiLwAA -->
