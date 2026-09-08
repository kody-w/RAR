---
name: "rar-cowork-cookbook-report-manage-active-suppliers"
description: "Builds a read-only summary report of active suppliers from Dynamics 365 F&SCM (legal entity USMF) for the most recent posted period, and outputs an Excel workbook with Summary, Detail, and Top 10 by value sheets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_active_suppliers", "rar_sha256": "299456277f6c2905cd29652e7aaa24bfb24d0176e9ea13112c281d78510200a5", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
