---
name: "rar-cowork-cookbook-report-plan-product-transitions"
description: "Builds a read-only summary report of plan product transitions from Dynamics 365 F&SCM for a given legal entity and posted period, delivered as an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_plan_product_transitions", "rar_sha256": "9083cbd1c79f7b24f997874fb5ffd77220d0706ede28ece89f8c185d417582ea", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
