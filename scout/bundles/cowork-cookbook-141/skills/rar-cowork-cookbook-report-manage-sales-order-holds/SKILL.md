---
name: "rar-cowork-cookbook-report-manage-sales-order-holds"
description: "Builds a read-only summary report of sales order holds from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_sales_order_holds", "rar_sha256": "6a574ddccc8529ecf1b25ee0118b3d903595bb69bcdcae4216879c4b5fe40742", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
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
