---
name: "rar-cowork-cookbook-report-develop-product-catalogs"
description: "Builds a read-only product catalog summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_product_catalogs", "rar_sha256": "dc65f342ba2f95fb958ea5f9f718465b7d4be701462a31b8da70e6a9ba60326b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_develop_product_catalogs`. The original RAPP
agent is preserved byte-for-byte in `report_develop_product_catalogs_agent.py` and in the RCI capsule.

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

Develop product catalogs Summary Report — Builds a read-only product catalog summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-product-catalogs
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
      "description": "Name of the Excel workbook to produce, e.g. report-develop-product-catalogs-2026-05-24.xlsx.",
      "type": "string"
    },
    "posted_period": {
      "description": "Posted period to summarize; defaults to the most recent available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_develop_product_catalogs_agent.py` and embedded as the fenced Python below (sha256 dc65f342ba2f95fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_develop_product_catalogs_agent.py` first:

```bash
python3 report_develop_product_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_develop_product_catalogs_agent.py   # or on stdin
python3 report_develop_product_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop product catalogs Summary Report — Builds a read-only product catalog summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-develop-product-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_develop_product_catalogs',
    "version": '3.0.3',
    "display_name": 'Develop product catalogs Summary Report',
    "description": 'Builds a read-only product catalog summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-develop-product-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-develop-product-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ddac4e35961d3318',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/develop-product-catalogs'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-develop-product-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-develop-product-catalogs-2026-05-24.xlsx.', 'posted_period': 'Posted period to summarize; defaults to the most recent available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where develop product catalogs stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of develop product catalogs for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-develop-product-catalogs-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads develop product catalogs records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only product catalog summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a product catalog summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent available in the tenant.', 'name': 'posted_period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-develop-product-catalogs-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of product catalog activity from D365 ERP, with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportDevelopProductCatalogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportDevelopProductCatalogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-develop-product-catalogs-2026-05-24.xlsx.', 'type': 'string'}, 'posted_period': {'description': 'Posted period to summarize; defaults to the most recent available in the tenant.', 'type': 'string'}},
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
    print(ReportDevelopProductCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
