---
name: "rar-cowork-cookbook-configure-purchase-assets"
description: "Applies bulk configuration changes to purchase assets in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies and returns a before/after co"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_purchase_assets", "rar_sha256": "62b1e411ab4edf3a093f883e1acaca25de3c54b5632879d077cb5d1953dd43f3", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/configure_purchase_assets`. The original RAPP
agent is preserved byte-for-byte in `configure_purchase_assets_agent.py` and in the RCI capsule.

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

Purchase assets Configuration Bulk Setup — Applies bulk configuration changes to purchase assets in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies and returns a before/after co

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-purchase-assets
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
      "description": "Attached Excel file with one row per purchase asset target and the new field values.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to run against (e.g. USMF); use a sandbox environment first.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_purchase_assets_agent.py` and embedded as the fenced Python below (sha256 62b1e411ab4edf3a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_purchase_assets_agent.py` first:

```bash
python3 configure_purchase_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_purchase_assets_agent.py   # or on stdin
python3 configure_purchase_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purchase assets Configuration Bulk Setup — Applies bulk configuration changes to purchase assets in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies and returns a before/after co

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
  Upstream entry : https://coworkcookbook.com/recipes/configure-purchase-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_purchase_assets',
    "version": '3.0.3',
    "display_name": 'Purchase assets Configuration Bulk Setup',
    "description": 'Applies bulk configuration changes to purchase assets in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies and returns a before/after co',
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
        "upstream_slug": 'configure-purchase-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-purchase-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'eae20dc699b5ae29',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/purchase-assets'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/configure-purchase-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'approval': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'configuration_excel_file': 'Attached Excel file with one row per purchase asset target and the new field values.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Eliminates the click-by-click burden of bulk configuration changes for purchase assets, cutting setup time from days to minutes while preserving auditability.', 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF (sandbox first!), read an attached configuration Excel file containing one row per purchase assets target with the new field values. Validate every row before applying anything (required fields present, valid references, no duplicates). Produce a 'validation' workbook showing which rows would succeed vs fail and why. Pause and ask me to approve before applying any changes. After approval, apply the validated changes and emit a confirmation workbook with before/after values. WARNING: this recipe modifies data - sandbox first.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads a configuration Excel file, validates each row, then applies updates via the D365 ERP plugin.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Applies bulk configuration changes to purchase assets in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies and returns a before/after co', 'example_request': 'Bulk update purchase assets in USMF sandbox from my attached config spreadsheet - validate first and wait for my approval.', 'inputs': [{'description': 'Attached Excel file with one row per purchase asset target and the new field values.', 'name': 'configuration_excel_file'}, {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'name': 'legal_entity'}, {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'name': 'approval'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when you need to bulk-update purchase asset field values in D365 F&SCM from a spreadsheet, with dry-run validation and approval before any data is written.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.', '**Before approving any write action, review the dry-run preview.**'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class ConfigurePurchaseAssets(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigurePurchaseAssets'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'approval': {'description': 'Explicit go-ahead after reviewing the validation workbook, before any changes are applied.', 'type': 'string'}, 'configuration_excel_file': {'description': 'Attached Excel file with one row per purchase asset target and the new field values.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to run against (e.g. USMF); use a sandbox environment first.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}},
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
    print(ConfigurePurchaseAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
