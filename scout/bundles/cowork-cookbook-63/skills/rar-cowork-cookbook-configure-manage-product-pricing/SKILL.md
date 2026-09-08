---
name: "rar-cowork-cookbook-configure-manage-product-pricing"
description: "Applies bulk product pricing changes in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirm"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_manage_product_pricing", "rar_sha256": "21ffd23aa76cf55dffe79888c8e9e3be229e2d16e516e844fa459955bf6437e7", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
