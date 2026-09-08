---
name: "rar-cowork-cookbook-report-develop-product-catalogs"
description: "Builds a read-only product catalog summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_develop_product_catalogs", "rar_sha256": "dc65f342ba2f95fb958ea5f9f718465b7d4be701462a31b8da70e6a9ba60326b", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
