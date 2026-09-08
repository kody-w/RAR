---
name: "rar-cowork-cookbook-report-take-inventory-on-software-licenses"
description: "Builds a read-only software license inventory summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_take_inventory_on_software_licenses", "rar_sha256": "2fb912e1d582a2da5433fb79406cb6c82d3ec21708f9b2996a9c81064ec441b3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_take_inventory_on_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `report_take_inventory_on_software_licenses_agent.py` and in the RCI capsule.

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

Take inventory on software licenses Summary Report — Builds a read-only software license inventory summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-take-inventory-on-software-licenses
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
      "description": "Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-take-inventory-on-software-licenses-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to report on; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_take_inventory_on_software_licenses_agent.py` and embedded as the fenced Python below (sha256 2fb912e1d582a2da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_take_inventory_on_software_licenses_agent.py` first:

```bash
python3 report_take_inventory_on_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_take_inventory_on_software_licenses_agent.py   # or on stdin
python3 report_take_inventory_on_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Take inventory on software licenses Summary Report — Builds a read-only software license inventory summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-take-inventory-on-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_take_inventory_on_software_licenses',
    "version": '3.0.3',
    "display_name": 'Take inventory on software licenses Summary Report',
    "description": 'Builds a read-only software license inventory summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-take-inventory-on-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-take-inventory-on-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '29025788f311f40f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/take-inventory-on-software-licenses'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/report-take-inventory-on-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-take-inventory-on-software-licenses-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where take inventory on software licenses stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of take inventory on software licenses for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-take-inventory-on-software-licenses-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads take inventory on software licenses records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only software license inventory summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a software license inventory summary report for USMF from D365 as an Excel workbook with a Top 10 by value sheet.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-take-inventory-on-software-licenses-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of software license inventory from D365 ERP, with totals, by-dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportTakeInventoryOnSoftwareLicenses(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportTakeInventoryOnSoftwareLicenses'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-take-inventory-on-software-licenses-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportTakeInventoryOnSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
