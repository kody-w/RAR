---
name: "rar-cowork-cookbook-report-reconcile-freight"
description: "Builds a read-only freight reconciliation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_reconcile_freight", "rar_sha256": "7e9e2d9822f204cd31b4fff85b06ee288befaec6b29dbe1eaea713dff7d31e07", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_reconcile_freight`. The original RAPP
agent is preserved byte-for-byte in `report_reconcile_freight_agent.py` and in the RCI capsule.

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

Reconcile freight Summary Report — Builds a read-only freight reconciliation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-reconcile-freight
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
      "description": "Dimensions for breakdowns, e.g. department, category, responsible owner.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
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
      "description": "Excel workbook filename, e.g. report-reconcile-freight-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_reconcile_freight_agent.py` and embedded as the fenced Python below (sha256 7e9e2d9822f204cd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_reconcile_freight_agent.py` first:

```bash
python3 report_reconcile_freight_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_reconcile_freight_agent.py   # or on stdin
python3 report_reconcile_freight_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile freight Summary Report — Builds a read-only freight reconciliation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-reconcile-freight
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_reconcile_freight',
    "version": '3.0.3',
    "display_name": 'Reconcile freight Summary Report',
    "description": 'Builds a read-only freight reconciliation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-reconcile-freight',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-reconcile-freight',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ced9a2fe84d08134',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/reconcile-freight'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/report-reconcile-freight', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Excel workbook filename, e.g. report-reconcile-freight-2026-05-24.xlsx.', 'period': 'Posted period to summarize; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where reconcile freight stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of reconcile freight for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-reconcile-freight-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads reconcile freight records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only freight reconciliation summary report from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a freight reconciliation summary for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook filename, e.g. report-reconcile-freight-2026-05-24.xlsx.', 'name': 'output_filename'}, {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'name': 'breakdown_dimensions'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a freight reconciliation summary with totals, by-dimension breakdowns, and top 10 by value from D365 ERP data, without modifying data.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportReconcileFreight(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportReconcileFreight'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns, e.g. department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook filename, e.g. report-reconcile-freight-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to summarize; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportReconcileFreight().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
