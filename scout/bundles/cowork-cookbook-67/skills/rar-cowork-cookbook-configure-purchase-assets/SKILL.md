---
name: "rar-cowork-cookbook-configure-purchase-assets"
description: "Applies bulk configuration changes to purchase assets in Dynamics 365 F&SCM from an attached Excel file: validates every row, returns a validation workbook, pauses for approval, then applies and returns a before/after co"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_purchase_assets", "rar_sha256": "62b1e411ab4edf3a093f883e1acaca25de3c54b5632879d077cb5d1953dd43f3", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
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
