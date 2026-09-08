---
name: "rar-cowork-cookbook-configure-manage-product-pricing"
description: "Applies bulk product pricing changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_product_pricing", "rar_sha256": "21ffd23aa76cf55dffe79888c8e9e3be229e2d16e516e844fa459955bf6437e7", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_manage_product_pricing`. The original RAPP
agent is preserved byte-for-byte in `configure_manage_product_pricing_agent.py` and in the RCI capsule.

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

Manage product pricing Configuration Bulk Setup — Applies bulk product pricing changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-product-pricing
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
      "description": "Attached Excel file with one row per product pricing target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_manage_product_pricing_agent.py` and embedded as the fenced Python below (sha256 21ffd23aa76cf55d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_manage_product_pricing_agent.py` first:

```bash
python3 configure_manage_product_pricing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_manage_product_pricing_agent.py   # or on stdin
python3 configure_manage_product_pricing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage product pricing Configuration Bulk Setup — Applies bulk product pricing changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirm

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-manage-product-pricing
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_manage_product_pricing',
    "version": '3.0.3',
    "display_name": 'Manage product pricing Configuration Bulk Setup',
    "description": 'Applies bulk product pricing changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirm',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-manage-product-pricing',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-manage-product-pricing',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ea87a33149bf9dd1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/manage-product-pricing'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-manage-product-pricing', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per product pricing target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for manage product pricing, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per manage product pricing target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk product pricing changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirm', 'example_request': 'Bulk-update product pricing in USMF sandbox from this Excel file — validate first and show me the dry run before applying.', 'inputs': [{'description': 'Attached Excel file with one row per product pricing target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you have an Excel file of product pricing updates to apply in bulk to D365 F&SCM and want row-level validation and an approval step before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureManageProductPricing(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureManageProductPricing'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per product pricing target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureManageProductPricing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
