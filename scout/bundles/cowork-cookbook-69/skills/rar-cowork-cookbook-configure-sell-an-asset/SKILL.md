---
name: "rar-cowork-cookbook-configure-sell-an-asset"
description: "Runs a bulk sell-an-asset configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a before/after confir"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_sell_an_asset", "rar_sha256": "13aa440f13bfdf2277ac06cf906c429bf65b33407970802050fa552304f79591", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_sell_an_asset`. The original RAPP
agent is preserved byte-for-byte in `configure_sell_an_asset_agent.py` and in the RCI capsule.

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

Sell an asset Configuration Bulk Setup — Runs a bulk sell-an-asset configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a before/after confir

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-sell-an-asset
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
      "description": "Attached Excel file with one row per sell-an-asset target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "environment": {
      "description": "Target environment; use sandbox first before production.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_sell_an_asset_agent.py` and embedded as the fenced Python below (sha256 13aa440f13bfdf22…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_sell_an_asset_agent.py` first:

```bash
python3 configure_sell_an_asset_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_sell_an_asset_agent.py   # or on stdin
python3 configure_sell_an_asset_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Sell an asset Configuration Bulk Setup — Runs a bulk sell-an-asset configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a before/after confir

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-sell-an-asset
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_sell_an_asset',
    "version": '3.0.3',
    "display_name": 'Sell an asset Configuration Bulk Setup',
    "description": 'Runs a bulk sell-an-asset configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a before/after confir',
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
        "upstream_slug": 'configure-sell-an-asset',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-sell-an-asset',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9fdaf1a459604a75',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/sell-an-asset'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-sell-an-asset', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per sell-an-asset target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'environment': 'Target environment; use sandbox first before production.', 'legal_entity': 'D365 legal entity to run against, e.g. USMF.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for sell an asset, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per sell an asset target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Runs a bulk sell-an-asset configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a before/after confir', 'example_request': 'Bulk-update sell-an-asset config in USMF sandbox from this Excel — validate first and wait for my approval.', 'inputs': [{'description': 'Attached Excel file with one row per sell-an-asset target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Target environment; use sandbox first before production.', 'name': 'environment'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when you need to apply bulk sell-an-asset field updates in D365 F&SCM from a spreadsheet, with dry-run validation and explicit approval before any write.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigureSellAnAsset(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureSellAnAsset'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per sell-an-asset target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'environment': {'description': 'Target environment; use sandbox first before production.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigureSellAnAsset().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
