---
name: "rar-cowork-cookbook-configure-reconcile-asset-subledger"
description: "Bulk-applies asset subledger reconciliation configuration changes in Dynamics 365 F&SCM from an attached Excel file, validating every row first and pausing for your approval before any write."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reconcile_asset_subledger", "rar_sha256": "e74b9a60aaa7c16cf85e5757bd708568c5cc8bc66c20e862c7421f9fc70b745d", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_reconcile_asset_subledger`. The original RAPP
agent is preserved byte-for-byte in `configure_reconcile_asset_subledger_agent.py` and in the RCI capsule.

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

Reconcile asset subledger Configuration Bulk Setup — Bulk-applies asset subledger reconciliation configuration changes in Dynamics 365 F&SCM from an attached Excel file, validating every row first and pausing for your approval before any write.

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-asset-subledger
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per reconcile asset subledger target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reconcile_asset_subledger_agent.py` and embedded as the fenced Python below (sha256 e74b9a60aaa7c16c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reconcile_asset_subledger_agent.py` first:

```bash
python3 configure_reconcile_asset_subledger_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reconcile_asset_subledger_agent.py   # or on stdin
python3 configure_reconcile_asset_subledger_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile asset subledger Configuration Bulk Setup — Bulk-applies asset subledger reconciliation configuration changes in Dynamics 365 F&SCM from an attached Excel file, validating every row first and pausing for your approval before any write.

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-asset-subledger
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reconcile_asset_subledger',
    "version": '3.0.3',
    "display_name": 'Reconcile asset subledger Configuration Bulk Setup',
    "description": 'Bulk-applies asset subledger reconciliation configuration changes in Dynamics 365 F&SCM from an attached Excel file, validating every row first and pausing for your approval before any write.',
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
        "upstream_slug": 'configure-reconcile-asset-subledger',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reconcile-asset-subledger',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3162bf7e4bc5dd92',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/reconcile-asset-subledger'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-reconcile-asset-subledger', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per reconcile asset subledger target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for reconcile asset subledger, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per reconcile asset subledger target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Bulk-applies asset subledger reconciliation configuration changes in Dynamics 365 F&SCM from an attached Excel file, validating every row first and pausing for your approval before any write.', 'example_request': 'Run the asset subledger reconciliation bulk config on USMF sandbox using my attached Excel file — validate first.', 'inputs': [{'description': 'Attached Excel file with one row per reconcile asset subledger target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to reconcile asset subledger settings across many records at once from a config spreadsheet, with a validation pass and approval gate before applying.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureReconcileAssetSubledger(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReconcileAssetSubledger'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per reconcile asset subledger target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureReconcileAssetSubledger().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
