---
name: "rar-cowork-cookbook-report-process-change-orders"
description: "Builds a read-only summary report of process change orders from Dynamics 365 F&SCM for a given legal entity and posted period, returning an Excel workbook with Summary, Detail, and Top10 sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_process_change_orders", "rar_sha256": "d8340136e57e8e9c35eaaefc73369935e5303abeea73758c33d959c1700f4c44", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
