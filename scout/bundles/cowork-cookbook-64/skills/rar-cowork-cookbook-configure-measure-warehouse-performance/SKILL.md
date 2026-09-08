---
name: "rar-cowork-cookbook-configure-measure-warehouse-performance"
description: "Reads an attached Excel file of warehouse performance target rows, validates each row, returns a validation workbook of pass/fail reasons, and after your approval applies the changes in D365 F&SCM (USMF) with a before/af"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_measure_warehouse_performance", "rar_sha256": "2f155c54e986a833bfee9d489bf47b93d5a0ef2fed0258df7c93520da9e7b14e", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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
