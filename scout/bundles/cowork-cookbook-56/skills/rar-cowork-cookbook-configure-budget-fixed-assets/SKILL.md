---
name: "rar-cowork-cookbook-configure-budget-fixed-assets"
description: "Reads an attached Excel file of budget fixed asset configuration changes for a D365 F&SCM legal entity, validates every row, returns a validation workbook, and after your approval applies the changes with a before/after"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_budget_fixed_assets", "rar_sha256": "e10739e63d7a2089dcc1a3d76a6fae5b1fc40fb23799e9b9f751991386732124", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
