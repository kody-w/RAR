---
name: "rar-cowork-cookbook-report-process-change-orders"
description: "Builds a read-only summary report of process change orders from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_change_orders", "rar_sha256": "d8340136e57e8e9c35eaaefc73369935e5303abeea73758c33d959c1700f4c44", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_process_change_orders`. The original RAPP
agent is preserved byte-for-byte in `report_process_change_orders_agent.py` and in the RCI capsule.

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

Process change orders Summary Report — Builds a read-only summary report of process change orders from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-process-change-orders
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
      "description": "Excel workbook name, e.g. report-process-change-orders-2026-05-24.xlsx, saved to Documents/Cowork/output/.",
      "type": "string"
    },
    "posted_period": {
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_process_change_orders_agent.py` and embedded as the fenced Python below (sha256 d8340136e57e8e9c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_process_change_orders_agent.py` first:

```bash
python3 report_process_change_orders_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_process_change_orders_agent.py   # or on stdin
python3 report_process_change_orders_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Process change orders Summary Report — Builds a read-only summary report of process change orders from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-process-change-orders
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_process_change_orders',
    "version": '3.0.3',
    "display_name": 'Process change orders Summary Report',
    "description": 'Builds a read-only summary report of process change orders from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.',
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
        "upstream_slug": 'report-process-change-orders',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-process-change-orders',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c136130026decda',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/process-change-orders'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/report-process-change-orders', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'breakdown_dimensions': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'output_filename': 'Excel workbook name, e.g. report-process-change-orders-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'posted_period': 'Posted period to cover; defaults to the most recent posted period available in the tenant.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where process change orders stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of process change orders for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-process-change-orders-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads process change orders records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of process change orders from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets.', 'example_request': 'Build a process change orders summary report for USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'name': 'posted_period'}, {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'name': 'breakdown_dimensions'}, {'description': 'Excel workbook name, e.g. report-process-change-orders-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write summary of process change order activity with totals, by-dimension breakdowns, and a Top 10 by value list from D365 ERP.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportProcessChangeOrders(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportProcessChangeOrders'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'breakdown_dimensions': {'description': 'Dimensions for breakdowns where applicable: department, category, responsible owner.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-process-change-orders-2026-05-24.xlsx, saved to Documents/Cowork/output/.', 'type': 'string'}, 'posted_period': {'description': 'Posted period to cover; defaults to the most recent posted period available in the tenant.', 'type': 'string'}},
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
    print(ReportProcessChangeOrders().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
