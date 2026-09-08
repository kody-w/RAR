---
name: "rar-cowork-cookbook-report-establish-sales-commission-and-incentive-structures"
description: "Builds a read-only Excel summary report of sales commission and incentive structures from Dynamics 365 F&SCM for a legal entity and posted period, with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_establish_sales_commission_and_incentive_structures", "rar_sha256": "cba94aa8731366fd684d232c6f35c6afbcb7c77073feb16d0d833bf3c977745d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_establish_sales_commission_and_incentive_structures`. The original RAPP
agent is preserved byte-for-byte in `report_establish_sales_commission_and_incentive_structures_agent.py` and in the RCI capsule.

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

Establish sales commission and incentive structures Summary Report — Builds a read-only Excel summary report of sales commission and incentive structures from Dynamics 365 F&SCM for a legal entity and posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-establish-sales-commission-and-incentive-structures
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
      "description": "Dimensions for breakdowns where applicable: department, category, responsible owner.",
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
      "description": "Name of the Excel workbook to produce, e.g. report-establish-sales-commission-and-incentive-structures-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_establish_sales_commission_and_incentive_structures_agent.py` and embedded as the fenced Python below (sha256 cba94aa8731366fd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_establish_sales_commission_and_incentive_structures_agent.py` first:

```bash
python3 report_establish_sales_commission_and_incentive_structures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_establish_sales_commission_and_incentive_structures_agent.py   # or on stdin
python3 report_establish_sales_commission_and_incentive_structures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish sales commission and incentive structures Summary Report — Builds a read-only Excel summary report of sales commission and incentive structures from Dynamics 365 F&SCM for a legal entity and posted period, with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-establish-sales-commission-and-incentive-structures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_establish_sales_commission_and_incentive_structures',
    "version": '3.0.3',
    "display_name": 'Establish sales commission and incentive structures Summary Report',
    "description": 'Builds a read-only Excel summary report of sales commission and incentive structures from Dynamics 365 F&SCM for a legal entity and posted period, with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-establish-sales-commission-and-incentive-structures',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-establish-sales-commission-and-incentive-structures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bf1774e84dd2387f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/define-sales-strategy-and-policies/establish-sales-commission-and-incentive-structures'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/report-establish-sales-commission-and-incentive-structures', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against, e.g. USMF.', 'output_filename': 'Name of the Excel workbook to produce, e.g. report-establish-sales-commission-and-incentive-structures-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where establish sales commission and incentive structures stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of establish sales commission and incentive structures for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-establish-sales-commission-and-incentive-structures-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads establish sales commission and incentive structures records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only Excel summary report of sales commission and incentive structures from Dynamics 365 F&SCM for a legal entity and posted period, with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a commission and incentive structure summary report for USMF from the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Name of the Excel workbook to produce, e.g. report-establish-sales-commission-and-incentive-structures-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write D365 ERP summary report of commission/incentive structures with totals, by-dimension breakdowns, and a Top 10 by value list.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportEstablishSalesCommissionAndIncentiveStructures(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportEstablishSalesCommissionAndIncentiveStructures'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Name of the Excel workbook to produce, e.g. report-establish-sales-commission-and-incentive-structures-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportEstablishSalesCommissionAndIncentiveStructures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
