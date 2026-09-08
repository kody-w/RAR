---
name: "rar-cowork-cookbook-report-count-inventory"
description: "Builds a read-only count inventory summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_count_inventory", "rar_sha256": "96fa19d64a16f3e8a80640570dced7e8021323a62c307ea654872f839da3256d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_count_inventory`. The original RAPP
agent is preserved byte-for-byte in `report_count_inventory_agent.py` and in the RCI capsule.

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

Count inventory Summary Report — Builds a read-only count inventory summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-count-inventory
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-count-inventory-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_count_inventory_agent.py` and embedded as the fenced Python below (sha256 96fa19d64a16f3e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_count_inventory_agent.py` first:

```bash
python3 report_count_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_count_inventory_agent.py   # or on stdin
python3 report_count_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Count inventory Summary Report — Builds a read-only count inventory summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-count-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_count_inventory',
    "version": '3.0.3',
    "display_name": 'Count inventory Summary Report',
    "description": 'Builds a read-only count inventory summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-count-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-count-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd3e0f205eeefb8b0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/maintain-inventory-levels/count-inventory'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-count-inventory', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-count-inventory-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where count inventory stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of count inventory for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-count-inventory-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads count inventory records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only count inventory summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a count inventory summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-count-inventory-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a count inventory summary with totals, by-dimension breakdowns, and top-10-by-value as an Excel workbook from D365 ERP data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportCountInventory(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportCountInventory'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-count-inventory-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportCountInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916adObWJbmX9G8HTGZ2bJfFrHJHR0xLJJAYhNCIEhXONlBrGJH2fnf5yLJzqVcXV0R82lkZ2rh3rOf5znX8Oub07VxWb99ejsFTrHYOVmWxEG9cAp/wZZDWafgrUxd8N/CK4u2TtyuLevm7cObHzRenVRtUhZgO9Mlmd8snEUdOP7HssgmsL4r2kVS9EEBtkyLpstzB7zXQVXW7SKsy3zBTYWTJ16zWBH4Yvu/T6y0CEugfhElYNsiCyInW4D9STs9bKrKpg3AW1Anpf8BiGq7ukiKCFxcbEYvyBazzQ9zh6SNF6enzg8LLmidJPvwEKKX1QKBF+606J2sCxZNHARt8w58CkYnr7Kgefv0898+vCXg89unX9+8zGnAT2/aw3B2dkv46hXYlDlFBK5WE4hkAb4D44APOfjJD8LF69uPTZCFHxb//u/p4NRR89Onz8Xi9fr8Nv/RumLRxsGiLZ2Hi55TOW6SAcffF3Q2OFPz8nYOcgMSUUTvz52/SwJ+/ed87cenkvcoaH/8/FYCE5w5TZ/fflqA4H5+q7v58/sspfrxp/esHIL6x59+l9N07jXw2lkYsPr9y+v7SyxY+PvSJFx8Oakb9qWrDrykCoDwP/g3v56mv8S9QvLlufjHsvqw+L7k2Z//BPY+S80Fcr8vFsQA7Hx7v5ZJ8eNLR12CDDmFF/z40z8S68WBl2ZJ0/6P5P78FByD+gbReoXkpw+P9P1tsXz59k3mP1ZbgYL5VzwBy7+q+xaofyT7kdm/iM6SImi+5fK74r63Yfmfi5//oW//3YYPi/DzGxdkoINrx82CT4tfHyXy8w/+7z/+8LffgOh/KuZUdrX3kPAld4okDJr2y5eff2geP//wt59/6CpQxYGTf+nq7HsyvxfXh54/RfC16sc/7wX6z0ValEOx+NZDi1/L6n/Vv70vDCdL/N9/bz4t/tiJ82u5mJ34qvQZgj90YwNs/UMcf3r7DSBOAbzpvMdlgB//9m8LKfHqsinDdnECeNouQILbJA9m4/U4aRbg74wadQDi2iQgsK91oP7nDM8Wl+Hil//jPcD8o/cCc+gJwl8eGP3lG0b/8r7QgbSyTqKkAMir0ar6uXCiYAbyBggNmqDuATq5Uxt8BE38cf4AMH7xy/cFfnnsfa+mXx7ImzwxTmOFGd+aLgveZ0/MGGD9024PAHkwBl4HxGalB2wIEwDIM9Q3ZdYDfJy9btIkyxZ+AhDkQS2zbBCZT7OwX375xXWa+HPxBOTV4klTDQQWfDNn8fEjcCbMkihuPxeBF5eLH3797YfFfy3+u10P4bMOFRDCK+7Awv1JkRegj7ocLAMpAUkEIPGI+6+/vUIKxBSAV0GWkjAJnptBHaaB/zW+J57+iOLEwg1AXEFM8zmeM7Ul7ftCCBff7H0R6MwDMaDDhR9UQeEHhTcBqQ5w51ski7JdNKDYmhAwYNcED62/uLXzMDEHDe20vywkVgWsU2bgf7OZj0Vgc1kkIPzfsv/8HQipf2gWzFcR7wt5rrxF5dROFdfOS0foPPMyU/lrOxDuLIpg+FzMtBrMoXq0wTM8YBGIjPdK6cc552B+ANxd+M1X3Y81zsyN+oMj689F8ypxp55T4QHIB0qjLvFn4P+PV0k1cdll/iN+wNJZ0isL/isrjxpk/zKtvCaHxZP0F587FEawxf8HY87sLL3baZsdrW+4xUbWNeuZhHnAm5P1nAlnW2YjHw33+zTyFXG+Au/nIktARdXTfzxXPlL3WvMEs64Grmi09pAP6gYkYZb7KOu5TOt6bgjnc/EV4YH5iwecgcwCDAA9MpfmV4Xz1a+WxqDR5++/s/2jDGp/DgAo3UXVuRkoqzAIfNfxUmDVnLiv2QQ1HsxtOsSJF//JqzkZIIdA/gIYkYBmAyzw/g11n1e/mv6njc+hZt7yGPg60Jn1QwCwI5gNnFMzJw2Y1z7naeDnp4cQ4EZetbPvLugN4Onzx6AObl3SJO2Mg8+4BhVA3o/z+9PT+ddgrEA7gGCBoq86EN1Hm8xVk4ORBdgAkAJ0TZ4UgMJBUF5BeAh08rnnAaa+ZsynxMfPL4eCR2/N3PN14+zIvGem82eZO8X0R2jQv1cmQF4+r3jo/WulfdM2y57hsQEQBzR+vfrk/fcndT9ng8VXuZ/+7sDy4792pnmQ8fnPBfBpEbdt1XyCoCeBfuXPdwBO0NPW5sWlHx9A8PEbEPxJ2tPRT4t/zaI/iXh1xKcF8g6/w/Ml8VVRrxcIAPuRsT5i89XPhRb8DphAfZmDkprTNc2I8JXdvi4BFBfVAIXA4ifbNTNJDoCXH/AOYv+5+GOJzy0G2KOI5pJsyj+0/oPmQbk/U/WNhcClogW6/XkAjIL5sPVoiCZ4+1R0WfbhDSBk8I8PWTPB5HP5NvOJDDQKwMY2CR7fXGBV6oMG/eKD8iya5/T0619OqNy3a49y+rYJOBC8R+8zjTp1O/PSB2B1G0TlDKhg7KjAlsdkBRYDsgDGtFM1m/o8hc1z2wOPxvbvlSqPD072/kLm5o9F/iKmmZj/0IvP6IKoesDHDwsfmNLMRAqiO7s/97HTpA8nvmvLg0y+PMnkO1GYGehPfDOz/pOqyuIVivNJ2n5X9rfh9e8Fm2CWmGX55aeZVj+8wAy8gwMHiOjXswPw6HWaexy4iw4clH+ezy1zkh9b5g9gD3j7tunbPze4wdvfvmfXA/G+zAX4LKO/WifPSAaQfg7wXwgU2Az0+p0XvLz/fjt/RGGU+AjjH1Hsfcya8bvxeRL236tX/8jns8bnkJDcwZDiB6HTZaBj2vJhXj7PdKAIZn770xywcHpQQTPafkc3UP5gCcC1czx/T9Tv4SofZ76HmZnTPv+J4tc30FQOqDHn1VavQwNYDkD1YzMPUBAAHKAQfH9CA7j2PzxOvHY1sQMGW7BtTYQOsvYJzEGIcBVQDgUTGIyTsO8FPhlQMIqs0JVDoN4KJgOHwDGKRENqtfadFZDgA3lPWPkyz4bJbAm+JkN4vUZDDEFhH8QSxXyfIijCw0kUdtaug7v42nF/35omhf9y7+nOHLtvJ5s5DC8vAbAQGFjJY41AP18stEZcyCTdSbxAF5gabWt7cJKLM11sUsRPOSppaBQxMlImd1FzunLLpad9iWgXAbeZuyHJLE8wKnoKyL7Y5/GSvbiTbpPoALMndl/cqwHnSegumapKDVbh2On5mJxDe3tIl2fcy+S2jaTlSkr7+7G/1zxEne9wY2hIuREqn5E3qB6wIYskY2svjRxJKrVd7uFs0NytWY+Itlxuk/XSW/GTebuf+J1usq28EWWfETkm3OqNtt/zwjlDhFCKvcrfbCqhnHTkNI1pO66vu3PjxgpFtFmeEXsHMRr+4One6SYepbO+74Xu7p2uFsl7yXHNXDa3WEYEE40pqagRahm6De7KK5sIE1JCyXYNkViL7Kx4vac1e3NmHFdmfSWRjKQkj0I0jdatSgLMCJjBNHMWiyMFuxpSEx506k5n1i3bYQJjH5NlYy1X9zU2Lc90JuXBdOu57W04bChk3E+8MnDaAUnrkiaWB+4uGgfBtuBeEhvhhpolGSh3GI1k6EhOiCpIm5hl9XzraKSGRz52SfDr1roZmbyZ2ANEb5a51NpJmmh6dcrG3hDjihSCMy2jTBvR3K3heP940HpH9fNLoOCUBdeHYTppctrvb4JUZum9VZko0c0Tu0tv6fa4FTMni86ospMcjF+6W1evbIMuXXlDZWJBgSw7W2Ov1tyYydmqq3p9bxInnsql/Hg/GC07TZt0v84GhxA2vc3E/ChMe3vip3pTXnghWAbJ0XAdbhIstHWDjF63RqdZu6gY9qBOvSN0PS5NmONcf881oyp5h8jgTFRmwYmark+wjIF69TOz1Q7aNTPGqjnnY150NXwX1L157EfagLYWedP3U2qrEHYSYP3KYqmqSNlyK7nsHivbMjiiLhfByKQeQ4WsGruwMumc25jPW2dKcvU7xHE+H2e7tb0diVNGQqI+LblybKjcXnLakohPDeVBGwGCLJVyXBVpxKZfDktbrajlsuipUByMDs8KtorYgT4RvmsyTOWcwThOyZ5tnZdeKpnD5ebTaDrsthDTQc6dvwx0TW7K6TIeWzScKp7W97tmOu5XJr+f0CNptzJ9up/2B3jD3Po02osaxcIhvZIDjzsPphhf+G7cbKDt3aJRLMgGeq0OdiOK0TS50rXlUXGzkgKKycZ9H68pyz1PvgIKdXubWM0x2dJG8vjs3XtMxPpCVAXCvCty1PJyTqYu4ewtWBA9I6RVhyy09F6dkXV+2xHLszkgVbxWDG1vSPvUjzp/LMdqwFJLTBu5lH2CNiOROhcqJ9Vau74fTHqouxN68Bl+nyv3ncqGQlrt2JtbA6hOhr22tqMTFsHCRWqWvOfFRgIxdepsl4iiXS4qbjGjy2zLk97zDrEWNYnyjpLlFUq1vYv4Ue5cA3OOpxNDbCJxRbjFijOKFtbF4+F66nA5j/vRLQz9Oo2Xxr2NjhbFnkEuN0vv4FETtfVljKMxmxgU6oCL4qZ1OJ5C0H3d9z5ec6w/VCp7wNkdGa3kvZ9WsUOVBtGz7UDyfVTn16PkHIjrQEtQiDumR8pLmzo2xu68QQqes3jXX9WCO66FoaHwaLcqd+j6nClq1PgZ2jnIADG9oXaXZdZdFCozU8liuishCCSCNlfGuuhqQBxi41apRLwjJbmw7j4rM7V7ECxuqq3cFHuUAZ3oJUoYstOQaEWp47RjRVNMyw3A202DjIlDV+POhZX2Qq4mHTS5p0WuEGEDHLdVvt/L6CY97GPUImpnuk4ZTEzrmhZsnmOs8UayQyKiiELv+Z3fwkUjN2lyM2zao+smbOVTvstZ3jFKMPVvJHbPxGWAXE/U2NVZejVr2gSzBFrx+2El89Pq6vPZJvAKrUCWfiGiuMIrZczDpx0Pm4az1xgG0vcygh5UzbrEx/Ngb1wSWkaROa1kvS2xyLIN9WSoW2yt9rhzqjMH6qATaps+vj1jd06CtvnIROxKyPrBXYmDYCXwXvVBJD1hYrpa7jLaPcKoEZ5IGjlP1NE9SPK6mwYmWQsSXuOciFXOPt6eRpX2Wj3KTW4ZH+ltkR60Iy4PIhfIp9Xp5qlUYMJlbDucgGStsXGb/nJ0hFW3Xxu8GwRBY4iHJrYacUDS9bJNLuMJu66JcnuT6ktDcNaO5RGPFwTpzoRH+E6cmvPoBlq+2wh34uIK1PkoCVaakdj62vk5kS757K7TguJNmsryJXPc71qO20cBD7sVH+rN0d8z+rg2ZYoHY9CNnmTOOnpHJhyGg3hWuVI1yvMdMdZ3uIQ2t5Rhm7Wxjo2jJgCmx5JtcNuOHMhcjy1pKEui/rZPrJKp7piJ23SJHs3J2hyNWtEVjoOWrXxmGf0Qj7eaOdvKcK0c9Njy9Xq3A+eRRI/KdMVcCW9rnptToksXAaDuQcoOlcIL+3u1wyJVOGAAIWh0ZQc1srcGK1+yR7PZH612iv1VFYynMT1nNNyxl8xeXVw1k9Ettl2rhZkIFzEZUzc5bSf/WI9nWTe8bYUFikFJyV53VhG1obWdRyFrzd8XZg/wh3X1wg83hFq0Oz2ytFE4TpR+k6YshwAyXSSZq0Vvfcx1KS2tKwhPvlX3Wz+JvNERDCrMzZsZ9e3GZXbudOB2S5KHr5iLybS4Vy8IfCFv+53CLq1M3QXb0UN5z9rn+xBOmDUUWLfrxdWJSTIpCaSeQtEw3EroJjpG9lSbS6qFb20pB9XuZJvAazGBlHsKX1WuD1P9IKej24pLPC6FaqN2mzVb6lpts7GVJ07inTQ2NSIVJhypyaT7KevPSXk9bhxcd+FRv1xNVl8PocQYhjRMDA8KawDMWnVsVISRVd/RTgta++Idj3HkdPs7Mkk2RA/4YXNsqDimNqf+5GnEdCo0hW9JMRoTS+nTltnJ0NrahOuTh2109das7Di1jXGSLwIbadtrVkFpopY6gt235CWT8Vu3g1ioh5YyvRJFLSeurszv2zMWpOu+h1epc8QdtZGKC3/IDlxTLE90VU7s6oLWguaR6n3MmPBk+8x5fzi2rl4LJ5rZ5NnEJMexPctbHBGdExhEaN/dwKYpKbua3Tq7iuZEB27RYFuvsQIxBpwdTheotVAqOscct1luWMEwDaWRzpoPe9zewiV00plJJEU7WB+Du9tk4kW5u8IE3847OoaNs7pHWEhYw2ITJEIyxefNUuAHTGQdJdsxfS4EwSntAhRJMRQ9Frpxs87sSnSk6ro8rUM+HJelqYlCSx3tMr6zG9YdEhbbXTf6oZWY5Cyop4pzggIel2SFLVU+xKMgvCNriO8hixggKr3l3MHb3rsWUfwNPLokoSD7S7Rz6GxT69ZSDbuE1TZctCKKVAsFeph8hmJbV8nhgqkSa1W1h3Jq09OtujnEqkjw6SJxO6uKhuu0ciIJwMjhJuwOq9MG9hy1i3DxUrWbPbLE0cNQW7JojAO/LK80okmKagqOGLJVuiFSJD36Q0CnDVGuMV4epcEk+WuDx57m0kPeZ5DPlZdLmW8VTKo79NAOO54JJxteRYpJkSu3xDlSj9VkQxQ7pzbwwa7dW4pAgqKEqCIsHT5wSkVB/WpF8ygr7jenDr7F49mKNPF4WbtblfG0hkmsKKLEFQb1/FhCS6bJsMwyxt1WpMQtvY+ce9Bah3x3NA+bjYjzgqJ5XCkOrSUzSDrElqAhWN42eZYzO9ElzLOcbqt7tmz2u9LE764aDeIIBavzhStre7VPcf2UnSv/1hvXtg/3DNydxBS2I5WQK2Wf4GiOb+wBAACWkWVFwfcLgcQTgrlwm/Yiv+3P+w2BEoV6CMa60w5FFEAqt4LdXncwN6GPymVgqsC33enI0DDkBJl+Y84OFDEAx5haYu541Ahjbt92VUO7F53B6L3iK8MtumEhNZhEhet0jdNjnGTkxgfcdNWac6QLKN3eBI6h+7tr6htjx4+0Zd043ybMnT1udveLIF5M9zDMxtSUxqdcWFmetueMIUkKx3BvhB9yxNW0Vy19HrcG50Ox6ATRaR25rri3xOi6r3xV9MpGW6MD75JKoxxQ4YCOqAVvESX0lUusOcjNaN2yR2FPwZOAlSpse0O10A35Uq6TdSusyLDp7yrvNT2CF/I6WS3jUXJH+ExkblPg0WUzkf25JNK13o0EOBfDUHmSN2SW8hmNsUOpbG7LPZflIUvIiDYgMZWarq5RPozladM3lFSfJULdnSk7ux+dcpUigesXO1UmEu/IMaXkkWsal92MivzNOBjSiq21SjVbDwlEHO53Dn7MkV06uMftnQXnFPuw9Og0JC/ltqX5JIjRPOf1XcUWGSmzd9QeujarOLXCDuvCsh2b4ANDu6KULnlgfBpX3JHYKFjanATMcfGuON5NfWr6fIIK0s5lmOLNUb6R6+vUEUF8vFx9BUx7K0O56oN5PZj9MV9pu3NI3QAd+Roz9fMElNRxG6Nx2Hh9nzSuOmUTlgdkXCG2B0lnDgGNYqxXqzME1z4/shIcp76f3lFtupUOy/gGxFxd0vVkfEMd3CBEp7q0yK2+D9fe4Jh87tyOUJazQdUx6Iitmluw3thQaXRVs0TbFu/gwINLicdWa6YY7GBXJPAljnbUFVp2HkRt1429nzTG7kJovEAOOCYLWNuyyNpnoMxBYNY9K8aBvCUOz2eoeCivV0gGx+y9QkOR6/T80SHNk26P0Oka8lrpYNfl5poyk75e9QHK+mv7Jo8WXjm5nd+vZSXf8lXAZaW6Q7blgMDnboLEwILx603f5HzBnRV9LZ2L7dVMjRYWO2hvSczGbK4qmba+7wcmdgITAA6Onmy1Xpk7F4xu6fUU7M9X4koZGSQtCb/ZtV0aBL1sm8gAk0qmn4O8PNwz5zKZGSSKhOT3wznkxD1TMVLCbKmOi9s1gYl6c+8TK48aM0eK22ZrqNfrTt8WWVGheYWvYvO2C/yzpaSy0zajgPek5PQU17SYrdCF3btSjvVh4nXGnjrKfqMdsMIRBX0T8vt4qd+C+Gxn4kaJ7AHSz/Vp3R34JeLvz3iZhzeWPXmyQDSHC+uwaKRf0dIdUxIDA7U2HvjWF3b3/eTbYDYGqalOOrQ2+ZiCwu5O9n3GEiJyzmRVx85uvk4sjIQMItka8pBKCl77WC76chzmvYIfxUJBJBgjoPWe2Po7fbeGr/J0rmQf9xMxx9nDMhjwfJ9XXBAiGDp1EX+ezPq+UVxDZy7taI84ggy8bheerFgyQaaV4JHlEe3o3slZf6mY4IR7CMGEhFY3jEpJVMZUHGTHdMwRcuhL3ssODIekVFXVUaHsqqmHyz0kyu6UbeMb7wynmoPNCwcfuotquh0tXG87t14pRN/uGJuGuiuUHqrUYDb2dQhXyqa6GIfl6cQT8Nbe29jRRWlZDVYEx47XXs97/2yvTXh5NQtlGeAHIk9sDcqDiw9KU1HFqKzsDF/VpXwPcYLQ15OHI12MxxzMOn6tu8ilJa4bKAw40jfqo4HsutRXbKsPq8bLFChoDeGQhMccEuCJkQOmunXIFvcrwJBETST7XeaQxr06GvyFR3nWV51rsDJXQcstbY3MyEM1+HiG7TBBOU9NhUXIsa9J61ozza68iz6B8Eip9bswG32LtnuCsBnKgw8anm2hLabfT9T6KFgDlLI5jKi5vimtm0dopoin7iUIzAB8rMAgvDmGbIGao9+GcYOK+uV0IFc3DeuGUFwd2En1bTiXhvBuXBo70MGoWjLwdqILISPpZINsTiy5gxgQh2NwVdCdcFcPl8SJKUV1+3turawOvXpR7w3gzNTWJtmKzQaFe2YqSKSMhxCr4oqP7yYZtLIie6usqmDK9upQWY3sLbNczlRP493eUkGOZNezjKRjpyxje8cFKzS/X4obY1DO/qKsNRSphJycJmg1isfbNU8HpaqXyEoM7KVi8WmLg8Pk9VRMAX2oz9SevvTd8aSmRc0hNMK6u67IEmKLL0++4PiotEV4vu6mtbMyb5eOLDqcyQ2VmKbwhlDQcEPKwMupEJPUXU+AU5nS3yIpkhqjTFZW6lF0eo3WN2ZUV+RllUGVKx2WZTN1GY7R0+1yPSnyvXbrE3lW0A4P3O68hhEPzTz+ekNv+Lrg/eLcOQJp8QfVMlZhrljLm9hUSIzZN00wb+VEbJFWK6AbF8Z4Q4ioeqerbb8qlTNSExKlqzSZNkezKnnWluwdQgLHU9YlSKnoZCPm+IoeWHZFssKR9S1yL4hEHoY+XTKcPLhqh+q1X8jdvcx2O5vyqCA7JgQ03nnO9Os2OHLLsy9rLrc1VayV6bWNGWFWbUM9HLNLQPT3JVzf63oLQR1sQNeokcGhZLgE0C6eekKmda8/hccuYOgVPxwsvz+UF7/JjCE1NOSim+2Uos56IhSsPzpTAl1UzNTVy80I7kbHkaBNqH51ID0T7cBUYBnYFcpLB7l7fiP0rrtauSeJ73ZmqAfawaodP2T0uoFSMFAZq8kbNoF1jY7MWeynGyj1nL4J2CG9Rf2A9Y6rR4N38S8m5RCnbcElSoBIyx28c1kzbbcaTKlsFJ5YsYbd/LI67KjbRun7O+9qYryGCBxqbKxZM1y44uTOt1rS0TDlUPhHJbte1wGeedtQCOkrew+W6Zk5j/djXE43Pu63/UVl70soDyMY47zIkTDIPI/rjekaUpZY9mUXohYORhBJUi1f3urnYiwL/ggtOVRtlyx9OEY0/fbh7febb2//5Fmw+V7M/7NbQs+7N18f/3jcSwwc/9ND16d/ZsjfPrzVXgLMeN7iarIuet0a+ssNro/fvyk475mej1J9vQP8vJndOtH8EPFbUvhd0wKVTZk9HvQAO9yumR9AbOZnVD3w/scbn081b/OTgF+Nbcsvr+cmHz/PT3AEfuK0wetr9LrR9+HNfz1l9GVF4F+Cuprdez01ALxavcPvq7ff/i/lLiug8y0AAA== -->
