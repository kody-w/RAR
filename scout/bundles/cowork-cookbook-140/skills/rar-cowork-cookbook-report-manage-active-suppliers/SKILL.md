---
name: "rar-cowork-cookbook-report-manage-active-suppliers"
description: "Builds a read-only summary report of active suppliers from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_active_suppliers", "rar_sha256": "299456277f6c2905cd29652e7aaa24bfb24d0176e9ea13112c281d78510200a5", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_active_suppliers`. The original RAPP
agent is preserved byte-for-byte in `report_manage_active_suppliers_agent.py` and in the RCI capsule.

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

Manage active suppliers Summary Report — Builds a read-only summary report of active suppliers from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-active-suppliers
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
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report against; defaults to USMF.",
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
      "description": "Excel workbook name, e.g. report-manage-active-suppliers-2026-05-24.xlsx.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_active_suppliers_agent.py` and embedded as the fenced Python below (sha256 299456277f6c2905…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_active_suppliers_agent.py` first:

```bash
python3 report_manage_active_suppliers_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_active_suppliers_agent.py   # or on stdin
python3 report_manage_active_suppliers_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage active suppliers Summary Report — Builds a read-only summary report of active suppliers from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top 10 by value sheets.

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
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-active-suppliers
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_active_suppliers',
    "version": '3.0.3',
    "display_name": 'Manage active suppliers Summary Report',
    "description": 'Builds a read-only summary report of active suppliers from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top 10 by value sheets.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-active-suppliers',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-active-suppliers',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '942971431efb5871',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-active-suppliers'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/report-manage-active-suppliers', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report against; defaults to USMF.', 'output_filename': 'Excel workbook name, e.g. report-manage-active-suppliers-2026-05-24.xlsx.', 'period': 'Posted period to report on; defaults to the most recent posted period available.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Gives leadership a fast, repeatable view of where manage active suppliers stands so decisions are made on facts rather than spreadsheet stitches.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, build a summary report of manage active suppliers for the most recent posted period available in the tenant (USMF demo data is mostly FY2017). Include totals, by-dimension breakdowns (by department / category / responsible owner where applicable), and a 'Top 10 by value' section. Output an Excel workbook 'report-manage-active-suppliers-2026-05-24.xlsx' with Summary, Detail, and Top10 sheets. Do not modify any data.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads manage active suppliers records, computes summary statistics and groupings, and emits an Excel report.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Builds a read-only summary report of active suppliers from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top 10 by value sheets.', 'example_request': 'Build the active suppliers summary report from D365 USMF for the latest posted period as an Excel workbook.', 'inputs': [{'description': 'D365 legal entity to report against; defaults to USMF.', 'name': 'legal_entity'}, {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'name': 'period'}, {'description': 'Excel workbook name, e.g. report-manage-active-suppliers-2026-05-24.xlsx.', 'name': 'output_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a no-write supplier activity summary from D365 ERP with totals, dimension breakdowns, and a Top 10 by value list delivered as an Excel workbook.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ReportManageActiveSuppliers(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageActiveSuppliers'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report against; defaults to USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'output_filename': {'description': 'Excel workbook name, e.g. report-manage-active-suppliers-2026-05-24.xlsx.', 'type': 'string'}, 'period': {'description': 'Posted period to report on; defaults to the most recent posted period available.', 'type': 'string'}},
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
    print(ReportManageActiveSuppliers().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
