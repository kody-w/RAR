---
name: "rar-cowork-cookbook-configure-budget-fixed-assets"
description: "Reads an attached Excel file of budget fixed asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_budget_fixed_assets", "rar_sha256": "e10739e63d7a2089dcc1a3d76a6fae5b1fc40fb23799e9b9f751991386732124", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_budget_fixed_assets`. The original RAPP
agent is preserved byte-for-byte in `configure_budget_fixed_assets_agent.py` and in the RCI capsule.

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

Budget fixed assets Configuration Bulk Setup — Reads an attached Excel file of budget fixed asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-budget-fixed-assets
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
    "configuration_file": {
      "description": "Excel file with one row per budget fixed asset target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against, e.g. USMF; use a sandbox first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_budget_fixed_assets_agent.py` and embedded as the fenced Python below (sha256 e10739e63d7a2089…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_budget_fixed_assets_agent.py` first:

```bash
python3 configure_budget_fixed_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_budget_fixed_assets_agent.py   # or on stdin
python3 configure_budget_fixed_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Budget fixed assets Configuration Bulk Setup — Reads an attached Excel file of budget fixed asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-budget-fixed-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_budget_fixed_assets',
    "version": '3.0.3',
    "display_name": 'Budget fixed assets Configuration Bulk Setup',
    "description": 'Reads an attached Excel file of budget fixed asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after',
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
        "upstream_slug": 'configure-budget-fixed-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-budget-fixed-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b44729ef76dbce81',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/budget-fixed-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-budget-fixed-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_file': 'Excel file with one row per budget fixed asset target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for budget fixed assets, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per budget fixed assets target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Reads an attached Excel file of budget fixed asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after', 'example_request': 'Bulk-update budget fixed assets in USMF sandbox from this Excel file — validate first and show me the dry run.', 'inputs': [{'description': 'Excel file with one row per budget fixed asset target and the new field values.', 'name': 'configuration_file'}, {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to bulk-update budget fixed asset configuration in Dynamics 365 F&SCM from a spreadsheet, with dry-run validation and approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureBudgetFixedAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureBudgetFixedAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_file': {'description': 'Excel file with one row per budget fixed asset target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF; use a sandbox first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureBudgetFixedAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
