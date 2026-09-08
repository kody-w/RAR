---
name: "rar-cowork-cookbook-configure-budget-asset-maintenance"
description: "Applies bulk configuration changes to budget asset maintenance in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for approval, then applies changes and returns a"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_budget_asset_maintenance", "rar_sha256": "0b33b3093a6637ea8d35eed50099654e973c409af1a5600e4ea48545684a9694", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
