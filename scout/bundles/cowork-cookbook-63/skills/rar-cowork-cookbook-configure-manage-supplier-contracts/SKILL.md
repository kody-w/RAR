---
name: "rar-cowork-cookbook-configure-manage-supplier-contracts"
description: "Reads an attached configuration Excel file of supplier-contract changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation wo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_supplier_contracts", "rar_sha256": "2c65b31ea93675e5252c1b303a9f85ee34c26731801015f7ad0db1920e780deb", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_supplier_contracts`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_supplier_contracts_agent.py` and in the RCI capsule.

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

Manage supplier contracts Configuration Bulk Setup — Reads an attached configuration Excel file of supplier-contract changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation wo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-supplier-contracts
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
      "description": "Explicit user approval after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_file": {
      "description": "Excel file with one row per supplier contract target and its new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_supplier_contracts_agent.py` and embedded as the fenced Python below (sha256 2c65b31ea93675e5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_supplier_contracts_agent.py` first:

```bash
python3 configure_manage_supplier_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_supplier_contracts_agent.py   # or on stdin
python3 configure_manage_supplier_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage supplier contracts Configuration Bulk Setup — Reads an attached configuration Excel file of supplier-contract changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation wo

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-supplier-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_supplier_contracts',
    "version": '3.0.3',
    "display_name": 'Manage supplier contracts Configuration Bulk Setup',
    "description": 'Reads an attached configuration Excel file of supplier-contract changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation wo',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-supplier-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-supplier-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7b3d4d180f2fd179',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/manage-supplier-relationships/manage-supplier-contracts'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/configure-manage-supplier-contracts', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'configuration_file': 'Excel file with one row per supplier contract target and its new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage supplier contracts, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage supplier contracts target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached configuration Excel file of supplier-contract changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation wo', 'example_request': 'Bulk-update supplier contracts in USMF sandbox from my attached Excel file — validate first and show me the preview.', 'inputs': [{'description': 'Excel file with one row per supplier contract target and its new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update supplier contract fields in Dynamics 365 F&SCM from a spreadsheet, with row validation and an approval step before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageSupplierContracts(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageSupplierContracts'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit user approval after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per supplier contract target and its new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageSupplierContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
