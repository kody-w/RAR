---
name: "rar-cowork-cookbook-configure-reconcile-freight"
description: "Reads an attached Excel file of freight reconciliation configuration rows in Dynamics 365 F&SCM, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_reconcile_freight", "rar_sha256": "1329d772496eefc6670998b4f9ab09b4491aec1df2da989b1c1499387af37f21", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_reconcile_freight`. The original RAPP
agent is preserved byte-for-byte in `configure_reconcile_freight_agent.py` and in the RCI capsule.

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

Reconcile freight Configuration Bulk Setup — Reads an attached Excel file of freight reconciliation configuration rows in Dynamics 365 F&SCM, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-freight
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
      "description": "Explicit user approval after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel": {
      "description": "Attached Excel file with one row per reconcile freight target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; sandbox first before production.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_reconcile_freight_agent.py` and embedded as the fenced Python below (sha256 1329d772496eefc6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_reconcile_freight_agent.py` first:

```bash
python3 configure_reconcile_freight_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_reconcile_freight_agent.py   # or on stdin
python3 configure_reconcile_freight_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Reconcile freight Configuration Bulk Setup — Reads an attached Excel file of freight reconciliation configuration rows in Dynamics 365 F&SCM, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-reconcile-freight
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_reconcile_freight',
    "version": '3.0.3',
    "display_name": 'Reconcile freight Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of freight reconciliation configuration rows in Dynamics 365 F&SCM, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after confirm',
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
        "upstream_slug": 'configure-reconcile-freight',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-reconcile-freight',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4b6b90436d45dd99',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-freight-and-transportation/reconcile-freight'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/configure-reconcile-freight', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'configuration_excel': 'Attached Excel file with one row per reconcile freight target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for reconcile freight, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per reconcile freight target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of freight reconciliation configuration rows in Dynamics 365 F&SCM, validates every row, emits a validation workbook, waits for approval, then applies changes and emits a before/after confirm', 'example_request': 'Bulk-apply the freight reconciliation config in this Excel to USMF sandbox — validate first and show me the dry run.', 'inputs': [{'description': 'Attached Excel file with one row per reconcile freight target and the new field values.', 'name': 'configuration_excel'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants to bulk-apply freight reconciliation configuration changes in D365 from a spreadsheet, with dry-run validation and explicit approval before writes.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureReconcileFreight(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureReconcileFreight'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel': {'description': 'Attached Excel file with one row per reconcile freight target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureReconcileFreight().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
