---
name: "rar-cowork-cookbook-report-launch-new-products"
description: "Builds a read-only summary report of launch-new-products activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_launch_new_products", "rar_sha256": "020188c088618926671586a243f938dac0e31838fbf2c42c6c0a0c34698beb38", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_launch_new_products`. The original RAPP
agent is preserved byte-for-byte in `report_launch_new_products_agent.py` and in the RCI capsule.

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

Launch new products Summary Report — Builds a read-only summary report of launch-new-products activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-launch-new-products
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
      "description": "Dynamics 365 legal entity to report against (default USMF).",
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
      "description": "Name of the Excel workbook to produce, e.g. report-launch-new-products-2026-05-24.xlsx.",
      "type": "string"
    },
    "period": {
      "description": "Posted period to cover; defaults to the most recent posted period available in the tenant.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_launch_new_products_agent.py` and embedded as the fenced Python below (sha256 020188c088618926…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_launch_new_products_agent.py` first:

```bash
python3 report_launch_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_launch_new_products_agent.py   # or on stdin
python3 report_launch_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Launch new products Summary Report — Builds a read-only summary report of launch-new-products activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-launch-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_launch_new_products',
    "version": '3.0.3',
    "display_name": 'Launch new products Summary Report',
    "description": 'Builds a read-only summary report of launch-new-products activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-launch-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-launch-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd409a24742b9daf7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/launch-new-products'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-launch-new-products', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'Dynamics 365 legal entity to report against (default USMF).', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-launch-new-products-2026-05-24.xlsx.', 'period': 'Posted period to cover; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where launch new products stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of launch new products for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-launch-new-products-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads launch new products records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of launch-new-products activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build the launch new products summary report for USMF from D365 and give me the Excel workbook.', 'inputs': [{'description': 'Dynamics 365 legal entity to report against (default USMF).', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-launch-new-products-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary of launch new products activity with totals, by-dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportLaunchNewProducts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportLaunchNewProducts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to report against (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-launch-new-products-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportLaunchNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
