---
name: "rar-cowork-cookbook-report-take-inventory-on-software-licenses"
description: "Builds a read-only software license inventory summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_take_inventory_on_software_licenses", "rar_sha256": "2fb912e1d582a2da5433fb79406cb6c82d3ec21708f9b2996a9c81064ec441b3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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
