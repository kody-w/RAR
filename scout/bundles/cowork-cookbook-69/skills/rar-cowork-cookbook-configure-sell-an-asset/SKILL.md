---
name: "rar-cowork-cookbook-configure-sell-an-asset"
description: "Runs a bulk sell-an-asset configuration change in Dynamics 365 F&SCM from an attached Excel file: validates every row, emits a validation workbook, waits for your approval, then applies changes with a before/after confir"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_sell_an_asset", "rar_sha256": "13aa440f13bfdf2277ac06cf906c429bf65b33407970802050fa552304f79591", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
