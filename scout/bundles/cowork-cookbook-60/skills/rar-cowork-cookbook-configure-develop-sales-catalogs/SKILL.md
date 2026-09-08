---
name: "rar-cowork-cookbook-configure-develop-sales-catalogs"
description: "Reads an attached Excel file of sales catalog configuration changes, validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmation workbook."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_develop_sales_catalogs", "rar_sha256": "d18c637372b8ef560f24d8d2e9c64af5b8c6d03a9cc66807e0200ca398c91136", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_develop_sales_catalogs`. The original RAPP
agent is preserved byte-for-byte in `configure_develop_sales_catalogs_agent.py` and in the RCI capsule.

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

Develop sales catalogs Configuration Bulk Setup — Reads an attached Excel file of sales catalog configuration changes, validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-sales-catalogs
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
      "description": "Explicit confirmation after reviewing the validation workbook, before changes are applied.",
      "type": "string"
    },
    "configuration_excel_file": {
      "description": "Attached Excel file with one row per sales catalog target and the new field values.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_develop_sales_catalogs_agent.py` and embedded as the fenced Python below (sha256 d18c637372b8ef56…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_develop_sales_catalogs_agent.py` first:

```bash
python3 configure_develop_sales_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_develop_sales_catalogs_agent.py   # or on stdin
python3 configure_develop_sales_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop sales catalogs Configuration Bulk Setup — Reads an attached Excel file of sales catalog configuration changes, validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmation workbook.

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-develop-sales-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_develop_sales_catalogs',
    "version": '3.0.3',
    "display_name": 'Develop sales catalogs Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of sales catalog configuration changes, validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmation workbook.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-develop-sales-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-develop-sales-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9d04d691948bdb0f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/develop-sales-catalogs'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/configure-develop-sales-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per sales catalog target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; run sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for develop sales catalogs, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per develop sales catalogs target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of sales catalog configuration changes, validates every row, returns a validation workbook, waits for your approval, then applies changes and returns a before/after confirmation workbook.', 'example_request': 'Bulk-update our sales catalog config in USMF sandbox from this Excel file — validate first and show me the results.', 'inputs': [{'description': 'Attached Excel file with one row per sales catalog target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; run sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update sales catalog configuration in Dynamics 365 F&SCM from a spreadsheet, with pre-apply validation and an approval step.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureDevelopSalesCatalogs(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureDevelopSalesCatalogs'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit confirmation after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per sales catalog target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; run sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureDevelopSalesCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
