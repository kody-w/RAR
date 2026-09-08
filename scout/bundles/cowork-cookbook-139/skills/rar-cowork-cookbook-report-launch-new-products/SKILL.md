---
name: "rar-cowork-cookbook-report-launch-new-products"
description: "Builds a read-only summary report of launch-new-products activity from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_launch_new_products", "rar_sha256": "020188c088618926671586a243f938dac0e31838fbf2c42c6c0a0c34698beb38", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
