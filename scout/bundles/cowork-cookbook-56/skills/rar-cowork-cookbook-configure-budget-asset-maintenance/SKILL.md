---
name: "rar-cowork-cookbook-configure-budget-asset-maintenance"
description: "Applies bulk configuration changes to budget asset maintenance in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_budget_asset_maintenance", "rar_sha256": "0b33b3093a6637ea8d35eed50099654e973c409af1a5600e4ea48545684a9694", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_budget_asset_maintenance`. The original RAPP
agent is preserved byte-for-byte in `configure_budget_asset_maintenance_agent.py` and in the RCI capsule.

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

Budget asset maintenance Configuration Bulk Setup — Applies bulk configuration changes to budget asset maintenance in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-budget-asset-maintenance
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
      "description": "Explicit user approval after reviewing the validation workbook, required before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel workbook with one row per budget asset maintenance target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; run sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "Dynamics 365 legal entity to run against (e.g. USMF).",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_budget_asset_maintenance_agent.py` and embedded as the fenced Python below (sha256 0b33b3093a6637ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_budget_asset_maintenance_agent.py` first:

```bash
python3 configure_budget_asset_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_budget_asset_maintenance_agent.py   # or on stdin
python3 configure_budget_asset_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget asset maintenance Configuration Bulk Setup — Applies bulk configuration changes to budget asset maintenance in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-budget-asset-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_budget_asset_maintenance',
    "version": '3.0.3',
    "display_name": 'Budget asset maintenance Configuration Bulk Setup',
    "description": 'Applies bulk configuration changes to budget asset maintenance in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-budget-asset-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-budget-asset-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3adc2f2d1e55bf98',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/budget-asset-maintenance'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-budget-asset-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'configuration_excel_file': 'Attached Excel workbook with one row per budget asset maintenance target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'Dynamics 365 legal entity to run against (e.g. USMF).'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for budget asset maintenance, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per budget asset maintenance target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk configuration changes to budget asset maintenance in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a', 'example_request': 'Bulk update budget asset maintenance in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel workbook with one row per budget asset maintenance target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'Dynamics 365 legal entity to run against (e.g. USMF).', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when updating many budget asset maintenance records at once from a spreadsheet and you need row-level validation and an approval gate before any writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureBudgetAssetMaintenance(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureBudgetAssetMaintenance'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, required before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel workbook with one row per budget asset maintenance target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'Dynamics 365 legal entity to run against (e.g. USMF).', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureBudgetAssetMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
