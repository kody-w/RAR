---
name: "rar-cowork-cookbook-report-manage-sales-order-holds"
description: "Builds a read-only summary report of sales order holds from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_sales_order_holds", "rar_sha256": "6a574ddccc8529ecf1b25ee0118b3d903595bb69bcdcae4216879c4b5fe40742", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_sales_order_holds`. The original RAPP
agent is preserved byte-for-byte in `report_manage_sales_order_holds_agent.py` and in the RCI capsule.

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

Manage sales order holds Summary Report — Builds a read-only summary report of sales order holds from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-sales-order-holds
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-manage-sales-order-holds-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_sales_order_holds_agent.py` and embedded as the fenced Python below (sha256 6a574ddccc8529ec…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_sales_order_holds_agent.py` first:

```bash
python3 report_manage_sales_order_holds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_sales_order_holds_agent.py   # or on stdin
python3 report_manage_sales_order_holds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales order holds Summary Report — Builds a read-only summary report of sales order holds from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-sales-order-holds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_sales_order_holds',
    "version": '3.0.3',
    "display_name": 'Manage sales order holds Summary Report',
    "description": 'Builds a read-only summary report of sales order holds from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-sales-order-holds',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-sales-order-holds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9c8ba4d6834011f2',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-sales-orders/manage-sales-order-holds'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-manage-sales-order-holds', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-manage-sales-order-holds-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage sales order holds stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage sales order holds for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-sales-order-holds-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage sales order holds records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of sales order holds from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a sales order holds summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-manage-sales-order-holds-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of sales order holds activity with totals, dimension breakdowns, and top-10-by-value, delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageSalesOrderHolds(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageSalesOrderHolds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-manage-sales-order-holds-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageSalesOrderHolds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
