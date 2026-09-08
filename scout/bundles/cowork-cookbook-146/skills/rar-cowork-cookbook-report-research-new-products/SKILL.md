---
name: "rar-cowork-cookbook-report-research-new-products"
description: "Builds a read-only summary report of research new products activity from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_research_new_products", "rar_sha256": "f294b31d3b6df0c7ca81185949c3aa9f258a906b91cfaa2ba6a96f02d3701593", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
