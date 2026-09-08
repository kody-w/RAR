---
name: "rar-cowork-cookbook-configure-define-product-categories"
description: "Runs a bulk product-category configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_product_categories", "rar_sha256": "6c41fc5684cad2d4e7c50fb4be2f6f92c122a167a65539740e1666dfd0f54d3a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_define_product_categories`. The original RAPP
agent is preserved byte-for-byte in `configure_define_product_categories_agent.py` and in the RCI capsule.

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

Define product categories Configuration Bulk Setup — Runs a bulk product-category configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-product-categories
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
      "description": "Explicit go-ahead after reviewing the validation workbook, before any changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per product-category target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_define_product_categories_agent.py` and embedded as the fenced Python below (sha256 6c41fc5684cad2d4…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_define_product_categories_agent.py` first:

```bash
python3 configure_define_product_categories_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_define_product_categories_agent.py   # or on stdin
python3 configure_define_product_categories_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define product categories Configuration Bulk Setup — Runs a bulk product-category configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-define-product-categories
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_define_product_categories',
    "version": '3.0.3',
    "display_name": 'Define product categories Configuration Bulk Setup',
    "description": 'Runs a bulk product-category configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/',
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
        "upstream_slug": 'configure-define-product-categories',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-define-product-categories',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8e88ebcacbc0249e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/develop-product-strategy/define-product-categories'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/configure-define-product-categories', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per product-category target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for define product categories, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per define product categories target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk product-category configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/', 'example_request': 'Bulk-define product categories in USMF sandbox from my attached Excel — validate first and let me approve before applying.', 'inputs': [{'description': 'Attached Excel file with one row per product-category target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-define product categories in D365 F&SCM from a spreadsheet and want row-level validation, an approval gate, and before/after evidence.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDefineProductCategories(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDefineProductCategories'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per product-category target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDefineProductCategories().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
