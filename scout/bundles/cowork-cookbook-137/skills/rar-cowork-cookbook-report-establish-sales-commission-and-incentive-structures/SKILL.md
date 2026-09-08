---
name: "rar-cowork-cookbook-report-establish-sales-commission-and-incentive-structures"
description: "Builds a read-only Excel summary report of sales commission and incentive structures from Dynamics 365 F&SCM for a legal entity and posted period, with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_establish_sales_commission_and_incentive_structures", "rar_sha256": "cba94aa8731366fd684d232c6f35c6afbcb7c77073feb16d0d833bf3c977745d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
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
