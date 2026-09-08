---
name: "rar-cowork-cookbook-report-research-new-products"
description: "Builds a read-only summary report of research new products activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_research_new_products", "rar_sha256": "f294b31d3b6df0c7ca81185949c3aa9f258a906b91cfaa2ba6a96f02d3701593", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_research_new_products`. The original RAPP
agent is preserved byte-for-byte in `report_research_new_products_agent.py` and in the RCI capsule.

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

Research new products Summary Report — Builds a read-only summary report of research new products activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-research-new-products
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
      "description": "D365 legal entity to query, e.g. USMF.",
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
      "description": "Excel workbook filename, e.g. report-research-new-products-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_research_new_products_agent.py` and embedded as the fenced Python below (sha256 f294b31d3b6df0c7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_research_new_products_agent.py` first:

```bash
python3 report_research_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_research_new_products_agent.py   # or on stdin
python3 report_research_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Research new products Summary Report — Builds a read-only summary report of research new products activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-research-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_research_new_products',
    "version": '3.0.3',
    "display_name": 'Research new products Summary Report',
    "description": 'Builds a read-only summary report of research new products activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
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
        "upstream_slug": 'report-research-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-research-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '312803d0211d0829',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/research-new-products'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-research-new-products', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to query, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-research-new-products-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where research new products stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of research new products for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-research-new-products-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads research new products records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of research new products activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build a research new products summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to query, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook filename, e.g. report-research-new-products-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary report of research new products activity from D365 ERP, with totals, dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportResearchNewProducts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportResearchNewProducts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to query, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-research-new-products-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportResearchNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
