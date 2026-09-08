---
name: "rar-cowork-cookbook-report-manage-product-pricing"
description: "Builds a read-only product pricing summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_product_pricing", "rar_sha256": "1517df6c56461c18b1b27a1b2f658388f4e79e6be2c8d8e8dcef8869ed8c405f", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_product_pricing`. The original RAPP
agent is preserved byte-for-byte in `report_manage_product_pricing_agent.py` and in the RCI capsule.

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

Manage product pricing Summary Report — Builds a read-only product pricing summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-product-pricing
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
      "description": "D365 legal entity to report on (default USMF).",
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
      "description": "Excel workbook filename, e.g. report-manage-product-pricing-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_product_pricing_agent.py` and embedded as the fenced Python below (sha256 1517df6c56461c18…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_product_pricing_agent.py` first:

```bash
python3 report_manage_product_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_product_pricing_agent.py   # or on stdin
python3 report_manage_product_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage product pricing Summary Report — Builds a read-only product pricing summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-product-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_product_pricing',
    "version": '3.0.3',
    "display_name": 'Manage product pricing Summary Report',
    "description": 'Builds a read-only product pricing summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-product-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-product-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'aa446f868c12f37c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-product-pricing'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-manage-product-pricing', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on (default USMF).', 'output_filename': 'Excel workbook filename, e.g. report-manage-product-pricing-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage product pricing stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage product pricing for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-product-pricing-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage product pricing records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only product pricing summary report from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a product pricing summary report for USMF from the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on (default USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook filename, e.g. report-manage-product-pricing-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-change summary of manage product pricing activity in D365 ERP with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageProductPricing(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageProductPricing'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-manage-product-pricing-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageProductPricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
