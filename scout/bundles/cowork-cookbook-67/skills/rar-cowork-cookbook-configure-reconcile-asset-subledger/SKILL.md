---
name: "rar-cowork-cookbook-configure-reconcile-asset-subledger"
description: "Bulk-applies asset subledger reconciliation configuration changes in Dynamics 365 F&SCM from an attached Excel file, validating every row first and pausing for your approval before any write."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reconcile_asset_subledger", "rar_sha256": "e74b9a60aaa7c16cf85e5757bd708568c5cc8bc66c20e862c7421f9fc70b745d", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
