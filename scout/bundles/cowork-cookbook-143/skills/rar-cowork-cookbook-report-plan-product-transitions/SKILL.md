---
name: "rar-cowork-cookbook-report-plan-product-transitions"
description: "Builds a read-only summary report of plan product transitions from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_product_transitions", "rar_sha256": "9083cbd1c79f7b24f997874fb5ffd77220d0706ede28ece89f8c185d417582ea", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_plan_product_transitions`. The original RAPP
agent is preserved byte-for-byte in `report_plan_product_transitions_agent.py` and in the RCI capsule.

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

Plan product transitions Summary Report — Builds a read-only summary report of plan product transitions from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-product-transitions
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
      "description": "Name of the Excel workbook to produce, e.g. report-plan-product-transitions-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_plan_product_transitions_agent.py` and embedded as the fenced Python below (sha256 9083cbd1c79f7b24…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_plan_product_transitions_agent.py` first:

```bash
python3 report_plan_product_transitions_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_plan_product_transitions_agent.py   # or on stdin
python3 report_plan_product_transitions_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan product transitions Summary Report — Builds a read-only summary report of plan product transitions from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-plan-product-transitions
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_plan_product_transitions',
    "version": '3.0.3',
    "display_name": 'Plan product transitions Summary Report',
    "description": 'Builds a read-only summary report of plan product transitions from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-plan-product-transitions',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-plan-product-transitions',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'fc2dac3a0c88a44b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/retire-products/plan-product-transitions'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-plan-product-transitions', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-plan-product-transitions-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where plan product transitions stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of plan product transitions for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-plan-product-transitions-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads plan product transitions records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of plan product transitions from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a plan product transitions summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'name': 'breakdown_dimensions'}, {'description': 'Name of the Excel workbook to produce, e.g. report-plan-product-transitions-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a totals, breakdown, and Top 10 by value report of plan product transitions activity from D365 ERP, without changing any data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportPlanProductTransitions(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportPlanProductTransitions'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, such as department, category, or responsible owner, where applicable.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-plan-product-transitions-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportPlanProductTransitions().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
