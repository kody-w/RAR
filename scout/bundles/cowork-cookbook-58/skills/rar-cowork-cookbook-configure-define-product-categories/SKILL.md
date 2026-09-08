---
name: "rar-cowork-cookbook-configure-define-product-categories"
description: "Runs a bulk product-category configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_define_product_categories", "rar_sha256": "6c41fc5684cad2d4e7c50fb4be2f6f92c122a167a65539740e1666dfd0f54d3a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
