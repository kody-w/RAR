---
name: "rar-cowork-cookbook-configure-measure-warehouse-performance"
description: "Reads an attached Excel file of warehouse performance target rows, validates each row, returns a validation workbook of pass/fail reasons, and after your approval applies the changes in D365 F&SCM (USMF) with a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_measure_warehouse_performance", "rar_sha256": "2f155c54e986a833bfee9d489bf47b93d5a0ef2fed0258df7c93520da9e7b14e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_measure_warehouse_performance`. The original RAPP
agent is preserved byte-for-byte in `configure_measure_warehouse_performance_agent.py` and in the RCI capsule.

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

Measure warehouse performance Configuration Bulk Setup — Reads an attached Excel file of warehouse performance target rows, validates each row, returns a validation workbook of pass/fail reasons, and after your approval applies the changes in D365 F&SCM (USMF) with a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-measure-warehouse-performance
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
    "approval": {
      "description": "Explicit confirmation after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "config_workbook": {
      "description": "Excel file with one row per warehouse performance target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; use sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (default USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_measure_warehouse_performance_agent.py` and embedded as the fenced Python below (sha256 2f155c54e986a833…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_measure_warehouse_performance_agent.py` first:

```bash
python3 configure_measure_warehouse_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_measure_warehouse_performance_agent.py   # or on stdin
python3 configure_measure_warehouse_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Measure warehouse performance Configuration Bulk Setup — Reads an attached Excel file of warehouse performance target rows, validates each row, returns a validation workbook of pass/fail reasons, and after your approval applies the changes in D365 F&SCM (USMF) with a before/af

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-measure-warehouse-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_measure_warehouse_performance',
    "version": '3.0.3',
    "display_name": 'Measure warehouse performance Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of warehouse performance target rows, validates each row, returns a validation workbook of pass/fail reasons, and after your approval applies the changes in D365 F&SCM (USMF) with a before/af',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-measure-warehouse-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-measure-warehouse-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7c0ffd73015343bb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/analyze-warehouse-operations/measure-warehouse-performance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-measure-warehouse-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'config_workbook': 'Excel file with one row per warehouse performance target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; use sandbox first before production.', 'legal_entity': 'D365 legal entity to run against (default USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for measure warehouse performance, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per measure warehouse performance target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of warehouse performance target rows, validates each row, returns a validation workbook of pass/fail reasons, and after your approval applies the changes in D365 F&SCM (USMF) with a before/af', 'example_request': 'Bulk-update our warehouse performance targets in USMF sandbox from this Excel file - validate first and show me before applying.', 'inputs': [{'description': 'Excel file with one row per warehouse performance target and the new field values.', 'name': 'config_workbook'}, {'description': 'D365 legal entity to run against (default USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; use sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when bulk-updating warehouse performance measure targets in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and explicit approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureMeasureWarehousePerformance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureMeasureWarehousePerformance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'config_workbook': {'description': 'Excel file with one row per warehouse performance target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; use sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (default USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureMeasureWarehousePerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
