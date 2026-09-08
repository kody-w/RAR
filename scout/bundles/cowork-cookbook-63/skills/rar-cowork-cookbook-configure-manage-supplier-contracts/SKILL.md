---
name: "rar-cowork-cookbook-configure-manage-supplier-contracts"
description: "Reads an attached configuration Excel file of supplier-contract changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, then applies approved changes with a before/after confirmation wo"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_supplier_contracts", "rar_sha256": "2c65b31ea93675e5252c1b303a9f85ee34c26731801015f7ad0db1920e780deb", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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
